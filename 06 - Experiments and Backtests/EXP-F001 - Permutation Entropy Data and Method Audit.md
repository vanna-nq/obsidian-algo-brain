---
type: experiment
experiment_id: "EXP-F001"
status: "planned-audit-only"
hypothesis: "HYP-F001"
execution_evidence: null
code_commit: null
dataset_sha256: null
backtest_executed: false
---
# EXP-F001 — Permutation Entropy Data and Method Audit

**First work item only: paper-method and data audit.** This file is a plan saved to GitHub, not a claim the source PDF was fully checked, local market data accessed, or a forecast tested.

## One verifiable objective
Establish whether [[01 - Paper Library/PAPER-090 - Permutation Entropy A Natural Complexity Measure for Time Series|PAPER-090]] can be translated causally into a deterministic rolling permutation-entropy statistic, and whether the previously discussed **GC.F 5-minute futures OHLCV** dataset meets a documented reproducibility standard. **No model/backtest code in this task.**

## Specified original source
- Bandt and Pompe, *Permutation Entropy: A Natural Complexity Measure for Time Series*, *Physical Review Letters* 88, 174102 (2002), DOI https://doi.org/10.1103/PhysRevLett.88.174102.
- Current vault evidence: bibliographic/abstract or summary screen; **full-text formulas have not yet been audited**.
- Audit ordinal rank definition, ties, embedding dimension, delay, normalization, finite-sample bias and the distinction between sequences of price levels and return innovations. If source access is unavailable, report BLOCKED.

## Exact expected dataset (historically reported, not verified here)
- Instrument: **GC.F continuous gold futures**; actual source/contract mappings and venue need inspection.
- Timeframe: **5-minute OHLCV**.
- Reported dates: **2025-01-01 through 2026-09-26**, approximately **122,359 rows**. These are previous project figures, *not a validated manifest*.
- Require the actual file or a verified connected-data view; don't pretend the GitHub knowledge repo contains licensed source data.

## Mandatory dataset preview BEFORE any predictive code
1. Source path, file version, SHA-256, row count, actual first and last timestamp, timezone and session definition.
2. Ten representative beginning and end rows plus rollover/session-transition examples, actual OHLCV column names and dtypes.
3. Count exact duplicate/out-of-order timestamps, OHLC violations, absent expected bars, interior gaps, zero/null volume, non-session timestamps, special/holiday sessions.
4. Identify exchange local clock, UTC conversion, daylight savings, Globex vs RTH hours, and whether each bar timestamp is its **start or completion** time.
5. Identify continuous-contract front-month roll policy, adjusted/unadjusted prices and roll discontinuities; stop if the roll policy cannot be validated.

## Candidate Stage-2 design (DO NOT RUN; may change only before freeze)
- Feature: ordinal permutation entropy over the most recent 120 **completed** 5-minute log returns at t; proposed dimension 3 and lag 1; resolve tied values deterministically from source formulas.
- Prediction target: squared-log-return realized variance over the following **12 completed** bars; never use partial future observations for the feature.
- Baseline: lagged 12/36/120-bar realized-variance predictors with identical regression class, training budget and calendar controls; EWMA secondary.
- Candidate: same baseline + one entropy term. No untracked signal alternatives.
- Primary forecasting score: lower-is-better QLIKE: y/f - ln(y/f) - 1 for realized variance y and positive forecast f. Determine a strictly positive, fixed policy for zero y BEFORE execution. Report positivity handling and calibration.
- Holdout: strictly chronological untouched future segment, with prediction origins spaced 12 bars apart, and purging/embargo at split boundaries as appropriate. Actual dates to be chosen only once the data's chronology is verified, before looking at model results.
- Uncertainty: paired loss difference with time-series dependence-aware block resampling. Predeclare minimum meaningful improvement and interval criterion before scoring.
- STOP if performance is equivalent to or worse than baseline, or sensitive to sampling/roll/session artifacts. This would reject *incremental forecasting*; neither outcome is a trading-performance claim.

## Audit output contract
- Paper math audit: quote/summarize exact relevant formulas with source-page references if available; list unresolved conventions.
- Immutable dataset manifest and actual preview/gap/roll evidence, not just verbal assurances.
- Explicit verdict **READY_FOR_FREEZE** or **BLOCKED**, justified with evidence and identified missing inputs.
- No generated strategy parameters beyond proposed specification; no predictive fit, trade signals, equity curve or Sharpe ratio.
- Use only tools verified callable in the research environment; do not assume Veron can write files, run Python, import LSE data, or run a blueprint unless its current function list explicitly supports the action.

## Current state and stop condition
- **Status:** PLANNED. No paper PDF was fetched/audited equation by equation in this step. No GC.F data file was read or hashed. No trading system, prediction or backtest has been executed.
- **STOP HERE** upon producing audit artifacts/ready-blocked verdict. A separately authorized, frozen experiment must receive a new ID before coding and evaluating the proposed forecast.

## Links
[[05 - Strategy Hypotheses/HYP-F001 - Permutation Entropy Future Volatility|HYP-F001]] · [[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]] · [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Graph]]
