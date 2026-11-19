# First real hand-off: tests for worker_diff.py

Run on 2026-11-17 with opus-playbook 0.2.0. The lead was Fable in a Claude Code cloud session.
The worker was an Opus subagent. The task was real work on this repository: `worker_diff.py`
had shipped with no tests.

## Record

```
Worker:      opus (served: claude-opus-5-5, read from the model field of the worker's transcript, 15 of 15 turns)
Brief:       add a unittest suite for scripts/worker_diff.py that would catch a broken detection
Enforced:    isolated git worktree on its own branch; model set on the spawn call
             Left to the brief: no push, no edits outside tests/, stop rule (tool limits were not available for this agent type)
Done when:   suite passes from the repo root            -> ran it myself: 14 tests, OK          -> pass
             one test per behaviour a to g              -> read all 252 lines of the diff       -> pass
             only new files are under tests/            -> worker_diff.py against start commit  -> pass (1 file, tests/test_worker_diff.py)
             worker_diff.py byte-for-byte unchanged     -> sha256 before and after              -> pass
Changed:     tests/test_worker_diff.py   Unmentioned: none   Tests edited: no existing tests; 36 assertion lines added
Cited facts: two script bugs reported -> reproduced both in a scratch repository -> both real
Unbriefed probe: broke the script eleven ways, one detection at a time -> the suite failed all eleven times
Irreversible actions: none; the remote head was unchanged after the run
Not checked: nothing in the brief was left unchecked
Decision:    GO
Exit:        none needed; the worker's commit was fast-forwarded into main by the lead
```

## What the worker did with the stop rule

The brief said: if the script is wrong, keep the failing test and report the bug; do not change
the script and do not weaken a test to get green. The worker found two bugs outside the listed
behaviours, changed nothing, and reported both with inputs and outputs:

1. A changed line whose own text starts with `-- ` or `++ ` was read as a diff file header and
   dropped, so it was invisible to every detection.
2. The "unmentioned" check was a substring match, so a report naming `data.py` also counted
   `a.py` as mentioned.

Both were fixed by the lead in 0.2.1, with five regression tests.

## What the run changed in the skill

- The script flagged seven lines in the new test file. All seven were fixture strings such as
  `"# TODO: handle the empty case"`. Step 2 now says hits are leads and each one is read.
- The runtime's built-in worktree isolation failed to start, so the lead made the worktree by
  hand. The enforcement table already listed that as an equal option.
- Tool limits could not be set for this agent type, so "no push" was left to the brief and
  verified afterwards against the remote. The record now shows which terms were enforced and
  which were only asked for.
- For a task whose deliverable is tests, the held-back probe was to break the code under test.
  Step 8 now says so.
- The bugs came back because the brief asked for "anything that looked wrong". That phrase is
  now in the example for part 6 of the brief.

## Limits of this run

One task, one worker, a small repository, and work that turned out to be good. It shows the
ladder runs end to end and that the go path works. It does not show a no-go: the return, take
over and escalate exits have not been exercised on real work.
