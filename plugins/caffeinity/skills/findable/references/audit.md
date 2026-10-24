# Audit: find the baseline before changing anything

Goal: know where the project appears today, where comparable projects appear, and what the repo's own metadata says. Without a baseline you cannot tell whether anything you change worked.

Contents: [1 Name searches](#1-name-searches) · [2 Task searches](#2-task-searches) · [3 Same-name projects](#3-same-name-projects) · [4 Repo metadata](#4-repo-metadata) · [5 Baseline table](#5-baseline-table) · [6 Reading the results](#6-reading-the-results)

## 1. Name searches

Run these and note whether the project appears and what ranks above it:

- the project name alone
- `owner/project`
- the project name plus "github"
- the project name plus its category ("agent skill", "MCP server")

Record the top results, not just the project's own position.

## 2. Task searches

These matter more than name searches, because most people do not know the name. Run each of the target queries (see SKILL.md step 3) and record:

- whether the project appears, and where
- which similar projects do appear, and on which sites (directories, aggregators, blog posts)
- which sites list competitors but not the project. Those are the distribution targets.

Use a plain web search, and also a GitHub search if you have `gh`: `gh search repos "<query>" --limit 20`. Be sceptical of results for `topic:` filters; they return a lot of noise.

## 3. Same-name projects

For every other project sharing the name, note:

- what it is and whether it overlaps in purpose (unrelated, adjacent, or direct competitor)
- where it is listed (an extra directory listing is often what makes one same-name project outrank another)
- how a reader could confuse the two

Anything adjacent or direct feeds the name decision in SKILL.md step 4. Even an unrelated same-name project needs a disambiguation line in the README and site FAQ.

## 4. Repo metadata

With the GitHub CLI:

```
gh repo view OWNER/REPO --json description,homepageUrl,repositoryTopics,licenseInfo,latestRelease,stargazerCount,pushedAt
```

Without it, read the repo page, or ask the user to paste the About panel and the first lines of the README. Some search and fetch tools cannot read GitHub tree or blob pages; say so and work from what you can see rather than guessing.

Check and record:

| Field | What good looks like |
|---|---|
| Description | Filled in, under 350 characters, says what the project does and for whom |
| Homepage | Set to the project's page on the user's site, if there is one |
| Topics | Present, relevant, and not only generic ones |
| License | A license file exists |
| Releases | At least one tagged release |
| README opening | First sentence names the task and audience, not just the project |
| Install line | One copy-paste command near the top |
| Social preview | Custom image set (cannot be seen through the API; ask) |
| Last push | Recent; stale repos look abandoned |

## 5. Baseline table

Present a short table to the user:

| Query | Project found? | Who ranks instead | Where those are listed |
|---|---|---|---|

Followed by a short list of metadata gaps from section 4.

## 6. Reading the results

- Not appearing is an index and distribution gap. It does not say the project is worse than the ones that appear.
- Likely contributors, stated as inferences: a project that is new, present only on GitHub, with a weak or shared name, against projects that have several listings.
- A project showing up only when you search its exact path is effectively undiscoverable to anyone who does not already know it.
- Directories that surface install counts or stars reward early installs. Note which ones do, but do not promise an effect you have not seen.
