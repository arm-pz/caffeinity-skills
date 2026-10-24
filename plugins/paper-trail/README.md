# paper-trail

Drafts the policy pages a small product needs before it takes money or data (privacy policy,
terms of service, refund policy, cookie notice) from a fact sheet the owner confirms, then checks
them with `scripts/check_pages.py`: unfilled placeholders, missing required sections, a missing
"Last updated" line, and emails or links the fact sheet does not contain all get flagged.

Step 4 of workflow W9 (launch a one-person product) in `caffeinity-routing`. Plain-language
drafts, not legal advice; the skill says when a lawyer should review.

```
/plugin marketplace add arm-pz/caffeinity-skills
/plugin install paper-trail@caffeinity-skills
```

Self-check: `python -I tests/test_check_pages.py`
