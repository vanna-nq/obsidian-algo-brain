---
type: paper
paper_id: PAPER-061
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "12 Cross Asset and Macro"
year: 2009
doi: "10.1086/593088"
source_url: "https://www.nber.org/books-and-chapters/nber-macroeconomics-annual-2008-volume-23/carry-trades-and-currency-crashes"
replicated: false
---
# PAPER-061 — Carry Trades and Currency Crashes

**Authors:** Markus K. Brunnermeier; Stefan Nagel; Lasse H. Pedersen  
**Venue/year:** NBER Macroeconomics Annual 2008, Vol. 23 (published 2009) (2009)  
**Verified primary source:** https://www.nber.org/books-and-chapters/nber-macroeconomics-annual-2008-volume-23/carry-trades-and-currency-crashes  
**DOI:** https://doi.org/10.1086/593088

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Explains negative skew, crash losses and abrupt unwinding of currency carry exposures in terms of global funding liquidity and risk appetite.

## Grounded finding / scope (authors, not our result)
Authors document negatively skewed returns for high-vs-low-interest currency carry and association of unwinding with funding liquidity distress.

## Required data and feasible replication
Point-in-time currency spot, forwards/carry rates, funding spread and rate histories, shorting/margin/executable rollover rules.

## Challenges, alternatives and invalid inference
Positive average carry can conceal fat left tails; currency data require matching time-zone and funding conventions; overnight risk cannot be ignored.

## Candidate falsifiable experiment — proposed only
Freeze FX carry definition, compare raw and ex-ante funding-stress-gated strategies in untouched periods using realistic rolls and tail expected shortfall.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/12 Cross Asset and Macro/README|Cross Asset and Macro]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
