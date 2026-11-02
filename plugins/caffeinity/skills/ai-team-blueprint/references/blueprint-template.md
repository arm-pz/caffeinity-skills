# Blueprint template

Read this at workflow step 3. Use these sections in this order. Keep each section short enough to act on.

## 1. Use case
- The chosen use case, in one sentence.
- Why: the user answers that drove the choice.
- Out of scope for v1: 2 or 3 things explicitly deferred.

## 2. Team structure
A table, one row per agent:

| Agent | Owns (one artifact) | Input | Output | Hands to | Success looks like |
| --- | --- | --- | --- | --- | --- |

Add one line on how overlap is avoided.

## 3. Agent specs and prompts
For each agent, the spec first: role, purpose, responsibilities (3 to 5 bullets), decision rules, input format, output format and success criteria. Then the prompt, ready to paste:

```
<role>You are the [Agent], one of [N] agents on [user]'s [use case] team. You own [artifact] and nothing else.</role>
<input>You receive: [exact format, from whom].</input>
<instructions>
1. ...
2. ...
</instructions>
<output>Return: [exact format and length]. Hand it to [next agent or human].</output>
<constraints>
- Do not [neighbouring agent's job].
- Cite a source for every factual claim. (Keep this when the agent states facts.)
- Use tools only for: [list].
</constraints>
<escalate>Stop and ask [user] for approval before publishing, sending, deleting, spending money or making any irreversible change. Also stop when: [use-case-specific triggers, such as low confidence or missing input]. Never ask for passwords or keys.</escalate>
```

## 4. Workflow
- A numbered flow from request to final output, or a simple text diagram such as `Request → A → B → [human review] → C → [human approval] → done`.
- Review points: where the human checks, and what they check.
- Feedback loops: what goes back to which agent when something fails, and the retry cap (default 2, then escalate).
- Assembly: who produces the final answer, and in what format.

## 5. Tool stack (lean v1)
A table with tool, job in this system, why it's needed, and cost tier. Cover only what's needed from: Claude (Projects or the app for each agent), a docs or knowledge base, a spreadsheet or database (the tracker), a task manager, communication, and light automation. Mark each optional tool "add in week 2+" when v1 can run by hand.

## 6. QA plan
- Checkpoints: where review happens (it should match the workflow).
- Common failure modes for this use case, each with its mitigation.
- Pre-launch tests: run 3 to 5 real past tasks through the team and compare with what the human did.
- Metrics: time per task before and after, the share of outputs accepted without edits, and one business metric tied to the 90-day goal. Review them weekly.

## 7. 7-day launch plan
| Day | Goal | Tasks | Done when |
| --- | --- | --- | --- |
Shape: day 1 set up tools and the tracker; day 2 agent 1; day 3 agent 2; day 4 the remaining agent or agents and the handoffs (with 4 or 5 agents, keep day 4 to wiring and simple prompts); day 5 test on real past tasks; day 6 fix the failures and tighten prompts; day 7 run live with approval gates on, then review the metrics.

## START HERE FIRST
Three actions for today, each under 30 minutes, the first one doable in the next 10 minutes.
