#!/usr/bin/env python3
"""Self-check for route_check.py: python -I tests/test_route_check.py"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent / "skills" / "caffeinity-routing"
SCRIPT = SKILL / "scripts" / "route_check.py"
sys.path.insert(0, str(SCRIPT.parent))
import route_check  # noqa: E402

flows = route_check.load()
assert [f["number"] for f in flows.values()] == list(range(1, 13)), list(flows)
assert list(flows)[:4] == ["build-a-skill", "get-found", "launch-safely", "grow-search-traffic"], list(flows)
# Old W ids, numbers, names and old brew names all resolve; other skills used to cite "W3" and "Espresso".
for ref in ("W3", "w3", "3", "workflow 3", "Workflow-3", "brew 3", "Brew-3", "launch-safely", "espresso", "Espresso"):
    assert route_check.resolve(flows, ref) == "launch-safely", ref
assert route_check.resolve(flows, "Cold brew") == "grow-search-traffic"
assert route_check.resolve(flows, "W99") is None
# Other skills cite these numbers; renumbering breaks them.
assert flows["launch-safely"]["steps"][0]["skills"] == ["web-preflight"], flows["launch-safely"]
assert [s["skills"] for s in flows["grow-search-traffic"]["steps"]] == [
    ["diagnose-search-visibility"], ["seo-crawl"], ["keyword-guard"], ["wordsmith"],
    ["pre-ship-performance-audit"], ["platform-content"], ["get-indexed"],
    ["verify-search-visibility"],
], flows["grow-search-traffic"]
assert all(f["steps"] for f in flows.values())
assert flows["maintain-skills"]["steps"][0]["skills"] == ["tune-skill"], flows["maintain-skills"]
assert route_check.install("paper-trail") == "npx skills add arm-pz/caffeinity-skills --skill paper-trail"
assert route_check.install("tune-and-ship") == "npx skills add arm-pz/caffeinity-skills --skill tune-and-ship"
assert route_check.install("topic-primer") == "npx skills add arm-pz/topic-primer"
# Missing skills come as one command, each once, so a user copies a single line.
assert route_check.install_all(["seo-crawl", "paper-trail", "seo-crawl"]) == (
    "npx skills add arm-pz/seo-crawl && npx skills add arm-pz/caffeinity-skills --skill paper-trail")
assert route_check.install_all([]) == ""
# Every skill that lives under plugins/ in this repo installs from the marketplace, in a workflow or not.
PLUGINS = SKILL.parents[2]
in_repo = {p.parent.name for p in PLUGINS.glob("*/skills/*/SKILL.md") if p.parents[2].name != "caffeinity"}
assert in_repo == route_check.IN_MARKETPLACE, in_repo ^ route_check.IN_MARKETPLACE
# A new workflow is appended, never inserted; get-indexed and the set-up-a-coding-agent steps are optional extras.
assert list(flows)[-1] == "set-up-a-coding-agent" and route_check.resolve(flows, "W12") == "set-up-a-coding-agent", list(flows)
assert flows["set-up-a-coding-agent"]["steps"][0]["skills"] == ["portable-harness", "harness-audit"], flows["set-up-a-coding-agent"]
assert [s["optional"] for s in flows["set-up-a-coding-agent"]["steps"]] == [False, True, True, True], flows["set-up-a-coding-agent"]
assert flows["get-found"]["steps"][-1]["skills"] == ["get-indexed"]
assert flows["get-found"]["steps"][-1]["optional"]
assert [s["optional"] for s in flows["grow-search-traffic"]["steps"]] == [
    False, False, False, False, True, True, True, False,
]


def run(*args, home):
    return subprocess.run([sys.executable, "-I", str(SCRIPT), *args], capture_output=True,
                          text=True, env={"HOME": str(home), "USERPROFILE": str(home), "PATH": ""}, cwd=home)


with tempfile.TemporaryDirectory() as tmp:
    home = Path(tmp)
    p = run("learn-any-topic", home=home)
    assert p.returncode == 1 and "MISSING" in p.stdout and "npx skills add arm-pz/topic-primer" in p.stdout, p.stdout

    for name in ("topic-primer", "study-system"):
        d = home / ".claude" / "skills" / name
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text(f"---\nname: {name}\ndescription: x\n---\n", encoding="utf-8")
    p = run("learn-any-topic", home=home)
    assert p.returncode == 0 and "MISSING" not in p.stdout, p.stdout
    assert "skip (optional)" in p.stdout, p.stdout   # course-builder is optional in learn-any-topic

    p = run("grow-search-traffic", home=home)
    assert p.stdout.count("install:") == 1, p.stdout
    required = [s["skills"][0] for s in flows["grow-search-traffic"]["steps"] if not s["optional"]]
    assert f"install: {route_check.install_all(required)}" in p.stdout, p.stdout
    assert all(route_check.install(n) in p.stdout for n in required), p.stdout

    p = run("launch-a-product", home=home)
    assert "npx skills add arm-pz/caffeinity-skills --skill paper-trail" in p.stdout, p.stdout

    # An optional step that is not installed is a skip, not a failure.
    p = run("W6", "--json", home=home)
    assert p.returncode == 1 and '"skip (optional)"' in p.stdout, p.stdout
    out = json.loads(p.stdout)["decision-memo"]
    assert out["workflow"] == out["brew"] == "Workflow 6 · decision-memo", out

    assert run(home=home).returncode == 2
    assert run("W99", home=home).returncode == 2

print("ok")
