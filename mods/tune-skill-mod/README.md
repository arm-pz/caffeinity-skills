# tune-skill-mod

After Claude edits a SKILL.md, holds git push and releases until tune-skill has validated the change.

This plugin is a Claude Code **mod** (needs Claude Code 2.1.287 or later). It bundles the
`tune-skill` skill, unchanged, in `skills/tune-skill/`, and adds code that runs inside Claude Code
to trigger it at the right moment.

## What it does

- **Arms on SKILL.md edits only.** When Claude edits or writes a `SKILL.md`, it adds one line telling Claude to validate it with tune-skill. Edits to any other file are ignored, so ordinary code pushes are never held.
- **Gate.** While an edited SKILL.md has not been through `tune-skill`, a `git push`, `gh pr create`, `gh release create` or `npm publish` is handled by the mode (default `nudge`: it runs, then Claude is reminded). Modes (set with `/plugin configure <plugin>@<marketplace>`): `ask`, `block`, `nudge`, `off`. After 2 holds it lets the command through, so a missing skill can never trap a session.
- **Prime.** When a prompt matches, one line of context tells Claude which skill applies.
- **/tune-skill-mod** shows the state; `/tune-skill-mod off` snoozes it for the session and `/tune-skill-mod on` resumes.
- It reads the text of commands and prompts, so it is a reminder, not a security control. It fails open.

## Install

```
/plugin install tune-skill-mod --marketplace arm-pz/caffeinity-skills
```

## Try it from a clone

```
claude --plugin-dir ./tune-skill-mod
```

Run `/plugin` and look for "1 mod active". To share it, list it in a marketplace and install
with `/plugin install tune-skill-mod@<marketplace>`.

## Trust surface

Mods are not sandboxed: they run with your permissions inside Claude Code. This block is the
report from `claude plugin validate`, refreshed by `verify_mod.py --update-readme`. Read the
`calls:` line before you install.

<!-- trust:start -->
```text
hooks: ./register.js session.start, skill.prompt, tool.call{tool=Edit|Write|MultiEdit}, tool.call{tool=Bash}, prompt.submit, command.run{command=tune-skill-mod}
calls: ./register.js $.command.register, $.ui.ask, $.ui.status, $.ui.toast
```
<!-- trust:end -->

## Tests

```
claude plugin test ./tune-skill-mod
```

## Licence

Choose one before publishing and add a LICENSE file or a `license` field in `plugin.json`.
