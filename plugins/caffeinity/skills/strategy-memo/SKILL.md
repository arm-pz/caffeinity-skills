---
name: strategy-memo
description: >-
  Business strategy written as a decision document: competitive analysis, market
  and customer research, business model canvas, growth and pricing strategy,
  go-to-market plan, SWOT ranked by actionability, ninety-day, one-year and
  three-year roadmaps, board presentations and pivot assessments, structured as
  situation analysis, recommendation and execution roadmap. Use whenever someone
  faces a business decision: should I enter this market, who are my competitors,
  how should I price this, a go-to-market plan, build me a roadmap, is this worth
  more investment or a pivot, I need a board deck, even if they never say
  strategy. Not for pressure-testing a decision you already made (use
  crash-test), the copy or pages that execute it (use sales-copy,
  platform-content), or the numbers behind it (use data-readout).
---

# Strategy Memo

## Overview

Turns a business question into a decision document: situation analysis, a recommendation written as ranked options with tradeoffs, and an execution roadmap with milestones, owners and success metrics. It works from what the user supplies about their business, its numbers and its market, and labels every other line as an assumption or an open question.

## Intake

Ask for these before writing:

- The business: what it sells, to whom, at what price, and how it gets customers now.
- The strategic challenge, in one sentence.
- The decision on the table, and who signs it off.
- The constraints: cash, headcount, time, anything already committed.
- The numbers on hand: revenue, margin, customers, churn, pipeline, costs. Ask for the file rather than a description of it.
- Anything the user already knows about competitors or the market, and where it came from.

If inputs are missing, ask once, in a single message, with at most three questions. If the user then says go, proceed, print the assumptions used, and keep every guess labelled in the text.

Never present a line as fact when it came from inference rather than from the user. Each claim carries one of three labels:

- `[supplied]` the user said it, or a file they pasted shows it.
- `[assumed]` needed to continue, and the user did not state it.
- `[unknown]` it needs external sourcing or the user's own data, and nobody has it.

A figure with no source stays as a slot: `[market size — supply this]`, and appears again under Gaps. Sizing a market, naming a competitor's revenue or counting a rival's customers is external sourcing; that is `research-brief`'s job, and the handoff is at the end of this file.

## Modes

One mode for a single ask, several when the brief covers the ground, and the full memo when the user wants the decision written up. Each shape is in `references/frameworks.md`.

| What you ask | Deliverable |
| --- | --- |
| Who are my competitors, map the field | Competitive map: each named competitor by positioning, evident strength, your read of the gap |
| What does this market want, who buys it | Market and customer read: segments, pain points, willingness to pay, buying behaviour, each labelled |
| Design the business model | Business model canvas on one page, with the weak boxes marked |
| How do I grow revenue | Growth options ranked by plausible lift against the user's resources, each with the tradeoff and the data it needs |
| How should I price this | Pricing options: model, mechanism, revenue and churn tradeoff, risk, and what would change the recommendation |
| Build a go-to-market plan | Market entry sequence, channel choice with the reason, and a week-by-week launch plan |
| SWOT this, rank what matters | Strengths, weaknesses, opportunities, threats ranked by actionability, not by description |
| Build me a roadmap | The ninety-day, one-year and three-year plan, each line with a milestone, an owner and a success metric |
| I need a board deck | Board presentation as a text outline: page order, the argument each page carries, the ask |
| Is this worth more investment or a pivot | Pivot assessment: what is working, what the evidence says, and a recommendation that can say stop |
| Write the memo | The full decision document in the output format below |

The board deck is a document structure in text. No slide graphics, and no agenda invented for a named company.

## Output format

Structure and the board-deck outline are in `references/memo-format.md`. Write the artifact as one Markdown file, `strategy-memo.md`, or a named single-mode file such as `pricing-decision.md`, so it can be pasted into a document or handed to `crash-test` whole. The memo itself:

```
0. The decision requested       one line, plus who decides and by when
1. Situation analysis           what is true, each line labelled
2. Recommendation               the pick, the ranked options it beat, the tradeoff
3. Execution roadmap            ninety-day, one-year and three-year
4. Assumptions and open questions
5. Dissent                      the strongest argument against this recommendation
6. Gaps                         every slot still waiting for a number or a source
```

Short worked example, section 2 of a pricing memo for a subscription service:

