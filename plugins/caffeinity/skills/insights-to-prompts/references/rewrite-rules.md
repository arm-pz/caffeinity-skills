# Rewrite rules

Open this when writing the rewrites in step 4.

## Friction → what the prompt was missing

| Friction (facet) | Usual cause in the prompt | Add to the rewrite |
| --- | --- | --- |
| misunderstood_request | Goal stated as a topic, not an outcome ("the auth thing") | One sentence on what must exist or be true when done |
| user_unclear | Several asks blended, or a pronoun with no referent | Split into numbered asks; name files/functions instead of "it", "this" |
| wrong_approach | Method left open where you had a preference | The approach to use, or the one to avoid and why |
| excessive_changes | No scope fence | "Only touch X. Don't refactor, rename or add deps." |
| wrong_file_or_location | Location implied, not named | Exact path, symbol or section |
| user_rejected_action | Claude acted when you wanted a plan, or ran a command you didn't want | "Propose first, wait for OK" or list the allowed commands |

Skip, and list under "not a prompt problem": tool_failed, external_issue, claude_got_blocked, slow_or_verbose, and buggy_code unless the friction_detail shows the spec itself was wrong.

## Signals that the fix is a CLAUDE.md rule, not a rewrite

- The same correction appears in follow-ups across 2+ sessions ("use pnpm", "don't touch tests").
- The report's CLAUDE.md suggestions section already names it.
- It is a project fact, not a property of this one ask.

Send these to harness-audit with the evidence; don't repeat them in every prompt.

## Using follow_ups

The digest keeps the first few follow-up messages. A follow-up that corrects Claude ("no, I meant…", "only the…", "stop") is the clearest statement of what the original prompt lacked — build the rewrite from it.

## Output block (one per rewrite)

    ### <short name for the pattern>
    **Evidence:** <friction types> in <n> session(s) — <one friction_detail, paraphrased>
    **Before:** > <original, first ~200 chars>
    **After:**  > <rewrite>
    **What changed:** <one line>

Keep the rewrite within about 2x the original length. If it needs more, the extra probably belongs in CLAUDE.md or a slash command.

## Repeated openers without friction

These aren't rewrites. List them as slash-command candidates with a suggested name and the parameter that varies.
