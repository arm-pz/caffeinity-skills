#!/usr/bin/env python3
"""Reduce a `claude plugin eval --json` result to evals/last-run.json and say what changed.

    python scripts/summarize_evals.py run.json evals/last-run.json

The summary keeps, per case, whether every run passed and which graders failed (`fires` means the
expected skill did not load; `quiet-<skill>` means that skill loaded when it should not have).
Compared with the previous summary it prints NEWLY FAILING and NOW PASSING cases, so a description
edit that breaks triggering shows up as a named regression.
"""
import json
import sys
from pathlib import Path


def summarize(run):
    cases = {}
    for case in run["cases"]:
        runs = [r for arm in case["arms"].values() for r in arm]
        failed = sorted({g["name"] for r in runs for g in r["graders"] if g.get("scored", True) and not g["passed"]})
        # Hitting the turn cap after the graders already decided is how a trigger run normally ends
        # (the skill loads on turn one, then starts working); only other errors count.
        errors = sorted({r["error"] for r in runs
                         if r.get("error") and "maximum number of turns" not in r["error"]})
        cases[case["name"]] = {"pass": not failed and not errors, "failed": failed, **({"errors": errors} if errors else {})}
    return {
        "startedAt": run.get("startedAt"),
        "claudeVersion": run.get("claudeVersion"),
        "costUsd": round(run.get("costUsd") or 0, 2),
        "partial": bool(run.get("partial")),
        "passed": sum(c["pass"] for c in cases.values()),
        "total": len(cases),
        "cases": dict(sorted(cases.items())),
    }


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[2].strip())
        return 2
    run_path, out_path = Path(argv[0]), Path(argv[1])
    if not run_path.is_file():
        print(f"no eval result at {run_path}; the run did not finish")
        return 1
    new = summarize(json.loads(run_path.read_text(encoding="utf-8")))
    old = json.loads(out_path.read_text(encoding="utf-8")) if out_path.is_file() else {"cases": {}}
    # A filtered run (--case) only updates the cases it ran.
    merged = dict(old.get("cases", {}))
    for name, result in new["cases"].items():
        before = merged.get(name)
        if before and before["pass"] and not result["pass"]:
            print(f"NEWLY FAILING  {name}: {', '.join(result['failed'] + result.get('errors', []))}")
        elif before and not before["pass"] and result["pass"]:
            print(f"NOW PASSING    {name}")
        merged[name] = result
    for name, result in sorted(new["cases"].items()):
        if not result["pass"]:
            print(f"FAIL  {name}: {', '.join(result['failed'] + result.get('errors', []))}")
    summary = dict(new, cases=dict(sorted(merged.items())),
                   passed=sum(c["pass"] for c in merged.values()), total=len(merged))
    out_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"\n{new['passed']}/{new['total']} cases passed this run (${new['costUsd']}); "
          f"{summary['passed']}/{summary['total']} overall in {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
