# Trigger cases for skill-estate

Written to tune-skill's case format (`references/test-cases.md` in arm-pz/tune-skill). Judged from
the `description` frontmatter only. Competing descriptions read: `caffeinity-routing`,
`publish-pipeline`, `upstream-check`, `findable`, `tune-skill`, `skill-launch`.

**Run:** written 2026-10-24 and hand-checked against the descriptions; the automated cases in
`evals/triggers.json` (caffeinity-skills) are the ones that run.

| # | Message | Expected skill | Pass condition | Result |
| --- | --- | --- | --- | --- |
| 1 | "My skills site doesn't match my GitHub repos. Sort the whole thing out." | skill-estate | starts with the inventory phase | written |
| 2 | "Audit all 40 of my skill repos and get the ecosystem consistent." | skill-estate | phases 1 to 3, PRs per repo | written |
| 3 | "Set everything up so a new skill repo goes live on my site and profile by itself." | skill-estate | phases 2 and 5 | written |
| 4 | "Do the same cleanup we did for arm-pz on my company's skills org." | skill-estate | full run from phase 1 | written |
| 5 | "My tune-skill isn't triggering." | tune-skill | skill-estate does not load | written |
| 6 | "Why does my site list 22 skills and GitHub 27?" | upstream-check | skill-estate does not load (one drift question) | written |
| 7 | "Run this week's maintenance on the skills." | caffeinity-routing (Brew 10 · Descale) | skill-estate does not load | written |
| 8 | "Set up the GitHub Actions publish pipeline for my skills site." | publish-pipeline | skill-estate does not load | written |

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "Clean up and set up my whole skills ecosystem." | skill-estate | the whole collection, every phase |
| "Fix the drift between my site and the marketplace." | upstream-check | one phase |
| "Get my skills repo more stars." | findable | one repo's discovery |
| "Weekly health check on my skills." | caffeinity-routing | upkeep of an estate already set up |
