---
type: paper
paper_id: PAPER-038
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "01 Statistical Arbitrage"
year: 2010
doi: "10.2469/faj.v66.n4.1"
source_url: "https://rpc.cfainstitute.org/research/financial-analysts-journal/2010/does-simple-pairs-trading-still-work"
replicated: false
---
# PAPER-038 — Does Simple Pairs Trading Still Work?

**Authors:** Binh Do; Robert Faff  
**Venue/year:** Financial Analysts Journal 66(4) (2010)  
**Verified primary source:** https://rpc.cfainstitute.org/research/financial-analysts-journal/2010/does-simple-pairs-trading-still-work  
**DOI:** https://doi.org/10.2469/faj.v66.n4.1

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Reassesses distance-based equity pairs profitability through newer market conditions and trading procedures.

## Grounded finding / scope (authors, not our result)
Finds that historical pairs-trading profitability has trended downward, while opportunities in turbulent periods and some alternative methods persist. This is a research finding, not a promise of a current executable edge.

## Required data and feasible replication
Survivorship-safe historical stock pairs, delistings, corporate actions, spreads, short/borrow costs, real-time formation sets and comparable industry controls.

## Challenges, alternatives and invalid inference
Historical pair-selection, structural breaks and market crowding can dominate; reported crisis returns should not be used as an ex-ante regime filter without retesting.

## Candidate falsifiable experiment — proposed only
Compare a completely frozen distance-pairs algorithm in chronological post-2010 data with a sector-matched random-pair null and realistic net returns.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/01 Statistical Arbitrage/README|Statistical Arbitrage]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
