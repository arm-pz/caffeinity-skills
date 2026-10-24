#!/usr/bin/env bash
# Run the trigger suite for the caffeinity bundle on your own Claude login (never in CI: it costs
# about $0.10 a case, ~$5 for the suite). Writes evals/last-run.json, a per-case summary you commit
# so the next run, and the weekly W10 session, can say what changed.
#
#   bash scripts/run_evals.sh                 # every case, one run each
#   bash scripts/run_evals.sh --case 'seo-*'  # extra flags go to `claude plugin eval`
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/build_evals.py --check
out=$(mktemp -d)
status=0
claude plugin eval plugins/caffeinity --ablation none --runs 1 -j 4 --trust-plugin --no-publish \
  --threshold 1 --max-cost-usd 10 --json "$out/run.json" "$@" || status=$?
python3 scripts/summarize_evals.py "$out/run.json" evals/last-run.json
exit $status
