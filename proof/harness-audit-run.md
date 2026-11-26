# harness-audit: real run

- **Date:** 2026-11-13
- **Target repo:** `arm-pz/caffeinity-skills` (branch `claude/harness-audit-proof-x3lxsl`, base commit `af1c597`)
- **Skill:** `arm-pz/harness-audit`, installed with `npx skills add arm-pz/harness-audit`. The installed copy is byte-identical to `plugins/caffeinity/skills/harness-audit` (checked with `diff -r`).
- **Scripts run:** `scripts/inventory.py` (with and without `~/.claude`) and `scripts/mine_sessions.py`, once before the change and once after.
- **Environment:** an ephemeral Claude Code cloud container running Python 3.13.18.

Every number below is copied from script or shell output. None are rounded or estimated.

## Summary

```text
$ harness-audit arm-pz/caffeinity-skills
inventory   instruction files: 0 (0 lines)   rules: 0   hooks: 0   mcp: 0
            project skills: 0                user skills: 19 (2465 lines)
sessions    1 transcript · 1 user message · 0 correction candidates
checks      1 missed-corrections   pass (n=1, INCONCLUSIVE)
            2 unproven-rules       pass (no rules)
            3 file-size            pass (no instruction files)
            4 tool/skill-load      FINDING  overlap -> handoff tune-skill
                                   FINDING  duplicate install -> trial-remove
            5 unenforced-prose     pass (no rules)
            6 drift                pass (no references)
score       5/6
applied     1 of 1 proposed diff (.gitignore)
untracked   3 -> 0
```

## Before and after

| Metric | Before | After |
|---|---|---|
| Instruction files (CLAUDE.md, AGENTS.md, …) | 0 files, 0 lines | 0 files, 0 lines |
| Project `.claude/` settings / rules / commands / agents | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| Rules: total / duplicated / conflicting / stale refs / unfollowable | 0 / 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 / 0 |
| Hooks (inventory count) | 0 | 0 |
| MCP servers in config | 0 | 0 |
| Project skills (inventory count) | 0 | 0 |
| User-level skills | 19 (2465 lines) | 19 (2465 lines) |
| Untracked harness files in `git status` | 3 (`.agents/skills/`, `.claude/`, `skills-lock.json`) | 0 (ignored) |
| Sessions mined / user messages / correction candidates | 1 / 1 / 0 | 1 / 2 / 0 |
| Score | 5/6 | 5/6 |

The repo has no agent harness of its own. The ~60 `SKILL.md` files under `plugins/` and `mods/` are what the repo ships; they don't configure an agent working on this repo. So the audit found nothing in the repo to prune. The one change it applied stops a duplicate skill install from being committed.

## Three most telling findings

1. **Three loaded skills overlap: `skill-creator`, `draft-skill`, `tune-skill`.** This is check 4, with action `handoff` to `tune-skill`.
   - `skill-creator/SKILL.md:3` claims "create a skill from scratch" and "optimize a skill's description for better triggering accuracy". Those overlap `draft-skill/SKILL.md:3` ("Create a new agent skill") and `tune-skill/SKILL.md:3` ("fine-tune… so it triggers").
   - `skill-creator` has no "Not for" boundary.
   - All three are account-synced skills outside this repo, so the fix wasn't applied here.
2. **The audit's own inventory doesn't see skills installed by `npx skills add`.** This is a blind spot in the tool.
   - The installer links the skill into Claude Code as a symlinked folder: `.claude/skills/harness-audit → ../../.agents/skills/harness-audit`.
   - `inventory.py` uses `Path.rglob`, which doesn't follow symlinked folders. `rglob("SKILL.md")` returned `[]`, while `rglob("SKILL.md", recurse_symlinks=True)` returned the skill.
   - The project skill count therefore reads 0 when the true count is 1. The fix belongs upstream in `arm-pz/harness-audit`.
3. **The install would have added a second, identical copy of a skill the repo already ships.** This is check 4, `remove-tool`, downgraded to `trial-remove` because fewer than 10 sessions were mined.
   - `.agents/skills/harness-audit` and `plugins/caffeinity/skills/harness-audit` are byte-identical (87-line `SKILL.md`).
   - **Applied:** `.gitignore` now ignores `.agents/skills/`, `.claude/skills/` and `skills-lock.json`.

```diff
--- a/.gitignore
+++ b/.gitignore
@@ -1,3 +1,7 @@
 __pycache__/
 *.pyc
 plugins/caffeinity/evals/results/
+# local skill installs (npx skills add); the repo ships these under plugins/
+.agents/skills/
+.claude/skills/
+skills-lock.json
```

## INCONCLUSIVE

- **Check 1, missed corrections.** The only transcript was this session. The container is ephemeral, so there was no earlier history to mine. A pass on a sample of one session proves nothing.
- **Check 4, tool usage.** One session is too small a sample to call any skill or tool unused. No usage-based removals were made.
- **Hooks.** The inventory reports 0, but the runtime has 2 hooks (SessionStart and Stop) in `~/.claude/launcher-settings.json`, which `inventory.py` doesn't read. Those hooks are set by the cloud environment, not by this repo, so they weren't audited.
- **Project skill count.** The 0 in the table is undercounted because of finding 2.
- **Checks 2, 3, 5 and 6 pass only because there was nothing to check.** No rules or instruction files exist, so these passes say nothing about how well the skill prunes a real harness.
