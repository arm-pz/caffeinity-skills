# Alignment and the course.json shape

Every outcome needs three things that point at it: a module that teaches it, an activity that
rehearses it, and an assessment that shows it was met. The JSON keeps those links explicit.

```json
{
  "title": "Ship a static site in four weeks",
  "learners": "career changers who can edit HTML; cohort of 20",
  "budget_hours": 24,
  "outcomes": [
    {"id": "O1", "text": "Deploy a static site to a host from a git push"},
    {"id": "O2", "text": "Diagnose a failing build from its log"}
  ],
  "modules": [
    {
      "id": "M1",
      "title": "First deploy",
      "outcomes": ["O1"],
      "prereqs": [],
      "hours": 6,
      "activity": "Deploy the starter site; break and fix the build once",
      "assessment": {"outcomes": ["O1"], "evidence": "live URL and the commit that deployed it"}
    },
    {
      "id": "M2",
      "title": "Reading build logs",
      "outcomes": ["O2"],
      "prereqs": ["M1"],
      "hours": 6,
      "activity": "Three broken builds, one fix each",
      "assessment": {"outcomes": ["O2"], "evidence": "a written diagnosis per log"}
    }
  ],
  "final": {"outcomes": ["O1", "O2"], "evidence": "deploy the capstone and explain one failure you fixed"}
}
```

- `hours` counts contact time plus work between sessions.
- `assessment` may be omitted on a module only when `final` assesses its outcomes; the checker
  warns so you say why.
- `prereqs` name earlier modules only. A prerequisite on a later module means the order is wrong.

## Activities that rehearse, assessments that show

| Outcome verb | Activity | Assessment evidence |
| --- | --- | --- |
| identify, list | sorting or labelling exercise | short quiz with feedback |
| explain, compare | pair explanation, worked example | a written or recorded explanation scored on a rubric |
| build, configure, run | guided build, then an unguided variation | the working artefact plus a note on choices made |
| diagnose, debug | broken examples with hints withdrawn over time | a diagnosis of an unseen broken example |
| justify, evaluate | a decision with a checklist, then a debrief | a decision memo scored on its reasons |
| design, write | studio critique on a draft | the final piece against a rubric |

## Rubric levels

Write three or four levels per criterion, each naming what the work shows: "the diagnosis names
the failing step and the evidence line" beats "excellent diagnosis".
