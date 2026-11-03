# Trigger cases for agent-audit

Written to tune-skill's case format (`references/test-cases.md` in arm-pz/tune-skill). Judged from
the `description` frontmatter only. Competing descriptions read: `tune-skill`, `skill-builder`
(agent), `consistent-code-review`, `pre-ship-security-red-team`, `skill-estate`, `ai-team-blueprint`.

**Run:** hand-run on 2026-11-02 against the descriptions only. No automated triggering loop was run.

| # | Message | Expected skill | Pass condition | Result |
| --- | --- | --- | --- | --- |
| 1 | "Review my subagents in .claude/agents and tell me what's missing before we rely on them." | agent-audit | runs check_agent.py, one table per agent | PASS ("review, audit ... subagents") |
| 2 | "Our support agent keeps emailing customers without asking. Fix it." | agent-audit | L7 finding with an approval list | PASS ("acts without asking") |
| 3 | "Make my research agent production-ready." | agent-audit | all seven layers judged | PASS ("production-ready") |
| 4 | "My agent never gets picked when I ask for a code review." | agent-audit | L2 routing finding, delegation tests | PASS ("never gets picked") |
| 5 | "My SKILL.md never triggers." | tune-skill | agent-audit does not load | PASS ("Not for SKILL.md files") |
| 6 | "Review this PR for bugs." | consistent-code-review | agent-audit does not load | PASS |
| 7 | "Which agents should my agency set up first?" | ai-team-blueprint | agent-audit does not load | PASS ("Not for designing a new agent team") |

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "Audit my agents." | agent-audit | agent definitions |
| "Audit my skills." | tune-skill | SKILL.md files |
| "Is my web app safe to launch?" | release-gatekeeper / web-preflight | a live app, not an agent file |
