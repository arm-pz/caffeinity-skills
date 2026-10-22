# release-gate-mod

Holds production deploys and PR merges until the release-gate chair (web-preflight, security red team, performance audit) has run since the last edit.

This plugin is a Claude Code **mod** (needs Claude Code 2.1.287 or later). It bundles the
`release-gate-chair` skill, unchanged, in `skills/release-gate-chair/`, and adds code that runs inside Claude Code
to trigger it at the right moment.

## What it does

- **Gate.** A Bash command that matches one of the ship patterns is held until the required skills (`release-gate-chair`) have run since the last edit. Modes (set with `/plugin configure <plugin>@<marketplace>`): `ask`, `block`, `nudge`, `off`. After 2 holds it lets the command through, so a missing skill can never trap a session.
- **Prime.** When a prompt matches, one line of context tells Claude which skill applies.
- **/release-gate-mod** shows the state; `/release-gate-mod off` snoozes it for the session and `/release-gate-mod on` resumes.
- Installing more than one of the deploy mods (`release-gate-mod`, `web-preflight-mod`, `pre-ship-security-red-team-mod`, `pre-ship-performance-audit-mod`) makes each hold the same deploy. Pick `release-gate-mod`, which runs all three checks through one gate.
- It reads the text of commands and prompts, so it is a reminder, not a security control. It fails open.

## Install

```
/plugin install release-gate-mod --marketplace arm-pz/caffeinity-skills
```

## Try it from a clone

```
claude --plugin-dir ./release-gate-mod
```

Run `/plugin` and look for "1 mod active". To share it, list it in a marketplace and install
with `/plugin install release-gate-mod@<marketplace>`.

## Trust surface

Mods are not sandboxed: they run with your permissions inside Claude Code. This block is the
report from `claude plugin validate`, refreshed by `verify_mod.py --update-readme`. Read the
`calls:` line before you install.

<!-- trust:start -->
```text
hooks: ./register.js session.start, skill.prompt, tool.call{tool=Edit|Write|MultiEdit|NotebookEdit}, tool.call{tool=Bash}, prompt.submit, command.run{command=release-gate-mod}
calls: ./register.js $.command.register, $.ui.ask, $.ui.status, $.ui.toast
```
<!-- trust:end -->

## Tests

```
claude plugin test ./release-gate-mod
```

## Licence

Choose one before publishing and add a LICENSE file or a `license` field in `plugin.json`.
