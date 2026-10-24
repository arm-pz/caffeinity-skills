# Example: recruiter-lens in action

## User request

```text
/recruiter-lens scan

Senior Software Engineer
TechCorp Inc. | San Francisco, CA
Jan 2022 - Present
→ Responsible for developing web applications
→ Worked with team on various projects
→ Improved application performance
```

## Expected output

```text
## 6-Second Resume Scan Results

**First Impression Score:** 2/5

### Key Info Found Immediately
- Current role and company visible
- Timeline appears continuous

### Key Info Requiring Hunt
- Tech stack buried in prose
- No achievements, only duties

### Immediate Concerns
- Special characters (→) will break ATS parsing
- "Improved application performance" — no scale, no evidence
- "Responsible for..." framing signals zero impact ownership

### Recommendation
REJECT in current form — fix encoding and impact before submitting.
```

## Follow-up: `impact-boost` on one bullet

**Before:** "Improved application performance"

**After (candidate supplied "about 2 seconds down to 1 second"):**
"Reduced typical page response time from ~2s to ~1s by profiling hot paths and adding a caching layer"

**After (candidate supplied nothing):**
"Improved application performance [add magnitude: e.g., typical response time, throughput, or error rate] by [method]"

Note the difference: when the candidate has no numbers, the skill leaves a bracketed
prompt — it never invents "40% (800ms→480ms)" on the candidate's behalf.
