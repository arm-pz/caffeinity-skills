# Finding list articles

Read this before step 2. It lists the query patterns, what to skip, and how to score priority.

## Query patterns

Run each pattern for every category keyword (`{kw}`) and every competitor (`{c}`). Add the current
year and the previous one, since editors date their titles and refresh them every year.

| Pattern | Finds |
| --- | --- |
| `best {kw}` / `best {kw} {year}` | the main roundups |
| `top {kw} tools` / `top {kw} software` | the same, worded differently |
| `{kw} for {audience}` | niche lists, which are usually smaller sites and easier to get onto |
| `{c} alternatives` / `alternatives to {c}` | lists where a reader is already looking to switch |
| `{c} vs` | comparison pages, which often link out to a list |
| `{c} competitors` | analyst-style roundups |
| `"{c}" "{c2}"` (two competitors in quotes) | any page naming both, including lists without "best" in the title |
| `{kw} tools we use` / `our {kw} stack` | stack posts by real businesses, which also feed step 3 |

Go two result pages deep per query. Past that, almost everything is a duplicate.

## Skip

- The user's own domains, the competitors' own domains, and anything on the brief's Exclude line.
- Review marketplaces (G2, Capterra, TrustRadius, GetApp, Product Hunt, AlternativeTo, SaaSworthy)
  and app stores. They have no editor to pitch, and getting listed there is a separate job
  (claim the profile). Note them in the report as "directory, not pitched".
- Forums, Q&A threads, videos and social posts. There's no article to update and no author who owns
  it.
- Pages that hold only a pay-to-be-listed form. Note them in the report with a `sponsored` flag
  rather than drafting a pitch, because a paid placement is a budget decision for the user.

## GitHub lists

In developer categories, many of the lists that matter are GitHub awesome-lists, not articles. Add
`awesome <kw>` and `<kw> github list` to the patterns. They qualify like any other page. Their
route and eligibility come from `CONTRIBUTING.md`, which step 4 of the skill reads. Their entry
format is one table row or one `- [name](link) - description` line. Copy the neighbouring entries
exactly.

## Qualify each page

A page qualifies when it is an editorial list or comparison, names at least one competitor, and
does not name the user. `scripts/scan_mentions.py` makes the naming decision so it is the same
every run. Read the page yourself for the rest:

- **Dates.** Take the published and updated dates from the byline or the page metadata. If neither
  is shown, write `unknown`. Don't infer a date from the title's year.
- **Takes submissions.** Look for "suggest a tool", "submit your product", "email us to be
  included" or a form. Write `yes` and the URL, or `no`.
- **Sponsored.** Look for "sponsored", "paid placement", "affiliate" or "we may earn a commission". An
  affiliate list can still be pitched, but say so in the notes, because the editor may ask about
  an affiliate program.

## Priority

Score `high`, `medium` or `low`, and write the reason in `notes`:

- **high**: names two or more competitors, updated in the last 18 months, and has a findable author
  or a submission route.
- **medium**: names one competitor, or is older than 18 months but still ranks for the query, or the
  contact route is a generic contact form.
- **low**: no date and no author, a site with no other content in the category, the only route is
  paid, or a GitHub list whose gate the user's repo doesn't meet yet (`NOT ELIGIBLE YET`).

If an authority metric (domain rating, organic traffic) is available from a connected SEO tool,
put it in `notes` with the tool's name. If none is available, don't estimate one.
