---
type: paper
paper_id: "PAPER-103"
status: "source-screened-not-replicated"
category: "11 Intraday Price Structure"
reviewed_on: 2026-10-13
source_url: "https://doi.org/10.1103/PhysRevLett.118.068301"
independently_validated: false
---
# PAPER-103 — Diffusive and Arrestedlike Dynamics in Currency Exchange Markets

**Authors:** Clara-Rahola; Puertas; Sanchez-Granero; Trinidad-Segovia; de las Nieves  
**Venue:** Physical Review Letters 118, 068301 (2017)  
**Source:** https://doi.org/10.1103/PhysRevLett.118.068301

> **Literature frontier / research lead ONLY.** Original source abstract or accessible paper material examined; no complete-paper equation audit, no independent backtest, and no demonstrated trading edge.

## Mechanism
Currency market price displacements resemble supercooled colloid glass two-stage relaxation.

## Data and implementation feasibility
**DIRECT ADAPTATION: GC 5m session-aligned; original EURUSD 1m not available**.

## Candidate falsifiable hypothesis — NOT TESTED
Do gold price displacement plateaus remain after controlling for session-liquidity cycles and predict later volatility?

## Comparator(s) and explicit falsification requirement
**Baselines:** Session-normalized GARCH and shuffled clock-time blocks.  
The candidate must improve the appropriate forward-chaining forecast statistic or risk/return metric against these baselines by a threshold defined before testing; otherwise reject or archive inconclusive. Predictions require realistic execution/cost evaluation before being called tradable.

## Main hazards
Market closure alone can cause plateaus; analogy does not prove glassy dynamics.

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
