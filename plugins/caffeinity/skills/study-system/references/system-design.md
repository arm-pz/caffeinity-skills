# System design

Read this before writing a `breakdown`, `roadmap`, `practice` or `schedule`. It covers decomposition, ordering, practice design and review timing. Assessment lives in `references/assessment.md`.

Nothing here is a researched constant. The numbers are defaults to adjust from what the learner actually does, and each one says so.

## 1. Skill decomposition

Goal: find the small set of components that make the rest reachable, and name what can be safely deferred.

### Start from an outcome, not a topic

Write the target as a sentence the learner can prove: "I can ship a small internal tool that reads a CSV, computes three metrics and renders a page." A topic ("data engineering") has no end, so it cannot be decomposed usefully. If the user gives a topic, ask what they want to be able to do, and say which outcome you assumed if they do not answer.

### Generate candidate components

List components as verbs, in the language of the field. Cover these five kinds, because a plan that only has one of them produces someone who recognises things but cannot do them:

| Kind | What it is | Proof of competence looks like |
| --- | --- | --- |
| Procedural | the repeated physical or mechanical act | doing it unaided, on a fresh case, at acceptable speed |
| Declarative | the facts, vocabulary, relationships | saying it back plainly and using the term correctly in a new sentence |
| Judgement | knowing which option, when, and why | choosing between two plausible approaches and defending the choice |
| Environment | the tools, setup, formats, plumbing | getting to a working state from a cold machine with no help |
| Recovery | diagnosing when it goes wrong | reading the failure, forming a hypothesis, testing it |

Recovery and environment are the two most often missing, and the two most often the reason a learner "knows it but cannot do it".

### Rank by leverage

For each component ask: how many other components get stuck behind this one, and how soon will the learner need it given their goal. Keep the components that unblock the most, and move the rest to a deferred list rather than deleting them. Do not report a percentage of the skill covered; that number cannot be computed for most skills.

### Minimum viable set

The minimum viable components are the ones where, without them, every other path to the outcome is blocked. Sanity check: can the learner attempt something recognisable as the whole outcome using only this set? If not, a real component is still missing, or the outcome is too ambitious for the stated time. Say which.

### The deferral list

Every deferred component gets one line: what it is, what breaks without it, and the trigger for picking it up ("when you hit your first permissions problem"). This stops the learner reading the plan as a slighting of the omitted material.

## 2. Roadmap ordering

Order by these rules, in this priority:

1. **Dependency.** If component B needs component A to be attempted at all, A comes first. State the dependency in the stage row.
2. **Feedback availability.** Among components with no dependency between them, put the one where the learner can get a checkable signal soonest. A stage nobody can self-check drifts into reading.
3. **Relevance to the stated goal.** Drop or delay whatever is load-bearing generally but useless for this learner's outcome.
4. **Transfer.** Anything the learner already does in an adjacent domain moves early and is labelled as reuse, not new learning.

Tie-breakers, in order: cheaper to fail first; more motivating to see working; shorter to complete.

### Shape the stages as slices, not layers

A slice touches several components at a low depth and produces something whole ("build one report end to end"). A layer exhausts one component before anything runs ("learn every join type"). Default to slices, then deepen the ones that matter. Use layers only where a wrong foundation actively poisons the slice, typically in procedural and environment components.

### Gates

Each stage ends in a gate written as observable behaviour, never as hours or calendar position:

> Gate: rebuild a report you already trust from base tables, no lookups, and notice when the row count changes.

Include, per stage: what to learn, what the learner will be able to do, the practice that produces it, the gate, and the assumption the stage rests on ("assumes you can already read a table schema"). Where the gate needs an answer or a reference solution and none exists, name how to construct one, or mark it as needing a second pair of eyes and say who might provide it.

### Readiness gates that fail

A gate can be failed. Write the fallback: which component to drill, and what evidence to collect before retrying. Do not write "revise the stage", which is not actionable.

### Time on the roadmap

Roadmaps are ordered, not dated. Add dates only when the learner gives a deadline, then work backwards from it and label the resulting pace as arithmetic on their own numbers. Where the user asks how long a skill takes, answer with a range bounded by the assumptions (hours per week, quality of feedback, prior transfer, whether practice is at the edge of competence) and say the spread is wide. If you cannot bound it, write `unknown` and name what would make it knowable.

## 3. Deliberate-practice routine design

