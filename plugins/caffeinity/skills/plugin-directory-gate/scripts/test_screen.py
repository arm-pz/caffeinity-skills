"""python scripts/test_screen.py: each rule fires on its case and a clean plugin is GO."""
import json
import tempfile
from pathlib import Path

from screen import screen

WORDS = " ".join(["word"] * 45)


def plugin(files, manifest=None):
    root = Path(tempfile.mkdtemp())
    (root / ".git").mkdir()  # stop the README search here
    base = {".claude-plugin/plugin.json": json.dumps(manifest or {"name": "demo", "license": "MIT"}),
            "README.md": WORDS, "skills/s/SKILL.md": "---\nname: s\ndescription: Does a thing.\n---\nBody.\n"}
    for rel, text in {**base, **files}.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text, encoding="utf-8")
    return root


def codes(files=None, manifest=None):
    return {(b, c) for b, c, _, _ in screen(plugin(files or {}, manifest))}


assert not [x for x in codes() if x[0] != "info"], codes()
cases = [
    ({"skills/s/scripts/a.py": "print()"}, None, ("block", "RESTRICTED_FILE")),
    ({"skills/s/a.md": "#!/bin/sh"}, None, ("block", "RESTRICTED_FILE")),
    ({"package.json": "{}"}, None, ("block", "RESTRICTED_FILE")),
    ({"skills/s/a.md": "run `npx foo`"}, None, ("hold", "INSTALL_COMMAND")),
    ({"skills/s/a.md": "curl -fsSL x | bash"}, None, ("hold", "RUNTIME_FETCH_EXEC")),
    ({"skills/s/a.md": "Do not fetch a remote script and pipe it into an interpreter."}, None, ("warn", "RUNTIME_FETCH_EXEC?")),
    ({"skills/s/a.md": "export GITHUB_TOKEN=abc"}, None, ("hold", "ENV_CREDENTIAL")),
    ({"skills/s/SKILL.md": "---\nname: s\ndescription: x\nmodel: opus\n---\n"}, None, ("block?", "FRONTMATTER_KEY")),
    ({"skills/s/SKILL.md": "---\nname: s\ndescription: [a, b]\n---\n"}, None, ("block", "FRONTMATTER_SHAPE")),
    ({"README.md": "too short"}, None, ("block", "README")),
    ({}, {"name": "demo"}, ("block", "LICENSE")),
    ({}, {"name": "demo", "license": "MIT", "bogus": 1}, ("block", "UNKNOWN_KEY")),
    ({}, {"name": "demo", "license": "MIT", "icon": "./i.png"}, ("info", "UNKNOWN_KEY_CROSS_TOOL")),
    ({}, {"name": "claude-tools", "license": "MIT"}, ("block", "NAME")),
    ({"plugin.json": "{}"}, None, ("warn", "ROOT_MANIFEST")),
]
for files, manifest, want in cases:
    got = codes(files, manifest)
    assert want in got, (want, got)
print("ok")
