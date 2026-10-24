# The GitHub listing

Contents: [About text](#about-text) · [Topics](#topics) · [Homepage](#homepage) · [README opening](#readme-opening) · [Release notes](#release-notes) · [Social preview](#social-preview) · [License](#license) · [Kit format](#kit-format) · [Apply commands](#apply-commands) · [Project-type notes](#project-type-notes)

## About text

The About description is shown in search results and on directory cards, so it has to make sense with no other context.

- Limit: 350 characters. Aim for 200 to 280.
- Formula: what it is, for what task, with the guarantee or differentiator, and where it works. For example: "Agent skill that reviews resumes the way recruiters screen them: ATS check, rejection reasons, gap analysis. Never invents metrics. Works with Claude Code, Cursor and Qoder."
- Start with the category and task, matching the target queries. Do not open with the project name; it already appears next to the text.
- Plain words. No emoji, no superlatives, no claims the repo cannot back.

## Topics

Topics feed GitHub's topic pages and search.

- At most 20. Each is lowercase letters, digits and hyphens, up to 50 characters. Use 10 to 15.
- Mix three kinds: type (`agent-skills`, `claude-code`, `mcp-server`), domain (`resume`, `ats`, `seo`), and platform (`cursor`, `qoder`).
- Prefer topics that already have a page with other projects on it; an unused topic helps nobody find you. Check `github.com/topics/<name>`.
- Only true topics. Do not add a popular topic the project does not belong to.
- Skip generic filler (`ai`, `tool`, `app`) unless it really is the core category.

## Homepage

Set it to the project's page on the user's own site if one exists, otherwise leave it empty. The About panel then links the repo and the site to each other.

## README opening

The first screen decides whether a visitor stays and what a search snippet shows.

1. `# project-name`
2. **A first paragraph** that names the task, audience and guarantee in plain words, using the target-query phrases: "A resume and LinkedIn review agent skill for Claude Code, Cursor and Qoder. It checks your resume the way a recruiter screens it..."
3. **One install line**, owner-qualified, e.g. `npx skills add owner/repo --skill name`.
4. **"Ask it things like"** with three or four prompts a user would type.
5. **A disambiguation line** if any same-name project exists: what this is, what the other one is, and that they are unrelated.
6. **A sibling line** if there are related projects, saying who does what.

Keep this above the first heading below the fold. Do not add badges before the first paragraph.

## Release notes

Cut a first tagged release (`v0.1.0`). Notes are factual: what it does, the commands or tools included, and the install command. A repo with no releases looks unfinished, and some listings read releases.

## Social preview

An image shown when the repo link is shared. Describe what it should contain for the user to produce: the project name, the one-line pitch, and the install line, large and legible. GitHub's current recommendation is a 1280 by 640 pixel image under 1 MB; confirm in the repo's Settings before relying on those numbers.

## License

Check for a `LICENSE` file. If missing, tell the user and ask which license they want; do not pick one for them.

## Kit format

Write About and Topics in exactly this shape in `discovery-kit.md`, so `scripts/check_listing.py --kit discovery-kit.md` can find them:

````
**About (description, 350 character limit):**

```
The about text, one paragraph, no line breaks.
```

**Topics:** `topic-one`, `topic-two`, `topic-three`
````

For site pages, put `title:` and `description:` in the frontmatter as `title: "..."` and `description: "..."` so the script can read them.

## Apply commands

```bash
gh repo edit OWNER/REPO \
  --description "About text" \
  --homepage "https://example.com/page" \
  --add-topic topic-one,topic-two,topic-three
gh release create v0.1.0 --title "v0.1.0" --notes "Release notes"
```

Run these only with the user's confirmation. They change public pages.

## Project-type notes

**Agent skills.** The common layout is `skills/<name>/SKILL.md` at the repo root, which installers such as `npx skills add owner/repo --skill name` resolve. Offer more than one install command if they apply (installer, plugin marketplace, manual copy), because readers use different tools. SKILL.md frontmatter allows only a small set of keys, so keep discovery copy in the README and site page rather than adding custom fields.

**Claude Code plugins.** A `.claude-plugin/plugin.json` makes the repo a plugin, and a `marketplace.json` makes it an installable marketplace. If the user keeps one marketplace repo for all their skills, add an entry there rather than creating another marketplace.

**MCP servers.** Add the `mcp-server` topic, list the tools the server exposes in the README opening, show the one-line client configuration, and state what credentials it needs and why.
