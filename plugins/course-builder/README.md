# course-builder

Designs a course for a group of learners (a class, cohort, workshop series or internal
training): measurable outcomes, modules in prerequisite order, an activity and an assessment for
every outcome, and a time budget that fits. The plan is written as `course.json` and checked by
`scripts/check_course.py`, which fails on an outcome nobody teaches or assesses, a prerequisite
out of order, or a plan over its hours.

Optional step 3 of workflow Brew 7 · Slow drip (learn a skill) in `caffeinity-routing`, for when the learner is a
class rather than one person.

```
/plugin marketplace add arm-pz/caffeinity-skills
/plugin install course-builder@caffeinity-skills
```

Self-check: `python -I tests/test_check_course.py`
