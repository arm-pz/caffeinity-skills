# Confirming a verdict

Read this before step 3. The script's verdict is a first pass. A tool goes into a pitch as dead,
acquired, sunsetting or stale only once a person could open the evidence and agree.

## Per suggested verdict

| Script says | Confirm by | Keep the verdict when |
| --- | --- | --- |
| DEAD (parked) | Open `final_url` with the fetch tool | the page is a registrar, for-sale or parking page |
| DEAD (dns / refused) | Fetch the root domain, then search `"<tool>"` for the last 12 months | the root also fails and nothing current exists under the name |
| ACQUIRED | Search `"<tool>" acquired` in news, and read the acquirer's announcement | an announcement or the redirect target names the acquisition |
| SUNSETTING | Read the notice and record the shutdown date | the notice is on the tool's own site or in its official channel |
| INCONCLUSIVE | Fetch the root domain with the fetch tool (it may route differently from the script), then search `"<tool>" shut down`, `"<tool>" acquired`, and `"<tool>"` for the past year | a fetch or search gives evidence for one of the verdicts above; otherwise leave it INCONCLUSIVE |
| ACQUIRED (domain-move) | Nothing to confirm: the script saw the same name on another TLD | always ALIVE; note the new URL |
| ACQUIRED, but the target names the same company | Read the target's terms, DPA or about page for the legal entity | a different company owns it. If it's the same entity, it's a **rebrand**: ALIVE, with a courtesy fix if the listed link no longer reaches the listed thing |
| INCONCLUSIVE (`github-search:not-found`) | `git ls-remote https://github.com/<owner>/<repo> HEAD` | the command fails too (search misses repos; git doesn't) |
| ALIVE | Run the stale check below only if the list is two or more years old | — |

Behind a forward proxy (as in a cloud sandbox), a domain that doesn't resolve comes back as a
proxy error, so the script reports it INCONCLUSIVE, not DEAD. That's expected. Confirm it with the
INCONCLUSIVE row above.

Seen on a real run (skillsmith.tech, November 2026): 12 flags out of 138 tools, 0 confirmed dead.
They were 3 domain moves, 2 rebrands, 2 shutdown-word matches in UI strings, and 5 blocked or
search-missed checks that loaded fine on a second route. Expect most flags to clear.

## STALE

STALE means the product exists but has visibly stopped: the listed entry misleads readers, but the
company may still answer. It needs **two** dated signals, each older than 12 months:

- last blog, changelog or release-notes entry
- last post on its official social account
- last app-store or extension-store update
- copyright footer year, which is the weakest signal and never enough on its own
- pricing or signup page that 404s while the homepage loads

Record each signal with its date and URL in `signals`. One signal is a note, not a verdict.

## Never

- Call a tool dead because the script couldn't reach it. Blocked isn't gone.
- Say a company "went bust" or "failed" unless a source says so. Write what the evidence shows:
  "the domain now redirects to Bigcorp", "the site shows a for-sale page".
- Treat a competitor's shutdown as a talking point beyond the list entry. The pitch is about
  keeping the editor's list accurate, not about the competitor.
