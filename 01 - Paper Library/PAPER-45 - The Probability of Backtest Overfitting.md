---
type: paper
paper_id: PAPER-45
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "04 Machine Learning"
year: 2017
doi: "10.21314/JCF.2016.322"
source_url: "https://www.risk.net/journal-of-computational-finance/2471206/the-probability-of-backtest-overfitting"
replicated: false
---
# PAPER-45 — The Probability of Backtest Overfitting

**Authors:** David H. Bailey; Jonathan M. Borwein; Marcos López de Prado; Qiji Jim Zhu  
**Venue/year:** Journal of Computational Finance (2017)  
**Verified primary source:** https://www.risk.net/journal-of-computational-finance/2471206/the-probability-of-backtest-overfitting  
**DOI:** https://doi.org/10.21314/JCF.2016.322

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Estimates risk that in-sample strategy rankings fail out-of-sample via combinatorially symmetric cross-validation (CSCV) and performance ranks.

## Grounded finding / scope (authors, not our result)
Authors propose and numerically illustrate the probability-of-backtest-overfitting metric; it is a diagnostic of multiple-comparison bias, not a guarantee of live performance.

## Required data and feasible replication
All compared parameter/model variants' date-aligned return streams, chosen train/test partitions, costs and sample chronology.

## Challenges, alternatives and invalid inference
CSCV rearranges temporal segments; it can violate causality if its splits are treated as an executable walk-forward path. Preserve a separate untouched chronological OOS test.

## Candidate falsifiable experiment — proposed only
Audit research logs for every tested variant, estimate PBO for the disclosed search universe and cross-check selected model on strict forward holdout.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/04 Machine Learning/README|Machine Learning]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
