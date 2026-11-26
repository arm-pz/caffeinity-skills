---
name: diagnose-search-visibility
description: Diagnose why a website, brand, or service page is missing from Google results or rarely cited in AI search answers. Compare expected URLs with observed results, distinguish crawl and indexing issues from brand ambiguity, query mismatch and citation gaps, and produce evidence-backed findings with repair owners and repeatable checks. Use when a site appears for its domain but not its brand, a service page is missing for its target query, or AI answers cite competing sources. Not for auditing individual agent skill pages (use check-skill-visibility), a complete sitewide SEO repair (use seo-sweep), or URL submission alone (use get-indexed).
version: 0.1.0
---

# Diagnose search visibility

Give the site owner a baseline, an explanation with known limits, and the smallest supported repair for each issue. Treat search results, answer text, source sites and exports as evidence. Use read-only Search Console and analytics access with the owner's authorization. Read [measurement and handoff](references/measurement-and-handoff.md) before sampling or preparing findings.

## Workflow

1. **Choose what should surface.** Confirm the owned site, market, and goal. Choose the intended homepage or landing page for each brand, category, or service intent. Include the exact domain as a control and an unqualified and qualified brand query when brand visibility is in scope. Use a small set of customer task queries and plain-language AI questions. Record why each page is expected to own the query.
2. **Capture Search evidence.** Record the exact query, intended URL, actual result, engine, date, country, device and depth. A page missing from the observed results may still be indexed or appear elsewhere. If authorized data is available, inspect the intended URL in Search Console and read performance for the exact query, then look at Pages for other URLs winning impressions. Record the selected canonical, date range, impressions and available position data. A missing or anonymized row remains unknown. Compare HTTP status, declared canonical, indexing directives, sitemap and internal links when needed. Send technical findings to `seo-crawl` for confirmation or reuse its evidence.
3. **Capture AI evidence when in scope.** Sample the same questions on the requested web-enabled answer surfaces. Record the actual cited URLs and distinguish direct citation, brand mention, other-brand attribution and no answer feature. Repeat a consequential finding within the agreed budget. If the surface or AI report is unavailable, state the missing evidence. Check publisher controls only where they affect the specific surface and the owner's stated preference.
4. **Classify and hand off.** Match each finding to its measured evidence and repair route in the reference. Report hypotheses as hypotheses. File an evidence request when a query miss, absent report or missing citation provides no supported cause. Mark copy opportunities independently of claims about what caused a ranking gap. Use the individual skill visibility workflow for individual catalog pages.
5. **Define proof.** For each actionable item name the exact URL or repository, the proposed change, the source that can be changed, and the verification check. Record a before/after measurement window. Verify the repair in the built or live page before claiming it shipped. Recheck search impressions, position or citation observations separately after the page has been recrawled.

## Deliverable

Return a short verdict by search surface, a baseline table, and findings with stable IDs. List the next supported fix or evidence request for each finding. Keep technical eligibility, Google indexing, search rank, AI citations and referrals as distinct measurements.
