---
type: hypothesis
hypothesis_id: "HYP-F009"
status: "proposed"
priority_tier: "T2"
backtest_executed: false
full_paper_audit_completed: false
---
# HYP-F009 — Multifractal Tail Scaling

**T2 / queue #9 / proposed — proposed, NOT independently tested.** The literature notes are source-screened rather than audited full-text replications.

## Source papers and mechanism
[[01 - Paper Library/PAPER-087 - Modelling financial time series using multifractal random walks|PAPER-087 — Modelling financial time series using multifractal random walks]], [[01 - Paper Library/PAPER-101 - Q-Gaussian diffusion in stock markets|PAPER-101 — Q-Gaussian diffusion in stock markets]]

## Exact proposed observable and prediction
- **Input dataset:** GC.F 5m or SPX500 1h. No local raw-data availability or SHA verified in this repository task.
- **Feature:** Past-only multifractal or q-Gaussian scaling statistic.
- **Target:** Future extreme return quantile.
- **Candidate null:** No incremental prospective utility over the benchmark on identical observations and cost assumptions.
- **Baseline:** Student-t GARCH and historical empirical quantile.
- **Primary evaluation:** Pinball loss and exceedance calibration. All exact hyperparameters, target timing, chronological splits and minimum worthwhile gain to be frozen *after* the source/data audit but *before* model execution.

## Research gate / data problems
Moment-estimation bias, multiple timescales, nonstationarity.

## Stop / failure definition
Stop if authentic data or original formulas cannot be audited. If a precommitted chronological holdout does not show a robust positive incremental gain over the baseline, mark FAIL or INCONCLUSIVE. One frozen task at a time; preserve negative outcomes and full selection history.

## Execution economics
There is **no approved trading entry, exit or sizing rule** for this hypothesis, except where specifically defined as a *future* PnL study. Confirmed predictive information and realistic execution economics are separate validation stages.

## Links
- [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]]
- [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]]
