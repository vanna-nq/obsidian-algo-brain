---
type: paper
paper_id: PAPER-049
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "06 Information Theory"
year: 2009
doi: "10.1103/PhysRevLett.103.238701"
source_url: "https://doi.org/10.1103/PhysRevLett.103.238701"
replicated: false
---
# PAPER-049 — Granger Causality and Transfer Entropy Are Equivalent for Gaussian Variables

**Authors:** Lionel Barnett; Adam B. Barrett; Anil K. Seth  
**Venue/year:** Physical Review Letters 103, 238701 (2009)  
**Verified primary source:** https://doi.org/10.1103/PhysRevLett.103.238701  
**DOI:** https://doi.org/10.1103/PhysRevLett.103.238701

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Proves equivalence of a predictive Granger-causality measure and transfer entropy for Gaussian random processes under the paper's assumptions.

## Grounded finding / scope (authors, not our result)
A foundational equivalence result, not proof of economic causal mechanisms or profits. Nonlinear and non-Gaussian market data need additional care.

## Required data and feasible replication
Synchronously timestamped signal and target return series, lag design, adequate conditioning variables and stationary/robust model estimators.

## Challenges, alternatives and invalid inference
Granger and transfer entropy measure statistical directed dependence, not intervention-level causality; common drivers, lead/lag shifts and alpha selection can create false directionality.

## Candidate falsifiable experiment — proposed only
Use Gaussian-surrogate simulations to check agreement of estimators, then hold out true financial series and compare incremental predictive log loss versus zero-lag and lag-shuffled controls.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/06 Information Theory/README|Information Theory]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
