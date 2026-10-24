---
name: prompts-to-skill
description: Turn a set of user-supplied prompts into a finished, tested agent skill. Runs an intent interview and overlap check, drafts with draft-skill, writes test cases, tunes with tune-skill, and optionally names and lists the repo with findable. Use whenever the user has a list of prompts, instructions, or example requests and wants them packaged as a reusable skill, even if they only say "make a skill from these", "turn these into a skill", or paste a batch of prompts with no further instruction. Not for editing an existing skill (use tune-skill), creating a skill from a plain description with no prompts (use draft-skill), or finding existing skills for a task.
---

# prompts-to-skill

This skill packages a set of prompts into a tested, tuned skill. It is a fixed pipeline with two confirmation points and two hard gates. Read `references/pipeline.md` for the detail of each step, and `references/gates.md` for the pass/fail rules.

## Dependencies

This skill drives two other skills and needs them installed: `draft-skill` (drafting, at https://github.com/arm-pz/draft-skill, installed with `npx skills add arm-pz/draft-skill --skill draft-skill`) and `tune-skill` (audit and validator, at https://github.com/arm-pz/tune-skill, installed with `npx skills add arm-pz/tune-skill --skill tune-skill`). Locate them by asking the agent to list its skills, or look in the skills directory it reads from. If either is missing, say so and stop rather than improvising their steps.

## Before you start

1. **Check there are enough prompts.** Three or more is the minimum for a trigger and scope to be visible. With fewer, ask for more.
2. **Screen the prompts.** Stop and tell the user if they ask for a skill that facilitates unauthorized access, data exfiltration, or malware, or if they contain personal data the skill would store. Skills must not surprise the user about what they do.
3. **Find the overlap.** Search the installed skills for descriptions that already claim these requests. If one already does the job, tell the user and ask whether to tune it instead. Do not draft a duplicate.
4. **Confirm intent (point 1).** Restate the purpose, the expected output format, and the trigger contexts in a few lines. Ask for confirmation. Do not draft until the user confirms.

## Pipeline

**Step 1 — Draft.** Invoke `draft-skill` on the confirmed intent and prompts. Its resource-planning and writing steps apply; skip its intent and boundary steps, which the confirmations above already settled here. Keep the description "pushy" enough to trigger on the user's own phrasing.

**Step 2 — Test cases.** Write at least eight cases in the format of tune-skill's test-case reference, plus an `evals/evals.json` (`skill_name` and a list of prompts). Show the list to the user and ask them to add or remove cases (point 2).

**Step 3 — Tune.** Follow tune-skill's workflow on the draft, then run its validator script against the folder and fix every FAIL. The script lives in tune-skill's own folder, not here.

**Step 4 — Name and list (optional).** Only if the user plans to publish the skill to GitHub. Use `findable` (https://github.com/arm-pz/findable, installed with `npx skills add arm-pz/findable --skill findable`). It makes the repo name decision and drafts the listing. Its audit needs a live repo, so if none exists yet, record the audit as pending. One owner per phase: listing copy is `findable`'s, packaging and the install checklist are `prompts-to-skill-release`'s, pushing an existing clone is `upstream-check`'s.

## Gates

Do not report success until both gates pass. See `references/gates.md`.

- **Gate A — structure:** tune-skill's validator reports no FAIL, the folder name, `name` field, and H1 match, and the description is under 1024 characters.
- **Gate B — triggering:** every original prompt triggers the skill, and every test case has a recorded pass or fail. Cases that were written but not run are marked as such.

If a gate fails, fix it inside the pipeline and re-run it. If it still fails, stop and report the failing item. Do not hand back a skill that fails a gate.

## Report

Keep it short:

- Skill name, folder path, and repo if any.
- Intent confirmed, and overlap found or not.
- One line per step: what changed.
- Gate A and Gate B results, with counts.
- Prompts not covered, with a reason.
- `findable` status: done, pending a repo, or skipped.
- One next step.

## Boundaries

This is a workflow, not an agent. The order and the gates are fixed. Do not add or drop steps based on what you think the skill needs. The user's confirmations are the only points where the order can pause.
