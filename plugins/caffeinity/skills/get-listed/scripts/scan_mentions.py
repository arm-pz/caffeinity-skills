#!/usr/bin/env python3
"""Decide which fetched list articles name competitors but not you, and pull their tool links.

Usage:
  python scan_mentions.py --you "Acme|acme.com" \
      --competitor "Rival|rival.io" --competitor "Other Co|other.co" \
      [--links-out outreach/list-tools.csv] outreach/pages/*.md

Each page file is the markdown text of one article. Its first line may be
`<!-- url: https://... -->` so the output can carry the article URL.

A brand matches on any of its |-separated aliases, case-insensitively, at word boundaries.
A domain alias also matches inside URLs. Prints one CSV row per page to stdout:
  slug,url,you_named,competitors_named,competitor_count,qualifies
qualifies = yes when at least one competitor is named and you are not.

With --links-out, writes the external markdown links of every qualifying page
(list_slug,list_url,tool_name,tool_url), excluding the article's own site, your domains and
common share/social/tracking hosts. The agent prunes the rest by hand: navigation and
citation links survive this filter.
"""
import argparse
import csv
import os
import re
import sys
from urllib.parse import urlparse

SKIP_HOSTS = {
    "twitter.com", "x.com", "facebook.com", "linkedin.com", "instagram.com",
    "youtube.com", "youtu.be", "pinterest.com", "reddit.com", "t.co", "bit.ly",
    "wa.me", "whatsapp.com", "telegram.me", "t.me", "google.com", "goo.gl",
    "doubleclick.net", "amazon-adsystem.com", "gravatar.com", "wordpress.org",
    "creativecommons.org", "w3.org", "schema.org",
    # badge and list-meta hosts: never a product entry (seen on GitHub awesome-lists)
    "shields.io", "badgen.net", "badge.fury.io", "awesome.re", "githubusercontent.com",
}
LINK_RE = re.compile(r"\[([^\]]{1,120})\]\((https?://[^)\s]+)\)")
URL_LINE_RE = re.compile(r"^<!--\s*url:\s*(\S+)\s*-->")


def parse_brand(spec):
    parts = [p.strip() for p in spec.split("|") if p.strip()]
    if not parts:
        raise SystemExit(f"empty brand spec: {spec!r}")
    return parts[0], parts


def host_of(url):
    h = (urlparse(url).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def alias_pattern(alias):
    # Word-ish boundaries that also work for names with dots or spaces.
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(alias.lower()) + r"(?![A-Za-z0-9])")


def named(text_lower, aliases):
    return any(alias_pattern(a).search(text_lower) for a in aliases)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--you", required=True, help='"Name|alias|domain.com"')
    ap.add_argument("--competitor", action="append", required=True, help='"Name|alias|domain.com" (repeat)')
    ap.add_argument("--links-out", help="write list-tools.csv rows for qualifying pages here")
    ap.add_argument("pages", nargs="+")
    a = ap.parse_args(argv)

    _, you_aliases = parse_brand(a.you)
    comps = [parse_brand(c) for c in a.competitor]
    you_hosts = {x.lower().removeprefix("www.") for x in you_aliases if "." in x and " " not in x}

    out = csv.writer(sys.stdout)
    out.writerow(["slug", "url", "you_named", "competitors_named", "competitor_count", "qualifies"])
    link_rows = []
    for path in a.pages:
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read()
        first = text.splitlines()[0] if text else ""
        m = URL_LINE_RE.match(first)
        url = m.group(1) if m else ""
        slug = os.path.splitext(os.path.basename(path))[0]
        low = text.lower()
        you = named(low, you_aliases)
        hits = [name for name, aliases in comps if named(low, aliases)]
        qualifies = bool(hits) and not you
        out.writerow([slug, url, "yes" if you else "no", "; ".join(hits), len(hits), "yes" if qualifies else "no"])
        if qualifies and a.links_out:
            own = host_of(url)
            seen = set()
            for name, link in LINK_RE.findall(text):
                h = host_of(link)
                if not h or h == own or h.endswith("." + own) or h in you_hosts:
                    continue
                if h in SKIP_HOSTS or any(h.endswith("." + s) for s in SKIP_HOSTS):
                    continue
                key = (h, name.strip().lower())
                if key in seen:
                    continue
                seen.add(key)
                link_rows.append([slug, url, name.strip(), link])

    if a.links_out:
        with open(a.links_out, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["list_slug", "list_url", "tool_name", "tool_url"])
            w.writerows(link_rows)
        print(f"# wrote {len(link_rows)} candidate tool links to {a.links_out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
