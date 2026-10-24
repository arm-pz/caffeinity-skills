#!/usr/bin/env python3
"""Check a course plan (course.json) for gaps and overload.

    python check_course.py course.json

FAIL (exit 1): an outcome no module teaches, an outcome nothing assesses, a prerequisite on a
later or unknown module, a module or outcome id used twice, or total hours over budget_hours.
WARN: an outcome starting with an unmeasurable verb, a module with no outcome or no assessment,
and a module taking more than a quarter of the budget. The shape is in references/alignment.md.
"""
import json
import sys

VAGUE = ("understand", "know", "learn", "appreciate", "be aware", "be familiar", "gain insight",
         "grasp", "get to know")


def check(course):
    fails, warns = [], []
    outcomes = course.get("outcomes", [])
    modules = course.get("modules", [])
    out_ids = [o["id"] for o in outcomes]
    mod_ids = [m["id"] for m in modules]
    for kind, ids in (("outcome", out_ids), ("module", mod_ids)):
        for i in sorted({i for i in ids if ids.count(i) > 1}):
            fails.append(f"{kind} id {i} is used more than once")
    if not outcomes:
        fails.append("no outcomes")
    if not modules:
        fails.append("no modules")

    for o in outcomes:
        text = o.get("text", "").strip().lower()
        for v in VAGUE:
            if text.startswith(v) or text.startswith("to " + v) or text.startswith("students will " + v):
                warns.append(f"{o['id']}: starts with {v!r}, which no assessment can observe; use a verb from references/outcomes.md")
                break

    taught, assessed = set(), set()
    final = course.get("final") or {}
    assessed.update(final.get("outcomes", []))
    for idx, m in enumerate(modules):
        mid = m["id"]
        if not m.get("outcomes"):
            warns.append(f"{mid}: teaches no course outcome; cut it or mark it optional")
        for oid in m.get("outcomes", []):
            if oid not in out_ids:
                fails.append(f"{mid}: names outcome {oid}, which is not defined")
            taught.add(oid)
        assessment = m.get("assessment")
        if assessment:
            for oid in assessment.get("outcomes", []):
                if oid not in out_ids:
                    fails.append(f"{mid}: assesses outcome {oid}, which is not defined")
                assessed.add(oid)
        else:
            covered = set(m.get("outcomes", [])) <= set(final.get("outcomes", []))
            warns.append(f"{mid}: no module assessment" + ("; the final covers its outcomes, say so in the syllabus" if covered else ""))
        for p in m.get("prereqs", []):
            if p not in mod_ids:
                fails.append(f"{mid}: prerequisite {p} is not a module")
            elif mod_ids.index(p) >= idx:
                fails.append(f"{mid}: prerequisite {p} comes at or after it; reorder the modules")

    for oid in out_ids:
        if oid not in taught:
            fails.append(f"{oid}: no module teaches it")
        if oid not in assessed:
            fails.append(f"{oid}: nothing assesses it")

    total = sum(float(m.get("hours", 0)) for m in modules)
    budget = course.get("budget_hours")
    if budget is None:
        warns.append(f"no budget_hours; the plan totals {total:g} hours")
    else:
        if total > float(budget):
            fails.append(f"plan totals {total:g} hours against a budget of {budget:g}; cut or merge modules")
        for m in modules:
            if float(m.get("hours", 0)) > float(budget) / 4 and len(modules) > 4:
                warns.append(f"{m['id']}: {float(m['hours']):g} hours is over a quarter of the budget; consider splitting it")
    missing_hours = [m["id"] for m in modules if "hours" not in m]
    if missing_hours:
        warns.append("no hours on " + ", ".join(missing_hours))
    return fails, warns, total


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print(__doc__.strip().splitlines()[2].strip())
        return 2
    with open(argv[0], encoding="utf-8") as f:
        course = json.load(f)
    fails, warns, total = check(course)
    for msg in fails:
        print(f"FAIL  {msg}")
    for msg in warns:
        print(f"WARN  {msg}")
    budget = course.get("budget_hours")
    print(f"\n{len(course.get('outcomes', []))} outcomes, {len(course.get('modules', []))} modules, "
          f"{total:g} of {budget if budget is not None else '?'} hours; {len(fails)} FAIL, {len(warns)} WARN")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
