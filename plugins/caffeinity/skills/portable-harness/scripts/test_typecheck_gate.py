import subprocess
import sys
from pathlib import Path

GATE = str(Path(__file__).with_name("typecheck_gate.py"))
OLD = "src/a.ts(3,1): error TS2322: Type 'x' is not assignable.\nFound 1 error.\n"


def run(stdin, *args):
    return subprocess.run([sys.executable, "-I", GATE, *args], input=stdin, text=True, capture_output=True)


def test_gate(tmp_path):
    base = str(tmp_path / "baseline.txt")
    assert run(OLD, base, "--update").returncode == 0
    # same error on a moved line: still grandfathered
    assert run(OLD.replace("(3,1)", "(40,7)"), base).returncode == 0
    # a new error fails, with the message shown
    r = run(OLD + "src/b.ts:9:2 - error TS2304: Cannot find name 'y'.\n", base)
    assert r.returncode == 1 and "TS2304" in r.stdout
    # a second copy of a grandfathered error is new
    assert run(OLD + OLD.splitlines()[0].replace("(3,1)", "(8,1)") + "\n", base).returncode == 1
    # fixing errors passes
    assert run("", base).returncode == 0
