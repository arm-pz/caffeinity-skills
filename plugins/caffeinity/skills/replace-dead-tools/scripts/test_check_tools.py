#!/usr/bin/env python3
"""Offline self-check for check_tools.py. Run: python -I test_check_tools.py"""
import os
import socket
import sys
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_tools as ct  # noqa: E402

CASES = [
    # (description, html, expected verdict, expected signal prefix or None)
    ("parked page", "<h1>This domain is for sale!</h1><p>Buy this domain at HugeDomains</p>", "DEAD", "parked:"),
    ("shutdown notice", "<p>After 8 years, Widgetly is shutting down on March 1.</p>", "SUNSETTING", "sunset:"),
    ("acquisition notice", "<p>Widgetly has been acquired by Bigcorp and joins its suite.</p>", "ACQUIRED", "acquired:"),
    ("lowercase acquired is not a company", "<p>All data acquired by sensors is encrypted.</p>", "ALIVE", None),
    ("ordinary product page", "<h1>Widgetly</h1><p>Plans from $9. Start free.</p><script>var x='shutting down'</script>", "ALIVE", None),
]


def main():
    n = 0
    for desc, html, want, sig in CASES:
        r = ct.check("https://widgetly.io/", html=html)
        assert r["verdict"] == want, (desc, r)
        if sig:
            assert sig in r["signals"], (desc, r)
        n += 1

    # Cross-domain redirect is ACQUIRED; same registrable domain is not.
    v, s = ct.verdict_from("https://widgetly.io/", "https://bigcorp.com/widgetly", 200, None, [])
    assert v == "ACQUIRED" and any(x.startswith("redirect:") for x in s), (v, s)
    v, _ = ct.verdict_from("https://widgetly.io/", "https://www.widgetly.io/home", 200, None, [])
    assert v == "ALIVE", v
    v, _ = ct.verdict_from("https://a.co.uk/", "https://b.a.co.uk/", 200, None, [])
    assert v == "ALIVE", v
    # Same brand, new TLD (seen live: notion.so -> notion.com, modem.dev -> modem.ai).
    v, s = ct.verdict_from("https://www.notion.so/x", "https://www.notion.com/x", 200, None, [])
    assert v == "ALIVE" and s == ["domain-move:notion.so->notion.com"], (v, s)
    # A UI string with "is retired" is not a shutdown (seen live on a sponsor link).
    r = ct.check("https://x.io/", html='<div>"legacyVersion":"The saved version is retired. V6 is selected"</div>')
    assert r["verdict"] == "ALIVE", r
    r = ct.check("https://x.io/", html="<p>Widgetly will be retired on 1 March 2027.</p>")
    assert r["verdict"] == "SUNSETTING", r
    n += 6

    # Errors: DNS and refused are DEAD; blocked, timeout and proxy are INCONCLUSIVE, never a pass.
    dns = ct.classify_error(urllib.error.URLError(socket.gaierror(-2, "Name or service not known")))
    assert ct.verdict_from("https://x.io/", "", None, dns, [])[0] == "DEAD"
    proxy = ct.classify_error(urllib.error.URLError(OSError("Tunnel connection failed: 403 Forbidden")))
    assert proxy[0] == "proxy" and ct.verdict_from("https://x.io/", "", None, proxy, [])[0] == "INCONCLUSIVE"
    for code in (403, 429, 503, 404):
        assert ct.verdict_from("https://x.io/", "https://x.io/", code, None, [])[0] == "INCONCLUSIVE", code
    n += 6

    # GitHub: URL parsing, verdicts, and both modes with a fake gh runner (no network).
    import datetime as dt, json
    assert ct.github_repo("https://github.com/Obra/Superpowers/tree/main/skills/x") == "obra/superpowers"
    assert ct.github_repo("https://github.com/topics/claude") is None
    assert ct.github_repo("https://gist.github.com/a/b") is None
    today = dt.date(2026, 11, 17)
    assert ct.github_verdict("a/b", {"archived": True, "pushed_at": "2024-01-02T00:00:00Z"}, today)[0] == "DEAD"
    v, sig, _ = ct.github_verdict("a/b", {"full_name": "a/b", "pushed_at": "2025-01-01T00:00:00Z"}, today)
    assert v == "ALIVE" and "github:last-push:2025-01-01" in sig, sig
    v, sig, _ = ct.github_verdict("a/b", {"full_name": "a/c", "pushed_at": "2026-11-01T00:00:00Z"}, today)
    assert v == "ALIVE" and sig == ["github:renamed-to:a/c"], sig
    assert ct.github_verdict("a/b", None)[0] == "DEAD"
    n += 7

    def fake_api(args):
        repo = args[0].split("/", 1)[1]
        if repo == "gone/repo":
            return 1, "", "gh: Not Found (HTTP 404)"
        if repo == "rate/limited":
            return 1, "", "gh: API rate limit exceeded (HTTP 403)"
        return 0, json.dumps({"full_name": repo, "archived": repo == "old/repo", "pushed_at": "2026-10-01T00:00:00Z"}), ""
    r = ct.github_check_api(["ok/repo", "old/repo", "gone/repo", "rate/limited"], runner=fake_api)
    assert [r[k][0] for k in ("ok/repo", "old/repo", "gone/repo", "rate/limited")] == ["ALIVE", "DEAD", "DEAD", "INCONCLUSIVE"], r

    calls = []
    def fake_search(args):
        calls.append(args)
        q = [x for x in args if x.startswith("q=")][0]
        items = [{"full_name": t[5:], "archived": False, "pushed_at": "2026-10-01T00:00:00Z"}
                 for t in q[2:].split() if t.startswith("repo:") and t != "repo:missing/one"]
        return 0, json.dumps({"items": items}), ""
    repos = [f"o/r{i}" for i in range(7)] + ["missing/one"]
    r = ct.github_check_search(repos, runner=fake_search, batch=6)
    assert len(calls) == 2, calls  # 8 repos in batches of 6
    assert r["missing/one"][0] == "INCONCLUSIVE" and r["o/r6"][0] == "ALIVE", r
    n += 3
    print(f"check_tools: {n} checks passed")


if __name__ == "__main__":
    main()
