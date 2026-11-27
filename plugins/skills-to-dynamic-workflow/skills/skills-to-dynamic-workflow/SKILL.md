---
name: skills-to-dynamic-workflow
description: Turns a workflow, an ordered set of agent skills, or an existing orchestrator (a chain skill, a workflow agent, a folder of subagent prompts) into a Claude Code dynamic workflow script that runs those skills as subagents. Maps each step's input, output and gate, turns approvals, pushes and deploys into resume points because a workflow cannot ask mid-run, picks Sonnet or Opus per step, writes the script from a tested preamble, and proves it with a no-token dry run. Use whenever someone wants a workflow, brew or set of skills to run as a /command, a Claude Code workflow, an ultracode script or a .claude/workflows file, or asks to automate a chain of skills, even if they never say "dynamic workflow". Not for picking which skills a goal needs (use caffeinity-routing), turning pasted prompts into skills (use prompts-to-workflow), running a skill on an event like git push (use skill-to-mod), or a one-off workflow with no skills behind it (use ultracode).
version: 0.1.0
---

# skills-to-dynamic-workflow

A dynamic workflow is a JavaScript file Claude Code runs in the background: `agent()` starts a
subagent, `pipeline()` and `parallel()` fan out, and the script, not Claude, decides what runs
next. Turning a chain of skills into one is mostly not code. It is deciding what each step
receives and hands on, where the chain must stop for a person, and which steps deserve the
stronger model. Get those right and the script is a table filled into a template.

The output is one `.js` file in the right place, a step table, a passing dry run, and a short
report that says how to call it and what a run costs.

## Ground rules

- **Check the rules live, not from memory.** The feature changes every few weeks. Reopen
  https://code.claude.com/docs/en/workflows, or run `/workflow-authoring` where Claude Code has
  it, and compare with `references/rules.md`. Fix the reference when it has drifted.
- **Read each skill's own SKILL.md.** What a step receives, hands on and stops on comes from the
  skill's file, never from its name. A step built on a guessed contract fails on its first run.
- **A workflow cannot ask.** Every confirmation, choice or sign-off becomes the end of a run plus a
  resume input. Never leave a step that silently picks for the user.
- **The script takes no outward action.** Pushes, PRs, PR comments, deploys, sends, purchases and
  deletions are prepared and listed in `proposedActions`, then taken after the run.
- **Opus only where a step judges or designs.** Sonnet runs every step that follows a procedure.
  Scheduled or nightly workflows stay on Sonnet unless the user says otherwise.
- **Do not run it to test it.** A run spends the user's usage. The dry run proves the control
  flow; offer one small first run and let the user choose.
- **Show the gaps.** When one step's output is not what the next step receives, say so in the
  report and in a comment in the script. Do not invent a converter or a file format.

## Before you start

1. **Get the chain.** Accept any of:
   - a named workflow with a step table (for example a caffeinity workflow in
     `caffeinity-routing/references/workflows.md`),
   - skill names in order ("consistent-code-review then address-findings"),
   - an orchestrator to port: a chain skill, a workflow agent's `.md`, or a folder of prompts.
   With one skill and no order, there is no chain: say a skill alone runs fine as itself.
2. **Confirm the job in one message.** Restate the steps in order, where the workflow will live,
   and what it returns. Wait for a yes or a correction before writing the script. If the user's
   message already names all three, say what you understood and go on.
3. **Find the skills.** Locate each `SKILL.md` (installed plugins, `~/.claude/skills`, the repo).
   A skill you cannot open stays in the table marked `unread`, and the report names it.

## Workflow

### 1. Write the step table

One row per step, in the format in `references/shapes.md`: skill, receives, hands on, stops when,
outward actions, what it runs alongside, model. Read every column from the skill's file. Mark each
handoff gap. Show the table with the confirmation in step 2 above when you can.

### 2. Pick the shape

Chain, lanes then a gate, fan-out, or a mix: `references/shapes.md` says which fits and why
`pipeline()` is the default over a `parallel()` barrier.

### 3. Turn gates and actions into resume points

Every step's own gate returns `stopped` with the one thing the user must decide; every outward
action ends the run as `needs_approval`; missing input returns `needs_input` with an example
before any agent starts. The preamble's `chain()` does this and builds the `resume` args, so a
rerun skips the steps that already finished.

### 4. Write the script

Copy `assets/workflow-template.js` to the target and keep its shared preamble whole: a workflow
cannot import, so every script carries its own copy. Then:

- set `meta`: a pure literal, `name` equal to the file name, a one-line `description`, a
  `whenToUse` that names the args, and one `phases` entry per phase title you use;
- set `INSTALL` to where these skills come from;
- replace the template's rows with one row per step from the table, each with `opts` set to its
  model tier, `receives` and `stopsWhen` copied from the table, and an `input` that passes only
  what the step needs;
- comment any handoff gap where it bites.

`references/examples/review-a-pull-request.js` is a finished one: two skills, a conditional second
step that reads the first step's verdict, and an outward action turned into a resume point.

Where it goes:

| For | Path | Runs as |
| --- | --- | --- |
| a plugin that ships the skills | `<plugin>/workflows/<name>.js` | `/<plugin>:<name>` |
| one repo | `.claude/workflows/<name>.js` | `/<name>` |
| the user alone | `~/.claude/workflows/<name>.js` | `/<name>` |

### 5. Check it

    node scripts/check_workflow.mjs <file.js> --args '<real-looking args JSON>'

Fix every FAIL. Read every warn: a phase never reached means a branch the dry run did not walk, so
walk it with `--stub '{"verdict": "fail"}'` (any field the branch reads). For a plugin, also run

    claude plugin validate --strict <plugin-dir>

and confirm it lists `workflows: <plugin>:<name>`. Both checks spend no tokens.

### 6. Hand it over

Do not run it. Offer one small first run on something the user names (one PR, one staging site,
one directory) and say how many agents it starts and on which models. For an unattended run, give
the allow rule it needs: `Workflow(<name>)`, because `ultracode` does not start a workflow from
`-p`, a schedule or a webhook.

## Hand off

- Which skills a goal needs, or in what order: `caffeinity-routing`.
- Prompts that still need to become skills: `prompts-to-workflow`, then come back.
- A step whose skill is missing or weak: `draft-skill` or `tune-skill`.
- The same chain triggered by an event such as `git push`: `skill-to-mod`.
- Releasing the plugin that carries the workflow: `prompts-to-skill-release`.

## Report

Short. The command it runs as and the file path. The step table, or one line per step with its
model. Agents per run from the dry run (all steps finish / stops at the first gate). Handoff gaps
and unread skills. Which checks ran and passed. One question: should it run once, and on what.
