---
type: research_intelligence_index
status: "proposed-research-triage"
tracked_hypotheses: 15
paper_library_count: 104
last_updated: 2026-10-13
---
# Research Intelligence Index — From papers to falsifiable tests

**104 source-screened notes, 16 mechanism families, 15 candidate hypotheses; ZERO experiments executed in this step.** Navigate the [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Mathematical Knowledge Graph]] and [[01 - Paper Library/RESEARCH CATALOG|original paper catalog]]. No model is validated.

## How ranking works
- **T1:** practical OHLCV feasibility, simple measurable hypothesis, clear null; source and actual dataset still need auditing.
- **T2:** reasonable research lead but complex estimation, stationarity, repaired data, or complete search logs required.
- **T3:** missing specialized data or deliberately synthetic model; do not fake a replication with OHLCV proxies.
- Ordering ranks research feasibility and falsifiability, **not expected Sharpe or profitability**.

| # | Candidate | Tier | Dataset requirement | Primary comparison | Status |
|---|---|---|---|---|---|
| 1 | [[05 - Strategy Hypotheses/HYP-F001 - Permutation Entropy Future Volatility|HYP-F001 — Permutation Entropy Future Volatility]] | T1 | GC.F 5m OHLCV | Lagged realized-variance HAR-style regression, EWMA | audit-queued |
| 2 | [[05 - Strategy Hypotheses/HYP-F002 - Roughness of Volatility|HYP-F002 — Roughness of Volatility]] | T1 | GC.F 5m or SPX500 1h | HAR-RV and EWMA/GARCH | proposed |
| 3 | [[05 - Strategy Hypotheses/HYP-F003 - Intraday Extremum Hazard and Seasonality|HYP-F003 — Intraday Extremum Hazard and Seasonality]] | T1 | GC.F 5m session OHLCV | Time-only empirical hazards and trailing session volatility | proposed |
| 4 | [[05 - Strategy Hypotheses/HYP-F004 - Time Reversal Volatility Feedback|HYP-F004 — Time Reversal Volatility Feedback]] | T1 | GC.F 5m or SPX500 1h | HAR-RV and symmetric GARCH | proposed |
| 5 | [[05 - Strategy Hypotheses/HYP-F005 - Low Order Path Signatures|HYP-F005 — Low Order Path Signatures]] | T2 | NVDA/SMH 5m corrected OHLCV | Matched lagged predictors using ridge or boosted trees | proposed |
| 6 | [[05 - Strategy Hypotheses/HYP-F006 - Recurrence Geometry Tail Warning|HYP-F006 — Recurrence Geometry Tail Warning]] | T2 | SPX500 1h OHLCV; not a replication of multi-index topology paper | Trailing vol, vol-of-vol and drawdown | proposed |
| 7 | [[05 - Strategy Hypotheses/HYP-F007 - OU Spread First Passage|HYP-F007 — OU Spread First Passage]] | T2 | NVDA/SMH corrected synchronized 5m | Simple z-score pair and no-trade | proposed |
| 8 | [[05 - Strategy Hypotheses/HYP-F008 - Glassy Two Timescale Price Displacements|HYP-F008 — Glassy Two Timescale Price Displacements]] | T2 | GC.F 5m; adaptation from currency-market research | Seasonally adjusted Student-t GARCH and mixture null | proposed |
| 9 | [[05 - Strategy Hypotheses/HYP-F009 - Multifractal Tail Scaling|HYP-F009 — Multifractal Tail Scaling]] | T2 | GC.F 5m or SPX500 1h | Student-t GARCH and historical empirical quantile | proposed |
| 10 | [[05 - Strategy Hypotheses/HYP-F010 - Cross Asset Lead Lag|HYP-F010 — Cross Asset Lead Lag]] | T2 | NVDA/SMH synchronized adjusted 5m | NVDA-only lag model and session seasonality | proposed |
| 11 | [[05 - Strategy Hypotheses/HYP-F011 - Backtest Selection Bias Audit|HYP-F011 — Backtest Selection Bias Audit]] | T2 | Complete dated trial-level return series needed; availability unverified | Uncorrected best-backtest plus untouched forward holdout | logs-needed |
| 12 | [[05 - Strategy Hypotheses/HYP-F012 - Hawkes Market Event Cascades|HYP-F012 — Hawkes Market Event Cascades]] | T3 | Tick-level trades/L1-L2 quotes currently unavailable | Inhomogeneous Poisson and autoregressive counts | data-blocked |
| 13 | [[05 - Strategy Hypotheses/HYP-F013 - Option Variance Premium State|HYP-F013 — Option Variance Premium State]] | T3 | Synchronized options chain and underlying price required | VIX/EWMA and price-only regressors | data-blocked |
| 14 | [[05 - Strategy Hypotheses/HYP-F014 - Random Matrix Cleaned Portfolio|HYP-F014 — Random Matrix Cleaned Portfolio]] | T3 | Broad point-in-time synchronized instrument universe required | Ledoit-Wolf covariance, sample covariance and 1/N | data-blocked |
| 15 | [[05 - Strategy Hypotheses/HYP-F015 - Minority Game Synthetic Market|HYP-F015 — Minority Game Synthetic Market]] | T3 | Simulated heterogeneous agents and reference market returns | Student-t random walk and GARCH synthetic generator | synthetic-only |

## Mandatory evidence ladder
1. Original paper source and bibliographic record screened (most notes stop here).
2. **Full-text formula and assumption audit.** Verify equations; distinguish paper findings from our hypotheses.
3. Dataset preview, SHA-256, bar conventions, gap/roll/corporate-action audit and train-only feature availability.
4. Freeze a single test: null, feature, baseline, target, horizon, chronological splits, cost model, metric, minimum benefit, uncertainty and stop condition.
5. Executed tool evidence, complete variant logs, negative results, and untouched chronological out-of-sample evaluation.
6. Only if predictive results hold: a **separate** execution-aware strategy test; independent forward validation required before promotion to Validated Models.

## First approved work item is audit-only, not a backtest
[[06 - Experiments and Backtests/EXP-F001 - Permutation Entropy Data and Method Audit|EXP-F001]]: source formulas and dataset preview for [[05 - Strategy Hypotheses/HYP-F001 - Permutation Entropy Future Volatility|HYP-F001]]. No new prediction code until the audit passes and a separate experiment is frozen.

## Reported available datasets (not actually read or hashed here)
- GC.F gold futures, 5m OHLCV; historically described as ~122,359 rows for 2025-01-01 to 2026-09-26. Verify rolls, venue, session and source.
- SPX500 1h OHLCV, historically ~45,000 bars. Verify exact date bounds, timezone, and data quality.
- NVDA/SMH 5m corrected canonical RTH history, historically ~288,123 rows. Verify split-scale repair manifest and synchronized timestamps.
- Order book/tick trades and full options chains: no confirmed access in this task; proposals requiring these are blocked.

## Research bias controls
- [[01 - Paper Library/PAPER-044 - A Reality Check for Data Snooping|White's Reality Check]] and [[01 - Paper Library/PAPER-045 - The Probability of Backtest Overfitting|PBO]] are different diagnostics and cannot replace an untouched time-series holdout.
- Preserve all attempts, failures, settings and data-provenance versions; don't quietly optimize on OOS.
- Veron tasks must use **only its verified callable function list**, one executable task at a time, and require dataset preview before any code.

[[03 - Mathematical Foundations/KNOWLEDGE GRAPH EDGES|Research connections]] · [[01 - Paper Library/RESEARCH FRONTIER|Niche Research Frontier]]
