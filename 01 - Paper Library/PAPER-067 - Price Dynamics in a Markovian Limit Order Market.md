---
type: paper
paper_id: PAPER-067
status: primary-source-abstract-screened
category: "03 Market Microstructure"
year: 2013
reviewed_on: 2026-10-13
doi: "10.1137/110856605"
source_url: "https://epubs.siam.org/doi/10.1137/110856605"
replicated: false
---
# PAPER-067 — Price Dynamics in a Markovian Limit Order Market

**Authors:** Rama Cont; Adrien de Larrard  
**Publication:** SIAM Journal on Financial Mathematics 4(1), 1–25 (2013)  
**Primary research source:** https://epubs.siam.org/doi/10.1137/110856605
**DOI:** https://doi.org/10.1137/110856605

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Represents limit-order and market-order arrivals and cancellations as a queueing system that governs endogenous price changes.

## Author-reported finding or theoretical scope
Provides analytical relationships for price-change timing, up-move probability conditional on queue state, and a price-process diffusion limit.

## Required data / feasibility gate
Level-1 bid/ask queue sizes and event-level messages for market, limit and cancellation events plus execution-timing data.

## Critique / potential failure
Queue-based probabilities depend on simplified assumptions; order-book imbalance is not accurately measurable using 5-minute candles.

## Falsifiable follow-up (proposal only)
Compare predicted next-price-move probability from calibrated queue model with simple imbalance and logistic baselines in untouched event-time L1/L2 data.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/03 Market Microstructure/README|Market Microstructure]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
