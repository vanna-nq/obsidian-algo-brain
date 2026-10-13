---
type: paper
paper_id: PAPER-056
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "10 Optimization and Physics"
year: 2009
doi: "10.1093/rfs/hhm075"
source_url: "https://doi.org/10.1093/rfs/hhm075"
replicated: false
---
# PAPER-056 — Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?

**Authors:** Victor DeMiguel; Lorenzo Garlappi; Raman Uppal  
**Venue/year:** The Review of Financial Studies 22(5) (2009)  
**Verified primary source:** https://doi.org/10.1093/rfs/hhm075  
**DOI:** https://doi.org/10.1093/rfs/hhm075

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Empirically compares estimated mean-variance and constrained optimized allocations with simple equal-weight allocations under out-of-sample estimation error.

## Grounded finding / scope (authors, not our result)
Finds many studied optimized allocation methods fail to consistently beat a simple 1/N benchmark out of sample across tested datasets, highlighting estimation risk.

## Required data and feasible replication
Asset return matrices, rolling means/covariances, asset availability and rebalance costs, leverage and short-selling rules.

## Challenges, alternatives and invalid inference
A mathematically exact optimizer can give economically poor portfolios under covariance/mean estimation error; selecting the winner after seeing OOS defeats the lesson.

## Candidate falsifiable experiment — proposed only
Run minimum-variance, regularized mean-variance and equal-weight allocations on non-overlapping future windows with turnover and estimation errors recorded.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/10 Optimization and Physics/README|Optimization and Physics]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
