# Measurement and handoff

## Sample and record

Begin with one homepage and up to three other business-critical pages. Let the brief determine the budget. A useful brand sample is the exact brand, brand plus qualifier, and domain control. A service sample is one category query and one buyer task query per intended page. Review at least the first results page as shown. Preserve the same query, language, country, device, engine and depth on follow-up.

| Surface | Record | Interpretation |
| --- | --- | --- |
| Public Google results | Exact query, visible URL, competing result URLs, date, locale, device and depth | Evidence for this observation only |
| Search Console URL Inspection | Inspected URL, indexed result, selected canonical, last crawl if available | Evidence for Google index state and canonical choice |
| Search Console Performance | Query and Pages views, comparison windows, filters, impressions, clicks and average position as available | Performance history under the selected filters |
| Google generative AI performance report | Report availability, covered surfaces, pages and impressions by date and filters | AI-feature impressions, with a missing report treated as unknown |
| Web-enabled AI answers | Exact question, provider/mode, date, locale if known, whether web sources were used, and cited URLs | An observed citation or mention. Record each run separately |
| Analytics | Referrals with the source and attribution window when available | Visits. A referral count does not estimate citation count |

When access is missing, continue with the public baseline and name the unavailable checks. Never substitute a general search provider for Google without labeling it. Separate Google's Web totals from its generative AI report. Avoid summing overlapping measures. Never count a brand mention without a citation URL as a citation. When answers are variable, record the number of observed runs and describe the change in that sample without projecting a general ranking.

Evaluate visible, useful answers and supporting evidence, plus crawl and index controls that the platform actually documents. For Google AI features, skip special markup and AI text files as proposed ranking fixes. For ChatGPT Search, consult publisher guidance for OAI-SearchBot and referral attribution. Respect intentional publisher exclusions.

## Route the finding

| Evidence | Send to | Required proof |
| --- | --- | --- |
| Verified unintended block, canonical conflict, or missing crawl path | SEO Crawl for technical evidence, then SEO Sweep for the scoped source change | Re-fetch live canonical, status, directive or crawlable link. Inspect selected canonical separately |
| Multiple pages demonstrably compete for the same intent | Keyword Guard, then Keyword Resolver | Document the intended owner and verify changed copy and links. Check later query/page data |
| Ambiguous brand or stale external listings | Findable and Findable Polish | Check the specific signal, such as a GitHub homepage or conflicting label. Re-read the authorized listing after change |
| Service page gives weak answers or hides proof | Wordsmith for copy, then the site maintainer for implementation | Verify readable copy, supporting links and claims in the rendered page |
| An individual agent skill is missing or outranked | Check Skill Visibility, then Fix Skill Visibility | Pass its URL-level report and require verification by finding ID |
| Eligible public fixes need a submission plan | Get Indexed | Record the authorized submission or manual inspection. Indexing and ranking still need separate evidence |

For each finding record `id`, `targetUrl`, `surface`, `queryOrPrompt`, `evidence`, `status`, `owner`, `proposedAction`, `fixCheck` and `outcomeCheck`. Use `actionable` for supported changes and `inconclusive` for missing evidence. Use a source URL or evidence file in each finding and preserve the baseline. Never claim that a task query miss, a single zero-citation answer or an absent metric proves root cause.

[Google URL Inspection](https://support.google.com/webmasters/answer/9012289) · [Google Search performance](https://support.google.com/webmasters/answer/17010961) · [Google generative AI performance report](https://support.google.com/webmasters/answer/16984139) · [Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features) · [OpenAI publisher guidance](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)
