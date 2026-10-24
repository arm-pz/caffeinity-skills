---
name: course-builder
description: >-
  Designs a course for a group of learners (a class, cohort, workshop series, bootcamp or
  internal training): measurable outcomes, a module sequence with prerequisites, activities and
  assessments aligned to each outcome, a time budget that fits the hours available, and a rubric,
  then checks the plan with a script so no outcome goes untaught or unassessed. Use when someone
  is teaching others and asks for a curriculum, syllabus, course outline, module plan, cohort or
  workshop structure, or wants an existing course checked for gaps and overload, even if they
  never say "curriculum". Not for one person's own learning plan (use study-system), for being
  taught the topic (use topic-primer), or for marketing the course (use sales-copy).
---

# course-builder

A course fails in two quiet ways: an outcome the syllabus promises that no session teaches or
tests, and twelve hours of content packed into eight hours of class. Both are visible on paper
before the first session. This skill writes the plan as data, so a script can find them.

It designs the course; it does not write every lesson. Lesson content goes to `topic-primer`
(concept explanations) and `wordsmith` (handouts and slides copy).

## Intake

Ask in one message, and mark what you assumed if the teacher does not answer:

1. **Who are the learners?** Level, what they can already do, how many, and why they are here.
2. **What must they be able to do at the end?** Tasks, not topics ("deploy a site", not "web hosting").
3. **How much time?** Number of sessions, length of each, and expected work between sessions.
4. **Format.** In person, live online or self-paced; group size; tools learners will have.
5. **Constraints.** Fixed exam or certification, required topics, accessibility needs.

If the teacher has run `topic-primer` or `study-system` on the subject, take their component map
as the starting decomposition instead of re-deriving it.

## Workflow

1. **Write the outcomes.** 3 to 8 course outcomes, each a learner-observable verb plus a
   condition ("Given a broken deploy log, identify the failing step"). Avoid unmeasurable verbs:
   understand, know, learn, appreciate, be aware of. `references/outcomes.md` has a verb list by
   level and examples.
2. **Sequence the modules.** Order by prerequisite, not by the textbook. Each module names the
   outcomes it teaches and the earlier modules it depends on. Start with the smallest end-to-end
   version of the final task, then deepen.
3. **Align every module.** For each module: one practice activity that rehearses the outcome and
   one assessment that would show it was met (`references/alignment.md`). An outcome with no
   assessment is a promise nobody checks.
4. **Budget the time.** Give each module hours for contact time and for work between sessions.
   The total must fit what the intake gave; cut or merge modules rather than squeezing.
5. **Write it as `course.json`** in the shape in `references/alignment.md`, then run:

       python scripts/check_course.py course.json

   It fails on an outcome nobody teaches or assesses, a prerequisite on a later or unknown
   module, and a plan over its hour budget; it warns on unmeasurable outcome verbs, modules with
   no outcome or no assessment, and modules over a quarter of the budget. Fix every FAIL.
6. **Render the syllabus** for learners from the checked JSON: outcomes, the module table
   (title, what you will be able to do, hours, assessment), how grading works and the rubric.

## Rules

- **Outcomes first, content second.** A topic that serves no outcome is cut or marked optional.
- **One assessment per outcome, at least.** Final projects may assess several; say which.
- **Rubrics describe evidence.** Each level says what the work shows, not "good" or "excellent".
- **No invented resources.** Do not cite a book, course, dataset or tool you are not confident
  exists; mark anything not checked this session `[unverified]`.
- **Respect the learners' time.** Between-session work is counted in the budget, not hidden.

## Handoffs

| Signal | Owner | What you send |
| --- | --- | --- |
| One learner's own plan, practice routine, revision schedule | `study-system` | the outcomes, restated as that learner's target skill |
| The concepts of one module need explaining | `topic-primer` | the module's outcome and the learners' starting level |
| Handout, slide or announcement copy | `wordsmith` | the syllabus and the voice wanted |
| Selling the course or cohort | `sales-copy` | the outcomes and who the course is for |
| Course pages or a policy for refunds | `paper-trail` | the price, refund window and what learners submit |

## Report

Lead with the outcomes and the checker result. Then the module table, total hours against the
budget, any WARN kept and why, assumptions made at intake, and the one next action.
`references/trigger-cases.md` holds the hand-run trigger cases; open it when tuning this
description.
