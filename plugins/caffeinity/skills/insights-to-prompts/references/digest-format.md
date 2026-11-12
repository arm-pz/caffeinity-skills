# Digest format

Fields in `insights-digest.json`, for when the summary isn't enough.

- `sources` — counts of facets, session-meta files and transcripts read; whether report.html existed.
- `report.age_days`, `report.sections` — report text split by heading, each capped at 4000 chars. Headings vary by Claude Code version; look for friction, CLAUDE.md suggestions and usage patterns by meaning, not exact title.
- `friction_totals` — every friction type summed across facets.
- `not_prompt_friction` — the subset no prompt wording would fix.
- `prompt_friction[]` — one entry per session with prompt-type friction, highest `score` first. Score = friction count + 2 if the outcome was not or only partially achieved. Carries `first_prompt` (from transcript, else session-meta), up to five `follow_ups`, `friction_detail`, `goal`, `summary`, `outcome`, `commands`.
- `repeated_prompts[]` — prompts whose first six normalized words recur 3+ times, with how many of those sessions had prompt friction.
- `skill_friction[]` — present only with `--skills-dir`; usage and friction per skill, matched by slash command or name mention.

Facets come from /insights' own Haiku pass and can mislabel. When `friction_detail` and the follow-ups disagree, trust the follow-ups.
