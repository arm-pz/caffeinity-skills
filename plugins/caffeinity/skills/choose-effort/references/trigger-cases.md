# Trigger cases: choose-effort

The expected triggers below were reviewed against the skill descriptions. A manual pass means the wording supports the expected result. Live skill activation was not measured.

| # | Prompt | Expect | Kind | Hand-read | Why |
|---|---|---|---|---|---|
| C1 | I'm about to refactor the whole auth module, what effort level should I use? | load | clear | pass | The core request |
| C2 | Should I use xhigh for this migration? | load | clear | pass | Names a level |
| C3 | Set me up to run this overnight without burning my limit | load | clear | pass | Unattended run |
| C4 | Plan an agent team run to rewrite the test suite | load | implicit | pass | Fan-out, no effort wording |
| C5 | Kick off a /goal to get all the tests passing | load | implicit | pass | Goal mode; the skill asks before it starts |
| C6 | Why did my last Claude Code session drain my whole limit? | no load, use diagnose-usage | boundary | pass | After the work, not before |
| C7 | What effort levels does Sonnet support? | no load, use product-self-knowledge | near-miss | pass, weak | Shares "effort level" wording; the model support boundary carries it |
| C8 | What is the Claude Pro plan's usage limit? | no load, use product-self-knowledge | near-miss | pass | Plan allowances |
| C9 | Rename this variable across the file | no load | unrelated | pass | Trivial, no decision to make |
| C10 | Which Claude model should I use for coding? | no load | near-miss | pass | Model choice, not effort |
| C11 | How can I use less in Claude Code from now on? | load | boundary | pass | Going forward; other side of D12 |
| C12 | Which is the orchestrator level in Codex? | load | clear | pass | Answer Ultra mode directly, with availability caveat |
| C13 | Should I use Ultra or High to debug this tightly coupled Codex issue? | load | clear | pass | Choose effort based on the scope and how well it splits |
| C14 | I want Codex to review three independent modules in parallel. How should I set it up? | load | implicit | pass | Recommend an available orchestration mode or explicitly scoped subagents |
| C15 | Which reasoning levels does my Codex model support? | no load, use official docs or the picker | near-miss | pass | Model capabilities without a task decision |
| C16 | Why did my last Codex session use up my quota? | no load, use diagnose-usage | boundary | pass | Completed run, outside prospective effort selection |
| C17 | Configure a permanent Codex advisor and lighter readers for this repo | no load, use setup-claude-advisor | boundary | pass | Persistent model roles without a per-task decision |
| C18 | What effort should I use for this refactor? (active host: Codex) | load | runtime | pass | Uses Codex controls without asking for a host or model |

Boundary pairs: C1 against C6 (before versus after the work); C11 against D12 in `diagnose-usage` (the same prompt: `choose-effort` loads and `diagnose-usage` does not); C2 against C7 (which level for this task versus which levels exist). In Codex, C12 versus C15 distinguishes the orchestration setting from model support. C14 versus C16 distinguishes setup from past usage.
