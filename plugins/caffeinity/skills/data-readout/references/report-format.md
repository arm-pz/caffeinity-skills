# Report format

The shape of the deliverable, and the fill-in rules for each part. Slots written as `[metric — supply this]` stay in the output until the user fills them; never quietly replace one with a guess.

## Section order

1. Title line: the question, the dataset, the run date.
2. Executive summary.
3. The data.
4. Findings ranked by impact.
5. Actions.
6. Chart specs.
7. Assumptions and caveats.
8. Gaps.
9. Appendix: methods and full tables, only if the numbers are not already in the body.

Keep it one document. A second "detailed" version is an appendix section, not a separate file, unless the user asks for a deck.

## Executive summary

Three to five lines. Each line: the number, its window, and the decision it changes. No method talk, no caveats, nothing you would have to retract.

Rules:

- Lead with the finding that moves the metric the user named, not the one you found first.
- Every line survives alone: a reader quoted from the meeting should not misstate it.
- If nothing actionable emerged, write that. "Across [n] rows the metric is flat and no cut differs materially" is a result; say it and name what would change the picture.
- Never open with a promise about an outcome, and never open with methodology.

## The data

Four to six lines, so a reader can judge how far to trust the rest:

- Source (file or export name, system), read date.
- n, and the grain (one row equals what).
- Window covered, plus the rows or periods excluded and why.
- Missingness on the columns the findings use.
- Anything you could not verify: a join you could not check, a definition that may have changed mid-window.

## Findings ranked by impact

One block per finding, in this fixed shape:

```
Finding <k> of <N> — <Observed|Inferred>
<Claim in one sentence, with the number, the window, and n.>
<Statistic line: test, p-value or interval, effect size. Omit only if the finding is a description, then say "descriptive, no test".>
Business implication: <one line in the user's units: revenue, cost, hours, risk>.
Confidence: <high|medium|low> because <n, missingness, the main confounder>.
```

Ranking, best to worst:

1. Changes a decision the user is making now.
2. Large in the user's own units, with a defensible interval.
3. Reliable but small, or big but uncertain.
4. Descriptive context that stops a wrong reading.

Rank on the metric the user named. Interest, novelty and how hard the calculation was are not impact. If two findings point in opposite directions, keep both visible and adjacent, with the check that resolves them.

`Observed` means the file shows it and the statistic supports it. `Inferred` means a plausible reading that still needs a check. Never let the wording of an inferred finding drift into observed territory between drafts.

## Actions

Each action names the finding it rests on, and nothing gets an action it does not deserve.

```
A<k> — <imperative, specific> | rests on Finding <k> | owner: <role, or [owner — supply this]> | moves: <metric> | by: <date or [date — supply this]> | verify by: <the measurement that will show it worked>
```

If a finding supports no action, label it context and stop there. If the user needs a decision made and sequenced across quarters, that is `strategy-memo`'s job, not a longer action list.

## Chart-spec table

One table per chart, six rows. Written for someone else to build; you are not drawing it.

| Field | What goes in it |
| --- | --- |
| Title | The takeaway as a sentence, not a label: "[metric] [moved how] for [segment] between [month] and [month]" |
| Question | What a reader should be able to answer in five seconds |
| Type and encoding | Chart type, x, y, series or colour encoding, aggregation and grain |
| Scale and order | Linear or log with the reason, axis start with the reason, sort key, time window |
| Marks | Reference or target line, error bars, annotations on named dates, direct labels versus legend |
| Delivery | Size, aspect ratio, palette with a colour-blind-safe note, what it must stay readable in when printed in grey |

Rules:

- One chart per finding. Two findings needing the same picture means one of them is not a finding.
- Choose the type from the question: part-to-whole, comparison across categories, movement over time, relationship between two variables, distribution, ranking. Name the reason in the spec.
- Log scale only with the reason stated, because it hides absolute size.
- Error bars wherever the reader is comparing estimates, not only means.
- Never write a spec for a chart of numbers you did not compute from the user's data, and never describe a screenshot you have not read. If the user shows a chart and asks what it says, quote only what they tell you is in it, or ask for the underlying rows.

## Assumptions and caveats

Bullets, each attackable on its own:

- What you held constant, and what would change the answer if it moved.
- For every forecast: the method, the holdout error behind the range, the horizon, and the assumptions the range rests on.
- For every A/B read: the design facts you assumed (assignment unit, planned end, no contamination) and whether you could check them.
- Multiple-comparison handling, or the absence of it.
- Known confounders you cannot exclude.

## Gaps

Every open slot, in one list, with who can supply it. This is where a missing figure stays visible instead of becoming a silent guess.

```
G<k> — <what is missing> — needed for: <finding, action or forecast> — ask: <the person or system that has it>
```

## Template mode

For a recurring report, ship the skeleton with variable slots and standing checks, then one version filled with the user's real numbers.

```
Run <date> | Source: <path or export> | n: <rows> (<grain>) | Window: <start>–<end>
Headline: <metric> = <value> (prev run <value>, delta <value>)
Checks: row count within band [pass|fail] | schema unchanged [pass|fail] | missingness under threshold [pass|fail] | values in range [pass|fail] | joins match [pass|fail]
Findings: <ranked blocks, fixed shape above>
Actions: <table above>
Charts: <specs above>
Assumptions / Gaps: <lists above>
```

A failed check prints at the top of the run and demotes every dependent finding to `Inferred` until it is resolved. Write the code that executes this template in `production-code`; here it stays a written procedure.
