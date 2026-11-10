# Trigger cases for tune-and-ship

Written to tune-skill's case format (`references/test-cases.md` in arm-pz/tune-skill). Judged from
the `description` frontmatter only. Competing descriptions read from their SKILL.md files on
2026-11-10: `tune-skill`, `tune-and-polish`, `findable-polish`, `skill-launch`, `skill-estate`,
`upstream-check`, `prompts-to-skill-release`. `caffeinity-routing` was read for the Descale brew
table only.

**Run:** written 2026-11-10 and hand-checked against the descriptions. No automated triggering run.

| # | Message | Expected skill | Pass condition | Result |
| --- | --- | --- | --- | --- |
| 1 | "Fine-tune my other skills on skillsmith.tech, one by one." | tune-and-ship | runs the queue, names one target | hand-checked |
| 2 | "Give research-brief the full treatment and get it live." | tune-and-ship | one skill, ends with a draft PR | hand-checked |
| 3 | "Fact-check the claims in my choose-effort skill and release the fix." | tune-and-ship | fact-check table, version bump, PR | hand-checked |
| 4 | "Which of my skills is next? Do it like the last one." | tune-and-ship | reads the ledger, picks the next row | hand-checked |
| 5 | "The numbers in that skill look made up. Sort it out and publish it." | tune-and-ship | implicit: fact check plus release | hand-checked |
| 6 | "My tune-skill isn't triggering." | tune-skill | tune-and-ship does not load | hand-checked |
| 7 | "Draft better trigger wording and a better About line, don't push anything." | tune-and-polish | tune-and-ship does not load | hand-checked |
| 8 | "Run this week's maintenance on the skills." | caffeinity-routing (Brew 10 · Descale) | tune-and-ship does not load | hand-checked |
| 9 | "I have an idea for a new skill, take it to published." | skill-launch | tune-and-ship does not load | hand-checked |
| 10 | "Audit all 40 of my skill repos and wire up publishing." | skill-estate | tune-and-ship does not load | hand-checked |

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "Tune this skill and ship it." | tune-and-ship | ends in a release and a live page |
| "Tune this skill." | tune-skill | no release asked for |
| "Fix the triggering and polish the listing." | tune-and-polish | drafts both halves, pushes nothing |
| "Go through my catalog and improve each skill properly." | tune-and-ship | one at a time, each shipped |
| "The nightly health issue is open, fix what regressed." | caffeinity-routing | regression-driven upkeep |
| "Is my site listing the same skills as GitHub?" | upstream-check | one drift question |
| "Tune all my skills." | tune-and-ship, after asking once whether each should be released | ambiguous between a family tune and a shipped sweep |

## Not verified

- Real model behaviour for triggering. These are description-level judgements.
- The overlap with `tune-and-polish` is the closest one: both run tune-skill then findable-polish.
  The split is that this skill fact-checks, releases and confirms, and that one drafts and stops.
  No live session has tested whether "tune and polish X" stays with `tune-and-polish`.
