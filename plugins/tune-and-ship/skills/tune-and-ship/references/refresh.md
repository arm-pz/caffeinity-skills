# Refresh and confirm

Read this at step 8, after the PR has merged. Paths and names below are the arm-pz setup; for
another owner, read the equivalent from their site repo's README before running anything.

## What updates on its own

| Surface | Source | Schedule |
| --- | --- | --- |
| Site page, `skillsmith.tech/<skill>/` | `publish.yml` in `arm-pz/skills-site` syncs each skill repo's HEAD | hourly, and on dispatch |
| Marketplace bundle, `plugins/caffeinity/skills/<skill>/` | `build-plugin.yml` in `arm-pz/caffeinity-skills` copies each repo at HEAD | hourly, and on dispatch |

Both are generated. Never edit a generated page or a bundled copy by hand; change the source repo.

## Start them now

Run each workflow on `main` through whichever GitHub access the session has. With the CLI:

```bash
gh workflow run publish.yml --repo arm-pz/skills-site --ref main
```

```bash
gh workflow run build-plugin.yml --repo arm-pz/caffeinity-skills --ref main
```

Starting a workflow in a repo is an outward action. The owner asking for the skill to go live
covers these two; nothing else in those repos is covered.

## Confirm

1. **Site.** Fetch `https://skillsmith.tech/<skill>/` every 20 seconds for up to 15 minutes and
   look for the new version string and one phrase that only the new description contains. The
   first run went live in under three minutes.
2. **Bundle.** Read `plugins/caffeinity/SOURCES.md` on `main` and check the skill's row shows the
   merge commit.
3. **Publish run.** Its sync message lists a `refresh` line for the skill. A `hold` line means the
   site refused the repo; quote the reason, since it names the clause that failed.

## What a merge does not update

- **About text and topics.** Repository settings. Give the owner the `gh repo edit` command and
  quote the live value so the difference is visible.
- **Tags and releases.** Compare `git ls-remote --tags` with the changelog. Give the owner one
  `gh release create` command per missing version.
- **Sibling skills.** A hand-off this skill now makes may not be returned. Queue the sibling in the
  ledger.
- **Directory listings** outside the owner's repos.
