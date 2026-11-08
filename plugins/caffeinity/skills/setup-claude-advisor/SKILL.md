---
name: setup-claude-advisor
version: 0.1.0
description: >-
  Configure Claude Code for quota-optimised model tiering: Sonnet as the main session model,
  Opus as the on-call advisor, Haiku for read-only subagents, and Sonnet for code-editing
  subagents. Audits existing subagents, environment variables, and CLI version before proposing
  changes; writes settings, subagent files, and an advisory rule to CLAUDE.md only after the
  user approves a diff preview. Use when the user wants to set up the Opus advisor pattern,
  configure Claude Code model tiers, optimise their $20 plan quota by splitting models across
  roles, or match a subagent tree that assigns different models to different jobs. Not for
  diagnosing why usage already drained (use diagnose-usage), choosing an effort level before a
  task (use choose-effort), or upgrading Claude Code itself.
---

# Setup Claude Advisor

Set up Claude Code so Sonnet does the work and Opus advises at three decision points, with subagents assigned to the cheapest model that can handle their job. Every change is shown as a diff first; nothing is written until the user says go.

## Ground rules

- **Show first, write never.** Collect every proposed change into a single diff preview. Do not edit any file until the user explicitly approves. If the user says "show me the changes first", stop after the preview.
- **Reuse before creating.** Scan `~/.claude/agents` and `.claude/agents` for existing subagent files. Propose a new file only when no existing one covers the role. List any existing subagent that already sets a model you would not have chosen, and leave it alone.
- **Report without touching.** Environment variables and the CLI version are diagnostic. Read and report them; never modify them.
- **Name the sibling.** If the user's real problem is post-mortem usage analysis, say "that is `diagnose-usage`" and stop. If they want a per-task effort recommendation, say "that is `choose-effort`" and stop.

## Workflow

### 1. Pre-flight diagnostics

Run these checks and present the results in a single report block before proposing anything:

1. **Claude Code version.** Run `claude --version` (or the installed equivalent). If the version is older than 2.1.293, warn: "In versions before 2.1.293, `haiku` still resolved to Haiku 4.5 instead of the current Haiku. Upgrade before applying these changes." Do not upgrade it.
2. **Environment variables.** Check and report (do not change):
   - `CLAUDE_CODE_DISABLE_ADVISOR_TOOL` — disables the advisor if set.
   - `DISABLE_TELEMETRY` — can block flag fetching, which disables the advisor indirectly.
   - `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` — forces every subagent onto one model, overriding per-file settings.
   - Any other variable whose name contains `ADVISOR` or `SUBAGENT`.
3. **Existing subagents.** List every `.md` file in `~/.claude/agents` and `.claude/agents` (if they exist). For each, extract the `model:` line. Classify into three buckets:
   - **Reusable as-is**: role and model match the target tree.
   - **Reusable, different model**: role fits but `model:` is set to something other than the target. **Leave these alone** and list them with a note.
   - **Missing**: no existing file covers the role. Propose a new one.
4. **Existing settings.** Read `~/.claude/settings.json` if it exists. Note the current `model` and `advisorModel` values.

### 2. Propose the subagent tree

The target tree has three subagent roles. For each missing role, draft a subagent markdown file. Read `references/advisor-architecture.md` for the role definitions, model assignments, and the rationale.

| Role | Model | Job |
|---|---|---|
| Code reader / searcher | `haiku` | Read files, grep, search docs. No edits. |
| Documentation lookup | `haiku` | Fetch and summarise API docs, READMEs, changelogs. No edits. |
| Code editor / test runner | `sonnet` | Edit files, run tests, execute commands. |

### 3. Propose settings changes

Draft the `~/.claude/settings.json` patch:

```json
{
  "model": "sonnet",
  "advisorModel": "opus"
}
```

Merge with existing keys; do not drop any key the user already has.

### 4. Draft the advisory rule

Propose appending this block to `~/.claude/CLAUDE.md` (create the file if it does not exist):

```markdown
## Advisor protocol

Ask the advisor (`/advisor`) at exactly three moments:
1. **Before committing to a plan.** After outlining a multi-step approach, ask: "Is this the right plan?"
2. **When the same error recurs.** If the same error appears a second time after a fix attempt, ask: "Am I heading the wrong way?"
3. **Before declaring done.** Before telling the user the task is complete, ask: "Did I miss anything?"

Do not call the advisor for routine edits, single-file fixes, or questions you can answer from context.
```

### 5. Present the diff preview

Combine all proposed changes into a single fenced diff block:

- `~/.claude/settings.json` — before/after
- Each new subagent file — full contents
- `~/.claude/CLAUDE.md` — the appended block
- Existing subagents left unchanged — listed with reason

End with: **"These are the proposed changes. Say 'apply' to write them, or tell me what to adjust."**

### 6. Apply (only on explicit approval)

If the user says "apply", "go", "do it", or equivalent:

1. Write or merge `~/.claude/settings.json`.
2. Write each new subagent file to `~/.claude/agents/`.
3. Append the advisor rule to `~/.claude/CLAUDE.md`.
4. Confirm each file written with its full path.

If the user said "show me the changes first" or "don't edit any files yet", **stop after step 5**. This is the most common invocation and it is complete at the preview.

### 7. Launch command

After applying (or as part of the preview), show the launch command:

```bash
claude --model sonnet --advisor opus
```

Explain: "This starts a session with Sonnet as the working model and Opus available via `/advisor`. Sonnet writes the code; Opus reads the full session and gives strategic advice when called."

## Hand off

- Wording pressure, trigger overlap, or test cases → `tune-skill` receives this skill folder.
- README, version, install checklist → `prompts-to-skill-release` receives the validated folder.
- Usage diagnosis after a session → `diagnose-usage` receives the user's `/usage` paste.
- Effort level selection before a task → `choose-effort` receives the task description.

## Report

Short. Skill name and path. Pre-flight results (version, flags, existing subagents). Files proposed versus files written. One next step.
