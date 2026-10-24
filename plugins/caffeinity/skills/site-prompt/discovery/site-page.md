---
title: "site-prompt: verified one-shot website prompts"
description: "An agent skill that turns a topic into one self-contained build prompt with final copy, complete source and a replay check."
slug: site-prompt
repo: https://github.com/arm-pz/site-prompt
install: "npx skills add arm-pz/site-prompt --skill site-prompt"
tags: [agent-skills, landing-page, prompt-engineering, web-design, qoder]
---

# site-prompt: verified one-shot website build prompts

An agent skill that turns a website topic into one markdown file a fresh agent can build from: a subject-native concept, final copy, every source file embedded verbatim, and the checks that were actually run. It builds and verifies the site in a scratch folder first, then replays the prompt into a clean directory and compares the trees byte for byte.

## What you can ask it

| Ask | What comes back |
|---|---|
| "One-shot build prompt for a cargo-ship landing page." | A concept container line with a rotation, manifest, vessel and booking cut-off — not a template with nautical nouns |
| "SELENE-style prompt for a ferry between Athens and the Cyclades." | A ferry-native page; the assumption about real operator vs concept is stated |
| "Mega-prompt for a marine insurance broker." | Concept marked as concept; no invented customers, ratings or certifications |
| "Every file, no placeholders, replay-tested." | One `## File:` section per file with the full contents, plus a replay result |

## Install

```
npx skills add arm-pz/site-prompt --skill site-prompt
```

Or clone the repo into `~/.qoder/skills/site-prompt` (Qoder) or `~/.claude/skills/site-prompt` (Claude Code).

## Example

Real output from the Northline cargo-ship run:

```
$ node scripts/replay-prompt.mjs prompts/cargo-ship.md --list
 477  index.html
1611  styles.css
 299  main.js
   5  favicon.svg

4 files, 66305 bytes
```

`--check` against the built directory reports `4 match, 0 differ, 0 missing`. The same verifier checked the original SELENE prompt at 21 files and 21 matches.

## Questions

**Is this just a prompt template?**
No. The prompt is assembled from a site that was built, served and measured. The checks section lists the viewports, sampled values and contrast ratios that ran, and names what did not.

**Does it build or host the site?**
No. The deliverable is the prompt. Building goes to the site tooling; hosting to deployment. This skill stops at the markdown file.

**What does "verified" mean here?**
Two things: the site was verified in a browser before the prompt was written, and the prompt's file sections were replayed into a clean directory and compared against the built site. Trigger cases are written but were not run against a live trigger model.

**Is it related to the other `site-prompt` repositories?**
No. Those are empty or unrelated. `SitePrompter` goes the other way, turning a site into a prompt.

## Related

- [tune-skill](https://github.com/arm-pz/tune-skill) audits a skill that already exists.
- [draft-skill](https://github.com/arm-pz/draft-skill) creates a new skill.
- [Source on GitHub](https://github.com/arm-pz/site-prompt)
