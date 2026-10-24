# Brews

The caffeinity workflows are called brews: each has a number, a brew name and a plain goal, as in
"Brew 3 · Espresso: Decide whether a site is safe to launch". Other skills cite them by name; the
old ids W1 to W11 still resolve in `route_check.py`.

One section per brew. Each table row is one step: the skill, what it receives, what it hands
on, and when the workflow stops there. `scripts/route_check.py` reads the skill names in backticks
from the second column, so keep one skill per row and mark optional steps with `(optional)`.
A row may name alternatives as `` `a` or `b` ``; either one satisfies the step.

Install any of them with `npx skills add arm-pz/<skill>`, except `paper-trail`, `course-builder` and
`skill-estate`, which live in this repo: `npx skills add arm-pz/caffeinity-skills --skill <skill>`.

## Brew 1 · Pour-over: Build a skill and make it installable

| Step | Skill | Receives | Hands on | Stops when |
| --- | --- | --- | --- | --- |
| 1 | `draft-skill` or `prompts-to-skill` | a plain idea (draft-skill) or a list of prompts the user keeps pasting (prompts-to-skill) | a skill folder that passes `check_skill.py`, plus written test cases | the user has not confirmed the purpose and trigger phrases |
| 2 | `tune-skill` | the new folder and every sibling it touches | minimal edits, one owner per request, boundary pairs | two skills still claim the same request and the user has not picked an owner |
| 3 | `prompts-to-skill-release` | the tuned folder and its test cases | a zip, a version, a README, an install checklist, recorded test results | a test case fails and the user has not accepted it |
| 4 | `skill-to-mod` (optional) | a skill that must run at a fixed moment, such as before git push | a mod plugin, or a decision that a description is enough | — |

`skill-launch` packages steps 1 and 2 with a discovery pass. Offer it when the user wants one
command; keep the steps visible when they want to stop between them.

## Brew 2 · Bloom: Get a repo, skill or plugin found

| Step | Skill | Receives | Hands on | Stops when |
| --- | --- | --- | --- | --- |
| 1 | `findable` | the repo and what it does | `discovery-kit.md`: baseline, target queries, About, topics, README opening, site page, distribution list | the user has not approved public changes |
| 2 | `publish-pipeline` | the approved site page and the skill repo | a manifest entry, a generated page, both discovery indexes and the sitemap, deployed and verified | the build or the post-deploy proof fails |
| 3 | `upstream-check` | the folder of clones and the site URL | push-state verdicts and a listing drift table | a repo is behind or diverged |

`findable-polish` and `upstream-polish` add a wordsmith rewrite to steps 1 and 3.

## Brew 3 · Espresso: Decide whether a site is safe to launch

| Step | Skill | Receives | Hands on | Stops when |
| --- | --- | --- | --- | --- |
| 1 | `web-preflight` | the live or staging URL of a site the user owns | one verdict per host: PASS, PASS WITH FIXES, BLOCK or INCONCLUSIVE | never; every lane runs and keeps its own verdict |
| 2 | `pre-ship-security-red-team` | the app's source and an isolated environment, never production | findings with evidence, and an untested list | never; the chair records it |
| 3 | `pre-ship-performance-audit` | the app's source and a build | measured before and after numbers per lane | never; the chair records it |
| 4 | `release-gate-chair` or `release-gate-ledger` or `release-gate-validator` | the three lane reports (the chair and the ledger can run the lanes themselves; the validator only reads existing reports) | one posture, HOLD or ready, computed by script | HOLD |

`ship-sentinel` or the `release-gate-mod` plugin can hold `git push` and deploy commands until
step 4 has run. Install those from the caffeinity-skills marketplace.

## Brew 4 · Cold brew: Grow organic search traffic

| Step | Skill | Receives | Hands on | Stops when |
| --- | --- | --- | --- | --- |
| 1 | `seo-crawl` | the URL of a site the user owns | findings JSON with stable IDs and complete or inconclusive checks | a check is inconclusive and the user needs that area judged |
| 2 | `keyword-guard` | titles, H1s, canonicals and the sitemap inventory from step 1 | a keyword ownership map: one owner page per query | the user has not signed off the map |
| 3 | `wordsmith` | the approved findings and the ownership map | rewritten titles, meta descriptions and copy, with the author's facts kept | — |
| 4 | `pre-ship-performance-audit` (optional) | the site, when speed or Core Web Vitals came up | measured fixes | — |
| 5 | `platform-content` (optional) | the owner pages and the keyword map from step 2 | posts that point back to those pages on the platforms the audience uses | — |

`seo-polish` packages steps 1 and 3; `keyword-resolver` packages steps 2 and 3. Re-run step 1
once after changes and compare finding IDs; a code change alone does not prove a fix.

## Brew 5 · French press: Land a job

