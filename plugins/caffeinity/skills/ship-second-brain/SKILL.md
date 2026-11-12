---
name: ship-second-brain
description: >-
  Builds and maintains a team second brain in one markdown folder: raw issues,
  PRs, specs and call notes saved first, cut into one-idea notes with a source
  and confidence (seen, verified, opinion), linked, verified against the source,
  summed up in today.md, and checked by an answer test, with misses in gaps.md.
  Use whenever a question or task touches such a vault (a folder with raw/ and
  notes carrying confidence front matter): what did we decide about X and where
  is it written down, a new spec or source that says something different from a
  verified note, ingest PRs or issues, file call notes, verify or upgrade notes,
  clean up or delete files, run the answer test, stop re-explaining context
  every session. Even if they never say second brain. Not for a one-off summary of one document, a shareable doc
  built from the vault (use docs), or a database or Notion setup.
version: 0.1.0
---

# Ship Second Brain

The vault is one folder of markdown, written by Claude, read by people, and never trusted until checked against its source. It is done when every note follows the format in `references/note-format.md`, every claim carries a source, and a fresh session can answer the team's questions from the vault alone.

## The rules

1. **Markdown only.** No database, no index service, no plugin that can disappear. A folder of `.md` files survives every tool change.
2. **Raw goes in first.** Save the source before interpreting it. An interpretation without its raw file cannot be checked later.
3. **One note, one idea.** A note that needs scrolling is two notes. Merged ideas cannot be linked, downgraded or contradicted separately.
4. **Every claim links to where it came from.** A line without a source is an opinion and is marked `Opinion:`. Unmarked, unsourced lines are how a vault starts lying.

## Inputs

| Field | Meaning | Default when missing |
| --- | --- | --- |
| `VAULT` | Vault folder path | `./vault` |
| `SOURCES` | Issues, PRs, specs, call notes: URLs, file paths or pasted text | none: nothing to ingest, run only Pass 4 to 6 on the existing vault |
| `QUESTIONS` | What the vault must answer | none: skip Pass 6 and say so in the report |
| `SCOPE` | What you may change | only files inside `VAULT` |
| `LIMIT` | Budget: sources, notes or time | no limit beyond `SOURCES` |

If a missing field changes the outcome, ask one question, once. Otherwise start and print the defaults you used.

## Vault layout

```
VAULT/
├── raw/            # sources exactly as received, never edited or deleted
├── inbox/          # notes with no links yet, waiting for review
├── <idea-name>.md  # one note per idea
├── today.md        # the daily note, the one file a human reads every day
└── gaps.md         # questions the vault could not answer
```

## The six passes

Run them in order. Each pass depends on the one before.

### Pass 1: Intake
For each item in `SOURCES`, save its raw text to `raw/YYYY-MM-DD-<origin>-<id>.md` with front matter `date`, `origin` (github-issue, github-pr, spec, call-notes, ...) and `url` (the exact URL, or the original file path). Copy the text as-is. Do not summarize yet. Do not delete or overwrite anything that came in: if a source changed, save a new dated raw file next to the old one.

After intake, record the raw files so later edits or deletions are caught:

    python scripts/check_vault.py VAULT --snapshot

### Pass 2: Atomize
Cut each raw file into notes of one idea each. Name the note after the idea (`retry-uses-exponential-backoff.md`), never after the meeting (`standup-nov-6.md`). Front matter follows `references/note-format.md`: `date`, `source`, `owner`, `confidence`. New notes start at `seen` or `opinion`. Nothing is `verified` until Pass 4.

### Pass 3: Link
Every new note links to at least one existing note: the decision it supports, contradicts or answers. Use `[[note-name]]`. Links to `today.md` or `gaps.md` do not count. On an empty vault, notes from the same intake may link to each other. A note with no real link goes to `inbox/` for human review, not into the vault root.

### Pass 4: Verify
For every note marked `verified`, and every note you want to raise to `verified`, re-open the raw source and confirm the quoted words are there. Downgrade anything that does not match to `seen` and add it to the downgrade list. Never upgrade confidence without the source open in front of you.

`scripts/check_vault.py` does the mechanical part: it checks that every `> ` quote in a verified note appears in its raw source. Run it after this pass:

    python scripts/check_vault.py VAULT

Fix every FAIL before continuing. The script cannot judge whether a quote supports the claim; that judgement is yours.

### Pass 5: Daily note
Write `today.md`: what shipped, what got linked, what got downgraded, and the three notes most worth re-reading, each as a `[[link]]`. Keep it under 20 lines. It is the only file a human reads every day, so a longer one stops being read.

### Pass 6: Answer test
Start a fresh session (in Claude Code, a subagent given only the vault path) and answer each question in `QUESTIONS` from the vault alone: no web, no memory, no raw files outside the vault. Every sentence of an answer cites a note path. A question the vault cannot answer goes to `gaps.md` with what is missing and which source would likely fill it. Do not answer from your own context to make the test pass; that defeats the test.

## Never

- Store a claim without a source.
- Merge two ideas into one note.
- Delete or edit a raw file.
- Answer from memory when the vault has the note.
- Build a plugin, database or service when a folder would do.

## Stop

Stop when the first of these happens:

- every question in `QUESTIONS` is answered from the vault;
- `LIMIT` is reached;
- a source conflicts with a `verified` note. A human has to choose: report both note paths and both quotes, and do not edit either note.

## Report

Return, in this order:

1. The vault tree.
2. `today.md` in full.
3. `gaps.md` in full, or "no gaps" if Pass 6 answered everything, or "answer test skipped: no QUESTIONS".
4. The downgraded notes, each with its path and the line that failed.
5. `check_vault.py` counts (PASS, WARN, FAIL), and which passes ran, which were skipped and why.

## Hand off

- A finished, shareable document built from the vault (a spec, a memo, a decision record for people outside the team) goes to `docs`.
- A wiki, Notion space or database is outside this skill; say so and stop.
