---
type: paper
paper_id: PAPER-063
status: primary-source-abstract-screened
category: "01 Statistical Arbitrage"
year: 2010
reviewed_on: 2026-10-13
doi: "10.1016/j.physa.2010.01.045"
source_url: "https://doi.org/10.1016/j.physa.2010.01.045"
replicated: false
---
# PAPER-063 — Analytic solutions for optimal statistical arbitrage trading

**Authors:** William K. Bertram  
**Publication:** Physica A 389(11), 2234–2243 (2010)  
**Primary research source:** https://doi.org/10.1016/j.physa.2010.01.045
**DOI:** https://doi.org/10.1016/j.physa.2010.01.045

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Derives first-passage-time based trade duration and returns for an Ornstein–Uhlenbeck mean-reverting price process, with optimal entry/exit under selected objectives.

## Author-reported finding or theoretical scope
The paper supplies analytical optimization under an assumed OU process, including an exact expected-return solution; not a proven universal price model.

## Required data / feasibility gate
High-quality synchronized spread-price series, prefit mean-reversion parameters, bid-ask spreads, contract rolls, shorting and timing constraints.

## Critique / potential failure
Real spreads can jump, be nonstationary or incur path-dependent costs; an optimal threshold conditional on assumed OU parameters is not robust to estimation error.

## Falsifiable follow-up (proposal only)
Simulate exact OU data to check formulas, then freeze thresholds and compare to simple z-score rules on held-out tradable spreads.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/01 Statistical Arbitrage/README|Statistical Arbitrage]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
