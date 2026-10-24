# Trigger cases for paper-trail

Written to tune-skill's case format (`references/test-cases.md` in arm-pz/tune-skill). Judged from
the `description` frontmatter only. Competing descriptions read: `solo-income-blueprint`,
`site-prompt`, `production-code`, `release-gate-chair`, `web-preflight`, `wordsmith`.

**Run:** hand-run on 2026-10-24 against the descriptions only. No automated triggering loop was run.

| # | Message | Expected skill | Pass condition | Result |
| --- | --- | --- | --- | --- |
| 1 | "I need a privacy policy for my newsletter signup page." | paper-trail | asks for the fact sheet before drafting | PASS ("privacy policy ... newsletter") |
| 2 | "What legal pages do I need before I start charging on Gumroad?" | paper-trail | picks pages from the table, includes refunds | PASS ("what legal pages they need before launch") |
| 3 | "Check my terms page against what the app actually does." | paper-trail | reads the product, runs check_pages.py | PASS ("existing policy pages checked") |
| 4 | "Write a refund policy for my course." | paper-trail | refunds.md with statutory exceptions noted | PASS |
| 5 | "Do I need a cookie banner? I use Plausible." | paper-trail | cookie notice only if non-essential cookies | PASS ("cookie ... page") |
| 6 | "Draft an NDA for my contractor." | none (lawyer) | paper-trail does not load | PASS ("not for contracts, NDAs") |
| 7 | "How do I make money from my design skills?" | solo-income-blueprint | paper-trail does not load | PASS |
| 8 | "Build me a landing page with a footer." | site-prompt | paper-trail does not load; footer links come later | PASS |
| 9 | "Is my site safe to launch?" | release-gate-chair | paper-trail does not load | PASS (the chair should ask whether the pages exist) |

## Boundary pairs

| Message | Should trigger | Why |
| --- | --- | --- |
| "Write my privacy policy." | paper-trail | the page itself |
| "Write the homepage copy." | wordsmith | marketing copy, not policy |
| "Terms of service for my SaaS." | paper-trail | user-facing terms |
| "A services agreement for an enterprise client." | none | a negotiated contract needs a lawyer |
