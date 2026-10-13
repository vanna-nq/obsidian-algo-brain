---
type: paper
paper_id: PAPER-044
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "04 Machine Learning"
year: 2000
doi: "10.1111/1468-0262.00152"
source_url: "https://doi.org/10.1111/1468-0262.00152"
replicated: false
---
# PAPER-044 — A Reality Check for Data Snooping

**Authors:** Halbert White  
**Venue/year:** Econometrica 68(5), 1097–1126 (2000)  
**Verified primary source:** https://doi.org/10.1111/1468-0262.00152  
**DOI:** https://doi.org/10.1111/1468-0262.00152

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Tests whether the best-performing member of a strategy/model search space truly outperforms a benchmark once the data-snooping search is accounted for.

## Grounded finding / scope (authors, not our result)
Develops a bootstrap-based reality check for superior predictive ability among many tried rules. This guards against false discoveries but does not replace a fresh holdout.

## Required data and feasible replication
Full predeclared candidate universe, dated differential returns against one benchmark, dependencies for block bootstrap and complete failed-strategy records.

## Challenges, alternatives and invalid inference
If only the winning strategy is retained, search penalty cannot be measured. Bootstrap assumptions and including many poor candidates affect power.

## Candidate falsifiable experiment — proposed only
Apply reality-check bootstrap to all retained research variants on a frozen window; separately validate the preselected winner in an untouched future period.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/04 Machine Learning/README|Machine Learning]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
