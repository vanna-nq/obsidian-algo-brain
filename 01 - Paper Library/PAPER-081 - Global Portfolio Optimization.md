---
type: paper
paper_id: PAPER-081
status: primary-source-abstract-screened
category: "10 Optimization and Physics"
year: 1992
reviewed_on: 2026-10-13
doi: "10.2469/faj.v48.n5.28"
source_url: "https://rpc.cfainstitute.org/research/financial-analysts-journal/1992/faj-v48-n5-28"
replicated: false
---
# PAPER-081 — Global Portfolio Optimization

**Authors:** Fischer Black; Robert Litterman  
**Publication:** Financial Analysts Journal 48(5), 28–43 (1992)  
**Primary research source:** https://rpc.cfainstitute.org/research/financial-analysts-journal/1992/faj-v48-n5-28
**DOI:** https://doi.org/10.2469/faj.v48.n5.28

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Combines market-equilibrium implied expected returns with subjective investor views, weighted by their uncertainty, as input to constrained allocation.

## Author-reported finding or theoretical scope
Offers a method to stabilize mean-variance portfolio construction and communicate confidence in views; no proof of future alpha.

## Required data / feasibility gate
Price/market-cap weights, covariance estimation, investable assets, confidence model, point-in-time forecasts and transaction costs.

## Critique / potential failure
Poor prior or overly confident forecasts can degrade allocations; Black–Litterman cannot rescue inaccurate asset covariance, leverage or costs.

## Falsifiable follow-up (proposal only)
Compare Black–Litterman allocations with 1/N and shrinkage minimum variance under OOS covariance uncertainty and turnover limits.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/10 Optimization and Physics/README|Optimization and Physics]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
