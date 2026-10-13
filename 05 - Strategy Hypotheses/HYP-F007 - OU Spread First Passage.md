---
type: hypothesis
hypothesis_id: "HYP-F007"
status: "proposed"
priority_tier: "T2"
backtest_executed: false
full_paper_audit_completed: false
---
# HYP-F007 — OU Spread First Passage

**T2 / queue #7 / proposed — proposed, NOT independently tested.** The literature notes are source-screened rather than audited full-text replications.

## Source papers and mechanism
[[01 - Paper Library/PAPER-002 - Pairs Trading - Gatev Goetzmann Rouwenhorst 2006|PAPER-002 — Pairs Trading]], [[01 - Paper Library/PAPER-014 - Co-Integration and Error Correction|PAPER-014 — Co-Integration and Error Correction]], [[01 - Paper Library/PAPER-015 - Pairs Trading|PAPER-015 — Pairs Trading]], [[01 - Paper Library/PAPER-039 - The profitability of pairs trading strategies distance cointegration and copula method|PAPER-039 — The profitability of pairs trading strategies: distance, cointegration and copula methods]], [[01 - Paper Library/PAPER-063 - Analytic solutions for optimal statistical arbitrage trading|PAPER-063 — Analytic solutions for optimal statistical arbitrage trading]]

## Exact proposed observable and prediction
- **Input dataset:** NVDA/SMH corrected synchronized 5m. No local raw-data availability or SHA verified in this repository task.
- **Feature:** Training-only mean-reverting spread and stopping thresholds.
- **Target:** Net OOS spread trade PnL.
- **Candidate null:** No incremental prospective utility over the benchmark on identical observations and cost assumptions.
- **Baseline:** Simple z-score pair and no-trade.
- **Primary evaluation:** Net PnL, drawdown, cost sensitivity. All exact hyperparameters, target timing, chronological splits and minimum worthwhile gain to be frozen *after* the source/data audit but *before* model execution.

## Research gate / data problems
Stationarity/structural breaks, short borrow, hedging units and tradable fills.

## Stop / failure definition
Stop if authentic data or original formulas cannot be audited. If a precommitted chronological holdout does not show a robust positive incremental gain over the baseline, mark FAIL or INCONCLUSIVE. One frozen task at a time; preserve negative outcomes and full selection history.

## Execution economics
There is **no approved trading entry, exit or sizing rule** for this hypothesis, except where specifically defined as a *future* PnL study. Confirmed predictive information and realistic execution economics are separate validation stages.

## Links
- [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]]
- [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]]
