# Report formats

The shape each mode produces. Every shape starts with the status line and ends with the source list; both are in `verification.md` and neither is optional. Sections between them are what changes per mode.

Rank everything by importance to the decision the user named, not by the order you found it in.

---

## Topic overview

For "what do we know about X". Scope it before you search: the version of X the user means, the time window, the geography, the segment. Say the scope in one line under the status; silent narrowing is how a brief misleads.

```
STATUS + SCOPE + DECISION THIS INFORMS
1. What this is, in three sentences     # definition, boundary, why it matters now
2. Load-bearing findings                # 3-7 bullets, each with a source row behind it
3. How the field works                  # actors, incentives, measures used
4. What is contested                    # live disputes, both positions, sources dated
5. What is not known                    # named gaps plus the route to closing each
6. Sources read
```

Rules for this mode:

- Put the answer in section 2, not at the end. A reader who stops after four bullets must not stop after the wrong ones.
- Definition first where the term is contested. Half of apparent disagreements are two sides using one word for different things; if the sources define X differently, say so before comparing their numbers.
- Do not narrate the search. "I checked several sources" adds nothing; the source list proves it.
- If the overview is a stepping stone to due diligence or a decision, end with the handoff block instead of a fifth finding.

---

## Competitive intelligence

For "who else does this" and "what should I know about <competitor>". Useful before a meeting, a pricing decision, or a positioning call. Sourced facts about them, never invented weaknesses.

Single-profile shape:

```
STATUS + WHO THIS PROFILE IS + DATE OF SCAN
1. Snapshot            # what they sell, to whom, at what stated price, from their own pages
2. Claim table         # one row per fact, sources dated; pricing and figures marked carefully
3. Positioning         # their own words from site, deck or filings; attributed quotes
4. Signals             # hiring, changelogs, release notes, funding, filings — each dated
5. What we cannot see  # retention, margin, real pipeline: not public, say so
6. Conflicts           # where a third-party claim disagrees with their own page
7. Sources read
```

Comparison shape (several competitors): one table, one column per competitor, one row per attribute, and a row of "not found" where an attribute is not public. Attributes the user did not ask about stay out; a nine-column table of trivia is not intelligence.

Rules:

- Their own marketing page is a claim by them, dated, and it goes in the table with that label. So does a review site's contradicting claim. Both, when they clash.
- Signals are not conclusions. "Hiring six engineers in this area, postings dated <month>" is a finding; "they are building X" is inference and must be labelled as inference.
- Never invent a client name, revenue, user count or churn figure. Public filings and their own pricing page are fine; your memory of a TechCrunch article is not.
- Name the date of scan in the header. Competitor facts rot in weeks and the reader needs the timestamp.

---

## Industry scan

For market size, growth drivers, key players and emerging trends in an industry and geography. This is the mode where fabrication is most likely, so the figure rules are strictest here.

```
STATUS + INDUSTRY DEFINITION + GEOGRAPHY + TIME WINDOW
1. Summary                # what the decision-relevant picture is, in 5 lines
2. Market size            # one row per figure, each with source, year, and method weakness
3. Growth drivers         # each tied to a dated source or marked [unverified]
4. Key players            # named, with what each is and the source that says so
5. Emerging trends        # see trend scan shape below
6. Conflicts              # where two estimates disagree, both kept
7. Gaps                   # the figures no public source supports
8. Sources read
```

Market-size rules:

- One row per figure, never a single blended number. Give each estimate its own line: source, publisher, year of estimate, what is counted in "the market".
- Name the methodology weakness on the same line. Typical weaknesses: a market definition that includes adjacent spend, a top-down share of a parent category, a forecast presented as measured revenue, a study commissioned by the vendors it forecasts for, no stated sample.
- When estimates differ by more than a trivial amount, keep the spread visible and state which you weight and why. Averaging a $2bn and a $40bn estimate into "$21bn market" is the failure this rule exists to stop.
- If no dated source is found, the line reads: `Market size: not established from public sources in this session [metric — supply this, or commission a definition]`. Then define the market precisely enough that a real figure could be found; a good definition is a deliverable.
- A forecast is not a measurement. Label CAGR and projections as the source's forecast, with its base year and its range of uncertainty if the source gives one.

---

## Literature review

For academic and professional research on a topic, synthesised into a knowledge map rather than an annotated list.

