# Directory rules for organizations that are not Verified

Open this when explaining a finding, when the user pastes a portal report, or when a rule here
disagrees with what the portal said (the portal wins; update this file). Sources: the portal's own
report text (2026-11-22), the plugin pre-submission checklist, and the plugin manifest reference.
Verified organizations (paid plan plus a proven domain) may ship scripts and extra fields; nothing
below applies to them the same way.

## Buckets

| Bucket | Portal says | Effect |
| --- | --- | --- |
| block | "N blocking issues to fix" | validation fails; nothing is submitted |
| hold | "N policy holds" | passes, then a person must clear it; can be refused |
| warn | "N warnings" | shown to reviewers and users; may still hold the version |
| info | "No action needed" | nothing to do |

`block?` in screen.py output means the portal's list is unpublished and this is the safe reading.

## Files (blocking: "accepts scripts ... only from Verified organizations")

- Only Markdown, text, JSON, YAML, PNG, JPEG, GIF, WebP, ICO. The icon may be SVG; no other SVG.
- Nothing starting with `#!`, whatever its extension.
- No package-manager config or package lists: `package.json` beside a lockfile, `requirements.txt`,
  `pnpm-workspace.yaml`, `package-lock.json`, `.npmrc`, `uv.toml`, `bunfig.toml`.
- No `.claude/skills` folder, no `.claude-plugin` folder except the plugin's own; inside it only
  `plugin.json`, images, or a `marketplace.json` with known fields.
- UTF-8 text, no NUL bytes; no path characters some systems drop; no `.DS_Store`, `Thumbs.db`.
- LICENSE, README, `.gitignore` and the icon may stay if they meet the above.
- Fix: move skills into `skills/`. If the repo needs other files, put the plugin in a subfolder
  and submit that folder.

## Limits

- 512 files or fewer, or the plugin is held ("Ship fewer files"). Generated eval suites are the
  usual cause: keep them outside the submitted folder.
- Text files under 256 KiB (held); any file over 5 MiB stops validation.
- README of at least 40 words outside code blocks; LICENSE file or `license` field. A plugin
  subfolder with no README passed when the repo root had one.

## plugin.json (blocking: "accepts fields outside the allowed lists only from Verified")

- Fields Claude Code reads are allowed. `metadata` was refused in practice: drop it.
- Listing-only fields, reported as UNKNOWN_KEY_CROSS_TOOL, need no action: `icon`,
  `documentationUrl`, `supportUrl`, `privacyPolicyUrl`, `termsOfServiceUrl`.
- `name`: lowercase, digits, hyphens, at most 64. Reserved: `claude`, `anthropic`, `official`,
  `plugin`, `mcp`, `test`, and any `claude-`, `anthropic-`, `cc-plugin-` prefix.
- A root `plugin.json` in agent-plugins.org format is ignored (warning only).

## Frontmatter (blocking for keys outside the allowed list)

- Plain `key: value` lines between two lines of exactly `---`.
- At most 32 `[` and `{` together and 1,000 commas, text included.
- `description` is one text value. `tags` only text; `author` text or name, email, url.
- Argument names only under top-level `arguments:` as a plain list, each at most 64 characters.
- `metadata` as indented lines.
- The allowed key list is not published. `name` and `description` alone passed for 33 skills.
  Refused in practice: `version`, `argument-hint`, `user-invocable`, `metadata` blocks, and agent
  keys `skills`, `model`, `memory`, `maxTurns`, `color` (some of these may be fine; the report
  did not say which). When unsure, strip to `name` and `description` and re-validate.

## Lines (held or warned, even in documentation)

- INSTALL_COMMAND: launchers (`npx`, `bunx`, `uvx`, `pnpm dlx`, `yarn dlx`, `pipx run`, `uv run`)
  and package installs. "Remove the command, even from documentation, and point the user to the
  tool's own install instructions instead."
- RUNTIME_FETCH_EXEC: a download piped into a shell or interpreter. The scanner also flagged
  prose: "Do not fetch a remote script and pipe it into an interpreter" and a workflow named
  "Descale brew". It did not flag a table cell reading "Brew 10 · Descale", so the screen's
  bare-`brew` check is wider than the portal; treat it as a prompt to reword, not a verdict.
- ENV_CREDENTIAL: reading `$GITHUB_TOKEN` and the like and sending it anywhere is held, README
  examples included. Hard-coded credentials block.
- Describe in the README everything the plugin runs, sends or fetches; the safety scan targets
  undisclosed behaviour.

## Directory edition

When most findings are scripts and install lines a skill genuinely needs, do not gut the main
plugin. Build a second, Markdown-only plugin from it: copy each skill only when every file passes,
strip frontmatter to `name` and `description`, list the rest with reasons, rebuild on a schedule.
Working example: `arm-pz/caffeinity-directory` (`scripts/build.py`, `EXCLUDED.md`), validated
"passed" on 2026-11-22 with 33 of 68 skills.
