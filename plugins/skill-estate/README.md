# skill-estate

Takes a whole collection of agent skill repos from scattered to published, consistent and
self-maintaining, in eight gated phases: inventory, reconcile listings, test and tune, close
workflow gaps, publish and bundle, trigger tests, discovery, maintenance loop. Each phase hands its
work to the skill that owns it (upstream-check, publish-pipeline, tune-skill, draft-skill,
caffeinity-routing, findable) and ends in PRs.

Workflow Brew 11 · Estate roast in `caffeinity-routing`. Distilled from the run that set up the arm-pz skills;
`references/brief.md` keeps the eight requests behind it.

```
/plugin marketplace add arm-pz/caffeinity-skills
/plugin install skill-estate@caffeinity-skills
```
