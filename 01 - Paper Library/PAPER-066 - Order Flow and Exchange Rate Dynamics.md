---
type: paper
paper_id: PAPER-066
status: primary-source-abstract-screened
category: "03 Market Microstructure"
year: 2002
reviewed_on: 2026-10-13
doi: "10.1086/324391"
source_url: "https://www.journals.uchicago.edu/doi/10.1086/324391"
replicated: false
---
# PAPER-066 — Order Flow and Exchange Rate Dynamics

**Authors:** Martin D. D. Evans; Richard K. Lyons  
**Publication:** Journal of Political Economy 110(1), 170–180 (2002)  
**Primary research source:** https://www.journals.uchicago.edu/doi/10.1086/324391
**DOI:** https://doi.org/10.1086/324391

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Introduces FX order flow as an information-bearing explanatory variable for exchange-rate movements, distinct from macro-only pricing models.

## Author-reported finding or theoretical scope
Authors report high contemporaneous explanatory power for daily DEM/USD price changes using their order-flow data.

## Required data / feasibility gate
Institutional signed FX dealing flow, timestamped quotes, known macro releases, spreads and dealer relationships.

## Critique / potential failure
Same-day explanatory R² is not out-of-sample direction accuracy; signed flow is not observable from OHLCV alone; FX market structure has evolved.

## Falsifiable follow-up (proposal only)
Compare only lagged, actually observable FX order flow to purely price-based predictors in future return forecasting and net execution tests.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/03 Market Microstructure/README|Market Microstructure]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
