---
type: paper
paper_id: PAPER-070
status: primary-source-abstract-screened
category: "05 Deep Learning"
year: 2023
reviewed_on: 2026-10-13
doi: "10.1111/mafi.12413"
source_url: "https://onlinelibrary.wiley.com/doi/full/10.1111/mafi.12413"
replicated: false
---
# PAPER-070 — Deep order flow imbalance: Extracting alpha at multiple horizons from the limit order book

**Authors:** Petter N. Kolm; Jeremy Turiel; Nicholas Westray  
**Publication:** Mathematical Finance 33(4), 1044–1081 (2023)  
**Primary research source:** https://onlinelibrary.wiley.com/doi/full/10.1111/mafi.12413
**DOI:** https://doi.org/10.1111/mafi.12413

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Tests deep high-frequency forecasting models on stationary order-flow features versus raw limit order book states across multiple response horizons.

## Author-reported finding or theoretical scope
Authors report gains from order-flow features for forecasts on 115 Nasdaq stocks, with effective price-prediction horizon near two price changes.

## Required data / feasibility gate
Event-level multi-level book/LOBSTER data, queue execution simulator and synchronized signed flow from 115-stock type universe.

## Critique / potential failure
Vendor data are not freely redistributed; prediction quality is not after-cost profit; overlapping event horizons can invalidate naive CV.

## Falsifiable follow-up (proposal only)
Contrast deep OFI models with simple OFI and logistic baselines using embargoed chronological holdouts, then model feasible next-queue executions.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/05 Deep Learning/README|Deep Learning]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
