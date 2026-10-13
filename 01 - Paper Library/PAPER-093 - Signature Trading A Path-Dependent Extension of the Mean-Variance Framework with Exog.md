---
type: paper
paper_id: "PAPER-093"
status: "source-screened-not-replicated"
category: "10 Optimization and Physics"
reviewed_on: 2026-10-13
source_url: "https://arxiv.org/abs/2308.15135"
independently_validated: false
---
# PAPER-093 — Signature Trading: A Path-Dependent Extension of the Mean-Variance Framework with Exogenous Signals

**Authors:** Owen Futter; Blanka Horvath; Magnus Wiese  
**Venue:** arXiv:2308.15135 (2023 preprint)  
**Source:** https://arxiv.org/abs/2308.15135

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Rough-path signatures encode ordering and cross-terms of multivariate historical signal paths.

## Data and implementation feasibility
**DIRECT ADAPTATION: GC 5m, NVDA/SMH 5m, SPX500 1h**.

## Candidate falsifiable hypothesis — NOT TESTED
Does low-order price-vol-volume path signature add out-of-sample predictive utility over conventional lag features?

## Comparator(s) and explicit falsification requirement
**Baselines:** Ridge, boosted trees and shuffled path order.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
High-dimensional signatures, path normalization and overlapping targets can overfit.

## One-task research execution contract
1. Verify full paper formulas, version, dataset path, ticker, time frame and exact available date ranges. Dataset preview **before coding**.
2. Freeze one horizon, targets, null models, hyperparameter search budget, primary metric, chronological holdout and failure rule.
3. Train only on past data. For test evaluation, forbid lookahead in rolling statistics, close-to-open execution, bar timestamps, or future-estimated scaling.
4. Report actual executed tool evidence, code and hashes; keep unsuccessful variants and exclude data-snooped feature permutations.
5. Stop after this single controlled test. Any changes require a newly numbered experiment; never promote literature claims to validated models.

## Wiki links
- [[02 - Trading Methodologies/10 Optimization and Physics/README|Optimization and Physics]]
- [[01 - Paper Library/RESEARCH FRONTIER|Research Frontier]]
- [[01 - Paper Library/RESEARCH CATALOG|Complete Research Catalog]]
