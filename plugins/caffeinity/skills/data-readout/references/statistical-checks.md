# Statistical checks

Run these before quoting a number. They exist because a confident readout of a bad statistic costs more than no readout at all.

## Significance and effect size answer different questions

- **Significance** asks: could this difference have come from noise in a sample this size? It says nothing about size.
- **Effect size** asks: how big is the difference, in the units the business uses? It says nothing about whether the estimate is reliable.
- Report both, plus the interval. `p = 0.001` on 900,000 rows can be a 0.05% change that no one should act on. A non-significant 8% swing on 40 rows may be the most important thing in the file and simply unmeasured.
- Absolute difference and relative difference side by side. A relative lift of 50% on a base of 0.2% is a rounding error; the same relative lift on a base of 4% is a strategy.

## The four-part set

Every statistic in a readout carries four things or it stays out of the readout:

1. The test or method, named, with why it fits this data.
2. The p-value or the confidence interval (prefer the interval; it carries direction and magnitude).
3. The effect size in business units.
4. n, per group where groups are involved, and the window the n covers.

## n, and what a sample can and cannot support

- Quote n before interpreting anything. A finding on 12 rows travels as a hypothesis, not a result.
- Ask what the design could have detected. If the smallest difference the test could see is larger than the difference that would change a decision, the test is the wrong instrument: say so and state the n that would settle it.
- Independent samples means independent units, not many rows. Ten orders from one customer are one customer for most purposes. Matching the analysis unit to the assignment unit matters most in A/B tests and time-series comparisons.
- Sub-slices shrink fast. A 3% slice of a 900-row file is 27 rows; a segment-level comparison there is decoration, not evidence.

## Multiple comparisons

- Every extra cut, metric, segment, lag or arm multiplies the chances of a false positive. Testing 20 things at p < 0.05 produces roughly one "significant" result from pure noise.
- Handle it explicitly: name the primary metric and treat the rest as exploratory; or apply a correction (Bonferroni when the family is small and the tests genuinely independent, Benjamini-Hochberg when you are screening many and can accept a controlled false-discovery rate).
- State which correction you used and how many comparisons it covers. If you did not correct, label the finding exploratory and name the check that would confirm it on fresh data.
- The same rule applies to forecasts and lag searches: trying 12 lags and reporting the best one is a multiple-comparison problem wearing a different hat.

## Sample sanity: what makes a clean-looking result untrustworthy

- **Missing data with a mechanism.** Blanks concentrated in one channel, one period, or one outcome (lost deals with no revenue) bend every mean you compute. Report the missingness before the average.
- **Survivorship.** A file of current customers says nothing about the ones who left, because they are not in it. Cohort and churn questions need the rows that exited.
- **Selection.** Comparing people who chose a feature against those who did not measures the choosing, not the feature.
- **Truncated series.** A date range that starts after a launch, or ends mid-month, produces trends that are artefacts of the window.
- **Schema and pipeline drift.** A metric that changed definition halfway through the window will look like a break in behaviour. Check the definition against the earlier period before explaining the curve.
- **Duplicate and bot rows.** Double-counted events, internal accounts, crawler traffic. All inflate rates that look like performance.
- **Unequal variance and heavy tails.** Revenue, session duration and order values are skewed. Means with medians, and a check that the mean is not set by five rows.
- **Aggregation disagreement.** If the overall trend reverses inside the segments, say so plainly before recommending anything built on the overall trend.
- **Regression to the mean.** Anything selected because it was extreme will move back toward average on its own. This is the standard reason a "rescue" of a bad cohort appears to work.

## Common traps

| Trap | What it looks like | What to write instead |
| --- | --- | --- |
| Significance confused with importance | "p < 0.001, so this matters" | The effect size in business units, the interval, and whether the magnitude could change a decision |
| Average of ratios | Mean of per-row percentages, weighting tiny rows equally with huge ones | Total numerator over total denominator, and note the difference |
| Ratio metric with a moving denominator | Conversion rate "improved" while traffic shifted to lower-intent sources | The raw numerator and denominator beside the rate |
| Correlation read as cause | Two series that move together with a third cause | The hypothesis, the confounder you cannot exclude, and the check that would separate them |
| Peeking at a test | The result called at whichever glance looked best | The planned end point, or a sequential method stated up front |
| One-week seasonality | A Monday-to-Wednesday run read as a win | Full-week coverage, and weekday mix on both arms |
| Novelty and primacy | Early traffic behaves differently in the treated arm | Day-by-day effect, and a decision that waits it out |
| Percentage of a percentage | "2 points" written as "2%" | Absolute change and relative change, labelled |
| Chart axis theatrics | A truncated y-axis turning a 1% drift into a cliff | State the scale in the spec, and start ratio axes at a defensible baseline with the reason |
| Extrapolation | Last quarter's slope projected two years out | A range, the assumptions, and the shortest horizon the data supports |

## Deciding when the numbers are soft

- Underpowered and pointing one way: name the direction as a hypothesis, state the n that would settle it, and offer to keep the test running with dates.
- Significant but tiny: report it, and ask whether the cost of acting exceeds the size of the effect.
- Large but not significant: do not call it a win, do not call it a null. Say the estimate is wide, give the interval, and say what would narrow it.
- Contradictory cuts: prefer the pre-planned primary metric, publish the disagreement, and pick the check that resolves it.
- Any call where the interval crosses the decision threshold: say the data does not decide it, and hand the framework to the decision rather than dressing up a coin flip.
