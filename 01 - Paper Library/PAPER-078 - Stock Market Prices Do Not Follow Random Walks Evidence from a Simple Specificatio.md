---
type: paper
paper_id: PAPER-078
status: primary-source-abstract-screened
category: "09 Mean Reversion"
year: 1988
reviewed_on: 2026-10-13
doi: "10.1093/rfs/1.1.41"
source_url: "https://academic.oup.com/rfs/article-abstract/1/1/41/1601244"
replicated: false
---
# PAPER-078 — Stock Market Prices Do Not Follow Random Walks: Evidence from a Simple Specification Test

**Authors:** Andrew W. Lo; A. Craig MacKinlay  
**Publication:** Review of Financial Studies 1(1), 41–66 (1988)  
**Primary research source:** https://academic.oup.com/rfs/article-abstract/1/1/41/1601244
**DOI:** https://doi.org/10.1093/rfs/1.1.41

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Develops a variance-ratio test using stock-return estimates at different frequencies to examine a random-walk null with appropriate uncertainty treatment.

## Author-reported finding or theoretical scope
Authors reject the random-walk model for weekly US portfolio/index returns in historical samples, but explicitly say this does not itself establish mean-reverting price levels.

## Required data / feasibility gate
Historical investable index or stock return series, non-synchronous trading controls, variance-ratio statistics and heteroskedasticity-robust errors.

## Critique / potential failure
Rejection of IID increments need not imply stationarity, and 1980s weekly results do not license minute-by-minute reversal strategies.

## Falsifiable follow-up (proposal only)
Run a pre-specified variance-ratio test over future weekly and intraday intervals, correcting for microstructure noise and evaluating economic effect sizes.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/09 Mean Reversion/README|Mean Reversion]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
