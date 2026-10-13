---
type: paper
paper_id: PAPER-042
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "03 Market Microstructure"
year: 1991
doi: "10.1111/j.1540-6261.1991.tb03749.x"
source_url: "https://doi.org/10.1111/j.1540-6261.1991.tb03749.x"
replicated: false
---
# PAPER-042 — Measuring the Information Content of Stock Trades

**Authors:** Joel Hasbrouck  
**Venue/year:** The Journal of Finance 46(1), 179–207 (1991)  
**Verified primary source:** https://doi.org/10.1111/j.1540-6261.1991.tb03749.x  
**DOI:** https://doi.org/10.1111/j.1540-6261.1991.tb03749.x

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Uses a trade/quote vector autoregression to distinguish a trade innovation's longer-run price effect from transitory microstructure noise.

## Grounded finding / scope (authors, not our result)
The study finds delayed price-impact incorporation, a concave impact/size relationship and higher price impact with larger spreads in sampled NYSE stocks.

## Required data and feasible replication
Historical trade print timestamps, contemporaneous bid-ask quotes, matched quote updates, trade signs, and midquote response horizons.

## Challenges, alternatives and invalid inference
A contemporaneous quote response is not a tradable forecast; trade signing and quote alignment can be erroneous; venue fragmentation changes market structure.

## Candidate falsifiable experiment — proposed only
Fit a VAR on lagged signed trade/quote innovations and test future midprice response at genuinely tradable horizons against a lagged-return benchmark.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/03 Market Microstructure/README|Market Microstructure]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
