---
type: paper
paper_id: "PAPER-104"
status: "source-screened-not-replicated"
category: "11 Intraday Price Structure"
reviewed_on: 2026-10-13
source_url: "https://doi.org/10.1371/journal.pone.0188814"
independently_validated: false
---
# PAPER-104 — A model for foreign exchange markets based on glassy Brownian systems

**Authors:** Sanchez-Granero; Trinidad-Segovia; Clara-Rahola; Puertas; de las Nieves  
**Venue:** PLOS ONE 12, e0188814 (2017)  
**Source:** https://doi.org/10.1371/journal.pone.0188814

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Two-timescale glassy particle diffusion adapts to exchange-rate displacement distributions.

## Data and implementation feasibility
**DIRECT ADAPTATION: GC 5m; ORIGINAL TEST requires multiple FX rates 1m**.

## Candidate falsifiable hypothesis — NOT TESTED
Do two-timescale diffusion parameters improve held-out return tail likelihood vs single-scale stochastic-volatility baselines?

## Comparator(s) and explicit falsification requirement
**Baselines:** Student-t GARCH, Gaussian and two-regime normal mixture.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Qualitative analogy and in-sample fit are not predictive validation.

## One-task research execution contract
1. Verify full paper formulas, version, dataset path, ticker, time frame and exact available date ranges. Dataset preview **before coding**.
2. Freeze one horizon, targets, null models, hyperparameter search budget, primary metric, chronological holdout and failure rule.
3. Train only on past data. For test evaluation, forbid lookahead in rolling statistics, close-to-open execution, bar timestamps, or future-estimated scaling.
4. Report actual executed tool evidence, code and hashes; keep unsuccessful variants and exclude data-snooped feature permutations.
5. Stop after this single controlled test. Any changes require a newly numbered experiment; never promote literature claims to validated models.

## Wiki links
- [[02 - Trading Methodologies/11 Intraday Price Structure/README|Intraday Price Structure]]
- [[01 - Paper Library/RESEARCH FRONTIER|Research Frontier]]
- [[01 - Paper Library/RESEARCH CATALOG|Complete Research Catalog]]
