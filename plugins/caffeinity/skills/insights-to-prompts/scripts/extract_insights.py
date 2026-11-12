#!/usr/bin/env python3
"""Build a prompt-friction digest from Claude Code /insights data.

Reads (all optional, whatever exists):
  <usage-dir>/facets/*.json        per-session facets cached by /insights
  <usage-dir>/session-meta/*.json  per-session metadata (newer builds)
  <usage-dir>/report.html          the rendered report
  <projects-dir>/**/*.jsonl        raw session transcripts (user prompts)
  --skills-dir <dir>               skill folders, to map friction onto skill use

Writes a JSON digest (--out) and prints a markdown summary to stdout.
Standard library only.
"""
import argparse
import html
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path

PROMPT_FRICTION = {
    "misunderstood_request", "user_unclear", "wrong_approach",
    "excessive_changes", "wrong_file_or_location", "user_rejected_action",
}
NOT_PROMPT = {"tool_failed", "external_issue", "claude_got_blocked", "buggy_code", "slow_or_verbose"}
WEAK_OUTCOMES = {"not_achieved", "partially_achieved"}
SKIP_PREFIXES = ("<local-command", "<command-message", "Caveat:", "<system-reminder", "[Request interrupted")
CMD_RE = re.compile(r"<command-name>\s*/?([\w:.-]+)\s*</command-name>(?:.*?<command-args>(.*?)</command-args>)?", re.S)


