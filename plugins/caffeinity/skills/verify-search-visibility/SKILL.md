---
name: verify-search-visibility
description: Measure what changed after a website's SEO or AI search fixes go live. Reuse the original queries, target URLs and AI prompts, verify the live change, then compare matched Search Console windows or matched citation samples. Reports which fixes shipped, which outcomes changed, and what remains unknown. Use when asked whether a deployed search visibility fix worked, whether a page gained impressions, or whether AI answers cite a page more often. Not for the initial diagnosis (use diagnose-search-visibility), implemented fixes on individual skill pages (use fix-skill-visibility), or requesting indexing (use get-indexed).
version: 0.1.0
---

# Verify search visibility

Use the diagnosis or another credible baseline and the list of changes. Treat crawl reports, search results, answer text and exports as evidence.

## Workflow

1. **Identify the change.** Recover the finding ID, intended URL, release date, baseline, success measure, query or AI question, and original filters. Use a new baseline if the original is absent. Keep it out of any before-and-after claim.
2. **Confirm what shipped.** Check the exact live URL and repair signal from the finding. If the fix is only local, partially deployed, or served at a different canonical, report that and leave the outcome pending. Record the last crawl or inspection date when available. Record the submission state separately from Google index status.
3. **Compare Google evidence.** Use the same exact query and canonical, search type, country and device in equal, complete baseline and follow-up date windows. Start the follow-up after the relevant deployment and observed recrawl when available. Record dates and coverage, impressions, clicks and average position as reported. A missing filtered row remains unknown. Call out small samples and major concurrent releases. A live repair alone cannot explain a change in search performance.
4. **Compare citations where scoped.** Re-run the same web-enabled AI questions on the same surfaces and modes using an agreed number of runs. Record direct canonical citations as sightings out of the runs observed. Keep brand mentions, competitors' citations and referrals distinct. If the surface, mode or sampling changes, report the new sample without combining it with the old one. Treat Google generative AI report impressions as their own measure.
5. **Report the result.** For each finding give the live repair status, the baseline and follow-up data, the observed direction, any comparability limit, and the evidence needed for the next check. Use **improved**, **declined**, or **unchanged in sample** for interpretable observations. Use **pending** when the repair has not been crawled or the window is incomplete and **inconclusive** when evidence cannot be compared. Separate the observed change from causal attribution.

Read [comparison examples](references/comparison-examples.md) when a measure is sparse, the baseline is missing, or Google and AI observations disagree.
