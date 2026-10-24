# Phases

Each phase: the skill that owns it, what it receives, what it hands on, and the gate that must pass
before the next phase starts. "Owner action" marks steps only the owner can do (a login, a form, a
dashboard).

| # | Phase | Owner skill | Receives | Hands on | Gate |
| --- | --- | --- | --- | --- | --- |
| 1 | Inventory | `upstream-check` | the owner or org name; clones of its repos | a table: repo, kind (skill, mod, bundle, none), where it is listed, drift | every repo classified; counts from SKILL.md files, not descriptions |
| 2 | Reconcile listings | `publish-pipeline` | the inventory | one manifest; generated hub, pages, indexes, sitemap, README block; aliases and 301s for renames | regenerated outputs match the manifest; a missing repo stops the sync instead of deleting |
| 3 | Test and tune | `tune-skill` (+ `web-preflight`, `seo-crawl` on the site) | every SKILL.md; the live site | validator results, a family regression baseline, fix PRs | 0 FAIL; no dangling handoff; site checks run and findings fixed or listed |
| 4 | Close workflow gaps | `caffeinity-routing`, `draft-skill` | the skills and their handoffs | numbered workflows with each step's input and output; new skills for missing steps | every handoff names a published skill; new skills pass the validator |
| 5 | Publish and bundle | `publish-pipeline` | the manifest and workflows | scheduled sync; a bundle plugin with one agent per workflow (Claude Code) and a portable manifest (Codex) | `claude plugin validate --strict` passes; the bundle versions only when content changes |
| 6 | Trigger tests | `tune-skill` (case format) | every skill's description | a `claude plugin eval` suite: one must-load case per skill, near-misses that must not load | baseline recorded; misses that repeat on a second run listed as tuning targets |
| 7 | Discovery | `findable` | the published set | topics and homepage per repo; site structured data; a directory kit with status | owner action: metadata applied from the owner's machine; forms submitted by the owner |
| 8 | Maintenance loop | `caffeinity-routing` Brew 10 · Descale | everything above | nightly health issue; weekly scheduled Brew 10 · Descale session; PROJECT.md | the loop has run once, or its first run is scheduled and the owner knows when |

## Patterns that worked

- **Manifest as the single list.** `site/skills.json` (name, repo, path, group, page kind, blurb,
  workflows). Hub, pages, indexes, sitemap, `llms.txt`, `_redirects` and the profile README are all
  generated from it; nothing is hand-copied.
- **Sync, not discovery PRs, for an owner's own repos.** Hourly: add (public repo, valid shape,
  non-empty About), refresh (HEAD moved), rename (old name redirects; keep an alias), remove (404 or
  private), hold (fails shape or no About). A failed API call stops the run.
- **Deploy without secrets.** CI builds and gates `dist/`, commits it to a `deploy` branch; a
  Git-connected Pages project serves that branch. CI then waits for the live version hash to
  match and opens one "Deploy pending" issue only if it never does. A direct-upload project cannot
  be switched to Git; create a new one and move the domain (owner action).
- **Bundle builder.** One script renders the agents from a workflow table and copies every skill
  at HEAD into the bundle, with a sources file recording each commit, and stamps a new version
  only when a content digest changes (installed users stay on a version until it changes).
- **Mods are pages, not archives.** A Claude Code mod (plugin.json, no SKILL.md) gets a page from
  its plugin.json description; it never enters the skills discovery index.
- **Scheduled jobs can lag or not fire.** After adding cron workflows, confirm the first scheduled
  run happened; until then trigger them by hand and say so.

## Owner actions to collect

A run usually ends waiting on: merging PRs, a hosting login or dashboard step, moving a domain,
applying repo metadata from the owner's machine, directory submission forms, and search-console
verification. List them together at the end of the report, each with the exact click path or
command.
