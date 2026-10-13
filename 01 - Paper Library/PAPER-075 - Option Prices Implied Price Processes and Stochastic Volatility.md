---
type: paper
paper_id: PAPER-075
status: primary-source-abstract-screened
category: "07 Volatility and Derivatives"
year: 2000
reviewed_on: 2026-10-13
doi: "10.1111/0022-1082.00228"
source_url: "https://onlinelibrary.wiley.com/doi/10.1111/0022-1082.00228"
replicated: false
---
# PAPER-075 — Option Prices, Implied Price Processes, and Stochastic Volatility

**Authors:** Mark Britten-Jones; Anthony Neuberger  
**Publication:** The Journal of Finance 55(2), 839–866 (2000)  
**Primary research source:** https://onlinelibrary.wiley.com/doi/10.1111/0022-1082.00228
**DOI:** https://doi.org/10.1111/0022-1082.00228

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Characterizes continuous price processes consistent with observed options and uses option prices to infer model-free volatility forecasts.

## Author-reported finding or theoretical scope
The paper derives market-option-implied variance information and option-consistent dynamics without fixing one deterministic-volatility pricing model.

## Required data / feasibility gate
Accurate full strike/expiry option surface, dividend/discount curves, mid vs executable quotes, interpolation and maturity alignment.

## Critique / potential failure
Risk-neutral option-implied expectations are not necessarily realized forecasts or alpha; surface data, tail truncation and jumps matter.

## Falsifiable follow-up (proposal only)
Compare model-free implied variance vs next-maturity realized variance and statistical forecasts in held-out options samples, then evaluate net hedging value separately.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/07 Volatility and Derivatives/README|Volatility and Derivatives]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
