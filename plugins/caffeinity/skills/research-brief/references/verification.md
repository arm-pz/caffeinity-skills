# Verification

The claim table and the honest postures. This file decides whether a brief is `SOURCED`, `PARTIAL` or `INCONCLUSIVE`, and what goes in each cell. Read it before writing any mode.

## The claim table

Every factual claim a reader could act on gets one row.

```
| Claim | Source + date read | Confidence | Conflicting source |
|---|---|---|---|
```

- **Claim** — one sentence, one testable assertion, written so a stranger could check it. No compound claims: two facts needing two sources is two rows.
- **Source + date read** — the title, the publisher, the publication date if the page shows one, and `read <date>` for the day you opened it in this session. Add the tool: `via search` or `via fetch`. If the page shows no publication date, write `undated`.
- **Confidence** — one of the labels below, never a number. A percentage of certainty invented on the spot is a fabrication wearing a decimal point.
- **Conflicting source** — the strongest source that says otherwise, with its date, or `none found`. `none found` means you looked and did not find, which is a weaker statement than "no one disputes this".

### Confidence labels

| Label | Meaning |
|---|---|
| `High` | A source you opened states it directly, the source is primary or close to the event, it is dated within the window that matters, and you found no contradiction. |
| `Medium` | Directly stated but secondary, or undated, or old relative to the question, or supported by one source with a thin look for others. |
| `Low` | Inferred from adjacent evidence, from a snippet you could not open, from a single interested party, or the source's own method is weak. |
| `[unverified]` | No source read in this session supports it. It stays in the brief with the label, or it moves to Gaps. |

An interested party can be a `High` source about its own price, its own product, its own filing. It is not a source about its own market share, its own retention or its competitor's weakness.

### Row examples, as shapes only

The angle brackets are placeholders. In a real brief each one becomes a source you opened in the session; a leftover placeholder is a bug, and so is an invented title or author name filling one.

```
| "<claim>" | <primary source title>, <publisher>, published <date>, read <date>, via fetch | High | none found |
| "<claim>" | <trade article>, undated, read <date>, via search snippet only | Low | <other source>, published <date>, gives <other figure> |
| "Market size in <geography> is <figure>" | <report title>, <publisher>, <year of estimate>, read <date> | Low | Top-down estimate counts <adjacent spend>; commissioned by <vendor group> `[unverified]` |
```

## Status line

Every brief opens with one of these, and the reason in the same line.

| Status | When to use it |
|---|---|
| `SOURCED` | A search or fetch tool was available, you opened the primary sources behind the load-bearing claims, and the table reflects that. |
| `PARTIAL` | Some claims are sourced, others rest on snippets, secondary citations or inference. Say which sections are which. |
| `INCONCLUSIVE` | No network in the session, or the sources needed do not exist publicly, or the search surface is blocked. Nothing here may read as a finding. |

## The INCONCLUSIVE posture

When the session has no network access, or no source was found, that is the result. Deliver the structure of what is assumed instead of a confident report.

Open the brief with exactly this, then continue:

```
STATUS: INCONCLUSIVE — no search or fetch tool is available in this session.
Nothing below is researched. It is the shape of the answer, with every line marked
[assumed], plus the sources and queries that would settle it. Treat it as a plan to
verify, not as findings to act on.
```

Then deliver:

1. **The questions the brief must answer**, phrased so a search can hit them.
2. **The assumed structure**, each line tagged `[assumed]`, stating what you would expect to be true and what it would take to confirm it. No figure in this section is presented as fact.
3. **The sources that would settle it**, named by type and by whoever publishes them: filings, registries, official statistics, standards bodies, the vendor's own pricing page, a specific journal.
4. **The queries to run**, in the form to type.
5. **What changes with the decision** depending on which way the answers fall.

Refuse, politely and in one line, to be talked into "just the headline numbers from memory". Recall without a source is not research, and a number remembered correctly is still a number nobody can check. If the user insists, produce the assumed skeleton with `[assumed]` on every line and note that the user asked for unverified figures.

## Handling conflicts

- Both sources stay in the brief. Never average two figures, never present the midpoint as the answer, never pick a winner in silence.
- Write a Conflicts section with each position, its source, its date, and the definitional or methodological reason they differ (what each counts, over what window, measured or forecast, who paid).
- Say which you weight and why, in one line. Weighting by primary-ness, recency and method is defensible; weighting by which number supports the user's plan is not.
- If the conflict is unresolved and matters to the decision, the confidence label is `Low` and the row goes into the executive summary, not buried in section four.
- If the conflict is unresolved and does not matter, name it in Gaps and move on.

## Figures and market sizes

Market sizes, growth rates, shares and per-user economics are the usual fabrication point. For each:

- A dated source, opened in the session, or the figure is `[unverified]`.
- Name the methodology weakness on the same line: market definition, who commissioned it, top-down versus bottom-up, sample, forecast versus measured, currency and base year.
- Report the spread when estimates disagree, and cite each estimate separately.
- Mark forecasts as forecasts, with the base year and horizon.
- If the user asks for a figure no public source carries, write `[metric — supply this]`, put it in Gaps, and describe what would produce it.

## Tool attribution

- `via search`: the claim rests on a result title or snippet you did not open. Cap it at `Low`; it is a pointer, not evidence.
- `via fetch`: you opened the document. Quote or state as read, with the page's own date.
- `user-supplied`: the user pasted or attached it. Label it as the user's material, dated by whatever the document itself says.
- Multiple tools on one claim: name the one that established it; put the corroborating source in its own row.

## Source quality, in brief

Primary and closest to the event beats secondary; secondary beats a summary of secondary. Regulator filings, official statistics, peer-reviewed papers, standards documents and a party's own pricing page are strong for what they can see. Trade press, aggregator rankings, vendor surveys and "experts say" round-ups are leads: use them to find the primary, cite the primary. A source's date of publication is not its date of accuracy; when a page describes a moving situation, note the lag.

If you cannot fetch a source (paywall, login, blocked), say so in one line, mark any claim resting on it `Low` or `[unverified]`, and name the source in Gaps as something to read. Never paraphrase a document you could not open as though you had.
