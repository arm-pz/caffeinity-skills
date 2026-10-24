# Trigger cases for course-builder

Written to tune-skill's case format (`references/test-cases.md` in arm-pz/tune-skill). Judged from
the `description` frontmatter only. Competing descriptions read: `study-system`, `topic-primer`,
`sales-copy`, `wordsmith`, `research-brief`.

**Run:** hand-run on 2026-10-24 against the descriptions only. No automated triggering loop was run.

| # | Message | Expected skill | Pass condition | Result |
| --- | --- | --- | --- | --- |
| 1 | "I'm teaching a 6-week Python cohort. Give me a syllabus." | course-builder | intake, outcomes, course.json, check_course.py | PASS ("cohort ... syllabus") |
| 2 | "Plan a 3-session workshop on prompt engineering for my team." | course-builder | time budget fits 3 sessions | PASS ("workshop structure", "internal training") |
| 3 | "Check my course outline; I think it's too much for 10 weeks." | course-builder | runs the checker, reports over-budget modules | PASS ("existing course checked for gaps and overload") |
| 4 | "Make me a study plan to learn SQL in a month." | study-system | course-builder does not load | PASS ("Not for one person's own learning plan") |
| 5 | "Explain recursion like I'm new to it." | topic-primer | course-builder does not load | PASS |
| 6 | "Write the sales page for my bootcamp." | sales-copy | course-builder does not load | PASS ("not for marketing the course") |
| 7 | "Turn my lecture notes into module outcomes." | course-builder | outcomes with measurable verbs | PASS ("module plan") |

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "Curriculum for my students." | course-builder | a group of learners |
| "Curriculum for me." | study-system | one learner |
| "Teach me the first module." | topic-primer | the teaching, not the design |
