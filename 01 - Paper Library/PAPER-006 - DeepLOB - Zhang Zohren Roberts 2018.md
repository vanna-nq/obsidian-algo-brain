---
type: paper
paper_id: PAPER-006
status: abstract-screened-not-replicated
primary_methodology: "05 Deep Learning"
year: 2018
doi: "10.48550/arXiv.1808.03668"
source_url: "https://arxiv.org/abs/1808.03668"
review_date: 2026-10-13
---
# PAPER-006 — DeepLOB: Deep Convolutional Neural Networks for Limit Order Books

**Authors:** Zihao Zhang; Stefan Zohren; Stephen Roberts  
**Publication:** arXiv:1808.03668 (revised 2020) (2018)  
**DOI:** https://doi.org/10.48550/arXiv.1808.03668  
**Source:** https://arxiv.org/abs/1808.03668  
**Evidence access:** Author preprint, arXiv abstract reviewed.

> **Research status: AUTHOR CLAIMS / THEORY ONLY.** Source metadata and abstract or author materials reviewed. No independent implementation, full-paper equation audit, dataset verification, or backtest was executed for this note. If replicating, obtain the full version of record and verify all detailed rules against it.

## Economic / mathematical mechanism
Convolutional layers learn spatial structure across limit-order-book levels and LSTM layers summarize the temporal evolution to classify subsequent short-term midprice direction.

## What the authors report (NOT our results)
Authors report performance above prior benchmark models and cross-instrument out-of-sample prediction on London Stock Exchange quote data. Prediction accuracy by itself is not net trading profitability.

## Data and implementation requirements
Time-aligned multi-level order book updates (price and size on bids/asks), event-level timestamps, exchange matching rules and fee/slippage model; 5-minute OHLCV alone is NOT sufficient.

## Limitations and replication hazards
Label horizons and overlapping sequences can leak test information, non-stationary microstructure, feed latency, queue priority, market-impact and spread can eliminate prediction-to-PnL transfer.

## Candidate falsifiable hypothesis (our proposal, UNTESTED)
Sequence models built on complete order books improve realized execution-aware directional utility beyond linear order imbalance and return-history baselines.

## Proposed validation / first test (NOT executed)
Gap-separated event-time temporal splits, no overlapping windows between train/test, untouched instruments, latency-aware execution simulation and uncertainty calibration; report post-cost PnL and benchmark.

## Knowledge graph
- **Primary:** [[02 - Trading Methodologies/05 Deep Learning/README|05 Deep Learning]]
- **Related:** [[02 - Trading Methodologies/03 Market Microstructure/README|03 Market Microstructure]]
- **Related:** [[02 - Trading Methodologies/04 Machine Learning/README|04 Machine Learning]]

## What this paper does NOT show
- That the reported pattern still exists after 2025-2026, under your broker/exchange, or with your current dataset.
- That reported prediction metrics or theoretical existence are the same as causal, executable after-cost trading alpha.
- That paper parameters may be retuned on a test set and still called independent out-of-sample validation.

## Next action
Retrieve and audit the full published paper or author manuscript before freezing an executable reproduction spec. No backtest performed.
