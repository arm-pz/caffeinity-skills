# caffeinity-routing

The start-here skill for the caffeinity skills. Tell it the outcome you want ("get my site ready
to ship and ranking", "take this idea to a published skill") and it picks the workflow, lists the
skills in order with what each one hands the next, and names the ones you have not installed.

| # | Goal | Steps |
| --- | --- | --- |
| Brew 1 · Pour-over | Build a skill and make it installable | draft-skill or prompts-to-skill → tune-skill → prompts-to-skill-release → skill-to-mod |
| Brew 2 · Bloom | Get a repo, skill or plugin found | findable → publish-pipeline → upstream-check |
| Brew 3 · Espresso | Decide whether a site is safe to launch | web-preflight → pre-ship-security-red-team → pre-ship-performance-audit → release-gate-chair |
| Brew 4 · Cold brew | Grow organic search traffic | seo-crawl → keyword-guard → wordsmith → pre-ship-performance-audit / platform-content (optional) |
| Brew 5 · French press | Land a job | recruiter-lens → applicant-kit → application-pilot → career-track |
| Brew 6 · Cupping | Make a decision | research-brief → data-readout → crash-test → strategy-memo |
| Brew 7 · Slow drip | Learn a skill | topic-primer → study-system → course-builder (for a class) |
| Brew 8 · Nitro | Run cold outbound | cold-email-list-gate → cold-email-ops → sales-copy |
| Brew 9 · Moka pot | Launch a one-person product | solo-income-blueprint → site-prompt → production-code → paper-trail → Brew 3 · Espresso → platform-content |
| Brew 10 · Descale | Maintain the skill family | tune-skill → prompts-to-skill-release (optional) → upstream-check |
| Brew 11 · Estate roast | Stand up or audit a skill estate | skill-estate |

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
