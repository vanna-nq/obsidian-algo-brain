---
type: paper
paper_id: "PAPER-096"
status: "source-screened-not-replicated"
category: "12 Cross Asset and Macro"
reviewed_on: 2026-10-13
source_url: "https://doi.org/10.1103/PhysRevE.68.056110"
independently_validated: false
---
# PAPER-096 — Dynamics of market correlations: Taxonomy and portfolio analysis

**Authors:** Onnela; Chakraborti; Kaski; Kertesz; Kanto  
**Venue:** Physical Review E 68, 056110 (2003)  
**Source:** https://doi.org/10.1103/PhysRevE.68.056110

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Rolling correlation distances form minimum spanning asset trees whose geometry changes under stress.

## Data and implementation feasibility
**GAP: broad multivariate market basket needed**.

## Candidate falsifiable hypothesis — NOT TESTED
Does rolling tree contraction add predictive signal for next-month correlation spikes?

## Comparator(s) and explicit falsification requirement
**Baselines:** Mean correlation, first PC, rolling vol.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Instability near ties and universe selection make tree changes noisy.

## One-task research execution contract
1. Verify full paper formulas, version, dataset path, ticker, time frame and exact available date ranges. Dataset preview **before coding**.
2. Freeze one horizon, targets, null models, hyperparameter search budget, primary metric, chronological holdout and failure rule.
3. Train only on past data. For test evaluation, forbid lookahead in rolling statistics, close-to-open execution, bar timestamps, or future-estimated scaling.
4. Report actual executed tool evidence, code and hashes; keep unsuccessful variants and exclude data-snooped feature permutations.
5. Stop after this single controlled test. Any changes require a newly numbered experiment; never promote literature claims to validated models.

## Wiki links
- [[02 - Trading Methodologies/12 Cross Asset and Macro/README|Cross Asset and Macro]]
- [[01 - Paper Library/RESEARCH FRONTIER|Research Frontier]]
- [[01 - Paper Library/RESEARCH CATALOG|Complete Research Catalog]]
