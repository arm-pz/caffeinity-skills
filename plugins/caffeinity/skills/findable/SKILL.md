---
name: findable
description: >-
  Sets up discovery for a GitHub repo, agent skill, Claude Code plugin or MCP
  server so people and agents can find it by what it does, not only by its name:
  audits current visibility and same-name collisions, derives the queries people
  actually search, drafts the GitHub About text, topics, README opening, release
  notes and a skill page for a website, lists directories to submit to, and plans
  a re-check. Use whenever the user wants more stars, installs, traffic or
  visibility for a repo, skill or skill page, asks why a similar project shows up
  instead of theirs, or is about to publish a skill, plugin or MCP server. Not for
  finding repos or skills for a task, which is the reverse problem. Not for
  authoring a new skill (use draft-skill) or tuning a SKILL.md description so an
  agent triggers it better (use tune-skill).
---

# Findable

Projects get found through what they say about themselves in the places search engines, directories and agents read: the GitHub About text and topics, the first lines of the README, a page on a site, directory listings. A name alone rarely works, and works worst when another project shares it. This skill makes those surfaces say what people actually search for, truthfully, and then checks whether it worked.

## Ground rules

- **Describe only what is real.** Read the repo (README, SKILL.md, commands, tests) before writing anything. Do not claim features, compatibility, benchmarks, install counts, stars or reviews that the repo does not support.
- **Queries before copy.** Work out what people type, by task rather than by name, then write every surface from those queries.
- **No gaming.** No star trading or buying, fake reviews, topic stuffing, or undisclosed promotion. It gets repos flagged, and the trust damage outlasts any short-term bump. When promoting your own work, say it is yours.
- **Examples must be real.** Leave a labeled slot for a real output rather than writing a sample the project never produced.
- **Public changes need a go-ahead.** Draft the kit and the commands first. Run `gh repo edit`, release, or submission steps only when the user confirms and the tools are available.
- **Verify what changes.** Directory rules, GitHub limits and installer behavior change. Check current docs for anything exact you are about to state, and treat the lists in `references/distribution.md` as starting points, not facts.

## Two audiences, two jobs

A skill's `description` frontmatter is read by agents deciding when to load it. Everything this skill produces is read by people, search engines and directories. Keep them separate: this skill does not tune triggering (that is `tune-skill`'s job, and `draft-skill` writes a new one), but it must not leave the two telling different stories, and in a family of sibling skills it must not give two of them the same trigger language.

## Workflow

1. **Read the repo.** Find out what it does in one sentence, who it is for, the install command, the agents it supports, and its commands or tools. If a page is blocked to you, ask the user to paste the README and SKILL.md instead of guessing.
2. **Audit the baseline.** Follow `references/audit.md`: search by name, search by task, check same-name projects, and inspect the repo's metadata. Record where the project appears and where comparable projects do. Absence from results is an index and distribution gap, not a verdict on quality.
3. **Fix the target queries.** Write five to ten queries a stranger would type, with at least two per capability and none that depend on knowing the owner or project name. Show them to the user. Everything below is written from them.
4. **Resolve name collisions.** If another project shares the name, lay out the choice: keep the name and qualify it everywhere, or rename while stars and installs are near zero and switching is cheapest. The user decides.
5. **Draft the kit.** Use `references/listing.md` for the GitHub About text, topics, README opening, release notes, social preview brief and license reminder, and `references/site-page.md` for a page on the user's site. Run `scripts/check_listing.py` on the drafts and fix every failure.
6. **Plan distribution.** Follow `references/distribution.md`: search for the current directories and lists that fit this kind of project, check each one's submission rules, and prepare the entry text. Do not claim to know how a directory ingests projects unless you checked.
7. **Hand over.** Write the kit as files (a `discovery-kit.md` plus any site pages), with copy-paste commands. Apply only what the user approves.
8. **Plan the re-check.** Record the baseline and name a date, two to three weeks out, to re-run the same queries and compare. Indexing lags, so one check right after publishing proves little.

## The kit file

Produce `discovery-kit.md` with these sections, each short:

0. Baseline (what the audit found)
1. Target queries
2. Name decision
3. GitHub listing: About, homepage, topics
4. README opening
5. Release notes
6. Site page(s), as separate files
7. Distribution list with entry text
8. Apply commands
9. Re-check plan

Write About and Topics in the exact format shown in `references/listing.md` so `scripts/check_listing.py --kit discovery-kit.md` can validate them.

## Families of projects

When the project has siblings (a judging skill and a producing skill, say), give each its own queries, cross-link them in the README opening and on the site pages, and state the boundary in one line on each, so a search lands on the right one. Check that no two descriptions claim the same trigger phrases.

## One surface to know about

If the user hosts several skills on their own domain, a machine-readable discovery index at `/.well-known/agent-skills/index.json` lets installers resolve them with `npx skills add https://their-domain`. Publishing that index is its own job; hand it to `publish-pipeline`, which builds the index, the per-skill pages and the sitemap from one manifest, rather than reinventing it here, and verify the current spec before relying on the details. When the listings already exist but disagree with the repos, that is drift, not discovery: hand it to `upstream-check`.
