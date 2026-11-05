---
max_turns: 3
timeout_seconds: 180
allowed_tools: [Agent, Skill, Read, Glob, Grep]
tags: [trigger, agent, positive]
---

We're starting cold email at 20k sends a month. Here's our ICP, a sample of the lead list and the offer:

ICP: B2B SaaS companies, 50-500 employees, selling to finance teams; buyer is the VP or Head of Finance.

company,domain,employees,title,industry
Ledgerline,ledgerline.example.com,140,VP Finance,B2B SaaS (AP automation)
Northwind Freight,northwind-freight.example.com,2300,Office Manager,Logistics
Quillbook,quillbook.example.com,85,Head of Finance,B2B SaaS (spend management)

Offer: a close-management tool that cuts month-end close from 10 days to 4.

Run the whole outbound setup: check the list against the ICP, size the inboxes and warmup, and write the sequence.
