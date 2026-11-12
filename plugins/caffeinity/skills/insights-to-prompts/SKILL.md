---
name: insights-to-prompts
description: Turn a Claude Code /insights report into before/after rewrites of the prompts that caused friction — both the prompts you type in sessions and the prompt text inside your own skills. Reads ~/.claude/usage-data (report.html, cached facets) plus session transcripts with a bundled script, ranks friction that better wording could have prevented, and rewrites the worst offenders. Use when the user says "improve my prompts from insights", "what am I prompting badly", "turn my insights report into better prompts", "coach my Claude Code prompting", or "why does Claude keep misreading me". Not for adding rules to CLAUDE.md, hooks or settings (use harness-audit), rewriting one prompt pasted in chat with no report behind it (use a sharpen-prompt skill), or building a new skill from prompts (use prompts-to-skill).
---

# Insights to prompts

`/insights` already diagnoses your sessions. What it does not do is rewrite the prompts behind the friction — it turns repeated instructions into CLAUDE.md rules and offers a few generic "copyable prompts". This skill closes that gap: every rewrite it produces is tied to a session where the original wording cost a correction, a redo or a rejected action.

## Ground rules

- **Evidence or nothing.** Each rewrite cites the session(s) and friction type behind it. A prompt with no friction attached is not rewritten, however rough it reads — rewriting prompts that worked is churn.
- **Fix only what wording can fix.** `tool_failed`, `external_issue` and most `buggy_code` are not prompt problems. Say so and leave them out; padding the list with them makes the real findings harder to act on.
- **Rules belong in CLAUDE.md, asks belong in prompts.** If the fix is "say this every time", it is a CLAUDE.md rule — hand it to harness-audit instead of baking it into every prompt.
- **Keep the user's voice and length budget.** A rewrite that triples the prompt gets ignored. Add the missing piece (scope, done-condition, constraint), not boilerplate.
- **Never edit a skill file without approval.** Skill-prompt fixes are shown as diffs first.

## Workflow

### 1. Get a fresh report

You cannot run `/insights` yourself; it is a built-in command. Check the age of `~/.claude/usage-data/report.html`. If it is missing or older than 7 days, ask the user to run `/insights` and wait. If they can't, continue from cached facets and say the report sections are missing.

### 2. Extract the digest

    python3 scripts/extract_insights.py --out insights-digest.json

Defaults read `~/.claude/usage-data` and `~/.claude/projects`. Add `--skills-dir <folder>` (repeatable) to also map friction onto skill invocations. The script prints a short markdown summary and writes the full JSON; read the summary first and open the JSON only for the sessions you rewrite. Every field it produces is described in `references/digest-format.md` — open that when a field is unclear.

### 3. Pick the targets

From the digest take, in order:

1. `prompt_friction` sessions (misunderstood_request, user_unclear, wrong_approach, excessive_changes, wrong_file_or_location, user_rejected_action) — ranked by count and by outcome below `mostly_achieved`.
2. `repeated_prompts` — openers typed three or more times. Frequent + friction is the top priority; frequent + no friction is a slash-command candidate, not a rewrite.
3. `skill_friction` — only when `--skills-dir` was given.

Cap the report at about ten rewrites. More than that and none get adopted.

### 4. Rewrite

Open `references/rewrite-rules.md` for the friction→fix table and the output block. For each target: quote the original prompt (truncated to its first ~200 characters), name the friction and its evidence, write the rewrite, and add one line on what changed.

For skill prompts, follow `references/skill-prompts.md`: the fix goes into the SKILL.md body or its description, shown as a diff.

### 5. Deliver

One markdown report, `prompt-rewrites.md`, in this order: a three-line summary of the patterns, the rewrites, then a short "not a prompt problem" list and a "send to harness-audit" list. Offer to apply skill diffs; never apply them unasked.

## Report

Short. Report age and sessions covered. Rewrites made, split session vs skill. What was handed to harness-audit. One habit to change first.
