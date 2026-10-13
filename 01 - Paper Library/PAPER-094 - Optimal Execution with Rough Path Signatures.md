---
type: paper
paper_id: "PAPER-094"
status: "source-screened-not-replicated"
category: "03 Market Microstructure"
reviewed_on: 2026-10-13
source_url: "https://doi.org/10.1137/19M1259778"
independently_validated: false
---
# PAPER-094 — Optimal Execution with Rough Path Signatures

**Authors:** Jasdeep Kalsi; Terry Lyons; Imanol Perez Arribas  
**Venue:** SIAM Journal on Financial Mathematics (2020)  
**Source:** https://doi.org/10.1137/19M1259778

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Optimize a trade schedule as a linear functional of a rough-path signature under price-impact functions.

## Data and implementation feasibility
**GAP: requires intraday trades, quote and fill data; synthetic demonstration feasible**.

## Candidate falsifiable hypothesis — NOT TESTED
Does a signature execution policy lower implementation shortfall versus TWAP under equal completion risk?

## Comparator(s) and explicit falsification requirement
**Baselines:** TWAP, VWAP, Almgren–Chriss.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Market-impact simulations fitted using future data yield invalid live claims.

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
