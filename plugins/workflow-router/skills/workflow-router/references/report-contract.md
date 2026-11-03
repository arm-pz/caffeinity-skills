# Brief and report contract

Every workflow run starts with a brief and ends with a report in the shape below. The workflow
agents in the `caffeinity` plugin follow the same contract; `scripts/build_plugin.py` renders it
into each agent.

The point is to keep the user able to stand behind the result, not only to see that it finished.
A polished summary invites a skim. The brief makes the user say what they expect before the
output can shape that expectation, and the report puts the evidence, the decisions taken on the
user's behalf and the blind spots ahead of the summary.

## Before step 1: the brief

Ask for, or confirm from the request, three things, and write them down at the top of the run:

| Field | What it holds | Example (Workflow 3 · launch-safely) |
| --- | --- | --- |
| Expect | What the user thinks the outcome will be. A rough guess is fine; it is there to compare against, not to be right. | "Probably ready, maybe a header or two to fix." |
| Done when | The evidence that ends the run: a script verdict, a passing test, a screenshot, a file at a path. Never "looks done". | "release-gate-chair prints a posture for the staging URL." |
| Out of scope | What this run will not touch. | "The marketing site; only app.example.com." |

- If the request already answers a field, fill it in and show it; do not ask again.
- If the user cannot say what done looks like, ask one or two questions about it before routing.
  A goal that cannot be stated is not ready to hand to a chain of skills, and guessing it fills
  the gap with your assumptions.
- When the user says to skip the brief, or the workflow is cheap to redo, write the fields you
  can infer, mark them `(assumed)`, and go on.
- Do not change the brief after the run has started without saying so in the report.

## During the run: pass the source, not only the summary

Each step receives what the previous step handed on, verbatim, and also the original inputs the
user gave (the URL, the resume, the dataset, the idea). A later step that sees only an earlier
step's digest is checking a summary of a summary.

## After the last step: the report

Four sections, in this order. The summary comes last on purpose.

### 1. Evidence

One line per step: skill, status (done, skipped and why, or stopped at its gate), and the
command it ran or the file it wrote, with the deciding line of its output quoted. A step with no
evidence is reported as planned, not done.

    1 web-preflight        done     verdict.json · "app.example.com: PASS WITH FIXES (2)"
    2 pre-ship-security…   done     report.md · 0 high, 1 medium · untested: OAuth callback
    3 pre-ship-perf…       skipped  no build available; asked the user, not improvised
    4 release-gate-chair   stopped  posture.json · "HOLD: performance lane missing"

### 2. Decisions and assumptions

What the run decided that the user did not: defaults picked, a requirement reinterpreted when two
clashed, an optional step run or skipped, an input that was guessed, anything in the brief marked
`(assumed)`. Write "none" only after checking each step. Each line is a choice the user can
reverse.

### 3. What the checks did not cover

For each green verdict, say what it proved and what it did not. A passing check proves one
property; name the nearby ones it left open, the lanes marked untested, the pages or files not
read, the claims taken from a source without checking it. Then answer, once, "what did this run
miss?" and list what comes back, or "nothing found" if nothing does.

### 4. Summary and next action

Compare the outcome with the brief's "Expect" line in one sentence (as expected, or how it
differed), state whether "Done when" was met, and give the one next action.

## What this contract does not do

It does not replace any step's own gate or verdict. A HOLD is still a HOLD, and a skill's own
report format still applies inside its step; this contract is the layer around the steps.