A routine is a repeated session with a target just past current ability and a way to find out what went wrong. Without the feedback part it is repetition, and the plan should not call it practice.

### The elements, every time

| Element | Rule |
| --- | --- |
| Target | one component, named before the session starts |
| Task | attemptable cold, completable inside the session, no tutorial to follow step by step |
| Difficulty band | reachable with effort; the learner fails on part of it |
| Feedback | a check the learner can run alone: tests, row counts, totals, an answer key, a diff against a reference, a recording replayed |
| Reps | enough to repeat the hard part once after the error is understood |
| Log | what was attempted, where it broke, the stated cause, next target |

### Session shape

Default to 45 to 90 minutes for cognitively heavy work; shorter blocks for memory or drill; longer blocks only where the skill itself is endurance, such as an exam paper or a live set. The bound is an attention assumption, not a finding: tell the learner to shorten it if the log stops being honest near the end.

Within a session: a few minutes of recall on last session's target, then the main block, then the error log, then write next session's target. The log is the part that makes the next session aimed.

### Moving the band

- Two sessions passing clean: raise difficulty, or remove one support (no notes, no autocomplete, timed, different data).
- Two failures in a row on the same error type: drop to the component underneath and drill that.
- Consistent success with no new errors: check that the task is still novel. Same task repeated is comfort, not competence.

### Blocked then interleaved

Early on, practise one component at a time so the mechanics get built. Once a component is reliable in isolation, switch to mixed sets, where the learner must first decide which approach applies. Deciding which tool is the harder skill and it is the one that transfers to real conditions.

### Whole-part-whole

For skills with a performance shape (a presentation, an exam answer, a deployment, a conversation), start the session by attempting the whole thing, drill the weakest part, end by redoing the whole. This keeps the drill tied to the outcome the learner actually cares about.

### Designing feedback when there is no teacher

Rank these by how cheap they are to set up: automated checks and tests; numeric invariants that break on a mistake (row counts, totals, balances); a reference solution diffed against the attempt; an answer key or past paper; recording the attempt and replaying it against a checklist; comparing against the learner's own earlier work. A checklist written from the component map beats a vague "review your work". Anything requiring another human is marked as a dependency the learner must arrange.

### What to refuse

Do not measure progress in time in seat, streaks or pages covered. A streak can be kept while competence is flat, so if the user asks for one, log sessions completed and gates passed as separate columns.

## 4. Spaced-repetition scheduling

Purpose: schedule reviews so recall is tested near the edge of forgetting, rather than re-read until familiar. The ladder below is a starting schedule, chosen because it is manageable in a normal week. It is not a researched constant, and the recall data outranks it as soon as there is any.

### Starting ladder

First review the same day or next day, then roughly: 1 day, 3 days, 1 week, 2 weeks, 4 weeks, 8 weeks, then every 1 to 3 months. Approximate spacing is fine; missing a review is cheaper than an over-tuned schedule.

### The adjustment rule

Score each recall attempt as one of three, and let the score move the next interval:

| Recall | Move |
| --- | --- |
| Correct, no hesitation | multiply the interval, starting at about 2 to 3 times |
| Correct after struggle, or partly right | hold the interval, review again soon |
| Failed, or confidently wrong | reset to the short end, and re-learn rather than re-review before the next attempt |

Record which item moved and why, so the schedule is auditable and the learner can see the cause. Report the failure rate per item type; a whole component failing repeatedly is a roadmap problem, not a memory problem, and belongs in the gap register.

### What to make a review item for

One fact or one decision per item, phrased as a question with a single checkable answer. Review items are for the declarative and judgement components. Procedural skill is maintained by doing, on the same interval logic but with a task rather than a card. An item that cannot be answered without the source open is a comprehension gap, not a memory gap: route it to the gap audit.

### Load control

Compute the reviews the schedule demands per day. If the daily load exceeds the hours the learner gave, lengthen intervals or cut items, do not let the queue build. Review debt is the usual reason these schedules are abandoned, so name the cap when writing the plan.

### Exam revision

Work backwards from the date. Split the remaining days across subjects weighted by weakness and by mark-per-topic value, not by when the material was last seen. Put the weakest high-value topics early enough that a failed gate still leaves time for a second pass, and reserve the last stretch for recall practice on already-passed material rather than new content. State the weights the learner gave you; do not invent mark distributions for an exam you have not read.
