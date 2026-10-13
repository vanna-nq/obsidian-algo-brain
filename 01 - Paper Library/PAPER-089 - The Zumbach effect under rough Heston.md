---
type: paper
paper_id: "PAPER-089"
status: "source-screened-not-replicated"
category: "07 Volatility and Derivatives"
reviewed_on: 2026-10-13
source_url: "https://doi.org/10.1080/14697688.2019.1658889"
independently_validated: false
---
# PAPER-089 — The Zumbach effect under rough Heston

**Authors:** El Euch; Gatheral; Radoicic; Rosenbaum  
**Venue:** Quantitative Finance 20(2), 235–241 (2020)  
**Source:** https://doi.org/10.1080/14697688.2019.1658889

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Rough-Heston feedback produces past squared-return versus future-variance asymmetry missing in classical Heston.

## Data and implementation feasibility
**PARTIAL with OHLCV; full option calibration requires option chains**.

## Candidate falsifiable hypothesis — NOT TESTED
Can a lag-asymmetry proxy explain future realized variance and match rough-Heston simulated moments?

## Comparator(s) and explicit falsification requirement
**Baselines:** Heston, GARCH simulation nulls.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Bars cannot identify option-implied model dynamics or market-maker causality.

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