```
STATUS + QUESTION + DISCIPLINES SEARCHED + DATE RANGE OF LITERATURE COVERED
1. Map of the field        # 2-5 clusters of findings, named by what they conclude
2. Consensus             # claims multiple independent groups support, each with sources
3. Disputes            # where the literature disagrees, and on what (sample, measure, population)
4. Weak evidence        # single-study findings, preprints, non-peer-reviewed claims: labelled
5. Method limits        # what the literature cannot see: study designs, populations, timescales
6. Gaps                # questions the literature has not addressed
7. Sources read          # full citations with publication years and the date you read them
```

Rules:

- Cluster by conclusion, not by paper. A list of twenty abstracts is a pile; four findings with three papers behind each is a map.
- Independent replication is the only thing that upgrades a finding. Say how many distinct groups, and whether they used different samples or the same one.
- Mark preprints, editorials, letters and non-peer-reviewed work as such on the row, without pretending the label settles the question.
- Never cite a paper you did not open. If you only saw it quoted in a review, write `[cited in <review you did open>]`.
- Report effect sizes and populations as the source states them. Do not convert "associated with" into "causes".
- If a paper's own limitation section contradicts its abstract, the limitation goes in the row.

---

## Trend scan

For "what is changing before it is obvious". A trend is a pattern with dated observations at both ends and a mechanism that explains it. Absent any of the three, it is a hunch and gets labelled that way.

```
STATUS + DOMAIN + LOOKBACK WINDOW USED
Per trend:
  Name                                   # one line, no marketing verbs
  Observations                           # >= 2 dated data points from sources read
  Mechanism                              # why it would continue, sourced or labelled inference
  Counter-case                           # the strongest evidence it is not a trend
  Falsifier                              # what would show it was wrong, and by when
  Confidence                             # see verification.md
Then: Not-a-trend list                    # patterns that looked like trends and were not, and why
Then: Sources read
```

Rules:

- Two dated points minimum, from sources you opened. One article announcing a shift is an announcement.
- Publication volume is not adoption. "More people are writing about X" needs a separate signal, e.g. hiring, funding, standards activity, or measured usage, from a dated source.
- Survivorship: the counter-case is mandatory. A trend scan with no failed candidates reads as promotion, not research.
- Do not date-shift old talk into new momentum. If the same claim ran in the trade press years ago, say when.

---

## One-page executive brief

For "summarise this so a leader can read it in two minutes". The page is the deliverable; the long version stays in the working notes and goes to the source list by reference.

```
Header: subject, decision informed, date, STATUS, who prepared it
1. Bottom line          # 2-3 sentences: what is known, what it means for the decision
2. Three to five findings  # one line each, each with a bracketed short source + date
3. The number that matters  # the single figure the decision rests on, with [unverified] if it is one
4. Conflicts            # 1-2 lines: where sources disagree and which way you lean
5. What we do not know  # 1-3 lines, each with the cheapest way to close it
Footer: Sources read (n), full claim table available on request
```

Rules:

- One page means one page. Cut findings that do not change the decision; the rest belongs in the full mode.
- Every line on the page inherits the claim table's sourcing. No "industry sources say".
- Never write "this proves", "clearly", or "obviously". Write what the source said, dated.
- If the status is INCONCLUSIVE, the bottom line says so first and the findings section is replaced by the assumed structure from `verification.md`.

---

## Fact check

Short form of the claim table for a single assertion: verdict wording (`SUPPORTED`, `PARTLY SUPPORTED`, `CONTRADICTED`, `NOT ESTABLISHED`), the strongest source for, the strongest source against, what each defines its terms as, and the date each was read. Full rules in `verification.md`.

## Expert synthesis

For "what do the leading thinkers argue". Attribute each position to a named person and a dated artifact read in the session: paper, talk transcript, interview, their own writing. State each position as its strongest argument, not its weakest. Where they disagree, put the disagreement in Conflicts. Where a person is quoted, quote them exactly from the fetched text and mark any paraphrase as paraphrase. Do not assemble a position for someone from vibes: if you cannot find them saying it, they go on the not-found list.

## Public-figure interpretation

For numbers found in published sources, not the user's own data (the user's file is `data-readout`'s). Read the figure in its own terms: what the source counted, over what period, in what currency or units, measured or forecast, who commissioned it. Then compare it only with figures using the same definition, and say which definitions differ. Any step beyond what the source states is inference and is labelled. If the interpretation the user wants requires the underlying data, say the public figure cannot support it and hand the question over with a note on what data would.
