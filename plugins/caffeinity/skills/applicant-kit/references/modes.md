# The modes

Contents: [1 Decode the JD](#1-decode-the-jd-and-tailor) · [2 Rewrite bullets](#2-rewrite-bullets) · [3 Keyword placement map](#3-keyword-placement-map) · [4 Summaries](#4-summaries) · [5 LinkedIn rewrite](#5-linkedin-rewrite) · [6 Interview answer pack](#6-interview-answer-pack) · [7 Judge it (hand-off)](#7-judge-it-hand-off)

Every mode inherits the ground rules in SKILL.md: never invent experience or numbers, only place keywords the user's experience supports, and quote the original line when changing it.

The recruiter-lens skill judges and this skill produces. Where a mode below touches judging, it says what to take from recruiter-lens when it is available and what to do standalone when it is not.

---

## 1. Decode the JD and tailor

**Goal:** Work out what the employer actually wants, then tailor the resume to it.

**Inputs:** JD (required). Resume or resume template (needed for the tailoring half).

**Where coverage analysis lives:** how well the resume already covers the role is recruiter-lens's `gap-analysis` and `tailor`. When it is available and the user wants the coverage view, take it as the starting point. This mode's own contribution is the decoded JD and the written, tailored resume. Standalone, do the coverage read yourself as part of the Gaps and honest notes section.

**Output, in this order:**

1. **Role in one sentence:** the problem this hire exists to solve, in plain words.
2. **Decode table:**

| Category | Item | JD evidence (short paraphrase) | Priority |
|---|---|---|---|

Use these categories: *Key skills*, *Responsibilities*, *Hiring goals* (the pain behind the posting, often inferred from phrases like "scale", "migrate", "own", "greenfield"; label these as inferences), *ATS keywords* (the exact strings, plus common variants and acronyms, e.g. "Amazon Web Services (AWS)"), *Standout traits* (signals that would separate a strong candidate from an adequate one). Priority is Must, Should, or Nice, judged by how often and how early the JD stresses it. Keep required and preferred requirements visibly separate when the JD itself separates them.

3. **Tailored resume:** if a resume was supplied, rewrite it for this role by reordering and rewording what is already true. If only a template was requested, give the structure below with guidance in each section.
4. **Gaps and honest notes:** JD requirements the resume does not evidence, with a suggestion for each (address in a cover letter, ask the user whether they have unlisted experience, or accept the gap).

**ATS-friendly structure for the resume body:** single column; standard headings (Summary, Skills, Experience, Education, Certifications); reverse-chronological; plain bullets; dates in one consistent format; no tables, text boxes, icons, photos, or content in headers and footers, because many parsers drop or scramble them. Put the target role's keywords in the Skills section and in the experience lines that really demonstrate them.

---

## 2. Rewrite bullets

**Goal:** Turn duty-style lines into achievement statements a hiring manager can picture.

**Inputs:** Resume, target role (ask for it if absent).

**Method:** Structure each line as Action → Task → Result → Business impact, compressed into one or two lines: *strong verb + what and scope + how (tools, approach) + measurable result + why it mattered to the business*. Drop the pieces the resume cannot support rather than filling them with plausible-sounding guesses.

**Output per bullet:**

- **Before:** the original, quoted
- **After:** the rewrite
- **Status:** one of `Supported` (every claim is in the resume), `Inferred, confirm` (reasonable reading, user must verify), or `Needs metric` (the strongest version requires a number the user has not given)
- **Question for you:** only when status is `Needs metric`; one specific question, e.g. "How many requests per day did the service handle?"

Start with the two most recent roles and the bullets closest to the target role; older or irrelevant roles can be shortened rather than rewritten. Keep tools and technologies exactly as the user named them.

---

## 3. Keyword placement map

**Goal:** Show exactly where each missing JD keyword can be worked into the resume honestly.

**Inputs:** Resume and JD.

**Where the gap list comes from:** if the recruiter-lens skill is available, take its gap-analysis findings (what is present, what is missing, how heavily the JD weighs each) as the starting lists. Standalone, build the three lists yourself, as below. This mode's own contribution is the placement map.

**Output:**

1. **Keywords already present:** each with where it appears.
2. **Important keywords missing:** ordered by how heavily the JD stresses them.
3. **Keywords that should be naturally added:** the subset the user's experience supports. Anything the user cannot honestly claim goes to a short **Genuine gaps (do not add)** list.
4. **Placement map:**

| Keyword | Where to add | Draft wording | Evidence status |
|---|---|---|---|

*Evidence status* is `In resume already (implied)`, `Confirm with user`, or `Gap`. Draft wording must be a complete, true sentence or a clause inside an existing bullet, never a bare list of terms.

Check literal-match variants: spelled-out and acronym forms ("Continuous Integration/Continuous Deployment (CI/CD)"), singular and plural, and the JD's exact wording over a synonym the user prefers. If the user has a GitHub handle and the role is technical, repo topics from the MCP server (see `github-mcp.md`) can reveal skills the user has but never wrote down; treat them as prompts to ask about, since a topic tag is not proof of skill.

---

## 4. Summaries

**Goal:** Give the user five distinct options for the top of the resume, each specific to this JD.

**Inputs:** Resume and JD.

**Output:** Five summaries of three to four sentences each. Give each a short label for its angle, for example *Technical depth*, *Delivery and impact*, *Domain fit*, *Ownership and leadership*, *Career-change bridge*, and choose angles that fit the user's real strengths. Each summary covers experience (title and years), the strongest skills that match the JD, one proof point taken from the resume, and the value the user would bring to this team.

Write without first-person pronouns, which is the resume convention. Avoid the filler phrases listed in SKILL.md. Finish by recommending one version and saying why in a sentence.

---

## 5. LinkedIn rewrite

**Goal:** Write the profile so it is findable in recruiter searches and believable to the human who opens it.

**Inputs:** Resume, target role.

**Where the audit lives:** auditing an existing profile (what is weak, what is missing) is recruiter-lens's linkedin-audit. When it is available and the user has a profile to audit, take its findings as the brief for this rewrite. This mode writes; it does not audit.

**Output:**

- **Headline:** three options, each under 220 characters, with the role and the searchable terms first, and a differentiator after.
- **About:** the first two or three lines carry the weight because LinkedIn truncates after that; open with something concrete about the user's work, not an adjective. First person is normal here. Close with what they are looking for or how to reach them.
- **Experience:** per role, a two to three line context sentence plus a few bullets, consistent with the resume. Titles, employers, and dates must match the resume exactly, because mismatches are a screening red flag.
- **Skills:** an ordered list of about 15 to 30, with the three to pin first. Order by what the target role searches for, and drop skills the user cannot back up.
- **Profile extras (when relevant):** Featured section suggestions (the best repo, article, or project), and a clean custom URL. For technical roles with a GitHub handle, the MCP server's profile facts can show whether the headline and the GitHub bio tell the same story.

Voice: write it so it sounds like this particular person. Use contractions where natural, vary sentence length, and avoid hype words, since recruiters read many AI-written profiles and distrust them.

---

## 6. Interview answer pack

**Goal:** Prepare the user's answers to the twenty questions this resume and this JD are most likely to produce.

**Inputs:** Resume and JD.

**Where the questions come from:** predicting what will be asked is recruiter-lens's predict-questions. When it is available, start from its list. Standalone, generate the twenty yourself. Either way, this mode's contribution is the answer material for each question.

**Question mix (adjust to the role):** about 5 role and technical, 4 behavioral, 3 probing the resume's weak spots (short stints, gaps, missing JD requirements), 3 deep-dives into specific projects, 3 motivation, fit, or situational, and 2 logistics (availability, compensation, notice period).

**For every question give:**

1. **What the interviewer is actually testing**
2. **Answer structure**, such as STAR, claim-evidence-tradeoff, or situation-approach-result, whichever fits the question type
3. **Sample answer** of roughly 80 to 120 words in spoken voice, built only from the resume. When the resume offers no material for the question, write `Story needed:` followed by what to dig up, instead of making one up
4. **Common mistake to avoid**

For a long set, deliver ten questions at a time, or offer to save the whole set as a file. For technical roles, the MCP server's repo facts for the two or three repos the resume cites can predict project deep-dive questions, including the uncomfortable ones (no tests, thin README, sparse commit history).

---

## 7. Judge it (hand-off)

**This is a router.** Questions of the form "what is wrong with this resume", "will it pass an ATS", "why am I not getting interviews", or "give me the recruiter's verdict" belong to the recruiter-lens skill. Do the following:

1. If the recruiter-lens skill is available, invoke it for the judging (`scan` for the 6-second impression, `critique` for the full review, `ats-check` for parsing, `reject-reasons` for the common rejection triggers) and say in one line that you are handing off. Then offer to apply its findings with modes 1 to 6.
2. If it is not available, say so in one line and run the fallback below.

**Fallback (only when recruiter-lens is not available):** a short document-level read, not a replacement for a full critique.

- **Verdict:** Interview, Maybe, or No, with two sentences of reasoning.
- **Rubric:** 1 to 100 on ATS compatibility, relevance, achievement strength, clarity, formatting, and keyword alignment, with one sentence of evidence each. Anchor the scale: 90 and up is very hard to improve, 70s are solid with fixable issues, 50s are noticeably weak, below 40 is likely screened out. State that these are judgment-based estimates, not an ATS result.
- **Top five obstacles:** each as Issue, Evidence (quote the line), and Fix. Frame them as potential obstacles, since you cannot know a real rejection reason.
- Then suggest installing recruiter-lens for the full critique.
