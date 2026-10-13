---
type: paper
paper_id: PAPER-057
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "10 Optimization and Physics"
year: 2019
doi: "10.1016/j.revip.2019.100028"
source_url: "https://doi.org/10.1016/j.revip.2019.100028"
replicated: false
---
# PAPER-057 — Quantum computing for finance: Overview and prospects

**Authors:** Román Orús; Samuel Mugel; Enrique Lizaso  
**Venue/year:** Reviews in Physics 4, 100028 (2019)  
**Verified primary source:** https://doi.org/10.1016/j.revip.2019.100028  
**DOI:** https://doi.org/10.1016/j.revip.2019.100028

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Survey of quantum optimization, annealing, finance applications and possible Monte Carlo acceleration; includes portfolio and credit examples.

## Grounded finding / scope (authors, not our result)
A technical review of methods and prospects, not an experimental demonstration of quantum advantage over best classical financial solvers.

## Required data and feasible replication
Explicit binary portfolio objective, constraints, coefficient scaling, hardware/solver specs, classical exact and heuristic baselines.

## Challenges, alternatives and invalid inference
Annealing and quantum-inspired computation do not create predictive financial information; QUBO penalty tuning and hardware performance can dominate stated improvements.

## Candidate falsifiable experiment — proposed only
Translate a cardinality-constrained portfolio into QUBO, audit exhaustive tiny cases and compare feasible objective quality and wall-clock vs modern MIP/classical annealing.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/10 Optimization and Physics/README|Optimization and Physics]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
