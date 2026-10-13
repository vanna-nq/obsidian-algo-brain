---
type: paper
paper_id: PAPER-076
status: primary-source-abstract-screened
category: "08 Regime Detection"
year: 1982
reviewed_on: 2026-10-13
doi: "10.2307/1912773"
source_url: "https://www.jstor.org/stable/1912773"
replicated: false
---
# PAPER-076 — Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation

**Authors:** Robert F. Engle  
**Publication:** Econometrica 50(4), 987–1007 (1982)  
**Primary research source:** https://www.jstor.org/stable/1912773
**DOI:** https://doi.org/10.2307/1912773

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Introduces ARCH processes in which conditional variance depends on past squared shocks, allowing time-varying volatility forecasts.

## Author-reported finding or theoretical scope
An econometric model for conditional heteroskedasticity, illustrated with UK inflation; neither a hidden-state HMM nor a profitable financial strategy.

## Required data / feasibility gate
Clean residual return/innovation series, known observation times, train-only maximum likelihood, volatility forecast horizon.

## Critique / potential failure
Even a better-fitting conditional variance model does not prove risk-premium predictability, and ARCH lags can overfit unstable markets.

## Falsifiable follow-up (proposal only)
Compare forecasted next-session volatility and strategy exposure gating against constant variance and rolling realized-vol baselines on future sessions.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/08 Regime Detection/README|Regime Detection]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
