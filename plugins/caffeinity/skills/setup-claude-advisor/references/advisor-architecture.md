# Advisor architecture reference

Read this when proposing the subagent tree (step 2) or drafting the advisory rule (step 4).

## Model tiering rationale

Since Claude Code 2.1.280 the Pro ($20) plan defaults to Opus for the entire session, and
`opus` resolves to Opus 5.5. Opus 5.5 lists at twice Sonnet 5.5's API price ($4/$20 versus
$2/$10 per million tokens). Anthropic does not publish how each model is weighted against a
subscription's usage limit, so do not quote a quota multiplier to the user. The advisor pattern
keeps Opus available for high-value strategic decisions while Sonnet handles the bulk of code
generation.

Each advisor call reads the full conversation uncached and counts toward the plan's usage
limits. That is why the advisory rule names three moments instead of leaving the advisor on
call for everything.

| Model | Role in this setup | Why |
|---|---|---|
| **Opus 5.5** | Advisor only (`advisor` tool) | Reads the full session context. Called at three decision gates. Never writes code directly. |
| **Sonnet 5.5** | Main session + code-editing subagent | Handles all file edits, test runs, and command execution. Handles the bulk of coding tasks. |
| **Haiku** (current version) | Read-only subagents | Cheap and fast for file reads, grep, doc lookups. No editing capability needed. |

## The three advisory moments

These are the only times the main session should call the `advisor` tool:

1. **Before committing to a plan.** After Sonnet outlines a multi-step approach (refactor,
   migration, new feature), it asks Opus: "Here is my plan. Is this the right approach, or am I
   missing a better path?" Opus reads the full context and either confirms or redirects.

2. **When the same error recurs.** If Sonnet hits the same error a second time after attempting
   a fix, it asks Opus: "I have hit this error twice. Am I heading the wrong way?" This
   prevents Sonnet from burning tokens in a loop.

3. **Before declaring done.** Before Sonnet tells the user the task is complete, it asks Opus:
   "I am about to say done. Did I miss anything?" This catches omissions that Sonnet's narrower
   focus might miss.

## Subagent role definitions

### Code reader / searcher (`model: haiku`)

- **Purpose**: Read source files, search codebases, grep for patterns, find usages.
- **Permissions**: Read-only. No file edits, no command execution beyond search tools.
- **When to use**: "Find all uses of X", "Read this file and summarise", "Search for Y in the codebase".

### Documentation lookup (`model: haiku`)

- **Purpose**: Fetch and summarise API documentation, README files, changelogs, type definitions.
- **Permissions**: Read-only. Network access for doc fetching if available.
- **When to use**: "What does this API return?", "Check the docs for X", "What changed in version Y?".

### Code editor / test runner (`model: sonnet`)

- **Purpose**: Edit files, write new code, run tests, execute build commands.
- **Permissions**: Full read-write. Command execution for tests and builds.
- **When to use**: "Fix this bug", "Add this feature", "Run the tests", "Refactor X to Y".

## Version compatibility

- **Claude Code ≥ 2.1.293**: `haiku` resolves to Haiku 5.5 on the Anthropic API (added in
  2.1.293 as the default Haiku model). Safe to use.
- **Claude Code < 2.1.293**: `haiku` resolves to Haiku 4.5 (legacy). Recommend upgrading
  before applying this setup.
- **Sonnet 5.5 main + Opus advisor**: an accepted pairing. The advisor must rank at or above
  the main model; Sonnet 5.5 accepts Fable, Opus 5 or later, or Sonnet 5.5. A lower-ranked
  advisor is silently not attached.
- **Subagents** inherit the configured advisor and apply the same pairing check against their
  own model.

## Requirements

- **Anthropic API only.** The advisor is not available on Amazon Bedrock, Google Cloud,
  Microsoft Foundry, or Claude Platform on AWS. Through an `ANTHROPIC_BASE_URL` gateway it
  works only if the gateway forwards the request intact.
- **Feature-flag fetching.** Claude Code turns the advisor on through a flag it fetches from
  Anthropic.
- The advisor tool is labelled experimental; behaviour and availability may change.

## Environment variable effects

| Variable | Effect |
|---|---|
| `CLAUDE_CODE_DISABLE_ADVISOR_TOOL` | Set to `1`, completely disables the advisor tool: `/advisor` is unavailable, `advisorModel` is ignored, `--advisor` has no effect. The advisory rule becomes inert. |
| `DISABLE_TELEMETRY` | Turns off feature-flag fetching, so the advisor stays off. |
| `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` | Applies `CLAUDE_CODE_SUBAGENT_MODEL` (or the main model) to every subagent. Per-role `model:` assignments are ignored. |
| `CLAUDE_CODE_SUBAGENT_MODEL` | On its own, only sets the default subagent model. A subagent file's `model:` still wins (since 2.1.251), so this setup keeps working. Report it; no warning needed. |
| `CLAUDE_CODE_USE_BEDROCK` / `_VERTEX` / `_FOUNDRY` | Routes to a provider where the advisor is not available. |

If any of these except plain `CLAUDE_CODE_SUBAGENT_MODEL` is set, warn the user that the setup
will not work as intended until the variable is unset.

## Settings file schema

`~/.claude/settings.json` relevant fields:

```json
{
  "model": "sonnet",
  "advisorModel": "opus"
}
```

- `model`: The default model for the main session. Set to `"sonnet"`.
- `advisorModel`: The model that answers `advisor` tool calls. `/advisor <model>` switches it for the session. Set to `"opus"`.
- Preserve all other keys when merging.

## Sources

Checked on 2026-11-10 against Claude Code 2.1.322:

- Claude Code changelog: 2.1.251 (`CLAUDE_CODE_SUBAGENT_MODEL` precedence), 2.1.257
  (`CLAUDE_CODE_SUBAGENT_MODEL_FORCE`), 2.1.260 (`/advisor <model>` and `/advisor off`),
  2.1.280 (Opus 5.5; Pro default changed from Sonnet to Opus), 2.1.284 (Sonnet 5.5 pricing),
  2.1.293 (Haiku 5.5 becomes the default Haiku).
- Claude Code docs, "Escalate hard decisions with the advisor tool"
  (`code.claude.com/docs/en/advisor`): enabling, pairings, requirements, cost, turning it off.

These details move between releases. Re-check them before changing a version number or a
variable name in this file.
