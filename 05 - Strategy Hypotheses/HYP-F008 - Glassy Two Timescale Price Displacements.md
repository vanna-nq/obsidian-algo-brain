---
type: hypothesis
hypothesis_id: "HYP-F008"
status: "proposed"
priority_tier: "T2"
backtest_executed: false
full_paper_audit_completed: false
---
# HYP-F008 — Glassy Two Timescale Price Displacements

**T2 / queue #8 / proposed — proposed, NOT independently tested.** The literature notes are source-screened rather than audited full-text replications.

## Source papers and mechanism
[[01 - Paper Library/PAPER-103 - Diffusive and Arrestedlike Dynamics in Currency Exchange Markets|PAPER-103 — Diffusive and Arrestedlike Dynamics in Currency Exchange Markets]], [[01 - Paper Library/PAPER-104 - A model for foreign exchange markets based on glassy Brownian systems|PAPER-104 — A model for foreign exchange markets based on glassy Brownian systems]], [[01 - Paper Library/PAPER-059 - Intraday periodicity and volatility persistence in financial markets|PAPER-059 — Intraday periodicity and volatility persistence in financial markets]]

## Exact proposed observable and prediction
- **Input dataset:** GC.F 5m; adaptation from currency-market research. No local raw-data availability or SHA verified in this repository task.
- **Feature:** Past-only estimate of two-stage displacement or plateau.
- **Target:** Future short-horizon variance or return-tail quantiles (freeze one).
- **Candidate null:** No incremental prospective utility over the benchmark on identical observations and cost assumptions.
- **Baseline:** Seasonally adjusted Student-t GARCH and mixture null.
- **Primary evaluation:** Forecast log score / QLIKE. All exact hyperparameters, target timing, chronological splits and minimum worthwhile gain to be frozen *after* the source/data audit but *before* model execution.

## Research gate / data problems
Physical analogy not mechanism identification; session closure and liquidity-seasonality null.

## Stop / failure definition
Stop if authentic data or original formulas cannot be audited. If a precommitted chronological holdout does not show a robust positive incremental gain over the baseline, mark FAIL or INCONCLUSIVE. One frozen task at a time; preserve negative outcomes and full selection history.

## Execution economics
There is **no approved trading entry, exit or sizing rule** for this hypothesis, except where specifically defined as a *future* PnL study. Confirmed predictive information and realistic execution economics are separate validation stages.

## Links
- [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]]
- [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]]
