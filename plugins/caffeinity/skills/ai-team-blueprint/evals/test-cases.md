# Test cases: ai-team-blueprint

Status: written, not run.

| # | Message | Expected skill | Type | Pass condition |
| --- | --- | --- | --- | --- |
| 1 | The original one_shot_setup.xml prompt | ai-team-blueprint | original | Asks the 5 questions first and does not dump a blueprint |
| 2 | "I want to set up a small team of AI agents for my business. Where do I start?" | ai-team-blueprint | clear | Asks the 5 questions in one message |
| 3 | "Design me a 3-agent setup for content research and writing, with prompts and a launch plan." | ai-team-blueprint | clear | Skips the use-case question (already given) and asks only for the gaps |
| 4 | "Which AI agents should I have working for me? I run a 2-person marketing agency." | ai-team-blueprint | clear | Infers the business context, asks the rest, then compares the top 3 use cases |
| 5 | "I'm drowning in support emails and lead follow-ups. Can Claude take some of this off me, and how would I organise it?" | ai-team-blueprint | implicit | Recommends one use case with a reason and waits for a yes |
| 6 | "How do I split work between a researcher, writer and editor agent so they don't step on each other?" | ai-team-blueprint | implicit | Each agent owns one artifact; handoffs are named |
| 7 | "Write Python using the Anthropic SDK that runs a researcher agent and a writer agent in a loop." | claude-api | near-miss (sibling) | Does not trigger ai-team-blueprint |
| 8 | "Make me a skill that formats my meeting notes." | draft-skill | near-miss (sibling) | Does not trigger ai-team-blueprint |
| 9 | "What's the best AI tool to transcribe this one podcast episode?" | none | near-miss (out of scope) | Answers directly, with no blueprint |
| 10 | "My team blueprint for the Q3 offsite needs an agenda. Can you draft it?" | none | near-miss (keywords) | Does not trigger despite "team blueprint" |
| 11 | "Spin up a few subagents and research the top 5 CRMs for me." | none (do the task) | near-miss (added in tune) | Runs the research and produces no blueprint |

## Boundary pairs
- claude-api: #6 (design the split, which triggers) vs #7 (code it, which goes to claude-api).
- draft-skill: #2 (a team of agents) vs #8 (a single skill).
- Spanning case: "Plan my AI content team, then give me the SDK code for it" should start with ai-team-blueprint and then hand the agent specs to claude-api.
