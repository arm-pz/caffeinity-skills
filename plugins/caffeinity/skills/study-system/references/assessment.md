# Assessment

Read this before running `gap-audit` or `mastery`, and before judging a `feynman-test`. It covers the knowledge-gap audit, the evidence rules, and the mastery rubric.

The point is a verdict the learner can act on and a stranger could check. An assessment that only confirms what the learner already believed is not an assessment.

## 1. Evidence, ranked

Trust these in this order, strongest first:

1. Something produced unaided, recently, on a case the learner had not seen before.
2. Something produced unaided on a familiar case, with the artefact available to inspect.
3. A live recall or explain-back attempt, with the hesitations and errors noted.
4. Diagnostic answers given without the source open.
5. What the learner says about their own level, and how long they have been "at it".

Self-rating is the weakest and is never the basis for a level. Where a plan or verdict rests on it, label it as such: "the learner reports intermediate; no artefact inspected".

### What counts as proof

A claim of competence needs a checkable event attached: the file, the score, the date, what was hard, what had to be looked up, what support was open while doing it. "I can do joins" is not evidence. "Rebuilt the weekly report Tuesday, took 40 minutes, one wrong key that the row count caught" is.

## 2. Gap audit

Purpose: find the assumptions that are wrong or missing, before the plan builds on them.

### Protocol

1. **Collect.** Ask for the artefacts: recent work, a failing attempt, notes, the error message, the last time they did it and what happened. If none exist, say so and run the audit on probes only.
2. **Probe.** Give four to six short tasks spanning: plain recall, applying the idea to a new case, diagnosing a broken example, and choosing between two plausible approaches. Keep the wording terse. Ask, then stop; the learner answers before you give anything back.
3. **Classify each failure.** Name the gap type, the evidence for it, and the consequence the learner will feel.
4. **Assign an owner.** Some gaps close with a drill in this system; others need teaching and go to `topic-primer` with the handoff block.
5. **Report.** Register plus three lines of narrative: the biggest gap, what it is currently costing, the first thing to do.

Do not teach during the audit. If a probe answer is wrong and the learner asks why, say that the audit records it now and that the explanation belongs to the teaching skill, then continue collecting.

### Gap types

| Type | Tell | Typical consequence |
| --- | --- | --- |
| Missing component | cannot start the task at all | the roadmap has a stage nobody wrote |
| Wrong mental model | consistent, confident errors in a pattern | practice reinforces the error; more reps make it worse |
| Terminology mismatch | answers the right idea in the wrong words, or freezes on jargon | breaks on docs, exams, conversations with others |
| Familiarity mistaken for recall | recognises the answer, cannot produce it | reads well, fails when the source is closed |
| Hidden support | performs only with a tutorial, template, or autocomplete open | collapses on a blank page |
| Missing recovery skill | builds it, cannot fix it | stuck at the first error, blames the tool |
| Environment gap | cannot get to a working state cold | every session loses its first half hour |
| Stale assumption | the model was true of an older version, or of a narrower case | works in the demo, fails in production |

### Explaining it back as a probe

The feynman test is a probe, not a lesson. Give one target, the constraint (plain words, no jargon, no reading from the source), and ask for it as if to a curious newcomer. Then listen for seams: a place where the account skips the mechanism ("and then it just works"), a step stated in the source's own order and words, an analogy that stops matching past the first sentence, an inability to answer "what would break if X were different", a confident claim that contradicts something said earlier.

Record the seam and the exact words around it. Do not supply the missing mechanism in the same message.

## 3. Mastery rubric

Assign one level, with the evidence quoted. Levels describe what the learner can do under stated conditions, not how they feel.

| Level | Can do | The tell that it is not yet reached |
| --- | --- | --- |
| 0. Unaware | not a gap they know about yet | cannot state what the skill involves |
| 1. Oriented | talks about it, recognises the parts, follows a worked example | cannot repeat the example without it open |
| 2. Supported | completes a familiar task with notes, a template or guidance at hand | fails when the supports are removed |
| 3. Unaided, familiar | completes a familiar task cold, recovers from ordinary errors | novel cases and edge conditions break it |
| 4. Unaided, novel | adapts to an unfamiliar case, diagnoses failures, explains the tradeoffs | speed or judgement degrades under real constraints (deadline, live audience, no retries) |
| 5. Practised | work survives review by a competent peer, and they can teach the parts to someone else, spot the newcomer's error and name why | can do it but not say why, or cannot transfer across sub-domains |

Calibration notes:

- Level 2 is the most commonly over-claimed. Ask what was open on the screen while working.
- Time spent is not a level. Ten years of a supported routine is still level 2.
- Levels are per component, not per skill. A learner can be level 4 on one component and level 1 on another; the rubric output should show that, not average it into a single flattering number.
- Exam and certification performance is evidence for the components the exam samples, nothing more.

### "Not ready" is a valid verdict

Say it when the evidence does not support the level the learner wants, in the same plain register as the rest. "Not ready for level 3 on joins: the two attempts both used a support, and the row-count check was not run."

Do not soften a verdict with adjectives, and do not invent a percentile, ranking or comparison to other learners without data. If the learner wants a number for how far to the next level, give the range bounded by their hours and the assumption attached, or say it depends on evidence you do not have.

### Verdict format

Write the assessment as:

```
Level: <per component>
Evidence: <the artefacts and probes, dated, quoted>
Missing: <the specific capability that keeps the level down>
Not judged: <what could not be assessed and why>
First fix: <one drill or one component>
Re-test: <the task that would prove the level, and under what conditions>
Owner: <study-system, or topic-primer with the handoff block>
```

`Not judged` is mandatory. When the learner supplies nothing, the honest verdict is "cannot assess", with the two or three probes that would change that.

## 4. Honesty checks before sending

1. Does the verdict contain at least one thing the learner did not volunteer?
2. Is every level claim tied to a dated event or a quoted answer?
3. Would the file survive a stranger checking each claim against the artefacts?
4. Is any invented statistic, percentile or comparison to "most learners" present? Delete it.
5. Is the next action a behaviour the learner can attempt, not a feeling?
6. Where teaching is needed, is the handoff block present instead of a lecture?
