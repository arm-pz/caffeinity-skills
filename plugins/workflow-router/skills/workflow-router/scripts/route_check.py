#!/usr/bin/env python3
"""Show which skills a caffeinity workflow needs and which of them are installed.

Usage:
  python route_check.py launch-safely      # one workflow, by name ("grow-search-traffic"), number ("4"), old id ("W4") or old brew name ("cold-brew")
  python route_check.py --all              # every workflow
  python route_check.py grow-search-traffic --path DIR   # also search DIR for installed skills
  python route_check.py --all --json       # for another agent to read

Reads the workflow tables in ../references/workflows.md, so that file stays the only list.
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


HEADING = re.compile(r"^## Workflow (\d+) · ([^:]+): (.+)$")

# The workflows were once brews with coffee names; those names still resolve.
LEGACY = {"pour-over": 1, "bloom": 2, "espresso": 3, "cold-brew": 4, "french-press": 5, "cupping": 6,
          "slow-drip": 7, "nitro": 8, "moka-pot": 9, "descale": 10, "estate-roast": 11, "dial-in": 12}


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def load(path=WORKFLOWS):
    """Return {"launch-safely": {"number", "name", "title", "steps": [{"step", "skills", "optional"}]}}
    in file order. Workflows used to be called W1 to W12, then brews; resolve() still accepts both."""
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
    """The workflow key for a name ("grow-search-traffic"), a number ("4", "workflow 4"), an old id
    ("W4") or an old brew name ("Cold brew", "brew 4")."""
    ref = ref.strip().lower()
    m = re.fullmatch(r"(?:w|workflow[ -]?|brew[ -]?)?(\d+)", ref)
    number = int(m.group(1)) if m else LEGACY.get(slug(ref))
    for key, f in flows.items():
        if key == slug(ref) or f["number"] == number:
            return key
    return None


def label(flow):
    return f"Workflow {flow['number']} · {flow['name']}"


# Skills that live in arm-pz/caffeinity-skills rather than a repo of their own. Every skill under
# plugins/ belongs here whether or not a workflow names it as a step, so a later edit to workflows.md
# cannot print an install command for a repo that does not exist; the self-check enforces it.
IN_MARKETPLACE = {"workflow-router", "paper-trail", "course-builder", "skill-estate",
                  "tune-and-ship", "agent-audit"}


def install(name):
    if name in IN_MARKETPLACE:
        return f"npx skills add arm-pz/caffeinity-skills --skill {name}"
    return f"npx skills add arm-pz/{name}"


def install_all(names):
    """One copy-paste command for every missing skill, each once, in the order the brew needs them."""
    return " && ".join(install(n) for n in dict.fromkeys(names))


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
    p.add_argument("workflow", nargs="?", help="a workflow: name, number, old W id or old brew name")
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
        print(f"unknown workflow {a.workflow}; have " + ", ".join(f"{label(f)} ({k})" for k, f in flows.items()))
        return 2

    have = installed(a.path)
    report, all_missing = {}, []
    for w in wanted:
        rows, missing = check(flows[w], have)
        # "brew" repeats "workflow" for readers of the old --json output; drop it in the next release.
        report[w] = {"workflow": label(flows[w]), "brew": label(flows[w]), "title": flows[w]["title"],
                     "steps": rows, "missing": missing,
                     "install": install_all(missing) or None}
        all_missing += missing

    if a.json:
        print(json.dumps(report, indent=2))
    else:
        for w, r in report.items():
            print(f"{r['workflow']}: {r['title']}")
            for row in r["steps"]:
                print(f"  {row['step']}. {' or '.join(row['skills']):<56} {row['status']}")
            if r["missing"]:
                print(f"  install: {install_all(r['missing'])}")
    return 1 if all_missing else 0


if __name__ == "__main__":
    sys.exit(main())
