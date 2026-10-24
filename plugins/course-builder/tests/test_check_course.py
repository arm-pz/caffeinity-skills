#!/usr/bin/env python3
"""Self-check for check_course.py: python -I tests/test_check_course.py"""
import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "skills" / "course-builder" / "scripts"))
import check_course  # noqa: E402

GOOD = {
    "title": "Ship a static site",
    "budget_hours": 12,
    "outcomes": [{"id": "O1", "text": "Deploy a static site from a git push"},
                 {"id": "O2", "text": "Diagnose a failing build from its log"}],
    "modules": [
        {"id": "M1", "title": "First deploy", "outcomes": ["O1"], "prereqs": [], "hours": 6,
         "assessment": {"outcomes": ["O1"], "evidence": "live URL"}},
        {"id": "M2", "title": "Logs", "outcomes": ["O2"], "prereqs": ["M1"], "hours": 6,
         "assessment": {"outcomes": ["O2"], "evidence": "diagnosis"}},
    ],
}

fails, warns, total = check_course.check(GOOD)
assert not fails and not warns and total == 12, (fails, warns)

bad = copy.deepcopy(GOOD)
bad["outcomes"].append({"id": "O3", "text": "Understand caching"})
bad["modules"][0]["prereqs"] = ["M2"]
bad["modules"][1]["hours"] = 9
fails, warns, _ = check_course.check(bad)
assert any("O3: no module teaches it" in f for f in fails), fails
assert any("O3: nothing assesses it" in f for f in fails), fails
assert any("M1: prerequisite M2 comes at or after it" in f for f in fails), fails
assert any("15 hours against a budget of 12" in f for f in fails), fails
assert any("O3: starts with 'understand'" in w for w in warns), warns

# The final project may assess a module's outcome; that is a warning, not a failure.
final = copy.deepcopy(GOOD)
del final["modules"][1]["assessment"]
final["final"] = {"outcomes": ["O2"], "evidence": "capstone"}
fails, warns, _ = check_course.check(final)
assert not fails, fails
assert any("M2: no module assessment; the final covers" in w for w in warns), warns

dup = copy.deepcopy(GOOD)
dup["modules"][1]["id"] = "M1"
fails, _, _ = check_course.check(dup)
assert any("module id M1 is used more than once" in f for f in fails), fails

print("check_course: ok")
