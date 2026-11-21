---
name: diagnose-usage
description: Diagnoses why a completed Codex or Claude Code run used more quota or credits than expected. Use when a session, automation, or day drained usage fast, the user hit a limit sooner than expected, or they want help interpreting usage evidence for work that already ran. Compares run evidence with account usage and gives up to three supported causes, each with a change to verify. Not for choosing effort for upcoming work (use choose-effort), configuring persistent advisor or subagent model tiers (use setup-claude-advisor), or plan limits, prices, and API billing.
version: 1.1.0
---

# Diagnose usage

## Select the host

Use the client that produced the affected run, if the user identified it. Otherwise, use the active client as the default and say so if that assumption matters. Usage from a different client may require a different report.

If the client is still unclear, diagnose from the supplied evidence and ask only if you need a client-specific report or control. For Codex, follow `references/codex-usage.md`. For Claude Code, continue below.

## Claude Code

Anthropic's Claude Code team reviewed the session IDs people shared in late October 2026 and found no single root cause and no regression. Most fast drains traced to one or two heavy sessions, plus a few smaller token-burn issues Anthropic said it was rolling out fixes for. This skill follows that finding: locate the heavy session first, and treat a product bug as the last explanation, not the first.

### Ground rules

- **Find the session before the setting.** Fast drains usually come from one or two sessions. Changing global settings for all work fixes the wrong thing and makes everything else worse.
- **Never promise a bug or a fix.** Say "update Claude Code, then re-check `/usage`", not "this is a known bug". Anthropic did not find a single cause.
- **Don't run slash commands for the user.** `/usage`, `/effort` and `/feedback` are built-ins the user types. Ask for the pasted output; do not guess at numbers.
- **Check names before you say them.** Effort levels, flags and features in Claude Code change month to month. If a level, flag or command is not in the user's paste or the current docs, say you could not confirm it. The docs map is in the `product-self-knowledge` skill when it is installed.

### Workflow

1. Ask once, in one message: which session or day, when the drain started, and which of these they used: goal mode, workflows, agent teams, subagents, an SDK or headless job, a raised effort level. Skip anything they already said.
2. Ask the user to run `/usage` and paste the result. It shows where a session's tokens went; without it any ranking is a guess.
3. Open `references/burn-sources.md` and match the evidence in the paste to its suspects. Rank by tokens in the paste, not by the order in the file.
4. Report in the shape below.
5. If nothing in the paste explains the drain, or it still looks wrong after the change, tell the user to run `/feedback` from that session. Anthropic said it follows up directly with people who share a session ID.

`references/trigger-cases.md` holds the test cases. Open it only when tuning the description above.

### Report

Up to three culprits, ranked. Each one: what the paste shows, why that costs a lot, and one change. Then one next step. Mark which findings came from the user's paste and which are general causes you could not confirm from it.

## Hand off

- Setting an effort level or fan-out for the next heavy task goes to `choose-effort`, as does "how do I use less from now on" when there is no past session to look at.
- Persistent advisor or subagent model tiers go to `setup-claude-advisor`.
- Plan allowances, prices, and API billing go to current provider docs or `product-self-knowledge` for Claude Code.
