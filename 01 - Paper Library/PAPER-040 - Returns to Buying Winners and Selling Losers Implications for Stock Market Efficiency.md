---
type: paper
paper_id: PAPER-040
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "02 Trend and Momentum"
year: 1993
doi: "10.1111/j.1540-6261.1993.tb04702.x"
source_url: "https://doi.org/10.1111/j.1540-6261.1993.tb04702.x"
replicated: false
---
# PAPER-040 — Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency

**Authors:** Narasimhan Jegadeesh; Sheridan Titman  
**Venue/year:** The Journal of Finance 48(1), 65–91 (1993)  
**Verified primary source:** https://doi.org/10.1111/j.1540-6261.1993.tb04702.x  
**DOI:** https://doi.org/10.1111/j.1540-6261.1993.tb04702.x

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Cross-sectional momentum: rank assets on historical returns, buy relative winners and sell relative losers for multi-month horizons.

## Grounded finding / scope (authors, not our result)
The authors document positive average returns over 3–12-month holding periods in their stock sample and partial subsequent reversal. This is not time-series or intraday momentum.

## Required data and feasible replication
Historical common-stock returns, delisting adjustments, point-in-time investability, borrow costs, turnover, risk factors and realistic portfolio formation/holding lag.

## Challenges, alternatives and invalid inference
Losers may be hard to short and exhibit crash risk; survivorship/selection biases and factor exposure confound naive replications; cannot import parameters into SPY 5-minute trend trades.

## Candidate falsifiable experiment — proposed only
Reproduce a single preregistered 6-month rank/6-month holding version in post-1993 periods, controlling for risk factors, turnover, borrow and momentum crashes.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/02 Trend and Momentum/README|Trend and Momentum]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
