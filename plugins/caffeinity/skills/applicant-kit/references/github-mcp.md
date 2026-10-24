# Optional: the third-party recruiter-lens MCP server

This is **not** the recruiter-lens skill. It is an unrelated open-source MCP server (dani-aisystems/recruiter-lens) that happens to share the name. It audits GitHub repositories and profiles for hiring signal and exposes two tools:

| Tool | Input | What it returns |
|---|---|---|
| `recruiter_scan` | a GitHub username | profile-level facts: bio, pinned repos, activity recency, and a rule-based verdict |
| `audit_repo` | `owner/repo` | repo-level facts: README presence, CI, license, topics, commit-message patterns, activity recency, and rule-based severity findings |

It does not call an LLM. Everything it returns is a deterministic fact or a rule-based verdict, so treat it as evidence. The judgment layer is yours: read the code and README when you can, weigh what the facts mean for this candidate and this role, and turn them into resume, LinkedIn, and interview changes. Tool names and behavior above come from the project's public README; if the tools in the session are named differently, use the ones actually listed.

## Trust note

This is third-party code, run through `npx`, that uses a GitHub token. Before suggesting it to a user:

- Say plainly that it is a separate project from the recruiter-lens skill and from this skill, and that the user is installing someone else's code.
- Suggest the least privilege that works: a read-only token limited to public data is enough for public repos. A classic token with `repo` scope also exposes private repos, so only suggest that if the user explicitly wants private repos audited.
- Suggest pinning a version rather than running whatever is latest, and reading the project's source and release notes first.
- Never ask the user to paste a token into the chat. The server reads `GITHUB_TOKEN` from its own configuration.

Setup, from the project's README:

```
claude mcp add recruiter-lens -e GITHUB_TOKEN=<your token> -- npx recruiter-lens-mcp
```

## When to call it

Only for technical roles, or when the user shares a GitHub handle and asks for it.

| Mode | Call | Why |
|---|---|---|
| 3 Keyword placement | `audit_repo` on the user's main repos | Topics and READMEs can reveal skills the user has but never wrote down. Ask before adding them. |
| 5 LinkedIn rewrite | `recruiter_scan` on the user's handle | Align the headline, About, and Featured section with what the GitHub profile shows. |
| 6 Answer pack | `audit_repo` on the 2 to 3 repos the resume cites | Predict project deep-dive questions and the weak spots an interviewer will probe. |
| Direct request | either | "How does my GitHub look to recruiters?" is a question for this server on its own. |

Use the handle the user gave you, and scan the user's own profile by default. If they ask you to scan someone else, stick to public data, report only what the tool returned, and do not draw conclusions about the person's character.

## If the tools are not available

Look for them first; if they are not visible in the tool list, try a tool search for "recruiter-lens" before concluding they are missing. If they are not there, say so once, in one line, and carry on without them. Offer the setup command above together with the trust note. Fallbacks: the user can paste their repo list and READMEs, or run `npx recruiter-lens scan <username>` themselves and paste the output. Do not fabricate tool output or guess what a scan would say.

## Reporting results

- Attribute facts to the tool ("the MCP server reports no CI on `repo-x`") and keep your own judgment visibly separate ("for a backend role that matters because...").
- Turn each finding into an action with a destination: a README fix, a pinned repo change, a resume line, a LinkedIn Featured item, or a prepared answer. A finding with no action attached is noise.
- Rank findings by recruiter impact. A missing README on the pinned flagship repo outweighs five small issues on forgotten ones.
- If a call fails (rate limit, 404, private repo, bad token), report the error plainly, say what it blocks, and move on; do not substitute assumptions.
- The server's verdict is one input, not the final word. Its facts are evidence; the verdict on the resume itself belongs to the recruiter-lens skill.
