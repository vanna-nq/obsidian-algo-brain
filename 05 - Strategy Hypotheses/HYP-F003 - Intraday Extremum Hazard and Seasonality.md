---
type: hypothesis
hypothesis_id: "HYP-F003"
status: "proposed"
priority_tier: "T1"
backtest_executed: false
full_paper_audit_completed: false
---
# HYP-F003 — Intraday Extremum Hazard and Seasonality

**T1 / queue #3 / proposed — proposed, NOT independently tested.** The literature notes are source-screened rather than audited full-text replications.

## Source papers and mechanism
[[01 - Paper Library/PAPER-001 - Beat the Market - SPY Intraday Momentum|PAPER-001 — Beat the Market - SPY Intraday Momentum]], [[01 - Paper Library/PAPER-012 - Market Intraday Momentum - Gao Han Li Zhou 2018|PAPER-012 — Market Intraday Momentum]], [[01 - Paper Library/PAPER-035 - Hedging Demand and Market Intraday Momentum|PAPER-035 — Hedging Demand and Market Intraday Momentum]], [[01 - Paper Library/PAPER-058 - A Theory of Intraday Patterns Volume and Price Variability|PAPER-058 — A Theory of Intraday Patterns: Volume and Price Variability]], [[01 - Paper Library/PAPER-059 - Intraday periodicity and volatility persistence in financial markets|PAPER-059 — Intraday periodicity and volatility persistence in financial markets]], [[01 - Paper Library/PAPER-082 - Periodic market closure and trading volume A model of intraday bids and asks|PAPER-082 — Periodic market closure and trading volume: A model of intraday bids and asks]], [[01 - Paper Library/PAPER-083 - A transaction data study of weekly and intradaily patterns in stock returns|PAPER-083 — A transaction data study of weekly and intradaily patterns in stock returns]]

## Exact proposed observable and prediction
- **Input dataset:** GC.F 5m session OHLCV. No local raw-data availability or SHA verified in this repository task.
- **Feature:** Time-of-session, historical extremes and realized range through time t.
- **Target:** Probability a current session high or low survives unbroken to session end.
- **Candidate null:** No incremental prospective utility over the benchmark on identical observations and cost assumptions.
- **Baseline:** Time-only empirical hazards and trailing session volatility.
- **Primary evaluation:** OOS Brier score and calibration. All exact hyperparameters, target timing, chronological splits and minimum worthwhile gain to be frozen *after* the source/data audit but *before* model execution.

## Research gate / data problems
Exchange session calendar, no future HOD/LOD as current feature.

## Stop / failure definition
Stop if authentic data or original formulas cannot be audited. If a precommitted chronological holdout does not show a robust positive incremental gain over the baseline, mark FAIL or INCONCLUSIVE. One frozen task at a time; preserve negative outcomes and full selection history.

## Execution economics
There is **no approved trading entry, exit or sizing rule** for this hypothesis, except where specifically defined as a *future* PnL study. Confirmed predictive information and realistic execution economics are separate validation stages.

## Links
- [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]]
- [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]]
