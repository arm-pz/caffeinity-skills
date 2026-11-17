# Handover between the three outreach skills

The same file ships in `get-listed`, `replace-dead-tools` and `find-partners`.
If you edit it, copy it to all three so the steps keep agreeing on what gets handed over.

The chain runs in this order. Each step writes into one `outreach/` folder in the user's working
directory and ends its run with a Handover block, so the user can see where they are and what the
next step picks up.

```
1. get-listed   lists that name competitors and not you, their authors, a pitch each
        │  brief.md, lists.csv, list-tools.csv, pages/, pitches/
        ▼
2. replace-dead-tools     dead or acquired tools still on those lists, "replace them" pitches
        │  dead-tools.csv, pitches/*-replace.md
        ▼
3. find-partners      non-competing businesses for guest posts, quotes and co-made content
           partners.csv, asks/
```

Each step can also start on its own. Step 2 accepts a list of article URLs, and step 3 needs only
the brief. If an expected file is missing, ask the user for that input; don't make up the rows.

## Folder layout

```
outreach/
  brief.md            who you are, category, competitors, signer, offer, proof (step 1 writes; all read)
  lists.csv           one row per qualifying list article (step 1)
  list-tools.csv      one row per tool named on a qualifying list (step 1; step 2 reads)
  pages/<slug>.md     the fetched text of each list article (step 1; step 2 rereads)
  pitches/<slug>.md   gap pitch per list (step 1)
  pitches/<slug>-replace.md   replacement pitch per list with a dead tool (step 2)
  dead-tools.csv      verdict per checked tool (step 2)
  partners.csv        one row per partner candidate (step 3)
  asks/<slug>.md      collaboration ask per partner (step 3)
```

`<slug>` is the article's host and path, lowercased, with every run of non-alphanumerics turned into one
hyphen and the result cut to 80 characters: `example-com-blog-best-crm-tools`.

## brief.md

```
# Outreach brief
- Site: https://...
- Product: one sentence, in the user's words
- Category keywords: 3–5 phrases buyers search
- Audience: who buys
- Competitors: Name (domain), Name (domain), ...
- Signer: name, role
- Offer to editors: e.g. free account for testing, a quote, screenshots, original data
- Proof: facts the user confirmed (customers, numbers, awards). Nothing else goes in a pitch.
- Exclude: domains never to pitch (partners, past disputes)
```

## lists.csv

`slug,url,title,site,published,updated,competitors_named,competitor_count,you_named,author,author_url,contact_route,contact_source,takes_submissions,sponsored,priority,notes`

- `you_named` is always `no` on a qualifying row. Rows where it is `yes` are dropped, not kept.
- `contact_route` is a published route only: an email shown on the page or the site, a contact
  form URL, or a public profile URL. `contact_source` is the URL where you saw it. If you found
  none, write `not found`. Never guess an address from a name pattern.
- `priority` is `high`, `medium` or `low`, scored by the rules in the step 1 skill.

## list-tools.csv

`list_slug,list_url,tool_name,tool_url`

## dead-tools.csv

`tool_name,tool_url,verdict,final_url,status,signals,evidence_url,checked_on,list_slugs`

`verdict` is one of `DEAD`, `ACQUIRED`, `SUNSETTING`, `STALE`, `ALIVE` or `INCONCLUSIVE`. A
verdict other than `ALIVE` or `INCONCLUSIVE` needs an `evidence_url` that a person can open.

## partners.csv

`slug,name,url,type,audience_fit,why_not_competitor,collab_type,value_to_them,value_to_you,contact_route,contact_source,red_flags,priority`

## The Handover block

End every run with this block, filled in. Write "none" in a field that has nothing; don't leave it out.

```
## Handover → <next skill, or "end of chain">
Done: <one line: what this step produced, with counts>
Files: <paths written or changed>
Next step receives: <the files and the rows it should use>
Needs you: <decisions or facts only the user can give>
Not verified: <checks that were blocked, skipped or only partly run>
```
