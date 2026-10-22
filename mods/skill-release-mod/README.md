# skill-release-mod

Holds gh release create and npm publish until prompts-to-skill-release has run its test cases since the last edit.

This plugin is a Claude Code **mod** (needs Claude Code 2.1.287 or later). It bundles the
`prompts-to-skill-release` skill, unchanged, in `skills/prompts-to-skill-release/`, and adds code that runs inside Claude Code
to trigger it at the right moment.

## What it does

- **Gate.** A Bash command that matches one of the ship patterns is held until the required skills (`prompts-to-skill-release`) have run since the last edit. Modes (set with `/plugin configure <plugin>@<marketplace>`): `ask`, `block`, `nudge`, `off`. After 2 holds it lets the command through, so a missing skill can never trap a session.
- **Prime.** When a prompt matches, one line of context tells Claude which skill applies.
- **/skill-release-mod** shows the state; `/skill-release-mod off` snoozes it for the session and `/skill-release-mod on` resumes.
- It reads the text of commands and prompts, so it is a reminder, not a security control. It fails open.

## Install

```
/plugin install skill-release-mod --marketplace arm-pz/caffeinity-skills
```

## Try it from a clone

```
claude --plugin-dir ./skill-release-mod
```

Run `/plugin` and look for "1 mod active". To share it, list it in a marketplace and install
with `/plugin install skill-release-mod@<marketplace>`.

## Trust surface

Mods are not sandboxed: they run with your permissions inside Claude Code. This block is the
report from `claude plugin validate`, refreshed by `verify_mod.py --update-readme`. Read the
`calls:` line before you install.

<!-- trust:start -->
```text
hooks: ./register.js session.start, skill.prompt, tool.call{tool=Edit|Write|MultiEdit|NotebookEdit}, tool.call{tool=Bash}, prompt.submit, command.run{command=skill-release-mod}
calls: ./register.js $.command.register, $.ui.ask, $.ui.status, $.ui.toast
```
<!-- trust:end -->

## Tests

```
claude plugin test ./skill-release-mod
```

## Licence

Choose one before publishing and add a LICENSE file or a `license` field in `plugin.json`.
