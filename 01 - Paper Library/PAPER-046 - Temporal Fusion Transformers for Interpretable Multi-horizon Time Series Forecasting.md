---
type: paper
paper_id: PAPER-046
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "05 Deep Learning"
year: 2021
doi: "10.1016/j.ijforecast.2021.03.012"
source_url: "https://doi.org/10.1016/j.ijforecast.2021.03.012"
replicated: false
---
# PAPER-046 — Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting

**Authors:** Bryan Lim; Sercan Ö. Arık; Nicolas Loeff; Tomas Pfister  
**Venue/year:** International Journal of Forecasting 37(4), 1748–1764 (2021)  
**Verified primary source:** https://doi.org/10.1016/j.ijforecast.2021.03.012  
**DOI:** https://doi.org/10.1016/j.ijforecast.2021.03.012

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Neural forecasting combining recurrent local sequence processing, temporal attention, variable selection and gating across known future, past observed and static covariates.

## Grounded finding / scope (authors, not our result)
Authors report better multi-horizon forecast performance than tested model baselines on several generic datasets. The publication does not establish market or trading profitability.

## Required data and feasible replication
Timestamped multi-horizon targets, known-in-advance covariates separated from observed-only data, missing-value policy, chronological splits and compute budget.

## Challenges, alternatives and invalid inference
Attention weights are not causal explanations; news, macro and options variables may be revised or unavailable at prediction time; label overlap can inflate fit.

## Candidate falsifiable experiment — proposed only
On a non-overlapping SPY or index-futures forecast task, compare TFT to ridge, gradient boost and simple LSTM using equal data and out-of-sample log loss plus after-cost utility.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/05 Deep Learning/README|Deep Learning]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
