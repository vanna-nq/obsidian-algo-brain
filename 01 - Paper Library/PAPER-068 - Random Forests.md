---
type: paper
paper_id: PAPER-068
status: primary-source-abstract-screened
category: "04 Machine Learning"
year: 2001
reviewed_on: 2026-10-13
doi: "10.1023/A:1010933404324"
source_url: "https://link.springer.com/article/10.1023/A:1010933404324"
replicated: false
---
# PAPER-068 — Random Forests

**Authors:** Leo Breiman  
**Publication:** Machine Learning 45, 5–32 (2001)  
**Primary research source:** https://link.springer.com/article/10.1023/A:1010933404324
**DOI:** https://doi.org/10.1023/A:1010933404324

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Develops bagged tree ensembles with randomized predictors, with analysis of individual tree strength, correlation and generalization error.

## Author-reported finding or theoretical scope
Methodological work establishes an efficient nonlinear forecasting baseline; does not itself claim financial return predictability.

## Required data / feasibility gate
Causal point-in-time predictors, training-only feature engineering, time-split validation and full strategy cost assumptions.

## Critique / potential failure
The out-of-bag estimate is not a substitute for time-respecting finance backtests if training mixes future regimes, overlapping labels or shared firms.

## Falsifiable follow-up (proposal only)
Use fixed random forest against regularized logistic/linear and XGBoost forecasts under an identical walk-forward split and calibration/cost audit.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/04 Machine Learning/README|Machine Learning]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
