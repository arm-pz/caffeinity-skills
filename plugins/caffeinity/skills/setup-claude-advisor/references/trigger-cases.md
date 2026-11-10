# Trigger cases for setup-claude-advisor

Written to the format in tune-skill's `references/test-cases.md`. The skill under test is
`setup-claude-advisor`, judged from its `description` frontmatter. Competing descriptions
checked: `choose-effort` and `diagnose-usage`, read from their own SKILL.md files (both
v1.0.0) on 2026-11-10. Both also name `product-self-knowledge` for plan limits and prices;
that skill's file was not read.

**Run:** cases 1–9 hand-run on 2026-11-08, cases 10–12 on 2026-11-10 (v0.1.2), against the
description and SKILL.md body only. No automated triggering loop.

## Cases

| # | Message | Expected skill | Pass condition | Result |
|---|---|---|---|---|
| 1 | "Set up my Claude Code to use Sonnet as main and Opus as advisor" | setup-claude-advisor | proposes settings.json changes and the advisory rule, shows diff first | PASS |
| 2 | "Configure Claude Code with the Opus advisor pattern to save quota" | setup-claude-advisor | runs pre-flight, proposes subagent tree, shows diff preview | PASS |
| 3 | "I want Haiku for my read-only subagents and Sonnet for editing, set it up in Claude Code" | setup-claude-advisor | scans existing subagents, proposes new ones with correct models | PASS |
| 4 | "Match this subagent tree in my Claude Code setup" (with tree pasted) | setup-claude-advisor | reads the tree, checks existing agents, proposes missing ones, shows diff | PASS |
| 5 | "Why did my Claude Code session eat my whole quota yesterday?" | diagnose-usage | does not load setup-claude-advisor | PASS |
| 6 | "What effort level should I use for this overnight refactor?" | choose-effort | does not load setup-claude-advisor | PASS |
| 7 | "Upgrade my Claude Code to the latest version" | neither (not a skill job) | does not load setup-claude-advisor | PASS |
| 8 | "Optimise my $20 Claude Code plan by splitting models across roles" | setup-claude-advisor | treats this as the advisor setup workflow | PASS |
| 9 | "Add a rule to CLAUDE.md that asks the advisor before committing to a plan" | setup-claude-advisor | drafts the advisory rule block, shows it, waits for approval | PASS |
| 10 | "Can Claude Code use the cheap model for the grunt work and keep Opus for the hard calls?" | setup-claude-advisor | implicit trigger with no "advisor" or "tiering"; runs pre-flight and shows a diff preview | PASS |
| 11 | "Run the advisor setup again" (CLAUDE.md already has `## Advisor protocol`) | setup-claude-advisor | preview proposes replacing the section; the block is not appended a second time | PASS |
| 12 | "Why did my quota drain yesterday?" (`diagnose-usage` not installed) | setup-claude-advisor names the sibling | says in one line that `diagnose-usage` is not installed, answers briefly, proposes no config changes | PASS |

## Boundary pairs

| Message | Should trigger | Why |
|---|---|---|
| "Set up Claude Code model tiers" | setup-claude-advisor | configuring persistent model assignments |
| "My quota drained fast, what happened?" | diagnose-usage | post-mortem analysis of existing usage |
| "What effort level for this task?" | choose-effort | per-task effort recommendation |
| "Configure Opus as advisor" | setup-claude-advisor | the advisor pattern specifically |
| "How do I use less usage from now on?" | choose-effort | its description claims this phrase; no model-tier ask |
| "I keep hitting my limit by lunchtime" | diagnose-usage | a drain that already happened; its description claims "hit their limit sooner than expected" |
| "What does the $20 plan include?" | product-self-knowledge | plan limits and prices, not configuration |
| "Make Claude Code cheaper to run" | setup-claude-advisor (if about model tiers) or choose-effort (if about effort levels) | ambiguous — ask once which (Ground rules, "Name the sibling") |

## Not verified

- Whether `claude --version` output format matches the version parsing logic on all platforms.
- Real model behaviour for triggering. These are description-level judgements only.
- The handoff is one-way: neither sibling's SKILL.md names `setup-claude-advisor`, so a user
  who asks either of them for model tiering is not sent here.
