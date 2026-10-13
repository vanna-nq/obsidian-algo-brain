---
type: paper
paper_id: "PAPER-091"
status: "source-screened-not-replicated"
category: "08 Regime Detection"
reviewed_on: 2026-10-13
source_url: "https://arxiv.org/abs/1703.04385"
independently_validated: false
---
# PAPER-091 — Topological Data Analysis of Financial Time Series: Landscapes of Crashes

**Authors:** Marian Gidea; Yuri Katz  
**Venue:** Physica A / arXiv:1703.04385 (2017)  
**Source:** https://arxiv.org/abs/1703.04385

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Persistent homology of multi-index return point clouds detects evolving loops and crash-associated landscapes.

## Data and implementation feasibility
**GAP: need four or more synchronized equity indices; two asset versions are adaptations**.

## Candidate falsifiable hypothesis — NOT TESTED
Do lagged persistence-landscape features improve future systemic drawdown alerts at fixed false-alarm count?

## Comparator(s) and explicit falsification requirement
**Baselines:** VIX, realized vol, average correlation.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Rare crash sample, event-based selection and hindsight have high false-discovery risk.

## One-task research execution contract
1. Verify full paper formulas, version, dataset path, ticker, time frame and exact available date ranges. Dataset preview **before coding**.
2. Freeze one horizon, targets, null models, hyperparameter search budget, primary metric, chronological holdout and failure rule.
3. Train only on past data. For test evaluation, forbid lookahead in rolling statistics, close-to-open execution, bar timestamps, or future-estimated scaling.
4. Report actual executed tool evidence, code and hashes; keep unsuccessful variants and exclude data-snooped feature permutations.
5. Stop after this single controlled test. Any changes require a newly numbered experiment; never promote literature claims to validated models.

## Wiki links
- [[02 - Trading Methodologies/08 Regime Detection/README|Regime Detection]]
- [[01 - Paper Library/RESEARCH FRONTIER|Research Frontier]]
- [[01 - Paper Library/RESEARCH CATALOG|Complete Research Catalog]]
