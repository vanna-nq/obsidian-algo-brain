---
type: paper
paper_id: "PAPER-102"
status: "source-screened-not-replicated"
category: "03 Market Microstructure"
reviewed_on: 2026-10-13
source_url: "https://doi.org/10.1080/14697688.2020.1841906"
independently_validated: false
---
# PAPER-102 — From quadratic Hawkes processes to super-Heston rough volatility models with Zumbach effect

**Authors:** Aditi Dandapani; Paul Jusselin; Mathieu Rosenbaum  
**Venue:** Quantitative Finance 21(8), 1235–1247 (2021)  
**Source:** https://doi.org/10.1080/14697688.2020.1841906

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Quadratic price-dependent excitation yields rough-volatility macro limits with time asymmetry.

## Data and implementation feasibility
**PARTIAL: OHLCV statistical moments; full needs trade events, option surfaces**.

## Candidate falsifiable hypothesis — NOT TESTED
Can nonlinear Hawkes simulation match empirical lag-asymmetry and roughness better than linear Hawkes?

## Comparator(s) and explicit falsification requirement
**Baselines:** Linear Hawkes, Heston, GARCH.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Bar proxies cannot identify high-frequency event excitation.

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
