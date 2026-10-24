# Analysis playbook

What to actually do in each mode: the run, the report, and the claim you must not make.

## Always first: profile the file

Do this before any mode, every time the data is on disk.

1. **Open the real file.** Take the row count, column names, types, and date range from what you see. If you cannot open it, say so and ask for the rows pasted, and scope the readout to what you were shown.
2. **Confirm the grain.** Is one row one order, one user-day, one session, one export line? State the grain in one sentence. Most wrong conclusions come from mixing grains (a per-user metric divided by per-session rows).
3. **Check duplicates and joins.** Same key twice, foreign keys with no match, rows that appear in one system but not the other. Report counts, not vibes.
4. **Measure missingness per column**, then judge its kind: missing at random, missing with a visible pattern in another field, or missing because of the outcome itself (a lost deal with blank revenue). The last one biases every mean you compute; name it before quoting one.
5. **Hunt sentinel values:** `-1` or `0` used for unknown, empty strings, `N/A`, test accounts, internal staff emails, bot traffic, refunded orders counted as revenue.
6. **Publish the profile** (source, n, grain, range, exclusions, missingness) at the top of the readout. Every later number inherits it.

---

## Dataset interpretation

**Run.** Start from the user's question, not from the columns. Compute the two or three aggregates that answer it, then look for the surprise: the segment, period or cohort that behaves differently from the headline.
**Report.** Plain-English findings, ranked by impact on the metric the user named. Each finding: the number, its n, the window, and whether it is `Observed` or `Inferred`.
**Do not claim.** That a finding matters because it is large. Size means nothing until it is priced against the user's own unit economics, or compared to their own history with a stated baseline.

## Statistical analysis

**Run.** Pick the test by data type and distribution, not by habit. Check its assumptions (independence, roughly symmetric errors, variance behaviour, sample size) before trusting it. Where the assumptions fail, use the non-parametric or resampled alternative and say you switched.

| Question | Statistic | Also report |
| --- | --- | --- |
| Difference between two groups, continuous | t-test, or Mann-Whitney if heavy tails | mean or median difference, CI, n per group |
| Difference between two groups, proportions | two-proportion z-test, or chi-square with small-cell caution | absolute and relative difference, CI |
| More than two groups | ANOVA on one factor, or a regression with the real confounders in | effect sizes, follow-up tests with correction |
| Relationship between two continuous variables | Pearson, Spearman if non-linear monotonic | n, CI on the coefficient, and what a third variable could do |
| Change over time | slope with CI, or a model with seasonality in | R² only as a secondary note, plus residuals |
| Share of an outcome explained by several inputs | regression coefficients, standardised | collinearity warning if inputs move together |

**Report.** The four-part set every time: test name, p-value or interval, effect size, n. Then one line of business implication: what the number costs, saves, or changes in decision terms. If it converts to money, show the formula and pull each input from the user's data, with `[metric — supply this]` where they have not given it.
**Do not claim.** Significance without effect size. "No effect" from a non-significant result on a small sample; that is "this test cannot tell".

## Chart specification

**Run.** Choose the chart from the question the reader must answer, from `references/report-format.md`. Specify, never draw.
**Report.** A spec with: title written as the takeaway sentence, the question it answers, chart type, x, y, series or colour encoding, aggregation and grain, sort order, time window, scale (linear or log, and why), reference or target line, annotations on named dates, error bars where the estimate has uncertainty, direct labels instead of a legend where possible, colour-blind-safe palette, and the size it will be shown at.
**Do not claim.** To know what a chart the user is holding looks like. Describe only what you computed from their data. Never produce an image of numbers you did not run, and never narrate a screenshot as if you had read it.

## Pattern detection

**Run.** Test each candidate separately: trend (slope with CI over a stated window), seasonality (compare like periods, not adjacent ones), correlation (with n, and a named confounder you cannot rule out), distribution shape (bimodality, fat tails), outlier clusters (a group that behaves differently, not one weird row), and lagged relationships (check how many lags you tried before you quote one).
**Report.** Two lists: patterns that survived the check, each with its statistic; and patterns that look real in the shape of the series and do not survive it. The second list is what stops a bad decision.
**Do not claim.** That a correlation is a cause. Offer the mechanism as a hypothesis with the check that would separate it from the confound.

