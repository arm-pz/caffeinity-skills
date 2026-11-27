# Trigger cases for skills-to-dynamic-workflow

Written to tune-skill's case format (`references/test-cases.md` in arm-pz/tune-skill). Judged from
the `description` frontmatter only. Competing descriptions read: `workflow-router`,
`prompts-to-workflow`, `skill-to-mod`, `draft-skill`, `skill-estate`.

**Run:** written 2026-11-27 and hand-checked against the descriptions; none run yet.

| # | Message | Expected skill | Pass condition | Result |
| --- | --- | --- | --- | --- |
| 1 | "Turn Workflow 3 launch-safely into a Claude Code dynamic workflow." | skills-to-dynamic-workflow | writes `workflows/launch-safely.js`, lanes then a gate | written |
| 2 | "I want consistent-code-review then address-findings to run as one /command." | skills-to-dynamic-workflow | a two-step chain, push and comment proposed, not taken | written |
| 3 | "Make my skill-builder agent into an ultracode script I can rerun." | skills-to-dynamic-workflow | ports the agent's skills in order | written |
| 4 | "Save these four skills as a workflow in .claude/workflows." | skills-to-dynamic-workflow | project location, `/<name>` | written |
| 5 | "Automate my land-a-job chain so the agents run in the background." | skills-to-dynamic-workflow (implicit) | chain with resume points at each choice | written |
| 6 | "Which skills do I run to get my site ready to launch?" | workflow-router | skills-to-dynamic-workflow does not load | written |
| 7 | "Here are 6 prompts I paste every week; make them a workflow." | prompts-to-workflow | skills-to-dynamic-workflow does not load | written |
| 8 | "Run web-preflight automatically before every deploy." | skill-to-mod | skills-to-dynamic-workflow does not load | written |
| 9 | "Use a workflow to audit every route in src/routes for auth checks." | none (Claude Code ultracode) | skills-to-dynamic-workflow does not load: no skills behind it | written |

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "Make this chain of skills a dynamic workflow." | skills-to-dynamic-workflow | skills exist, the ask is the script |
| "Make these prompts a chain of skills." | prompts-to-workflow | the skills do not exist yet |
| "Run this skill on every git push." | skill-to-mod | an event, not a background run |
| "What order should these skills run in?" | workflow-router | the order, not the script |
