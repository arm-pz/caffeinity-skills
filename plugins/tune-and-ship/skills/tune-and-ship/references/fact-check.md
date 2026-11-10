# Fact check

Read this at step 4. A skill's instructions are only as good as the facts they repeat to the user,
and product details move faster than a skill is re-read.

## What counts as a checkable claim

Go through `SKILL.md` and every reference and list each of these, with file and line:

- Version numbers and "since version X" thresholds.
- Command names, flags, slash commands, settings keys, environment variables, file paths.
- Prices, limits, multipliers, percentages and any "N× faster" or "N% of cases".
- Model, product and plan names, and which one is the default.
- Counts of the skill's own parts ("seven steps", "9 cases") and dates.
- Statements about what a third-party tool does or does not do.

Judgement and advice are not claims. "Ask before recommending" needs no source.

## Where to check, in order

1. **The tool itself.** `--version`, `--help`, the binary or package on disk. A name that appears
   in the installed binary exists; one that does not is suspect.
2. **The changelog.** It dates a behaviour to a version. Download the file and search it; a page
   summary truncates long changelogs and misses old entries.
3. **Official documentation.** Fetch the page and quote the sentence.
4. **The skill's own files**, for counts and cross-references.

A blog post, a forum answer, another skill or your own memory is not a source. If only those
support a claim, it is unverified.

## What to do with each result

| Result | Action |
| --- | --- |
| Confirmed | Keep. Tighten the wording if the source is more exact, such as "can disable" where the docs say "disables". |
| Wrong | Correct it to what the source says, and cite the source. |
| Unverifiable number | Remove it, or replace it with a related figure the source does publish and say what is not published. |
| Unverifiable soft claim | Soften to what the skill can stand behind, or remove. |
| Stale but once true | Correct, and note the version where it changed. |

The first run found "burns quota 3–5× faster" with no source. The published API prices gave 2×, and
the subscription weighting is not published. The fix was the 2× price ratio plus a line telling the
agent not to quote a multiplier, not a different guess.

A source often says more than the claim. When it shows a condition the skill does not handle, such
as a provider where the feature does not exist, add the smallest check that covers it and list it
as a finding. Do not redesign the workflow.

## Record

Put the result in the PR body as a table: claim, result, source. In the skill, add or update a
short "Sources" section in the most relevant reference file: what was checked, against which
version, on which date. State what was not checked.
