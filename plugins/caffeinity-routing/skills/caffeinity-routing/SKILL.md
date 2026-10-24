---
name: caffeinity-routing
description: >-
  Picks which caffeinity skills to run, in what order, for a goal that spans more than one of
  them, and says what each step hands the next: build and publish a skill, get a project found,
  pass a release gate, grow organic search traffic, run a job search, make a decision, learn a
  skill, run cold outbound, launch a one-person product, or set up and keep the skills themselves healthy. Checks which of those skills are
  installed and names the missing ones instead of improvising their work. Use whenever someone
  asks which skill to use, what to run first, how the skills fit together, or describes a
  multi-step outcome such as "take this idea to a published skill" or "get my site ready to
  ship and ranking", even if they never name a skill. Not for a request one skill already owns
  (load that skill directly), and not for doing a step's work itself: the named skill does it.
---

# caffeinity-routing

A goal like "ship my site" or "get hired" crosses several skills, and each one only knows its own
edges. This skill holds the map: eleven numbered brews (Brew 1 to Brew 11; older docs call them W1 to W11), each an ordered list of
skills with what every step receives and what it hands on. Other skills cite these numbers
(`release-gate-chair` implements Brew 3 · Espresso; `seo-crawl` is the first step of Brew 4 · Cold brew), so keep them stable.

Routing is a decision, not the work. Name the workflow, the first step and its input, then hand
off. Doing a step's job here produces a worse version of a skill that already exists.

## Ground rules

- **One skill owns a single-step request.** If the request fits one skill's description, route
  straight to it and stop. A workflow is for goals that need two or more.
- **Name the brew by number and name, and the steps by skill name.** "Brew 4 · Cold brew, step 1: seo-crawl on
  https://example.com" is checkable; "do some SEO first" is not.
- **Never fill a missing step yourself.** Run `scripts/route_check.py` and report what is not
  installed with its install command. A step skipped for lack of a skill is reported as skipped,
  not as passed.
- **Carry outputs forward verbatim.** Each step's output is the next step's input, as listed in
  `references/workflows.md`. Summarizing between steps loses the evidence the next skill checks.
- **Respect each skill's own gates.** A release gate that says HOLD, a keyword map that is not
  signed off, or a draft the user has not confirmed stops the workflow there. Say so; do not
  route around it.

## Workflow

1. **Classify the goal.** Read the request against the workflow table below. If it fits one
   skill, route there and stop. If it fits more than one workflow, pick the one whose first step the user
   can start now and say which you set aside.
2. **Check what is installed.** Run:

       python scripts/route_check.py espresso      # one brew, by name, number or old W id
       python scripts/route_check.py --all         # every brew

   It reads `references/workflows.md` and looks for each skill's `SKILL.md` under the usual skill
   folders (`~/.claude/skills`, `~/.qoder/skills`, `~/.cursor/skills`, `~/.agents/skills`,
   `.claude/skills` and plugin caches). Add `--path <dir>` for any other location.
3. **Lay out the route.** Open `references/workflows.md` for the chosen workflow and write one
   line per step: skill, what it receives, what it hands on, and whether it is installed. Mark the
   chain skill if one already packages the steps (Brew 1 · Pour-over has `skill-launch`, Brew 3 · Espresso has the
   `release-gate-*` forks, Brew 4 · Cold brew has `seo-polish` and `keyword-resolver`).
4. **Hand off step 1.** Load the first skill with its input. When a step finishes, come back to
   the route, record the step's verdict or output location, and hand off the next one.
5. **Close the loop.** When the last step finishes, list each step as done, skipped (with the
   reason) or stopped at a gate, plus the one next action.

## The brews

| # | Goal | Steps, in order |
| --- | --- | --- |
| Brew 1 · Pour-over | Build a skill and make it installable | draft-skill or prompts-to-skill → tune-skill → prompts-to-skill-release → skill-to-mod (only if it must run at a fixed moment) |
| Brew 2 · Bloom | Get a repo, skill or plugin found | findable → publish-pipeline → upstream-check |
| Brew 3 · Espresso | Decide whether a site is safe to launch | web-preflight → pre-ship-security-red-team → pre-ship-performance-audit → release-gate-chair |
| Brew 4 · Cold brew | Grow organic search traffic | seo-crawl → keyword-guard → wordsmith → pre-ship-performance-audit or platform-content (if they apply) |
| Brew 5 · French press | Land a job | recruiter-lens → applicant-kit → application-pilot → career-track |
| Brew 6 · Cupping | Make a decision | research-brief → data-readout (if there is data) → crash-test → strategy-memo |
| Brew 7 · Slow drip | Learn a skill | topic-primer → study-system → course-builder (only when teaching a group) |
| Brew 8 · Nitro | Run cold outbound | cold-email-list-gate → cold-email-ops → sales-copy |
| Brew 9 · Moka pot | Launch a one-person product | solo-income-blueprint → site-prompt → production-code → paper-trail → Brew 3 · Espresso → platform-content |
| Brew 10 · Descale | Maintain the skill family | tune-skill (regress.py) → prompts-to-skill-release (if behaviour changed) → upstream-check |
| Brew 11 · Estate roast | Stand up or audit a skill estate | skill-estate (eight gated phases over the whole collection) |

Per-step inputs, outputs and stop conditions are in `references/workflows.md`. Open it at step 3,
and whenever a user asks what one skill needs from the previous one.
`references/trigger-cases.md` holds the hand-run trigger cases; open it when tuning this
description or adding a workflow.

## Report

Lead with the route: workflow number, then one line per step with its status. Then the missing
skills with install commands, any gate that stopped the run, and the one next action. Say which
steps you only planned and which actually ran.
