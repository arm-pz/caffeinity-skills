# Discovery kit: `opus-playbook`

Drafted on 2026-11-17 by a tune-and-polish pass (tune-skill, then findable-polish). Nothing in
sections 3 to 5 has been applied. The apply commands are in section 8.

## 0. Baseline

- **Repo metadata (GitHub search API, 2026-11-17):** About empty, no topics, no homepage, 0
  stars, no release. MIT licence present. The skills-site sync holds any repo with an empty
  About, so the skill is not on skillsmith.tech.
- **Name search:** no repository is named exactly `opus-playbook` and no topic uses the name.
  Five repositories have close names; all are guides to prompting or configuring Opus. The
  largest is `rennf93/opus-fable-playbook` (34 stars), which makes Opus behave like Fable.
- **Task search, GitHub repositories:**
  - `verify subagent work skill`: 29 results. Top: `float1122/sub-agent-forced` (4 stars, an
    orchestrator that verifies by hand), `rellyholdem/fable-runner` (3, verifies Fable
    background subagents and catches silent Opus fallback).
  - `delegate subagent review claude skill`: 10 results. Top: `pvjbuilds/delegate-router` (42,
    routes tasks to another model).
  - `orchestrator worker verification agent skill`: 9 results. Top: `maxtechera/orchestrator`
    (2, dispatch workers and run independent checks).
  - This repo appears in none of them. The field is small and low-starred; nothing found pairs
    a checkable brief with an explicit go/no-go.
- **Not done:** no web search outside GitHub, and no directory listings were checked.

## 1. Target queries

1. `verify subagent work claude code`
2. `check what a subagent did before merging`
3. `claude code subagent says tests pass but they fail`
4. `delegate to opus and verify result`
5. `lead model worker model verification skill`
6. `subagent brief template acceptance criteria`
7. `go no-go checklist ai agent output`
8. `detect agent weakened tests to pass`
9. `orchestrator worker agent skill SKILL.md`

## 2. Name decision

Open, and the owner's to make. The name has no exact collision, but every close name is a
prompting guide, and query 4 is the only target query that contains "opus". Keeping the name
means qualifying it on every surface, which the drafts below do. `check-the-worker` was offered
earlier as a model-neutral alternative; renaming is cheapest while the repo has 0 stars.

## 3. GitHub listing

Three options were drafted. Option B is the one in the validated block below.

- **Option A (role first):** Agent skill for a lead model that delegates to subagents. It decides whether a task is safe to hand off, writes a checkable brief, enforces scope and tool limits, then verifies the worker's diff and gives a go or no-go with evidence. Written for Fable leading Opus in Claude Code; works in any agent that loads a SKILL.md.
- **Option B (task first):** see below.
- **Option C (short):** Subagent verification playbook as an agent skill. Hand-off tests, a checkable brief, enforcement rules, a diff inventory script and a go/no-go list, so a lead model does not relay "done" it has not checked. Not a prompting guide for Opus.

Best: B. It opens with the words of queries 1 and 2, names the pieces a visitor gets, and
ends with the disambiguation.

**About (description, 350 character limit):**

```
Verify what a subagent says it did before you relay or ship it. Agent skill for a lead model (Fable leading Opus, or any orchestrator and worker): checkable brief, enforcement rules, a nine-step check ladder, a diff inventory script and an explicit go/no-go. For Claude Code and any agent that loads a SKILL.md. Not an Opus prompting guide.
```

**Topics:** `agent-skills`, `claude-code`, `claude-skills`, `claude-code-skills`, `subagents`, `multi-agent`, `agent-orchestration`, `ai-agents`, `verification`

Repository counts on 2026-11-17: agent-skills 44,220; claude-code 121,495; claude-skills
16,405; claude-code-skills 2,814; subagents 2,015; multi-agent 23,601; agent-orchestration
5,205; ai-agents 154,960; verification 5,965. Nine topics, all counted; `llm-evaluation` was
counted (10,620) and left out because the skill does not evaluate models.

