#!/usr/bin/env python3
"""Screen a Claude Code plugin folder against the Claude plugin directory's rules before you submit.

    python screen.py PLUGIN_FOLDER            # the folder that holds .claude-plugin/plugin.json
    python screen.py PLUGIN_FOLDER --json

Prints GO or HOLD and every finding as `[bucket] CODE rule -> path:line`. Buckets follow the
portal: block (validation fails), hold (passes, then held for review), warn (shown to reviewers),
info (no action). Rules are for organizations that are not Verified. The portal's safety scan is
stricter than any regex: a GO here means "nothing known blocks", not "will pass". Exit 1 on HOLD.
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # frontmatter still gets the shape checks without it
    yaml = None

ALLOWED_EXT = {".md", ".txt", ".json", ".yaml", ".yml", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico"}
TEXT_EXT = {".md", ".txt", ".json", ".yaml", ".yml"}
KEEP_NAMES = {"LICENSE", "LICENSE.md", "LICENSE.txt", "README", "README.md", ".gitignore"}
JUNK = {".DS_Store", "Thumbs.db", "desktop.ini", "__MACOSX"}
PKG_FILE = re.compile(r"^(package(-lock)?\.json|npm-shrinkwrap\.json|requirements.*\.txt|pnpm-.*\.yaml|yarn\.lock"
                      r"|.*\.lock|\.npmrc|\.yarnrc(\.yml)?|bunfig\.toml|uv\.toml|pyproject\.toml|Pipfile|Gemfile|go\.(mod|sum))$")
# Manifest fields Claude Code reads (manifest reference) plus listing-only fields the directory reads.
MANIFEST = {"$schema", "name", "displayName", "version", "description", "author", "homepage", "repository", "license",
            "keywords", "metadata", "defaultEnabled", "engines", "dependencies", "network", "userConfig", "types",
            "channels", "skills", "commands", "agents", "hooks", "mcpServers", "lspServers", "outputStyles",
            "workflows", "experimental"}
LISTING_ONLY = {"icon", "documentationUrl", "supportUrl", "privacyPolicyUrl", "termsOfServiceUrl"}
SAFE_FRONTMATTER = {"name", "description"}  # the portal does not publish its list; these always pass
RESERVED = re.compile(r"^(claude|anthropic|anthropics|claude-code|claude-mods|official|plugin|mcp|test)$|^(claude|anthropic|anthropics|cc-plugin)-")
LINE_RULES = [
    ("hold", "INSTALL_COMMAND", "install or launcher command, even in docs: link to the tool's own install page",
     re.compile(r"\b(npx|bunx|uvx|pnpm dlx|yarn dlx|pipx run|uv run|uv pip|npm (i|install|ci)|pip3? install|brew install"
                r"|pnpm (add|install)|yarn add|cargo install|go install|gem install|apt(-get)? install|choco install"
                r"|winget install|scoop install)\b")),
    ("hold", "RUNTIME_FETCH_EXEC", "download piped into a shell or interpreter",
     re.compile(r"\b(curl|wget|iwr|irm|Invoke-WebRequest|Invoke-RestMethod)\b.*\|\s*(sudo\s+)?(ba|z)?sh\b"
                r"|\|\s*(python3?|node|iex|Invoke-Expression)\b")),
    ("warn", "RUNTIME_FETCH_EXEC?", "prose the portal's scanner read as download-and-execute: reword it",
     re.compile(r"\b(fetch|download)\w*\b.{0,60}\b(pipe|interpreter|execute|run it)\b|\bbrew\b", re.I)),
    ("hold", "ENV_CREDENTIAL", "reads a credential from the environment: held even in a README example",
     re.compile(r"\$\{?[A-Z][A-Z0-9_]*(TOKEN|SECRET|API_KEY|PASSWORD|ACCESS_KEY)\b|\b[A-Z][A-Z0-9_]*(TOKEN|SECRET|API_KEY|PASSWORD|ACCESS_KEY)=")),
]


def frontmatter_findings(rel, text):
    out = []
    m = re.match(r"---\r?\n(.*?)\r?\n---(\r?\n|$)", text, re.S)
    if not m:
        return [("warn", "NO_FRONTMATTER", "no frontmatter block; description is expected", rel)]
    raw = m.group(1)
    if raw.count("[") + raw.count("{") > 32:
        out.append(("block", "FRONTMATTER_SHAPE", "more than 32 [ and { together", rel))
    if raw.count(",") > 1000:
        out.append(("block", "FRONTMATTER_SHAPE", "more than 1,000 commas", rel))
    keys = re.findall(r"^([A-Za-z_][\w-]*)\s*:", raw, re.M)
    for k in keys:
        if k not in SAFE_FRONTMATTER:
            out.append(("block?", "FRONTMATTER_KEY", f"key `{k}` may be outside the allowed list: keep name and description only, or validate to learn", rel))
    if yaml:
        try:
            meta = yaml.safe_load(raw) or {}
            if not isinstance(meta.get("description"), str):
                out.append(("block", "FRONTMATTER_SHAPE", "description must be one text value", rel))
        except yaml.YAMLError:
            out.append(("block", "FRONTMATTER_SHAPE", "frontmatter does not parse as YAML", rel))
    return out


def screen(root):
    root = Path(root)
    f = []  # (bucket, code, rule, where)
    mpath = root / ".claude-plugin" / "plugin.json"
    if not mpath.is_file():
        return [("block", "NO_MANIFEST", "no .claude-plugin/plugin.json: submit the folder that holds it", str(root))]
    try:
        man = json.loads(mpath.read_text(encoding="utf-8-sig"))
    except ValueError as e:
        return [("block", "MANIFEST_JSON", f"plugin.json does not parse: {e}", ".claude-plugin/plugin.json")]
    name = str(man.get("name", ""))
    if not re.fullmatch(r"[a-z0-9]([a-z0-9-]{0,62}[a-z0-9])?", name):
        f.append(("block", "NAME", "name must be lowercase letters, digits and hyphens, at most 64", ".claude-plugin/plugin.json"))
    if RESERVED.search(name):
        f.append(("block", "NAME", f"`{name}` is a reserved name", ".claude-plugin/plugin.json"))
    for k in man:
        where = f".claude-plugin/plugin.json · {k}"
        if k in LISTING_ONLY:
            f.append(("info", "UNKNOWN_KEY_CROSS_TOOL", "listing field the directory reads; no action", where))
        elif k not in MANIFEST:
            f.append(("block", "UNKNOWN_KEY", "field outside the allowed list: remove it", where))
    if "metadata" in man:
        f.append(("block?", "UNKNOWN_KEY", "`metadata` was refused for a non-Verified org in practice: remove it", ".claude-plugin/plugin.json · metadata"))
    if (root / "plugin.json").is_file():
        f.append(("warn", "ROOT_MANIFEST", "root plugin.json (agent-plugins format) is ignored by Claude; drop it from this folder", "plugin.json"))
    if not any((root / n).is_file() for n in ("LICENSE", "LICENSE.md", "LICENSE.txt")) and not man.get("license"):
        f.append(("block", "LICENSE", "add a LICENSE file or set license in plugin.json", "."))
    # The portal accepted a plugin subfolder with no README when the repo root had one.
    dirs = [root.resolve(), *root.resolve().parents]
    dirs = dirs[: next((i + 1 for i, d in enumerate(dirs) if (d / ".git").exists()), 1)]
    readme = next((d / n for d in dirs for n in ("README.md", "README") if (d / n).is_file()), None)
    words = len(re.sub(r"```.*?```", "", readme.read_text(encoding="utf-8-sig", errors="replace"), flags=re.S).split()) if readme else 0
    if words < 40:
        f.append(("block", "README", f"README needs at least 40 words outside code blocks (has {words})", "README.md"))

    files = [p for p in root.rglob("*") if p.is_file() and ".git" not in p.relative_to(root).parts]
    if len(files) > 512:
        f.append(("hold", "FILE_COUNT", f"{len(files)} files; ship 512 or fewer (generated eval suites are the usual cause)", "."))
    icon = str(man.get("icon", "")).lstrip("./")
    for p in files:
        rel = p.relative_to(root).as_posix()
        parts = rel.split("/")
        if p.name in JUNK or "__MACOSX" in parts:
            f.append(("block", "JUNK_FILE", "OS junk file", rel)); continue
        if ".claude" in parts and "skills" in parts:
            f.append(("block", "RESTRICTED_FILE", ".claude/skills folder: move skills to skills/", rel))
        if ".claude-plugin" in parts[:-1] and parts.index(".claude-plugin") > 0:
            f.append(("block", "RESTRICTED_FILE", "a .claude-plugin folder other than the plugin's own", rel))
        if re.search(r'[<>:"\\|?*\x00-\x1f]', rel) or any(s.rstrip(". ") != s for s in parts):
            f.append(("block", "PATH_NAME", "path not every computer keeps", rel))
        ext = p.suffix.lower()
        if p.suffix == ".svg" and rel != icon:
            f.append(("block", "RESTRICTED_FILE", "only the plugin's icon may be .svg: use PNG", rel)); continue
        if ext not in ALLOWED_EXT and p.name not in KEEP_NAMES and rel != icon:
            f.append(("block", "RESTRICTED_FILE", f"{ext or p.name} file: only Markdown, text, JSON, YAML and images", rel)); continue
        if PKG_FILE.match(p.name):
            f.append(("block", "RESTRICTED_FILE", "package-manager file", rel))
        if p.stat().st_size > 256 * 1024 and ext in TEXT_EXT:
            f.append(("hold", "FILE_SIZE", "text file over 256 KiB", rel))
        if ext not in TEXT_EXT and p.name not in KEEP_NAMES:
            continue
        data = p.read_bytes()
        if b"\0" in data:
            f.append(("block", "ENCODING", "NUL byte: save as UTF-8 text", rel)); continue
        try:
            text = data.decode("utf-8-sig")
        except UnicodeDecodeError:
            f.append(("block", "ENCODING", "not UTF-8", rel)); continue
        if text.startswith("#!"):
            f.append(("block", "RESTRICTED_FILE", "starts with #!", rel))
        for i, line in enumerate(text.splitlines(), 1):
            for bucket, code, rule, rx in LINE_RULES:
                if rx.search(line):
                    f.append((bucket, code, rule, f"{rel}:{i}"))
        if ext == ".md" and (parts[0] in ("skills", "agents", "commands")):
            f += frontmatter_findings(rel, text) if p.name == "SKILL.md" or parts[0] != "skills" else []
    return f


ORDER = {"block": 0, "block?": 1, "hold": 2, "warn": 3, "info": 4}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("folder")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    found = sorted(set(screen(a.folder)), key=lambda x: (ORDER[x[0]], x[1], x[3]))
    verdict = "HOLD" if any(b in ("block", "block?", "hold") for b, *_ in found) else "GO"
    if a.json:
        print(json.dumps({"verdict": verdict, "findings": [dict(zip(("bucket", "code", "rule", "where"), x)) for x in found]}, indent=1))
    else:
        counts = {b: sum(1 for x in found if x[0] == b) for b in ORDER}
        print(f"{verdict}  " + "  ".join(f"{b}={n}" for b, n in counts.items() if n))
        for b, code, rule, where in found:
            print(f"[{b}] {code} {rule} -> {where}")
    return 1 if verdict == "HOLD" else 0


if __name__ == "__main__":
    sys.exit(main())
