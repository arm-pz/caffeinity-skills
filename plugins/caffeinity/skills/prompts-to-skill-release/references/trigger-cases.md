# Trigger cases for prompts-to-skill-release

Written to the format in tune-skill's `references/test-cases.md`. The skill under test is
`prompts-to-skill-release`, judged from its `description` frontmatter only, as an agent deciding
what to load would. Competing descriptions read: `prompts-to-skill`, `tune-skill`, `draft-skill`,
`findable`, `upstream-check`, `skill-launch`, and Qoder's built-in `skill-creator`.

**Run:** hand-run on 2026-10-19 against the descriptions only. No automated triggering loop was
run. Every case below is a routing judgement, not an executed release.

## Cases

| # | Message | Expected skill | Pass condition | Result |
| --- | --- | --- | --- | --- |
| 1 | "Package this skill." | prompts-to-skill-release | checks the preconditions and stops with a report if any fail | PASS (verbatim trigger) |
| 2 | "Is it ready to install? Run the tests on it." | prompts-to-skill-release | marks a case pass only after running it, or says "reviewed, not executed" | PASS (verbatim trigger) |
| 3 | "Ship it: zip, version and a README." | prompts-to-skill-release | produces the install checklist | PASS ("ship it", "make it installable") |
| 4 | "Make a zip of the folder and check a fresh session picks it up." | prompts-to-skill-release | tests discovery in a new session, not just the file list | PASS ("run its test cases and record real results", "check install and discovery in a fresh session") |
| 5 | "Give this skill a version number and write its repo README." | prompts-to-skill-release | does not touch the skill's behaviour | PASS |
| 6 | "One of its test cases fails." | prompts-to-skill-release → tune-skill | the release skill goes back to tune-skill instead of editing the skill itself | PASS: but only because the body says so; the description alone would route a failing case to tune-skill directly, which is also acceptable |
| 7 | "Polish the README so the repo gets stars." | findable | release does not load | PASS ("Not for … finding repo discoverability") |
| 8 | "The description doesn't trigger on the right requests." | tune-skill | release does not load | PASS ("Not for drafting or tuning a skill") |
| 9 | "Push my clones to GitHub." (several repos, none being released) | upstream-check | release does not load | PASS: release never names a multi-repo push, and this message names no skill folder |
| 10 | "Publish it to GitHub." with no skill folder in context | unclear | the release skill should not load on a bare "publish" | FAIL: "publish to GitHub" is a listed trigger, yet it also matches `findable` (about text, topics, directories), `upstream-check` (push a batch) and `skill-launch` ("zero to published"). Four descriptions claim one phrase |

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "Make a skill from these prompts" | prompts-to-skill | input is prompts, output is a draft |
| "The draft is done, make it installable" | prompts-to-skill-release | input is a finished folder |
| "Fix its triggering" | tune-skill | behaviour |
| "Write its release notes" | prompts-to-skill-release | packaging surface, not behaviour |
| "Write its GitHub About text and topics" | findable | listing |
| "Check whether the site index and the repos still agree" | upstream-check | post-publish drift, not a release |
| "Is it ready to install?" | prompts-to-skill-release | its own trigger phrase |
| "Install it into my skills folder" | prompts-to-skill-release's checklist, run by the user | the skill documents the install; it does not perform one silently |

Spans the family: "these prompts → a skill → on GitHub" runs `prompts-to-skill` (Gates A and B)
then `prompts-to-skill-release`. The release skill's precondition 2 refuses to proceed when a gate
is only "written, not run", so the order is enforced by the preconditions, not by the descriptions.

## Fix applied 2026-10-19

The trigger now reads "the user has a finished skill folder in context and says ...", and a bare
"publish this to GitHub" with no skill to package is named as not this job. Pushing existing clones
went to `upstream-check` and listing copy to `findable`, both named in the "Not for" clause.

## Not verified

- No zip has been built or installed from a clean machine, so the install-and-discovery step is
  untested, not passed.
- None of the four family repos ships an `evals/evals.json`, so step 1 has only a test-case table
  to run against, and prompts-to-skill step 2, which is supposed to produce that file, has never
  been run end to end on a real skill.
- Whether an agent respects precondition 2 (a gate marked "written, not run" is a warning, not a
  pass) was not tested against a real run.
