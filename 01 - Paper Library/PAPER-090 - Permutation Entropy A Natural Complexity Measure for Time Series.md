---
type: paper
paper_id: "PAPER-090"
status: "source-screened-not-replicated"
category: "06 Information Theory"
reviewed_on: 2026-10-13
source_url: "https://doi.org/10.1103/PhysRevLett.88.174102"
independently_validated: false
---
# PAPER-090 — Permutation Entropy: A Natural Complexity Measure for Time Series

**Authors:** Christoph Bandt; Bernd Pompe  
**Venue:** Physical Review Letters 88, 174102 (2002)  
**Source:** https://doi.org/10.1103/PhysRevLett.88.174102

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Ordinal patterns encode relative order and entropy measures sequence complexity robust to scale.

## Data and implementation feasibility
**DIRECT: GC 5m, SPX500 1h, NVDA/SMH 5m**.

## Candidate falsifiable hypothesis — NOT TESTED
Does fixed rolling ordinal entropy predict next-six-bar volatility or trend continuation beyond simple autocorrelation?

## Comparator(s) and explicit falsification requirement
**Baselines:** Volatility, momentum and order-preserving surrogate baselines.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Embedding order/delay/window tuning is a major data-mining hazard.

## One-task research execution contract
1. Verify full paper formulas, version, dataset path, ticker, time frame and exact available date ranges. Dataset preview **before coding**.
2. Freeze one horizon, targets, null models, hyperparameter search budget, primary metric, chronological holdout and failure rule.
3. Train only on past data. For test evaluation, forbid lookahead in rolling statistics, close-to-open execution, bar timestamps, or future-estimated scaling.
4. Report actual executed tool evidence, code and hashes; keep unsuccessful variants and exclude data-snooped feature permutations.
5. Stop after this single controlled test. Any changes require a newly numbered experiment; never promote literature claims to validated models.

## Wiki links
- [[02 - Trading Methodologies/06 Information Theory/README|Information Theory]]
- [[01 - Paper Library/RESEARCH FRONTIER|Research Frontier]]
- [[01 - Paper Library/RESEARCH CATALOG|Complete Research Catalog]]
