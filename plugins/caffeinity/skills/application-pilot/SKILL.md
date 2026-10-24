---
name: application-pilot
description: >-
  Runs the job search around the applications: turns role criteria into a live
  shortlist, scores each role for fit with evidence, keeps a reviewable tracker
  (status, submission and follow-up dates, dedupe), flags roles gone quiet past
  an aging threshold, drafts follow-ups and interview briefings, and reviews the
  funnel weekly. Use when the user wants to find, organize, compare, track or
  follow up on roles: "find backend roles posted this week", "build my
  application tracker", "brief me before Thursday's interview". Not for writing
  application material (resume, bullets, summaries, LinkedIn, answer scripts):
  use applicant-kit. Not for judging (scans, ATS checks, critique, rejection reasons,
  gap analysis): use recruiter-lens. Markdown and CSV only: no CLI, no cloud
  state, no telemetry, no browser automation, no submit path; the user approves
  every application. If job-application-agent is installed and the user wants
  automated filling, batch submission, or a programmatic ledger, that skill owns
  it.
version: 1.0.1
argument-hint: "[mode] [target]"
user-invocable: true
metadata:
  version: "1.0.1"
---

# Application Pilot

Run a focused, honest, reviewable job search: criteria, discovery, fit scoring, tracker, follow-ups, interview briefings, and a weekly read of what is working. This skill coordinates the search; `applicant-kit` writes the material and `recruiter-lens` judges it.

**Credits.** The workflow shape is adapted from a public prompt thread by @HeyAirahAi on X (October 2026). That thread's central move, sending hundreds of automated applications overnight, is deliberately not implemented here; see the submission rule below.

## Where this skill ends and the others begin

| Skill | One-line job | It says |
|---|---|---|
| application-pilot | runs the search by hand | "what should I apply to, where does it stand, what happens next" |
| applicant-kit | produces material | "write me the better version" |
| recruiter-lens | judges material | "tell me what is wrong" |
| job-application-agent | heavy automation | "fill and submit these for me" |

Skills sharing one subject must not share triggers, or the wrong one fires half the time. `references/siblings.md` holds the hand-off table for applicant-kit and recruiter-lens, the precedence rule against job-application-agent, and the exact wording that keeps the boundaries intact.

application-pilot is the desk, not the machine: a reviewed shortlist, one plain tracker file, drafts the user sends, and briefings. It has no CLI, no cloud state, no telemetry, and no browser submission path, and it does not acquire those to be more convenient.

## Step 1: Pick the mode

Match the request to a mode, then read the matching section of `references/modes.md` before writing anything. It holds the exact output format for each mode.

| # | Mode | User says things like | Needs |
|---|------|-----------------------|-------|
| 1 | Set the search brief | "help me decide what to apply for" | role, level, location, constraints |
| 2 | Discover roles | "find roles matching my brief from this week" | brief (mode 1) |
| 3 | Score fit | "which of these are worth my time" | list of roles + resume |
| 4 | Build the packet | "get this one ready to send" | one role + resume (hand-off to applicant-kit) |
| 5 | Track applications | "build/update my tracker" | applications so far |
| 6 | Follow-up queue | "what went quiet", "write the follow-ups" | tracker |
| 7 | Interview briefing | "brief me before this interview" | scheduled role + company |
| 8 | Funnel review | "how is my search going" | tracker history |

If the request is really "fill these forms and submit them", that is the job-application-agent skill's job when it is installed; say so in one line and stop rather than half-implementing automation here. With only this skill installed, the answer is the same packet-plus-approval flow it always is.

If the user gives a resume and a vague ask ("run my job search"), confirm the mode 1 brief in one short message, then run 2, 3, 5 and stop before any material work. Do not silently pick a target role.

If a required input is missing, ask once, naming everything missing together. Resumes and JDs often arrive as files: read them with the file-reading skill instead of asking for a paste.

## Step 2: Follow the ground rules

These exist because a job search runs under someone's name. A fabricated claim or a mass of generated applications costs the candidate their account or their reputation, not yours.

- **Never submit, never send.** This skill prepares; the user dispatches. Show the final materials and the exact target, then wait for approval of that specific action. No batch of applications is ever opened, filled, or sent unattended, and the tracker records a submission only after the user says it happened.
- **Never invent.** No experience, qualifications, dates, metrics, hiring-manager or recruiter names, application statuses, salary figures, or company facts. Everything in a follow-up or briefing must trace to the user's materials, a posting, or something read this session. Mark open slots, for example `[recruiter name?]`.
- **No invented recency.** If a posting shows no date, record `unknown`, not "recent". Never present an undated listing as new. See `references/sources.md`.
- **No status claims without evidence.** Do not say an application was opened, viewed, or read, or that a recruiter responded, unless the user or a tool showed it. Unknown is a valid cell.
- **Fit scores are a rubric, not an ATS.** State the rubric, show the matched evidence and the gaps, and label the number as this skill's estimate. It is a prioritisation aid with no predictive power about interviews.
- **Volume is not the lever.** Reject "apply to 500 while you sleep" as a plan. Automated bulk applying breaks LinkedIn's and Indeed's terms (LinkedIn's user agreement bars automated access; both run detection and suspend accounts), and employers now filter generated applications. A reviewed shortlist with specific material outperforms a spray at the same hour of effort. Say this plainly when a user asks for the spray.
- **Respect access rules.** Use only the browsing and search tools the host actually provides, within each site's access rules. If a site forbids automated access, or the tool is not available, fall back to links, drafts, and a tracker rather than working around it.
- **Protect the candidate's data.** Keep the tracker and materials local. Do not paste a resume or personal details into third-party sites or tools the user has not chosen.
- **Keep it reviewable.** The tracker and shortlist live in a plain Markdown table or CSV the user can open, edit, and audit, not only in chat.

## Step 3: Run the loop

Discovery, scoring, and tracking feed each other, so keep the artifacts current rather than recreating them per conversation:

1. Mode 1 writes the search brief to a file the user can edit.
2. Mode 2 collects roles against it, deduped by the key in `references/tracker.md`.
3. Mode 3 ranks them; the user picks the shortlist.
4. Mode 4 hands each shortlisted role to `applicant-kit`, then to `recruiter-lens` for a check before sending.
5. Mode 5 records what the user actually submitted.
6. Mode 6 works the aging queue from the tracker and drafts, never sends.
7. Mode 7 briefs on confirmed interviews; mode 8 reads the funnel weekly.

Long outputs (a 40-role shortlist, a briefing) are easier to keep as a file. Offer to save when the reply gets long, and write one when they say yes.

## Standalone behaviour

`applicant-kit` and `recruiter-lens` make modes 4 and 7 stronger but are not required. When either is missing, say so once, do the coordination work yourself with a short note that a sibling does it better, and offer the install line rather than imitating their full output.

## Resources

- `references/modes.md`: per-mode output formats and the mode 8 funnel math
- `references/tracker.md`: tracker schema, status machine, dedupe key, aging rules
- `references/sources.md`: where roles come from, what is allowed per source, date honesty
- `references/siblings.md`: hand-off table for applicant-kit and recruiter-lens, and the precedence rule against job-application-agent
