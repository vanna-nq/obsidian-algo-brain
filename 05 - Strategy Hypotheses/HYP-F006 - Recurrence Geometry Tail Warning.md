---
type: hypothesis
hypothesis_id: "HYP-F006"
status: "proposed"
priority_tier: "T2"
backtest_executed: false
full_paper_audit_completed: false
---
# HYP-F006 — Recurrence Geometry Tail Warning

**T2 / queue #6 / proposed — proposed, NOT independently tested.** The literature notes are source-screened rather than audited full-text replications.

## Source papers and mechanism
[[01 - Paper Library/PAPER-091 - Topological Data Analysis of Financial Time Series Landscapes of Crashes|PAPER-091 — Topological Data Analysis of Financial Time Series: Landscapes of Crashes]], [[01 - Paper Library/PAPER-092 - Early warning signals for stock market crashes empirical and analytical insights util|PAPER-092 — Early warning signals for stock market crashes: empirical and analytical insights utilizing nonlinear methods]], [[01 - Paper Library/PAPER-098 - Large financial crashes|PAPER-098 — Large financial crashes]]

## Exact proposed observable and prediction
- **Input dataset:** SPX500 1h OHLCV; not a replication of multi-index topology paper. No local raw-data availability or SHA verified in this repository task.
- **Feature:** Lagged recurrence determinism, laminarity, or persistence statistic.
- **Target:** Predefined future tail-risk event.
- **Candidate null:** No incremental prospective utility over the benchmark on identical observations and cost assumptions.
- **Baseline:** Trailing vol, vol-of-vol and drawdown.
- **Primary evaluation:** Event PR-AUC and false alarms/year. All exact hyperparameters, target timing, chronological splits and minimum worthwhile gain to be frozen *after* the source/data audit but *before* model execution.

## Research gate / data problems
Frozen event/radius definitions and rare-event time-series splits.

## Stop / failure definition
Stop if authentic data or original formulas cannot be audited. If a precommitted chronological holdout does not show a robust positive incremental gain over the baseline, mark FAIL or INCONCLUSIVE. One frozen task at a time; preserve negative outcomes and full selection history.

## Execution economics
There is **no approved trading entry, exit or sizing rule** for this hypothesis, except where specifically defined as a *future* PnL study. Confirmed predictive information and realistic execution economics are separate validation stages.

## Links
- [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]]
- [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]]
