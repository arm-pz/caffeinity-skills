#!/usr/bin/env python3
"""Self-check for tune-and-ship's queue.py. Offline: no network, no git.

    python -I plugins/tune-and-ship/tests/test_queue.py
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "tune-and-ship" / "scripts" / "queue.py"

MANIFEST = {"skills": [
    {"name": "alpha", "repo": "o/alpha", "path": "."},
    {"name": "beta", "repo": "o/beta", "path": "."},
    {"name": "gamma", "repo": "o/bundle", "path": "plugins/gamma/skills/gamma"},
    {"name": "delta-mod", "repo": "o/bundle", "path": "mods/delta", "kind": "mod"},
    {"name": "old", "repo": "o/old", "path": ".", "legacy": True},
]}
SOURCES = """| Skill | Source | Commit |
| --- | --- | --- |
| alpha | [o/alpha](https://github.com/o/alpha) | `aaaaaaa` |
| beta | [o/beta](https://github.com/o/beta) | `bbbbbbb` |
| gamma | [o/bundle](https://github.com/o/bundle) | `this re` |
"""


def run(d, *args):
    r = subprocess.run([sys.executable, "-I", str(SCRIPT), "--offline",
                        "--manifest", str(d / "m.json"), "--sources", str(d / "s.md"), *args],
                       capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


def main():
    with tempfile.TemporaryDirectory() as t:
        d = Path(t)
        (d / "m.json").write_text(json.dumps(MANIFEST))
        (d / "s.md").write_text(SOURCES)

        code, out, _ = run(d)
        assert code == 0, out
        assert "delta-mod" not in out and "| old |" not in out, "mods and legacy are skipped"
        assert "| gamma | o/bundle | plugins/gamma/skills/gamma | - | - | in-repo | todo |" in out, out
        assert "3 skills: 3 todo, 0 queued, 0 done. Next: alpha" in out, out

        code, out, _ = run(d, "--next", "--ledger", str(d / "missing.md"))
        assert (code, out.strip()) == (0, "alpha"), "a missing ledger is an empty one"

        (d / "l.md").write_text("| skill | from | to | PR | date | open |\n| --- | --- | --- | --- | --- | --- |\n"
                                "| alpha | 0.1.1 | 0.1.2 | #2 | 2026-11-10 | none |\n"
                                "| gamma | - | - | - | 2026-11-10 | queued: hand-off is one-way |\n")
        code, out, _ = run(d, "--ledger", str(d / "l.md"))
        assert "| alpha | o/alpha | . | - | aaaaaaa | unknown | done |" in out, out
        assert "1 todo, 1 queued, 1 done. Next: gamma" in out, "queued siblings go first"

        (d / "l.md").write_text("| alpha | x |\n| beta | x |\n| gamma | x |\n")
        code, out, err = run(d, "--next", "--ledger", str(d / "l.md"))
        assert code != 0 and "every skill" in err, "an empty queue is an error, not a blank line"

        (d / "m.json").write_text("{not json")
        code, _, err = run(d)
        assert code != 0 and "cannot read the catalog" in err
    print("ok: 6 checks")


if __name__ == "__main__":
    main()
