---
type: paper
paper_id: PAPER-050
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "07 Volatility and Derivatives"
year: 2009
doi: "10.1016/j.jfineco.2009.01.001"
source_url: "https://doi.org/10.1016/j.jfineco.2009.01.001"
replicated: false
---
# PAPER-050 — Cross-section of option returns and volatility

**Authors:** Amit Goyal; Alessio Saretto  
**Venue/year:** Journal of Financial Economics 94(2), 310–326 (2009)  
**Verified primary source:** https://doi.org/10.1016/j.jfineco.2009.01.001  
**DOI:** https://doi.org/10.1016/j.jfineco.2009.01.001

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Rank underlying equities by the gap between historical realized stock volatility and contemporaneous at-the-money option-implied volatility; study subsequent option returns.

## Grounded finding / scope (authors, not our result)
Finds a statistically and economically significant historical long-short option-return differential across stock sorts. The strategy is distinct from simply buying or selling VIX.

## Required data and feasible replication
Timestamped liquid option chains, stock histories, rates, expiries, exercise/assignment rules, quote spreads and tradability constraints.

## Challenges, alternatives and invalid inference
ATM implied minus realized volatility often proxies different risks, including jump/tail and demand; historical average returns may hide extreme short-option losses and stale prints.

## Candidate falsifiable experiment — proposed only
Fix maturity, moneyness and volatility measurement ex ante; run post-publication option-chain backtest with executable bid-ask, spread stress, margin and worst-decile tail loss.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/07 Volatility and Derivatives/README|Volatility and Derivatives]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
