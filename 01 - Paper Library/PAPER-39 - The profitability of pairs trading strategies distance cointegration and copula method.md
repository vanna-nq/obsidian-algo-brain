---
type: paper
paper_id: PAPER-39
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "01 Statistical Arbitrage"
year: 2016
doi: "10.1080/14697688.2016.1164337"
source_url: "https://doi.org/10.1080/14697688.2016.1164337"
replicated: false
---
# PAPER-39 — The profitability of pairs trading strategies: distance, cointegration and copula methods

**Authors:** Hossein Rad; Rand Kwong Yew Low; Robert Faff  
**Venue/year:** Quantitative Finance 16(10), 1541–1558 (2016)  
**Verified primary source:** https://doi.org/10.1080/14697688.2016.1164337  
**DOI:** https://doi.org/10.1080/14697688.2016.1164337

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Compares three structurally different relative-value pair-formation and signal definitions—distance, cointegration, and copula—with trading costs.

## Grounded finding / scope (authors, not our result)
Authors study US equities across 1962–2014 with time-varying costs, finding differences in profitability by strategy and market turbulence; copulas capture dependence beyond a linear spread.

## Required data and feasible replication
Point-in-time US common-stock universe, trading-cost histories, prices with delistings, rolling dependence fitting, lagged liquidity characteristics.

## Challenges, alternatives and invalid inference
A better in-sample fit of joint dependence is not necessarily better execution; copula family/tail parameter selection increases multiple testing; pair failures can cause fat losses.

## Candidate falsifiable experiment — proposed only
Freeze pair selection and transaction-cost protocol and compare all three methods in the same held-out years at equal net risk, using an explicit no-trade baseline.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/01 Statistical Arbitrage/README|Statistical Arbitrage]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
