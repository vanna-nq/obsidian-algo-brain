---
type: paper
paper_id: PAPER-077
status: primary-source-abstract-screened
category: "08 Regime Detection"
year: 1986
reviewed_on: 2026-10-13
doi: "10.1016/0304-4076(86)90063-1"
source_url: "https://doi.org/10.1016/0304-4076(86)90063-1"
replicated: false
---
# PAPER-077 — Generalized autoregressive conditional heteroskedasticity

**Authors:** Tim Bollerslev  
**Publication:** Journal of Econometrics 31(3), 307–327 (1986)  
**Primary research source:** https://doi.org/10.1016/0304-4076(86)90063-1
**DOI:** https://doi.org/10.1016/0304-4076(86)90063-1

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Extends ARCH by using past conditional variances as well as past residual shocks to estimate time-varying volatility.

## Author-reported finding or theoretical scope
Derives conditions and estimation methods for GARCH models, demonstrating an improved empirical variance model compared to simple ARCH in its application.

## Required data / feasibility gate
Time-stamped return innovations, fixed volatility horizon, train-only GARCH fitting, appropriate asymmetric model benchmarks.

## Critique / potential failure
A volatility forecast is a risk-state estimate, NOT a directly observable market regime or a directional predictor; leverage effects and jumps are often asymmetric.

## Falsifiable follow-up (proposal only)
Benchmark GARCH(1,1), EWMA, historical volatility and a pre-specified Markov model on next-day realized volatility and OOS calibration, then assess trade value.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/08 Regime Detection/README|Regime Detection]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
