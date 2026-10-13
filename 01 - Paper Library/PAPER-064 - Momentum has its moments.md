---
type: paper
paper_id: PAPER-064
status: primary-source-abstract-screened
category: "02 Trend and Momentum"
year: 2015
reviewed_on: 2026-10-13
doi: "10.1016/j.jfineco.2014.11.010"
source_url: "https://doi.org/10.1016/j.jfineco.2014.11.010"
replicated: false
---
# PAPER-064 — Momentum has its moments

**Authors:** Pedro Barroso; Pedro Santa-Clara  
**Publication:** Journal of Financial Economics 116(1), 111–120 (2015)  
**Primary research source:** https://doi.org/10.1016/j.jfineco.2014.11.010
**DOI:** https://doi.org/10.1016/j.jfineco.2014.11.010

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Scales cross-sectional equity momentum exposures by historical momentum portfolio volatility to manage time-varying crash risk.

## Author-reported finding or theoretical scope
Authors report volatility-managed momentum substantially reduces historical crash severity and improves historical risk-adjusted results.

## Required data / feasibility gate
Long-short momentum constituent histories, robust point-in-time realized-vol estimates, financing and turnover costs.

## Critique / potential failure
This is equity winner-minus-loser momentum, not the SPY intraday band strategy; inverse-vol sizing can magnify risk when recent volatility is deceptively low.

## Falsifiable follow-up (proposal only)
Freeze sizing caps and compare raw versus vol-managed equity momentum on untouched post-2015 data at comparable costs and gross exposure.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/02 Trend and Momentum/README|Trend and Momentum]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
