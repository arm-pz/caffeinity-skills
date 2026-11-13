#!/usr/bin/env python3
"""List bundled skills and agents that have no case in evals/triggers.json.

Usage: python .claude/skills/trigger-coverage/scripts/list_uncovered.py [repo-root]

Prints JSON: each uncovered skill with its description (which holds the
"Not for ... (use X)" siblings to put in `not`), each uncovered agent, any
other validation errors, and the existing case ids so new ids don't collide.
Read-only. Reuses scripts/build_evals.py so the rules stay in one place.
"""
import contextlib
import io
import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
sys.path.insert(0, str(root / "scripts"))
import build_evals  # noqa: E402

with contextlib.redirect_stdout(io.StringIO()):
    cases, errors = build_evals.load()

skill_re = re.compile(r"^(\S+): no case expects it")
agent_re = re.compile(r"^(\S+): no case delegates to it")


def description(skill):
    text = (build_evals.PLUGIN / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
    front = text.split("---", 2)[1] if text.startswith("---") else ""
    m = re.search(r"^description:\s*(?:>-?|\|-?)?\s*\n?(.*?)(?=^\S[^:\n]*:|\Z)", front, re.S | re.M)
    return " ".join(m.group(1).split()).strip("'\"") if m else ""


skills = [m.group(1) for e in errors if (m := skill_re.match(e))]
agents = [m.group(1) for e in errors if (m := agent_re.match(e))]
other = [e for e in errors if not skill_re.match(e) and not agent_re.match(e)]
json.dump({
    "uncovered_skills": [{"name": s, "description": description(s)} for s in skills],
    "uncovered_agents": agents,
    "other_errors": other,
    "existing_ids": sorted(c.get("id", "") for c in cases),
}, sys.stdout, indent=2)
print()
