# Trigger cases: replace-dead-tools

Run **by hand on 2026-11-17** against the descriptions only, competing with:
get-listed, find-partners, seo-crawl, research-brief (re-checked 2026-11-21 after the
own-site handoff moved from broken-links, which isn't published, to seo-crawl). Not run
through an automated triggering loop. The script's offline self-check (`test_check_tools.py`, 14
checks) and one live run (an alive URL, a non-existent domain, and the user's own site) were run.

| # | Message | Expected skill | Pass condition | Result |
| --- | --- | --- | --- | --- |
| 1 | "Find the dead tools still sitting on those lists, so I can be the replacement." (original prompt 2) | replace-dead-tools | picks up `list-tools.csv` when present | PASS ("dead … tools still sitting on roundup articles so they can pitch themselves as the replacement") |
| 2 | "Which of the tools in these 'best project management apps' articles were discontinued or acquired?" | replace-dead-tools | runs check_tools.py, then confirms by hand | PASS |
| 3 | "Check these 12 listicle URLs for products that no longer exist." | replace-dead-tools | starts without step 1's files; builds list-tools.csv from the URLs | PASS ("or a list of article URLs") |
| 4 | "Some of the apps on those roundups redirect to other companies now. Turn that into a pitch." | replace-dead-tools | ACQUIRED verdicts come with an evidence URL | PASS (implicit) |
| 5 | "Give me a broken-entry angle for my list outreach." | replace-dead-tools | — | PASS ("broken-entry angle for list outreach") |
| 6 | "Find the listicles that name my competitors but not me." | get-listed | replace-dead-tools doesn't load | PASS |
| 7 | "Find broken links on my own website." | seo-crawl | replace-dead-tools doesn't load | PASS ("broken links on your own site (use seo-crawl)"; seo-crawl lists "find broken internal links") |
| 8 | "Is Pipedrive a dead company? Research its financials." | research-brief | replace-dead-tools doesn't load | PASS: no list context; the description is about entries on lists |

8 of 8 pass by hand.

## Executed run

Case 1 (the original prompt) was **run end to end on 2026-11-17** on the 138 tools from
get-listed's skillsmith.tech run. First pass: 12 flags. After confirmation: 0 dead, so no
replacement pitches, which the skill now reports as a normal result. Fixed from that run:
domain moves read as acquisitions, a bare "is retired" match, GitHub links checked as pages
(now a repo-level check with `--github api|search`), and a missing rebrand row in confirm.md.

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "Dead links on my site" | seo-crawl | the user's own pages |
| "Dead products on other people's lists" | replace-dead-tools | third-party list entries |
