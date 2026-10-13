---
type: paper
paper_id: PAPER-004
status: abstract-screened-not-replicated
primary_methodology: "03 Market Microstructure"
year: 1985
doi: "10.2307/1913210"
source_url: "https://www.econometricsociety.org/publications/econometrica/browse/1985/11/01/continuous-auctions-and-insider-trading"
review_date: 2026-10-13
---
# PAPER-004 — Continuous Auctions and Insider Trading

**Authors:** Albert S. Kyle  
**Publication:** Econometrica 53(6), 1315-1336 (1985)  
**DOI:** https://doi.org/10.2307/1913210  
**Source:** https://www.econometricsociety.org/publications/econometrica/browse/1985/11/01/continuous-auctions-and-insider-trading  
**Evidence access:** Theoretical peer-reviewed, publisher abstract reviewed.

> **Research status: AUTHOR CLAIMS / THEORY ONLY.** Source metadata and abstract or author materials reviewed. No independent implementation, full-paper equation audit, dataset verification, or backtest was executed for this note. If replicating, obtain the full version of record and verify all detailed rules against it.

## Economic / mathematical mechanism
A risk-neutral informed trader optimizes trade disclosure against competitive market makers and stochastic liquidity/noise traders. Price impact is endogenous to asymmetric information, depth and market-maker inference.

## What the authors report (NOT our results)
The model characterizes sequential trading and a continuous-time limit with information incorporated into prices. It is a theory of price formation, NOT an empirical backtested trading system.

## Data and implementation requirements
To empirically test implications requires trade/quote timestamps, order imbalance or aggressor classification, depth/impact and spreads; OHLCV cannot directly reveal insiders, trading direction, or quote depth.

## Limitations and replication hazards
Stylized strategic assumptions, single insider, competitive makers and Gaussian-type modeling assumptions need not hold in electronic multi-venue markets; applying Kyle lambda naively to candles is misleading.

## Candidate falsifiable hypothesis (our proposal, UNTESTED)
Causal signed order flow explains short-horizon price response after controlling for volatility and spread; effects weaken or invert with high liquidity.

## Proposed validation / first test (NOT executed)
Estimate out-of-sample price impact vs contemporaneous and future flow with clean L1/L2 data; isolate lookahead from same-interval trade directions; compare to return-only baseline.

## Knowledge graph
- **Primary:** [[02 - Trading Methodologies/03 Market Microstructure/README|03 Market Microstructure]]
- **Related:** [[02 - Trading Methodologies/05 Deep Learning/README|05 Deep Learning]]
- **Related:** [[02 - Trading Methodologies/11 Intraday Price Structure/README|11 Intraday Price Structure]]

## What this paper does NOT show
- That the reported pattern still exists after 2025-2026, under your broker/exchange, or with your current dataset.
- That reported prediction metrics or theoretical existence are the same as causal, executable after-cost trading alpha.
- That paper parameters may be retuned on a test set and still called independent out-of-sample validation.

## Next action
Retrieve and audit the full published paper or author manuscript before freezing an executable reproduction spec. No backtest performed.
