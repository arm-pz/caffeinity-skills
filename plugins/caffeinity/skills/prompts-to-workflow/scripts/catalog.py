#!/usr/bin/env python3
"""Print the skillsmith catalog the split decision is made against.

Reads the live skill index (name + description for every published skill),
marks which skills are installed locally, and prints the brew table from
caffeinity-routing's references/workflows.md so a chain can be compared with
the workflows that already exist.

    python catalog.py                 # skills + brews, markdown
    python catalog.py --json          # same data as JSON
    python catalog.py --offline       # installed skills only, no network
    python catalog.py --path DIR      # extra folder to look for installed skills

Standard library only. Exit 0 on success; exit 2 if neither the site nor any
local skill folder could be read, because a split decided against nothing is
a guess.
"""
import argparse
import io
import json
import os
import re
import sys
import tarfile
import urllib.request
from pathlib import Path

SITE = "https://skillsmith.tech"
INDEX = SITE + "/.well-known/agent-skills/index.json"
ROUTING_ARCHIVE = SITE + "/agent-skills/caffeinity-routing.tar.gz"
SKILL_DIRS = [
    "~/.claude/skills", "~/.qoder/skills", "~/.cursor/skills", "~/.agents/skills",
    ".claude/skills", "~/.claude/plugins",
]


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "prompts-to-workflow/0.1"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    block, out = m.group(1), {}
    for key in ("name", "description"):
        km = re.search(rf"^{key}:\s*(.*?)(?=^\w[\w-]*:|\Z)", block, re.S | re.M)
        if km:
            val = km.group(1).strip()
            val = re.sub(r"^[>|]-?\s*", "", val)
            val = val.replace("\\n", " ")
            val = re.sub(r"\s+", " ", val).strip().strip("'\"")
            out[key] = val
    return out


def installed_skills(extra):
    found = {}
    for d in SKILL_DIRS + extra:
        root = Path(os.path.expanduser(d))
        if not root.is_dir():
            continue
        for p in root.rglob("SKILL.md"):
            try:
                fm = frontmatter(p.read_text(encoding="utf-8", errors="replace"))
            except OSError:
                continue
            name = fm.get("name") or p.parent.name
            found.setdefault(name, {"description": fm.get("description", ""), "path": str(p.parent)})
    return found


def brews_from_archive(blob):
    with tarfile.open(fileobj=io.BytesIO(blob), mode="r:gz") as tf:
        for m in tf.getmembers():
            if m.isfile() and m.name.endswith("references/workflows.md"):
                text = tf.extractfile(m).read().decode("utf-8", "replace")
                return parse_brews(text)
    return []


def brews_from_local(installed):
    info = installed.get("caffeinity-routing")
    if not info:
        return []
    p = Path(info["path"]) / "references" / "workflows.md"
    return parse_brews(p.read_text(encoding="utf-8")) if p.is_file() else []


def parse_brews(text):
    brews = []
    for sec in re.split(r"^## ", text, flags=re.M)[1:]:
        title = sec.splitlines()[0].strip()
        steps = []
        for line in sec.splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0].isdigit():
                skills = re.findall(r"`([a-z0-9-]+)`", cells[1])
                steps.append({"step": int(cells[0]), "skills": skills,
                              "optional": "optional" in cells[1]})
        if steps:
            brews.append({"brew": title, "steps": steps})
    return brews


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--path", action="append", default=[])
    a = ap.parse_args()

    installed = installed_skills(a.path)
    published, brews, notes = {}, [], []

    if not a.offline:
        try:
            idx = json.loads(fetch(INDEX))
            for s in idx.get("skills", []):
                published[s["name"]] = s.get("description", "")
        except Exception as e:  # network, proxy, JSON
            notes.append(f"live index unreachable ({e.__class__.__name__}); using installed skills only")
        try:
            brews = brews_from_archive(fetch(ROUTING_ARCHIVE))
        except Exception as e:
            notes.append(f"brew table unreachable ({e.__class__.__name__})")
    if not brews:
        brews = brews_from_local(installed)
        if brews:
            notes.append("brew table read from installed caffeinity-routing")

    names = sorted(set(published) | set(installed))
    if not names:
        print("No catalog: the site was unreachable and no installed skills were found.", file=sys.stderr)
        return 2
    rows = [{"name": n,
             "description": published.get(n) or installed.get(n, {}).get("description", ""),
             "published": n in published,
             "installed": n in installed} for n in names]

    if a.json:
        print(json.dumps({"skills": rows, "brews": brews, "notes": notes}, indent=1))
        return 0

    for n in notes:
        print(f"> note: {n}")
    print(f"\n## Skills ({len(rows)}; {sum(r['published'] for r in rows)} published, "
          f"{sum(r['installed'] for r in rows)} installed)\n")
    print("| Skill | Installed | Published | Description |\n| --- | --- | --- | --- |")
    for r in rows:
        d = r["description"].replace("|", "/")
        print(f"| `{r['name']}` | {'yes' if r['installed'] else 'no'} | "
              f"{'yes' if r['published'] else 'no'} | {d} |")
    print(f"\n## Brews ({len(brews)})\n")
    for b in brews:
        chain = " → ".join(" or ".join(s["skills"]) + (" (optional)" if s["optional"] else "")
                           for s in b["steps"])
        print(f"- **{b['brew']}**: {chain}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
