---
type: hypothesis
hypothesis_id: "HYP-F004"
status: "proposed"
priority_tier: "T1"
backtest_executed: false
full_paper_audit_completed: false
---
# HYP-F004 — Time Reversal Volatility Feedback

**T1 / queue #4 / proposed — proposed, NOT independently tested.** The literature notes are source-screened rather than audited full-text replications.

## Source papers and mechanism
[[01 - Paper Library/PAPER-088 - Time reversal invariance in finance|PAPER-088 — Time reversal invariance in finance]], [[01 - Paper Library/PAPER-089 - The Zumbach effect under rough Heston|PAPER-089 — The Zumbach effect under rough Heston]], [[01 - Paper Library/PAPER-102 - From quadratic Hawkes processes to super-Heston rough volatility models with Zumbach |PAPER-102 — From quadratic Hawkes processes to super-Heston rough volatility models with Zumbach effect]]

## Exact proposed observable and prediction
- **Input dataset:** GC.F 5m or SPX500 1h. No local raw-data availability or SHA verified in this repository task.
- **Feature:** Past-only lagged returns-versus-variance asymmetry.
- **Target:** Next-window realized variance.
- **Candidate null:** No incremental prospective utility over the benchmark on identical observations and cost assumptions.
- **Baseline:** HAR-RV and symmetric GARCH.
- **Primary evaluation:** OOS QLIKE and reversal-surrogate check. All exact hyperparameters, target timing, chronological splits and minimum worthwhile gain to be frozen *after* the source/data audit but *before* model execution.

## Research gate / data problems
Original moment definition, offline reverse-time null separate from causal feature.

## Stop / failure definition
Stop if authentic data or original formulas cannot be audited. If a precommitted chronological holdout does not show a robust positive incremental gain over the baseline, mark FAIL or INCONCLUSIVE. One frozen task at a time; preserve negative outcomes and full selection history.

## Execution economics
There is **no approved trading entry, exit or sizing rule** for this hypothesis, except where specifically defined as a *future* PnL study. Confirmed predictive information and realistic execution economics are separate validation stages.

## Links
- [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]]
- [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]]
