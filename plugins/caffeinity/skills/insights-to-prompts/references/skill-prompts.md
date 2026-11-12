# Skill-prompt mode

Open this when `--skills-dir` was passed and `skill_friction` is non-empty.

## Reading the evidence

`skill_friction` lists each skill used in the window, how often, and which sessions had prompt-type friction. A skill is worth fixing when friction shows up in two or more sessions, or in one session with a weak outcome.

For each candidate, open its SKILL.md and the friction sessions' `friction_detail` and `follow_ups`, then decide where the fault sits:

| What the follow-ups show | Fix in the skill |
| --- | --- |
| Claude did a step the user didn't want | Tighten the step or add a "don't" with its reason |
| Claude asked for something the skill could have read | Point the body at where it lives |
| The skill fired for the wrong request | Narrow the description; hand to tune-skill if it's a sibling overlap |
| The output shape was wrong | State the output format in the body |
| The user's invocation was vague | Not the skill's fault — rewrite the invocation as a session prompt instead |

## Showing the fix

Show a unified diff of SKILL.md per skill, with the evidence line above it. Don't apply until the user approves. Triggering and sibling-boundary changes go to tune-skill rather than being made here.
