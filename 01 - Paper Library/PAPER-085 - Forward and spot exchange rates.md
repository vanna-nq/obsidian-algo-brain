---
type: paper
paper_id: PAPER-085
status: primary-source-abstract-screened
category: "12 Cross Asset and Macro"
year: 1984
reviewed_on: 2026-10-13
doi: "10.1016/0304-3932(84)90046-1"
source_url: "https://doi.org/10.1016/0304-3932(84)90046-1"
replicated: false
---
# PAPER-085 — Forward and spot exchange rates

**Authors:** Eugene F. Fama  
**Publication:** Journal of Monetary Economics 14(3), 319–338 (1984)  
**Primary research source:** https://doi.org/10.1016/0304-3932(84)90046-1
**DOI:** https://doi.org/10.1016/0304-3932(84)90046-1

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Decomposes forward exchange rate variation into time-varying expected spot movement and foreign exchange risk premiums.

## Author-reported finding or theoretical scope
Authors find that in historical data much forward-rate variation reflects risk premium rather than straightforward future spot appreciation.

## Required data / feasibility gate
Synchronous FX spot/forward quotes, benchmark interest rates, settlement, bid-ask, currency funding, rebalancing dates and realized future spot moves.

## Critique / potential failure
Spot forecast vs forward excess-return definitions differ; the forward premium puzzle does not mean a free carry strategy after funding and crash risks.

## Falsifiable follow-up (proposal only)
Reproduce a fixed forward-discount predictive regression in later eras, using investable currency excess returns and realistic roll/funding costs.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/12 Cross Asset and Macro/README|Cross Asset and Macro]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
