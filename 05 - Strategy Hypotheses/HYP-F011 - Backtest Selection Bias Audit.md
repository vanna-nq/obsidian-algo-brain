---
type: hypothesis
hypothesis_id: "HYP-F011"
status: "logs-needed"
priority_tier: "T2"
backtest_executed: false
full_paper_audit_completed: false
---
# HYP-F011 — Backtest Selection Bias Audit

**T2 / queue #11 / logs-needed — proposed, NOT independently tested.** The literature notes are source-screened rather than audited full-text replications.

## Source papers and mechanism
[[01 - Paper Library/PAPER-044 - A Reality Check for Data Snooping|PAPER-044 — A Reality Check for Data Snooping]], [[01 - Paper Library/PAPER-045 - The Probability of Backtest Overfitting|PAPER-045 — The Probability of Backtest Overfitting]], [[01 - Paper Library/PAPER-062 - Testing market efficiency using statistical arbitrage with applications to momentu|PAPER-062 — Testing market efficiency using statistical arbitrage with applications to momentum and value strategies]]

## Exact proposed observable and prediction
- **Input dataset:** Complete dated trial-level return series needed; availability unverified. No local raw-data availability or SHA verified in this repository task.
- **Feature:** All tried variants and their date-aligned excess returns.
- **Target:** Whether selected winner survives multiple-search correction.
- **Candidate null:** No incremental prospective utility over the benchmark on identical observations and cost assumptions.
- **Baseline:** Uncorrected best-backtest plus untouched forward holdout.
- **Primary evaluation:** Reality Check adjusted p-values and PBO. All exact hyperparameters, target timing, chronological splits and minimum worthwhile gain to be frozen *after* the source/data audit but *before* model execution.

## Research gate / data problems
Must have unsuccessful search variants; cannot reconstruct from winner alone.

## Stop / failure definition
Stop if authentic data or original formulas cannot be audited. If a precommitted chronological holdout does not show a robust positive incremental gain over the baseline, mark FAIL or INCONCLUSIVE. One frozen task at a time; preserve negative outcomes and full selection history.

## Execution economics
There is **no approved trading entry, exit or sizing rule** for this hypothesis, except where specifically defined as a *future* PnL study. Confirmed predictive information and realistic execution economics are separate validation stages.

## Links
- [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]]
- [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]]
