# skills-to-dynamic-workflow

Turns a workflow, an ordered set of agent skills, or an existing orchestrator into a Claude Code
[dynamic workflow](https://code.claude.com/docs/en/workflows): one JavaScript file that runs each
skill as a subagent in the background and comes back with one result. It maps what every step
receives, hands on and stops on, turns approvals, pushes and deploys into resume points (a
workflow cannot ask anything mid-run), picks Sonnet or Opus per step, writes the script from a
shared preamble, and checks it with a dry run that spends no tokens.

Distilled from building the twelve caffeinity workflows as dynamic workflows
(caffeinity-skills PRs #35 and #36). `references/examples/review-a-pull-request.js` is one it
produced: consistent-code-review, then address-findings.

```
/plugin marketplace add arm-pz/caffeinity-skills
/plugin install skills-to-dynamic-workflow@caffeinity-skills
```

Check a workflow script, with no Claude login and no tokens. The checker runs the script's
top-level code against stub hooks in a separate `node:vm` context (no process, require or network,
stopped after 10 seconds or 1,000 agent calls). That is not a security boundary, so check scripts
you would be willing to run:

```
node skills/skills-to-dynamic-workflow/scripts/check_workflow.mjs path/to/workflow.js --args '{"pr": 12}'
```
