# Output Format Standards

All metrics in these examples (percentages, times, counts) are illustrative format only — never copy them into a candidate's materials. Use only figures the candidate provides or approximates.

## Resume Scan Output

```markdown
## 6-Second Resume Scan Results

**First Impression Score:** 3/5

### Key Info Found Immediately
- ✓ Name and contact information prominent
- ✓ Current role: Senior Developer at TechCorp
- ✓ Education: BS Computer Science visible
- ✓ Timeline appears continuous

### Key Info Requiring Hunt
- ✗ Specific tech stack buried in paragraph text
- ✗ No clear skills section
- ✗ Achievements mixed with responsibilities

### Immediate Concerns
- Formatting inconsistency in date styles (some "Jan 2020", some "01/2020")
- Email address unprofessional (coder_dude_99@...)

### Recommendation
**Proceed to deep review** - Strong foundation but needs polish before submission
```

---

## Resume Critique Output

```markdown
## Comprehensive Resume Review

**Overall Assessment:** Competitive

### Top 3 Strengths
1. **Strong technical depth** - Clear expertise in Python/Django stack with 5 years focused experience
2. **Quantified impact** - Multiple bullet points include metrics (40% performance improvement, $2M savings)
3. **Logical progression** - Promotions from Junior → Mid → Senior show growth trajectory

### Top 3 Weaknesses
1. **Weak opening summary** - Generic statement doesn't differentiate or target specific role
   - **Fix:** Rewrite to highlight commodity trading domain expertise + AI focus
2. **Missing leadership examples** - Senior role but no team/mentoring mentions
   - **Fix:** Add bullet about code reviews, onboarding juniors, or tech talks given
3. **Skills section disorganized** - 30+ technologies listed alphabetically without prioritization
   - **Fix:** Categorize by proficiency (Expert/Proficient/Familiar) and relevance to target role

### Red Flag Analysis
- **Employment gap (Mar-Aug 2022):** 6 months unexplained between roles
  - **Severity:** Moderate
  - **Mitigation:** Add line explaining sabbatical for upskilling/family/travel with productive activities noted

### Priority Recommendations
1. Rewrite summary to target [specific role/company]
2. Add context for 2022 employment gap
3. Restructure skills section with categories
4. Include 1-2 leadership/mentoring examples
5. Standardize date formatting throughout

**Optional closing offer** (only when the applicant-kit skill is installed or the user asks what to do next): "Want these fixes written into the resume? applicant-kit can do that."
```

---

## ATS Check Output

```markdown
## ATS Compatibility Report

**ATS Compatibility Score:** 7/10

### Critical Issues (Will Cause Parse Failures)
✗ **Contact info in header** - Name/email/phone placed in document header; many ATS ignore headers
  - **Fix:** Move contact info to top of main body text

✗ **Two-column layout** - Skills listed in left sidebar column; reading order will scramble
  - **Fix:** Convert to single-column layout with skills section after experience

### Warning Issues (May Cause Confusion)
⚠️ **Special characters** - Using arrows (→) and checkmarks (✓) in bullet points
  - **Fix:** Replace with standard hyphens (-) or asterisks (*)

⚠️ **Non-standard section header** - "My Professional Journey" instead of "Experience"
  - **Fix:** Change to "Professional Experience" or "Work History"

⚠️ **Inconsistent dates** - Mix of "MM/YYYY" and "Month YYYY" formats
  - **Fix:** Standardize to one format throughout (recommend "MMM YYYY")

### Parsing Test Results
- ✓ Name extracted correctly
- ✗ Email not found (in header)
- ✓ Experience section identified
- ⚠️ Skills section may be missed (sidebar location)
- ✓ Education parsed correctly

### Recommended Actions
1. Move contact info from header to body (HIGH PRIORITY)
2. Convert to single-column layout (HIGH PRIORITY)
3. Replace special characters with standard equivalents
4. Rename section headers to standard labels
5. Standardize date formatting
```

---

## Rejection Reasons Output

```markdown
## Rejection Risk Analysis

### Identified Triggers

**1. Employment Gap (Critical)**
- **Issue:** 8-month gap (Jan-Aug 2023) with no explanation
- **Recruiter interpretation:** Unable to find work? Skills outdated?
- **Mitigation:** Add entry: "Career Break | Skill Development | Jan-Aug 2023" with relevant courses/certifications completed

**2. Job-Hopping Pattern (Moderate)**
- **Issue:** 4 roles in 3 years (2020-2023), all <12 months
- **Recruiter interpretation:** Can't commit, can't pass probation, always looking
- **Mitigation:** If contract work, group under "Independent Consultant" umbrella. If full-time, add context notes explaining departures

**3. Generic Objective (Minor)**
- **Issue:** "Seeking challenging opportunity in dynamic organization"
- **Recruiter interpretation:** Mass-applied without tailoring
- **Mitigation:** Replace with targeted summary mentioning specific company/role/domain

### Overall Risk Level: HIGH
**Recommendation:** Address critical and moderate issues before submitting. Without fixes, likelihood of quick rejection is high.
```

