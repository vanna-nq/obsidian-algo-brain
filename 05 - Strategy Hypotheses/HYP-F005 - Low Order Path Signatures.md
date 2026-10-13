---
type: hypothesis
hypothesis_id: "HYP-F005"
status: "proposed"
priority_tier: "T2"
backtest_executed: false
full_paper_audit_completed: false
---
# HYP-F005 — Low Order Path Signatures

**T2 / queue #5 / proposed — proposed, NOT independently tested.** The literature notes are source-screened rather than audited full-text replications.

## Source papers and mechanism
[[01 - Paper Library/PAPER-093 - Signature Trading A Path-Dependent Extension of the Mean-Variance Framework with Exog|PAPER-093 — Signature Trading: A Path-Dependent Extension of the Mean-Variance Framework with Exogenous Signals]], [[01 - Paper Library/PAPER-094 - Optimal Execution with Rough Path Signatures|PAPER-094 — Optimal Execution with Rough Path Signatures]], [[01 - Paper Library/PAPER-090 - Permutation Entropy A Natural Complexity Measure for Time Series|PAPER-090 — Permutation Entropy: A Natural Complexity Measure for Time Series]]

## Exact proposed observable and prediction
- **Input dataset:** NVDA/SMH 5m corrected OHLCV. No local raw-data availability or SHA verified in this repository task.
- **Feature:** Order-2 price-return/volume/volatility path signatures.
- **Target:** Future six-bar variance (subject to freeze).
- **Candidate null:** No incremental prospective utility over the benchmark on identical observations and cost assumptions.
- **Baseline:** Matched lagged predictors using ridge or boosted trees.
- **Primary evaluation:** OOS QLIKE. All exact hyperparameters, target timing, chronological splits and minimum worthwhile gain to be frozen *after* the source/data audit but *before* model execution.

## Research gate / data problems
Full signature math, adjusted prices, leakage-free path normalization.

## Stop / failure definition
Stop if authentic data or original formulas cannot be audited. If a precommitted chronological holdout does not show a robust positive incremental gain over the baseline, mark FAIL or INCONCLUSIVE. One frozen task at a time; preserve negative outcomes and full selection history.

## Execution economics
There is **no approved trading entry, exit or sizing rule** for this hypothesis, except where specifically defined as a *future* PnL study. Confirmed predictive information and realistic execution economics are separate validation stages.

## Links
- [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]]
- [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]]
