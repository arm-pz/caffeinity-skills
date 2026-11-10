# tune-and-ship

Takes one published agent skill at a time from as-is to tuned, fact-checked, released and live, then
moves to the next one in the catalog. Each run hands the audit to `tune-skill` and the listing to
`findable-polish`, and does the parts between and after them itself: checking every version number,
flag, price and command against its primary source, reading the siblings' real SKILL.md files,
writing the version and release notes, opening one PR, and confirming the site page and the
marketplace copy actually changed.

Distilled from the run that took `setup-claude-advisor` from 0.1.1 to 0.1.2;
`references/first-run.md` keeps what each step taught.

```
/plugin marketplace add arm-pz/caffeinity-skills
/plugin install tune-and-ship@caffeinity-skills
```

## Ask it things like

- "Fine-tune my other skills on skillsmith.tech, one by one."
- "Give research-brief the full treatment and get it live."
- "Fact-check the claims in this skill and release the fix."

## Boundaries

- **Handles**: one published skill per run, through to a merged PR and a confirmed live page.
- **Does not handle**: a tune with no release (`tune-skill`), drafts with nothing pushed
  (`tune-and-polish`), a new skill (`skill-launch`), regression upkeep (the Descale brew in
  `caffeinity-routing`), or a whole collection (`skill-estate`).

## Requires

`tune-skill` and `findable-polish` installed. `scripts/queue.py` needs Python 3.9+ and `git`.
