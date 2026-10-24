# Frameworks

The shape each analysis takes, and what it must not fake. Every table below is filled from what the user supplied. A cell nobody has is a slot, written as `[metric — supply this]`, and it also appears in the memo's Gaps section. Rows read as fact only when they came from the user or from a source fetched in the session with a date.

## Competitive map

Write a row only for competitors the user named or that a dated source covers. Do not populate the field from memory of an industry.

| Competitor | What they claim to be for the buyer | Evident strength | Evident weakness | Gap this creates | Confidence |
| --- | --- | --- | --- | --- | --- |

Rules:

- Positioning is the story they tell their buyers, in their words or the user's paraphrase, not your inference about their strategy.
- A strength needs a reason you can point at: something the user observed, a page the user pasted, a dated source. Otherwise write "reported by user" or leave it a slot.
- The Gap column is the only place opinion belongs, and it gets labelled `[assumed]` unless the evidence for it is in the row.
- Close with three lines: the gap worth exploiting, what exploiting it costs, and the one competitor whose response would close it.
- If the user named no competitors and no sourcing is available, say the map is empty and hand the filling to `research-brief`. An empty honest map beats a plausible invented one.

## Market and customer read

| Segment | Who they are, as the user describes them | Pain, in their words | Willingness to pay | Buying behaviour | Evidence status |
| --- | --- | --- | --- | --- | --- |

Rules:

- Segments come from the user's own customers, deals lost, or a dated source. Never from a typology invented to fill the table.
- Willingness to pay is a range with the assumption attached, or a slot. Never a single confident number.
- Buying behaviour means: who else signs, what triggers the purchase, what stops it, how long it takes. Each of those gets a label.
- End with the segment you would serve first and why, plus the question that would confirm it.

## Business model canvas

One page, nine boxes: customer segments, value proposition, channels, customer relationships, revenue streams, key resources, key activities, key partners, cost structure.

Rules:

- Fill value proposition, revenue streams and cost structure first; they decide the rest.
- Mark each box `clear`, `thin` or `unknown`. A thin box is a finding, and the memo says which decision it blocks.
- Under revenue streams, write how money actually arrives and how often. Under cost structure, write the cost that grows fastest with volume; that number constrains every growth option later in the memo.
- Do not draw a diagram. A text canvas with labelled boxes is the deliverable.

## Growth options, ranked

Do not promise a fixed count of moves and do not pad the list to look complete. Rank the options you can defend.

| Rank | Option | Mechanism, why it would work | Plausible lift | What it costs | Data the ranking needs | Assumption it rests on |
| --- | --- | --- | --- | --- | --- | --- |

Rules:

- Rank against the user's resources and market position as they stated them. A move that needs headcount they do not have is not rank one.
- Plausible lift is a mechanism plus a range with the assumption attached, or a slot. No growth promises.
- Each option gets a kill line: the single number that would take it out of contention.
- State what would change the ranking as a whole. Usually one or two numbers, named.

## Pricing logic

| Option | Model | Who pays more, who pays less | Revenue tradeoff | Churn and sales friction | Risk | Data needed | What would change my mind |
| --- | --- | --- | --- | --- | --- | --- | --- |

Rules:

- Rank the models you can defend from what the user said about their buyer and competitors. Per unit, per seat, tiered, usage-based, flat, annual-with-discount, freemium are candidates, not conclusions.
- Price changes are reversible or they are not. Say which, and what a rollback costs; a price rise that cannot be unwound is a different kind of decision.
- Never assert a competitor's price. The user supplied it or a dated source did.
- The revenue tradeoff always pairs with the churn or sales friction it buys. A raise that costs deals is written as such.
- One line at the end: the experiment that would settle this within the ninety-day plan, and what it measures.

## Go-to-market sequence

Three layers, then the week-by-week.

1. Market entry: which segment or geography first, what you deliberately skip, the reason.
2. Channel choice: the route to the buyer, why that route over the alternatives, what it costs per acquisition if the user knows, otherwise `[cost per acquisition — supply this]`.
3. Launch execution: a week-by-week table inside the ninety-day plan.

| Week | Work | Owner | Output | Decision or gate at the end of it |
| --- | --- | --- | --- | --- |

Rules:

- Sequence is real calendar weeks with the user's start date. If there is no start date, write "week one is the week you decide" and leave the gate columns.
- Every phase ends in a gate: a go, a hold or a stop, plus what the gate looks at.
- Name the first thing that breaks if the launch slips, so the cost of delay is visible.
- Anything about how a platform distributes content is phrased as "commonly reported, test this", never as a fact about ranking internals.

## SWOT, ranked by actionability

Plain SWOT lists four quadrants and stops. This one ranks each line by whether it changes what you do this quarter.

| Item | Quadrant | Impact | Actionable now | Owner | Action, or why it is context |
| --- | --- | --- | --- | --- | --- |

The ranking rule: an item scores high only if someone can act on it inside ninety days and the consequence of acting is visible in a number. Impact without an owner or a horizon is context and moves to a short "noted, not actionable" list. Threats nobody can respond to this quarter are stated once and dropped, not padded into actions.

Rules:

- Do not manufacture four equal quadrants. If there are two strengths and one weakness, say so; a thin column is information.
- Every item traces to evidence in the situation analysis or a label.
- Cross-check: a strength that costs money to keep is written as a cost, and a weakness that is also a threat is counted once.

## Roadmap horizons

The horizons are the ninety-day, one-year and three-year plans.

| Horizon | Milestone | Owner | Success metric | Evidence it is on track | What stops it |
| --- | --- | --- | --- | --- | --- |

Rules:

- The ninety-day plan is the only one written in weeks, and it lists the first two weeks of work explicitly.
- One-year and three-year are milestones and the bets that must come true, not dates on features. Mark each as a plan or a hope.
- Every metric is measurable by someone named, with the measurement source. "Customer satisfaction improves" is a wish; write the survey, the cadence and the number.
- Each horizon carries the assumption it rests on and the checkpoint that revisits it.

## Board presentation

Text outline only, in `references/memo-format.md`. No slide graphics, no invented agenda for a named company, no claim about what a board expects unless the user said it.

## Pivot assessment

Honest, and it must be able to say stop.

| Question | Evidence | Reading | Confidence |
| --- | --- | --- | --- |

Run through: is the problem real to the buyer, is the current solution gaining, does the user have the resources for the next phase, is the market moving toward or away from this, what would a fresh start cost against what a pivot costs.

Then one of four verdicts, never a hedge in place of a verdict:

- **Invest more** — what it buys, what it costs, the number that proves it within ninety days.
- **Pivot** — from what, to what, what carries over, what gets written off.
- **Hold and gather evidence** — the single question, who answers it, by when.
- **Stop** — the evidence that says so, and what ending looks like.

Rules:

- Sunk cost is stated as sunk, not as a reason.
- The dissent line here is the argument the founder would make against stopping. Write it, then answer it with evidence or admit it lands.
- "Not enough evidence" is a legitimate verdict and gets named as such, with the cheapest thing that would settle it.
