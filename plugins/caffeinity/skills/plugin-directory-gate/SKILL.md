---
name: plugin-directory-gate
description: Checks a Claude Code plugin folder against the Claude plugin directory's submission rules and returns GO or HOLD, with each blocking issue, policy hold and warning as rule, file:line and fix (scripts, install lines even in docs, download-and-run, credentials, manifest fields, frontmatter, file limits). Turns a pasted portal validation report into fixes, and says when to split out a Markdown-only directory edition instead. Use when someone asks whether a plugin will pass the Claude directory, is about to submit one there, or got back "blocking issues", "policy holds" or "your organization isn't Verified", even if they never say gate. Not for choosing where to list (use findable), packaging or versioning a release (use prompts-to-skill-release), or go/no-go on a site or app launch (use release-gate).
---

# Plugin directory gate

The directory's portal rejects a plugin for things `claude plugin validate` passes: scripts,
install lines in documentation, fields and frontmatter keys outside an unpublished list. Each
round trip through the portal costs a submission and a review slot, so screen locally first.

## Steps

1. **Find the folder.** The one holding `.claude-plugin/plugin.json`, not the repo root, unless
   they are the same. If the user pasted a portal report, note the commit it names: a report on
   an old commit says nothing about the current tree.
2. **Run Claude Code's own checks first:** `claude plugin validate --strict <folder>`. Fix
   anything it reports; it is the cheaper loop.
3. **Run the screen:** `python scripts/screen.py <folder>` (add `--json` to post-process). It
   needs PyYAML for the frontmatter parse; without it the shape checks still run. Exit 1 is HOLD.
4. **Read every finding before reporting it.** Open the line. A `RUNTIME_FETCH_EXEC?` or
   `INSTALL_COMMAND` hit inside prose that forbids the practice still counts, because the
   portal's scanner flagged exactly that; but say it is prose and offer a rewording.
5. **Explain and fix** using `references/rules.md`: it has the portal's wording for each rule and
   what passed or failed in practice. Change files only when the user asks.
6. **Decide fix versus split.** If most blocking findings are scripts or install steps the skills
   genuinely need, recommend a directory edition (last section of `references/rules.md`) rather
   than stripping the main plugin, which breaks it for everyone else.

## Reading a pasted portal report

Map each portal code to the rule in `references/rules.md` (UNKNOWN_KEY, UNKNOWN_KEY_CROSS_TOOL,
RUNTIME_FETCH_EXEC, ASSETS_PASSED_UNREAD and the three blocking paragraphs). The portal names up
to ten files per warning; if the paste has no file names, ask the user to expand the warnings.
When the portal and this skill disagree, the portal is right: say so and update `rules.md`.

## Report

Verdict first (GO or HOLD), then counts per bucket, then findings grouped by rule with
`path:line` and the fix. End with what ran (`plugin validate`, `screen.py`) and what did not: the
portal's safety scan and human review cannot be reproduced locally, so GO means "nothing known
blocks", never "will be accepted".
