---
type: paper
paper_id: PAPER-074
status: primary-source-abstract-screened
category: "07 Volatility and Derivatives"
year: 1973
reviewed_on: 2026-10-13
doi: "10.1086/260062"
source_url: "https://www.journals.uchicago.edu/doi/10.1086/260062"
replicated: false
---
# PAPER-074 — The Pricing of Options and Corporate Liabilities

**Authors:** Fischer Black; Myron Scholes  
**Publication:** Journal of Political Economy 81(3), 637–654 (1973)  
**Primary research source:** https://www.journals.uchicago.edu/doi/10.1086/260062
**DOI:** https://doi.org/10.1086/260062

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Builds an arbitrage-based valuation model for options using dynamic hedging and an idealized price-diffusion framework.

## Author-reported finding or theoretical scope
A foundational theoretical model for derivative valuation, not evidence that trading volatility using Black–Scholes formulas yields riskless profits.

## Required data / feasibility gate
Underlying/option synchronized prices, current rates, dividends, trading-hour and exercise rules, executable hedges and option quotes.

## Critique / potential failure
Continuous trading, constant volatility, no jump, no friction and unlimited financing approximations are not valid during market stress.

## Falsifiable follow-up (proposal only)
Test pricing/hedging error and net PnL of benchmark delta hedges under stochastic vol, jumps, spreads and discrete rebalance schedules.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/07 Volatility and Derivatives/README|Volatility and Derivatives]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
