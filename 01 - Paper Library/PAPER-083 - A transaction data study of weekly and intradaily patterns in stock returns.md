---
type: paper
paper_id: PAPER-083
status: primary-source-abstract-screened
category: "11 Intraday Price Structure"
year: 1986
reviewed_on: 2026-10-13
doi: "10.1016/0304-405X(86)90044-9"
source_url: "https://doi.org/10.1016/0304-405X(86)90044-9"
replicated: false
---
# PAPER-083 — A transaction data study of weekly and intradaily patterns in stock returns

**Authors:** Lawrence Harris  
**Publication:** Journal of Financial Economics 16(1), 99–117 (1986)  
**Primary research source:** https://doi.org/10.1016/0304-405X(86)90044-9
**DOI:** https://doi.org/10.1016/0304-405X(86)90044-9

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Analyzes transaction-level historical patterns in day-of-week and intraday returns, including how the first part of the trading day differs by weekday.

## Author-reported finding or theoretical scope
Authors report weekday differences in first 45 minutes and last-trade price effects in their historical equity transaction sample.

## Required data / feasibility gate
Historical print/quote-aligned returns, spread-matched fills, market open/closing auctions and calendar identifiers.

## Critique / potential failure
Daypart anomalies are sample-dependent and may reflect bid/ask bounce or auction pricing; 1980s effects cannot be treated as current SPY/HOD/LOD rules.

## Falsifiable follow-up (proposal only)
Pre-register weekday × time-of-day windows and examine net future-return predictability on recent minute data with multiple-testing correction.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/11 Intraday Price Structure/README|Intraday Price Structure]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
