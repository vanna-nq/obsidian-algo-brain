---
type: hypothesis
hypothesis_id: "HYP-F010"
status: "proposed"
priority_tier: "T2"
backtest_executed: false
full_paper_audit_completed: false
---
# HYP-F010 — Cross Asset Lead Lag

**T2 / queue #10 / proposed — proposed, NOT independently tested.** The literature notes are source-screened rather than audited full-text replications.

## Source papers and mechanism
[[01 - Paper Library/PAPER-013 - Value and Momentum Everywhere - Asness Moskowitz Pedersen 2013|PAPER-013 — Value and Momentum Everywhere]], [[01 - Paper Library/PAPER-037 - International Stock Return Predictability What Is the Role of the United States|PAPER-037 — International Stock Return Predictability What Is the Role of the United States]], [[01 - Paper Library/PAPER-060 - Common risk factors in the returns on stocks and bonds|PAPER-060 — Common risk factors in the returns on stocks and bonds]], [[01 - Paper Library/PAPER-066 - Order Flow and Exchange Rate Dynamics|PAPER-066 — Order Flow and Exchange Rate Dynamics]]

## Exact proposed observable and prediction
- **Input dataset:** NVDA/SMH synchronized adjusted 5m. No local raw-data availability or SHA verified in this repository task.
- **Feature:** Lagged SMH innovations conditional on lagged NVDA and clock time.
- **Target:** Next NVDA return sign (freeze before testing).
- **Candidate null:** No incremental prospective utility over the benchmark on identical observations and cost assumptions.
- **Baseline:** NVDA-only lag model and session seasonality.
- **Primary evaluation:** Log loss, then net execution study. All exact hyperparameters, target timing, chronological splits and minimum worthwhile gain to be frozen *after* the source/data audit but *before* model execution.

## Research gate / data problems
Split repairs, timestamp asynchrony and same-bar lookahead.

## Stop / failure definition
Stop if authentic data or original formulas cannot be audited. If a precommitted chronological holdout does not show a robust positive incremental gain over the baseline, mark FAIL or INCONCLUSIVE. One frozen task at a time; preserve negative outcomes and full selection history.

## Execution economics
There is **no approved trading entry, exit or sizing rule** for this hypothesis, except where specifically defined as a *future* PnL study. Confirmed predictive information and realistic execution economics are separate validation stages.

## Links
- [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]]
- [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]]
