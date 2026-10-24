#!/usr/bin/env python3
"""Check drafted policy pages against the fact sheet they were written from.

    python check_pages.py --facts facts.md privacy.md terms.md refunds.md cookies.md

The page kind comes from the file name (privacy, terms, refund(s), cookie(s)) or --kind for a
single page. FAIL (exit 1): an unfilled placeholder, a required section missing, no "Last updated"
line, or an email address the fact sheet does not contain. WARN: a URL whose host is not in the
fact sheet, the owner's name never appearing, pages with different "Last updated" dates, and
fact-sheet entries still marked [NEEDS: ...] or (observed).
"""
import argparse
import re
import sys
from pathlib import Path

# Each required section is a set of alternative heading words; a heading matches if it contains any.
REQUIRED = {
    "privacy": [("who we are", "about us"), ("what we collect", "information we collect", "data we collect"),
                ("why we", "how we use", "purpose"), ("share", "third part", "processor"),
                ("how long", "retention", "keep"), ("your rights", "your choices"), ("contact",)],
    "terms": [("the service", "our service", "what we provide"), ("acceptable use", "rules", "prohibited"),
              ("termination", "closing", "suspension"), ("liability", "disclaimer"),
              ("governing law", "law and disputes", "disputes"), ("contact",)],
    "refunds": [("refund",), ("how to ask", "how to request", "requesting"), ("contact",)],
    "cookies": [("cookies we use", "cookies used", "list of cookies"), ("your choices", "manage", "opt out", "consent"),
                ("contact",)],
}
KINDS = {"privacy": "privacy", "terms": "terms", "tos": "terms", "refund": "refunds", "refunds": "refunds",
         "cookie": "cookies", "cookies": "cookies"}
PLACEHOLDER = re.compile(r"\[NEEDS:[^\]]*\]|\bTODO\b|\bTBD\b|lorem ipsum|\{\{[^}]*\}\}|\[(?:your|company|insert)[^\]]*\]"
                         r"|\bXXX+\b|\bexample\.(?:com|org)\b", re.I)
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
URL = re.compile(r"https?://([^/\s)>\]\"']+)", re.I)
UPDATED = re.compile(r"last updated:?\**\s*(.+)", re.I)
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$|^\s*\*\*(.+?)\*\*\s*$")
FACT = re.compile(r"^\s*[-*]?\s*([a-z_]+)\*?:\s*(.*)$")


def load_facts(path):
    text = Path(path).read_text(encoding="utf-8")
    facts = {}
    for line in text.splitlines():
        m = FACT.match(line)
        if m:
            facts[m.group(1)] = m.group(2).strip()
    return text, facts


def kind_of(path, forced):
    if forced:
        return forced
    stem = Path(path).stem.lower()
    for key, kind in KINDS.items():
        if key in re.split(r"[-_.\s]", stem) or stem.startswith(key):
            return kind
    return None


def check_page(path, kind, facts_text, facts):
    text = Path(path).read_text(encoding="utf-8")
    fails, warns = [], []
    for m in PLACEHOLDER.finditer(text):
        line = text.count("\n", 0, m.start()) + 1
        fails.append(f"line {line}: placeholder {m.group(0)!r}")
    headings = [(m.group(1) or m.group(2)).lower() for m in map(HEADING.match, text.splitlines()) if m]
    for alts in REQUIRED.get(kind, []):
        if not any(a in h for h in headings for a in alts):
            fails.append(f"missing section: {alts[0]!r} (any heading containing one of {', '.join(alts)})")
    updated = UPDATED.search(text)
    if not updated:
        fails.append("no 'Last updated: <date>' line")
    known = facts_text.lower()
    for email in sorted(set(EMAIL.findall(text))):
        if email.lower() not in known:
            fails.append(f"email {email} is not in the fact sheet (invented, or the sheet is incomplete)")
    for host in sorted(set(h.lower() for h in URL.findall(text))):
        bare = host[4:] if host.startswith("www.") else host
        if bare not in known:
            warns.append(f"link to {host} is not in the fact sheet; confirm it is a real processor or page")
    names = [facts.get(k, "") for k in ("legal_name", "trading_name", "product_name")]
    names = [n for n in names if n and not n.startswith("[NEEDS") and ":" not in n]
    if names and not any(n.lower() in text.lower() for n in names):
        warns.append(f"none of {', '.join(names)} appears; the page does not say who it is from")
    return fails, warns, (updated.group(1).strip().strip("*").strip() if updated else None)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--facts", required=True)
    ap.add_argument("--kind", choices=sorted(REQUIRED), help="page kind when there is one page with an unusual name")
    ap.add_argument("pages", nargs="+")
    a = ap.parse_args(argv)
    if a.kind and len(a.pages) > 1:
        ap.error("--kind applies to a single page")
    facts_text, facts = load_facts(a.facts)
    total_fail, dates = 0, {}
    for key, value in facts.items():
        if value.startswith("[NEEDS") or "(observed)" in value:
            print(f"WARN  facts: {key} is {value!r}; the owner has not confirmed it")
    for page in a.pages:
        kind = kind_of(page, a.kind)
        if kind is None:
            print(f"FAIL  {page}: cannot tell the page kind from its name; pass --kind")
            total_fail += 1
            continue
        fails, warns, date = check_page(page, kind, facts_text, facts)
        if date:
            dates[page] = date
        for f in fails:
            print(f"FAIL  {page} ({kind}): {f}")
        for w in warns:
            print(f"WARN  {page} ({kind}): {w}")
        if not fails and not warns:
            print(f"PASS  {page} ({kind})")
        total_fail += len(fails)
    if len(set(dates.values())) > 1:
        print("WARN  pages carry different 'Last updated' dates: "
              + "; ".join(f"{Path(p).name} {d}" for p, d in dates.items()))
    print(f"\n{total_fail} FAIL" if total_fail else "\nall pages pass")
    return 1 if total_fail else 0


if __name__ == "__main__":
    sys.exit(main())
