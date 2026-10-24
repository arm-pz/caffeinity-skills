# Trigger cases for caffeinity-routing

Written to tune-skill's case format (`references/test-cases.md` in arm-pz/tune-skill). Judged from
the `description` frontmatter only, as an agent choosing what to load would. Competing
descriptions read: `skill-launch`, `tune-and-polish`, `release-gate-chair`, `seo-polish`,
`keyword-resolver`, `recruiter-lens`, `applicant-kit`, `solo-income-blueprint`, `findable`.

**Run:** hand-run on 2026-10-23 against the descriptions only. No automated triggering loop was run.

| # | Message | Expected skill | Pass condition | Result |
| --- | --- | --- | --- | --- |
| 1 | "I've got all your skills installed. Where do I start if I want to sell a small product online?" | caffeinity-routing | names Brew 9 · Moka pot and hands step 1 to solo-income-blueprint | PASS ("which skill to use, what to run first") |
| 2 | "How do these skills fit together?" | caffeinity-routing | prints the workflow table, runs `route_check.py --all` | PASS ("how the skills fit together") |
| 3 | "Get my site ready to ship and ranking on Google." | caffeinity-routing | Brew 3 · Espresso then Brew 4 · Cold brew, says which it set aside first | PASS (quoted almost verbatim) |
| 4 | "I want to go from job hunting to an offer, step by step." | caffeinity-routing | Brew 5 · French press, step 1 recruiter-lens | PASS ("run a job search") |
| 5 | "What should I run before I deploy this?" | caffeinity-routing → release-gate-chair | routes to Brew 3 · Espresso and hands the whole gate to the chair | PASS, though release-gate-chair also matches "should we deploy"; both lead to the same chair |
| 6 | "Review my resume." | recruiter-lens | routing does not load | PASS ("Not for a request one skill already owns") |
| 7 | "Is this safe to launch? Give me a go/no-go." | release-gate-chair | routing does not load | PASS: one skill owns the verdict |
| 8 | "Take my skill idea all the way to published." | caffeinity-routing or skill-launch | either loads; routing offers skill-launch as Brew 1 · Pour-over's packaged chain | PASS with overlap: both descriptions claim it. Routing defers to skill-launch when the user wants one command |
| 9 | "My skill isn't triggering." | tune-skill | routing does not load | PASS (single-skill request) |
| 10 | "Rewrite the meta descriptions on these pages." | wordsmith or seo-polish | routing does not load | PASS (single-skill request) |

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "Which skills do I need to launch a skill, and in what order?" | caffeinity-routing | asks for the route, not the run |
| "Launch this skill end to end now." | skill-launch | asks for the packaged run |
| "What do I run to get this site safe and ranked?" | caffeinity-routing | spans Brew 3 · Espresso and Brew 4 · Cold brew |
| "Is this build safe to ship?" | release-gate-chair | one verdict, one owner |