---

## Interview Question Prediction Output

```markdown
## Predicted Interview Questions

Based on your resume and the [Job Title] role at [Company], here are likely questions:

### Must-Prepare Questions (Top 10)

**Resume-Based:**
1. "I see a 6-month gap in 2023. What were you doing during that time?"
2. "You've changed companies 4 times in 3 years. What's driving those moves?"
3. "Your most recent role emphasizes Python, but this role requires Java. How do you bridge that gap?"

**Role-Based:**
4. "Walk me through how you'd design a scalable API for commodity trading data"
5. "How have you handled real-time data processing in previous roles?"
6. "Describe your experience with AWS services, particularly Lambda and S3"

**Behavioral:**
7. "Tell me about a time you disagreed with a technical decision. How did you handle it?"
8. "Describe a project that failed or didn't meet expectations. What did you learn?"
9. "Give an example of when you had to learn a new technology quickly"

**Curveball:**
10. "If you could redesign any system you've worked on, what would you change and why?"

### Preparation Strategy

**For gap/job-hopping questions:**
- Prepare honest, concise explanation (30 seconds max)
- Emphasize what you learned during transitions
- Show pattern is stabilizing (longer recent roles)

**For technical questions:**
- Review distributed systems fundamentals
- Prepare 2-3 detailed project stories using STAR format
- Be ready to whiteboard/code simple algorithms

**For behavioral questions:**
- Prepare 5 versatile stories covering: conflict, failure, success, leadership, learning
- Practice STAR format: Situation, Task, Action, Result
- Quantify results wherever possible
```

---

## LinkedIn Audit Output

```markdown
## LinkedIn Profile Optimization Report

**Discoverability Score:** 6/10
**Credibility Score:** 7/10

### Missing Elements
- ✗ No profile photo (profiles with photos get 21x more views)
- ✗ Background banner image missing
- ✗ Featured section empty (no portfolio/work samples)
- ✗ Only 3 skills listed (optimal: 15-25)
- ✗ No recent activity (last post 8 months ago)

### Quick Wins (<30 minutes)
1. **Add professional headshot** - Well-lit, business casual, neutral background
2. **Customize headline** - Change from "Software Engineer at XYZ" to "Python Developer | Building Scalable Trading Systems | Django + AWS"
3. **Expand About section** - Currently 2 sentences; expand to 3-4 paragraphs telling your story
4. **Add 10+ relevant skills** - Include all technologies from target job descriptions
5. **Request 2-3 recommendations** - Reach out to former managers/colleagues this week

### Strategic Improvements
1. **Publish 1 article/post per month** - Share insights on commodity trading tech, AI applications, etc.
2. **Engage with target companies** - Comment thoughtfully on posts from companies you want to join
3. **Join relevant groups** - Join 5-10 industry groups; participate in discussions
4. **Optimize for search** - Include keywords (Python, Django, AWS, Trading Systems) in headline, about, and experience sections
5. **Add multimedia to experience** - Link GitHub repos, project demos, presentations

### SEO Keywords to Add
- Python, Django, Flask
- AWS, Lambda, S3, EC2
- REST APIs, Microservices
- Commodity Trading, FinTech
- Agile, Scrum

### Priority Action Plan
**This week:** Add photo, update headline, expand About section
**Next 2 weeks:** Add skills, request recommendations, customize URL
**Ongoing:** Post monthly, engage weekly, grow network strategically
```

---

## AI Guidelines Output

