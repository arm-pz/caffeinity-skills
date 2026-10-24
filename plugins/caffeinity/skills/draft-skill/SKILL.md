---
name: draft-skill
description: Create a new agent skill from a plain idea, with no prompt list to work from. Confirms intent before writing anything, decides what belongs in scripts versus references versus assets, writes a description that actually triggers, validates with tune-skill's check_skill.py, then hands off for boundaries and packaging. Use whenever the user wants to build, scaffold, author, start or design a new skill, describes a capability they want an agent to have repeatedly, points at an empty skill folder, or says "make me a skill for X", even if they never mention frontmatter or file layout. Not for turning a batch of existing prompts into a skill (use prompts-to-skill), tightening a skill that already exists (use tune-skill), or releasing a finished one (use prompts-to-skill-release).
---

# Draft skill

Drafting is deciding what a skill is for, then writing only the files that carry that decision. It is not a template you fill in. Most of the work happens before `SKILL.md` exists, and the parts that fail in production are the parts nobody confirmed: the trigger, the boundary against its siblings, and the claim the body cannot actually keep.

## Ground rules

- **Confirm before writing.** Restate the purpose, the expected output, and the phrases the user would really type. Wait for a yes. A skill drafted on a guessed purpose triggers on the wrong requests forever, and the fix costs a re-publish.
- **Nothing exists unless it earns its tokens.** The agent reading this already knows what Python is. Keep only what it would otherwise get wrong: your conventions, your file names, your order of operations, your gotchas. Detail the agent does not need goes in `references/`, and a reference nobody is pointed at is dead weight.
- **Match the specificity to the fragility.** A judgement call gets a heuristic. A sequence that breaks if reordered gets a script with fixed output. Writing prose for the second kind is how you get a skill that works when you watch it.
- **Name the owner of every verb.** Before you write, list what the installed siblings claim. If two skills promise the same artifact, one of them is about to stop triggering. Settle it and say which.
- **Do not claim what you did not run.** Report which checks ran, which test cases were only written, and which siblings you never opened.

## Workflow

### 1. Get concrete examples

Ask for three or four requests the skill should catch, and one it should refuse. Ask what the output looks like — a report, an edited file, a command, a decision. Do not run an interview; propose a shape from what the user already said and ask them to correct it.

If the examples are all phrased the same way, ask for one in different words. Triggering fails on variety, not on the obvious case.

### 2. Check the installed set

Read the `description` of every sibling the examples touch — from the file, not from memory or a README. Write one line each: what it claims, what it produces, what it hands off. Compare against the requests from step 1 and record any overlap before designing anything. If the job is already claimed, stop and say whether tuning the existing skill is the cheaper move.

### 3. Decide the boundary, in both directions

A skill needs one line saying what it owns and one saying where it stops and who takes over. Write both down and show them. The "Not for" clause in the description is this boundary, not decoration.

### 4. Plan the resources

- `scripts/` — code you would otherwise rewrite every run, or anything that must be deterministic. Must be tested by running it.
- `references/` — knowledge loaded while working: schemas, checklists, house conventions. Split when a section stops being necessary to every run.
- `assets/` — things that end up in the output, never read into context.

Create only the directories you fill. If all three are empty, the skill is prose and that is fine.

### 5. Choose the name

Lowercase words joined by hyphens, short, verb-led, and the folder named exactly after it. Before settling, search GitHub for the name and check whether something better-established already owns it — see `references/structure.md` for how to read a collision, because a name that ranks below an unrelated project is a tax you pay forever.

### 6. Write it

Frontmatter is `name` and `description`, nothing else unless the agent needs it. Write the description last: what it produces, then the contexts in the user's words, then the "Not for" clause. Body in imperative form, each rule carrying its reason. Point at every reference file with a line saying when to open it.

### 7. Validate

Run tune-skill's validator on the folder and fix every FAIL, judging each WARN:

    python <path-to>/tune-skill/scripts/check_skill.py <path-to-skill-folder>

Work through `references/structure.md` for the checks the script cannot make, including the one that bites hardest: a description whose promise the body does not keep.

### 8. Write the test cases

Follow the case format in tune-skill (`<path-to>/tune-skill/references/test-cases.md`). The examples from step 1 become your clear triggers; add implicit triggers, near-misses, and one case on each side of every boundary from step 3. Mark a case written until it has been run.

## Hand off

- Overlaps and wording pressure go to `tune-skill`.
- A batch of prompts instead of an idea goes to `prompts-to-skill`.
- Zip, version, README, install checklist go to `prompts-to-skill-release`.
- Repo name and listing go to `findable`.

Say which handoff you are making and what the next skill receives.

## Report

Short. Name and path. The boundary, in one line each direction. Files created and why each exists. Validator counts. Test cases written versus run. Siblings you did not get to read. One next step.
