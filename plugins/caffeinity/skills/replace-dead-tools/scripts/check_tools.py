#!/usr/bin/env python3
"""First-pass liveness check for the tools named on list articles.

Usage:
  python check_tools.py outreach/list-tools.csv > outreach/dead-tools.draft.csv
  python check_tools.py --url https://example.com [--url ...]
  python check_tools.py --html saved.html --url https://example.com   # offline, for tests
  python check_tools.py --github search outreach/list-tools.csv       # restricted sandboxes

Reads tool_url (and tool_name, list_slug when present) from the CSV, checks each unique URL once
and prints:
  tool_name,tool_url,verdict,final_url,status,signals,evidence_url,checked_on,list_slugs

The verdict is a suggestion that the agent confirms by hand:
  DEAD          the host does not resolve, refuses connections, or shows a parked or for-sale page
  ACQUIRED      the request ends on a different registrable domain with a different name, or the
                page says it was acquired (a confirmed rebrand of the same company is ALIVE)
  SUNSETTING    the page announces a shutdown, sunset or end of life
  ALIVE         a 2xx page with none of the above
  INCONCLUSIVE  blocked (401/403/429), a timeout, a proxy refusal or a 5xx: the check did not
                really run, so it is never treated as a pass or a fail
A 404 or 410 on the exact listed URL is reported as signal http-404 / http-410 with
verdict INCONCLUSIVE, because a moved page is not a dead product; the agent checks the homepage.
STALE is never suggested here: it needs dated evidence a single fetch cannot give.

GitHub repos (github.com/<owner>/<repo>/...) are checked at the repo level, not by fetching the
page, because github.com HTML is rate-limited and often blocked. Deep links to the same repo
collapse into one check.
  --github api      (default) `gh api repos/<o>/<r>`, or the unauthenticated REST API if gh is
                    missing. 404 means deleted or private (renamed repos redirect), so DEAD.
  --github search   GitHub search with several repo: qualifiers per call, for environments where
                    only the search API is allowed. A repo missing from search stays INCONCLUSIVE.
  --github off      treat GitHub URLs like any other page.
archived -> DEAD (signal github:archived). A last push over 365 days ago adds the signal
github:last-push:<date> but keeps ALIVE: one date is not STALE.
"""
import argparse
import csv
import datetime as dt
import json
import re
import shutil
import subprocess
import socket
import ssl
import sys
import urllib.error
import urllib.request
from urllib.parse import urlparse

UA = "Mozilla/5.0 (compatible; replace-dead-tools/1.0; liveness check)"
TIMEOUT = 15
MAX_BYTES = 400_000

PARKED = [
    r"this domain (?:is|may be) for sale", r"buy this domain", r"domain (?:is )?parked",
    r"parked (?:free|domain)", r"hugedomains", r"sedo(?:parking)?\.com", r"dan\.com",
    r"afternic", r"godaddy\.com/domainsearch", r"the domain .{0,40} is available",
    r"domain has expired", r"this site can.t be reached",
]
SUNSET = [
    r"(?:is|are|will be) shutting down", r"(?:has|have) shut down", r"we.re shutting down",
    # "retired" alone is not here: UI strings like "the saved version is retired" matched it
    # on a live product (seen on the skillsmith.tech run). Only dated retirement counts.
    r"(?:is|has been|will be) (?:sunset|sunsetted|discontinued)", r"will be retired on",
    r"end[- ]of[- ]life", r"no longer (?:available|supported|accepting (?:new )?sign ?ups)",
    r"ceased operations", r"final day of service", r"service (?:will|has) (?:end|ended)",
]
# Case-sensitive on purpose: the company name after the phrase must be capitalised, so
# "data acquired by sensors" does not count. The leading words are case-insensitive.
ACQ = [
    r"(?i:has|have) been acquired by [A-Z]", r"(?i:is|are) now (?i:a )?part of [A-Z]",
    r"(?i:has|have) joined forces with [A-Z]", r"(?i:acquired) by [A-Z][\w.]+",
]
TWO_LEVEL = {"co.uk", "com.au", "co.nz", "co.jp", "com.br", "co.in", "co.za", "com.mx", "com.sg", "org.uk"}


def reg_domain(url):
    h = (urlparse(url).hostname or "").lower().rstrip(".")
    parts = h.split(".")
    if len(parts) >= 3 and ".".join(parts[-2:]) in TWO_LEVEL:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


