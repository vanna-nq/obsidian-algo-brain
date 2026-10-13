---
type: paper
paper_id: PAPER-55
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "09 Mean Reversion"
year: 2012
doi: "10.1093/rfs/hhs066"
source_url: "https://doi.org/10.1093/rfs/hhs066"
replicated: false
---
# PAPER-55 — Evaporating Liquidity

**Authors:** Stefan Nagel  
**Venue/year:** The Review of Financial Studies 25(7), 2005–2039 (2012)  
**Verified primary source:** https://doi.org/10.1093/rfs/hhs066  
**DOI:** https://doi.org/10.1093/rfs/hhs066

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Uses short-term stock return reversal as a proxy for compensation earned by liquidity providers, studying its time-variation with market stress.

## Grounded finding / scope (authors, not our result)
Reports substantially larger expected reversal/liquidity-provision returns in market turmoil and strong prediction from VIX changes/levels; a reflection of constrained liquidity supply.

## Required data and feasible replication
Liquid and illiquid stock price/quote histories, portfolio rebalancing constraints, historical VIX, spread, borrow, fill and market impact measures.

## Challenges, alternatives and invalid inference
Higher estimated return during stress comes with worse fills, defaults and capital constraints; a paper estimate of a liquidity premium does not imply a retail trader captures it.

## Candidate falsifiable experiment — proposed only
Compare a fixed, cost-aware short-term reversal portfolio across ex-ante VIX states, control for transaction costs and capacity, and assess liquidity-crisis tail risk.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/09 Mean Reversion/README|Mean Reversion]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
