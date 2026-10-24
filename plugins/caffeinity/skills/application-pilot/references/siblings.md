# Working with the other job-search skills

Skills sharing one subject must not share triggers, so the division is stated in all of them.

- **recruiter-lens judges** ("tell me what is wrong")
- **applicant-kit produces** ("write me the better version")
- **application-pilot coordinates** ("what should I apply to, where does it stand, what happens next")
- **job-application-agent automates** ("fill these forms and submit them")

Command and mode names below were checked against the installed skills in October 2026. Where an installed skill behaves differently, trust the installed skill.

## Who answers what

| Question | Owner | Notes |
|---|---|---|
| What roles match me, where are they posted, which are new? | application-pilot mode 2 | the other two never search |
| Is this role worth applying to? | application-pilot mode 3 | rubric over the user's own evidence |
| How well does my resume cover this JD? | recruiter-lens `gap-analysis`, `tailor` | coverage verdict; feeds mode 3's gap column |
| Write the tailored resume, bullets, summaries, LinkedIn, answers | applicant-kit modes 1 to 6 | mode 4 hands the target back here |
| Will an ATS parse it, what is the 6-second impression, red flags? | recruiter-lens `ats-check`, `scan`, `critique`, `red-flag-review`, `reject-reasons` | run before the user sends |
| What may I use AI for in a job search? | recruiter-lens `ai-guidelines` | takes precedence over all three skills' defaults |
| Keep my list of applications, dates, follow-ups | application-pilot modes 5 and 6 | neither sibling owns a tracker |
| Brief me before Thursday's interview | application-pilot mode 7 | assembles applicant-kit mode 6 and recruiter-lens `predict-questions` |
| Is my search working? What do I change? | application-pilot mode 8 | funnel from the user's own rows |
| Cover letters, offer and salary negotiation, relocation or visa advice | none | answer normally; do not force it through a skill |

## Hand-off wording

One line, then the call: "This is material writing, so I am handing it to `applicant-kit` mode 1." If the environment can invoke a skill by name, do it; otherwise give the command, for example `/applicant-kit` or `/recruiter-lens ats-check`. Take their findings as given: this skill turns verdicts into next actions, it does not re-judge them.

Never let the tracker imply work that has not happened. A `ready` row means a packet exists; only the user makes it `submitted`.

## Standalone fallback

If a sibling is not installed, say so once and keep going with a short note that the sibling does it better. Do not imitate their full output. Offer:

```
npx skills add arm-pz/applicant-kit --skill applicant-kit
npx skills add arm-pz/recruiter-lens --skill recruiter-lens
```

## The heavyweight neighbour: job-application-agent

`job-application-agent` is a different kind of skill: an installed Node CLI with OS-keychain profile storage, a discovery-source catalog, score gates, append-only ledgers, cloud state and leases, browser form filling and uploads, and an autonomy mode that submits without a per-application prompt. It is not an arm-pz skill and this skill does not speak for it. Its behaviour below is read from its own `SKILL.md`; where the installed skill differs, trust the installed skill.

| Owns | Why it is not this skill's |
|---|---|
| Filling and submitting applications, in batches or unattended | application-pilot has no submit path by design |
| `score --stdin` gates, `ledger check`, duplicate requisition detection | deterministic code beats a Markdown table at this |
| Cloud leases, rounds, attention queues, telemetry, outcome datasets | infrastructure, not a desk |
| Verified-source catalogs and community-shared boards | it maintains them; this skill reads pages the user opens |

Hand off, in one line, when: the user asks to auto-fill or auto-submit, wants the same job de-duplicated across many boards programmatically, wants a ledger that survives agents, or asks for outreach/bulk tracking at volume. Example: "That is automated submission, so it belongs to the job-application-agent skill if you have it installed; here is the packet and the tracker row for you to send."

What stays here regardless: the search brief the user edits, the reviewed shortlist, follow-up drafts, interview briefings, the funnel read, and every hand-off to applicant-kit and recruiter-lens. A user can run both skills at once, and often should: this one decides what is worth applying to, that one pushes the forms.

Say plainly, without editorialising, if the user is about to rely on the neighbour for volume: automated submission is where LinkedIn's and Indeed's terms bite, and its analytics defaults share structured usage plus the candidate's name and email with the maintainer, with community sharing of job links on by default. Point at its own `telemetry disable`, `telemetry identity disable`, and `sources sharing disable` commands. Do not change its state yourself, and do not touch its stored autonomy grant unless the user asks.

## Reciprocal boundary wording

For the other two skills' descriptions, so all three state the same split:

> Not for running the search itself (finding roles, the application tracker, follow-ups, interview briefings): use the application-pilot skill.

And the matching non-activation group in both `tests/test-discovery.md` files:

- "Find me backend roles posted this week."
- "Build/update my application tracker."
- "Which of my applications went quiet past seven days?"
- "Write the follow-up for the ones with no reply."
- "Brief me before Thursday's interview."

All five belong to application-pilot.
