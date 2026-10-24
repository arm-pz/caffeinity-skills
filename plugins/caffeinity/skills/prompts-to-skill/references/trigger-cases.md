# Trigger cases for prompts-to-skill

Written to the format in tune-skill's `references/test-cases.md`. The skill under test is
`prompts-to-skill`, judged from its `description` frontmatter only, as an agent deciding what to
load would. Competing descriptions read: `draft-skill`, `tune-skill`,
`prompts-to-skill-release`, `findable`, `skill-launch`, and Qoder's built-in `skill-creator`.

**Run:** hand-run on 2026-10-19 against the descriptions only. Gate B in
`references/gates.md` cannot pass on written-only cases, so it stays "passed by review, not run"
for anything below that was not executed against a real agent.

## Cases

| # | Message | Expected skill | Pass condition | Result |
| --- | --- | --- | --- | --- |
| 1 | "make this into a skill" + eight pasted prompts | prompts-to-skill | confirms intent (point 1) before drafting anything | PASS ("make a skill from these") |
| 2 | "Turn these into a skill." + a markdown file of example requests | prompts-to-skill | counts the prompts first; with fewer than three, asks for more instead of drafting | PASS ("turn these into a skill") |
| 3 | "I give the agent the same five instructions every week. Bundle them." | prompts-to-skill | runs the installed-skill overlap check before drafting | PASS ("a list of prompts, instructions, or example requests") |
| 4 | (a batch of prompts pasted with no instruction at all) | prompts-to-skill | asks what outcome the user wants rather than assuming | PASS ("paste a batch of prompts with no further instruction") |
| 5 | "These megaprompts work well, and I want them as one installable capability." | prompts-to-skill | drives draft-skill at step 1 rather than re-drafting by hand | PASS |
| 6 | "I have an idea for a skill but no prompts." | draft-skill | prompts-to-skill does not load | PASS ("… creating a skill from a plain description with no prompts") |
| 7 | "This skill triggers on the wrong requests." (an existing skill) | tune-skill | prompts-to-skill does not load | PASS ("Not for editing an existing skill") |
| 8 | "Is there already a skill that does this?" | the agent's skill list / find-extensions | prompts-to-skill does not load | PASS ("Not for finding existing skills for a task") |
| 9 | "Make a skill from these prompts and publish it to GitHub." | prompts-to-skill → prompts-to-skill-release | the first pass stops at Gate A/B and hands over; packaging is not folded in | FAIL: prompts-to-skill step 4 optionally invokes `findable` for the name and listing, so "publish" has two plausible owners (findable here, prompts-to-skill-release next door). No description says which |
| 10 | "I have a prompt list and want it from zero to published." | either prompts-to-skill or `skill-launch` | one owner for a prompt-list input | FAIL: `skill-launch`'s `argument-hint` is "[skill idea \| prompt list]", so it claims the batch input while its description only describes an idea, and it chains draft-skill → tune-skill → findable-polish, skipping prompts-to-skill entirely |

Nine of ten would route correctly. Cases 9 and 10 are ours to fix.

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "A plain description, no prompts: make a skill" | draft-skill | idea is the input |
| "A list of prompts: make a skill" | prompts-to-skill | prompt list is the input |
| "Package the skill you just made" | prompts-to-skill-release | drafting and tuning are done |
| "The packaged skill misfires" | tune-skill | an existing skill, regardless of how it got there |
| "Make the repo findable" | findable | listing, not behaviour |
| "Name the repo and list it, as part of packaging these prompts" | prompts-to-skill (step 4, optional) | findable is called from inside, not instead |

Spans the family: "here are my prompts: make a skill, get it tested and installable, and put it on
GitHub" → `prompts-to-skill` (intent, overlap, draft, cases, tune; Gate A + Gate B), hand back the
skill folder plus the gate results, then `prompts-to-skill-release` (zip, tests recorded, README,
version, install checklist), then `findable` only if the user still wants listing work. Nothing
should jump straight to release: its precondition 2 requires the recorded gates.

## Fixes applied 2026-10-19

- `skill-launch` no longer claims the batch: its `argument-hint` is `[skill idea]`, its description
  adds "not for a batch of prompts the user already wrote (use prompts-to-skill)", and its Phase 1
  stops and hands over when the input is a prompt list.
- Step 4 here now names one owner per phase: listing copy `findable`, packaging and install
  checklist `prompts-to-skill-release`, pushing an existing clone `upstream-check`.

## Not verified

- Whether the dependencies resolve in practice: `npx skills add arm-pz/draft-skill` and
  `arm-pz/tune-skill` were never run from a clean machine.
- The <three-prompt guard, the safety screen, and the overlap check are written as instructions;
  no case above exercised them against a real agent.
