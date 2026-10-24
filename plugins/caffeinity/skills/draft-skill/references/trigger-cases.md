# Trigger cases for draft-skill

Written to the format in tune-skill's `references/test-cases.md`. The skill under test is
`draft-skill`, judged only from its `description` frontmatter, as an agent would when deciding
what to load. Competing descriptions read for these cases: `tune-skill`, `prompts-to-skill`,
`prompts-to-skill-release`, `findable`, `skill-launch`, `tune-and-polish`, `upstream-check`, and
the Qoder built-in `skill-creator`.

**Run:** hand-run on 2026-10-19 against the descriptions only. No automated triggering loop was
run; none exists in this environment for these skills.

## Cases

| # | Message | Expected skill | Pass condition | Result |
| --- | --- | --- | --- | --- |
| 1 | "Make me a skill that follows our internal deploy runbook instead of me re-explaining it every time." | draft-skill | asks for purpose, output and trigger phrases and waits for a yes before writing any file | PASS |
| 2 | "Scaffold a new skill for summarising WhatsApp client threads." | draft-skill | creates the folder, `SKILL.md` and only the resource dirs that earn their place | PASS |
| 3 | "I want an agent to check every outbound refund email against our policy, repeatably. Design that as a skill." | draft-skill | names what belongs in scripts vs references vs assets before writing | PASS |
| 4 | "There's an empty folder at `~/.qoder/skills/invoice-parser`. Fill it in." | draft-skill | confirms intent first; does not drop a template into the folder | PASS |
| 5 | "Every time I ask the agent to format a transcript it gets the headings wrong. Can you make that stick?" | draft-skill | picks drafting over tuning, because no skill exists yet | FAIL: reads equally like an existing skill misbehaving (`tune-skill`: "fires on the wrong requests"). Nothing in either description says what to do when the *behaviour* is wrong but no skill file exists |
| 6 | "Here are six prompts I keep pasting. Package them as one skill." | prompts-to-skill | does not load draft-skill | PASS (explicit "Not for turning a batch of existing prompts into a skill") |
| 7 | "My `tune-skill` description is too long, tighten it." | tune-skill | does not load draft-skill | PASS |
| 8 | "Write a README for my skill repo so people can find it." | findable | does not load draft-skill | PASS |
| 9 | "Build a skill that does X" on a machine that also has Qoder's built-in `skill-creator`. | draft-skill alone | only one authoring skill loads | FAIL: `skill-creator`'s description ("users want to create a new skill") claims the same request. Both can load; the built-in cannot be edited from this repo |

Eight of nine cases would route correctly if `skill-creator` were absent; the collisions that are
ours to fix are cases 5 and 9.

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "I have an idea for a skill, no prompts" | draft-skill | idea is the input |
| "I have a list of prompts, make a skill" | prompts-to-skill | prompt list is the input |
| "This skill triggers on the wrong things" | tune-skill | an existing skill is edited, not written |
| "Write me a new skill" | draft-skill | nothing exists yet |
| "Make this skill installable, with a version and README" | prompts-to-skill-release | behaviour is settled, packaging is the job |
| "Publish my finished skill to GitHub" | prompts-to-skill-release + `upstream-check` for the push | draft-skill must not claim release |

Spans both: "turn these prompts into a skill and get it ready to install" → start
`prompts-to-skill` (it invokes draft-skill at step 1), hand over at Gate B, finish in
`prompts-to-skill-release`. draft-skill should not be picked directly.

## Not verified

- Whether `npx skills add arm-pz/draft-skill --skill draft-skill` resolves on a clean machine.
- Real model behaviour. These are description-level judgements, not triggering runs.
