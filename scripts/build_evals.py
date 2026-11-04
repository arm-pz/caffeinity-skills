#!/usr/bin/env python3
"""Turn evals/triggers.json into a `claude plugin eval` suite for the caffeinity bundle.

    python scripts/build_evals.py           # write plugins/caffeinity/evals/
    python scripts/build_evals.py --check   # exit 1 if the suite is stale or a case is invalid

Each case becomes plugins/caffeinity/evals/<id>/prompt.md plus one tool_used grader per skill:
`fires` (the expected skill loaded at least once) and `quiet-<skill>` (a skill that must not load).
The graders read the Skill tool's input, so they test triggering only: the run is capped at a few
turns and given read-only tools. Every bundled skill must have at least one case that expects it.

A case with `agent` instead of `expect` tests delegation to a workflow agent: the run may also use
the Agent tool, and `delegates` checks the Agent input names that agent (`not_agents` must not be
delegated to). Every agent in plugins/caffeinity/agents.json must have at least one such case.
Run the suite with scripts/run_evals.sh; it needs a Claude login, so it never runs in CI.
"""
import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "evals" / "triggers.json"
PLUGIN = ROOT / "plugins" / "caffeinity"
OUT = PLUGIN / "evals"
ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
KEEP = {"results"}   # run output lives beside the cases; never generated, never deleted

PROMPT = """---
max_turns: 3
timeout_seconds: 180
allowed_tools: [{tools}]
tags: [trigger{tags}]
---

{prompt}
"""

GRADER = """---
type: tool_used
tool: {tool}
input_match: '{pattern}'
{bound}
---
"""


def pattern(skill):
    # The Skill input names the skill bare or plugin-qualified ("caffeinity:paper-trail"); the
    # closing quote keeps "findable" from matching "findable-polish".
    return f'[":]{re.escape(skill)}"'


def load():
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    skills = sorted(p.name for p in (PLUGIN / "skills").iterdir() if (p / "SKILL.md").is_file())
    # Skills that live in this repo count before the hourly rebuild has bundled them.
    known = set(skills) | {p.parent.name for p in ROOT.glob("plugins/*/skills/*/SKILL.md")}
    agents = {a["name"] for a in json.loads((PLUGIN / "agents.json").read_text(encoding="utf-8"))["agents"]}
    errors, seen, covered, delegated = [], set(), set(), set()
    for case in data["cases"]:
        cid = case.get("id", "")
        if not ID.fullmatch(cid):
            errors.append(f"{cid!r}: id must be lowercase words joined by hyphens")
        if cid in seen:
            errors.append(f"{cid}: duplicate id")
        seen.add(cid)
        if not str(case.get("prompt", "")).strip():
            errors.append(f"{cid}: empty prompt")
        expect, nots = case.get("expect"), case.get("not", [])
        agent, not_agents = case.get("agent"), case.get("not_agents", [])
        if expect is None and not nots and agent is None and not not_agents:
            errors.append(f"{cid}: needs `expect`, `not`, `agent` or `not_agents`")
        for name in ([agent] if agent else []) + not_agents:
            if name not in agents:
                errors.append(f"{cid}: {name} is not an agent in agents.json")
        if agent and agent in not_agents:
            errors.append(f"{cid}: {agent} is both expected and forbidden")
        if agent:
            delegated.add(agent)
        for name in ([expect] if expect else []) + nots:
            if name not in known:
                errors.append(f"{cid}: {name} is neither bundled nor in this repo")
        if expect in nots:
            errors.append(f"{cid}: {expect} is both expected and forbidden")
        if expect:
            covered.add(expect)
    for name in skills:
        if name not in covered:
            errors.append(f"{name}: no case expects it; add one to evals/triggers.json")
    for name in sorted(agents - delegated):
        errors.append(f"{name}: no case delegates to it; add one with `agent` to evals/triggers.json")
    return data["cases"], errors


def render(case):
    files = {}
    is_agent = bool(case.get("agent") or case.get("not_agents"))
    tags = (["agent"] if is_agent else []) \
        + (["positive"] if case.get("expect") or case.get("agent") else []) \
        + (["negative"] if case.get("not") or case.get("not_agents") else [])
    tools = "Agent, Skill, Read, Glob, Grep" if is_agent else "Skill, Read, Glob, Grep"
    files["prompt.md"] = PROMPT.format(tools=tools, tags="".join(f", {t}" for t in tags),
                                       prompt=case["prompt"].strip())
    if case.get("expect"):
        files["graders/fires.md"] = GRADER.format(tool="Skill", pattern=pattern(case["expect"]), bound="min: 1")
    for name in case.get("not", []):
        files[f"graders/quiet-{name}.md"] = GRADER.format(tool="Skill", pattern=pattern(name), bound="min: 0\nmax: 0")
    if case.get("agent"):
        files["graders/delegates.md"] = GRADER.format(tool="Agent", pattern=pattern(case["agent"]), bound="min: 1")
    for name in case.get("not_agents", []):
        files[f"graders/quiet-agent-{name}.md"] = GRADER.format(tool="Agent", pattern=pattern(name), bound="min: 0\nmax: 0")
    return files


def wanted(cases):
    return {f"{c['id']}/{rel}": text for c in cases for rel, text in render(c).items()}


def current():
    if not OUT.is_dir():
        return {}
    return {p.relative_to(OUT).as_posix(): p.read_text(encoding="utf-8")
            for p in OUT.rglob("*") if p.is_file() and p.relative_to(OUT).parts[0] not in KEEP}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    cases, errors = load()
    for e in errors:
        print(f"invalid: {e}")
    if errors:
        return 1
    want, have = wanted(cases), current()
    stale = sorted(k for k in set(want) | set(have) if want.get(k) != have.get(k))
    if a.check:
        for k in stale:
            print(f"stale: evals/{k}")
        print(f"{len(cases)} cases, {'stale' if stale else 'current'}")
        return 1 if stale else 0
    for d in OUT.iterdir() if OUT.is_dir() else []:
        if d.is_dir() and d.name not in KEEP:
            shutil.rmtree(d)
    for rel, text in want.items():
        path = OUT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    print(f"evals: {len(cases)} cases written to {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
