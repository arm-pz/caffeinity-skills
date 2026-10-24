# Gates

## Gate A: structure (must pass)

| Check | Pass condition |
| --- | --- |
| Folder and name | Folder name, frontmatter `name`, and H1 are identical, lowercase, hyphenated |
| Description length | Under 1024 characters; aim for 950 or less |
| Trigger wording | Description says what it does and when to use it |
| Boundary wording | Description has a "Not for" clause naming the owning sibling |
| Body length | SKILL.md under about 500 lines |
| References | Every referenced file exists |
| Script | `check_skill.py` run with no FAIL |

## Gate B: triggering (must pass)

| Check | Pass condition |
| --- | --- |
| Original prompts | Each original prompt would trigger the skill, or the report states why one would not |
| Test cases | At least eight, covering clear, implicit, and near-miss cases |
| Boundary pairs | Each boundary has one case on each side |
| Results | Each case is marked pass, fail, or written-not-run, with counts reported |

Gate B cannot pass on written-only cases. If the cases cannot be run in this environment, the report must say so, and the gate is marked "passed by review, not run."

## Failure handling

- Fix the item, re-run the check, and record the change.
- If a fix conflicts with the user's intent, stop and ask.
- Never report a skill as complete while a gate is failing.
