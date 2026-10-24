# ATS (Applicant Tracking System) Technical Specifications

> **As of:** October 2026. Platform parsing behavior changes with vendor updates — re-verify against current vendor docs or a fresh parse test before relying on specific claims below.

## How ATS Systems Work

ATS platforms parse resumes into structured database fields before any human sees them. Understanding this process is critical for resume optimization.

### Major ATS Platforms

1. **Workday** - Enterprise-focused, strict parsing rules
2. **Greenhouse** - Startup/tech favorite, moderate flexibility
3. **Lever** - Tech/modern companies, good with creative formats
4. **iCIMS** - Large enterprise, older parsing engine
5. **Taleo (Oracle)** - Corporate/legacy, very strict formatting requirements
6. **SuccessFactors (SAP)** - Enterprise, moderate parsing ability
7. **BambooHR** - SMB market, simpler parsing
8. **JazzHR** - Mid-market, decent format handling

## Critical Formatting Rules

### File Format

**Preferred:** PDF (unless job posting specifies .docx)

**Why PDF:**
- Preserves formatting across systems
- Most modern ATS handle PDF well
- Prevents accidental reformatting

**When to use .docx:**
- Job posting explicitly requests it
- Older ATS systems (pre-2018) may prefer it
- Some government/academic systems require it

