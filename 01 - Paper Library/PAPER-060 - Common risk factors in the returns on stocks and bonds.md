---
type: paper
paper_id: PAPER-060
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "12 Cross Asset and Macro"
year: 1993
doi: "10.1016/0304-405X(93)90023-5"
source_url: "https://doi.org/10.1016/0304-405X(93)90023-5"
replicated: false
---
# PAPER-060 — Common risk factors in the returns on stocks and bonds

**Authors:** Eugene F. Fama; Kenneth R. French  
**Venue/year:** Journal of Financial Economics 33(1), 3–56 (1993)  
**Verified primary source:** https://doi.org/10.1016/0304-405X(93)90023-5  
**DOI:** https://doi.org/10.1016/0304-405X(93)90023-5

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Identifies common stock and bond factor dimensions related to market, size, value, bond maturity and default-risk return exposures.

## Grounded finding / scope (authors, not our result)
Empirical evidence suggests systematic factor covariation helps explain realized average stock/bond returns and cross-sectional differences; factors are not direct intraday alpha generators.

## Required data and feasible replication
Point-in-time stock returns and fundamentals, bond maturity and ratings/term factors, corporate-action-safe history, released factor construction rules.

## Challenges, alternatives and invalid inference
Factor exposure can falsely appear as alpha; lookahead in company accounting data and changing bond composition affects regressions and hedges.

## Candidate falsifiable experiment — proposed only
Regress strategy returns on lagged tradable stock/bond factor proxies and test whether residual net alpha persists across held-out periods and cost assumptions.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/12 Cross Asset and Macro/README|Cross Asset and Macro]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
