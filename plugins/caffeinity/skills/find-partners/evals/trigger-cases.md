# Trigger cases: find-partners

Run **by hand on 2026-11-17** against the descriptions only, competing with:
get-listed, replace-dead-tools, research-brief, cold-email-ops, searchfit-seo
content-strategy. Not run through an automated triggering loop.

| # | Message | Expected skill | Pass condition | Result |
| --- | --- | --- | --- | --- |
| 1 | "Swap links for me. My articles link out to other real businesses on the same connector, theirs link back to me." (original prompt 3) | find-partners | says once why a swap is a link scheme, then finds collaborations; builds no swap list | PASS ("swap links for me, find link exchange partners") |
| 2 | "Find non-competing SaaS companies we could co-market with." | find-partners | excludes the brief's competitors | PASS ("who could we co-market with") |
| 3 | "Who could we guest post for in the freelancer niche?" | find-partners | screens red flags before listing | PASS ("guest post opportunities") |
| 4 | "We need more backlinks, but not from best-of lists. Who could we make content with?" | find-partners | — | PASS (implicit; "not from best-of lists" steers away from step 1) |
| 5 | "Find podcasts and newsletters our buyers read that might feature us." | find-partners | collab_type is podcast or newsletter feature | PASS (implicit) |
| 6 | "Find the best-of lists that name my competitors and not me." | get-listed | find-partners doesn't load | PASS ("Not for best-of list outreach") |
| 7 | "Plan inbox and domain capacity for 20k cold emails a month." | cold-email-ops | find-partners doesn't load | PASS: no shared trigger words |
| 8 | "Research who our competitors partner with and summarise their strategy." | research-brief | find-partners doesn't load | PASS, borderline: shares "partner"; the "competitor research (use research-brief)" clause decides it |

8 of 8 pass by hand. Case 8 is the weakest.

## Executed run

Run end to end on 2026-11-17 for skillsmith.tech after the other two steps: 7 partners kept, 1 link
seller dropped (a dofollow menu plus an invoice), 4 asks written. Fixed from that run: the
link-type menu as a single drop flag, AI-hosted podcasts as a flag, green flags, and how to pitch
publishers that refuse promotion.

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "Find businesses we could swap links with" | find-partners | converts the swap into collaborations |
| "Get us onto existing roundups" | get-listed | list placement, not partnership |
