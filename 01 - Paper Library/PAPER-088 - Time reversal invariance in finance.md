---
type: paper
paper_id: "PAPER-088"
status: "source-screened-not-replicated"
category: "06 Information Theory"
reviewed_on: 2026-10-13
source_url: "https://doi.org/10.1080/14697680802616712"
independently_validated: false
---
# PAPER-088 — Time reversal invariance in finance

**Authors:** Gilles Zumbach  
**Venue:** Quantitative Finance 9(5), 505–515 (2009)  
**Source:** https://doi.org/10.1080/14697680802616712

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Market statistics differ under reversal of time; past-return-to-volatility effects may differ from backward effects.

## Data and implementation feasibility
**GC 5m, SPX500 1h, NVDA/SMH 5m**.

## Candidate falsifiable hypothesis — NOT TESTED
Does a causal lag-asymmetry statistic improve next-horizon volatility forecasts?

## Comparator(s) and explicit falsification requirement
**Baselines:** GARCH, volatility-only and block-reversed surrogates.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Use reverse-time data only for offline diagnostics, never live features.

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