```markdown
## AI Usage Guidelines for Job Search

### ✅ Green Light (Safe to Use Freely)

**Grammar and Spelling**
- Tools: Grammarly, LanguageTool, built-in spellcheck
- Example: Running resume through Grammarly to catch typos
- Why safe: Purely mechanical correction, no content invention

**Formatting Suggestions**
- Tools: ResumeWorded, Canva templates, LaTeX templates
- Example: Using template to improve visual hierarchy
- Why safe: Enhances presentation of existing content

**Keyword Optimization**
- Tools: Jobscan.co, manual JD comparison
- Example: Identifying missing keywords from job description and naturally incorporating them
- Why safe: You're highlighting real skills, not inventing them

**Structure Feedback**
- Tools: ChatGPT/Claude asking "Is this resume well-organized?"
- Example: Getting suggestions on section ordering
- Why safe: Advisory only, you control final content

---

### ⚠️ Yellow Light (Use with Caution/Review)

**Bullet Point Rewriting**
- Tools: ChatGPT, Claude, specialized resume tools
- Example: "Make this bullet point stronger"
- **Caution:** Ensure AI doesn't exaggerate or invent metrics
- **Required review:** Verify all facts, numbers, and claims remain accurate

**Cover Letter Drafting**
- Tools: ChatGPT with your background info
- Example: "Draft a cover letter for [role] emphasizing [skills]"
- **Caution:** AI voice often sounds generic/impersonal
- **Required review:** Rewrite in your authentic voice, add specific company research

**Interview Question Prep**
- Tools: ChatGPT simulating interviewer
- Example: "Ask me questions for a senior developer role"
- **Caution:** Don't memorize scripted answers
- **Required review:** Use as practice, but prepare authentic personal stories

**LinkedIn Summary Writing**
- Tools: AI writing assistants
- Example: "Help me write a compelling LinkedIn About section"
- **Caution:** Avoid buzzword-heavy, soulless language
- **Required review:** Ensure it sounds like you, not a corporate robot

---

### ❌ Red Light (Avoid Entirely)

**Fabricating Experiences**
- Example: "Add a project where I led a team of 10"
- Why dangerous: Will be exposed in interview, destroys credibility permanently
- Alternative: Highlight actual leadership experiences, even if smaller scale

**Generating Fake Metrics**
- Example: "Make my achievements sound more impressive with numbers"
- Why dangerous: Specific claims will be probed in interview
- Alternative: Use scope indicators (team size, user count) if exact metrics unavailable

**Automated Mass Applications**
- Example: Bot applying to 500 jobs with your resume
- Why dangerous: No quality control, may submit to wrong roles, can't track submissions
- Alternative: Apply to fewer roles with higher quality tailoring

**Having AI Answer Application Questions**
- Example: "Why do you want to work here?" answered by ChatGPT
- Why dangerous: Generic answers obvious to recruiters, may contain factual errors
- Alternative: Use AI to brainstorm angles, then write authentic response yourself

**Impersonating Someone Else**
- Example: AI writing resume for different person/background
- Why dangerous: Fundamental dishonesty, will collapse under scrutiny
- Alternative: Present your genuine self authentically

---

## Best Practices Summary

1. **AI as Editor, Not Author** - You write first draft, AI suggests improvements
2. **Verify Everything** - Never accept AI output without fact-checking
3. **Maintain Your Voice** - Read output aloud; if it doesn't sound like you, rewrite
4. **Stay Defensible** - Every claim should be something you can discuss confidently in interview
5. **Quality Over Speed** - Don't use AI to apply faster; use it to apply better

### Golden Rule
**If you wouldn't say it confidently in an interview while looking the hiring manager in the eye, don't put it in your application.**
```

---

## Gap Analysis Output

```markdown
## Experience Gap Analysis

**Target Role:** Senior Backend Engineer at [Company]

### Must-Have Requirements Coverage

| Requirement | Your Status | Match Level | Notes |
|-------------|-------------|-------------|-------|
| 5+ years Python | 4 years | Partial | Close; emphasize depth over breadth |
| Django/Flask | Django 3 years | Strong | Direct match |
| AWS (Lambda, S3) | Used S3 only | Partial | Need to highlight S3 projects prominently |
| Microservices architecture | 2 projects | Strong | Can discuss in detail |
| SQL + NoSQL | PostgreSQL only | Partial | Missing MongoDB/Redis experience |
| Team leadership | Mentored 2 interns | Weak | Limited formal leadership |
| CI/CD pipelines | Jenkins experience | Strong | Direct match |

**Must-Have Coverage:** 57% (4/7 strong/partial)

### Nice-to-Have Coverage

| Requirement | Your Status | Match Level |
|-------------|-------------|-------------|
| Kubernetes | None | No match |
| GraphQL | Self-studied | Weak |
| React basics | Personal projects | Partial |
| Agile/Scrum | 2 years experience | Strong |

**Nice-to-Have Coverage:** 50% (2/4 partial or better)

### Critical Gaps
1. **No NoSQL database experience** - Job requires MongoDB or Redis
   - **Severity:** High
   - **Mitigation:** Complete MongoDB University course this week; build small project demonstrating CRUD operations

2. **Limited leadership experience** - Role expects team lead capabilities
   - **Severity:** Moderate
   - **Mitigation:** Emphasize mentoring of interns, code review responsibilities, tech talk presentations

### Partial Matches Needing Emphasis
1. **AWS experience** - Currently buried in resume; move to prominent position
2. **Years of Python** - 4 years vs. 5 required; frame as "nearly 5 years" and emphasize project complexity

### Transferable Skills to Highlight
- **PostgreSQL → NoSQL transition:** Emphasize understanding of database fundamentals; learning new DB type is straightforward
- **Jenkins CI/CD → Broader DevOps:** Shows understanding of deployment pipelines; can extend to other tools
- **Intern mentoring → Leadership:** Demonstrates teaching ability, patience, code quality focus

### Honest Assessment
**Verdict:** Stretch candidate but competitive with preparation

**Recommended actions before applying:**
1. Complete MongoDB crash course (4-6 hours)
2. Build small demo app using MongoDB + deploy to AWS
3. Rewrite resume to emphasize AWS and leadership examples
4. Prepare to discuss database learning agility in interview

**Timeline:** Can be ready to apply in 1-2 weeks with focused prep
```