def load_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def text_of(content):
    """User message content -> plain text, or None if it is only tool results."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = [c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text"]
        return "\n".join(p for p in parts if p) or None
    return None


def read_transcripts(projects_dir, since):
    sessions = defaultdict(lambda: {"prompts": [], "commands": [], "project": None})
    for path in Path(projects_dir).glob("**/*.jsonl"):
        if path.name.startswith("agent-"):
            continue
        try:
            if path.stat().st_mtime < since:
                continue
            lines = path.open(encoding="utf-8", errors="replace")
        except OSError:
            continue
        with lines:
            for line in lines:
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                if rec.get("type") != "user" or rec.get("isMeta") or rec.get("isSidechain"):
                    continue
                msg = rec.get("message") or {}
                txt = text_of(msg.get("content"))
                if not txt:
                    continue
                sid = rec.get("sessionId") or path.stem
                s = sessions[sid]
                s["project"] = s["project"] or path.parent.name
                m = CMD_RE.search(txt)
                if m:
                    s["commands"].append(m.group(1))
                    args = (m.group(2) or "").strip()
                    if args:
                        s["prompts"].append(f"/{m.group(1)} {args}")
                    continue
                if txt.lstrip().startswith(SKIP_PREFIXES):
                    continue
                s["prompts"].append(txt.strip())
    return sessions


class ReportParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections, self.current, self.skip, self.in_head = {}, "Intro", 0, False
        self.buf = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        elif tag in ("h1", "h2", "h3"):
            self._flush()
            self.in_head = True
            self.buf = []

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        elif tag in ("h1", "h2", "h3") and self.in_head:
            self.current = " ".join("".join(self.buf).split()) or self.current
            self.in_head = False
            self.buf = []
        elif tag in ("p", "li", "div", "pre", "code", "tr"):
            self.buf.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.buf.append(data)

    def _flush(self):
        text = re.sub(r"\n\s*\n+", "\n", "".join(self.buf)).strip()
        if text:
            prev = self.sections.get(self.current, "")
            self.sections[self.current] = (prev + "\n" + text).strip()

    def close(self):
        super().close()
        self._flush()


def read_report(path):
    if not path.exists():
        return None
    p = ReportParser()
    p.feed(html.unescape(path.read_text(encoding="utf-8", errors="replace")))
    p.close()
    age_days = round((time.time() - path.stat().st_mtime) / 86400, 1)
    keep = {k: v[:4000] for k, v in p.sections.items() if len(v) > 40}
    return {"path": str(path), "age_days": age_days, "sections": keep}


def norm_opener(prompt):
    words = re.sub(r"[`'\"*_#>\[\](){}]", " ", prompt.lower()).split()
    return " ".join(words[:6])


def skill_names(dirs):
    names = set()
    for d in dirs:
        for skill_md in Path(d).expanduser().glob("**/SKILL.md"):
            m = re.search(r"^name:\s*(\S+)", skill_md.read_text(encoding="utf-8", errors="replace"), re.M)
            names.add(m.group(1) if m else skill_md.parent.name)
    return names


def main():
    home = Path.home() / ".claude"
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--usage-dir", default=str(home / "usage-data"))
    ap.add_argument("--projects-dir", default=str(home / "projects"))
    ap.add_argument("--skills-dir", action="append", default=[])
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--out", default="insights-digest.json")
    a = ap.parse_args()

    usage = Path(a.usage_dir).expanduser()
    since = time.time() - a.days * 86400
    facets = {}
    for f in (usage / "facets").glob("*.json"):
        data = load_json(f)
        if isinstance(data, dict):
            facets[data.get("session_id") or f.stem] = data
    meta = {}
    for f in (usage / "session-meta").glob("*.json"):
        data = load_json(f)
        if isinstance(data, dict):
            meta[data.get("session_id") or f.stem] = data
    sessions = read_transcripts(Path(a.projects_dir).expanduser(), since) if Path(a.projects_dir).expanduser().exists() else {}
    report = read_report(usage / "report.html")

    if not facets and not sessions and not report:
        sys.exit(f"No /insights data found under {usage} or transcripts under {a.projects_dir}. Run /insights first.")

    friction_totals, prompt_friction, other_friction = Counter(), [], Counter()
    for sid, fc in facets.items():
        counts = fc.get("friction_counts") or {}
        friction_totals.update({k: int(v) for k, v in counts.items() if isinstance(v, (int, float))})
        hits = {k: v for k, v in counts.items() if k in PROMPT_FRICTION and v}
        for k, v in counts.items():
            if k not in PROMPT_FRICTION and v:
                other_friction[k] += int(v)
        if not hits:
            continue
        s = sessions.get(sid, {})
        prompts = s.get("prompts") or []
        first = prompts[0] if prompts else (meta.get(sid, {}).get("first_prompt") or "")
        score = sum(hits.values()) + (2 if fc.get("outcome") in WEAK_OUTCOMES else 0)
        prompt_friction.append({
            "session_id": sid,
            "project": s.get("project"),
            "score": score,
            "friction": hits,
            "friction_detail": fc.get("friction_detail", ""),
            "outcome": fc.get("outcome"),
            "satisfaction": fc.get("user_satisfaction_counts", {}),
            "goal": fc.get("underlying_goal", ""),
            "summary": fc.get("brief_summary", ""),
            "first_prompt": first[:1500],
            "follow_ups": [p[:400] for p in prompts[1:6]],
            "commands": s.get("commands", []),
        })
    prompt_friction.sort(key=lambda r: -r["score"])

    friction_sids = {r["session_id"] for r in prompt_friction}
    openers = defaultdict(list)
    for sid, s in sessions.items():
        for p in s["prompts"]:
            if len(p) >= 12:
                openers[norm_opener(p)].append((sid, p))
    repeated = []
    for key, items in openers.items():
        sids = {sid for sid, _ in items}
        if len(items) >= 3:
            repeated.append({
                "opener": key,
                "count": len(items),
                "sessions": len(sids),
                "sessions_with_prompt_friction": len(sids & friction_sids),
                "examples": [p[:300] for _, p in items[:3]],
            })
    repeated.sort(key=lambda r: (-r["sessions_with_prompt_friction"], -r["count"]))

    skill_friction = []
    names = skill_names(a.skills_dir)
    if names:
        by_skill = defaultdict(lambda: {"invocations": 0, "friction_sessions": [], "friction": Counter()})
        for sid, s in sessions.items():
            used = {c.split(":")[-1] for c in s["commands"]} & names
            text = " ".join(s["prompts"]).lower()
            used |= {n for n in names if n.lower() in text}
            for n in used:
                by_skill[n]["invocations"] += 1
                fc = (facets.get(sid) or {}).get("friction_counts") or {}
                if any(fc.get(k) for k in PROMPT_FRICTION):
                    by_skill[n]["friction_sessions"].append(sid)
                    by_skill[n]["friction"].update({k: int(v) for k, v in fc.items() if k in PROMPT_FRICTION and v})
        for n, d in by_skill.items():
            skill_friction.append({"skill": n, "invocations": d["invocations"],
                                   "friction_sessions": d["friction_sessions"], "friction": dict(d["friction"])})
        skill_friction.sort(key=lambda r: (-len(r["friction_sessions"]), -r["invocations"]))

    digest = {
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "window_days": a.days,
        "sources": {"facets": len(facets), "session_meta": len(meta), "transcripts": len(sessions),
                    "report": bool(report)},
        "report": report,
        "friction_totals": dict(friction_totals.most_common()),
        "not_prompt_friction": dict(other_friction.most_common()),
        "prompt_friction": prompt_friction,
        "repeated_prompts": repeated[:25],
        "skill_friction": skill_friction,
    }
    Path(a.out).write_text(json.dumps(digest, indent=2, ensure_ascii=False), encoding="utf-8")

    out = ["# Insights digest", ""]
    src = digest["sources"]
    out.append(f"Sources: {src['facets']} facets, {src['transcripts']} transcripts, "
               f"report {'%s days old' % report['age_days'] if report else 'missing'}.")
    if report and report["age_days"] > 7:
        out.append("WARNING: report.html is over 7 days old - ask the user to re-run /insights.")
    out += ["", "## Friction totals"]
    out += [f"- {k}: {v}{'' if k in PROMPT_FRICTION else '  (not a prompt problem)'}"
            for k, v in friction_totals.most_common()] or ["- none recorded"]
    out += ["", f"## Top prompt-friction sessions ({len(prompt_friction)})"]
    for r in prompt_friction[:10]:
        out.append(f"- [{r['score']}] {r['session_id'][:8]} {', '.join(r['friction'])} | {r['outcome']} | "
                   f"{(r['first_prompt'] or r['goal'])[:100]!r}")
    out += ["", f"## Repeated openers ({len(repeated)})"]
    for r in repeated[:8]:
        out.append(f"- x{r['count']} ({r['sessions_with_prompt_friction']} with friction): {r['opener']!r}")
    if skill_friction:
        out += ["", "## Skills"]
        for r in skill_friction[:10]:
            out.append(f"- {r['skill']}: {r['invocations']} uses, {len(r['friction_sessions'])} with friction {r['friction']}")
    out += ["", f"Full digest: {os.path.abspath(a.out)}"]
    print("\n".join(out))


if __name__ == "__main__":
    main()
