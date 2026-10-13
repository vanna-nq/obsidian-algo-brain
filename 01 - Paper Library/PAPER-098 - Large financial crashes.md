---
type: paper
paper_id: "PAPER-098"
status: "source-screened-not-replicated"
category: "08 Regime Detection"
reviewed_on: 2026-10-13
source_url: "https://doi.org/10.1016/S0378-4371(97)00318-X"
independently_validated: false
---
# PAPER-098 — Large financial crashes

**Authors:** Didier Sornette; Anders Johansen  
**Venue:** Physica A 245, 411–422 (1997)  
**Source:** https://doi.org/10.1016/S0378-4371(97)00318-X

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Log-periodic power-law acceleration hypothesized near speculative critical points.

## Data and implementation feasibility
**DIRECT LIMITED: SPX500 1h aggregated daily; few independent crashes**.

## Candidate falsifiable hypothesis — NOT TESTED
Do frozen forward-fitted LPPL alerts beat vol/drawdown baselines in future crash onset alerts?

## Comparator(s) and explicit falsification requirement
**Baselines:** Exponent trend and volatility threshold.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Extremely high look-elsewhere bias from window, time and critical-date scans.

## One-task research execution contract
1. Verify full paper formulas, version, dataset path, ticker, time frame and exact available date ranges. Dataset preview **before coding**.
2. Freeze one horizon, targets, null models, hyperparameter search budget, primary metric, chronological holdout and failure rule.
3. Train only on past data. For test evaluation, forbid lookahead in rolling statistics, close-to-open execution, bar timestamps, or future-estimated scaling.
4. Report actual executed tool evidence, code and hashes; keep unsuccessful variants and exclude data-snooped feature permutations.
5. Stop after this single controlled test. Any changes require a newly numbered experiment; never promote literature claims to validated models.

## Wiki links
- [[02 - Trading Methodologies/08 Regime Detection/README|Regime Detection]]
- [[01 - Paper Library/RESEARCH FRONTIER|Research Frontier]]
- [[01 - Paper Library/RESEARCH CATALOG|Complete Research Catalog]]
