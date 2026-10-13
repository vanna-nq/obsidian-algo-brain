---
type: paper
paper_id: PAPER-59
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "11 Intraday Price Structure"
year: 1997
doi: "10.1016/S0927-5398(97)00004-2"
source_url: "https://doi.org/10.1016/S0927-5398(97)00004-2"
replicated: false
---
# PAPER-59 — Intraday periodicity and volatility persistence in financial markets

**Authors:** Torben G. Andersen; Tim Bollerslev  
**Venue/year:** Journal of Empirical Finance 4(2–3), 115–158 (1997)  
**Verified primary source:** https://doi.org/10.1016/S0927-5398(97)00004-2  
**DOI:** https://doi.org/10.1016/S0927-5398(97)00004-2

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Separates predictable intraday volatility seasonality from stochastic volatility persistence in foreign exchange and equity markets.

## Grounded finding / scope (authors, not our result)
The authors show clock-time seasonal volatility has a substantial effect on measured high-frequency dynamics and must be accounted for before interpreting volatility clustering.

## Required data and feasible replication
High-quality minute/5-minute session bars, timezone/DST corrections, holidays, clock-time bins and stable 14–90 day seasonal estimators.

## Challenges, alternatives and invalid inference
Mixing different session clocks or rescaling against future sessions creates apparent predictable patterns; normalized volatility does not imply a directional trading edge.

## Candidate falsifiable experiment — proposed only
Compare raw vs causally seasonal-adjusted breakout thresholds for forecasting next 30-minute range and HOD/LOD formation probability with unseen-session calibration.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/11 Intraday Price Structure/README|Intraday Price Structure]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