def scan_text(html):
    text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    found = []
    for label, pats, flags in (("parked", PARKED, re.I), ("sunset", SUNSET, re.I), ("acquired", ACQ, 0)):
        for p in pats:
            m = re.search(p, text, flags)
            if m:
                found.append(f"{label}:{m.group(0)[:60]}")
                break
    return found


def verdict_from(start_url, final_url, status, err, signals):
    sig = list(signals)
    if err:
        kind, detail = err
        sig.append(f"{kind}:{detail}"[:80])
        if kind in ("dns", "refused"):
            return "DEAD", sig
        return "INCONCLUSIVE", sig
    if final_url and reg_domain(final_url) != reg_domain(start_url):
        a, b = reg_domain(start_url), reg_domain(final_url)
        if a.split(".")[0] == b.split(".")[0]:
            # notion.so -> notion.com: the same brand on another TLD is a domain move.
            sig.append(f"domain-move:{a}->{b}")
        else:
            sig.append(f"redirect:{a}->{b}")
    if status in (404, 410):
        sig.append(f"http-{status}")
        return "INCONCLUSIVE", sig
    if status and (status in (401, 403, 429) or status >= 500):
        sig.append(f"http-{status}")
        return "INCONCLUSIVE", sig
    if any(s.startswith("parked:") for s in sig):
        return "DEAD", sig
    if any(s.startswith("sunset:") for s in sig):
        return "SUNSETTING", sig
    if any(s.startswith(("acquired:", "redirect:")) for s in sig):
        return "ACQUIRED", sig
    if status and 200 <= status < 300:
        return "ALIVE", sig
    return "INCONCLUSIVE", sig


def classify_error(e):
    reason = getattr(e, "reason", e)
    s = str(reason)
    if isinstance(reason, socket.gaierror) or "Name or service not known" in s or "nodename nor servname" in s:
        return ("dns", "host does not resolve")
    if isinstance(reason, ConnectionRefusedError) or "Connection refused" in s:
        return ("refused", "connection refused")
    if isinstance(reason, (socket.timeout, TimeoutError)) or "timed out" in s:
        return ("timeout", "timed out")
    if isinstance(reason, ssl.SSLError) or "CERTIFICATE" in s.upper():
        return ("tls", s[:50])
    if "proxy" in s.lower() or "Tunnel connection failed" in s:
        # A proxy that refuses or cannot resolve the host is not evidence about the host.
        return ("proxy", s[:50])
    return ("error", s[:50])


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read(MAX_BYTES).decode("utf-8", errors="replace")
            return r.geturl(), r.status, body, None
    except urllib.error.HTTPError as e:
        try:
            body = e.read(MAX_BYTES).decode("utf-8", errors="replace")
        except Exception:
            body = ""
        return e.geturl() or url, e.code, body, None
    except Exception as e:  # URLError, socket errors, timeouts
        return url, None, "", classify_error(e)


def check(url, html=None):
    if html is not None:
        final, status, body, err = url, 200, html, None
    else:
        final, status, body, err = fetch(url)
    signals = scan_text(body) if body else []
    verdict, signals = verdict_from(url, final, status, err, signals)
    return {"verdict": verdict, "final_url": final, "status": status or "", "signals": "; ".join(signals)}

GH_RESERVED = {"topics", "orgs", "sponsors", "features", "marketplace", "apps", "settings",
               "login", "about", "collections", "trending", "search", "enterprise", "pricing"}


def github_repo(url):
    """Return 'owner/repo' (lowercased) for a github.com repo URL, else None."""
    m = re.match(r"https?://(?:www\.)?github\.com/([^/#?]+)/([^/#?]+)", url or "")
    if not m or m.group(1).lower() in GH_RESERVED:
        return None
    return f"{m.group(1)}/{m.group(2).removesuffix('.git')}".lower()


def _gh(args):
    r = subprocess.run(["gh", "api", *args], capture_output=True, text=True, timeout=60)
    return r.returncode, r.stdout, r.stderr


def github_verdict(repo, info, today=None):
    """info: dict from the API (or None when not found). Returns (verdict, signals, final_url)."""
    today = today or dt.date.today()
    url = f"https://github.com/{repo}"
    if info is None:
        return "DEAD", ["github:not-found (deleted or private)"], url
    sig = []
    final = info.get("html_url") or url
    if (info.get("full_name") or repo).lower() != repo:
        sig.append(f"github:renamed-to:{info['full_name']}")
    pushed = (info.get("pushed_at") or "")[:10]
    if pushed:
        try:
            if (today - dt.date.fromisoformat(pushed)).days > 365:
                sig.append(f"github:last-push:{pushed}")
        except ValueError:
            pass
    if info.get("archived"):
        return "DEAD", ["github:archived"] + sig, final
    return "ALIVE", sig, final


