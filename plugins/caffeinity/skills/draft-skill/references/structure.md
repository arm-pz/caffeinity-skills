# Structure and naming reference

Two jobs: reading a name collision (step 5), and the checks `check_skill.py` cannot make (step 7).

## Reading a collision

Searching GitHub matches repo names and topics, not prose. So a name's position is mostly decided before you write a description.

Run, in this order:

```
gh api "search/repositories?q=<name>+in:name&per_page=10" --jq '.total_count, (.items[] | [.full_name, .stargazers_count, .description] | @tsv)'
gh api "search/repositories?q=topic:<name>&per_page=1" --jq .total_count
```

Then read the result:

- **Exact-name-free and topic-free.** Take it. Nothing ranks above you and no one else owns the phrase.
- **Fuzzy hits only** (compound names like `opencode-<name>`, or unrelated matches on one word). Fine — but qualify the repo description with what the thing is, because search will show you next to strangers.
- **A same-name repo with real stars doing something else.** This is the expensive case. You will rank below it for every search of your own name, and people will land on the wrong project. Note the star counts and the other project's purpose, then bring the user two options: keep the name and qualify it everywhere (repo description, README opening, site page), or rename while the repo has near-zero stars, which is the cheapest it will ever be. **The user decides.** Do not pick silently.
- **A same-name repo doing the same job.** Say so plainly and stop. Duplicating an established skill is a worse outcome than tuning one that exists.

`github.com/topics/<name>` returns HTTP 200 and a plausible page for names that do not exist, so opening the URL proves nothing. Only the `topic:` search count above is evidence.

Record the numbers you actually got. A collision report with invented star counts is worse than no report.

## Checks the script cannot make

`check_skill.py` covers frontmatter shape, name hygiene, description length, H1, body length and dangling file pointers. These are its blind spots, in the order they bite:

1. **Does the body keep the description's promise?** Every verb in the description must be performed by a numbered step. A description that says "and writes test cases" with no step that writes them will trigger correctly and then do something else — the worst failure mode, because nothing errors.
2. **Is the trigger language the user's?** Re-read the requests from step 1. Would each one match the description as written, or only because you know the skill exists? Rewrite the phrase, not the grammar.
3. **Is the boundary real in both directions?** The "Not for" clause names a sibling. Confirm that sibling's own description does not claim this skill's job back. Two skills that each defer to the other, or each claim the other, both lose.
4. **Would this pass without the description?** A skill whose steps are obvious to the agent is a list of sentences costing tokens on every run. Delete what the agent already knows; keep what it would get wrong.
5. **Is anything untested claiming to work?** A `scripts/` file that has never been run, an example output the skill never produced, an install command for an agent you have not installed on. Either run it, or label it as unverified.
6. **Do the references get opened?** Every file in `references/` must be pointed at by a line saying *when* to read it. A reference the body never routes to is dead weight that inflates the folder.
7. **Is the handoff a shape, not a wish?** If the skill hands work to a sibling, say what the sibling receives (a list of findings, a validated folder, a kit file). "Use tune-skill next" transfers no context.

Fix 1 through 3 before polishing prose. They are the ones that change whether the skill fires and does the right thing.
