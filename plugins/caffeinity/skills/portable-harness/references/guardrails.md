# Guardrail recipes

Read the repo's existing config first and extend it. Use the stack's own mechanism; add nothing new when one exists.

## 1. Type check fails only on new errors

Copy `scripts/typecheck_gate.py` into the repo (e.g. `tools/`), then record the baseline once and commit it:

| Stack | Command piped into the gate |
| --- | --- |
| TypeScript | `npx tsc --noEmit --pretty false` |
| Python (mypy) | `mypy .` |
| Python (pyright) | `npx pyright` |
| .NET | `dotnet build --no-incremental` |

```
<command> 2>&1 | python3 tools/typecheck_gate.py typecheck-baseline.txt --update   # once, commit the file
<command> 2>&1 | python3 tools/typecheck_gate.py typecheck-baseline.txt            # in CI and pre-push
```

If the checker already has a baseline feature the repo uses (basedpyright `--baselinefile`, a `.NET` suppression file), use that instead of the script.

Tell the user: only a human runs `--update`, and only to shrink the baseline. Add that line to the instruction file's "Do not" list.

## 2. Live-service tests are opt-in

Tag each test that calls a real network service, database or paid API. Default runs skip them.

| Runner | Tag | Default skip | Opt in |
| --- | --- | --- | --- |
| pytest | `@pytest.mark.live` | `addopts = -m "not live"` in config, register the marker | `pytest -m live` |
| Jest / Vitest | `const live = process.env.RUN_LIVE ? describe : describe.skip` | env unset | `RUN_LIVE=1` |
| xUnit | `[Trait("Category","Live")]` | `--filter "Category!=Live"` in the test script | `--filter "Category=Live"` |
| Go | `//go:build live` | default build | `go test -tags live` |

Add to the instruction file: "Never run live tests unless the user asks in this session."

## 3. Push to main: tests and type check before deploy

The deploy job must depend on both checks. GitHub Actions shape:

```yaml
on: { push: { branches: [main] } }
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: <install>
      - run: <test command, live tests excluded>
      - run: <type check command> 2>&1 | python3 tools/typecheck_gate.py typecheck-baseline.txt
  deploy:
    needs: check
    # existing deploy steps, moved here unchanged
```

`set -o pipefail` is the default for `run:` on GitHub's bash shell; in other CI systems add it, or the gate's exit code is lost in the pipe.

Fail loud (rule 12): if the runner reports skipped tests other than the live tag, fail the job. pytest: `-rs` and check the summary; Jest: `--passWithNoTests=false`.

For GitLab, Azure Pipelines or a deploy hook: same rule, deploy stage needs the check stage. Do not rewrite the deploy steps themselves.
