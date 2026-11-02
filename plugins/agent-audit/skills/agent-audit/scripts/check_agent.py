#!/usr/bin/env python3
"""Lint Claude Code subagent definitions against the seven layers of a production agent.

    python check_agent.py .claude/agents/*.md
    python check_agent.py plugins/my-plugin/agents/ --json

Each finding is FAIL, WARN or INFO and names its layer:
  L1 model · L2 instructions · L3 tools · L4 memory · L5 loop · L6 guardrails · L7 approval
FAIL is a definition Claude Code will misread or reject (a misspelled field is silently ignored).
WARN is a missing production layer. INFO is worth a look. Exit 1 when any FAIL.
Standard library only; the frontmatter parser handles the flat YAML subagent files use.
"""
import argparse
import difflib
import json
import re
import sys
from pathlib import Path

FIELDS = {
    "name", "description", "tools", "disallowedTools", "model", "permissionMode", "maxTurns",
    "autoCompactWindow", "skills", "mcpServers", "hooks", "memory", "background", "omitClaudeMd",
    "effort", "isolation", "color", "initialPrompt", "experimental",
}
# Plugin-shipped agents ignore these for security; they work only in .claude/agents or ~/.claude/agents.
PLUGIN_IGNORED = {"permissionMode", "hooks", "mcpServers", "initialPrompt"}
ENUMS = {
    "model": None,  # alias or full model id; checked separately
    "permissionMode": {"default", "acceptEdits", "auto", "dontAsk", "bypassPermissions", "plan", "manual"},
    "memory": {"user", "project", "local"},
    "effort": {"low", "medium", "high", "xhigh", "max"},
    "isolation": {"worktree"},
    "color": {"red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"},
}
MODEL_ALIASES = {"inherit", "sonnet", "opus", "haiku", "fable"}
WEB_TOOLS = {"WebFetch", "WebSearch"}
ACT_TOOLS = {"Bash", "Write", "Edit", "NotebookEdit"}

STOP = re.compile(r"\b(stop(s|ping)?\b|exit condition|done when|until\b|finish(es)? when|gate)", re.I)
APPROVAL = re.compile(r"\b(confirm|approv|ask (the user |first|before)|wait for (the user|a yes|approval)|user's yes)", re.I)
UNTRUSTED = re.compile(r"(untrusted|data,? not instructions|prompt injection|never act on (it|instructions)|"
                       r"instructions? (inside|in|embedded in) (it|them|the (page|content|file)))", re.I)
NOT_FOR = re.compile(r"\b(not for|do not use|don't use|never use)\b", re.I)
USE_WHEN = re.compile(r"\b(use (proactively|when|whenever|for|after|before|immediately)|when (someone|the user|asked))", re.I)


def parse(text):
    """Return (frontmatter dict, body, error). Values: str, list[str], or True for nested blocks."""
    if not text.startswith("---"):
        return None, text, "no frontmatter: the file must start with a --- block"
    end = re.search(r"^---\s*$", text[3:], re.M)
    if not end:
        return None, text, "frontmatter is never closed with ---"
    head, body = text[3:3 + end.start()], text[3 + end.end():]
    fm, key = {}, None
    for line in head.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        top = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if top:
            key, val = top.group(1), top.group(2).strip()
            if val == "":
                fm[key] = None                      # a list or mapping follows
            elif val in (">", ">-", "|", "|-"):
                fm[key] = ""                        # a folded or literal string follows
            elif val.startswith("[") and val.endswith("]"):
                fm[key] = [v.strip().strip("\"'") for v in val[1:-1].split(",") if v.strip()]
            else:
                fm[key] = val.strip("\"'")
            continue
        if key is None:
            continue
        item = re.match(r"^\s+-\s+(.*)$", line)
        cur = fm[key]
        if item and (cur is None or isinstance(cur, list)):
            fm[key] = (cur or []) + [item.group(1).strip().strip("\"'")]
        elif cur is None:
            fm[key] = True                          # a nested mapping: hooks, mcpServers, experimental
        elif isinstance(cur, str):
            fm[key] = (cur + " " + line.strip()).strip()
    fm = {k: ("" if v is None else v) for k, v in fm.items()}
    return fm, body, None


def as_list(val):
    if isinstance(val, list):
        return val
    if isinstance(val, str):
        return [v.strip() for v in val.split(",") if v.strip()]
    return []


def in_plugin(path):
    for parent in path.resolve().parents:
        if (parent / ".claude-plugin" / "plugin.json").is_file():
            return True
        if parent.name in (".claude", "") or (parent / ".git").exists():
            return False
    return False


