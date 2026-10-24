---
name: skill-estate
description: >-
  Takes a whole collection of agent skill repos from scattered to published, consistent and
  self-maintaining, in gated phases: inventory every repo, reconcile site, marketplace and README
  listings, test and tune the family, close workflow gaps, wire publishing so new skill repos go
  live on their own, bundle a plugin with agents, add trigger tests and directory listings, and
  leave a maintenance loop and a map. Each phase hands off to the skill that owns it and ends in
  PRs. Use when someone's skills site and GitHub disagree, wants all their skill repos audited or
  cleaned up, wants new skills to publish themselves, or wants that cleanup repeated on another
  org, even if they never say estate. Not for one skill (use tune-skill), one listing (use
  findable), the site pipeline alone (use publish-pipeline), or weekly upkeep (use
  caffeinity-routing's Descale brew).
---

# skill-estate

A skill collection decays at its seams, not inside any one skill: the site lists 22, the
marketplace 25, GitHub 27; a skill hands off to one that was never published; a repo was renamed
and three pages still use the old name; nothing deploys unless someone remembers. Every one of
those was found and fixed in the run this skill is distilled from (`references/brief.md`). This
skill runs that sweep again, in order, and stops at each gate.

It orchestrates. Each phase belongs to a skill that already exists; doing a phase's work here
produces a worse copy of that skill. When a phase's owner is not installed, say so and stop that
phase instead of improvising it.

## Ground rules

- **Measure before you change.** Phase 1 produces counts from the repos themselves (a skill exists
  only if a `SKILL.md` does); every later claim cites them. A description or a README is not
  evidence that a skill exists.
- **One PR per repo per phase, owner merges.** Batch the edits a phase makes to one repo into one
  PR with the evidence in the body. Merge only when the owner has said to; say which PRs wait.
- **No secrets in CI.** Deploys either run from the owner's machine or are pulled by the host
  (a Git-connected Pages project watching a build branch). Never ask for an API token to be
  stored in GitHub to make a phase easier.
- **Additive by default.** Add topics, pages, entries and redirects; remove only what is provably
  gone (repo deleted or private), and keep an alias or a 301 for every rename.
- **Report what ran.** Each phase ends with checks run, checks only written, and owner actions
  pending. A plan is not a pass.

## Workflow

Open `references/phases.md` before starting: for each phase it names the owner skill, what it
receives, what it hands on, and the gate. Run the phases in order; a later phase may start only
when the earlier gate passed or the owner waived it.

1. **Inventory.** List every repo the owner controls; classify each as skill, mod, plugin bundle,
   or not a skill. Count what the site, marketplace(s) and profile README publish. Owner:
   `upstream-check` (its drift checker does the counting).
2. **Reconcile listings.** One manifest decides what is public; generate the site, indexes,
   sitemap and README block from it. Follow renames with aliases and 301s. Owner: `publish-pipeline`.
3. **Test and tune.** Validate every SKILL.md, run the family regression, fix FAILs and dangling
   handoffs, run the cheapest real targets (the site itself is a good one). Owner: `tune-skill`,
   plus the check skills on the site (`web-preflight`, `seo-crawl`).
4. **Close workflow gaps.** Map the workflows across skills; every handoff must land on a published
   skill. Draft the missing ones. Owners: `caffeinity-routing` (the map), `draft-skill` (new skills).
5. **Publish and bundle.** Hourly sync from GitHub to the site and profile README; a plugin that
   bundles every skill plus one agent per workflow, for Claude Code and Codex. Owner:
   `publish-pipeline`; the bundle builder pattern is in `references/phases.md`.
6. **Trigger tests.** A case per skill (must load) and near-misses (must not), run with
   `claude plugin eval` on the owner's login, never in CI. Record a baseline.
7. **Discovery.** Topics and homepages on every repo, structured data on the site, and a
   directory kit the owner submits. Owner: `findable`.
8. **Maintenance loop.** A nightly health check that opens an issue on regression, and a weekly
   scheduled session that runs the Descale brew and opens PRs. Write the project map (`PROJECT.md`): what
   exists, how a skill goes live, the workflows, and the gaps still open.

## Report

Lead with the inventory counts before and after. Then one line per phase: done, waived (why), or
stopped at its gate, with the PRs it opened. Then owner actions pending (logins, merges,
dashboard steps, directory forms), the gaps still open, and the one next action.

`references/brief.md` holds the original eight requests this skill was built from; reread it when
a phase's scope is unclear. `references/trigger-cases.md` holds the trigger cases; open it when
tuning this description.
