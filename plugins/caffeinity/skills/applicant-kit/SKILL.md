---
name: applicant-kit
description: >-
  Produces tailored job-application material from a resume and a job description:
  a decoded JD table with must-have versus nice-to-have, resume bullets rewritten
  as action-task-result-impact, a keyword-gap placement map, five drafted resume
  summaries, a full LinkedIn rewrite, and twenty likely interview questions with
  sample answers. Use whenever the user wants the better version written: a resume
  rewritten for a role, stronger bullets, missing keywords worked in, a summary or
  LinkedIn headline and About section, or interview answers. Not for judging
  (scans, critiques, ATS checks, rejection reasons, gap analysis, LinkedIn audits,
  predicting questions): use the recruiter-lens skill. Not for running the search
  itself (finding roles, the application tracker, follow-ups, interview briefings):
  use the application-pilot skill. Optionally uses the third-party dani-aisystems
  recruiter-lens MCP server for checkable GitHub facts; it runs third-party code.
  Works standalone or with either companion.
---

# Applicant Kit

Six workflows that produce the material a job application needs, plus a hand-off to the recruiter-lens skill for the judging that should not be duplicated here.

**Credits.** The workflow patterns are adapted from a public prompt thread by @codeby_abir on X. The optional GitHub-facts integration uses the third-party recruiter-lens MCP server from dani-aisystems; this skill is not affiliated with it.

## Two things named "recruiter-lens"

Keep these apart, because they are unrelated projects that share a name:

- **recruiter-lens skill** (the sibling of this skill). It judges: 6-second scans, critiques, ATS checks, reject reasons, question prediction, gap analysis and tailoring coverage, LinkedIn audits, and AI-use guidelines. This skill defers to it for anything that is a verdict. See `references/recruiter-lens-skill.md`.
- **recruiter-lens MCP server** (third-party, dani-aisystems). It reports checkable GitHub facts through `audit_repo` and `recruiter_scan`. It is optional and runs third-party code with a GitHub token. See `references/github-mcp.md`.

The division of labor: recruiter-lens judges, applicant-kit produces. If a request is "tell me what is wrong", it belongs to the recruiter-lens skill. If it is "write me the better version", it belongs here.

## Step 1: Pick the mode

Match the request to a mode, then read the matching section of `references/modes.md` before writing anything. It holds the exact output format for each mode.

| # | Mode | User says things like | Needs |
|---|------|----------------------|-------|
| 1 | Decode the JD and tailor | "decode this job description", "rewrite my resume for this role" | JD (+ resume to tailor) |
| 2 | Rewrite bullets | "improve my bullets", "make my experience sound stronger" | Resume, target role |
| 3 | Keyword placement map | "add the missing keywords", "work the JD keywords in" | Resume + JD |
| 4 | Summaries | "write my resume summary / profile" | Resume + JD |
| 5 | LinkedIn rewrite | "rewrite my headline / About / experience" | Resume, target role |
| 6 | Interview answer pack | "prepare my answers", "what will they ask me and what do I say" | Resume + JD |
| 7 | Judge it (hand-off) | "why am I not getting interviews", "ATS check", "scan my resume", "critique it" | Resume |

Mode 7 is a router, not a workflow of its own. Hand the request to the recruiter-lens skill. Only when that skill is not available does the short fallback in `references/modes.md` apply.

If the user gives a resume and JD with no clear ask, offer the full pass (below) in one line and start with modes 1 and 3, because they establish what the role values and what the resume lacks, and every other mode builds on that.

If a required input is missing, ask for it once, in a single short message, naming everything that is missing together. Resumes and JDs often arrive as uploaded files: read them with the file-reading skill rather than asking the user to paste. If the final deliverable is a resume file the user wants to send, build it with the docx skill, using the plain ATS-safe structure described in `references/modes.md` (mode 1).

## Step 2: Follow the ground rules

These exist because the output gets used in real applications, where mistakes cost the person an interview or a job.

- **Never invent.** The resume is the evidence base. Do not add employers, titles, dates, tools, certifications, or numbers that the user has not given. A fabricated claim is the most damaging thing this skill can produce, because the candidate has to defend it in an interview and a background check. When a metric would strengthen a line and the resume does not supply one, either keep the line qualitative or ask the user for the number. Mark any open slot clearly, for example `[team size?]`.
- **Truth before keywords.** Only add a JD keyword where the user's real experience supports it. A keyword they lack is a gap to report, not a word to sneak in. Place keywords inside true sentences rather than stuffing lists; an ATS may parse the list, but a human reads the rest.
- **Sound like a person.** Avoid filler such as "hardworking", "results-driven", "team player", "passionate", "detail-oriented", "dynamic", "proven track record", and "leveraged" used as a verb for everything. Prefer concrete nouns, specific tools, and varied sentence openings, so the text reads like the candidate wrote it on a good day, not like generated copy. When the recruiter-lens skill is available, its `ai-guidelines` (what is fine, risky, and off-limits when using AI in a job search) take precedence over these defaults.
- **Be honest about what you cannot measure.** There is no real ATS here. Any score or "match" estimate is a rubric-based judgment; present it that way and never as an ATS result.
- **Show your evidence.** When you rewrite a line, quote the original so the user can see what the change is based on.
- **Separate facts from inferences.** Say which statements come from the resume or JD and which are your reading of them, especially when you infer a JD's hiring goals.

## Step 3: Hand off or enrich when companions are present

- **recruiter-lens skill available:** let it do the judging and feed its findings into modes 1 to 6. Read `references/recruiter-lens-skill.md` for which sub-skill answers which question and how to hand over.
- **Technical role and a GitHub handle available:** the third-party MCP server can supply GitHub facts for modes 3, 5 and 6. Read `references/github-mcp.md` first, including its trust note.
- **Neither present:** carry on standalone. Every mode works without them; the companions only make the judging and the evidence stronger.

## Full pass (when the user wants everything)

Run in this order, because later steps reuse the earlier findings, and keep a short running list of "gaps the user must close" instead of repeating them in every mode:

1. Judge the current resume (mode 7: hand off to recruiter-lens, or the fallback)
2. Mode 1: decode the JD and tailor
3. Mode 3: keyword placement map against the tailored resume
4. Mode 2: bullet rewrites
5. Mode 4: summaries
6. Mode 5: LinkedIn rewrite
7. Mode 6: interview answer pack
8. Hand the finished resume back to recruiter-lens for a final check, when it is available

Long outputs, especially mode 6, are easier to use as a file the user can keep. Offer to save them when the reply gets long, and write one when they say yes.