## Forecast

**Run.** Match the method to the series shape: rolling mean for a noisy flat series, seasonal decomposition when the calendar matters, exponential smoothing when recent behaviour dominates, a fit on a log scale when growth is proportional. Hold out the most recent period and report the error you actually made on it. Build the range from that error, widened for whatever the holdout could not see (launch, outage, price change, season).
**Report.** The range with its basis (backtest error, horizon, method), the assumption list a stakeholder can attack (what is held constant, what would break it, which single assumption moves the range most), and the point estimate only as the middle of the range.
**Do not claim.** A single number as "the forecast". A projection is what the data implies under these assumptions, not a prediction of the future.

## Segmentation

**Run.** Fix the segmentation variable before you compute, on grounds the user can see (tier, channel, cohort month, region, plan), and keep segment count small enough that each has an n worth quoting. For each segment: size, share of the outcome, the metric that differs, and the test for that difference with a multiple-comparison correction because you ran several at once. Check whether the aggregate and the segments disagree (Simpson's paradox) and say so when they do.
**Report.** A table of segments with size, metric, spread, and the strategic implication in one line each: defend, grow, fix, or drop, plus what it would cost to be wrong about that call.
**Do not claim.** That a small segment's extreme rate is a strategy. Quote the n and the interval next to it.

## A/B test interpretation

**Run.** Audit the design before the numbers: assignment unit versus analysis unit, the sample-ratio check against the intended split, contamination or overlap between arms, calendar coverage (at least one full week, and no holiday-only run), and whether anyone looked at the result before the planned end. Then compute the primary metric once, as the pre-registered metric, with a test, effect size and CI; then read the guardrails.
**Report.** n per arm, the primary metric difference with CI, p-value, the smallest effect the design could have detected, guardrail results, and one call: ship, keep running (with the extra n and dates that would settle it), or stop (with the reason). If the test is underpowered, the honest call is "this test cannot answer the question", and say what would.
**Do not claim.** A win from a result that crossed the line once after repeated peeking. Do not promote secondary metrics that were never the primary one.

## Dashboard metric selection

**Run.** Ask what decision the dashboard changes each week, then pick the fewest metrics that make that decision visible: one headline number that moves with the thing the team controls, one or two counters that expose a metric being gamed (quality against volume, retention against acquisition), plus the leading indicator if the headline lags. For each: exact formula, source table or tool, grain, owner, review cadence, and the data-quality check that tells you the number is broken rather than bad.
**Report.** A metric table with a target column. Targets are the user's to set: leave `[target — yours to set]` unless they supplied one, or unless you have a source and a date to quote.
**Do not claim.** An industry benchmark you have not sourced and dated, or a target you invented. Do not promise that tracking a metric produces an outcome.

## Report template

**Run.** Build the repeatable skeleton in `references/report-format.md`: a slot list (source path, run date, n, window, headline metric, variance against the previous run), the fixed calculation order, and the standing checks: row count within the expected band, no new or renamed columns, missingness under the agreed threshold, values inside plausible ranges, joins still matching.
**Report.** The template plus a "first run" version filled with the user's real numbers, and the checks listed as pass/fail lines so a bad run announces itself.
**Do not claim.** That the template auto-runs. It is a written procedure until the user has code that executes it, which is `production-code`'s job.

## Anomaly explanation

**Run.** Quantify the anomaly first: how far from the expected band, over what window, and how many units it covers (one account, one channel, one day). Then rule out data artefacts before real causes: pipeline change, backfill, de-duplication, timezone shift, a renamed field, a bot filter that stopped working, a test account. Then list the plausible business causes, ranked by how much of the anomaly each explains and how cheaply each can be checked.
**Report.** A ranked hypothesis table: hypothesis, the check that confirms or kills it, what that check needs (a table, a date, access), and what it costs to be wrong. Say explicitly which hypotheses you could not test.
**Do not claim.** A single confident cause. An unexplained anomaly stays unexplained, with the shortest check named as the next step.
