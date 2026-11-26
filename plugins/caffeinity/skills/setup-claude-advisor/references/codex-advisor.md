# Codex advisor setup

Use this branch for persistent model assignments in a local Codex client. Use a custom advisor subagent for a second opinion. The main agent gives it a focused brief and remains responsible for edits and decisions.

1. Identify the client, available models, and desired scope. For Codex CLI, check `codex --version` and use `/model` to confirm model choices. In the app, use the model picker. Prefer project scope unless the user wants personal defaults. Check managed constraints and project trust if configuration is unavailable.
2. Inspect the active user and project `.codex/config.toml`, agent TOMLs under the corresponding `.codex/agents/` directories, and applicable `AGENTS.md` or override. Read only relevant settings and redact secrets. Check for an existing advisor, role name collisions, and applicable guidance before proposing new files.
3. Keep the current main model unless the user requests a change. Choose an available stronger model for decision review and a lighter model for repetitive read-heavy work if useful. Reuse existing agents for exploration and editing unless the user needs persistent model overrides for those roles.

| Role | Responsibilities |
|---|---|
| Main | Own the work, make decisions, apply edits, and run verification |
| Advisor | Review a decision, surface risks, and recommend next checks |
| Explorer or worker | Take scoped reading or editing work when the task benefits |

4. Prepare the TOML in `.codex/agents/advisor.toml` (project) or `~/.codex/agents/advisor.toml` (personal, under the active Codex home). Set `model` only to a verified ID. Omit it if unknown and explain that it inherits the effective default. Only add `model_reasoning_effort` if supported and needed.

```toml
name = "advisor"
description = "Reviews consequential plans, repeated blockers, and release decisions."
developer_instructions = """
Review the brief and relevant evidence. Do not edit files or change settings.
Return a recommendation, the main risk, and one verification step.
"""
```

5. Propose a short block in the applicable `AGENTS.md` (or the active override). Reuse or replace an existing protocol section. When delegation is available and allowed, consult the advisor before a consequential plan is committed, after the same blocker recurs after a fix attempt, or before closing release-critical work. Send only the context needed. Skip routine tasks. These instructions guide behavior. Custom agents inherit the parent's permissions, so use a read-only session when an enforced no-write boundary is required.
6. Preview the diff, including a config change only if needed. Wait for explicit approval before writing. After applying, parse each new or edited TOML and check that a fresh local session recognizes the advisor. If the user wants a smoke test, ask the advisor for a scoped second opinion without changing files. Use `/subagents` in the CLI to inspect a run. Document any unsupported client or verification you could not perform.

[Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) · [Project instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
