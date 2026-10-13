---
type: paper
paper_id: PAPER-041
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "02 Trend and Momentum"
year: 2017
doi: "10.1111/jofi.12513"
source_url: "https://doi.org/10.1111/jofi.12513"
replicated: false
---
# PAPER-041 — Volatility-Managed Portfolios

**Authors:** Alan Moreira; Tyler Muir  
**Venue/year:** The Journal of Finance 72(4), 1611–1644 (2017)  
**Verified primary source:** https://doi.org/10.1111/jofi.12513  
**DOI:** https://doi.org/10.1111/jofi.12513

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Scales systematic factor exposure inversely with lagged realized variance to test whether expected return adjusts sufficiently to compensate for changing risk.

## Grounded finding / scope (authors, not our result)
Authors report historical factor Sharpe improvements from inverse-volatility exposure management because volatility and expected returns have different dynamics.

## Required data and feasible replication
Total factor excess returns, risk-free rates, lagged daily/monthly variance, exposure/leverage constraints and funding costs.

## Challenges, alternatives and invalid inference
Levered volatility targeting can create extreme exposure in calm periods, with whipsaws and crash convexity; changes in volatility signal at decision time must be known; compare matched-volatility and equal-risk baselines.

## Candidate falsifiable experiment — proposed only
Fix inverse-variance sizing, caps and cost model, compare to constant-dollar and equal-target-vol exposures in unseen factor data, with severe gap-up/gap-down stress.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/02 Trend and Momentum/README|Trend and Momentum]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
