# Output formats

Open at steps 1, 4 and 5. Formats match caffeinity-routing's `references/workflows.md`, so a confirmed workflow can be added there as a new brew without rewriting.

## Workflow map (step 1)

```markdown
## <Workflow name>: <plain goal>

| Step | Does | Receives | Hands on | Stops when | Prompts |
| --- | --- | --- | --- | --- | --- |
| 1 | research the topic | a topic and audience | sourced notes | sources are under three | 1, 4 |
| 2 | draft the post | the notes from step 1 | a draft | the user has not approved the angle | 2, 5, 7 |
| 3 | tighten the copy | the approved draft | final copy | — | 3 |

Orphans: prompt 6 (asks for a logo; unrelated to the chain).
Merged: prompts 2, 5 and 7 all draft; 5 adds a word limit, kept as a parameter.
```

Chains are often not a straight line: after a strategy step, colour, type and voice can all run in parallel, and a final guide needs everything. Name the source steps in "Receives" ("the palette from step 2 and the fonts from step 3") and number steps in the order they can first run. A step that needs input only the user has (their customer emails, their writing) says so in "Receives".

"Stops when" is a gate: a condition under which the next step must not run. Use "—" when there is none. A step with no gate is fine; a chain with no gates at all usually means the user confirms nothing, which is worth asking about.

## Split table (step 4)

```markdown
| Step | Verdict | Skill | Evidence | Installed |
| --- | --- | --- | --- | --- |
| 1 | reuse | `research-brief` | "sourced evidence for a question" | no |
| 2 | new | `draft-post` | nothing claims a blog draft from notes; recurs in 3 prompts | — |
| 3 | reuse | `wordsmith` | "rewrites copy, keeps the author's facts" | yes |
| 2–3 | — | — | no chain skill joins drafting and editing | — |

Brew match: none. Partial: Brew 6 · Cupping step 1.
```

Evidence is a short quote from the catalog description, or the reason none fits.

## Chain skill template (step 5)

```markdown
---
name: <chain-name>
description: <What it produces>. Chains <skill-a>, <skill-b> and <skill-c> in order, carrying each step's output to the next. Use when <the user's own phrasings for the whole job>. Not for <step-a's job alone> (use <skill-a>), <step-c's job alone> (use <skill-c>), or <adjacent job> (use <owner>).
---

# <chain-name>

<One paragraph: the job, and why it is a chain rather than one skill.>

## Dependencies

Needs <skill-a>, <skill-b> installed (`npx skills add arm-pz/<skill>`). If one is missing, say so and stop; do not improvise its step.

## Workflow

### Step 1: <does> with <skill-a>
Receives: <input>. Hands on: <output>. Stops when: <gate>.

### Step 2: <inline step>
<Imperative instructions, with the reason.>

...

## Boundaries

- Carries outputs forward verbatim; summarizing between steps loses what the next skill checks.
- Respects each skill's gate; a gate that stops stops the chain.
- Does not do a routed step's work itself.

## Report

One line per step: done, skipped (why) or stopped at a gate. One next step.
```

The chain skill's "Not for" clause names every reused skill's solo job. Without it, the chain steals single-step requests from its own dependencies.

## New-skill brief (step 5)

```markdown
# Brief: <proposed-name>

- **Step it fills:** <workflow name>, step <n>.
- **Receives:** <input>. **Hands on:** <output>.
- **Why new:** <which catalog skills were checked and why each does not fit>.
- **Trigger phrases:** <three requests in the user's words, at least one without the chain's vocabulary>.
- **Near-miss:** <one request it must refuse, and the owner>.
- **Prompts:** <the original prompts that showed this step, verbatim>.
- **Hand to:** `prompts-to-skill` (prompts attached) or `draft-skill` (idea only).
```
