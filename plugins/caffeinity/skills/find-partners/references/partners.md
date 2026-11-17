# Finding and qualifying partners

Read this before step 2.

## Who counts as a partner

A real business or publisher with the same audience and a different product. Typical types:

| Type | Example for a CRM | Usual collaboration |
| --- | --- | --- |
| Complementary tool | email platform, invoicing app | integration listing, co-written guide, joint webinar |
| Service provider | agency, consultant, implementer | guest post, expert quote, case study with a shared client |
| Publisher | niche newsletter, blog, podcast | guest post, interview, newsletter feature, original data |
| Community | association, Slack or Discord group, meetup | talk, resource, sponsored slot (disclosed) |

Competitors from the brief are never partners. Neither is anyone on the Exclude line.

## Queries

Run these with `{kw}` = each category keyword and `{aud}` = the audience:

- `{kw} integrations` and `"works with" {competitor}`: tools that already plug into the category
- `{kw} "write for us"`, `{kw} "guest post"`, `{kw} "contribute"`: sites that take contributions
- `{aud} newsletter`, `{aud} podcast`: publishers with the audience
- `{kw} agency` / `{kw} consultant`: service providers
- `"tools we use"` + `{kw}` / `"our stack"` + `{aud}`: businesses that publish stack posts
- Sites in `outreach/lists.csv` that publish more than one article in the category

## Red flags: drop the candidate

Two or more of these, and the site is a link seller, not a partner:

- A "write for us" page with a price list, a menu of link types ("dofollow, nofollow or
  sponsored") or an invoice after publishing. Any one of these is enough to drop the candidate.
- Recent posts on unrelated topics (casino, CBD, loans, essay writing) alongside the category
- Every post ends with two or three outbound commercial links in the same pattern
- No named authors, no about page, no product or service of its own
- Traffic or authority claims on the contribute page, but no audience to speak of (no comments,
  social following or newsletter)

Write the flags in `red_flags` even for candidates you keep. One flag is a note. For podcasts,
AI-generated hosts are a flag too, because there's no one to interview, only a mention to hope for.

Green flags count as well: a contribute page that refuses paid links and link insertions, asks for
a pitch before a draft, or names an editor is a publisher protecting its readers. Those are the
ones worth the effort.

## Priority

- **high**: clear audience overlap, a named contact, and a collaboration type the partner already
  does (they publish guest posts, run a podcast, list integrations).
- **medium**: audience overlap, but a generic contact or no sign that they do this kind of
  collaboration yet.
- **low**: partial overlap, or one red flag.
