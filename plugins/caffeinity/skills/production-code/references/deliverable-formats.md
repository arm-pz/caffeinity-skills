# Deliverable formats

The shape per mode. Every mode ends with the blocks in SKILL.md: Run it, The code, Section map, Verification report. This file says what to read first, what differs in the shape, and the failure each mode tends to make.

SPEC GAP: the spec names the modes this file covers but leaves out plain script writing, which is the first item in the source list and a row in the modes table, so `write` is documented here first and the rest follow.

## `write`: a script for a described task

Read first: the runtime version on the machine, any existing file that will call this one, the input format from a real sample.

Shape: one file unless the task genuinely needs more. Entry point at the bottom, arguments parsed at the top, work in named functions, errors caught at the boundary with a message that says what to do next. Non-zero exit on failure. No writes outside the paths the user named.

Tends to fail by: solving a slightly different problem than asked, or growing a framework where a script was wanted.

## `fix`: an error, a traceback, wrong output

Read first: the whole traceback, not the last line; the code at the raising frame; the data that reached it. Reproduce before patching: run the failing command, or write the smallest test that fails the same way.

Shape: root cause in two sentences, then the patch as a diff or the replaced function, then the check that keeps it from returning, then the verification report showing the failure and the pass. If you could not reproduce it, say so and mark the fix as a hypothesis with the run that would confirm it.

Tends to fail by: wrapping the crash in a `try` and calling it fixed.

## `review`: code or a diff judged

Read first: the diff in context, the surrounding file, the tests that cover it, the calling code.

Shape: findings ranked by real impact, each as `file:line`, what breaks, the smallest change. Correctness and data loss first, then security, then performance, then clarity. A line for what you checked and found sound. If nothing is wrong, write that and stop.

Tends to fail by: inventing risks to look thorough, or reviewing style when the question was about behaviour.

## `integrate`: two tools that must talk

Read first: the current API docs you fetched in the session, the auth model, the rate limits, the webhook payload sample, the existing HTTP client in the repo.

Shape: a client module with credential handling from the environment, timeouts set explicitly, retries with backoff only on retryable statuses, paging handled, the response narrowed to the fields used, and one test that runs without the network against a recorded fixture. State the API version. Anything you did not verify against live docs is `[unverified]`.

Tends to fail by: silently dropping a failed call, or trusting a webhook signature that was never verified.

## `query`: SQL

Read first: the real schema, indexes that exist, row counts, the engine and version.

Shape: the statement, then plain-English reasoning: what it scans, the complexity it implies, which index serves it and whether one is missing, what the write cost is. Give the count check for anything that mutates. If you can reach the database, run it read-only and report the actual numbers; if not, report the plan you could not obtain.

Tends to fail by: recommending an index the schema does not have, or timing claims with no measurement.

## `automate`: a repeated manual task

Read first: the steps the user does today, where the input arrives, what should happen when a run fails.

Shape: an idempotent job (a second run must be safe), a lock or state file so runs do not overlap, a log line per meaningful step, one clear failure signal, and the schedule entry (cron, systemd timer, task scheduler) for the user's actual OS. Separate the dry-run path from the live one and make dry run the default when it writes anywhere.

Tends to fail by: assuming the last run succeeded because it did not crash.

## `collect`: data held on web pages

Read first: robots.txt, the site's terms, whether an official API or a bulk export exists, and the user's authorisation to collect. Say plainly what you found, quoting the relevant term.

Shape: polite by default (a delay between requests, a stated identity, caching, resume, a hard cap on requests), parses the response rather than scraping a rendered browser unless needed, and stores to a file the user chose. When the terms forbid collection, or the only way through is evasion, stop and return the decision to the user with the reason.

Tends to fail by: treating a login wall or a block as an obstacle to code around.

SPEC GAP: the source prompt lists "web scraping ... with anti detection" as a capability. That is not carried over: the mode is named `collect`, authorisation comes before code, and no evasion or user-agent rotation is offered.

## `analyse`: a file that must be crunched

Read first: the real file. Row count, column names, dtype per column, missing values, duplicates. Never describe a dataset from its name.

Shape: load, clean with the rules printed, one transformation per named step, the output as a table the user can check, and the numbers that back each line. Report n, and for any comparison the spread as well as the centre. Hand the ranked business readout to `data-readout`; you deliver the code and its output.

Tends to fail by: reporting a conclusion the sample size cannot carry.

SPEC GAP: the source prompt calls this "data analysis" and asks for insights leadership acts on. The mode is named `analyse` because the deliverable here is the crunching code; the ranked readout is `data-readout`'s.

## `document`: code nobody can follow

Read first: the code as it is, the tests, the real config, the deploy target.

Shape: what it is for, install and run, configuration by name, the behaviour a caller can rely on, an example that matches the actual signature, errors and what they mean, and what is not supported. Write for the person who has to run it at two in the morning. Keep it accurate to the code in front of you, not to the version the user remembers.

Tends to fail by: documenting an API that no longer exists, or pasting a secret from the config into an example.

## `architect`: the shape a system should take

Read first: what exists now, the real load figures the user supplied, the team's constraints and the deadline.

Shape: the current state, the options that fit (two or three, no more), what each costs and forecloses, the trade-offs named, the smallest first slice that delivers something, and the migration path with its rollback. Any figure the user did not give is `[metric — supply this]`. Numbers about third-party systems need a source fetched in the session or the `[unverified]` mark.

Tends to fail by: designing for a scale the user does not have yet.
