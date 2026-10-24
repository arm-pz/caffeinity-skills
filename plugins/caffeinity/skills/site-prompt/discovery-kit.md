# Discovery kit: site-prompt

Prepared 2026-10-22 with the findable skill. Every claim below was checked in this pass or is marked as unverified.

## 0. Baseline

`arm-pz/site-prompt` is public, has no README, license, topics or release, and 0 stars. It is not indexed for any task query checked.

| Query (where checked) | Project found? | What ranks instead | Where those are listed |
|---|---|---|---|
| `site-prompt` — GitHub repo search | No, not in the top 15 | Unrelated empty repos: `mugadaszk/site-prompt`, `HuQyang/site_prompt`, `Shadow-Dev1/Site-Prompt`, plus prompt-sharing sites | GitHub only, no directories |
| `site prompt` — GitHub repo search | Yes, 6th | `xNewt0/SitePrompter`, `Unar92/SitePrompt-Lab` | GitHub |
| `website build prompt skill` — GitHub | No matches | — | — |
| `mega prompt website generator` — GitHub | No matches | — | — |
| `one-shot website skill` — GitHub | No matches | — | — |
| `verified website prompt` — GitHub | No matches | — | — |
| "one-shot AI websites" — web | No | `codeswithroh/tastemaker`, Taste Skill (`tasteskill.dev`), `ParthPipermintwala/prompt2site` | GitHub, Reddit, Instagram, YouTube, SkillsLLM, directory reviews |
| "SELENE" website prompt — web | No | `seline`, an unrelated desktop agent app on SkillsLLM | SkillsLLM |

Metadata gaps found: description present but README, license, topics, release and homepage all absent. `npx skills add arm-pz/site-prompt --list` resolves the repo and reports one skill, so installation by owner/repo already works; search discovery does not.

## 1. Target queries

A stranger would type these by task, not by name:

1. website build prompt agent skill
2. one-shot website prompt
3. landing page prompt with full source code
4. prompt to rebuild a website exactly
5. website prompt with complete source code
6. make a website prompt from a topic
7. SELENE-style website prompt
8. agent skill that writes website prompts
9. verified website build prompt
10. replay-tested website prompt

Numbers 1, 2, 6 and 7 were checked in this pass; 3, 4, 5, 8, 9 and 10 are the queries the About and README are written for and were not run.

## 2. Name decision

**Keep `site-prompt`, qualified everywhere.**

- There is no direct competitor under the name; the same-name repos are empty or off-topic.
- `SitePrompter` is adjacent but reverses the job: it turns a site into a prompt. The README and the site page say so.
- Tastemaker, Taste Skill, MotionVault and `prompt2site` compete for the same searches but make different artifacts: taste/reference grounding, animation prompts, or a generator app. None claims complete source plus a byte-for-byte replay.
- Renaming would lose the installed name and the repo URL for no measured gain. The About text, README and topics carry the task words; the name stays owner-qualified.

## 3. GitHub listing

**About (description, 350 character limit):**

```
Agent skill that turns a website topic or landing-page brief into one self-contained build prompt: subject-native concept, final copy, every source file embedded verbatim, and a replay check that compares the rebuilt tree byte for byte. Portable SKILL.md; tested in Qoder.
```

**Topics:** `agent-skill`, `agent-skills`, `claude-code`, `claude-skills`, `codex`, `frontend-design`, `landing-page`, `prompt-engineering`, `prompt-library`, `qoder`, `static-site`, `web-design`

Homepage: leave empty. There is no live page for this skill. The draft in `discovery/site-page.md` is not deployed.

Social preview brief: 1280×640, ink background (`#061014`), one orange rule, the wordmark `site-prompt`, the line "verified one-shot website build prompts", and the install command in monospace. Not produced.

## 4. README opening

> # site-prompt
>
> An agent skill that turns a website topic into one self-contained, paste-and-build prompt. Give it "cargo ship", "a ferry between Athens and the Cyclades" or "a marine insurance broker", and it returns one markdown file with the concept, final copy, complete source for every file, and the checks that were actually run — enough for a fresh agent to rebuild the site without seeing the session that produced it.
>
> It does not stop at an outline or a list of sections. It narrows a category to one concrete subject, derives the page from that subject's world, builds and verifies the site in a scratch folder first, then embeds each file verbatim under a `## File:` heading. The included replay verifier materialises the prompt into a clean directory and compares it against the built site, so "complete source" is tested rather than claimed.
>
> ```
> npx skills add arm-pz/site-prompt --skill site-prompt
> ```
>
> The name is shared with several unrelated, empty repositories. This is the agent skill from arm-pz. `SitePrompter` goes in the opposite direction — it turns a site into a prompt.
>
> Sibling: tune-skill audits a skill that already exists; this skill produces a website prompt.

