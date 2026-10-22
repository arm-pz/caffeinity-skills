# prompts-to-skill-release

An agent skill that takes a drafted skill and makes it installable: runs its trigger test cases and
records what actually passed, sets a version and CHANGELOG, builds the zip, checks whether the
description would get it found, writes the README, and hands you a per-platform install checklist.

It does not change how the skill behaves. A failing test sends the skill back to `tune-skill` rather
than getting an edit here, and a failed test is reported as a failure — the release never looks cleaner
than its results.

Works with Qoder, Claude Code and other agents that load skills.

**Heads up before you install:** precondition 1 checks the skill against `tune-skill`'s validator, so
install [`tune-skill`](https://github.com/arm-pz/tune-skill) alongside this one — this repo does not
carry it. Without it you can still run steps 3–7, but step 1's gate check has nothing to read.

## Install

```
npx skills add arm-pz/prompts-to-skill-release --skill prompts-to-skill-release
```

Or copy the `prompts-to-skill-release/` folder into `~/.qoder/skills/` (Qoder) or `~/.claude/skills/`
(Claude Code), then start a new session.

## Ask it things like

- "Package this skill as a zip."
- "Run the test cases on this skill and tell me what fails."
- "Is this skill ready to install? Give me the checklist."
- "Write the README and CHANGELOG for this skill before I push it."

## Preconditions

Refuses to start unless the skill folder exists with a matching name and H1, `tune-skill`'s validator
reports no FAIL, and you have said whether you want a zip, a GitHub repo, or both.

## Sibling

`arm-pz/prompts-to-skill` builds the skill this one releases. Drafting and tuning belong there;
naming and GitHub listing belong to `findable`.

## Layout

```
prompts-to-skill-release/
├── SKILL.md
└── references/
    ├── release-steps.md      # detail for each of the eight steps
    └── readme-template.md    # the README skeleton step 6 fills in
```

## Status

Built from the author's own prompt list on 2026-10-19. `SKILL.md` passes `tune-skill`'s validator with
no FAIL. Its own trigger test cases have not been run in a live session.

## License

MIT. See `LICENSE`.