**Homepage:** `https://skillsmith.tech/opus-playbook/` once the sync has published the page.
Leave it empty until that URL resolves.

## 4. README opening

The current opening describes the lead's four jobs but does not use the words people search
("verify", "subagent says", "tests pass"), and its disambiguation sits far down the page.

**Option A (recommended):**

```markdown
# opus-playbook

An agent skill for verifying what a subagent says it did. It is for a lead model that
delegates work, Fable leading Opus in the usual setup, and it works for any orchestrator and
worker. The lead decides whether a task is safe to hand off, writes a brief that can be
checked, enforces its terms, runs a nine-step check on what comes back, and calls go or no-go
with the evidence. It never relays "done" on the worker's word.

    npx skills add arm-pz/opus-playbook

Ask it things like:

- "Hand this fix to Opus and make sure it actually did it before we merge."
- "The subagent says the tests pass. Is that true?"
- "If you give this to Opus, how will you check it, and what is your go/no-go?"

This is not a guide to prompting Opus. Repositories with similar names, such as
`opus-fable-playbook`, are prompting and configuration guides and are unrelated.

Related skills: `consistent-code-review` reviews code for defects, `setup-claude-advisor` sets
which model takes which role, and `choose-effort` picks effort and fan-out. This one checks a
delegated result against its brief.
```

**Option B (shorter, problem first):**

```markdown
# opus-playbook

Subagents report "done, tests pass" and the lead model passes it on. This agent skill makes the
lead check first: a brief with testable conditions, enforced scope and tool limits, a
diff inventory script, and a go/no-go list. Written for Fable leading Opus; works for any
orchestrator and worker in Claude Code or any agent that loads a SKILL.md.

    npx skills add arm-pz/opus-playbook
```

Best: A. It carries queries 1, 2, 3 and 7, the install line, example prompts, the
disambiguation and the sibling line that the listing guide asks for. B is the fallback if the
opening should stay under ten lines.

## 5. Release notes

No release exists. Draft for `v0.2.1`:

```
opus-playbook 0.2.1

An agent skill for a lead model that delegates work to Opus or any subagent.

- SKILL.md: hand-off tests, six-part brief, enforcement table, nine-step check ladder,
  go and automatic no-go lists, record template
- scripts/worker_diff.py: inventory of a worker's changes, with 19 unit tests
- runs/: the record of the first real hand-off (Fable leading Opus), decision go

Install: npx skills add arm-pz/opus-playbook
```

## 6. Site page

None drafted. The page at skillsmith.tech is generated from this repository by the skills-site
sync once the About is set. Its `tested` field can then point to
`runs/2026-11-17-first-hand-off.md` in this repo as evidence.

## 7. Distribution

- **skillsmith.tech:** automatic within the hour once the About is non-empty.
- **`caffeinity` plugin bundle:** PROJECT.md in skills-site says it is rebuilt hourly from every
  skill repo. Not verified for this repo.
- **Other directories:** not searched in this pass. No claim is made about any of them.

## 8. Apply commands

These change public pages. Run them only if you agree with the drafts.

```bash
gh repo edit arm-pz/opus-playbook \
  --description "Verify what a subagent says it did before you relay or ship it. Agent skill for a lead model (Fable leading Opus, or any orchestrator and worker): checkable brief, enforcement rules, a nine-step check ladder, a diff inventory script and an explicit go/no-go. For Claude Code and any agent that loads a SKILL.md. Not an Opus prompting guide." \
  --add-topic agent-skills,claude-code,claude-skills,claude-code-skills,subagents,multi-agent,agent-orchestration,ai-agents,verification

gh release create v0.2.1 --title "v0.2.1" --notes-file release-notes.txt
```

The README opening is a file change: replace everything above `## Install` in `README.md` with
Option A.

## 9. Re-check plan

On 2026-12-08, re-run the three GitHub task searches in section 0 and target queries 1, 2 and
4, and record whether this repo appears and where. Compare stars and the About text with this
baseline. Indexing lags, so an earlier check proves little.
