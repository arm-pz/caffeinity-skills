# Release steps: detail

## Test execution

- Source of cases: `evals/evals.json` (`skill_name` plus an `evals` list of prompts) and the tune-skill test-case table (at least eight cases, including boundary pairs).
- For each case record: id, message, expected skill or mode, result (pass, fail, reviewed-only, not-run), and a one-line note.
- Pass condition is the one written in the table. Do not invent a looser one.
- Counts go in the report. If any case is not-run, say so in the first line of the report.

## Version

- Semantic version. The first release is 0.1.0.
- Do not change an existing `version` field to a different value. Bump only when the user asks, or when a release follows a tune-skill change.
- CHANGELOG entry format:

      ## 0.1.0 (YYYY-MM-DD)
      - Initial release from prompts: N prompts, M test cases.
      - Tests: X pass, Y fail, Z reviewed-only.

## Packaging

- Archive root is the skill folder. Example: `prompts-to-skill.zip` contains `prompts-to-skill/SKILL.md`.
- Exclude `.DS_Store`, `__pycache__`, `*.pyc`, and any file under `evals/` that holds real user data.
- Verify with `unzip -l` and confirm the SKILL.md path.

## Discovery check

- Three should-trigger prompts in the user's own words, no skill name.
- One should-not-trigger prompt that shares keywords with the description.
- Judge from the description text only. Record that this was a read-through, not a live session.

## Install by platform

- Claude app or web: upload the zip through the skills settings.
- Claude Code: copy the folder into `~/.claude/skills/` or the project's `.claude/skills/`.
- Qoder: copy the folder into `~/.qoder/skills/<name>/`, then reload skills or start a new session.
- Other agents: copy into the directory that agent reads (`.agents/skills/`, `.cursor/skills/`, and similar), per its docs.
- GitHub installs: `npx skills add <owner>/<repo> --skill <name>`.
- Always end with a check: the skill appears in the agent's skill list.
