---
type: paper
paper_id: PAPER-43
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "03 Market Microstructure"
year: 2001
doi: "10.21314/JOR.2001.041"
source_url: "https://doi.org/10.21314/JOR.2001.041"
replicated: false
---
# PAPER-43 — Optimal Execution of Portfolio Transactions

**Authors:** Robert Almgren; Neil Chriss  
**Venue/year:** Journal of Risk 3(2) (2001)  
**Verified primary source:** https://doi.org/10.21314/JOR.2001.041  
**DOI:** https://doi.org/10.21314/JOR.2001.041

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Balances risk from delaying execution against temporary and permanent price impact; under a linear model derives efficient liquidation trajectories.

## Grounded finding / scope (authors, not our result)
Analytical optimal-execution model and liquidation-cost frontier. It is not alpha forecasting research and does not report a universal fill/slippage rate.

## Required data and feasible replication
Asset liquidity and volatility by horizon, market impact calibrated to order participation, order size, latency and broker execution logs.

## Challenges, alternatives and invalid inference
Linear impact and stationary volatility assumptions can break in volatile conditions; hidden liquidity, queue priority and market response affect realized costs.

## Candidate falsifiable experiment — proposed only
Compare precommitted model schedules to TWAP/VWAP and immediate market-order baselines at equal completion risk using actual historical trade/quote replay.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/03 Market Microstructure/README|Market Microstructure]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
