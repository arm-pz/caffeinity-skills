# Trigger cases for prompts-to-workflow

Written to the format in tune-skill's `references/test-cases.md`, judged from the `description` only. Competing descriptions read: `prompts-to-skill`, `draft-skill`, `skill-launch`, `caffeinity-routing`, `tune-skill`, `tune-and-polish`, `findable-polish`.

**Status:** written 2026-11-01, not run against an agent. Every result below is "written".

## Cases

| # | Message | Expected skill | Expected mode | Pass condition | Result |
| --- | --- | --- | --- | --- | --- |
| 1 | "Here's my prompt log from launching my last three skills. Make it a workflow." + 9 prompts | prompts-to-workflow | map, then split | shows the map and waits before naming skills | written |
| 2 | "[10 prompts] which of these are already skillsmith skills and what's missing?" | prompts-to-workflow | split | runs `catalog.py`; every step gets a verdict with evidence | written |
| 3 | "Split this prompt chain into skills." + 6 prompts | prompts-to-workflow | split | reuses catalog skills before proposing new ones | written |
| 4 | "I do these seven steps by hand every Monday, can it be one thing?" + the steps | prompts-to-workflow | map | treats it as a chain, not seven skills | written |
| 5 | "Turn these into a brew." + prompts | prompts-to-workflow | map | output matches the brew table format | written |
| 6 | "Crawl my site, fix keywords, rewrite copy" as 5 pasted prompts | prompts-to-workflow → caffeinity-routing | whole-chain match | reports Brew 4 · Cold brew and hands off; writes no chain skill | written |
| 7 | "Make each of these five prompts its own skill." | prompts-to-skill | — | prompts-to-workflow does not load | written |
| 8 | "I have an idea for a skill that checks invoices." | draft-skill | — | prompts-to-workflow does not load | written |
| 9 | "Take my skill from idea to published." | skill-launch or caffeinity-routing | — | no prompts pasted; prompts-to-workflow does not load | written |
| 10 | "My tune-and-polish skill triggers on the wrong things." | tune-skill | — | an existing skill; prompts-to-workflow does not load | written |
| 11 | "Which skill should I run first to ship my site?" | caffeinity-routing | — | outcome, no prompts; prompts-to-workflow does not load | written |
| 12 | Two pasted prompts, "make a workflow" | prompts-to-workflow | before you start | says two prompts are too few for a chain and asks for the rest of the log | written |

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "These prompts are steps of one job; make it a workflow" | prompts-to-workflow | chain in the prompts |
| "These prompts are separate; make them skills" | prompts-to-skill | no chain |
| "Here's what I want to achieve; which brew?" | caffeinity-routing | outcome, no prompts |
| "Here are the prompts I use to achieve it; which brew, and what's missing?" | prompts-to-workflow | prompts present; may hand to caffeinity-routing on a full match |
| A bare pasted batch with no instruction | prompts-to-skill | its description claims this; its Before-you-start step 2 hands a chained batch here |

Spanning case: "Here are my prompts. Make it a workflow, build the missing skills, and publish them." Starts here; ends with briefs handed to prompts-to-skill, then prompts-to-skill-release per skill.

## Resolved 2026-11-01

`prompts-to-skill` claimed every bare pasted batch, so a chained batch became one skill. Fixed there: its description now says "Not for prompts that are the steps of one multi-step job … (use prompts-to-workflow)", its Before-you-start step 2 hands a chain here, and its three-prompt guard accepts this skill's briefs.
