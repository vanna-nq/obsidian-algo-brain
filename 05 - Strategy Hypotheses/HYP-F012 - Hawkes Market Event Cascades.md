---
type: hypothesis
hypothesis_id: "HYP-F012"
status: "data-blocked"
priority_tier: "T3"
backtest_executed: false
full_paper_audit_completed: false
---
# HYP-F012 — Hawkes Market Event Cascades

**T3 / queue #12 / data-blocked — proposed, NOT independently tested.** The literature notes are source-screened rather than audited full-text replications.

## Source papers and mechanism
[[01 - Paper Library/PAPER-067 - Price Dynamics in a Markovian Limit Order Market|PAPER-067 — Price Dynamics in a Markovian Limit Order Market]], [[01 - Paper Library/PAPER-097 - Hawkes processes in finance|PAPER-097 — Hawkes processes in finance]], [[01 - Paper Library/PAPER-102 - From quadratic Hawkes processes to super-Heston rough volatility models with Zumbach |PAPER-102 — From quadratic Hawkes processes to super-Heston rough volatility models with Zumbach effect]]

## Exact proposed observable and prediction
- **Input dataset:** Tick-level trades/L1-L2 quotes currently unavailable. No local raw-data availability or SHA verified in this repository task.
- **Feature:** Lagged self and cross-exciting trade/quote event intensity.
- **Target:** Next event arrivals/jump hazard.
- **Candidate null:** No incremental prospective utility over the benchmark on identical observations and cost assumptions.
- **Baseline:** Inhomogeneous Poisson and autoregressive counts.
- **Primary evaluation:** Event-time log likelihood. All exact hyperparameters, target timing, chronological splits and minimum worthwhile gain to be frozen *after* the source/data audit but *before* model execution.

## Research gate / data problems
OHLCV cannot identify true order and cancellation events.

## Stop / failure definition
Stop if authentic data or original formulas cannot be audited. If a precommitted chronological holdout does not show a robust positive incremental gain over the baseline, mark FAIL or INCONCLUSIVE. One frozen task at a time; preserve negative outcomes and full selection history.

## Execution economics
There is **no approved trading entry, exit or sizing rule** for this hypothesis, except where specifically defined as a *future* PnL study. Confirmed predictive information and realistic execution economics are separate validation stages.

## Links
- [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]]
- [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]]
