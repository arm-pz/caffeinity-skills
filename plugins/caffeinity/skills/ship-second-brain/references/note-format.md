# Note format

Open this when writing a note in Pass 2, or when `check_vault.py` reports a front-matter FAIL.

## Raw file (`raw/`)

```markdown
---
date: 2026-11-06
origin: github-pr
url: https://github.com/acme/api/pull/412
---

<the source text, copied as-is>
```

File name: `YYYY-MM-DD-<origin>-<id>.md`, for example `2026-11-06-github-pr-412.md`. Raw files are never edited after they are saved. A newer version of the same source is a new file.

## Note

```markdown
---
date: 2026-11-06
source: raw/2026-11-06-github-pr-412.md
owner: "@dana"
confidence: verified
---

# Retries use exponential backoff, capped at 30 seconds

> Retries now back off exponentially, with a hard cap of 30s.

The cap exists so a stuck dependency cannot hold a worker for minutes. ([raw](raw/2026-11-06-github-pr-412.md))

Opinion: the cap may be too low for the batch exporter.

Supports [[retry-policy-decision]]. Contradicts [[exporter-waits-indefinitely]].
```

### Fields

| Field | Required | Value |
| --- | --- | --- |
| `date` | yes | The date of the source, `YYYY-MM-DD`, not the date of ingestion |
| `source` | yes | Path to the raw file, relative to the vault root. Several sources: a YAML list |
| `owner` | yes | The person or team who owns the idea (the PR author, the decision maker). `unknown` if the source does not say |
| `confidence` | yes | `seen`, `verified` or `opinion` |

### Confidence

- **seen**: read in the source but not yet checked word for word. The default for new notes.
- **verified**: the `> ` quote lines were confirmed against the raw source in Pass 4. A verified note needs at least one `> ` quote; that is what the check script compares.
- **opinion**: no source supports it. Allowed, but labelled, and never cited as fact in an answer.

Confidence only goes up with the source open. It goes down whenever a quote stops matching.

### Body

- One `#` heading that states the idea as a sentence.
- Claims from the source are quoted with `> ` or followed by a link to the raw file.
- Any line that is not sourced starts with `Opinion:`.
- At least one `[[link]]` to another note, with the relation in words: supports, contradicts, answers.
- Short. If it needs scrolling, split it.

## today.md

```markdown
# 2026-11-06

Shipped: retry backoff ([[retry-uses-exponential-backoff]])
Linked: 4 new notes, 1 to inbox
Downgraded: [[exporter-timeout-is-60s]] (quote not in source)
Re-read:
- [[retry-policy-decision]]
- [[auth-tokens-rotate-weekly]]
- [[exporter-waits-indefinitely]]
```

Under 20 lines.

## gaps.md

```markdown
# Gaps

## Who owns the exporter on-call rotation?
Missing: no note names an owner. Likely source: the on-call spec or the team channel.
```
