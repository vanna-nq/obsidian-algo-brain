---
type: paper
paper_id: PAPER-047
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "05 Deep Learning"
year: 2019
doi: "10.1080/14697688.2019.1571683"
source_url: "https://doi.org/10.1080/14697688.2019.1571683"
replicated: false
---
# PAPER-047 — Deep Hedging

**Authors:** Hans Buehler; Lukas Gonon; Josef Teichmann; Ben Wood  
**Venue/year:** Quantitative Finance 19(8), 1271–1291 (2019)  
**Verified primary source:** https://doi.org/10.1080/14697688.2019.1571683  
**DOI:** https://doi.org/10.1080/14697688.2019.1571683

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Uses deep reinforcement learning to learn derivative hedge decisions under nonlinear risk criteria, transaction costs and trading constraints.

## Grounded finding / scope (authors, not our result)
Authors demonstrate the architecture and synthetic-model hedging gains relative to some frictionless-style hedging benchmarks; this is a risk-management method, not a directional trading signal.

## Required data and feasible replication
Option surface, underlying paths, dates, hedge inventories, transaction costs, constraints, trading decisions and relevant simulated or actual scenarios.

## Challenges, alternatives and invalid inference
A successful result on Heston paths may not transport to live markets; financial risk criteria, simulation misspecification and tail robustness are crucial.

## Candidate falsifiable experiment — proposed only
Reproduce a synthetic one-option hedge with realistic proportional costs versus delta hedge and no-rehedge baselines; evaluate risk across unseen volatility regimes.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/05 Deep Learning/README|Deep Learning]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