**Never use:**
- .pages (Apple-only, won't parse)
- .txt (loses all formatting)
- Image-based PDFs (can't extract text)
- .rtf (inconsistent rendering)

### Font Requirements

**Safe fonts (universally recognized):**
- Arial
- Calibri
- Times New Roman
- Helvetica
- Georgia
- Verdana
- Tahoma
- Trebuchet MS

**Avoid:**
- Custom/downloaded fonts
- Script or decorative fonts
- Symbol fonts (Wingdings, Webdings)
- Fonts with special ligatures

**Font size:**
- Body text: 10-12pt
- Headers: 14-16pt
- Name: 18-24pt

### Section Headers

**Use standard labels:**
- Experience / Work Experience / Professional Experience
- Education / Academic Background
- Skills / Technical Skills / Core Competencies
- Summary / Professional Summary / About
- Certifications / Licenses

**Avoid creative headers:**
- "My Journey" (use Experience)
- "What I Bring" (use Skills)
- "Knowledge Base" (use Skills)
- "Where I've Been" (use Experience)

**Why:** ATS maps sections to database fields using header recognition. Non-standard headers may be skipped entirely.

### Layout Structure

**Single-column layout:**
- Most ATS read left-to-right, top-to-bottom
- Multi-column layouts scramble reading order
- Tables create parsing confusion

**Chronological order:**
- Reverse chronological (newest first) is standard
- Be consistent throughout
- Use clear date formatting

**White space:**
- Adequate spacing improves readability
- Don't cram content to save space
- Minimum 0.5 inch margins

### Date Formatting

**Recommended formats:**
- MM/YYYY (03/2020)
- Month YYYY (March 2020)
- YYYY-MM (2020-03)

**Avoid:**
- Relative dates ("3 years ago")
- Season references ("Spring 2020")
- Inconsistent formats within same resume

**For current roles:**
- Use "Present" or "Current" (not "Now" or "Today")

## Content That Breaks Parsing

### Special Characters

**Problematic characters:**
- Arrows: →, ←, ↑, ↓
- Bullets: •, ◦, ▪ (use hyphen - or asterisk * instead)
- Checkmarks: ✓, ✔
- Stars: ★, ☆
- Emojis: Any emoji
- Math symbols: ≠, ≤, ≥, ±
- Currency symbols other than $: €, £, ¥

**Safe alternatives:**
- Use hyphens (-) or asterisks (*) for bullets
- Use ">" for arrows
- Spell out symbols when needed

### Graphics and Images

**Never include:**
- Text embedded in images/logos
- Infographics showing skills/experience
- Photo/headshot (unless specifically requested)
- Charts/graphs showing metrics
- Icons representing skills

**Why:** ATS cannot extract text from images. Information becomes invisible.

### Tables and Text Boxes

**Avoid:**
- Multi-column tables
- Text boxes for content
- Sidebars with important info
- Floating elements

**Why:** Many ATS read tables row-by-row, scrambling the intended structure. Text boxes may be ignored entirely.

### Headers and Footers

**Critical rule:** Do NOT place contact information in header/footer

**Why:** Many ATS systems ignore headers and footers completely, losing your name, email, and phone.

**Instead:** Place contact info at top of main document body.

## Keyword Optimization for ATS

### How ATS Keyword Matching Works

Most ATS rank candidates by keyword match percentage against the job description.

**High-value keywords:**
- Specific tools/technologies named in JD
- Required certifications
- Industry terminology
- Methodologies/frameworks
- Job titles/roles

**Keyword placement priority:**
1. Skills section (highest weight)
2. Job title/current role
3. Bullet points describing work
4. Summary/objective
5. Education/certifications

### Keyword Density

**Optimal range:** 2-4% keyword density

**Too low:** May not register as qualified
**Too high:** Triggers spam filters, looks unnatural

**Natural integration:**
- Mention key tools in context of actual work
- Include in project descriptions
- List in skills section
- Reference in achievement statements

### Synonym Handling

Modern ATS use synonym databases, but don't rely on this:

**Example:**
- JD says "project management"
- Resume says "program coordination"
- ATS may or may not match these

**Best practice:** Use exact terminology from JD when accurate.

## Contact Information Parsing

### Required Fields

Ensure these are easily extractable:

1. **Full name** - First line of resume
2. **Email address** - Standard format, professional domain
3. **Phone number** - Include country code if international
4. **Location** - City, State/Country (full address not needed)
5. **LinkedIn URL** - Optional but recommended

### Email Address Best Practices

**Professional format:**
- firstname.lastname@gmail.com
- firstinitiallastname@gmail.com
- firstname_lastname@domain.com

**Avoid:**
- Unprofessional usernames (partyanimal99@...)
- Current work email (looks disloyal)
- Obscure domains that look like spam

### Phone Number Format

**Standard formats:**
- (555) 123-4567
- 555-123-4567
- +1-555-123-4567 (international)

**Avoid:**
- Extensions without main number
- Virtual numbers that expire
- Only providing WhatsApp/Skype

## Skills Section Optimization

### Structure for ATS

**Format options:**

Option 1 - Categorized:
```
Technical Skills:
- Languages: Python, JavaScript, SQL
- Frameworks: React, Django, Flask
- Tools: Git, Docker, AWS
```

Option 2 - Simple list:
```
Skills: Python, JavaScript, React, Django, SQL, Git, Docker, AWS, Project Management, Agile
```

**Why categorization helps:**
- Easier for humans to scan
- Shows depth in specific areas
- Groups related technologies

### Skill Naming Conventions

**Use industry-standard names:**
- "JavaScript" not "JS" (unless both mentioned)
- "Amazon Web Services (AWS)" first time, then "AWS"
- "Microsoft Excel" not just "Excel"

**Include variations:**
- "React.js (React)"
- "Node.js (Node)"
- Helps catch different JD phrasings

### Proficiency Levels

**If including proficiency:**
- Use simple terms: Beginner, Intermediate, Advanced, Expert
- Avoid: 4/5 stars, visual bars, percentage ratings

**Better approach:**
- Don't rate skills
- Let experience bullet points demonstrate level
- Or separate into "Proficient in:" vs "Familiar with:"

## Common ATS Parsing Errors

### Error 1: Name Misidentification

**Symptom:** ATS extracts wrong text as candidate name

**Causes:**
- Name not on first line
- Name in header/footer
- Multiple names close together (co-authoring?)

**Fix:** Ensure name is prominent, first line, largest font

### Error 2: Date Confusion

**Symptom:** Employment dates parsed incorrectly or missing

**Causes:**
- Inconsistent date formats
- Dates in tables
- Overlapping date ranges unclear

**Fix:** Use consistent MM/YYYY format, clear start/end labels

### Error 3: Company/Title Swap

**Symptom:** Company name parsed as job title or vice versa

**Causes:**
- Unclear hierarchy in experience entries
- Missing labels
- Unusual formatting

**Fix:** Use clear structure:
```
Job Title
Company Name | Location | Dates
- Achievement 1
- Achievement 2
```

### Error 4: Skills Section Ignored

**Symptom:** Skills not extracted into skills database field

**Causes:**
- Non-standard section header
- Skills embedded only in paragraphs
- Visual skill bars/charts instead of text

**Fix:** Use "Skills" or "Technical Skills" header, list as text

### Error 5: Contact Info Lost

**Symptom:** Email/phone not found by ATS

**Causes:**
- Info in header/footer
- Info in side column
- Unusual formatting or symbols

**Fix:** Top of main body, standard format, clear labels

## Testing ATS Compatibility

### Manual Checks

1. **Copy-paste test:** Copy entire resume into plain text editor. Does content appear in logical order?

2. **Readability test:** Can you quickly find name, current role, contact info?

3. **Keyword search:** Search for key terms from target JD. Are they present?

4. **Length check:** Is resume appropriate length for experience level?

### Online Tools

Several free ATS simulators exist:
- Jobscan.co (free tier)
- ResumeWorded.com
- SkillSyncer.com

**Note:** These are approximations. Actual ATS behavior varies by configuration.

## Mobile vs. Desktop ATS

### Consideration

Some recruiters review resumes on mobile devices through ATS apps.

**Mobile-friendly practices:**
- Single column layout
- Adequate font size (11pt minimum)
- Clear section breaks
- Short bullet points (2 lines max on mobile)

## Accessibility and ATS

### Screen Reader Compatibility

While not strictly ATS-related, accessible resumes also tend to parse better:

- Use semantic headings
- Provide alt text for any necessary graphics
- Maintain logical reading order
- Use sufficient color contrast (if using color)

## Industry-Specific ATS Variations

### Tech Companies

**Typically use:** Greenhouse, Lever, Workday

**Parsing strengths:**
- Good with technical terminology
- Handle GitHub/portfolio links
- Recognize programming languages

**Watch out for:**
- Automated coding challenge triggers
- Degree requirement filters (can exclude self-taught)

### Enterprise/Corporate

**Typically use:** Taleo, SuccessFactors, iCIMS

**Parsing characteristics:**
- Very strict formatting requirements
- Strong emphasis on education/credentials
- May filter by years of experience automatically

**Watch out for:**
- Knockout questions (yes/no filters)
- Rigid field mapping

### Startups/SMBs

**Typically use:** BambooHR, JazzHR, Breezy HR

**Parsing characteristics:**
- More flexible formatting
- Human review happens sooner
- Less automated filtering

**Watch out for:**
- May still have basic keyword matching
- Often value culture fit indicators

## Red Flags for ATS Filters

### Automatic Rejection Triggers

Some ATS configurations auto-reject based on:

1. **Missing required fields** - No email, no phone, no location
2. **File issues** - Corrupted file, wrong format, password protected
3. **Keyword threshold** - <50% match on must-have skills
4. **Experience range** - Years outside specified range
5. **Location mismatch** - No relocation mentioned for on-site role
6. **Duplicate application** - Same candidate applied recently

### Work Authorization Filters

Many ATS ask: "Are you authorized to work in [country]?"

**Impact:**
- "No" often triggers automatic rejection
- Sponsorship requirements may filter out candidates
- Be honest but strategic in answering

## Best Practices Summary

### Do:
- Use single-column, clean layout
- Stick to standard fonts and headers
- Include keywords from job description naturally
- Save as PDF (unless told otherwise)
- Keep contact info in main body
- Use consistent date formatting
- Quantify achievements with numbers

### Don't:
- Use tables, text boxes, or multi-column layouts
- Embed text in images or graphics
- Place critical info in headers/footers
- Use special characters or symbols extensively
- Create overly creative section headers
- Submit files >2MB (may be rejected)
- Password-protect your resume

## Version Control for ATS

### Strategy

Maintain multiple resume versions optimized for different role types:

1. **Master resume** - Complete history, all skills
2. **Tech-focused version** - Emphasizes technical skills
3. **Leadership version** - Highlights management experience
4. **Industry-specific version** - Tailored to particular sector

**Benefits:**
- Quick tailoring for applications
- Consistent branding per role type
- Easier to track what's been submitted where
