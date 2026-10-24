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
assert list(flows)[:4] == ["pour-over", "bloom", "espresso", "cold-brew"], list(flows)
# Old W ids, numbers and names all resolve; other skills used to cite "W3".
for ref in ("W3", "w3", "3", "brew 3", "Brew-3", "espresso", "Espresso"):
    assert route_check.resolve(flows, ref) == "espresso", ref
assert route_check.resolve(flows, "W99") is None
# Other skills cite these numbers; renumbering breaks them.
assert flows["espresso"]["steps"][0]["skills"] == ["web-preflight"], flows["espresso"]
assert flows["cold-brew"]["steps"][0]["skills"] == ["seo-crawl"], flows["cold-brew"]
assert all(f["steps"] for f in flows.values())
assert flows["descale"]["steps"][0]["skills"] == ["tune-skill"], flows["descale"]
assert route_check.install("paper-trail") == "npx skills add arm-pz/caffeinity-skills --skill paper-trail"


def run(*args, home):
    return subprocess.run([sys.executable, "-I", str(SCRIPT), *args], capture_output=True,
                          text=True, env={"HOME": str(home), "PATH": ""}, cwd=home)


with tempfile.TemporaryDirectory() as tmp:
    home = Path(tmp)
    p = run("slow-drip", home=home)
    assert p.returncode == 1 and "MISSING" in p.stdout and "npx skills add arm-pz/topic-primer" in p.stdout, p.stdout

    for name in ("topic-primer", "study-system"):
        d = home / ".claude" / "skills" / name
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text(f"---\nname: {name}\ndescription: x\n---\n", encoding="utf-8")
    p = run("slow-drip", home=home)
    assert p.returncode == 0 and "MISSING" not in p.stdout, p.stdout
    assert "skip (optional)" in p.stdout, p.stdout   # course-builder is optional in Slow drip

    p = run("moka-pot", home=home)
    assert "npx skills add arm-pz/caffeinity-skills --skill paper-trail" in p.stdout, p.stdout

    # An optional step that is not installed is a skip, not a failure.
    p = run("W6", "--json", home=home)
    assert p.returncode == 1 and '"skip (optional)"' in p.stdout, p.stdout

    assert run(home=home).returncode == 2
    assert run("W99", home=home).returncode == 2

print("ok")
