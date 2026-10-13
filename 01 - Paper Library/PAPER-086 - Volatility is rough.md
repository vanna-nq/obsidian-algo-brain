---
type: paper
paper_id: "PAPER-086"
status: "source-screened-not-replicated"
category: "07 Volatility and Derivatives"
reviewed_on: 2026-10-13
source_url: "https://doi.org/10.1080/14697688.2017.1393551"
independently_validated: false
---
# PAPER-086 — Volatility is rough

**Authors:** Gatheral; Jaisson; Rosenbaum  
**Venue:** Quantitative Finance 18(6) (2018)  
**Source:** https://doi.org/10.1080/14697688.2017.1393551

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Rough fractional log-volatility with Hurst H well below 1/2.

## Data and implementation feasibility
**GC 5m, SPX500 1h, NVDA/SMH 5m: estimate past realized-vol scaling**.

## Candidate falsifiable hypothesis — NOT TESTED
Does rolling roughness improve next-session realized-volatility QLIKE versus HAR-RV?

## Comparator(s) and explicit falsification requirement
**Baselines:** HAR-RV and EWMA.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Sampling noise, overlap, seasonality, biased H estimates.

## One-task research execution contract
1. Verify full paper formulas, version, dataset path, ticker, time frame and exact available date ranges. Dataset preview **before coding**.
2. Freeze one horizon, targets, null models, hyperparameter search budget, primary metric, chronological holdout and failure rule.
3. Train only on past data. For test evaluation, forbid lookahead in rolling statistics, close-to-open execution, bar timestamps, or future-estimated scaling.
4. Report actual executed tool evidence, code and hashes; keep unsuccessful variants and exclude data-snooped feature permutations.
5. Stop after this single controlled test. Any changes require a newly numbered experiment; never promote literature claims to validated models.

## Wiki links
- [[02 - Trading Methodologies/07 Volatility and Derivatives/README|Volatility and Derivatives]]
- [[01 - Paper Library/RESEARCH FRONTIER|Research Frontier]]
- [[01 - Paper Library/RESEARCH CATALOG|Complete Research Catalog]]
