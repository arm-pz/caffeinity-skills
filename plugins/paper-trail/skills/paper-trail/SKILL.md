---
name: paper-trail
description: >-
  Drafts the policy pages a small product needs before it takes money or data (privacy policy,
  terms of service, refund policy, cookie notice) from a fact sheet about what the product
  actually collects, stores, shares and charges, then checks the drafts for placeholders,
  missing sections and facts nobody supplied. Use when someone needs a privacy policy, terms,
  refund or cookie page for a site, app, SaaS, newsletter or digital product, asks what legal
  pages they need before launch, or wants existing policy pages checked against what the product
  really does, even if they never say "legal". Not legal advice and not for contracts, NDAs or
  employment documents (use a lawyer), and not for the launch plan itself (use
  solo-income-blueprint) or the site build (use site-prompt).
---

# paper-trail

A privacy policy that says "we never share your data" while the site loads Google Analytics is
worse than no policy: it is a false statement with your name on it. Every line in these pages has
to come from a fact the owner confirmed. This skill gets the facts first, writes only what they
support, and leaves a visible gap where a fact is missing.

These are plain-language drafts for a small product, not legal advice. Say so once in the report,
and say when the facts point to something a lawyer should review (see the escalation list).

## Ground rules

- **Facts before prose.** Fill `references/facts.md` with the owner before drafting. A page
  written from assumptions is the failure this skill exists to prevent.
- **Never invent a fact.** No company name, address, email, processor, retention period, refund
  window or jurisdiction that the owner did not give. Where one is missing, write
  `[NEEDS: <what>]`; the checker fails on it, which is the point.
- **Read the product, not just the owner.** If you can see the site or code, list the third-party
  scripts, forms, cookies and payment providers you find and ask about any the owner did not
  mention. Owners routinely forget analytics, embedded fonts and error trackers.
- **Plain language.** Short sentences, second person, no "heretofore". A user should be able to
  answer "what do you collect and why" from the page in under a minute.
- **One owner per fact.** The company name, contact email and effective date must read the same on
  every page; the checker compares them.

## Workflow

1. **Collect the facts.** Walk the owner through `references/facts.md` in one message (group the
   questions, mark which are required). If you can read the site or repo, pre-fill what you can
   see and mark those entries `(observed)` so the owner confirms rather than recalls.
2. **Pick the pages.** Use the "Which pages" table in `references/pages.md`. Most products need a
   privacy policy and terms; a refund policy once they charge; a cookie notice only when they set
   non-essential cookies.
3. **Check the jurisdiction list.** Open `references/jurisdictions.md` for every place the owner
   operates or has users. Each one adds required sections or rights; add them, and add its
   "verify" note to the report. Never claim compliance with a law; describe what the product does.
4. **Draft each page** from the anatomy in `references/pages.md`, in Markdown, one file per page
   (`privacy.md`, `terms.md`, `refunds.md`, `cookies.md`). Every statement traces to a fact-sheet
   entry. Put `Last updated: <date>` under the title.
5. **Run the checker:**

       python scripts/check_pages.py --facts facts.md privacy.md terms.md refunds.md

   It fails on unfilled placeholders, missing required sections, a missing "Last updated" line,
   and emails, URLs or company names that do not appear in the fact sheet (an invented fact).
   Fix every FAIL; explain every WARN you keep.
6. **Hand on.** The pages go to whoever builds the site (`site-prompt` or `production-code` in W9)
   with the footer links they need, then to `release-gate-chair`, which should see them before a
   launch verdict.

## Escalate to a lawyer

Say plainly that these need professional review, and draft nothing that pretends otherwise, when
the facts include any of: health, biometric, financial-account or children's data; users under
16; selling or sharing personal data for advertising; regulated goods or services (finance,
medical, legal, gambling); a marketplace that takes payments for third parties; or a dispute,
complaint or regulator letter already in hand.

## Report

Lead with the pages written and the checker result (PASS, or each FAIL left and why). Then the
open `[NEEDS: ...]` items the owner must answer, the jurisdiction notes to verify, any escalation
trigger that applied, and the one next action. State once that this is a plain-language draft,
not legal advice.

`references/trigger-cases.md` holds the hand-run trigger cases; open it when tuning this
description.
