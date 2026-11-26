# Diagnose Codex usage

Use this branch for a Codex run or usage window that already happened.

1. Ask once for the client, affected time window and timezone, and whether the concern is an included usage limit or credits consumed. Ask for the smallest evidence needed. In the desktop app, `/usage` opens usage and billing settings where available and `/status` shows chat context and rate limits. In the CLI, `/usage` shows account token activity with ChatGPT sign-in and `/status` shows session context and remaining limits. Use the usage dashboard if these controls are unavailable.
2. Compare the same account or workspace and matching limit window around the reported drop. Ask for relevant run metadata when available: timestamps, model, effort, speed tier, local or cloud, and agent activity. A saved CLI automation's `turn.completed` event from `codex exec --json`, if available, gives token counts for that turn. Compare those counts only at their recorded scope. Ask for redacted figures or event summaries and avoid requesting raw logs, prompts, credentials, or account IDs.
3. Separate account, session, and turn evidence. Account totals, context occupancy, credits, and token counts measure different things. A quota drop during one run can coincide with other work and does not give the run's token or credit breakdown. Without attribution data, state the observed change and label candidate causes as unconfirmed.
4. Match the evidence to these common causes. Give up to three, with a change and a way to verify each. With no supporting evidence, give the next measurement instead of ranking causes.

| Evidence to look for | Candidate cause | One change to compare |
|---|---|---|
| Several overlapping subagent threads or long cloud or goal activity around the drop | Repeated model and tool work across agents or turns | Compare one-agent and delegated runs with equivalent inputs and the same model and effort where possible. Use the same mode with explicit delegation and no proactive fan-out for both runs. Confirm the control run used one agent and the comparison run delegated |
| Long-running chat or large repeated file reads and tool outputs | Higher context or retrieval load | Start a focused chat with a concise handoff and narrow inputs |
| Higher effort, a different model, or Fast or Ultrafast confirmed on the affected run | Different reasoning load or usage rates | Change one setting and compare equivalent work in the same account and window |

5. If usage still looks unexplained after the comparable check, suggest sending a redacted summary via the client's feedback or support path. In the app, `/feedback` opens the dialog. Let the user decide whether to attach logs. Route plan limits, rate cards, and API billing to current official product documentation.

[Desktop commands](https://learn.chatgpt.com/docs/app/slash-commands) · [CLI commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli) · [Codex usage and pricing](https://learn.chatgpt.com/docs/pricing) · [Fast and Ultrafast](https://learn.chatgpt.com/docs/agent-configuration/speed)
