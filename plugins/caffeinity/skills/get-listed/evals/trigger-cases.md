# Trigger cases: get-listed

Format from tune-skill's `references/test-cases.md`. Run **by hand on 2026-11-17** against the
descriptions only, competing with: replace-dead-tools, find-partners, research-brief,
cold-email-ops, sales-copy, searchfit-seo competitor-analyzer and on-page-seo. Not run through an
automated triggering loop.

| # | Message | Expected skill | Pass condition | Result |
| --- | --- | --- | --- | --- |
| 1 | "Find the best-of lists that name my competitors and not me. Find the author and draft the pitch." (original prompt 1) | get-listed | asks for the brief before searching | PASS ("which listicles mention my competitors and not me") |
| 2 | "Which 'top CRM tools' articles mention HubSpot and Pipedrive but not us?" | get-listed | uses the two competitors given; doesn't re-ask for them | PASS |
| 3 | "Get us onto the alternatives-to-Notion roundups our rivals are on." | get-listed | runs the `{c} alternatives` pattern | PASS ("get onto the roundups their competitors are on") |
| 4 | "Why do we never show up when people google 'best invoicing software'? I want those placements." | get-listed | targets the list articles, not the user's own page | PASS, borderline: "I want those placements" carries it. Without that clause, on-page-seo is a fair pick |
| 5 | "Draft pitches to the editors of the comparison posts that skip our product." | get-listed | drafts only and never sends | PASS ("pitch editors to add us") |
| 6 | "Which tools on these best-of lists have shut down?" | replace-dead-tools | get-listed doesn't load | PASS ("Not for spotting dead tools on those lists") |
| 7 | "Find guest post partners in the HR space." | find-partners | get-listed doesn't load | PASS |
| 8 | "Do a competitor analysis of Pipedrive's pricing and positioning." | research-brief / competitor-analyzer | get-listed doesn't load | PASS ("general competitor research (use research-brief)") |

| 9 | "Get us onto the awesome-claude-skills lists our competitors are on." | get-listed | reads CONTRIBUTING before drafting; uses the PR or issue-form shape | PASS ("awesome lists", added 2026-11-17 after the run showed most targets in this category are GitHub lists) |

9 of 9 pass by hand. Case 4 is the weakest. Watch it in real use.

## Executed run

Case 1 (the original prompt) was **run end to end on 2026-11-17** against skillsmith.tech, with
the output in `proof/skillsmith-tech/`. The pass conditions held: brief before search, the naming
decision by script (18 of 19 qualified), published contact routes only, 2 ineligible GitHub lists
held back. Defects it exposed were fixed in the same pass: the GitHub-list route and gate, the
raw-README fetch, badge-host filtering, and proof lines needing a source.

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "Find the lists my competitors are on and I'm not" | get-listed | finding the lists is the input |
| "Which tools on these lists are dead?" | replace-dead-tools | the lists already exist |
| "Find lists we're missing from, then which entries on them are dead" | get-listed → replace-dead-tools | starts here and hands over `list-tools.csv` |
