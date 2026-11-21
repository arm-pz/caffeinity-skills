# Trigger cases: diagnose-usage

Status: 19 cases reviewed manually. D1-D13 were reviewed on 2026-10-29 and checked against the current descriptions alongside D14-D19. No live session and no automated triggering loop was run, so "pass" means the description's wording supports the expected result, not that an agent was observed loading or skipping the skill.

| # | Prompt | Expect | Kind | Hand-read | Why |
|---|---|---|---|---|---|
| D1 | Why is my Claude Code usage draining so fast today? | load | clear | pass | The core request |
| D2 | I hit my Claude Code limit in an hour, something is wrong | load | clear | pass | Limit hit sooner than expected |
| D3 | What does /usage actually show me? | load | clear | pass | Names /usage |
| D4 | One session ate half my weekly limit, how do I cut token burn in Claude Code? | load | clear | pass | One heavy session that already ran |
| D5 | My agent team run finished and I'm at 90% of my limit | load | implicit | pass, weak | Matches "nearing their limit"; no "usage" or "drain" wording |
| D6 | Same work as last week but I run out of Claude Code five times faster. Is it broken? | load | implicit | pass | Frames it as a bug; the skill must not confirm one |
| D7 | What are the usage limits on the Max plan? | no load, use product-self-knowledge | near-miss | pass | Plan allowances |
| D8 | How much does Opus cost per million tokens on the API? | no load, use product-self-knowledge | near-miss | pass | API pricing |
| D9 | I'm about to start a big refactor, what effort should I use? | no load, use choose-effort | boundary | pass | Before the work, not after |
| D10 | Why is my Anthropic API bill so high this month? | no load | near-miss | pass | API billing is out of scope |
| D11 | Speed up my Node build | no load | unrelated | pass | Not usage |
| D12 | How can I use less in Claude Code from now on? | no load, use choose-effort | boundary | pass | Going forward, no past session |
| D13 | Claude.ai says I've hit my message limit, why? | no load | near-miss | pass | Claude.ai chat, not Claude Code |
| D14 | Why did yesterday's Codex automation burn through my limit? | load | clear | pass | A finished run with an affected usage window |
| D15 | My quota dropped after an Ultra run. What did each agent cost? | load | clear | pass | Account data alone cannot attribute subagent cost |
| D16 | Should I use Ultra or High for tomorrow's Codex migration? | no load, use choose-effort | boundary | pass | Upcoming task |
| D17 | Set up a cheaper reader model for all my Codex projects | no load, use setup-claude-advisor | boundary | pass | Persistent model configuration |
| D18 | How much does my Codex plan include? | no load, use official docs | near-miss | pass | Plan allowance |
| D19 | Why did yesterday's run eat my limit? (active host: Claude Code) | load | runtime | pass | Requests the Claude Code usage breakdown without asking the user to pick a host |

Boundary pairs: D1 against D9 (after versus before the work); D4 against D12 (a session that ran versus use less from now on), whose other side is C11 in `choose-effort`.
