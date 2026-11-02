#!/usr/bin/env python3
"""Self-check for route_check.py: python -I tests/test_route_check.py"""
import subprocess
import sys
import tempfile
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent / "skills" / "caffeinity-routing"
SCRIPT = SKILL / "scripts" / "route_check.py"
sys.path.insert(0, str(SCRIPT.parent))
import route_check  # noqa: E402

flows = route_check.load()
assert [f["number"] for f in flows.values()] == list(range(1, 12)), list(flows)
assert list(flows) == [
    "build-a-skill", "get-found", "launch-safely", "grow-search-traffic", "land-a-job",
    "make-a-decision", "learn-a-skill", "run-cold-outbound", "launch-a-product",
    "maintain-skills", "audit-a-skill-estate"], list(flows)
# The name, the number and every older way to cite a workflow resolve to the same one: the plain
# name, "workflow 3", the old W ids, "Brew 3 · Espresso" and the coffee name alone.
for ref in ("launch-safely", "Launch safely", "workflow 3", "3", "W3", "w3", "brew 3", "Brew-3",
            "Brew 3 · Espresso", "espresso", "Espresso"):
    assert route_check.resolve(flows, ref) == "launch-safely", ref
for old, new in route_check.LEGACY_NAMES.items():
    assert route_check.resolve(flows, old) == new, old
assert route_check.resolve(flows, "W99") is None
assert route_check.resolve(flows, "no-such-workflow") is None
# Other skills cite these numbers; renumbering breaks them.
assert flows["launch-safely"]["steps"][0]["skills"] == ["web-preflight"], flows["launch-safely"]
assert flows["grow-search-traffic"]["steps"][0]["skills"] == ["seo-crawl"], flows["grow-search-traffic"]
assert all(f["steps"] for f in flows.values())
assert flows["maintain-skills"]["steps"][0]["skills"] == ["tune-skill"], flows["maintain-skills"]
assert route_check.install("paper-trail") == "npx skills add arm-pz/caffeinity-skills --skill paper-trail"


def run(*args, home):
    return subprocess.run([sys.executable, "-I", str(SCRIPT), *args], capture_output=True,
                          text=True, env={"HOME": str(home), "PATH": ""}, cwd=home)


with tempfile.TemporaryDirectory() as tmp:
    home = Path(tmp)
    p = run("learn-a-skill", home=home)
    assert p.returncode == 1 and "MISSING" in p.stdout and "npx skills add arm-pz/topic-primer" in p.stdout, p.stdout
    assert "Workflow 7 · learn-a-skill" in p.stdout, p.stdout

    for name in ("topic-primer", "study-system"):
        d = home / ".claude" / "skills" / name
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text(f"---\nname: {name}\ndescription: x\n---\n", encoding="utf-8")
    for ref in ("learn-a-skill", "slow-drip"):   # the old coffee name keeps working
        p = run(ref, home=home)
        assert p.returncode == 0 and "MISSING" not in p.stdout, p.stdout
        assert "skip (optional)" in p.stdout, p.stdout   # course-builder is optional in learn-a-skill

    p = run("launch-a-product", home=home)
    assert "npx skills add arm-pz/caffeinity-skills --skill paper-trail" in p.stdout, p.stdout

    # An optional step that is not installed is a skip, not a failure.
    p = run("W6", "--json", home=home)
    assert p.returncode == 1 and '"skip (optional)"' in p.stdout, p.stdout

    assert run(home=home).returncode == 2
    assert run("W99", home=home).returncode == 2

print("ok")
