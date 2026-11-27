# Dynamic workflow rules

What the Claude Code runtime enforces when it loads and runs a workflow script. Checked on
2026-11-27 against https://code.claude.com/docs/en/workflows and the Workflow tool's own
reference in Claude Code 2.1.332. The feature moves fast: before writing a script, reopen the docs
page (or run the bundled `/workflow-authoring` skill, Claude Code 2.1.248 or later) and fix this
file where it has drifted.

## The file

- Plain JavaScript with top-level `await`. No TypeScript annotations: they fail to parse.
- First statement: `export const meta = { name, description, whenToUse?, phases? }`.
  - A pure literal: no variables, calls, spreads or template interpolation. Anything else drops
    `/<name>` from `/` autocomplete.
  - `description` is one line; the permission dialog shows it.
  - `phases`: one `{ title, detail? }` per `phase()` call, titles matched exactly. A `phase()`
    title with no entry gets its own progress group.
- The body runs in an async context. Its `return` value is what Claude receives.

## Body hooks

| Hook | What it does |
| --- | --- |
| `agent(prompt, opts)` | One subagent. `opts`: `label`, `phase`, `schema`, `model`, `effort`, `isolation: 'worktree'`, `agentType`, `stallMs`. Resolves to text, or to the validated object when `schema` is given, or to `null` if stopped or it hit an unrecoverable error |
| `pipeline(items, stage1, stage2, ...)` | Each item runs through all stages independently, no barrier. Stages get `(prevResult, originalItem, index)`. The default for multi-stage work |
| `parallel(thunks)` | Runs `() => Promise` thunks at once and waits for all (a barrier). A thunk that throws resolves to `null`; the call never rejects |
| `phase(title)` | Groups the agents that follow under a title in `/workflows` |
| `log(message)` | A narrator line above the progress tree |
| `args` | The input the caller passed, verbatim, as real JSON. `undefined` when omitted |
| `budget` | `{ total, spent(), remaining() }` from a "+500k" style directive. `total` is `null` when unset, so never loop on `remaining()` alone |
| `workflow(nameOrRef, args)` | Runs another saved workflow (or `{ scriptPath }`) inline and returns its result |

Schemas need `{ type: 'object', properties: {...} }` at the root, and `required` must be a subset
of `properties`. A schema the runtime can prove contradictory fails before the agent starts; output
that fails validation five times fails the call.

## What the script cannot do

- **Ask the user anything mid-run.** A run pauses only for agent permission prompts and usage-limit
  waits. Every approval, choice or sign-off becomes the end of a run plus a resume input.
- **Touch the filesystem or shell itself.** Agents read, write and run commands; the script only
  coordinates them.
- **Load modules.** `import()` fails before the run starts. So every saved script carries its own
  copy of any shared helpers.
- **Use clocks or randomness.** `Date.now()`, `Math.random()` and an argless `new Date()` throw, so
  a relaunch repeats the same `agent()` calls. Pass a timestamp in through `args`.

## Limits

- Up to 16 concurrent agents (fewer on small machines); 4,096 items per `parallel()`/`pipeline()`;
  1,000 agents per run.
- A run over 25 agents or 1.5M projected tokens shows a `Large workflow` warning.
- Relaunching replays agents in start order: completed ones return cached results until the first
  changed or failed one, which runs again with everything after it.

## Where it lives and how it is called

| Location | Command |
| --- | --- |
| `.claude/workflows/<name>.js` in a project | `/<name>`, shared with the repo |
| `~/.claude/workflows/<name>.js` | `/<name>`, every project, only you |
| `workflows/<name>.js` at a plugin root (or the manifest's `workflows` field) | `/<plugin>:<name>` |

A project workflow wins over a personal one with the same name. After editing, `/reload-skills`
re-reads the directories.

## Starting a run

- Typed by a person: `/<name>`, the keyword `ultracode`, or "use a workflow".
- `claude -p`, the Agent SDK without a human origin, scheduled tasks, webhooks and relayed PR
  comments do not start one from the keyword. They need the saved name plus an allow rule:
  `Workflow(<name>)` (or `Workflow` for all), auto mode, bypass mode, or a `PreToolUse` hook.
- Agents a workflow starts use the session's permission rules; add the tools they need to allow
  rules before a long unattended run.
- Model per agent: `opts.model` counts as the per-invocation model; with none, the agent runs on
  the session's model. An `availableModels` allowlist can substitute it.
