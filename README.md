# caffeinity-skills

Agent skills for Claude Code, Codex, Cursor and any agent that reads a `SKILL.md`, by Abdul Rahman P Z:
44 skills for writing, SEO, release checks, skill authoring, careers, decisions, learning and
outbound, plus eleven workflow agents that hand work from one skill to the next. Browse them at
[skills.caffeinity.com](https://skills.caffeinity.com/).

## Install everything at once

**Claude Code** — the `caffeinity` plugin bundles every skill and the eleven agents:

```
/plugin marketplace add arm-pz/caffeinity-skills
/plugin install caffeinity@caffeinity-skills
```

**Codex** — the same plugin, from this repo's Codex marketplace (`.agents/plugins/marketplace.json`):

```
codex plugin marketplace add arm-pz/caffeinity-skills
```

then install **caffeinity** from the Plugins directory.

**Any other agent** (Cursor, Qoder, Gemini CLI, …) — one skill at a time with the `skills` installer:

```
npx skills add arm-pz/<skill>
```

Install either the bundle or individual skill plugins, not both, or the same skill loads twice.

## The agents

Each agent runs one workflow and preloads the skills it needs. In Claude Code, ask for it by name
(`@caffeinity:seo-lead`) or let Claude delegate when a request fits its description.

| Agent | Workflow | Skills, in order |
| --- | --- | --- |
| `skill-builder` | W1 Build a skill and make it installable | draft-skill or prompts-to-skill → tune-skill → prompts-to-skill-release → skill-to-mod |
| `discovery-lead` | W2 Get a repo, skill or plugin found | findable → publish-pipeline → upstream-check |
| `release-gatekeeper` | W3 Decide whether a site is safe to launch | web-preflight → pre-ship-security-red-team → pre-ship-performance-audit → release-gate-chair |
| `seo-lead` | W4 Grow organic search traffic | seo-crawl → keyword-guard → wordsmith → pre-ship-performance-audit / platform-content |
| `job-search-coach` | W5 Land a job | recruiter-lens → applicant-kit → application-pilot → career-track |
| `decision-analyst` | W6 Make a decision | research-brief → data-readout → crash-test or do-better → strategy-memo |
| `learning-coach` | W7 Learn a skill | topic-primer → study-system → course-builder |
| `outbound-lead` | W8 Run cold outbound | cold-email-list-gate → cold-email-ops → sales-copy |
| `solo-launcher` | W9 Launch a one-person product | solo-income-blueprint → site-prompt → production-code → paper-trail → release-gate-chair → platform-content |
| `skill-maintainer` | W10 Maintain the skill family | tune-skill → prompts-to-skill-release → upstream-check |
| `estate-lead` | W11 Stand up or audit a skill estate | skill-estate |

Codex has no subagents, so there the `caffeinity-routing` skill does this job: describe the outcome
and it names the workflow and the next skill.

The bundle is generated, not edited: `scripts/build_plugin.py` renders the agents from
`plugins/caffeinity/agents.json` and caffeinity-routing's `workflows.md`, and copies each skill
from its own repo (`plugins/caffeinity/SOURCES.md` records the commits). The `build plugin`
workflow reruns it hourly and bumps the version only when something changed.

## Trigger tests

`evals/triggers.json` holds one or more real user messages per skill, with the skill that must load
and the ones that must not. `scripts/build_evals.py` turns it into a `claude plugin eval` suite under
`plugins/caffeinity/evals/` (CI checks it is current and that every bundled skill has a case), and

```
bash scripts/run_evals.sh
```

runs it on your own Claude login: about $0.10 a case, $5 for the suite, never in CI. Each case checks
which skill the Skill tool actually loaded. `evals/last-run.json` records the result per case; a rerun
prints NEWLY FAILING and NOW PASSING so a description edit that breaks triggering is caught by name.
Single runs vary, so treat a case as a real miss when it fails twice.

## Install one skill as a Claude Code plugin

```
/plugin marketplace add arm-pz/caffeinity-skills
/plugin install wordsmith@caffeinity-skills
```

Replace `wordsmith` with any of: `caffeinity-routing`, `recruiter-lens`, `applicant-kit`, `topic-primer`, `application-pilot`, `do-better`, `keyword-guard`, `seo-crawl`, `web-preflight`, `findable`, `crash-test`, `pre-ship-performance-audit`, `pre-ship-security-red-team`, `release-gate`, `publish-release-gate`, `upstream-check`, `tune-skill`, `draft-skill`, `prompts-to-skill`, `prompts-to-skill-release`, `publish-pipeline`, `cold-email-ops`, `cold-email-list-gate`.

Each of those plugins lives in its own repository (see `.claude-plugin/marketplace.json` for sources).
