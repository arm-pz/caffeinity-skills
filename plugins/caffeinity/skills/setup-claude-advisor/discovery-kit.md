# Discovery Kit: `setup-claude-advisor`

## 0. Baseline (Audit findings)

- **Name search**: Exact-name free and topic-free on GitHub prior to publication (no prior collisions or competing same-name repos).
- **Task search**: Related repositories (`claude-code-advisor`, `claude-tiers`, `claude-model-guard`) focus on external API routing, adversarial testing, or single-classifier selection, but none automate persistent native Claude Code model tiering and subagent configuration.
- **Re-audit, 2026-11-10 (findable-polish pass)**: GitHub repository search, 0 stars on this repo.
  - `claude code opus advisor` returns 25 repos, led by `shalomeir/advisor-opus`, `vzwjustin/advisor`, `PUSHINGSQUARES/advisor-driven-dev` and `Divinci-AI/opus-advisor-mcp`. Most add a plugin, an MCP server or their own orchestration. None of the top results configures the built-in advisor tool through `settings.json`, so that is the differentiator the listing now leads with.
  - `advisorModel` and `claude code sonnet opus advisor settings` return 0 repos. Both are open, and the README and About text now carry those words.
  - `claude code haiku subagents` (110) and `claude code model tiering` (313) are crowded by orchestrators and router hooks with 100+ stars; this repo will not rank there on those words alone.
  - The live About text still read "Opus on call via /advisor", wording that v0.1.1 corrected everywhere else.
- **Initial metadata state**: Empty homepage, missing topics, unreleased v0.1.0 tag, missing license. Now resolved with MIT license, 13 curated topics, and v0.1.0 release.

---

## 1. Target queries

Queries strangers search when experiencing quota limits or setting up subagents in Claude Code:

1. `claude code opus advisor`
2. `claude code save quota 20 plan`
3. `claude code model tiering sonnet opus haiku`
4. `claude code advisor prompt rule`
5. `claude code haiku subagents`
6. `claude code reduce token burn`
7. `claude code advisor pattern settings`
8. `advisorModel settings.json`
9. `claude code built-in advisor tool setup`
10. `claude pro plan opus default usage limit`

---

## 2. Name decision

- **Chosen Name**: `setup-claude-advisor`
- **Rationale**: Lowercase, verb-led, exact-name-free and topic-free on GitHub. Clearly indicates configuration action rather than a runtime wrapper or proxy.

---

## 3. GitHub listing: About, homepage, topics

**About (description, 350 character limit):**

```
Agent skill that sets up Claude Code's built-in advisor tool: Sonnet as the main model, Opus as advisor (advisorModel in settings.json), Haiku for read-only subagents. No plugin, MCP server or proxy. Audits version and env flags, shows a diff preview, and writes nothing without approval.
```

Alternatives considered (2026-11-10):

- **A, chosen above**: leads with the built-in advisor tool and `advisorModel`, the two things no competing listing says.
- **B**: "Make a Claude Pro plan last longer in Claude Code: an agent skill that puts Sonnet on the work, Opus on call through the built-in advisor tool, and Haiku on read-only subagents. Edits settings.json only after you approve a diff preview." Leads with the outcome; weaker on the exact-match terms.
- **C**: the previous text with "via the advisor tool". Smallest change, but keeps "quota-optimised model tiering", a phrase nobody searches.

**Topics:** `agent-skills`, `claude-code`, `claude-code-plugin`, `claude-code-skills`, `claude-code-subagents`, `advisor-tool`, `opus-advisor`, `model-tiering`, `quota-optimization`, `token-optimization`, `claude-pro`, `subagents`, `anthropic`, `skillsmith`

Dropped `sonnet`, `opus` and `haiku`: bare model names are crowded and say nothing about what the repo does. Added `advisor-tool`, `claude-code-subagents`, `token-optimization` and `claude-pro`.

**Homepage:** `https://skillsmith.tech/setup-claude-advisor/`

---

## 4. README opening

```markdown
# setup-claude-advisor

An agent skill that sets up Claude Code's built-in advisor tool: Sonnet does the work, Opus advises at three decision points, and Haiku handles read-only subagents. It writes `model` and `advisorModel` to `settings.json`, with no plugin, MCP server or proxy, and shows every change as a diff preview before touching any file.

Built for Claude Pro ($20) users whose Claude Code sessions now default to Opus and who want their usage limit to last longer.

```bash
npx skills add arm-pz/setup-claude-advisor --skill setup-claude-advisor
```

### Ask it things like

- "Set up my Claude Code to use Sonnet as main and Opus as advisor"
- "Configure Claude Code with the Opus advisor pattern to save quota"
- "Match this subagent tree: Haiku for readers, Sonnet for editors, Opus advises"

### Boundaries

- **Handles**: Persistent Claude Code model tiering configuration (settings.json, subagent files, CLAUDE.md advisory rule).
- **Does not handle**: Post-mortem usage diagnosis (use `diagnose-usage`), per-task effort level sliders (use `choose-effort`), or CLI binary upgrades.
```

