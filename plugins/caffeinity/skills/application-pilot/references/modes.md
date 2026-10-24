# Mode formats

Read the section for the mode you are running. Formats are the deliverable; keep the prose around them short.

This desk is sized for a search a person can actually review: roughly 40 tracked rows and a 25-row shortlist. Past that, tables stop being readable and dedupe by hand stops being reliable, so say which limit is being hit and either narrow the brief or hand the volume to `job-application-agent` (`references/siblings.md`). Do not quietly grow the tables to match the request.

## Mode 1: Set the search brief

Write `job-search-brief.md` (or update it) with the user's answers. Ask only for what is missing, in one message.

```markdown
# Search brief — updated <date>
- Target roles: <titles, and the titles that are close but not wanted>
- Level: <seniority / years / "roles I can defend in an interview">
- Location: <cities, remote-only or remote-region, visa or relocation constraints>
- Non-negotiables: <salary floor, on-site days, sector exclusions, notice period>
- Evidence base: <path to resume / master resume, LinkedIn URL if any>
- Must show in materials: <e.g. .NET and AWS depth, 10 years, export-business tooling>
- Avoid: <e.g. pure team-management titles, roles needing a clearance>
- Cadence: <applications per week, follow-up threshold in days, default 7>
- Stop conditions: <e.g. pause discovery if 3 weeks with no response: review brief>
```

Confirm the brief back in two lines. A vague brief is the main reason a search turns into spray; if the user cannot name a level or a non-negotiable, say which mode you can still run (2 and 3) and what will be weaker for it.

## Mode 2: Discover roles

Deliver a shortlist table plus a sources note. One row per role, deduped per `references/tracker.md`.

```markdown
| # | Role | Employer | Location | Posted | Source | Link |
|---|---|---|---|---|---|---|
| 1 | Senior Backend Engineer | Acme | Remote (EU) | 2026-10-08 | company ATS | <url> |
| 2 | ... | ... | ... | unknown | LinkedIn | <url> |
```

Rules: exact posting URL; posting date as stated on the page, else `unknown`; never present an undated or older role as new; drop anything outside the brief's non-negotiables rather than listing it with a caveat; note the number searched versus the number kept. Cap the table at what the user can actually review, typically 15 to 25 rows, and say how many were cut and why.

## Mode 3: Score fit

Rubric first, then the table. State that the score is this skill's estimate, not an ATS match rate.

```markdown
Rubric (weights stated, evidence-based only):
- Must-have coverage: 0-40 (each JD must-have the resume can prove)
- Level and scope match: 0-20
- Domain or stack overlap: 0-20
- Constraints fit (location, salary, notice): 0-10
- Interview defensibility: 0-10  (can the candidate speak to this without bluffing)
```

| Role | Employer | Score | Strong matches | Gaps | Verdict |
|---|---|---|---|---|---|

Verdict is one of `apply`, `apply with gaps named`, `skip`. Each gap names the JD line it comes from and whether it is a real absence or a presentation problem (a presentation problem becomes a `applicant-kit` task; a real absence stays a gap and never gets smuggled into the resume).

## Mode 4: Build the application packet

Per selected role, in this order:

1. Hand the JD and resume to `applicant-kit` (its modes 1, 3, then 2 and 4 as needed) for the tailored resume and keyword work.
2. Hand the result to `recruiter-lens` (`ats-check`, then `critique`) when available.
3. Report the target: role, employer, URL, and what the user is about to send.
4. List anything still unverified: `[salary band?]`, `[recruiter name?]`.
5. Stop. The user submits.

Then record the row in the tracker as `ready`, not `submitted`.

## Mode 5: Track applications

Own the tracker file described in `references/tracker.md`. Update from what the user reports or what a tool shows this session. If the user pastes a messy list, normalise it into the schema and show the mapping in three lines. Never mark `submitted` without the user or evidence.

## Mode 6: Follow-up queue

Split into two outputs.

```markdown
Quiet past <threshold> days (<n>):
| Role | Employer | Applied | Days quiet | Last touch | Channel |
```

Then the drafts, each under 90 words, each naming the role and one specific line from its JD, one line on what the candidate would deliver in the first 30 days, and no pressure. Keep the candidate's voice: plain sentences, no generated polish. Before sending anything, show the drafts and wait for approval per recipient.

If the follow-up depends on a fact not in evidence (a name, an email, a date), leave the slot bracketed and say the draft is not ready to send.

## Mode 7: Interview briefing

For a confirmed interview. Only include what you read or what the user provided this session; label the rest as unknown rather than filling it in.

```markdown
# Briefing — <role> at <employer>, <date>
What the role is about: <from the JD>
Company facts on file: <source + date for each, or "not verified">
Ten likely questions, ordered by how the JD points at them
For each: what is being tested, the evidence from the resume to use, the trap to avoid
Three questions to ask them (specific to this JD, not generic curiosity)
Open gaps to admit gracefully: <the honest one-liner for each gap mode 3 found>
Logistics unknowns: <panel, format, length, travel>
```

Question drafting belongs to `applicant-kit` mode 6 (and `recruiter-lens` `predict-questions` for the list). This mode assembles it with the company and JD context and keeps it in one file the user can read the morning of.

## Mode 8: Funnel review

From the tracker, with real counts only. If a stage has no data, report it as unmeasured.

```markdown
Last <period>: discovered <n>, shortlisted <n>, packets ready <n>, submitted <n>
Responses: <n> (<rate> of submitted) | interviews <n> | rejections <n> | no reply <n>
By source: <same funnel per source>
By role type: <where responses actually come from>
Read: <one or two sentences, and the single change to try next period>
```

The rate is arithmetic on the user's own rows, not a benchmark. Compare against the user's earlier weeks, not against invented industry averages. If the numbers are too small to mean anything, say so and point at the qualitative signal instead (which brief line produced nothing).
