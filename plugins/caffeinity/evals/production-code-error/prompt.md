---
max_turns: 3
timeout_seconds: 180
allowed_tools: [Skill, Read, Glob, Grep]
tags: [trigger, positive]
---

This Python script throws KeyError: 'user_id' on line 42 when the CSV has an empty row. Fix it and explain the root cause.

for row in csv.DictReader(f):
    users[row['user_id']] = row
