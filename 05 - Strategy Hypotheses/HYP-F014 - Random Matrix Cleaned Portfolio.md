---
type: hypothesis
hypothesis_id: "HYP-F014"
status: "data-blocked"
priority_tier: "T3"
backtest_executed: false
full_paper_audit_completed: false
---
# HYP-F014 — Random Matrix Cleaned Portfolio

**T3 / queue #14 / data-blocked — proposed, NOT independently tested.** The literature notes are source-screened rather than audited full-text replications.

## Source papers and mechanism
[[01 - Paper Library/PAPER-032 - Portfolio Selection|PAPER-032 — Portfolio Selection]], [[01 - Paper Library/PAPER-056 - Optimal Versus Naive Diversification How Inefficient is the 1N Portfolio Strategy|PAPER-056 — Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?]], [[01 - Paper Library/PAPER-095 - Noise Dressing of Financial Correlation Matrices|PAPER-095 — Noise Dressing of Financial Correlation Matrices]], [[01 - Paper Library/PAPER-096 - Dynamics of market correlations Taxonomy and portfolio analysis|PAPER-096 — Dynamics of market correlations: Taxonomy and portfolio analysis]]

## Exact proposed observable and prediction
- **Input dataset:** Broad point-in-time synchronized instrument universe required. No local raw-data availability or SHA verified in this repository task.
- **Feature:** Marchenko–Pastur spectral denoising fitted using past returns.
- **Target:** Future covariance forecast / portfolio risk.
- **Candidate null:** No incremental prospective utility over the benchmark on identical observations and cost assumptions.
- **Baseline:** Ledoit-Wolf covariance, sample covariance and 1/N.
- **Primary evaluation:** Forward variance, forecast error and turnover. All exact hyperparameters, target timing, chronological splits and minimum worthwhile gain to be frozen *after* the source/data audit but *before* model execution.

## Research gate / data problems
Two correlated ETFs are not sufficient for high-dimensional spectral test.

## Stop / failure definition
Stop if authentic data or original formulas cannot be audited. If a precommitted chronological holdout does not show a robust positive incremental gain over the baseline, mark FAIL or INCONCLUSIVE. One frozen task at a time; preserve negative outcomes and full selection history.

## Execution economics
There is **no approved trading entry, exit or sizing rule** for this hypothesis, except where specifically defined as a *future* PnL study. Confirmed predictive information and realistic execution economics are separate validation stages.

## Links
- [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]]
- [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]]
