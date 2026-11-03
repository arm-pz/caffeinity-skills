---
name: workflow-router
description: >-
  Picks which caffeinity skills to run, in what order, for a goal that spans more than one of
  them, and says what each step hands the next: build and publish a skill, get a project found,
  decide whether a site is safe to launch (a release gate), grow organic search traffic, land a
  job, make a decision, learn a skill, run cold outbound, launch a one-person product, keep your
  skills healthy, or audit all your skills. Checks which of those skills are installed and names
  the missing ones instead of improvising their work. Use whenever someone
  asks which skill to use, what to run first, how the skills fit together, or describes a
  multi-step outcome such as "take this idea to a published skill" or "get my site ready to
  ship and ranking", even if they never name a skill. Not for a request one skill already owns
  (load that skill directly), and not for doing a step's work itself: the named skill does it.
---

# workflow-router

A goal like "ship my site" or "get hired" crosses several skills, and each one only knows its own
edges. This skill holds the map: eleven numbered workflows (Workflow 1 to Workflow 11), each an
ordered list of skills with what every step receives and what it hands on. Other skills cite
these numbers and names (`release-gate-chair` implements Workflow 3 (launch-safely); `seo-crawl`
is the first step of Workflow 4 (grow-search-traffic)), so keep them stable. Older docs call the
workflows brews with coffee names (Brew 3 · Espresso) or W1 to W11; `route_check.py` still
resolves those.

Routing is a decision, not the work. Name the workflow, the first step and its input, then hand
off. Doing a step's job here produces a worse version of a skill that already exists.

## Ground rules

- **One skill owns a single-step request.** If the request fits one skill's description, route
  straight to it and stop. A workflow is for goals that need two or more.
- **Name the workflow by number and name, and the steps by skill name.** "Workflow 4
  (grow-search-traffic), step 1: seo-crawl on https://example.com" is checkable; "do some SEO
  first" is not.
- **Never fill a missing step yourself.** Run `scripts/route_check.py` and report what is not
  installed with its install command. A step skipped for lack of a skill is reported as skipped,
  not as passed.
- **Carry outputs forward verbatim, with the source.** Each step's output is the next step's
  input, as listed in `references/workflows.md`, and every step also gets the user's original
  inputs. Summarizing between steps loses the evidence the next skill checks.
- **Brief first, evidence last.** Every run starts with a brief (what the user expects, what
  done looks like, what is out of scope) and ends with the four-part report in
  `references/report-contract.md`: evidence, decisions, what the checks did not cover, then the
  summary.
- **Respect each skill's own gates.** A release gate that says HOLD, a keyword map that is not
  signed off, or a draft the user has not confirmed stops the workflow there. Say so; do not
  route around it.

## Workflow

1. **Classify the goal.** Read the request against the workflow table below. If it fits one
   skill, route there and stop. If it fits more than one workflow, pick the one whose first step the user
   can start now and say which you set aside.
2. **Write the brief.** Before routing a multi-step run, get the user's "Expect", "Done when"
   and "Out of scope" lines, or fill them from the request and show them. Open
   `references/report-contract.md` for the fields and for when to mark them `(assumed)` instead
   of asking. If the user cannot say what done looks like, ask about that before going on.
3. **Check what is installed.** Run:

       python scripts/route_check.py launch-safely # one workflow, by name, number or old W id
       python scripts/route_check.py --all         # every workflow

   It reads `references/workflows.md` and looks for each skill's `SKILL.md` under the usual skill
   folders (`~/.claude/skills`, `~/.qoder/skills`, `~/.cursor/skills`, `~/.agents/skills`,
   `.claude/skills` and plugin caches). Add `--path <dir>` for any other location.
4. **Lay out the route.** Open `references/workflows.md` for the chosen workflow and write one
   line per step: skill, what it receives, what it hands on, and whether it is installed. Mark the
   chain skill if one already packages the steps (Workflow 1 (build-a-skill) has `skill-launch`, Workflow 3 (launch-safely) has the
   `release-gate-*` forks, Workflow 4 (grow-search-traffic) has `seo-polish` and `keyword-resolver`).
5. **Hand off step 1.** Load the first skill with its input and the user's original inputs.
   When a step finishes, come back to the route, record the step's verdict or output location, and hand off the next one.
6. **Close the loop.** When the last step finishes, write the report in
   `references/report-contract.md`.

## The workflows

| Workflow | Goal | Steps, in order |
| --- | --- | --- |
| Workflow 1 (build-a-skill) | Build a skill and make it installable | draft-skill or prompts-to-skill → tune-skill → prompts-to-skill-release → skill-to-mod (only if it must run at a fixed moment) |
| Workflow 2 (get-found) | Get a repo, skill or plugin found | findable → publish-pipeline → upstream-check |
| Workflow 3 (launch-safely) | Decide whether a site is safe to launch | web-preflight → pre-ship-security-red-team → pre-ship-performance-audit → release-gate-chair |
| Workflow 4 (grow-search-traffic) | Grow organic search traffic | seo-crawl → keyword-guard → wordsmith → pre-ship-performance-audit or platform-content (if they apply) |
| Workflow 5 (land-a-job) | Land a job | recruiter-lens → applicant-kit → application-pilot → career-track |
| Workflow 6 (make-a-decision) | Make a decision | research-brief → data-readout (if there is data) → crash-test → strategy-memo |
| Workflow 7 (learn-a-skill) | Learn a skill | topic-primer → study-system → course-builder (only when teaching a group) |
| Workflow 8 (run-cold-outbound) | Run cold outbound | cold-email-list-gate → cold-email-ops → sales-copy |
| Workflow 9 (launch-a-product) | Launch a one-person product | solo-income-blueprint → site-prompt → production-code → paper-trail → Workflow 3 (launch-safely) → platform-content |
| Workflow 10 (maintain-skills) | Keep your skills healthy | tune-skill (regress.py) → prompts-to-skill-release (if behaviour changed) → upstream-check |
| Workflow 11 (audit-a-skill-estate) | Audit all your skills | skill-estate (eight gated phases over the whole collection) |

Per-step inputs, outputs and stop conditions are in `references/workflows.md`. Open it at step 4,
and whenever a user asks what one skill needs from the previous one.
`references/trigger-cases.md` holds the hand-run trigger cases; open it when tuning this
description or adding a workflow.

## Report

For a routing answer (no step has run yet): the workflow number and name, the brief, one line per
step with whether it is installed, the missing skills with install commands, and the first
hand-off.

After a run: the four sections of `references/report-contract.md`, in order.

1. **Evidence:** one line per step with its status and the deciding line of its output. A step
   with no evidence is planned, not done.
2. **Decisions and assumptions:** what the run chose that the user did not.
3. **What the checks did not cover:** for each green verdict, what it proved and what it left
   open, plus the answer to "what did this run miss?"
4. **Summary and next action:** the outcome against the brief's "Expect" line, whether "Done
   when" was met, and the one next action.
