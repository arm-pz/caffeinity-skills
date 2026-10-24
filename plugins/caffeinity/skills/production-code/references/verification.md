# Verification

The rule this file exists for: run what the machine can run, then report exactly which ran. Nothing here asks for a test suite where none is wanted; seconds of checking is the price of an honest claim.

## The tiers

| Tier | Check | What it proves | What it does not prove |
| --- | --- | --- | --- |
| 1 | Parse or compile | The syntax is valid | Nothing about behaviour |
| 2 | Unit test, or the code run against a fixture you wrote or the user supplied | The logic behaves on that input | The real input, the live service, the deployment |
| 3 | The actual command against the user's data or target | It works there, then | It works on the user's machine tomorrow |

Aim for the highest tier the machine allows. Tier 1 alone must never be reported as "tested".

## Per runtime

Confirm the interpreter or toolchain exists and its version before quoting a command, and report the version you ran against.

| Runtime | Tier 1 | Tier 2 | Tier 3 |
| --- | --- | --- | --- |
| Python | `python -m py_compile file.py` | `pytest -q` | `python file.py --dry-run` on the real input |
| Node / JavaScript | `node --check file.mjs` | `npm test` | `node file.mjs` with test credentials or a local stub |
| TypeScript | `tsc --noEmit` | `npm test` | the built entry point run |
| Bash | `bash -n script.sh`, `shellcheck` when installed | run functions with stubbed commands | run with the dry flag, then the live one |
| SQL | parse via the engine | run the `SELECT` read-only, `EXPLAIN` it | mutation only inside a transaction you can roll back, after the row-count check |
| Go | `go build ./...` | `go test ./...` | the binary run locally |
| Rust | `cargo check` | `cargo test` | `cargo run` |
| Java | the build's compile task | its test task | the jar run |
| R | `Rscript -e 'parse("file.R")'` | `testthat` when present | `Rscript file.R` on the real file |
| PHP | `php -l file.php` | `phpunit` | the route against a local server |
| Docker / compose | `docker compose config` | build the image | run it and hit one endpoint |
| Front-end bundle | the project's build | its test runner | rendering in a browser you actually opened |
| Cron / timer / Windows task | the unit file or schedule expression parses | the command run by hand once | the scheduled fire itself, which you cannot observe |

## Installing to get a check to run

Ask before installing a package or a toolchain; it changes the user's machine. If you did install, say what and from where. If you did not, name the check you skipped and the reason.

## When you cannot run it

Say so in the first line of the report, not buried at the end. Common honest reasons: no interpreter for that language on this machine, dependency not installed and none requested, no network from the sandbox, no credentials for the service, database not reachable, the user's data file was never supplied, the target is the user's production host, the OS here differs from the one it will run on.

Report in four labelled lines:

```
Verified: the commands actually run, each with its real outcome.
Not verified: what did not run, each with the reason.
Assumed: versions, file paths, field names, behaviour taken on trust.
Needs from you: the single command to run, or the input required.
```

Rules for the wording:

- Quote the command and its result as observed. A paraphrase of output you did not see is a fabrication.
- A failing check stays failing in the report. Show it, then the fix, then the re-run.
- No result is a result: "could not run, no Python on PATH" is the finding.
- Never write "should work", "this will run first time" or "zero debugging required". Write what happened.
- Performance claims need a measurement on this machine, with the machine's caveat attached. Otherwise `[unverified]`.
- Test counts, coverage figures and query timings come from a run you performed in this session or they are slots.

## Fix mode specifically

Reproduce before you patch. If you cannot reproduce the user's error, deliver the patch labelled as a hypothesis, with the one command that would confirm or kill it, and say the reproduction was attempted and failed here.

## Self-check on the report

Before sending: does every verb in the Verification line correspond to a command I ran in this session? Could the user re-run what I listed and get the same words? Is each Not verified item given a reason rather than left out?
