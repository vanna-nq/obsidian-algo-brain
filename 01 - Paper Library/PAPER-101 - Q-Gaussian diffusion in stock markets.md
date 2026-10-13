---
type: paper
paper_id: "PAPER-101"
status: "source-screened-not-replicated"
category: "10 Optimization and Physics"
reviewed_on: 2026-10-13
source_url: "https://doi.org/10.1103/PhysRevE.99.062313"
independently_validated: false
---
# PAPER-101 — Q-Gaussian diffusion in stock markets

**Authors:** Alonso-Marroquin; Arias-Calluari; Harre; Najafi; Herrmann  
**Venue:** Physical Review E 99, 062313 (2019)  
**Source:** https://doi.org/10.1103/PhysRevE.99.062313

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Nonlinear porous-medium/Fokker-Planck dynamics and Tsallis q-Gaussian scaling of prices.

## Data and implementation feasibility
**DIRECT: SPX500 1h and GC 5m return scales**.

## Candidate falsifiable hypothesis — NOT TESTED
Do training-only q-Gaussian regimes improve held-out extreme-tail quantile forecasts?

## Comparator(s) and explicit falsification requirement
**Baselines:** Student-t, skew-t, GED, historical quantile.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Static density fit does not imply forecast gain; time aggregation may induce fake regimes.

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
