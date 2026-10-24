#!/usr/bin/env python3
"""Check discovery copy against GitHub and search-snippet limits.

Usage:
  python check_listing.py --about "text" --topics a,b,c [--title "..."] [--meta "..."]
  python check_listing.py --kit discovery-kit.md [--page site-page.md ...]

Checks (exit code 1 if any FAIL):
  About        <= 350 characters, one line, not empty
  Topics       <= 20, each matches [a-z0-9][a-z0-9-]* and <= 50 characters, no duplicates
  Title        warns above 70 characters
  Meta         warns above 155 characters, fails above 160

The limits for About and Topics are GitHub's repository settings limits. The title
and meta limits are conventions for search snippets. Re-check GitHub's current docs
if you rely on exact numbers.
"""
import argparse
import re
import sys

ABOUT_MAX = 350
TOPICS_MAX = 20
TOPIC_LEN_MAX = 50
TOPIC_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
TITLE_WARN = 70
META_WARN = 155
META_FAIL = 160

failures = 0


def report(level, label, message):
    global failures
    if level == "FAIL":
        failures += 1
    print(f"{level:5} {label}: {message}")


def check_about(text, label="About"):
    text = text.strip()
    if not text:
        report("FAIL", label, "empty")
        return
    if "\n" in text:
        report("FAIL", label, "contains a line break; use one paragraph")
    n = len(text)
    if n > ABOUT_MAX:
        report("FAIL", label, f"{n} characters, limit {ABOUT_MAX}")
    else:
        report("PASS", label, f"{n} characters (limit {ABOUT_MAX})")


def check_topics(topics, label="Topics"):
    topics = [t.strip() for t in topics if t.strip()]
    if not topics:
        report("FAIL", label, "none given")
        return
    if len(topics) > TOPICS_MAX:
        report("FAIL", label, f"{len(topics)} topics, limit {TOPICS_MAX}")
    seen = set()
    bad = []
    for t in topics:
        if t in seen:
            bad.append(f"{t} (duplicate)")
        seen.add(t)
        if not TOPIC_RE.match(t) or len(t) > TOPIC_LEN_MAX:
            bad.append(t)
    if bad:
        report("FAIL", label, "invalid or duplicate: " + ", ".join(bad))
    else:
        report("PASS", label, f"{len(topics)} topics, all valid (limit {TOPICS_MAX})")


def check_title(text, label="Title"):
    n = len(text)
    if n > TITLE_WARN:
        report("WARN", label, f"{n} characters, may be cut off in search results (about {TITLE_WARN})")
    else:
        report("PASS", label, f"{n} characters")


def check_meta(text, label="Meta description"):
    n = len(text)
    if n > META_FAIL:
        report("FAIL", label, f"{n} characters, keep under {META_FAIL}")
    elif n > META_WARN:
        report("WARN", label, f"{n} characters, close to the limit")
    else:
        report("PASS", label, f"{n} characters")


def check_kit(path):
    text = open(path, encoding="utf-8").read()
    abouts = re.findall(
        r"\*\*About[^\n]*:\*\*\s*\n\s*```[^\n]*\n(.*?)\n```", text, re.S
    )
    topic_lines = re.findall(r"\*\*Topics:\*\*[ \t]*([^\n]+)", text)
    if not abouts:
        report("FAIL", path, "no About block found (see references/listing.md, Kit format)")
    for i, a in enumerate(abouts, 1):
        check_about(a, f"About #{i}")
    if not topic_lines:
        report("FAIL", path, "no Topics line found (see references/listing.md, Kit format)")
    for i, line in enumerate(topic_lines, 1):
        check_topics(re.findall(r"`([^`]+)`", line), f"Topics #{i}")


def check_page(path):
    text = open(path, encoding="utf-8").read()
    title = re.search(r'^title:\s*"(.*)"\s*$', text, re.M)
    meta = re.search(r'^description:\s*"(.*)"\s*$', text, re.M)
    if title:
        check_title(title.group(1), f"{path} title")
    else:
        report("FAIL", path, 'no title: "..." line in frontmatter')
    if meta:
        check_meta(meta.group(1), f"{path} meta description")
    else:
        report("FAIL", path, 'no description: "..." line in frontmatter')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--about")
    ap.add_argument("--topics", help="comma-separated")
    ap.add_argument("--title")
    ap.add_argument("--meta")
    ap.add_argument("--kit", help="path to discovery-kit.md")
    ap.add_argument("--page", action="append", default=[], help="path to a site page; repeatable")
    args = ap.parse_args()

    if not any([args.about, args.topics, args.title, args.meta, args.kit, args.page]):
        ap.print_help()
        return 2

    if args.about:
        check_about(args.about)
    if args.topics:
        check_topics(args.topics.split(","))
    if args.title:
        check_title(args.title)
    if args.meta:
        check_meta(args.meta)
    if args.kit:
        check_kit(args.kit)
    for p in args.page:
        check_page(p)

    print("\nResult:", "FAIL" if failures else "OK")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
