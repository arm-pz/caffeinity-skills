# Trigger cases for setup-claude-advisor

Written to the format in tune-skill's `references/test-cases.md`. The skill under test is
`setup-claude-advisor`, judged from its `description` frontmatter. Competing descriptions
checked: `choose-effort`, `diagnose-usage`, `choose-effort`.

**Run:** hand-run on 2026-11-08 against descriptions only. No automated triggering loop.

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

## Boundary pairs

| Message | Should trigger | Why |
|---|---|---|
| "Set up Claude Code model tiers" | setup-claude-advisor | configuring persistent model assignments |
| "My quota drained fast, what happened?" | diagnose-usage | post-mortem analysis of existing usage |
| "What effort level for this task?" | choose-effort | per-task effort recommendation |
| "Configure Opus as advisor" | setup-claude-advisor | the advisor pattern specifically |
| "Make Claude Code cheaper to run" | setup-claude-advisor (if about model tiers) or choose-effort (if about effort levels) | ambiguous — ask which |

## Not verified

- Whether `claude --version` output format matches the version parsing logic on all platforms.
- Real model behaviour for triggering. These are description-level judgements only.