def github_check_api(repos, runner=None):
    out = {}
    use_gh = runner is not None or shutil.which("gh")
    for repo in repos:
        if use_gh:
            code, so, se = (runner or _gh)([f"repos/{repo}"])
            if code == 0:
                out[repo] = github_verdict(repo, json.loads(so))
            elif "404" in se or "Not Found" in se:
                out[repo] = github_verdict(repo, None)
            else:
                out[repo] = ("INCONCLUSIVE", [f"github-api:{se.strip()[:50]}"], f"https://github.com/{repo}")
            continue
        final, status, body, err = fetch(f"https://api.github.com/repos/{repo}")
        if status == 200:
            out[repo] = github_verdict(repo, json.loads(body))
        elif status == 404:
            out[repo] = github_verdict(repo, None)
        else:
            why = f"{err[0]}:{err[1]}" if err else f"http-{status}"
            out[repo] = ("INCONCLUSIVE", [f"github-api:{why}"[:60]], f"https://github.com/{repo}")
    return out


def github_check_search(repos, runner=None, batch=6):
    out = {}
    repos = list(repos)
    for i in range(0, len(repos), batch):
        chunk = repos[i:i + batch]
        q = " ".join(f"repo:{r}" for r in chunk) + " fork:true"
        code, so, se = (runner or _gh)(["-X", "GET", "search/repositories", "-f", f"q={q}", "-f", "per_page=100"])
        if code != 0:
            for r in chunk:
                out[r] = ("INCONCLUSIVE", [f"github-search:{se.strip()[:50]}"], f"https://github.com/{r}")
            continue
        found = {it["full_name"].lower(): it for it in json.loads(so).get("items", [])}
        for r in chunk:
            if r in found:
                out[r] = github_verdict(r, found[r])
            else:
                # Missing from search: deleted, private, renamed, or a search miss. Not proof.
                out[r] = ("INCONCLUSIVE", ["github-search:not-found"], f"https://github.com/{r}")
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", nargs="?", help="list-tools.csv")
    ap.add_argument("--url", action="append", default=[])
    ap.add_argument("--html", help="check this saved HTML instead of fetching (single --url)")
    ap.add_argument("--github", choices=["api", "search", "off"], default="api",
                    help="how to check github.com repo URLs (default: api)")
    a = ap.parse_args(argv)

    tools = {}
    if a.csv:
        with open(a.csv, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                u = (row.get("tool_url") or "").strip()
                if not u:
                    continue
                t = tools.setdefault(u, {"name": row.get("tool_name", ""), "slugs": set()})
                if row.get("list_slug"):
                    t["slugs"].add(row["list_slug"])
    for u in a.url:
        tools.setdefault(u, {"name": "", "slugs": set()})
    if not tools:
        ap.error("give a CSV with a tool_url column or at least one --url")

    html = None
    if a.html:
        with open(a.html, encoding="utf-8", errors="replace") as f:
            html = f.read()

    # Collapse GitHub deep links into one row per repo.
    if a.github != "off" and html is None:
        merged = {}
        for u, t in tools.items():
            repo = github_repo(u)
            key = f"https://github.com/{repo}" if repo else u
            m = merged.setdefault(key, {"name": t["name"], "slugs": set()})
            m["slugs"] |= t["slugs"]
            m["name"] = m["name"] or t["name"]
        tools = merged
        repos = [github_repo(u) for u in tools if github_repo(u)]
        gh = (github_check_search if a.github == "search" else github_check_api)(repos)
    else:
        gh = {}

    today = dt.date.today().isoformat()
    w = csv.writer(sys.stdout)
    w.writerow(["tool_name", "tool_url", "verdict", "final_url", "status", "signals", "evidence_url", "checked_on", "list_slugs"])
    for u, t in tools.items():
        repo = github_repo(u) if gh else None
        if repo in gh:
            v, sig, final = gh[repo]
            r = {"verdict": v, "final_url": final, "status": "", "signals": "; ".join(sig)}
        else:
            r = check(u, html)
        evidence = r["final_url"] if r["verdict"] in ("DEAD", "ACQUIRED", "SUNSETTING") else ""
        w.writerow([t["name"], u, r["verdict"], r["final_url"], r["status"], r["signals"], evidence, today, "; ".join(sorted(t["slugs"]))])
    return 0


if __name__ == "__main__":
    sys.exit(main())
