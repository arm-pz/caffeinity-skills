---
name: skill-launch
description: >-
  Launch a new skill end-to-end. Create it with draft-skill, validate and tune it with tune-skill,
  then audit its discoverability and polish it with findable-polish. Use when the user has an idea for
  a skill and wants to go from zero to published, with triggering, validation and discovery surfaces
  all handled in one pipeline. Chains draft-skill, tune-skill and findable-polish sequentially.
  Not for editing existing skills (use tune-and-polish), and not for a batch of prompts the user
  already wrote (use prompts-to-skill).
version: 0.1.0
argument-hint: "[skill idea]"
user-invocable: true
metadata:
  version: "0.1.0"
---

# Skill-Launch

Execute a complete skill creation pipeline in three phases: **Draft-Skill** creates the initial skill from an idea, **Tune-Skill** validates and fine-tunes its triggering and boundaries, then **Findable-Polish** audits its discoverability and generates polished alternatives for repo metadata, README, and site page.

## Invocation

```text
/skill-launch "I want a skill that checks if my code is production-ready"
/skill-launch "a skill that turns support tickets into release notes"
Create a skill that audits repos before deployment.
```

If no idea is provided, ask the user what problem they want the skill to solve.

## Workflow

### Phase 1: Create with Draft-Skill

Invoke the **Draft-Skill skill** with the provided idea. If the input is a list of prompts
rather than an idea, stop and hand the batch to `prompts-to-skill`, which owns the intent interview,
the gates and the packaging for prompt sets:

1. Confirm intent before writing anything.
2. Decide what belongs in scripts vs references vs assets.
3. Write SKILL.md with description that actually triggers, H1 matching name, body with clear workflow.
4. Create reference files for handoff protocols, command routing, test cases.
5. Add scripts directory if automation is needed.
6. Output: a complete skill folder at `~/.qoder/skills/<skill-name>/`.

**Handoff rule:** Capture draft-skill's output, especially the skill name chosen and any design decisions made.

### Phase 2: Validate and Tune with Tune-Skill

Pass the newly created skill to the **Tune-Skill skill**:

1. Read the real SKILL.md and sibling skills to check for overlaps.
2. Audit description fit, trigger wording, boundary clarity, reference file completeness.
3. Make minimal edits to fix each finding.
4. Run `python scripts/check_skill.py` to validate.
5. Write near-miss test cases for each boundary.
6. Output: report of changes made, validation results, remaining warnings.

**Handoff rule:** Capture tune-skill's report, especially any WARNings that need addressing before publication.

### Phase 3: Polish Discoverability with Findable-Polish

Pass the tuned skill's repo/path to the **Findable-Polish skill**:

1. Findable audits discoverability: derives search queries, identifies gaps in description/topics/README.
2. Wordsmith generates 2–3 polished alternatives for each gap.
3. Output: audit findings + rewrite options side-by-side.

Use this instruction for Wordsmith:

```
This skill was just created and validated. Now make it discoverable.

Focus on:
- GitHub About text and topics that match the tuned description exactly
- README opening line that states what it does + who it's for in one sentence
- Site page entry that distinguishes it from siblings (no trigger overlap)
- Release notes that explain the problem it solves

Tune-Skill validation report:
[Paste tune-skill's report here]

Target skill path:
[Path to the new skill's folder]
```

### Phase 4: Present Results

Return a four-part response:

1. **Draft-Skill Output** (what was created, structure overview)
2. **Tune-Skill Changes** (what was edited, validation status)
3. **Findable-Polish Alternatives** (discovery surfaces with options labeled)
4. **Publication Checklist** (files to commit, commands to run, next steps)

Format so the user can copy-paste directly into their repo and push.

## Boundaries

- **Does not** push to GitHub or publish to marketplace automatically — hands over commands.
- **Does not** own the push or the listing either way: pushing existing clones is `upstream-check`,
  GitHub About text, topics and directory entries are `findable`, packaging a finished folder is
  `prompts-to-skill-release`. This skill runs the pipeline for one new skill from an idea.
- **Does not** create multiple skills at once — one skill per invocation.
- **Does not** skip validation — tune-skill must pass before proceeding to findable-polish.
- **Does not** invent features the user didn't ask for — stays faithful to the original idea.

## Dependencies

This skill requires `draft-skill`, `tune-skill`, `findable-polish` (which needs `findable` + `wordsmith`) to be installed. If any are missing, tell the user and stop.