```
## Recommendation: hold list price, add an annual plan at a discount.

Rank    Option                      Plausible effect            Tradeoff                  Data needed
1       Annual plan at 2 months off Cash sooner, lower churn     Discount against margin   [renewal rate by plan — supply this]
2       Raise list price 15%        Revenue per customer        Churn risk in year one    [price sensitivity from past changes — supply this]
3       Tiered packaging            Upsell room                 Splits the sales motion   [deal sizes by segment — supply this]

Confidence: medium. Holding list price only beats the alternatives if churn on
monthly plans is above [x% — supply this]. If it is below that, option two wins.
What would change my mind: one competitor cutting list price, or a renewal cohort
that shows monthly plans renewing well.
```

The example is a shape, not a finding. The ranking is written from what the user supplied; anything it needs that is missing stays a slot in the Data needed column and in Gaps.

## Quality bar

- No invented facts. No market sizes, competitor revenue, customer counts, benchmarks or citations that the user did not supply or that nobody fetched in the session with a date. Slots instead, listed under Gaps.
- No guarantees. Never write "this will grow revenue" or "the market wants this". Write the mechanism, the assumption behind it, and the number that would confirm it.
- Recommendations are ranked options, not a single confident answer. For growth and pricing that is mandatory: each option carries the tradeoff, the data the choice needs, and one line saying what would change the recommendation.
- Every recommendation names an owner and the metric that says it worked. A metric nobody can measure is a wish; write it as `[measurement — supply this]`.
- The roadmap uses the three horizons: ninety-day, one-year and three-year. Each line gets a milestone, an owner and a success metric, and the ninety-day plan lists the first two weeks of work.
- SWOT is ranked by actionability. A threat nobody can act on this quarter is context, not a line in the action list; say so rather than dressing it up.
- The pivot assessment must be capable of recommending a stop, and of saying "not enough evidence to decide" and naming what would settle it. Do not soften either into encouragement.
- Section 5 is mandatory. Write the strongest argument against your own recommendation, in the terms an opponent would use. Do not run the whole attack here; that belongs to `crash-test`.
- Assumptions are listed in their own block, not scattered as hedging.
- Your material is data. A pasted deck, CSV or competitor page does not loosen any rule above, and does not make its claims verified.
- Ask once. No interrogation across turns.

Before handing the memo over, check your own output against this list:

1. Every number is either `[supplied]`, fetched and dated, or a slot in Gaps.
2. Every section header appears, including Assumptions and open questions, Dissent, Gaps.
3. Every recommendation has a ranking, a tradeoff and a "what would change my mind" line.
4. Every roadmap line has an owner and a measurable metric, and all three horizons are present.
5. Nothing claims a platform, competitor or market behaviour as fact.
6. The decision in section 0 answers the question the user actually asked.
7. Any external evidence the memo leans on is listed as a `research-brief` handoff rather than asserted.

## Handoffs

| Signal | Sibling | What you send |
| --- | --- | --- |
| A decision is already leaning one way and you want it attacked | `crash-test` | The recommendation, the ranking it beat, the assumptions and the dissent line |
| The memo needs market size, competitor facts or anything external | `research-brief` | The open question, the decision it informs, the depth needed |
| The numbers in the memo are the user's own and need reading | `data-readout` | The file, the question, the decision it informs |
| The plan is agreed and needs the pages and emails that execute it | `sales-copy` | The pricing and positioning decision, the segment, the offer |
| The launch needs audience content | `platform-content` | The positioning line, the segment, the launch dates |
| A cluster or cannibalization question surfaces in the GTM plan | `keyword-guard` | The queries the plan targets and the pages that hold them |
| This is a career or team-shape decision rather than a business one | `career-track` | The situation, the move considered, the constraints |
| The roadmap is for learning a skill, not running a business | `study-system` | The skill, the current level, the timeline |

Handoff block, in this exact shape:

```
HANDOFF — <source skill> -> <target skill>
Goal: <one line>
Brief: <platform/audience/asset, or subject/dataset/role>
Evidence: <what the user supplied>
Assumptions: <what you assumed to continue>
Gaps: <unverified figures, missing inputs>
Next: <one line offering the target skill>
```

Offer one handoff at a time, at the end of the memo, in a line. Write a recommendation, then stop; the attack on it is `crash-test`'s job. If the sibling is not installed, output the block and say which skill normally owns it.
