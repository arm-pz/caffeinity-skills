# Working with the recruiter-lens skill

The recruiter-lens skill (github.com/arm-pz/recruiter-lens) is this skill's sibling. It judges a candidate's material from a recruiter's perspective; applicant-kit produces the material. They share a subject and must not share triggers: if both claim "why am I not getting interviews", the wrong one will fire half the time.

The command names and behaviors below are verified against the recruiter-lens skill's SKILL.md and `references/commands.md` (arm-pz/recruiter-lens, October 2026). Where the installed skill behaves differently, trust the installed skill.

Both skills hold the same core principle: optimize the presentation of real experience, never fabricate it, and numbers only ever come from the candidate. Keep that consistent when handing work back and forth.

## Who answers what

| Question | recruiter-lens command | Where it lands in applicant-kit |
|---|---|---|
| What is the 6-second impression? | `scan` | Mode 7 hand-off |
| What is wrong with this resume? | `critique` | Mode 7 hand-off; findings become to-dos for modes 1 to 6 |
| Will an ATS parse it? | `ats-check` | Feeds the formatting rules in mode 1 and the final check in the full pass |
| Why might it be rejected? | `reject-reasons` | Mode 7 hand-off |
| How well does it cover this role, and what is missing? | `gap-analysis`, `tailor` | Coverage view for modes 1 and 3; applicant-kit writes the tailored resume and the placement map |
| What will they ask me? | `predict-questions` | Question list for mode 6 |
| What is wrong with my LinkedIn? | `linkedin-audit` | Brief for the mode 5 rewrite |
| What may I use AI for in a job search? | `ai-guidelines` | Overrides applicant-kit's defaults on authenticity |
| Write the better version | applicant-kit | Modes 1 to 6 |

**`tailor` is settled: it reports coverage.** In recruiter-lens it maps each JD requirement to Full/Partial/Missing against the candidate's real experience and recommends repositioning; applicant-kit writes the tailored resume and the placement map (modes 1 and 3). Both descriptions state the same split, so nothing overlaps at the trigger level.

## How to hand off

- Say in one line that you are handing off, and to which command.
- Invoke the skill by name if the environment lets you, otherwise tell the user the command to run, for example `/recruiter-lens critique`.
- Take its findings as given. Do not re-judge them in applicant-kit; turn them into edits.
- When producing finished material, offer a final `ats-check` or `critique` pass before the user sends anything.

## Standalone fallback

Users may install applicant-kit alone, for example from a marketplace. If recruiter-lens is not available, say so once and keep going: mode 1 does its own coverage read, mode 3 builds its own gap lists, mode 6 generates its own questions, mode 5 writes without an audit, and mode 7 runs its short fallback. Do not imitate recruiter-lens's full output. Offer the install line instead:

```
npx skills add arm-pz/recruiter-lens --skill recruiter-lens
```

## Reciprocal boundary line for recruiter-lens

For the recruiter-lens skill's description and "Not for" wording, so both skills stay out of each other's way:

> Not for producing finished application material (a rewritten resume, new summaries, a full LinkedIn rewrite, interview answer scripts): use the applicant-kit skill, which takes this skill's findings as input.
