# Gate rules and report template

Thresholds come from one operator's account:

> Will Breton (@bretonwill), "Everything I Learned From Managing 3.5M+ Cold Emails/Month",
> X article, 18 October 2026.

The 10-row sample and the "2 wrong means the list is wrong" rule are his. The 50–100
contact provider sample is an adaptation: the source compared phone providers on dials
per in-profile person, not email valid-contact rate. Treat all of it as a starting
threshold, not a law, and label borrowed figures "source benchmark" in the gate report.

| Rule | Value | Basis |
| --- | --- | --- |
| Pre-load sample | 10 rows, random | Source: open 10 rows before anything loads |
| HOLD | 2 or more wrong in 10 | Source: if 2 of 10 are off, the whole list has a problem |
| GO | 0 or 1 wrong in 10 | Derived from the HOLD rule; name the one bad row |
| Provider comparison | 50–100 contacts per provider | Adaptation; same criteria, sample only |
| Email provider metric | Valid-contact rate | Adaptation of the source's phone metric |
| Phone provider metric | Dials per in-profile person | Source: 50 dials fell to ~15 on the same criteria with a different provider |
| No ICP | INCONCLUSIVE | Fit cannot be judged; mailbox validity alone is not a gate |
| Fewer than 10 rows | INCONCLUSIVE | Sample every row and say the sample is short |

## Row rubric

- **Company** — exists, matches the ICP's industry and geography.
- **Title** — matches the buying role, not just any employee.
- **Size** — headcount or revenue band matches the ICP.
- **Mailbox** — a real, deliverable address; a pattern that only looks valid is a fail.

A row fails if any one check fails. Record the failing check, not just "bad".

## Gate report template

```
Decision: GO | HOLD | INCONCLUSIVE
List: <name>   Rows: <count>   Sampled: <count>   Date: <date>   Reviewer: <name>

| # | Company | Title | Size fit | Mailbox valid | Note |
|---|---------|-------|----------|---------------|------|

Fail pattern: <wrong filter | stale source | wrong seniority | invalid mailboxes | none>
Cause: <the query, provider, or enrichment step that produced it>
Required change: <specific fix>
Re-run condition: <fresh 10-row sample after the change>

Source benchmarks used: <rules taken from the article, labeled as such>
```

A HOLD is a verdict on the list, not on the offer, the market, or the sender.
