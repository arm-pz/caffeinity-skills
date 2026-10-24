#!/usr/bin/env python3
"""Show which skills a caffeinity brew (workflow) needs and which of them are installed.

Usage:
  python route_check.py espresso           # one brew, by name ("cold-brew"), number ("4") or old id ("W4")
  python route_check.py --all              # every brew
  python route_check.py cold-brew --path DIR   # also search DIR for installed skills
  python route_check.py --all --json       # for another agent to read

Reads the brew tables in ../references/workflows.md, so that file stays the only list.
Exit code 1 when a required step has no installed skill, 2 on bad usage.
"""
import argparse
import json
import re
import sys
from pathlib import Path

WORKFLOWS = Path(__file__).resolve().parent.parent / "references" / "workflows.md"
HOME = Path.home()
SEARCH = [HOME / ".claude" / "skills", HOME / ".qoder" / "skills", HOME / ".cursor" / "skills",
          HOME / ".agents" / "skills", HOME / ".codex" / "skills", HOME / ".claude" / "plugins",
          Path.cwd() / ".claude" / "skills", Path.cwd() / ".agents" / "skills"]


HEADING = re.compile(r"^## Brew (\d+) · ([^:]+): (.+)$")


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def load(path=WORKFLOWS):
    """Return {"espresso": {"number", "name", "title", "steps": [{"step", "skills", "optional"}]}}
    in file order. Brews used to be called W1 to W11; resolve() still accepts those ids."""
    flows, current = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        head = HEADING.match(line)
        if head:
            current = flows.setdefault(slug(head.group(2)), {
                "number": int(head.group(1)), "name": head.group(2).strip(),
                "title": head.group(3).strip(), "steps": []})
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if current is None or len(cells) < 2 or not cells[0].isdigit():
            continue
        names = re.findall(r"`([a-z0-9-]+)`", cells[1])
        if names:
            current["steps"].append({"step": int(cells[0]), "skills": names,
                                     "optional": "(optional)" in cells[1]})
    return flows


def resolve(flows, ref):
    """The brew key for a name ("Cold brew", "cold-brew"), a number ("4", "brew 4") or an old id ("W4")."""
    ref = ref.strip().lower()
    m = re.fullmatch(r"(?:w|brew[ -]?)?(\d+)", ref)
    for key, f in flows.items():
        if key == slug(ref) or (m and f["number"] == int(m.group(1))):
            return key
    return None


def label(flow):
    return f"Brew {flow['number']} · {flow['name']}"


# Skills that live in arm-pz/caffeinity-skills rather than a repo of their own.
IN_MARKETPLACE = {"caffeinity-routing", "paper-trail", "course-builder", "skill-estate"}


def install(name):
    if name in IN_MARKETPLACE:
        return f"npx skills add arm-pz/caffeinity-skills --skill {name}"
    return f"npx skills add arm-pz/{name}"


def installed(extra=()):
    """Names of every SKILL.md found under the search roots, by frontmatter name or folder."""
    found = {}
    for root in [*SEARCH, *map(Path, extra)]:
        if not root.is_dir():
            continue
        for skill in root.rglob("SKILL.md"):
            text = skill.read_text(encoding="utf-8-sig", errors="replace")
            m = re.search(r"^name:\s*['\"]?([a-z0-9-]+)", text, re.M)
            found.setdefault(m.group(1) if m else skill.parent.name, str(skill.parent))
    return found


def check(flow, have):
    rows, missing = [], []
    for s in flow["steps"]:
        hit = next((n for n in s["skills"] if n in have), None)
        status = "installed" if hit else ("skip (optional)" if s["optional"] else "MISSING")
        rows.append({"step": s["step"], "skills": s["skills"], "status": status,
                     "path": have.get(hit) if hit else None})
        if not hit and not s["optional"]:
            missing.append(s["skills"][0])
    return rows, missing


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("workflow", nargs="?", help="a brew: name, number or old W id")
    p.add_argument("--all", action="store_true")
    p.add_argument("--path", action="append", default=[], help="another folder to search")
    p.add_argument("--json", action="store_true")
    p.add_argument("--workflows", default=str(WORKFLOWS), help=argparse.SUPPRESS)
    a = p.parse_args(argv)

    flows = load(Path(a.workflows))
    if a.all == bool(a.workflow):
        p.print_usage()
        return 2
    wanted = list(flows) if a.all else [resolve(flows, a.workflow)]
    if None in wanted:
        print(f"unknown brew {a.workflow}; have " + ", ".join(f"{label(f)} ({k})" for k, f in flows.items()))
        return 2

    have = installed(a.path)
    report, all_missing = {}, []
    for w in wanted:
        rows, missing = check(flows[w], have)
        report[w] = {"brew": label(flows[w]), "title": flows[w]["title"], "steps": rows, "missing": missing}
        all_missing += missing

    if a.json:
        print(json.dumps(report, indent=2))
    else:
        for w, r in report.items():
            print(f"{r['brew']}: {r['title']}")
            for row in r["steps"]:
                print(f"  {row['step']}. {' or '.join(row['skills']):<56} {row['status']}")
            for name in r["missing"]:
                print(f"  install: {install(name)}")
    return 1 if all_missing else 0


if __name__ == "__main__":
    sys.exit(main())
