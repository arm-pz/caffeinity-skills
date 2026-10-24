# Command-Specific Instructions

## Analysis Commands

### `scan` - 6-Second Resume Scan Simulation

Simulate a recruiter's initial rapid review. Focus on:

**What recruiters look for in 6 seconds:**
1. Current/most recent role and company
2. Job title relevance to target position
3. Education/certifications (if required)
4. Employment timeline continuity
5. Contact information presence
6. Overall formatting cleanliness

**Output format:**
- First impression score (1-5)
- Key info found: [list what's immediately visible]
- Key info missing: [what requires hunting]
- Immediate concerns: [red flags or confusion points]
- Recommendation: proceed/deep-review/reject

**Do not:** Analyze bullet point quality, keyword optimization, or content depth at this stage.

---

### `critique` - Deep Resume Review

Comprehensive evaluation using recruiter priorities:

**Evaluation areas:**
1. **Structure & Flow** - Is information hierarchy logical? Can relevant experience be found quickly?
2. **Impact vs. Responsibilities** - Are achievements quantified or just duties listed?
3. **Relevance Signaling** - Does the resume make it obvious why the candidate fits the target role?
4. **Risk Assessment** - Any unexplained gaps, job-hopping, title inflation, or inconsistencies?
5. **ATS Compatibility** - Formatting that might break parsing (see `ats-check` for details)

**Output format:**
- Overall assessment (strong/competitive/weak/unqualified)
- Top 3 strengths
- Top 3 weaknesses with specific fixes
- Red flag analysis (if any)
- Priority recommendations (max 5)

---

### `ats-check` - ATS Compatibility Verification

Check for technical issues that prevent proper parsing:

**Critical checks:**
- File format: PDF preferred (unless specified otherwise)
- Font usage: Standard fonts only (Arial, Calibri, Times New Roman, Helvetica, Georgia, Verdana)
- Section headers: Clear, standard labels (Experience, Education, Skills)
- Tables/columns: Avoid multi-column layouts that scramble reading order
- Graphics/images: No text embedded in images
- Special characters: Avoid symbols that convert to gibberish (→, •, ✓, ★)
- Headers/footers: Contact info should NOT be in header/footer (many ATS ignore these)
- Page breaks: Ensure no awkward mid-section breaks

**Parsing test indicators:**
- Name appears first and prominently
- Contact info grouped together
- Chronological order is clear
- Company names, titles, dates are easily extractable
- Skills section uses common terminology

**Output format:**
- ATS compatibility score (1-10)
- Critical issues (will cause parse failures)
- Warning issues (may cause confusion)
- Specific fixes for each issue

See `references/ats-specs.md` for detailed technical requirements.

---

### `reject-reasons` - Rejection Trigger Analysis

Identify factors that commonly cause automatic or quick rejections:

**Common rejection triggers:**
1. **Employment gaps >6 months** without explanation
2. **Job-hopping**: 3+ jobs in <2 years without context
3. **Title/seniority mismatch**: Applying for senior role with junior experience
4. **Missing must-haves**: Job description requirements clearly absent from resume
5. **Generic/respray resume**: Obvious mass-application with no tailoring
6. **Poor presentation**: Typos, inconsistent formatting, unprofessional email
7. **Overqualification**: Senior candidate applying for junior role (seen as flight risk)
8. **Location mismatch**: Remote not offered, candidate elsewhere, no relocation mentioned
9. **Salary mismatch**: Compensation expectations far above range (if disclosed)
10. **Industry pivot without bridge**: No transferable skills highlighted

**For each potential trigger found:**
- State the issue clearly
- Assess severity (critical/moderate/minor)
- Provide mitigation strategy (how to address in resume or cover letter)
- Note if context could change the assessment (e.g., gap due to education, caregiving, health)

---

### `linkedin-audit` - LinkedIn Profile Optimization

**Input rule:** This command needs actual profile content (pasted text or a screenshot). If the user provides only a resume, request the profile text or a screenshot; if unavailable, explicitly downgrade to a resume-derived audit and label every finding as inferred, not observed.

Evaluate LinkedIn profile for recruiter discoverability and appeal:

**Key areas:**
1. **Headline**: Beyond current title—includes value proposition or specialization
2. **About section**: Compelling narrative, keywords, clear positioning
3. **Experience descriptions**: Outcome-focused, not just responsibilities
4. **Skills & endorsements**: Relevant skills listed, strategic ordering
5. **Recommendations**: Quality and recency
6. **Activity**: Recent posts, comments, engagement signals
7. **Profile completeness**: Photo, background image, featured section, certifications
8. **SEO optimization**: Keywords in headline, about, experience for recruiter searches

**Output format:**
- Discoverability score (1-10)
- Credibility score (1-10)
- Missing elements checklist
- Quick wins (changes taking <30 minutes)
- Strategic improvements (longer-term optimizations)

---

## Preparation Commands

### `predict-questions` - Interview Question Prediction

Generate likely interview questions based on resume + job description:

**Question categories:**
1. **Resume-based**: Gaps, transitions, specific projects, claimed skills
2. **Role-based**: Technical competencies, scenario questions from JD requirements
3. **Behavioral**: STAR-format questions targeting key competencies
4. **Culture fit**: Work style, values alignment, team dynamics
5. **Weakness probes**: Areas where resume shows limited experience

**Process:**
1. Identify top 5 job requirements from JD
2. Map each requirement to resume evidence (or lack thereof)
3. Generate questions probing both strengths and gaps
4. Include 2-3 curveball questions (unexpected but relevant)

**Output format:**
- Must-prepare questions (top 10)
- Likely questions (next 10)
- Curveball questions (3-5)
- Suggested preparation approach for each category

---

### `gap-analysis` - Experience/Skill Gap Identification

Compare candidate qualifications against job requirements:

**Analysis framework:**
1. Extract all explicit requirements from JD (must-haves vs. nice-to-haves)
2. Map each requirement to resume evidence:
   - **Strong match**: Direct experience, measurable outcomes
   - **Partial match**: Related experience, transferable skills
   - **Weak match**: Tangential exposure, self-taught only
   - **No match**: Completely absent
3. Calculate coverage percentage for must-haves
4. Identify critical gaps (must-haves with no match)

**Output format:**
- Must-have coverage: X%
- Nice-to-have coverage: X%
- Critical gaps: [list with severity]
- Partial matches needing emphasis: [list]
- Transferable skills to highlight: [list]
- Honest assessment: competitive/stretch/unqualified

---

### `tailor` - Tailoring Coverage for a Specific JD

Report how well the current material covers one specific job description and where real experience could legitimately move. This command judges coverage; the applicant-kit skill writes the finished tailored material. If applicant-kit is not installed, recommend concrete placements but keep them as recommendations, not a full rewritten document.

**Tailoring process:**
1. Extract key terminology from JD (tools, methodologies, competencies)
2. Identify priority themes (what the JD emphasizes most)
3. Map coverage: each JD requirement against the candidate's real experience as Full / Partial / Missing
4. Identify repositioning opportunities (which bullets or sections should surface relevant work earlier)
5. Note honest keyword placements (existing true sentences, never stuffed lists)

**Rules:**
- NEVER invent experience or skills not present
- DO use JD terminology to describe existing work
- DO suggest section reordering to surface relevant experience
- DON'T claim proficiency levels beyond actual capability
- DON'T add keywords the experience cannot support; report them as gaps

**Output format:**
- Coverage table (JD requirement → Full/Partial/Missing → supporting line in the material)
- Priority themes and which are uncovered
- Repositioning suggestions (what to move where, and why)
- Honest keyword placements
- Remaining concerns (if any)

To produce the finished tailored document, hand off to the applicant-kit skill (mode 1) when it is installed.

---

### `ai-guidelines` - Authentic AI Usage Rules

Provide guidance on using AI tools ethically in job search:

**Acceptable AI uses:**
- Grammar and spelling correction
- Formatting and structure suggestions
- Keyword optimization against JDs
- Brainstorming impact statement phrasing from real work
- Generating cover letter structure (with personal content filled in)
- Practicing interview responses
- Researching companies/roles

**Unacceptable AI uses:**
- Writing entire resumes with fabricated experiences
- Generating fake projects or achievements
- Creating misleading skill claims
- Automating mass applications without human review
- Having AI answer application questions with invented information
- Using AI to impersonate someone else's voice/experience

**Best practices:**
- Always review and edit AI output for accuracy
- Maintain your authentic voice
- Verify all facts and claims
- Use AI as editor/enhancer, not author
- Be prepared to defend every word in an interview

**Output format:**
- Green light activities (safe to use freely)
- Yellow light activities (use with caution/review)
- Red light activities (avoid entirely)
- Specific examples of acceptable vs. unacceptable use

---

## Optimization Commands

### `format-fix` - Formatting Issue Correction

Fix formatting problems that confuse ATS or annoy recruiters:

**Common fixes:**
- Converting tables to linear text
- Replacing special characters with standard equivalents
- Ensuring consistent date formats
- Fixing inconsistent bullet point styles
- Removing headers/footers with critical info
- Adding clear section headers
- Ensuring proper white space and readability

**Output:** Show exact before/after for each fix needed.

---

### `keyword-match` - JD Keyword Alignment

Align resume terminology with job description keywords:

**Process:**
1. Extract high-value keywords from JD (tools, skills, methodologies)
2. Find natural placement opportunities in resume
3. Rewrite bullet points to incorporate keywords authentically
4. Add missing keywords to skills section (only if candidate has that skill)

**Output:** List of keywords added, where placed, and rewritten examples.

---

### `impact-boost` - Weak Bullet Point Strengthening

Transform responsibility-only bullets into impact statements:

**Formula:** Action verb + Task + Method/Tool + Measurable outcome

**Metrics rule:** The numbers below are illustrative format only. Use metrics the candidate provides; if none exist, ask for a rough sense ("about how many users?") or fall back to the qualitative patterns below. Never emit a precise figure the candidate hasn't supplied or approximated.

**Before:** "Responsible for managing social media accounts"
**After (illustrative — replace with candidate's real numbers):** "Grew Instagram following 40% (2K→2.8K) in 6 months through data-driven content calendar and A/B testing post timing"

**When metrics unavailable:**
- Use scope indicators (team size, budget range, user count)
- Mention improvements qualitatively ("reduced errors," "improved response time")
- Highlight complexity managed

**Output:** Before/after for each weak bullet point with explanation of improvements.

---

### `red-flag-review` - Disqualifier Check

Systematic check for common resume red flags:

**Checklist:**
- Unexplained employment gaps >6 months
- Job-hopping pattern (3+ roles in <2 years)
- Title inflation (VP at 2-person startup)
- Vague company descriptions (can't verify legitimacy)
- Generic objective statement ("seeking challenging opportunity")
- Unprofessional email address
- Typos or grammatical errors
- Inconsistent date formats
- Missing contact information
- Outdated references ("References available upon request")
- Age-revealing details (graduation year >15 years ago for non-senior roles)
- Overly long resume (>2 pages for <10 years experience)

**Output:** Each flag found, severity level, and mitigation strategy.
