---
type: hypothesis
hypothesis_id: "HYP-F015"
status: "synthetic-only"
priority_tier: "T3"
backtest_executed: false
full_paper_audit_completed: false
---
# HYP-F015 — Minority Game Synthetic Market

**T3 / queue #15 / synthetic-only — proposed, NOT independently tested.** The literature notes are source-screened rather than audited full-text replications.

## Source papers and mechanism
[[01 - Paper Library/PAPER-099 - Stylized facts of financial markets and market crashes in Minority Games|PAPER-099 — Stylized facts of financial markets and market crashes in Minority Games]], [[01 - Paper Library/PAPER-100 - Price variations in a stock market with many agents|PAPER-100 — Price variations in a stock market with many agents]], [[01 - Paper Library/PAPER-098 - Large financial crashes|PAPER-098 — Large financial crashes]]

## Exact proposed observable and prediction
- **Input dataset:** Simulated heterogeneous agents and reference market returns. No local raw-data availability or SHA verified in this repository task.
- **Feature:** Minority-game agent population and transition parameters.
- **Target:** Reproduce heavy tails, vol clustering and drawdown distributions.
- **Candidate null:** No incremental prospective utility over the benchmark on identical observations and cost assumptions.
- **Baseline:** Student-t random walk and GARCH synthetic generator.
- **Primary evaluation:** Held-out distributional distance. All exact hyperparameters, target timing, chronological splits and minimum worthwhile gain to be frozen *after* the source/data audit but *before* model execution.

## Research gate / data problems
Stylized-fact matching does not establish real market mechanism or alpha.

## Stop / failure definition
Stop if authentic data or original formulas cannot be audited. If a precommitted chronological holdout does not show a robust positive incremental gain over the baseline, mark FAIL or INCONCLUSIVE. One frozen task at a time; preserve negative outcomes and full selection history.

## Execution economics
There is **no approved trading entry, exit or sizing rule** for this hypothesis, except where specifically defined as a *future* PnL study. Confirmed predictive information and realistic execution economics are separate validation stages.

## Links
- [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]]
- [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]]