---

## 5. Release notes

### v0.1.0

Configures Claude Code for quota-optimised model tiering: Sonnet main session, Opus on-call strategic advisor (advisor tool), Haiku for read-only doc/search subagents, and Sonnet for code-editing subagents.

- **Pre-flight diagnostics**: Checks version (>= 2.1.293), environment flags (`CLAUDE_CODE_DISABLE_ADVISOR_TOOL`, `DISABLE_TELEMETRY`, `CLAUDE_CODE_SUBAGENT_MODEL_FORCE`), and existing subagents.
- **Diff preview safety**: Shows all proposed changes to `settings.json`, `CLAUDE.md`, and subagent configs in one diff block before touching any files.
- **Advisory protocol**: Adds 3 decision-gate moments to `CLAUDE.md` (before committing to a plan, when an error recurs, before declaring done).

### v0.1.1

Corrects how the advisor is consulted and launched.

- **Advisor wording**: consultation happens through the `advisor` tool. `/advisor` only shows or switches the advisor model.
- **Launch**: plain `claude` with `model` and `advisorModel` in `settings.json` is the primary path; `--advisor opus` is documented as a working flag that `claude --help` does not list.
- **Handoffs**: says what to do when `diagnose-usage` or `choose-effort` is not installed.

### v0.1.2

Tuning pass with facts checked against the Claude Code changelog and advisor docs.

- **Safe to re-run**: an existing `## Advisor protocol` section in `CLAUDE.md` is replaced, not duplicated.
- **Clearer rules**: "write only on approval" replaces a ground rule that contradicted the Apply step; pasted trees and existing config files are treated as data.
- **Checked facts**: the quota multiplier claim is replaced by the published API price ratio; `DISABLE_TELEMETRY` and third-party providers (Bedrock, Vertex, Foundry) are reported as turning the advisor off.
- **Boundaries**: plan limits and prices go to `product-self-knowledge`; triggers catch requests that never say "advisor" or "tiering".

---

## 6. Site page

Live on Skillsmith:
- Canonical URL: `https://skillsmith.tech/setup-claude-advisor/`
- Hub listing: `https://skillsmith.tech/skills/`
- Discovery index: `https://skillsmith.tech/.well-known/skills.json`

---

## 7. Distribution list with entry text

| Surface | Target / Channel | Entry format | Status |
|---|---|---|---|
| **Skillsmith Hub** | `skillsmith.tech` | Automated repo ingestion via CI | Active |
| **Claude Marketplace** | `arm-pz/caffeinity-skills` | `.claude-plugin/marketplace.json` | Published |
| **Agent Skills Index** | `skills.sh` / `npx skills` | Public GitHub repo discovery | Ready (`npx skills add arm-pz/setup-claude-advisor`) |
| **Community Forums** | r/ClaudeAI / Discord | Educational tip + advisor tree walkthrough | Optional |

---

## 8. Apply commands

Applied commands:

```bash
gh repo edit arm-pz/setup-claude-advisor \
  --description "Agent skill that sets up Claude Code's built-in advisor tool: Sonnet as the main model, Opus as advisor (advisorModel in settings.json), Haiku for read-only subagents. No plugin, MCP server or proxy. Audits version and env flags, shows a diff preview, and writes nothing without approval." \
  --homepage "https://skillsmith.tech/setup-claude-advisor/" \
  --add-topic agent-skills,claude-code,claude-code-plugin,claude-code-skills,claude-code-subagents,advisor-tool,opus-advisor,model-tiering,quota-optimization,token-optimization,claude-pro,subagents,anthropic,skillsmith

gh release create v0.1.0 --repo arm-pz/setup-claude-advisor --title "v0.1.0" --notes-file release-notes.md
```

Pending as of 2026-11-10:

- Only the `v0.1.0` tag exists. Tag and release `v0.1.1` (merge commit of the advisor wording fix) and `v0.1.2` (after its pull request merges), using the notes in section 5.
- The live About text still reads "Opus on call via /advisor", and the live topics are the old set. Re-run the `gh repo edit` command above to apply the new About text and add the new topics, then remove the three dropped ones:

```bash
gh repo edit arm-pz/setup-claude-advisor --remove-topic sonnet,opus,haiku
```

```bash
gh release create v0.1.1 --repo arm-pz/setup-claude-advisor --target 1218642 --title "v0.1.1" --notes-file release-notes-0.1.1.md
```

```bash
gh release create v0.1.2 --repo arm-pz/setup-claude-advisor --title "v0.1.2" --notes-file release-notes-0.1.2.md
```

---

## 9. Re-check plan

- **Target date**: 2026-11-29 (3 weeks post-release).
- **Check items**:
  1. Re-run `gh search repos "claude code advisor"` to check ranking progress.
  2. Inspect Google / GitHub search index for `setup-claude-advisor` queries.
  3. Verify `skills.sh` / `npx skills` install resolution on a fresh environment.
