# Visibility findings handoff

Send one object with `schemaVersion: 1`, `site` (canonical HTTPS origin), `observedOn` (ISO date), and arrays named `queries` and `findings`. Use empty arrays when evidence is unavailable. Do not insert placeholder text as evidence.

A query has `id`, `query`, `engine`, `scope` (locale, device and results depth as available), `expectedUrl`, `observedUrl` (null if absent or unavailable), and `observation`. The observation must distinguish checked and absent from unrun or blocked. Query IDs are unique within a report.

Each finding has `id`, `url` (the exact landing page or affected surface), `category`, `status`, `evidence` (non-empty array of observations with source URLs or artifact paths), `queryIds` (zero or more existing query IDs), `action` and `verify`. Use short stable IDs derived from the issue and page. Keep repository or generator paths when verified, and use a specific evidence request when the action cannot proceed.

| Category | Evidence for an actionable issue |
| --- | --- |
| `eligibility` | A measured status, robots directive or crawl block conflicts with intended publication. |
| `discovery` | A confirmed sitemap, manifest or crawlable internal-link gap on an intended landing page. |
| `canonical` | Explicit conflicting canonical signals, or URL Inspection showing Google selected a different URL. Distinguish the two sources. |
| `content` | A specific title, heading, introduction or rendered content mismatch with the page's verified task. Length alone is advisory. |
| `ownership` | Documented intent overlap. Use page/query evidence when claiming real cannibalization. |
| `distribution` | A verified stale, missing or incorrect public listing for this page or its corresponding skill. |
| `measurement` | A result is absent or the evidence is insufficient. Request the missing inspection or performance data. |

Use `actionable` for a supported correction and `inconclusive` for an evidence request. A public search miss alone is inconclusive about indexation and the cause of the miss. `verify` names a direct check for the change, or the specific evidence to retrieve. Coordinate copy fixes and ranking follow-up without claiming one proves the other.

Sources: [Google site operator](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site), [URL Inspection](https://developers.google.com/search/help/debug), [Search performance filters](https://support.google.com/webmasters/answer/17011165?hl=en).