| Step | Skill | Receives | Hands on | Stops when |
| --- | --- | --- | --- | --- |
| 1 | `recruiter-lens` | a resume, CV or LinkedIn profile, plus a job description if there is one | a screening verdict and a findings block | — |
| 2 | `applicant-kit` | the findings block, the resume and the job description | tailored bullets, summaries, a LinkedIn rewrite and interview answers, from experience the user already has | the user has not confirmed a claim it would otherwise invent |
| 3 | `application-pilot` | role criteria and the tailored material | a deduplicated shortlist, fit scores with evidence, and a tracker | it never submits; the user sends every application |
| 4 | `career-track` (optional) | an offer, a promotion case or a pivot | negotiation scripts, a positioning line and a 90-day plan | — |

## Brew 6 · Cupping: Make a decision

| Step | Skill | Receives | Hands on | Stops when |
| --- | --- | --- | --- | --- |
| 1 | `research-brief` | the question | a sourced brief with dated sources and named unknowns | — |
| 2 | `data-readout` (optional) | the user's own dataset, when there is one | findings with the business implication of each | — |
| 3 | `crash-test` or `do-better` | the brief and the decision to make (crash-test), or one artifact to make as good as possible (do-better) | a merged answer with a dissent log, or one winning draft | — |
| 4 | `strategy-memo` | the brief and the crash-tested option | a decision document: recommendation, risks and roadmap | — |

## Brew 7 · Slow drip: Learn a skill

| Step | Skill | Receives | Hands on | Stops when |
| --- | --- | --- | --- | --- |
| 1 | `topic-primer` | a topic and the learner's level | teaching from foundations, concept by concept | — |
| 2 | `study-system` | the skill in progress | a practice routine, spaced repetition and a mastery check | — |
| 3 | `course-builder` (optional) | the component map, when the learner is a class or cohort rather than one person | outcomes, modules, aligned assessments and a time budget that pass `check_course.py` | an outcome is untaught or unassessed, or the plan is over its hours |

## Brew 8 · Nitro: Run cold outbound

| Step | Skill | Receives | Hands on | Stops when |
| --- | --- | --- | --- | --- |
| 1 | `cold-email-list-gate` | a lead list and the ICP | a ten-row sample verdict: load or do not load | the list fails the gate |
| 2 | `cold-email-ops` | the gated list and a monthly send target | inbox and domain capacity, per-domain limits, a warmup and audit plan | — |
| 3 | `sales-copy` | the offer and the audience | the email sequence and landing copy | — |

## Brew 9 · Moka pot: Launch a one-person product

| Step | Skill | Receives | Hands on | Stops when |
| --- | --- | --- | --- | --- |
| 1 | `solo-income-blueprint` | the user's skills, time and budget | one business model, one offer and a 7-day launch plan | — |
| 2 | `site-prompt` | the offer as a website topic | one paste-and-build prompt for the site | — |
| 3 | `production-code` | the prompt or the code to finish | a complete, runnable artifact | — |
| 4 | `paper-trail` | the offer, the built site and what it collects, stores, shares and charges | privacy, terms, refund and cookie pages that pass `check_pages.py`, with open questions listed | a `[NEEDS: ...]` fact is unanswered, or a lawyer-review trigger applies |
| 5 | `release-gate-chair` | the built site with its policy pages; run Brew 3 · Espresso in full | HOLD or ready | HOLD |
| 6 | `platform-content` | the offer, the platform and the audience | a platform-native content pack | — |

## Brew 10 · Descale: Maintain the skill family

| Step | Skill | Receives | Hands on | Stops when |
| --- | --- | --- | --- | --- |
| 1 | `tune-skill` | every installed skill folder (or the open "Skill health" issue) and `health.json`; run `regress.py --baseline` | one minimal, evidenced fix per regression, each skill re-checked, the family re-regressed with no new findings | a fix needs two skills to change which request they own and the user has not picked the owner |
| 2 | `prompts-to-skill-release` (optional) | a fixed skill whose behaviour changed, with its trigger cases | a new version, changelog line and recorded test results | a trigger case fails and the user has not accepted it |
| 3 | `upstream-check` | the local skill clones after the fixes | what is unpushed, pushed when clean, and whether the site, marketplaces and READMEs count the same skills | a clone has diverged from its remote |

Run it on a schedule (the skills-site nightly health job opens the issue it starts from) or after
any batch of skill edits. Accept an intended change with `regress.py --write` (or `health.py --accept-all` in skills-site)
only after saying why in the PR.

## Brew 11 · Estate roast: Stand up or audit a skill estate

| Step | Skill | Receives | Hands on | Stops when |
| --- | --- | --- | --- | --- |
| 1 | `skill-estate` | an owner or org with a collection of skill repos | eight gated phases run in order, each handed to its owner skill, with PRs and a list of owner actions | a phase gate fails and the owner has not waived it |

`skill-estate` packages Brew 2 · Bloom, Brew 3 · Espresso, Brew 10 · Descale and the publishing setup into one run for a whole collection.
Use Brew 10 · Descale for weekly upkeep once the estate is set up.