---

## Tailoring Output

Default template for `tailor` — coverage judgment only; the applicant-kit skill writes finished material:

```markdown
## Tailoring Coverage for [Specific Role]

**Target:** Senior Backend Engineer at Caffeinity

### Coverage
| JD requirement | Status | Supporting line in the material |
|---|---|---|
| Python/Django | Full | "Designed and deployed 3 microservices … Django REST Framework" |
| AWS | Partial | "AWS Lambda" appears once; deployment ownership not shown |
| NoSQL | Missing | no Mongo/DynamoDB experience visible |

### Priority Themes
- Which themes the JD stresses most, and whether the material covers them

### Repositioning Suggestions
- What to move where (e.g. promote the trading-systems bullet to first in the most recent role) and why

### Honest Keyword Placements
- Keyword → the true sentence or section it belongs in; nothing the experience cannot support

### Remaining Concerns
- Gaps that cannot be closed by rewording

Finished-tailored-document work (rewritten summary, new bullets, cover letter) goes to the applicant-kit skill, mode 1, when it is installed.
```

**Full-rewrite format** — use only when applicant-kit is not installed and the user asks for the rewrite itself. Same never-invent rule: all figures must come from the candidate, the numbers below are illustrative format only.

```markdown
## Application Tailoring for [Specific Role]

**Target:** Senior Backend Engineer at Caffeinity

### Revised Summary

**Before:**
"Experienced software engineer with expertise in Python and web development. Seeking challenging opportunity to contribute to innovative team."

**After:**
"Backend engineer with 4 years building scalable trading systems using Python/Django. Passionate about leveraging AI to optimize commodity trading workflows. Excited to bring API design expertise and AWS deployment experience to Caffeinity's Dubai-based engineering team."

### Rewritten Bullet Points

**Bullet 1 - Performance Optimization:**

Before:
"Improved application performance"

After:
"Reduced API response time 40% (800ms→480ms) by implementing Redis caching layer and optimizing database queries, directly improving trader user experience"

**Why better:** Specific metric, named technology, business impact clear

**Bullet 2 - System Design:**

Before:
"Built microservices for trading platform"

After:
"Designed and deployed 3 microservices (order management, pricing engine, notification service) handling 10K+ daily transactions using Django REST Framework and AWS Lambda"

**Why better:** Quantifies scope, names specific services, shows scale

**Bullet 3 - Collaboration:**

Before:
"Worked with team on projects"

After:
"Collaborated with 5-person agile team using Scrum methodology; conducted weekly code reviews and mentored 2 junior developers on Python best practices"

**Why better:** Shows team size, methodology, leadership behaviors

### Suggested Section Reordering

**Current order:**
1. Education
2. Skills
3. Experience
4. Projects

**Recommended order:**
1. Summary (new tailored version)
2. Technical Skills (reordered to highlight Python/Django/AWS first)
3. Professional Experience (with rewritten bullets)
4. Projects (emphasizing trading/finance-related work)
5. Education (move down; experience is stronger signal)

### Keywords Added Naturally
- "Commodity trading" (in summary)
- "API design" (in experience)
- "AWS Lambda" (specific service named)
- "Agile/Scrum" (methodology mentioned)
- "Code review" (leadership signal)
- "Mentoring" (leadership signal)

### Remaining Concerns
- Still short on total years (4 vs. 5 requested)
- No direct NoSQL experience yet (planning MongoDB course)
- Limited formal leadership title (mitigated by mentoring examples)

### Next Steps
1. Complete MongoDB tutorial before submitting
2. Add small MongoDB project to GitHub
3. Update LinkedIn to mirror resume changes
4. Write brief cover letter connecting trading background to Caffeinity's mission
```
