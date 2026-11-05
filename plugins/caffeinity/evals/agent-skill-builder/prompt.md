---
max_turns: 3
timeout_seconds: 180
allowed_tools: [Agent, Skill, Read, Glob, Grep]
tags: [trigger, agent, positive]
---

I paste these five prompts every week when I review our Terraform:

1. Review this Terraform plan for anything that would destroy or replace a resource.
2. List every security group rule in this .tf that opens a port to 0.0.0.0/0.
3. Check these modules for hard-coded secrets, account IDs or regions.
4. Which resources here have no tags for owner, environment and cost centre?
5. Summarise this plan for a non-engineer in five bullet points.

Take that all the way to a released skill I can install, start to finish.
