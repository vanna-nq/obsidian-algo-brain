---
type: paper
paper_id: PAPER-52
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "08 Regime Detection"
year: 1994
doi: "10.1016/0304-4076(94)90036-1"
source_url: "https://doi.org/10.1016/0304-4076(94)90036-1"
replicated: false
---
# PAPER-52 — Dynamic linear models with Markov-switching

**Authors:** Chang-Jin Kim  
**Venue/year:** Journal of Econometrics 60(1–2), 1–22 (1994)  
**Verified primary source:** https://doi.org/10.1016/0304-4076(94)90036-1  
**DOI:** https://doi.org/10.1016/0304-4076(94)90036-1

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Extends Hamilton Markov switching to state-space models allowing regime dependence in measurement/transition dynamics, with filtering, smoothing and likelihood estimation.

## Grounded finding / scope (authors, not our result)
Introduces an estimation/filtering framework and computational approximation for latent-regime dynamic linear models; not a trading-performance study.

## Required data and feasible replication
Consistent return/volatility series, model likelihood, time-filtered regime beliefs and diagnostic simulation; full implementation needs detailed math audit.

## Challenges, alternatives and invalid inference
Smoothing uses future data and is invalid as a historical live decision variable. Latent state labels are unidentified up to permutation, regime count selection is fragile.

## Candidate falsifiable experiment — proposed only
Simulate known two-regime data, prove online filtered state recovery without future access, then measure incremental risk-management value on held-out markets.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/08 Regime Detection/README|Regime Detection]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
