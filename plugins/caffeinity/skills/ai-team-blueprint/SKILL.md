---
name: ai-team-blueprint
description: Guide a solo operator or small business from "I want an AI team" to a ready-to-run v1 blueprint for a team of 3 to 5 Claude agents. Asks five sharp questions, recommends one starting use case, then delivers the team structure, a production prompt per agent, the handoff workflow, a lean tool stack, a QA plan and a 7-day launch plan ending in START HERE FIRST. Use whenever someone wants to set up their first AI agents or multi-agent team, asks which agents they need, how to split work between agents, how to get Claude to take a recurring chunk of their work off their plate, or how to use AI agents for content, lead generation, support, research or operations, even if they never say "blueprint" or "team". Not for writing agent code against the Claude API or Agent SDK (use claude-api), building a single skill (use draft-skill), running agents on a task right now, or picking one AI tool for a one-off task.
---

# ai-team-blueprint

Turn a vague wish for "an AI team" into a small, real system one person can run. The output is a single blueprint document. The work is mostly judgement: picking the narrowest use case that pays off, and keeping the team small enough to actually launch.

## Rules that apply throughout

- **Narrow beats impressive.** Recommend 3 agents unless the use case clearly needs a 4th or 5th. Every extra agent adds a handoff that can break, and a beginner debugging five agents gives up.
- **Real, not a demo.** Every agent must produce an output a human would otherwise make by hand. If an agent only "coordinates" or "thinks", cut it or merge it.
- **Evidence before big decisions.** Base the use-case pick on the user's answers, and say which answer drove it. If the answers conflict, ask instead of guessing.
- **Human approval gates.** Every agent prompt and the workflow must stop for the user's approval before publishing, sending, deleting, spending money, or any irreversible change. These gates are the main safety mechanism for a beginner's first system, so never drop one to make the flow smoother.
- **No secrets in chat.** Never ask for passwords, API keys or tokens. When a tool needs credentials, say where the user enters them (the tool's own settings or an environment secret), not that they should paste them.
- **Model-agnostic.** Recommend "the current most capable Claude model" for reasoning-heavy agents and a faster, cheaper Claude model for high-volume simple steps. Don't hardcode a version name, because the blueprint will outlive it.

## Workflow

### 1. Ask five sharp questions, once

Ask them in one message, numbered, and skip any the user already answered:

1. What outcome do you want in the next 90 days? (Revenue, hours saved, output volume.)
2. What are your skills? Can you edit a spreadsheet, use no-code automation, or write a little code?
3. How many hours a week can you give this, both to set it up and to run it?
4. Do you already have a use case in mind?
5. What is the first concrete task you want off your plate?

Infer from the conversation where you can, for example from connected tools or the user's business. If the user wants to skip the questions, state your assumptions and go on.

### 2. Recommend one use case

Score the realistic options against the answers using `references/use-cases.md`, and show a short comparison of the top three. Recommend one, give a one-line reason tied to the user's answers, and ask for a yes before building. The whole blueprint hangs on this choice, so it is the one point worth pausing for.

### 3. Build the blueprint

Follow `references/blueprint-template.md` exactly; where it and this file disagree, this file wins. It fixes the section order, the per-agent spec, the prompt format and the 7-day plan shape. Write each agent prompt so it can be pasted straight into a Claude Project or system prompt.

Keep agents from overlapping: each owns one artifact, and the workflow section names who hands what to whom. If two agents could both produce the same thing, merge them.

### 4. Deliver

The blueprint is long-lived material the user will edit and come back to, so put it in a document or page when the environment offers one, and keep chat for a short summary. Otherwise give it as Markdown. End with **START HERE FIRST**: the three actions for today, each under 30 minutes.

## Handoffs

- **To code:** if the user wants the team built in code with the Claude API or Agent SDK, offer one line handing over to `claude-api`. Pass the team-structure table, the agent prompts and the workflow section as they are. If `claude-api` isn't installed, say so and stop at the blueprint. Don't write the code here.
- **Doing, not designing:** if the user wants agents run on a task now, skip the blueprint and just do the task.

## Check before handing over

- 3 to 5 agents, each with a distinct output and named handoffs.
- Every agent prompt has an escalation section with the approval gates.
- The tool stack has no tool the 7-day plan doesn't use.
- The QA plan has at least one metric that shows whether the team actually saves time or makes money.
- No hardcoded model version, and no request for secrets.
