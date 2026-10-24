---
name: data-readout
description: >-
  Raw numbers turned into a decision: dataset interpretation, statistics with
  the business implication of each finding, chart specifications, pattern and
  anomaly detection, forecasts built on stated assumptions, segmentation, A/B
  test significance, dashboard metric selection and report templates, output
  as an executive summary, findings ranked by impact and the specific actions
  they support. Use whenever someone brings data, a spreadsheet, a CSV, an
  analytics export, an A/B result or an unexpected number and asks what it
  means, what to chart, whether the test won or which metrics to track, even
  if they never say analysis. Not for writing the pandas or R code that
  crunches the file (use production-code), for market research outside the
  user's own data (use research-brief) or for the strategic roadmap that
  follows (use strategy-memo).
---

# Data Readout

## Overview

Turns the numbers the user already owns (a CSV, a spreadsheet, an analytics export, an A/B result, one unexpected figure) into a written readout: what the data says, how strongly it says it, and which action that supports. Nothing in the output is a guess about the file, and anything you could not compute is listed as a gap rather than filled in.

## Intake

What it needs, in order of importance:

- The data itself: a path you can read, or rows pasted into the chat.
- The business question in the user's own words ("are we losing the small accounts", "did the test win").
- The decision the answer feeds and who reads it.
- Scope the file cannot tell you: which date range, which rows to exclude, what counts as one unit.
- For an A/B test: assignment unit, arms, start and end dates, the one primary metric, anything else watched.
- For a forecast: the horizon, and any known break in the series (price change, outage, launch, seasonal event).

Rules:

- **Read the file before you describe it.** If the data is on disk, open it and take the row count, column names, types and missingness from what you actually see, never from a guess about it. Report n.
- **Ask once, in a single message, and cap it at three questions.** If the user says go, proceed and print the assumptions you used.
- **No file and no numbers means no invented dataset.** Ship the framework with `[metric — supply this]` slots, or ask for the export.

## Modes

| The user asks | You deliver |
| --- | --- |
| "What does this data say?" (dataset interpretation) | Findings in plain English ranked by business impact, each carrying its n and its observed-or-inferred label |
| "Run the numbers" (statistical analysis) | Each statistic with test, p-value or interval, effect size, and the business implication in one line |
| "What should I chart?" (chart specification) | A written build spec per chart: axes, encoding, scale choice, sort order, annotations, and why that chart answers that question |
| "Is there a trend or a hidden pattern?" (pattern detection) | Candidate trends, correlations and outlier clusters with the statistic behind each, plus the ones that look like patterns and fail the check |
| "Where is this heading?" (forecast) | A range over the stated horizon, never a point, with the assumption list attached so any stakeholder can challenge it |
| "Split it by segment" (segmentation) | Segments with size, behaviour, the metric that differs, and the strategic implication of each |
| "Did the test win?" (A/B interpretation) | Significance, effect size, guardrail read, and one call: ship, keep running, or stop, with the reason |
| "Which metrics should I track weekly?" (dashboard selection) | A metric list, each with definition, formula, owner, review cadence, and a target marked `[target — yours to set]` unless the user gave one |
| "Make this repeatable" (report template) | A template mapping raw input to a formatted executive report, plus the checks every run must pass |
| "This number is weird" (anomaly explanation) | Ranked hypotheses, each with the check that would confirm or kill it and what that check needs |

Method per mode: `references/analysis-playbook.md`. Statistical checks and traps: `references/statistical-checks.md`. Report shape and the chart-spec table: `references/report-format.md`.

## Output format

One artifact, in this order (fill-in rules in `references/report-format.md`):

1. **Executive summary**: three to five lines, each with a number and the decision it changes.
2. **The data, briefly**: source, n, date range, what you excluded and why, missingness.
3. **Findings ranked by impact**, each labelled `Observed` (the file shows it) or `Inferred` (a plausible reading that still needs a check).
4. **Actions**: the finding each one rests on, the owner, the metric it moves.
5. **Chart specs** for the findings that need a picture to be believed.
6. **Assumptions and caveats**, then **Gaps** listing every open slot.

Worked fragment, shown with slots rather than invented results:

```
Finding 2 of 4 — Observed
Refunds on the [tier] tier rose from [x]% to [y]% between [month] and [month]
(n = [rows] orders; [test name], p = [value]; effect size [value], 95% CI [lo]–[hi]).
Business implication: [one line tying the number to revenue, retention or cost].
Action: [owner] verifies [specific check] by [date]; watch [metric] weekly.
Confidence: [high|medium|low] because [n, missingness, the one confounder].
```

## Quality bar

- A pattern you can see is not a finding until it has a number and a test behind it. Never infer significance from appearance.
- Never write "statistically significant" without the test, the p-value or interval, and the effect size. A big sample makes tiny differences significant; say which you have.
- Observed and inferred stay visibly separated. A plausible cause must not read like a result.
- Forecasts ship as ranges with their assumptions listed. If an assumption breaks, the forecast is void, and you say so.
- Chart specs are build instructions for someone else. Never describe a screenshot you have not seen and never draw an image of data you did not compute.
- Benchmarks and industry averages appear only with a source and a date, otherwise the slot stays empty and marked `[unverified]`. Targets are the user's to set.
- Rank findings by impact on the metric the user named, not by how interesting the calculation was.
- Say what you did not do: columns you did not inspect, joins you could not verify, tests the toolchain would not let you run.
- An anomaly earns ranked hypotheses with confirming checks, never one confident cause.

Pre-handoff check, run against your own output:

- [ ] Every number traces to the file or to a calculation you ran on it, and n is stated.
- [ ] No statistic stands without its test, interval and effect size.
- [ ] Each finding carries `Observed` or `Inferred`.
- [ ] Every forecast is a range and carries its assumptions.
- [ ] Every chart spec names axes, encoding, scale and why that chart.
- [ ] Every metric target is the user's, or sourced and dated, or an open slot.
- [ ] No promise of an outcome ("this will lift conversion"); mechanisms and evidence only.
- [ ] The Gaps list is complete and matches every slot in the body.
- [ ] Missing data, exclusions and known confounders are named, not buried.

## Handoffs

| Signal | Sibling | What you send |
| --- | --- | --- |
| The user wants the pandas, R or SQL that produces these numbers as reusable code | `production-code` | The calculation spec: input file, columns, filters, formula per metric, expected output shape, the checks you used to verify |
| A finding needs a figure from outside the user's data (market size, competitor behaviour, an industry rate) | `research-brief` | The exact question, the granularity and period needed, and how the number will be used |
| The readout supports a decision the user now has to make and sequence | `strategy-memo` | The ranked findings, the actions already implied, the constraints the data exposed |
| The user has already decided and wants the readout used to attack that decision | `crash-test` | The findings with their confidence labels, and the checks that were never run |
| The user only wants the prose of the readout tightened | `wordsmith` | The readout text with the numbers untouched |

Handoff block, in this exact shape:

```
HANDOFF — data-readout -> <target skill>
Goal: <one line>
Brief: <subject/dataset/role>
Evidence: <what the user supplied>
Assumptions: <what you assumed to continue>
Gaps: <unverified figures, missing inputs>
Next: <one line offering the target skill>
```

If the sibling is not installed, output the block anyway and say which skill normally owns it.
