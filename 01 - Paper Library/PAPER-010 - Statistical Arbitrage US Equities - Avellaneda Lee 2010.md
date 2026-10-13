---
type: paper
paper_id: PAPER-010
status: abstract-screened-not-replicated
primary_methodology: "09 Mean Reversion"
year: 2010
doi: "10.1080/14697680903124632"
source_url: "https://math.nyu.edu/~avellane/AvellanedaLeeStatArb071108.pdf"
review_date: 2026-10-13
---
# PAPER-010 — Statistical Arbitrage in the U.S. Equities Market

**Authors:** Marco Avellaneda; Jeong-Hyun Lee  
**Publication:** Quantitative Finance 10(7), 761-782 (2010)  
**DOI:** https://doi.org/10.1080/14697680903124632  
**Source:** https://math.nyu.edu/~avellane/AvellanedaLeeStatArb071108.pdf  
**Evidence access:** Empirical peer-reviewed, author PDF/abstract examined.

> **Research status: AUTHOR CLAIMS / THEORY ONLY.** Source metadata and abstract or author materials reviewed. No independent implementation, full-paper equation audit, dataset verification, or backtest was executed for this note. If replicating, obtain the full version of record and verify all detailed rules against it.

## Economic / mathematical mechanism
Remove systematic stock-return components using principal components or sector-ETF regressions, then model the residual cumulative process as mean reverting; trade departures from estimated equilibrium with diversified market-neutral books.

## What the authors report (NOT our results)
Authors report PCA-based Sharpe ~1.44 over 1997–2007 but only ~0.9 over 2003–2007 after costs. ETF signals plus volume-based trading-time adjustments report improved later-sample results. This deterioration is a key warning.

## Data and implementation requirements
Historical survivorship-safe individual stock prices, sector ETFs, PCA fit windows, volume, borrow availability, spreads, cross-sectional portfolio/risk constraints.

## Limitations and replication hazards
Residual factor instability, changing index constituents, biased PCA fitted over future observations, crowded liquidation (Aug 2007 quant drawdown), short costs and leverage blowups.

## Candidate falsifiable hypothesis (our proposal, UNTESTED)
An ex-ante ETF-residual mean-reversion signal retains incremental after-cost power in post-publication data after controlling for market-neutral factor exposure and execution costs.

## Proposed validation / first test (NOT executed)
Fit risk model on trailing window only, never full sample; no hindsight factor selection; time-segment performance, hard stress August 2007 and recent shocks, liquidity-aware costs and crowding proxies.

## Knowledge graph
- **Primary:** [[02 - Trading Methodologies/09 Mean Reversion/README|09 Mean Reversion]]
- **Related:** [[02 - Trading Methodologies/01 Statistical Arbitrage/README|01 Statistical Arbitrage]]
- **Related:** [[02 - Trading Methodologies/08 Regime Detection/README|08 Regime Detection]]

## What this paper does NOT show
- That the reported pattern still exists after 2025-2026, under your broker/exchange, or with your current dataset.
- That reported prediction metrics or theoretical existence are the same as causal, executable after-cost trading alpha.
- That paper parameters may be retuned on a test set and still called independent out-of-sample validation.

## Next action
Retrieve and audit the full published paper or author manuscript before freezing an executable reproduction spec. No backtest performed.
