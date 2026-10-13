---
type: paper
paper_id: PAPER-051
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "07 Volatility and Derivatives"
year: 2011
doi: "10.1016/j.jeconom.2010.03.033"
source_url: "https://doi.org/10.1016/j.jeconom.2010.03.033"
replicated: false
---
# PAPER-051 — Dynamic estimation of volatility risk premia and investor risk aversion from option-implied and realized volatilities

**Authors:** Tim Bollerslev; Michael Gibson; Hao Zhou  
**Venue/year:** Journal of Econometrics 160(1), 235–245 (2011)  
**Verified primary source:** https://doi.org/10.1016/j.jeconom.2010.03.033  
**DOI:** https://doi.org/10.1016/j.jeconom.2010.03.033

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Estimates time-varying volatility risk compensation by combining model-free option-implied variance and high-frequency realized-volatility evidence.

## Grounded finding / scope (authors, not our result)
Authors report temporal dependence in estimated volatility risk premia, links to macro-finance conditions and predictive relations for future stock returns.

## Required data and feasible replication
Five-minute S&P returns, contemporaneous model-free implied variance, option quotes and macro release dates; precise horizon agreement.

## Challenges, alternatives and invalid inference
Premium sign convention and scaling must be declared; historical realized variance estimates are not forward forecasts; options interpolation and term mismatch can create pseudo-signals.

## Candidate falsifiable experiment — proposed only
Estimate a lagged variance-premium signal against VIX and realized-vol baselines; assess forecast stability and after-cost usefulness on strictly post-2011 data.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/07 Volatility and Derivatives/README|Volatility and Derivatives]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
