# Mapping steps to a script

How the twelve caffeinity workflows were turned into dynamic workflows (arm-pz/caffeinity-skills
PRs #35 and #36), written down so the next one comes out the same way.

## 1. The step table

Write one row per step before any code. Every column comes from the skill's own `SKILL.md`, not
from its name.

| # | Skill | Receives | Hands on | Stops when | Outward actions | Runs with | Model |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | web-preflight | a URL the user owns | a lane report | never | none | lanes 1-3 together | sonnet |

- **Receives / hands on**: if step N's output is not what step N+1 says it receives, that is a
  **handoff gap**. Record it in the report. Do not invent a converter step or a file format the
  skills never defined; tell the step's prompt what it will receive and let its skill decide.
- **Stops when**: the step's own gate (a confirmation, a choice between owners, a failing check).
- **Outward actions**: anything that leaves the machine or can't be undone: push, PR, comment,
  deploy, send, publish, purchase, delete. The script never takes these.
- **Runs with**: which steps don't depend on each other's output.

## 2. Pick the shape

| Shape | When | Script |
| --- | --- | --- |
| **Chain** | each step needs the previous step's output | `chain()` from the preamble: one `step()` per row, in order |
| **Lanes then gate** | several independent checks, then one verdict | `parallel()` of `step()` calls (a barrier is right: the gate needs all lanes), then one gate agent |
| **Fan-out** | the same step over many items (files, repos, leads) | `pipeline(items, stage1, stage2)` with no barrier; a final agent merges |
| **Mixed** | a chain where one row is lanes or a fan-out | `chain()` whose row calls `parallel()` or `pipeline()` |

Default to `pipeline()` over `parallel()` unless the next stage truly needs every result at once
(dedupe, an early exit on zero, a gate that compares all lanes).

## 3. Gates become resume points

A workflow can't ask anything mid-run, so:

- **A step's own gate** (draft-skill confirming purpose and triggers, tune-skill picking an owner):
  the step returns `status: "stopped"` with `askUser`. The run ends there. The result carries
  `resume`: the same args plus `from: n`, and the user adds `decisions` (or a named field such as
  `confirmed`) and runs it again. Completed steps are not repeated.
- **An outward action**: the step prepares it and lists it in `proposedActions`. The run ends with
  `needs_approval`; `resume` starts at the next step with the step's output carried. The user (or
  an ordinary turn after the run) takes the action.
- **Missing input**: with no `args`, the script returns `needs_input` and an example before
  starting any agent. That is the only "question" a workflow can ask.
- **A missing skill**: the step returns `status: "skipped"` with the install command. The run ends
  with `needs_input` and a `resume` from that step, so it never reports `done` on work that did
  not happen.
- **Optional steps** (skill-to-mod only when there is a fixed moment): a `when` test on the row,
  driven by an arg, with `whenNot` saying which arg turns it on.

## 4. Pick a model per step

- **Sonnet** (`effort: 'medium'`) for steps that follow a skill's procedure: crawl, check, package,
  render, apply a known fix, compute a gate with a script. Use `effort: 'high'` when the step reads
  a lot or the procedure is long.
- **Opus** (`effort: 'high'`) only where the step judges or designs: drafting or tuning a skill,
  red-teaming, diagnosing a cause, a stress test, a strategy memo, an offer or a tailoring choice.
- Name the tier in a constant (`SONNET`, `SONNET_HIGH`, `OPUS`) so one edit changes all of them.
- For a scheduled or nightly workflow, use Sonnet throughout unless the user says otherwise.

## 5. Name and place it

- `meta.name`: lowercase words joined by hyphens, verb-led, the same as the file name. For a
  workflow that already has a slug (Workflow 3 · launch-safely), use the slug.
- Place it where it will be called from: a plugin's `workflows/` for something shipped with skills,
  `.claude/workflows/` for one repo, `~/.claude/workflows/` for the user alone.
- In a plugin it runs as `/<plugin>:<name>`; tell the user that full command.

## 6. Prove it without running it

- `scripts/check_workflow.mjs` checks the load rules and dry-runs the body three times with stub
  agents (all steps finish, no args, every step stops at its gate). It prints how many agents each
  run would start and on which model. Give it real-looking args with `--args`.
- For a plugin, `claude plugin validate --strict <plugin-dir>` must list the workflow and pass.
- Do not run the workflow to test it: a run spends the user's usage. Offer one small first run
  (one site, one PR, one directory) and let them choose.
