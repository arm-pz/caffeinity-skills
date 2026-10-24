---
max_turns: 3
timeout_seconds: 180
allowed_tools: [Skill, Read, Glob, Grep]
tags: [trigger, positive]
---

Run the ledger variant of the release gate, where each lane writes its own rows into the release-gate ledger.
