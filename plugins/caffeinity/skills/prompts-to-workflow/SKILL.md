---
name: prompts-to-workflow
description: Turns a pasted batch of prompts that together do one multi-step job into a workflow, then decides how to split it into skills. Maps the prompts to ordered steps with inputs, outputs and gates, checks every step against the live skillsmith.tech catalog and its brews, reuses existing skills such as tune-and-polish, wordsmith or findable where they fit, drafts a thin chain skill that runs the steps, and writes a brief for each new skill only where nothing covers a step. Use whenever the user pastes prompts or a prompt log and asks to make it a workflow or a brew, split it into skills, work out which skills they already have, or stop doing these steps by hand, even if they never say "workflow". Not for prompts that each become their own skill (use prompts-to-skill), a single idea (use draft-skill or skill-launch), an outcome described without prompts (use caffeinity-routing), or an existing skill (use tune-and-polish).
version: 0.1.0
---

# prompts-to-workflow

A pile of prompts someone keeps pasting is usually not one skill and not N skills. It is a chain: research, then draft, then check, then publish, with the same handoffs every time. `prompts-to-skill` packages prompts as skills; this skill finds the chain first, and only then decides what each link should be. Most links already exist on skillsmith.tech. Writing a new skill for a step that `wordsmith` or `tune-and-polish` already does creates a sibling that steals its triggers.

The output is a decision plus the files that carry it: a workflow map, a split table, a chain skill, and one brief per genuinely new skill.

## Ground rules

- **Map before you split.** Do not name a single skill until every prompt is placed on a step. A split decided prompt-by-prompt reproduces the prompts, not the job.
- **Decide against the live catalog, not memory.** Run `scripts/catalog.py` every time. The site adds skills weekly, and a split that proposes a skill which shipped last Tuesday is wrong.
- **Reuse beats new.** A step goes to an existing skill when that skill's description claims the step's input and output. Partial fit is a reuse with a note, not a new skill. See `references/split-rules.md`.
- **A whole-chain match stops here.** If the chain is an existing brew, say which and hand to `caffeinity-routing`. Do not write a second Brew 4.
- **Do not write the new skills' bodies.** Each new skill gets a brief and goes to `prompts-to-skill` (when the brief carries its own prompts) or `draft-skill` (when it is an idea). This skill owns the split, not every skill in it.
- **Report what was installed versus only published.** A chain that runs on skills the user has not installed is a plan, not a workflow. List the install lines.

## Before you start

1. **Count the prompts.** Three or more. With fewer, there is no chain to find: ask for the rest of the log, or treat a single prompt as an idea for `draft-skill`. (`prompts-to-skill` also needs three, so do not send it two.)
2. **Check it is one job.** If the prompts do unrelated things with no output feeding the next input, they are separate skills: hand the batch to `prompts-to-skill` and stop. Say so in one line.
3. **Screen the prompts.** Stop if they ask for unauthorized access, exfiltration or malware, or carry personal data the workflow would store.

## Workflow

### 1. Map the chain

Write the workflow map in the format in `references/workflow-map.md`: one row per step with what it receives, what it hands on, where it stops, and which prompt numbers show it. Merge prompts that do the same step in different words. Mark prompts that fit no step as **orphans**; they are not forced into the chain.

Show the map and wait for the user to confirm the order and the gates (**confirmation 1**). Order errors here cost a re-split later.

### 2. Load the catalog

    python scripts/catalog.py            # live skills + brews, installed flags
    python scripts/catalog.py --offline  # if the network is down; say so in the report

Read each candidate skill's full description from the output, not its name. If the script prints a note that the live index was unreachable, the split is provisional; say that in the report.

### 3. Compare with the brews

Lay the mapped steps against every brew. If one brew covers all non-optional steps in order, it is a **whole-chain match**: report the brew by number and name, list any orphans, and hand to `caffeinity-routing`. If a brew covers a run of consecutive steps, use it as a sub-chain and note it in the split table.

### 4. Route each step

For each step, apply `references/split-rules.md` in order and record exactly one verdict:

- **reuse** `<skill>`: an existing skill claims this input and output.
- **chain** `<skill>`: an existing chain skill (`tune-and-polish`, `findable-polish`, `seo-polish`, `skill-launch`...) already runs this run of steps.
- **new** `<proposed-name>`: repeatable, self-contained, has its own trigger, and nothing claims it.
- **inline**: too small or too specific to stand alone; it stays as a step inside the chain skill.

Write the split table (format in `references/workflow-map.md`). Every verdict carries one line of evidence quoted from the catalog description, or the reason none fits. Show it and wait for a yes (**confirmation 2**). This is the decision the user is paying for; do not write files on a split they have not seen.

### 5. Write the outputs

Into `<output>/<workflow-name>/` (ask where; default `./skills/`):

- `workflow.md`: the confirmed map and split table, plus install lines for every reused skill (`npx skills add arm-pz/<skill>`; the caffeinity-skills repo for `paper-trail`, `course-builder` and `skill-estate`).
- `<chain-name>/SKILL.md`: the chain skill, only when two or more steps route to skills. Use the template in `references/workflow-map.md`. It names each step's skill, carries outputs forward verbatim, keeps each skill's gate, and stops when a dependency is missing rather than improvising it. When the chain is one reuse plus inline steps, skip the chain skill and say so.
- `briefs/<new-skill>.md`: one per **new** verdict, in the brief format in `references/workflow-map.md`, with the prompts that showed the step attached.

### 6. Validate

Run tune-skill's validator on the chain skill and fix every FAIL:

    python <path-to>/tune-skill/scripts/check_skill.py <output>/<workflow-name>/<chain-name>

If tune-skill is not installed, say the chain skill is unvalidated and give its install line. Then write trigger cases for the chain skill in tune-skill's format, including a near-miss for every reused skill (a request that one step alone should own) and mark them written, not run.

## Hand off

- Each brief goes to `prompts-to-skill` (brief with prompts) or `draft-skill` (brief as an idea). Say which per brief.
- A whole-chain match goes to `caffeinity-routing` with the brew name.
- Overlap between the chain skill's description and a reused skill's goes to `tune-skill`; overlap plus listing goes to `tune-and-polish`.
- Packaging the finished chain skill goes to `prompts-to-skill-release`; its listing to `findable`.
- A chain that must run at a fixed moment (before push, on deploy) can go to `skill-to-mod` once it works.

## Report

Short:

- Workflow name and output path.
- Steps mapped, prompts merged, orphans (with reason).
- Brew match: whole, partial (which steps), or none.
- Split counts: reuse, chain, new, inline. One line per new skill with its handoff target.
- Not installed: skills the chain needs, with install lines.
- Validator counts for the chain skill; trigger cases written versus run.
- Whether the catalog was live or offline.
- One next step.

`references/trigger-cases.md` holds this skill's own trigger cases; open it when tuning this skill's description.
