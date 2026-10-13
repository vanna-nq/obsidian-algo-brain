---
type: paper
paper_id: "PAPER-100"
status: "source-screened-not-replicated"
category: "10 Optimization and Physics"
reviewed_on: 2026-10-13
source_url: "https://arxiv.org/abs/cond-mat/9609144"
independently_validated: false
---
# PAPER-100 — Price variations in a stock market with many agents

**Authors:** Per Bak; Maya Paczuski; Martin Shubik  
**Venue:** arXiv:cond-mat/9609144 (1996)  
**Source:** https://arxiv.org/abs/cond-mat/9609144

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Imitation-driven price moves linked in a stylized setting to diffusing/annihilating particles.

## Data and implementation feasibility
**SYNTHETIC: interacting-agent simulation and empirical comparisons**.

## Candidate falsifiable hypothesis — NOT TESTED
Do frozen crowd imitation models reproduce multi-scale burst durations better than equally parameterized null models?

## Comparator(s) and explicit falsification requirement
**Baselines:** Random walk, GARCH, block bootstrap.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Physical analogy is not identification of real trader identities.

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