def check(path, plugin=None):
    text = path.read_text(encoding="utf-8")
    fm, body, err = parse(text)
    out = []

    def add(level, layer, msg):
        out.append({"level": level, "layer": layer, "message": msg})

    if err:
        add("FAIL", 2, err)
        return out
    plugin = in_plugin(path) if plugin is None else plugin

    # Shape: Claude Code silently ignores what it cannot read.
    for k in fm:
        if k not in FIELDS:
            near = difflib.get_close_matches(k, FIELDS, n=1, cutoff=0.6)
            add("FAIL", 2, f"unknown field `{k}` is silently ignored" + (f"; did you mean `{near[0]}`?" if near else ""))
    name = fm.get("name")
    if not name or name is True:
        add("FAIL", 2, "missing `name`")
    elif ":" in name or name.startswith("-") or len(name) > 256:
        add("FAIL", 2, f"invalid name `{name}`: no `:`, no leading `-`, at most 256 characters")
    desc = fm.get("description")
    if not desc or desc is True:
        add("FAIL", 2, "missing `description`: Claude routes to an agent by its description alone")
        desc = ""
    for k, allowed in ENUMS.items():
        v = fm.get(k)
        if allowed and isinstance(v, str) and v and v not in allowed:
            add("FAIL", 1 if k in ("model", "effort") else 6, f"`{k}: {v}` is not one of {sorted(allowed)}")
    model = fm.get("model")
    if isinstance(model, str) and model and model not in MODEL_ALIASES and not re.match(r"^[a-z0-9][a-z0-9.\-\[\]_]+$", model):
        add("FAIL", 1, f"`model: {model}` is neither an alias ({', '.join(sorted(MODEL_ALIASES))}) nor a model id")
    mt = fm.get("maxTurns")
    if mt is not None and not (isinstance(mt, str) and mt.isdigit() and int(mt) > 0):
        add("FAIL", 5, f"`maxTurns: {mt}` must be a positive integer")
    if fm.get("permissionMode") == "bypassPermissions":
        add("WARN", 6, "`permissionMode: bypassPermissions` removes every permission prompt for this agent")
    if plugin:
        for k in sorted(PLUGIN_IGNORED & set(fm)):
            add("WARN", 6, f"`{k}` is ignored in a plugin agent; ship hooks in hooks/hooks.json, or install the agent in .claude/agents")

    # L1 model
    if model is None:
        add("INFO", 1, "no `model`: the agent inherits the session's; set one only when evals show a smaller model passes")

    # L2 instructions
    words = len(body.split())
    if words < 40:
        add("WARN", 2, f"the prompt is {words} words: say what the agent receives, does in order, and hands back")
    elif words > 2500:
        add("WARN", 2, f"the prompt is {words} words: long prompts lose recall; move reference material to files or skills")
    if desc and not USE_WHEN.search(desc):
        add("WARN", 2, "the description never says when to use it (\"Use when ...\", \"Use proactively ...\")")
    if desc and not NOT_FOR.search(desc):
        add("WARN", 2, "the description has no \"Not for ...\" boundary, so near-miss requests can land here")

    # L3 tools
    tools, denied = as_list(fm.get("tools")), as_list(fm.get("disallowedTools"))
    if not tools and not denied:
        add("WARN", 3, "no `tools` or `disallowedTools`: the agent inherits every tool, including Bash and every MCP server")
    if tools and "Agent" in [t.split("(")[0] for t in tools]:
        add("INFO", 3, "`Agent` in tools lets it spawn subagents (up to the depth limit); type lists in Agent(...) are ignored in subagents")

    # L4 memory
    if "memory" not in fm:
        add("INFO", 4, "no `memory`: nothing survives between runs, so a multi-session job cannot resume")

    # L5 loop
    if mt is None:
        add("WARN", 5, "no `maxTurns`: nothing caps a runaway loop")
    if not STOP.search(body):
        add("WARN", 5, "the prompt never says when to stop (done, unrecoverable error, or waiting on approval)")

    # L6 guardrails
    effective = set(t.split("(")[0] for t in tools) if tools else None   # None = everything
    def has(group):
        return effective is None or bool(effective & group) or any(t.startswith("mcp__") for t in (effective or []))
    reads_untrusted = has(WEB_TOOLS)
    can_act = has(ACT_TOOLS)
    if reads_untrusted and not UNTRUSTED.search(body):
        add("WARN", 6, "it can read web or external content but never says that content is data, not instructions")
    if reads_untrusted and can_act and not APPROVAL.search(body):
        add("WARN", 6, "lethal-trifecta risk: it reads untrusted content and can act (Bash, writes or MCP) with no approval step")

    # L7 approval
    if can_act and not APPROVAL.search(body):
        add("WARN", 7, "no human approval rule: name the actions that wait for a yes (send, publish, delete, spend)")
    elif APPROVAL.search(body) and not re.search(r"\b(delet|spend|money|pay|purchas|buy)", body, re.I):
        add("INFO", 7, "the approval rule names no delete or spend actions; check those are covered")
    return out


def files_from(args):
    for a in args:
        p = Path(a)
        if p.is_dir():
            yield from sorted(p.glob("*.md"))
        else:
            yield p


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="+", help="agent .md files or folders of them")
    ap.add_argument("--plugin", action="store_true", default=None, help="treat every file as a plugin agent")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    report, fails = {}, 0
    for path in files_from(a.paths):
        if not path.is_file():
            print(f"not found: {path}", file=sys.stderr)
            return 2
        findings = check(path, plugin=a.plugin)
        report[str(path)] = findings
        fails += sum(f["level"] == "FAIL" for f in findings)
    if a.json:
        print(json.dumps(report, indent=2))
    else:
        for path, findings in report.items():
            print(f"{path}: {sum(f['level'] == 'FAIL' for f in findings)} FAIL, "
                  f"{sum(f['level'] == 'WARN' for f in findings)} WARN")
            for f in sorted(findings, key=lambda f: (["FAIL", "WARN", "INFO"].index(f["level"]), f["layer"])):
                print(f"  {f['level']:4} L{f['layer']}  {f['message']}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
