---
type: paper
paper_id: PAPER-53
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "08 Regime Detection"
year: 2007
doi: "10.1016/j.jedc.2006.12.004"
source_url: "https://doi.org/10.1016/j.jedc.2006.12.004"
replicated: false
---
# PAPER-53 — Asset allocation under multivariate regime switching

**Authors:** Massimo Guidolin; Allan Timmermann  
**Venue/year:** Journal of Economic Dynamics and Control 31(11), 3503–3544 (2007)  
**Verified primary source:** https://doi.org/10.1016/j.jedc.2006.12.004  
**DOI:** https://doi.org/10.1016/j.jedc.2006.12.004

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Models joint stock/bond return distribution with states characterized by different means, variances and correlations and evaluates regime-aware portfolio decisions.

## Grounded finding / scope (authors, not our result)
Finds evidence supporting multiple market regimes including crash, slow growth, bull and recovery in historical stock/bond returns; recommended exposures depend on state probabilities and investment horizon.

## Required data and feasible replication
Long point-in-time joint stock/bond return series, risk-free rates, true release timestamps, training-only transition matrix and constrained portfolio weights.

## Challenges, alternatives and invalid inference
Regime probabilities are estimated, not observed. Recovered historical states and optimal hindsight weights create severe lookahead if reused as live labels.

## Candidate falsifiable experiment — proposed only
Compare one-sided filtered-regime allocation to rolling-covariance risk-parity and static 60/40 on chronological unseen data with turnover and leverage caps.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/08 Regime Detection/README|Regime Detection]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
