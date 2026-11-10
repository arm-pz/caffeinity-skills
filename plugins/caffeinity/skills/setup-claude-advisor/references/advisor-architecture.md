# Advisor architecture reference

Read this when proposing the subagent tree (step 2) or drafting the advisory rule (step 4).

## Model tiering rationale

Claude Code on the $20 plan now defaults to Opus 5.5 for the entire session. This burns quota
roughly 3–5× faster than Sonnet 5.5 for the same token count. The advisor pattern keeps Opus
available for high-value strategic decisions while Sonnet handles the bulk of code generation.

| Model | Role in this setup | Why |
|---|---|---|
| **Opus 5.5** | Advisor only (`advisor` tool) | Reads the full session context. Called at three decision gates. Never writes code directly. |
| **Sonnet 5.5** | Main session + code-editing subagent | Handles all file edits, test runs, and command execution. Good enough for 95% of coding tasks. |
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

- **Claude Code ≥ 2.1.293**: `haiku` resolves to the current Haiku model. Safe to use.
- **Claude Code < 2.1.293**: `haiku` resolves to Haiku 4.5 (legacy). The cost savings are
  smaller and the capability gap is larger. Recommend upgrading before applying this setup.

## Environment variable effects

| Variable | Effect |
|---|---|
| `CLAUDE_CODE_DISABLE_ADVISOR_TOOL` | Completely disables the advisor tool. The advisory rule becomes inert. |
| `DISABLE_TELEMETRY` | Blocks flag fetching, which can disable advisor functionality indirectly. |
| `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` | Overrides every subagent's `model:` field with one value. Per-role model assignments are ignored. |

If any of these are set, warn the user that the setup will not work as intended until the
variable is unset.

## Settings file schema

`~/.claude/settings.json` relevant fields:

```json
{
  "model": "sonnet",
  "advisorModel": "opus",
  "customInstructions": "..."
}
```

- `model`: The default model for the main session. Set to `"sonnet"`.
- `advisorModel`: The model that answers `advisor` tool calls. `/advisor <model>` switches it for the session. Set to `"opus"`.
- Preserve all other keys when merging.
