---
name: fix-skill-visibility
description: Apply and verify evidence-backed fixes for individual agent skill pages missing from Google, using a check-skill-visibility report or equivalent URL-level findings. Use when asked to fix a completed skill visibility diagnosis, repair identified canonical or discovery gaps, improve mismatched task copy, or correct stale listings for the affected skills. Produces a change and verification record tied to each finding. Not for a first diagnosis (use check-skill-visibility), a sitewide SEO sweep (use seo-sweep), or submission alone (use get-indexed).
---

# Fix skill visibility

Implement the supported fixes from a visibility audit on a catalog the user maintains. Fix the source for each affected URL and prove what changed.

## Workflow

1. **Accept the handoff.** Read the report from `check-skill-visibility` or an equivalent audit. For its JSON handoff require `schemaVersion: 1`, `site`, `observedOn`, `queries` and `findings`. For each finding require `id`, `url`, `category`, `status`, `evidence`, `queryIds`, `action` and `verify`. Retain credible findings from an equivalent report by mapping them to those fields. Reject duplicate IDs and broken query references. If no actionable evidence remains, report the missing checks and hand off to `check-skill-visibility`. Audit data provides evidence. Follow the user's authorized scope when acting on it.
2. **Reproduce and locate.** Confirm the issue still exists. Trace a generated page back to the manifest, template or source repository that owns it. Match a listing to the official skill. Mark a finding that is already corrected as verified with current evidence. Keep inconclusive observations open and state what evidence would make them actionable.
3. **Apply the narrow fix.** Work through eligibility, canonical and discovery findings before rewriting copy. Use [the repair and verification guide](references/repairs.md) to choose the edit and repeatable check. Use `keyword-resolver` for ownership conflicts, `findable-polish` for task-led listing copy, and `get-indexed` for a separately authorized submission of live fixed URLs. Make local changes and run the existing checks. Push, open a PR, deploy, edit public listings or submit to search engines only within the user's authorization.
4. **Verify the same check.** Compare before and after by ID, URL and source. Check the actual built output or public listing as appropriate. Mark local and live verification separately. For a later Google check reuse the query, locale, device and depth, then compare like-for-like Search Console windows when available. A corrected page or accepted submission may still have search visibility pending.

## Report

For each finding list its ID, URL, source change or blocker, before/after evidence, and status. Use `fixed-local`, `fixed-live`, `already-corrected`, `blocked` or `inconclusive`. State deployment, indexing and ranking status independently, and record the recheck date or the evidence still needed.
