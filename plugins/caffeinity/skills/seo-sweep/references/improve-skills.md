# Improving a skill while you run it

A skill run on a real site is the best test it will get. When it reports something false, misses something real, or makes the work harder than it should be, that is a defect in the skill, and the sweep is the moment to fix it, while the evidence is in front of you.

## 1. Log it when you see it

Keep a defect log during the sweep. One row per defect:

| Skill | What happened | Evidence | Kind |
|---|---|---|---|
| seo-crawl | `--out reports/x.json` crawled 70 pages, then failed: folder missing | the error line | bug |
| seo-crawl | 4 findings with the same ID for one broken URL | finding IDs from the report | bug |
| findable | audit never searched the name plus the domain word | the user's screenshot of "acme tech" | gap |

Kinds:

- **bug**: the skill's own code or instructions produce a wrong result (false positive, duplicate, crash, wrong default).
- **gap**: the skill is silent about a case it should cover, and the sweep had to improvise.
- **friction**: correct but costly (a check that says *that* something is wrong but not *which*, a step that wastes a run).

Do not stop the sweep to fix a skill. Work around the defect, note the workaround in the log, and continue.

## 2. Check it is the skill, not the site

Before calling it a defect, confirm the skill is wrong and the site is not. A 404 the crawler reports may be a real broken link; it is a false positive only if the link works for people (Cloudflare's `/cdn-cgi/l/email-protection` links are decoded in the browser, for example). Read the skill's own docs: a documented limit is not a bug, though it may still be a gap or friction worth fixing.

## 3. Fix it with a test

For a skill with code and tests:

1. Get the skill's repo (clone it; if you cannot push to it, work in a scratch clone).
2. Write the smallest test that reproduces the defect. Run it against the unchanged code and **see it fail**. A test that passes before the fix proves nothing.
3. Make the smallest fix. Run the whole suite; everything passes.
4. Re-run the skill on the real site and show the defect is gone from real output.
5. Update the skill's SKILL.md and references wherever they describe the old behavior.

For an instruction-only skill (no code): edit the SKILL.md or reference that should have covered the case, and add a test prompt to its `tests/` (prompt, setup, what a good response does, what counts as failure), modeled on the ones already there. Keep the edit to what the defect needs; do not rewrite the skill.

## 4. Hand it over

- **With push access:** commit to a branch in the skill's repo with a message that names the site run that exposed the defect, and follow the user's instructions on pushing and pull requests.
- **Without it:** commit in the scratch clone and export `git format-patch -1`, then give the user the patch path and the one command to apply it (`git am <patch>`).

Then check the skill's other surfaces against what you changed: plugin.json `homepage` should point at the skill's page, and the site page, README and marketplace entry should describe the same behavior. When they drift, hand that to `upstream-check`.

## 5. Report

List each defect in the sweep report: the evidence, the fix, the test that now covers it, before-and-after output from the real site, and where the change lives (commit, branch or patch file).
