# Distribution: getting listed where people and agents look

Contents: [Starting points](#starting-points) · [How to work through them](#how-to-work-through-them) · [Entry text](#entry-text) · [Community posts](#community-posts) · [Do not](#do-not) · [Measuring](#measuring)

## Starting points

These are surfaces that turned up in research on agent-skill discovery. Treat them as places to look, not as facts. Directories change, merge and close, and how each one ingests projects (crawling, install telemetry, manual submission) was not verified. Search for current ones before recommending any, and read each one's submission rules.

| Type | Examples seen | What to check |
|---|---|---|
| Skill directories and aggregators | skills.sh (the registry behind the `npx skills` installer), Skillselion, Agent Skills Finder, Smithery's skills listings | Whether it indexes public repos automatically or takes submissions; Agent Skills Finder was described as accepting a repo URL, a skill directory URL or a direct SKILL.md URL, with a review status |
| MCP server directories | Glama, Smithery, the official MCP registry, PulseMCP | Required metadata, whether a listing needs a manifest or claim step |
| Plugin marketplaces | The Claude Code community marketplace, the user's own marketplace repo | Contribution guidelines; whether entries point at a repo or are copied in |
| Curated lists | awesome-agent-skills lists, awesome-mcp lists | The list's entry format, ordering rules and whether it wants a PR |
| Machine-readable index on the user's own domain | `/.well-known/agent-skills/index.json`, read by `npx skills add https://their-domain` | Hand to `publish-pipeline` (or follow the current spec); verify digests and that the index parses |
| The user's own surfaces | Site page per project, profile README, a blog post, cross-links between sibling projects | Consistency of names, install commands and descriptions |

Directories that display install counts or stars suggest early installs matter. Say that as a possibility, not a promise.

## How to work through them

1. Pick the surfaces that fit the project type (skill, plugin, MCP server).
2. For each, search for the current submission page or guidelines, and note what it asks for.
3. Prepare the entry text once, then adapt it to each format.
4. Present the list to the user with the effort and the expected value for each. A listing that auto-indexes costs nothing; a PR to a curated list costs a few minutes; a community post costs credibility if done badly.
5. Submit only with the user's go-ahead, and for submissions that require an account or a PR, give the user the exact text and steps.

## Entry text

Prepare these once:

- **One line (under 120 characters):** what it does, for what, with the install command or link.
- **Short description (one or two sentences):** the About text, lightly expanded.
- **Category and tags:** from the repo topics.
- **Links:** repo, project page, install command.

Use the same wording and the same project name everywhere, so listings reinforce each other.

## Community posts

Posts in communities (r/ClaudeAI, a forum, X, LinkedIn, a "Show HN" style post) can help, but only when they give readers something.

- Say it is your project.
- Lead with a concrete before and after or a real output, not the pitch.
- Read each community's self-promotion rules first, and post once per community.
- Do not ask for stars. Ask for feedback on something specific.
- Match the audience: job-search skills fit where job seekers and developers talk, MCP servers fit where agent builders do.

## Do not

- Buy, trade or arrange stars, installs, follows or reviews.
- Create fake accounts or have friends post undisclosed praise.
- Stuff topics, descriptions or pages with keywords the project does not deserve.
- Submit to many directories with copy-pasted spam text.
- Claim integrations, compatibility or results that have not been tested.

These can get a repo flagged or delisted, and they cost trust that is hard to rebuild.

## Measuring

Stars are a weak signal. Better ones:

- GitHub Insights, Traffic: views, unique visitors and referring sites, visible to the owner only and covering a short recent window, so record it regularly.
- Install counts where a directory shows them.
- Search position for each target query, re-run from the same baseline as the audit.
- Referrals and traffic to the project page on the user's site.
- Issues, questions and forks, which show real use.

Re-run the baseline queries two to three weeks after the changes, and again after a couple of months. Indexing lags, and a single early check is misleading.
