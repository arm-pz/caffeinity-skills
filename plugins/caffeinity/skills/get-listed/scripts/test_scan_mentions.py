#!/usr/bin/env python3
"""Self-check for scan_mentions.py. Run: python -I test_scan_mentions.py"""
import csv
import io
import os
import sys
import tempfile
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scan_mentions  # noqa: E402

GAP = """<!-- url: https://blog.example.com/best-crm -->
# 7 best CRM tools
1. [Rival](https://rival.io/?ref=list) is great.
2. [Other Co](https://www.other.co) works too.
Share on [X](https://x.com/intent) or read [our guide](https://blog.example.com/guide).
"""
HAS_YOU = """<!-- url: https://news.example.org/crm -->
Rival, Other Co and Acme all made the cut.
"""
NONE = """<!-- url: https://site.example.net/x -->
Nothing about rivalry here, and no othercompany either.
"""


def run(pages, links_out):
    buf = io.StringIO()
    with redirect_stdout(buf):
        scan_mentions.main(["--you", "Acme|acme.com", "--competitor", "Rival|rival.io",
                            "--competitor", "Other Co|other.co", "--links-out", links_out, *pages])
    return list(csv.DictReader(io.StringIO(buf.getvalue())))


def main():
    with tempfile.TemporaryDirectory() as d:
        paths = []
        for name, body in (("gap", GAP), ("has-you", HAS_YOU), ("none", NONE)):
            p = os.path.join(d, name + ".md")
            with open(p, "w", encoding="utf-8") as f:
                f.write(body)
            paths.append(p)
        links = os.path.join(d, "tools.csv")
        rows = {r["slug"]: r for r in run(paths, links)}
        assert rows["gap"]["qualifies"] == "yes", rows["gap"]
        assert rows["gap"]["competitor_count"] == "2", rows["gap"]
        assert rows["gap"]["url"] == "https://blog.example.com/best-crm"
        assert rows["has-you"]["you_named"] == "yes" and rows["has-you"]["qualifies"] == "no"
        # "rivalry" and "othercompany" must not count as mentions
        assert rows["none"]["competitor_count"] == "0", rows["none"]
        with open(links, encoding="utf-8") as f:
            tools = list(csv.DictReader(f))
        names = sorted(t["tool_name"] for t in tools)
        assert names == ["Other Co", "Rival"], names  # own-site and social links filtered
    print("scan_mentions: 6 checks passed")


if __name__ == "__main__":
    main()
