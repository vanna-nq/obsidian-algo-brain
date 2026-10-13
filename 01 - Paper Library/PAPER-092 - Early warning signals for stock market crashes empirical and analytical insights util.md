---
type: paper
paper_id: "PAPER-092"
status: "source-screened-not-replicated"
category: "08 Regime Detection"
reviewed_on: 2026-10-13
source_url: "https://doi.org/10.1140/epjds/s13688-024-00457-2"
independently_validated: false
---
# PAPER-092 — Early warning signals for stock market crashes: empirical and analytical insights utilizing nonlinear methods

**Authors:** Shijia Song; Handong Li  
**Venue:** EPJ Data Science 13, article 16 (2024)  
**Source:** https://doi.org/10.1140/epjds/s13688-024-00457-2

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Recurrence plots and multiplex recurrence networks identify nonlinear states and possible transitions.

## Data and implementation feasibility
**DIRECT ADAPTATION: GC 5m and SPX500 1h lagged return/vol state vectors**.

## Candidate falsifiable hypothesis — NOT TESTED
Can recurrence determinism/laminarity improve future volatility-spike prediction beyond EWMA?

## Comparator(s) and explicit falsification requirement
**Baselines:** EWMA, volatility-of-volatility, lagged ACF.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Recurrence threshold and embedding chosen in-sample must be frozen.

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
