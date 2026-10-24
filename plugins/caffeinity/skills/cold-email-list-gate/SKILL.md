---
name: cold-email-list-gate
description: >-
  Gate a cold-email lead list before it loads: sample ten rows, check company, title,
  size, and mailbox against the ICP, compare data providers on the same criteria, and
  return a GO or HOLD decision with the fail pattern and the re-run condition. Use when
  someone wants a list QA'd, checked, sampled, or approved before a send, asks whether
  a list is clean or safe to load, or is choosing between data providers for one
  filter set. Not for buying, scraping, or enriching contacts (out of scope), writing
  the email copy (wordsmith), or diagnosing a list that already sent (cold-email-ops).
---

# Cold email list gate

The list breaks before deliverability does. A bad filter reaches 20,000 inboxes before anyone notices; ten rows read before load catch it while the fix is still one query change.

## Confirm the job

- You need three inputs: the list (rows or CSV), the ICP definition, and the query or provider that built it.
- No ICP definition means fit cannot be judged. Check mailbox validity only, return INCONCLUSIVE, and ask for the missing definition rather than guessing.
- Sends already happened → hand the case to `cold-email-ops` for an audit. This skill gates before load only.
- Buying, scraping, or enriching contacts → out of scope. Stop and say so.

## Gate the list

1. Sample 10 rows at random before the full list loads. Read each as a prospect: right company, right title, right size, real mailbox. Record the row itself, not a summary.
2. Two or more wrong in ten → HOLD. Fix the query or provider; do not patch individual rows, because patching hides the bad filter.
3. One wrong in ten → GO with the row named in the report. Zero or one is tolerable; two is a pattern.
4. Re-run a fresh 10-row sample after the fix. A HOLD is never lifted on the old sample.
5. Name the common fail pattern: wrong filter, stale source, wrong seniority, invalid mailboxes. The pattern tells the owner what to change.

## Compare providers when that is the question

- Same criteria, 50–100 contacts per provider, not the full list.
- Email: valid-contact rate. Phone: dials to reach one in-profile person.
- Attribute differences to the provider, not to copy or infrastructure. The same criteria can move valid contacts sharply across providers.

## Decide and report

Use the template in `references/gate-rules.md`. The first line is GO or HOLD. Include the 10-row table (#, company, title, size fit, mailbox valid, note), the fail pattern and its cause, and the specific change that triggers a fresh sample. Never invent rows. If the list has fewer than 10 rows, sample all of them and mark the gate INCONCLUSIVE.

## Boundaries

- Copy writing or rewriting → `wordsmith`.
- Post-send diagnosis, capacity, deliverability, or automation → `cold-email-ops`.
- Acquisition, enrichment, and sending → out of scope.
