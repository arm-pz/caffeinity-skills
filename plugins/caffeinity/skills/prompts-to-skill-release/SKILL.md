---
name: prompts-to-skill-release
description: Release a skill built from prompts. Use after prompts-to-skill has drafted and tuned a skill, to package it as a zip, run its test cases and record real results, check install and discovery in a fresh session, write the repo README and version, and hand the user an install checklist. Use whenever the user has a finished skill folder in context and says "package this skill", "release it", "ship it", "make it installable", "run the tests on this skill", or "is it ready to install", even if they don't name a step. A bare "publish this to GitHub" with no skill to package is not this job. Not for drafting or tuning a skill (use prompts-to-skill or tune-skill), for repo discoverability copy (use findable), or for pushing existing clones (use upstream-check).
---

# prompts-to-skill-release

This skill takes a finished draft and makes it installable, tested and documented. It does not change the skill's behaviour. If a test fails, it goes back to tune-skill rather than editing the skill itself. Read `references/release-steps.md` for each step and `references/readme-template.md` for the README.

## Preconditions

Stop and report if any of these fail:

1. The skill folder exists, its name matches the `name` field and H1, and `check_skill.py` shows no FAIL.
2. `prompts-to-skill` has recorded its Gate A and Gate B results. A gate marked "written, not run" is a warning, not a pass.
3. The user has said what they want: a zip only, a GitHub repo, or both.

## Steps

**1. Test.** Run each case in `evals/evals.json` and each row in the tune-skill test-case table. Record pass, fail, or not-run for each. Never mark a case pass without running or reasoning through it against the real description. If you can only reason, say "reviewed, not executed".

**2. Fix or return.** For each failure, decide whether the fix is in the description (go back to tune-skill) or the body (go back to tune-skill as well). Do not edit the skill in this step. Re-run only the affected cases after tune-skill returns.

**3. Version.** Set `version: 0.1.0` in the frontmatter if there is none, and keep any existing version field unchanged. Add a `CHANGELOG.md` with one entry: what the skill does, the date, and the test results.

**4. Package.** Build the zip with the skill folder as the top-level entry, so unzipping gives `skill-name/SKILL.md`. Exclude `.DS_Store`, `__pycache__`, and any `evals/` results that contain personal data. Verify the archive with a listing.

**5. Discovery check.** Write three prompts that should trigger the skill and one that should not, using the user's own words. Judge each by reading the description. Record the result. Do not claim the skill is discoverable in a live session unless you tested it in one.

**6. README.** Write `README.md` from the template: what it does, install options, example prompts, the boundary with sibling skills, test results, and version. Keep the README out of the skill folder if the platform treats extra files as noise, and say which you chose.

**7. Install checklist.** Give the user the install steps for their platform: upload the zip in skills settings, or unzip into the skills directory, or use the `npx skills add` command if they publish to GitHub. Include a check to confirm the skill is visible.

**8. Publish (optional).** Only if the user asks. Create the repo, push the folder, and tag the version. Then hand off to `findable` for the name decision and listing, since that skill needs a live repo.

## Report

- Test results: counts for pass, fail, and reviewed-only.
- Files produced: zip, README, CHANGELOG, and their paths.
- Discovery result.
- Anything that needs the user's action, such as install or push.
- One next step.

## Boundaries

This skill packages and documents. It does not draft, tune, or name. Do not hide a failing test to make the release look clean. A failed test means the skill is not ready, and the report must say so.
