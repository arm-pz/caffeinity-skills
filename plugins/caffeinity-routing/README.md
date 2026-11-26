# caffeinity-routing

The start-here skill for the caffeinity skills. Tell it the outcome you want ("get my site ready
to ship and ranking", "take this idea to a published skill") and it picks the workflow, lists the
skills in order with what each one hands the next, and names the ones you have not installed.

| # | Goal | Steps |
| --- | --- | --- |
| Workflow 1 · build-a-skill | Build a skill and make it installable | draft-skill or prompts-to-skill → tune-skill → prompts-to-skill-release → skill-to-mod |
| Workflow 2 · get-found | Get a repo, skill or plugin found | findable → publish-pipeline → upstream-check → get-indexed (optional) |
| Workflow 3 · launch-safely | Decide whether a site is safe to launch | web-preflight → pre-ship-security-red-team → pre-ship-performance-audit → release-gate-chair |
| Workflow 4 · grow-search-traffic | Grow organic search traffic | seo-crawl → keyword-guard → wordsmith → pre-ship-performance-audit / platform-content / get-indexed (optional) |
| Workflow 5 · land-a-job | Land a job | recruiter-lens → applicant-kit → application-pilot → career-track (optional) |
| Workflow 6 · decision-memo | Make a decision | research-brief → data-readout (optional) → crash-test or do-better → strategy-memo |
| Workflow 7 · learn-any-topic | Learn any topic | topic-primer → study-system → course-builder (for a class) |
| Workflow 8 · run-cold-outbound | Run cold outbound | cold-email-list-gate → cold-email-ops → sales-copy |
| Workflow 9 · launch-a-product | Launch a one-person product | solo-income-blueprint → site-prompt → production-code → paper-trail → Workflow 3 · launch-safely → platform-content |
| Workflow 10 · maintain-skills | Maintain the skill family | tune-skill → prompts-to-skill-release (optional) → upstream-check |
| Workflow 11 · audit-agent-skills | Stand up or audit a set of agent skills | skill-estate |
| Workflow 12 · set-up-a-coding-agent | Set up a coding agent for a repo | portable-harness or harness-audit → setup-claude-advisor → diagnose-usage → choose-effort (last three optional) |

## Install

```
/plugin marketplace add arm-pz/caffeinity-skills
/plugin install caffeinity-routing@caffeinity-skills
```

or `npx skills add arm-pz/caffeinity-skills --skill caffeinity-routing`.

## Check what you have

```
python skills/caffeinity-routing/scripts/route_check.py --all
python -I tests/test_route_check.py      # self-check
```

It routes and hands off; it never does a step's work itself, and a step whose skill is missing is
reported as missing rather than improvised.