The full file is `README.md`.

## 5. Release notes

```
v0.1.0 — first release

An agent skill that produces one self-contained website build prompt from a
topic: subject brief and swap test, smallest-stack choice, a real scratch
build, browser verification, every text file embedded verbatim under a
## File: heading, and an Assets section for anything that is not text.

Includes:
- SKILL.md with the workflow and the two gates (swap test, replay check)
- references/ for the subject brief, stack presets, prompt format and verification
- scripts/replay-prompt.mjs: --list, --out, --check, path guards, CRLF normalisation
- 14 recorded replay-verifier cases

Verified: SELENE, 21 files, 21/21 replay match; Northline / Rotation 7E,
a concept container line, 4 files, 4/4 replay match.

Install:
npx skills add arm-pz/site-prompt --skill site-prompt
```

## 6. Site page

Draft at `discovery/site-page.md`, ready for the skills site when a page is wanted. Not deployed. Do not set the GitHub homepage until it is live.

## 7. Distribution list

| Surface | Fit | Effort | Expected value | Status |
|---|---|---|---|---|
| GitHub About, topics, README, license | Every search and directory reads them | Minutes | The baseline fix; nothing else works without it | Apply now |
| `v0.1.0` release | GitHub search and listings that read releases | Minutes | Removes the "unfinished" signal | Apply now |
| `npx skills add` resolution | Installers | None | Already resolves one skill | Verified this pass |
| skills.sh index | Large skill registry | None known | Possible install-time discovery; indexing rules and telemetry behaviour were not verified | Do not claim a listing |
| skills site page | The user's own domain | Needs the site's page format | One owned surface and a GitHub homepage target | Deferred; draft only |
| awesome-agent-skills lists | Curated GitHub traffic | PR per list | Unverified; rules not read in this pass | Not attempted |
| Community post | Reddit / X / LinkedIn | High, one shot | Needs a real before-and-after; credibility cost if generic | Not planned |

No directory was submitted in this pass. Nothing here claims the project is listed anywhere beyond GitHub.

## 8. Apply commands

```bash
cd ~/.qoder/skills/site-prompt
git add README.md LICENSE discovery-kit.md discovery/site-page.md
git commit -m "Add README, license and discovery kit"
git push origin main

gh repo edit arm-pz/site-prompt \
  --description "Agent skill that turns a website topic or landing-page brief into one self-contained build prompt: subject-native concept, final copy, every source file embedded verbatim, and a replay check that compares the rebuilt tree byte for byte. Portable SKILL.md; tested in Qoder." \
  --add-topic agent-skill,agent-skills,claude-code,claude-skills,codex,frontend-design,landing-page,prompt-engineering,prompt-library,qoder,static-site,web-design

gh release create v0.1.0 \
  --title "v0.1.0" \
  --notes "$(cat <<'EOF'
v0.1.0 — first release

An agent skill that produces one self-contained website build prompt from a
topic: subject brief and swap test, smallest-stack choice, a real scratch
build, browser verification, every text file embedded verbatim under a
## File: heading, and an Assets section for anything that is not text.

Includes SKILL.md, four references, scripts/replay-prompt.mjs and 14 recorded
replay-verifier cases. Verified on SELENE (21 files, 21/21) and Northline /
Rotation 7E, a concept container line (4 files, 4/4).

Install:
npx skills add arm-pz/site-prompt --skill site-prompt
EOF
)"
```

## 9. Re-check plan

Re-run on **2026-11-12** (three weeks out), from the same queries and the same search engine, and record:

- position of `arm-pz/site-prompt` for queries 1–10, or "absent";
- `gh repo view arm-pz/site-prompt --json description,repositoryTopics,latestRelease,licenseInfo,stargazerCount`;
- whether skills.sh surfaces the repo, and the install count if one is shown;
- GitHub Traffic → referring sites, if a page links it;
- any issues or forks, which are stronger than stars.

Indexing lags. One check immediately after publishing proves little; compare the two dates.
