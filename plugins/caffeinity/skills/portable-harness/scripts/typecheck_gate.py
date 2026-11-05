#!/usr/bin/env python3
"""Fail only on type-check errors that are not in the baseline.

Usage:
  <type checker> 2>&1 | python3 typecheck_gate.py baseline.txt           # gate
  <type checker> 2>&1 | python3 typecheck_gate.py baseline.txt --update  # record today's errors

Errors are matched by file and message with line and column numbers removed,
so moving code does not create "new" errors. Counts matter: a second copy of a
grandfathered error in the same file is new.
"""
import re
import sys
from collections import Counter
from pathlib import Path

# file(12,5) / file:12:5 / file:12 -> file
POS = re.compile(r"(\(\d+,\d+\)|:\d+:\d+|:\d+)(?=[\s:-])")
# "error TS2322", "error CS0103", "error:" (mypy, pyright); skips summaries like "Found 3 errors."
ERROR = re.compile(r"\berror\b\s*(:|[A-Z]+\d+)", re.IGNORECASE)


def keys(text):
    return Counter(POS.sub("", line).strip() for line in text.splitlines() if ERROR.search(line))


def main():
    if len(sys.argv) not in (2, 3) or sys.argv[2:] not in ([], ["--update"]):
        print(__doc__)
        return 2
    baseline_path = Path(sys.argv[1])
    current = keys(sys.stdin.read())
    if sys.argv[2:] == ["--update"]:
        baseline_path.write_text("".join(f"{k}\n" * n for k, n in sorted(current.items())))
        print(f"baseline: {sum(current.values())} errors recorded in {baseline_path}")
        return 0
    old = Counter(baseline_path.read_text().splitlines()) if baseline_path.exists() else Counter()
    new = current - old
    for k, n in sorted(new.items()):
        print(f"NEW ({n}x): {k}")
    fixed = sum((old - current).values())
    print(f"{sum(new.values())} new, {fixed} fixed (run --update to shrink the baseline)")
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main())
