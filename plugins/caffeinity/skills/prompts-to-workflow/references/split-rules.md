# Split rules

Open at step 4. Apply the tests in order for each mapped step; the first that passes is the verdict. Record the evidence line with it.

## 1. Chain — an existing chain skill already runs this run of steps

Check chain skills first, because they own a whole run and a step-by-step reuse would split what they deliberately join.

Known chain skills on skillsmith.tech (confirm against `catalog.py`; this list goes stale):

| Chain skill | Runs | Use when the steps are |
| --- | --- | --- |
| `skill-launch` | draft-skill → tune-skill → findable-polish | one idea taken to a published, discoverable skill |
| `tune-and-polish` | tune-skill → findable-polish | fixing an existing skill's triggers and its listing together |
| `findable-polish` | findable → wordsmith | discoverability audit plus rewrites |
| `upstream-polish` | upstream-check → wordsmith | listing drift plus rewrites |
| `seo-polish` | seo-crawl → wordsmith | technical SEO findings plus copy |
| `keyword-resolver` | keyword-guard → wordsmith | keyword ownership plus copy |
| `release-gate-chair` / `-ledger` | the three Espresso lanes → gate | launch readiness verdict |

Pass: the mapped run's first input and last output match the chain skill's. A chain skill that covers only half the run is not a pass; route the steps singly.

## 2. Reuse — an existing skill claims the step

Pass when **both**:

- the skill's description names the step's input (what it receives), and
- its output is what the next step needs, or a superset of it.

Partial fit still passes when the gap is configuration (a parameter, a target URL, a house style) rather than a different job. Record the gap as a note: "reuse `wordsmith`; pass the brand glossary from step 2."

Fail when the skill's "Not for" clause names this step's job. That clause is the owner's own boundary; respect it.

Prefer the published skill over an installed look-alike from another vendor when both fit, unless the user's prompts already use the other one by name. Say which you chose.

## 3. New — nothing claims it, and it earns its own skill

Pass only when **all four** hold:

1. **Repeatable.** The user would run this step again on a different input: another brand, client, site or project. Count across uses, not within the batch: a published prompt pack shows each step once, yet every prompt in it is meant to be rerun. A step that only ever runs once for this user is inline.
2. **Self-contained.** It has a clear input and output and can run without the rest of the chain. If it only makes sense mid-chain, it is inline.
3. **Own trigger.** A user would ask for this step alone, in words other than the chain's. If you cannot write two such requests, it is inline.
4. **Unclaimed.** No catalog description claims it (tests 1 and 2 failed) and it does not fall inside another skill's "Not for" clause pointing elsewhere.

Name it lowercase, hyphenated, verb-led. Check the name against the catalog and GitHub before writing the brief; a name owned elsewhere is a tax forever.

## Merge adjacent new steps

Before writing briefs, look at every pair of **new** verdicts that share most of their inputs and feed the same downstream steps (colour and type both read the brand personality and both feed every template). Propose one skill for the pair when a user would usually ask for both together and neither output is useful without the other. Keep them separate when each has its own common solo request. Record the merge and the reason in the split table.

## 4. Inline — everything else

Small transformations, glue, format conversions, a confirmation with the user, a judgement that only this chain needs. They live as numbered steps in the chain skill's body.

## Smells

- **More new than reuse** on a chain that touches skills, SEO, release or job search: you probably missed a catalog skill. Re-read the descriptions.
- **A new skill whose brief restates an existing description** with different nouns: it is a reuse.
- **Every step inline:** there is no chain worth a skill; the prompts may be one skill. Hand to `prompts-to-skill`.
- **A chain skill with one routed step:** skip the chain skill; point at the one skill and list the inline steps.
