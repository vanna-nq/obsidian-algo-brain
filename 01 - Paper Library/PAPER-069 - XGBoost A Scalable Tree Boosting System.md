---
type: paper
paper_id: PAPER-069
status: primary-source-abstract-screened
category: "04 Machine Learning"
year: 2016
reviewed_on: 2026-10-13
doi: "10.1145/2939672.2939785"
source_url: "https://doi.org/10.1145/2939672.2939785"
replicated: false
---
# PAPER-069 — XGBoost: A Scalable Tree Boosting System

**Authors:** Tianqi Chen; Carlos Guestrin  
**Publication:** ACM SIGKDD 2016, 785–794 (2016)  
**Primary research source:** https://doi.org/10.1145/2939672.2939785
**DOI:** https://doi.org/10.1145/2939672.2939785

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Describes a regularized scalable gradient-tree boosting system with sparsity handling and approximate quantile sketch tree-building.

## Author-reported finding or theoretical scope
Algorithms and computer-systems results on generic machine learning benchmarks; no finance alpha is established.

## Required data / feasibility gate
Consistent lagged features and target horizon, chronology, train-only hyperparameter tuning and fair compute budget.

## Critique / potential failure
Leakage or repeated test-set tuning can make even a strong algorithm appear to discover false trading signals; interpretability claims require scrutiny.

## Falsifiable follow-up (proposal only)
Benchmark boosted trees against ridge and RF on the same frozen, realistic after-cost market prediction task, logging all search trials.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/04 Machine Learning/README|Machine Learning]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
