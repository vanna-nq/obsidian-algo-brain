---
type: paper
paper_id: "PAPER-097"
status: "source-screened-not-replicated"
category: "03 Market Microstructure"
reviewed_on: 2026-10-13
source_url: "https://arxiv.org/abs/1502.04592"
independently_validated: false
---
# PAPER-097 — Hawkes processes in finance

**Authors:** Bacry; Mastromatteo; Muzy  
**Venue:** Market Microstructure and Liquidity 1, 1550005 (2015 review)  
**Source:** https://arxiv.org/abs/1502.04592

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Self- and cross-exciting point-process intensity models market-order bursts and cascading activity.

## Data and implementation feasibility
**GAP: real trade/quote event timestamps needed; candle events are a different proxy**.

## Candidate falsifiable hypothesis — NOT TESTED
Does a multivariate Hawkes model improve future event-arrival log-likelihood vs intraday-seasonal Poisson?

## Comparator(s) and explicit falsification requirement
**Baselines:** Seasonal Poisson and event-count autoregression.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
REVIEW article; bar-level aggregation does not identify microscopic excitation.

## One-task research execution contract
1. Verify full paper formulas, version, dataset path, ticker, time frame and exact available date ranges. Dataset preview **before coding**.
2. Freeze one horizon, targets, null models, hyperparameter search budget, primary metric, chronological holdout and failure rule.
3. Train only on past data. For test evaluation, forbid lookahead in rolling statistics, close-to-open execution, bar timestamps, or future-estimated scaling.
4. Report actual executed tool evidence, code and hashes; keep unsuccessful variants and exclude data-snooped feature permutations.
5. Stop after this single controlled test. Any changes require a newly numbered experiment; never promote literature claims to validated models.

## Wiki links
- [[02 - Trading Methodologies/03 Market Microstructure/README|Market Microstructure]]
- [[01 - Paper Library/RESEARCH FRONTIER|Research Frontier]]
- [[01 - Paper Library/RESEARCH CATALOG|Complete Research Catalog]]
