---
name: portable-harness
description: Set up a repo so any coding agent (Claude Code, Codex, Cursor) behaves the same wherever it runs - writes 12 working rules at the top of CLAUDE.md or AGENTS.md, adds map sections only where the agent keeps getting things wrong, and installs guardrails it cannot talk past - a type check that fails only on new errors, live-service tests that run only on request, and tests plus type check before every deploy from main. Use when someone wants agent rules for a repo, a better CLAUDE.md or AGENTS.md, says the agent keeps ignoring conventions, hiding behind old type errors or calling real services in tests, or wants their setup to move between harnesses, even if they never say harness. Not for pruning or auditing a setup that already exists (use harness-audit), reviewing code (use consistent-code-review), writing features or fixes (use production-code), or turning a skill into a Claude Code plugin (use skill-to-mod).
---

# portable-harness

Three layers, in this order. Each one is a change to the user's repo, so show the diff and get a yes before writing.

The rules, the map and the guardrails live in the repo, not in the harness. That is the point: the user can switch between Claude Code and Codex and keep all three.

## Before you start

1. Find the instruction file. Use `CLAUDE.md` if it exists, else `AGENTS.md`. If both exist, edit the one the other points to, or ask. If neither exists, create `AGENTS.md` and a one-line `CLAUDE.md` containing `@AGENTS.md`.
2. Find the stack: language, type checker, test runner, CI system, deploy step. Read the config files, do not guess. Missing pieces (no type checker, no CI) are reported, not invented.
3. Ask which layers to apply if the user did not say. Default: all three.

## Step 1 - Rules

Put the 12 rules from `references/rules.md` at the very top of the instruction file, above anything already there. Keep the credit line. If the file already has rules, do not average the two sets: list each conflict (rule 7) and ask which wins.

## Step 2 - Map, not manual

Ask one question: "Where does the agent keep getting things wrong in this repo?" Offer what you found while reading (env vars, auth or access control, migrations, a generated folder) as options.

For each area the user picks, write one section of at most ~180 lines with:

- what the agent must know (file paths, the one helper to use, the order of operations)
- one worked example taken from this repo's code
- a "Do not" list of the mistakes the user named

Write nothing for areas the user did not pick. Do not document the whole repo.

## Step 3 - Guardrails

Read `references/guardrails.md` for the recipe per stack. Apply only the ones that fit this repo:

1. **Type check fails only on new errors.** Record today's errors as a baseline file and gate on it with `scripts/typecheck_gate.py`. Old errors are grandfathered; any new one fails. Commit the baseline.
2. **Live-service tests are opt-in.** Tests that hit real services are tagged and skipped by default; they run only with an explicit flag or env var.
3. **Push to main runs tests and type check before deploy.** The deploy job depends on both. Skipped tests make the run fail loud (rule 12) unless the skip is the live-service tag.

Run each guardrail once locally and show the output. A guardrail that was written but not run is reported as not run.

## Report

- Instruction file changed, and rule conflicts resolved.
- Map sections written, one line each.
- Each guardrail: added, already present, or not possible (with why).
- What was run and what was not.
- Next step: after the agent's next big change, run `consistent-code-review` on it.

## Boundaries

This skill writes setup, not features. It never edits application code beyond tagging live-service tests. Code review after the agent finishes belongs to `consistent-code-review`; hand it the diff or branch name.
