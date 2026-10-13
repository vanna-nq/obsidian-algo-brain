---
type: hypothesis
hypothesis_id: "HYP-F001"
status: "audit-queued"
priority_tier: "T1"
backtest_executed: false
full_paper_audit_completed: false
---
# HYP-F001 — Permutation Entropy Future Volatility

**T1 / queue #1 / audit-queued — proposed, NOT independently tested.** The literature notes are source-screened rather than audited full-text replications.

## Source papers and mechanism
[[01 - Paper Library/PAPER-090 - Permutation Entropy A Natural Complexity Measure for Time Series|PAPER-090 — Permutation Entropy: A Natural Complexity Measure for Time Series]], [[01 - Paper Library/PAPER-024 - A Mathematical Theory of Communication|PAPER-024 — A Mathematical Theory of Communication]], [[01 - Paper Library/PAPER-059 - Intraday periodicity and volatility persistence in financial markets|PAPER-059 — Intraday periodicity and volatility persistence in financial markets]]

## Exact proposed observable and prediction
- **Input dataset:** GC.F 5m OHLCV. No local raw-data availability or SHA verified in this repository task.
- **Feature:** Rolling m=3 ordinal entropy from past 120 completed returns.
- **Target:** Next 12-bar realized variance.
- **Candidate null:** No incremental prospective utility over the benchmark on identical observations and cost assumptions.
- **Baseline:** Lagged realized-variance HAR-style regression, EWMA.
- **Primary evaluation:** OOS QLIKE. All exact hyperparameters, target timing, chronological splits and minimum worthwhile gain to be frozen *after* the source/data audit but *before* model execution.

## Research gate / data problems
Full original paper and GC data preview with futures roll/session definition.

## Stop / failure definition
Stop if authentic data or original formulas cannot be audited. If a precommitted chronological holdout does not show a robust positive incremental gain over the baseline, mark FAIL or INCONCLUSIVE. One frozen task at a time; preserve negative outcomes and full selection history.

## Execution economics
There is **no approved trading entry, exit or sizing rule** for this hypothesis, except where specifically defined as a *future* PnL study. Confirmed predictive information and realistic execution economics are separate validation stages.

## Links
- [[06 - Experiments and Backtests/EXP-F001 - Permutation Entropy Data and Method Audit|EXP-F001 — audit-only first task]]
- [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]]
- [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]]
