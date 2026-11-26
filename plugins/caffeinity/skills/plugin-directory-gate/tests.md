# Trigger cases: plugin-directory-gate

Format from tune-skill's `references/test-cases.md`. "Run by hand" means judged against the
descriptions of plugin-directory-gate, findable, prompts-to-skill-release and release-gate only.
No automated triggering loop (`claude plugin eval`) has run.

| # | Message | Expected skill | Expected mode | Pass condition | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | "Will plugins/caffeinity pass the Claude plugin directory?" | plugin-directory-gate | screen | runs `claude plugin validate --strict`, then screen.py; verdict first | run by hand: pass |
| 2 | "I'm about to submit this plugin to Anthropic's directory, check it first" | plugin-directory-gate | screen | names the folder holding .claude-plugin/plugin.json | run by hand: pass |
| 3 | (pastes a portal report) "3 blocking issues, 7 policy holds. What do I fix?" | plugin-directory-gate | report | maps each paragraph to a rule; asks to expand warnings with no file names | run by hand: pass |
| 4 | "The portal says my organization isn't Verified and won't take my scripts" | plugin-directory-gate | report + split | weighs fix versus directory edition | run by hand: pass |
| 5 | "Why is the directory holding my plugin for review?" | plugin-directory-gate | report | asks for the report or runs the screen; does not guess | run by hand: pass |
| 6 | "Which directories should I list my new skill in?" | findable | — | plugin-directory-gate does not load | run by hand: pass |
| 7 | "Package this skill as a zip and bump the version" | prompts-to-skill-release | — | plugin-directory-gate does not load | run by hand: pass |
| 8 | "Give me a go/no-go on launching the marketing site" | release-gate | — | plugin-directory-gate does not load | run by hand: pass |
| 9 | "Validate my SKILL.md frontmatter and description" | tune-skill | — | shares "frontmatter" and "validate"; plugin-directory-gate does not load | run by hand: pass |

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "Is my plugin ready for the Claude directory?" | plugin-directory-gate | the directory's rules |
| "Is my plugin ready to install?" | prompts-to-skill-release | install and packaging, no directory named |
| "Get my plugin found: where should I submit it?" | findable | where to list |
| "Will my plugin get through the directory's checks?" | plugin-directory-gate | whether it passes |

Spanning case: "Check my plugin for the directory and then list it everywhere else too" starts with
plugin-directory-gate (verdict), then hands the listing question to findable.
