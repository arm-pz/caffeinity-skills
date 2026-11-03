# workflow-router

The start-here skill for the caffeinity skills. Tell it the outcome you want ("get my site ready
to ship and ranking", "take this idea to a published skill") and it picks the workflow, lists the
skills in order with what each one hands the next, and names the ones you have not installed.

| # | Goal | Steps |
| --- | --- | --- |
| Workflow 1 (build-a-skill) | Build a skill and make it installable | draft-skill or prompts-to-skill → tune-skill → prompts-to-skill-release → skill-to-mod |
| Workflow 2 (get-found) | Get a repo, skill or plugin found | findable → publish-pipeline → upstream-check |
| Workflow 3 (launch-safely) | Decide whether a site is safe to launch | web-preflight → pre-ship-security-red-team → pre-ship-performance-audit → release-gate-chair |
| Workflow 4 (grow-search-traffic) | Grow organic search traffic | seo-crawl → keyword-guard → wordsmith → pre-ship-performance-audit / platform-content (optional) |
| Workflow 5 (land-a-job) | Land a job | recruiter-lens → applicant-kit → application-pilot → career-track |
| Workflow 6 (make-a-decision) | Make a decision | research-brief → data-readout → crash-test → strategy-memo |
| Workflow 7 (learn-a-skill) | Learn a skill | topic-primer → study-system → course-builder (for a class) |
| Workflow 8 (run-cold-outbound) | Run cold outbound | cold-email-list-gate → cold-email-ops → sales-copy |
| Workflow 9 (launch-a-product) | Launch a one-person product | solo-income-blueprint → site-prompt → production-code → paper-trail → Workflow 3 (launch-safely) → platform-content |
| Workflow 10 (maintain-skills) | Keep your skills healthy | tune-skill → prompts-to-skill-release (optional) → upstream-check |
| Workflow 11 (audit-a-skill-estate) | Audit all your skills | skill-estate |

## Install

```
/plugin marketplace add arm-pz/caffeinity-skills
/plugin install workflow-router@caffeinity-skills
```

or `npx skills add arm-pz/caffeinity-skills --skill workflow-router`.

## Check what you have

```
python skills/workflow-router/scripts/route_check.py --all
python -I tests/test_route_check.py      # self-check
```

It routes and hands off; it never does a step's work itself, and a step whose skill is missing is
reported as missing rather than improvised.

Every run starts with a brief (what you expect, what done looks like, what is out of scope) and
ends with a report that puts the evidence first, then the decisions it made for you, then what its
checks did not cover, and the summary last. The workflow agents in the `caffeinity` plugin follow
the same contract: `skills/workflow-router/references/report-contract.md`.
