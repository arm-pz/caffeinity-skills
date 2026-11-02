# agent-audit

Audits an AI agent (a Claude Code subagent, a plugin's agents, or another framework's agent)
against the seven layers a production agent needs: model, instructions, tools, memory, loop,
guardrails and human approval. `scripts/check_agent.py` lints Claude Code agent files for
misspelled or plugin-ignored fields, no loop cap, no tool boundary, no stop condition and no
approval rule; the rest is judged from the file with quoted evidence. Fixes go to a generated
agent's sources, and every agent gets a routing test and a near-miss test.

```
/plugin marketplace add arm-pz/caffeinity-skills
/plugin install agent-audit@caffeinity-skills
```

Lint without the skill: `python scripts/check_agent.py .claude/agents/`

Self-check: `python -I tests/test_check_agent.py`
