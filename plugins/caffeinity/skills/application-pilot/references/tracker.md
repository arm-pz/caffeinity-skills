# Tracker

One plain file the user owns: `job-applications.csv` (spreadsheet-friendly) or `job-applications.md` (readable in chat). Offer the choice once and keep it; CSV is the default when they want to open it in Excel or Google Sheets.

## Columns

| Column | Meaning | Rules |
|---|---|---|
| `id` | stable row number | never reused |
| `role` | title as posted | keep the employer's wording |
| `employer` | company | one canonical spelling per company |
| `location` | city or Remote | plus region if the posting states one |
| `posted` | date on the page | `unknown` if the page shows none |
| `source` | where it was found | `linkedin`, `indeed`, `ats`, `referral`, `other` |
| `url` | exact posting link | one link; extra links go in `notes` |
| `score` | mode 3 rubric estimate | label as estimate, not ATS |
| `verdict` | `apply` / `apply-with-gaps` / `skip` | mode 3 |
| `status` | machine below | the only field with a fixed vocabulary |
| `applied` | date the user submitted | blank until the user says so |
| `last_touch` | last real interaction | reply, call, message; `unknown` if none |
| `follow_up_due` | `applied` + threshold | recompute from today's actual date |
| `contact` | recruiter or hiring manager | only if named; else `[recruiter name?]` |
| `outcome` | `rejected` / `interview` / `offer` / `no-reply` | with `outcome_date` |
| `notes` | JD line, referral path, second link | free text |

## Status machine

```
discovered -> shortlisted -> ready -> submitted -> acknowledged -> interview -> offer
                              |            |             |             |
                              v            v             v             v
                            skip        no-reply      rejected      rejected
```

`ready` means a packet exists that the user has not yet sent. `submitted` requires the user's confirmation or direct evidence from this session. `acknowledged` is an automated receipt, which is not a response and must not be counted as one in mode 8. Transitions backwards are allowed when the user corrects the record; note the correction rather than quietly rewriting history.

## Dedupe key

`canonical employer + normalised role + location`, compared case-insensitively with tracking parameters stripped from URLs (`utm_*`, `ref`, `fbclid`). The same job on LinkedIn and on the company's own ATS is one row: keep the company ATS link in `url`, put the LinkedIn link in `notes`, and use the earlier of the two dates for `posted`. Near-duplicate titles at one employer (`Backend Engineer III` versus `Senior Backend Engineer`) stay separate rows only if the postings are genuinely separate; otherwise merge and note it.

## Aging rules

- `days_quiet` = today minus `applied`, or minus `last_touch` when a touch happened after applying. Use the real current date from the environment; never assume or round it.
- The threshold comes from the search brief (default 7 days). State it in the queue header.
- One follow-up draft per row by default. A second only if the user asks, and only after twice the threshold.
- Rows with `applied` blank never age. Rows with `posted` unknown can be tracked but are excluded from any "this week" filter.
- Past the second threshold, offer to mark `no-reply` rather than leaving the queue to grow.

## Snapshots

For mode 8, keep counts by reading the current rows; if the user wants trend data, append a dated snapshot line to `job-search-log.md`:

```markdown
2026-10-13 | discovered 41 | shortlisted 12 | submitted 9 | responses 3 | interviews 1
```

Never backfill a snapshot for a week that was not recorded.

## Privacy

The tracker holds personal data and a map of where the user has applied. Keep it in their own workspace, not in a repo they intend to publish, and never commit it. Do not upload it to third-party services on their behalf. If they push the repo publicly, that is their decision with the file listed in `.gitignore` first.
