#!/usr/bin/env python3
"""List the catalog's skills and which one tune-and-ship should take next.

    python queue.py                          # every skill, with HEAD and bundled commits
    python queue.py --ledger ledger.md       # also mark the ones already shipped
    python queue.py --next --ledger ledger.md   # print only the next skill's name
    python queue.py --manifest skills.json --sources SOURCES.md --offline   # local files, no git

The manifest is the site's skills.json (mods and legacy archives are skipped). SOURCES.md is the
marketplace bundle's record of the commit it copied for each skill. A ledger is a markdown table
whose first column is a skill name; any skill named there counts as done unless its row says
"queued". HEAD comes from `git ls-remote`, so no token is needed for public repos.
"""
import argparse
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

MANIFEST = "https://raw.githubusercontent.com/arm-pz/skills-site/main/site/skills.json"
SOURCES = "https://raw.githubusercontent.com/arm-pz/caffeinity-skills/main/plugins/caffeinity/SOURCES.md"
ROW = re.compile(r"^\|\s*`?([a-z0-9][a-z0-9-]*)`?\s*\|(.*)$")
NAME = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")


def read(src):
    if re.match(r"https?://", src):
        with urllib.request.urlopen(src, timeout=30) as r:
            return r.read().decode("utf-8")
    return Path(src).read_text(encoding="utf-8")


def bundled(text):
    """{skill: short commit} from SOURCES.md; in-repo skills have no commit of their own."""
    out = {}
    for line in text.splitlines():
        m = ROW.match(line)
        if not m:
            continue
        c = re.search(r"`([0-9a-f]{7,40})`\s*\|?\s*$", line)
        out[m.group(1)] = c.group(1)[:7] if c else None
    return out


def ledger(path):
    """({done}, {queued}) from a ledger table. A missing ledger is an empty one."""
    done, queued = set(), set()
    if not path or not Path(path).exists():
        return done, queued
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if not m or m.group(1) in ("skill", "name"):
            continue
        (queued if "queued" in m.group(2).lower() else done).add(m.group(1))
    return done - queued, queued


def head(repo):
    if not NAME.fullmatch(repo):
        return None
    try:
        r = subprocess.run(["git", "ls-remote", f"https://github.com/{repo}", "HEAD"],
                           capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return r.stdout.split()[0][:7] if r.returncode == 0 and r.stdout.strip() else None


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--manifest", default=MANIFEST)
    ap.add_argument("--sources", default=SOURCES)
    ap.add_argument("--ledger")
    ap.add_argument("--offline", action="store_true", help="skip git ls-remote")
    ap.add_argument("--next", action="store_true", help="print only the next skill's name")
    a = ap.parse_args()

    try:
        skills = json.loads(read(a.manifest))["skills"]
        pinned = bundled(read(a.sources))
    except (OSError, ValueError, KeyError) as e:
        sys.exit(f"queue: cannot read the catalog: {e}")
    done, queued = ledger(a.ledger)

    rows = []
    for s in skills:
        if s.get("kind") == "mod" or s.get("legacy"):
            continue
        name, repo = s["name"], s.get("repo", "")
        own_repo = name in pinned and pinned[name] is not None
        h = None if a.offline or not own_repo else head(repo)
        b = pinned.get(name)
        if name in queued:
            state = "queued"
        elif name in done:
            state = "done"
        else:
            state = "todo"
        if not own_repo:
            bundle = "in-repo"
        elif h is None:
            bundle = "unknown"
        else:
            bundle = "current" if h == b else "stale"
        rows.append((name, repo, s.get("path", "."), h or "-", b or "-", bundle, state))

    # Queued siblings first (someone already found a reason), then untouched ones, in catalog order.
    order = [r for r in rows if r[6] == "queued"] + [r for r in rows if r[6] == "todo"]
    if a.next:
        if not order:
            sys.exit("queue: every skill in the catalog is done")
        print(order[0][0])
        return
    print("| skill | repo | path | head | bundled | bundle | state |")
    print("| --- | --- | --- | --- | --- | --- | --- |")
    for r in rows:
        print("| " + " | ".join(r) + " |")
    n = {k: sum(1 for r in rows if r[6] == k) for k in ("todo", "queued", "done")}
    print(f"\n{len(rows)} skills: {n['todo']} todo, {n['queued']} queued, {n['done']} done."
          + (f" Next: {order[0][0]}" if order else " Nothing left."))


if __name__ == "__main__":
    main()
