---
type: paper
paper_id: PAPER-005
status: abstract-screened-not-replicated
primary_methodology: "04 Machine Learning"
year: 2020
doi: "10.1093/rfs/hhaa009"
source_url: "https://doi.org/10.1093/rfs/hhaa009"
review_date: 2026-10-13
---
# PAPER-005 — Empirical Asset Pricing via Machine Learning

**Authors:** Shihao Gu; Bryan Kelly; Dacheng Xiu  
**Publication:** Review of Financial Studies 33(5), 2223-2273 (2020)  
**DOI:** https://doi.org/10.1093/rfs/hhaa009  
**Source:** https://doi.org/10.1093/rfs/hhaa009  
**Evidence access:** Empirical peer-reviewed, publisher abstract reviewed.

> **Research status: AUTHOR CLAIMS / THEORY ONLY.** Source metadata and abstract or author materials reviewed. No independent implementation, full-paper equation audit, dataset verification, or backtest was executed for this note. If replicating, obtain the full version of record and verify all detailed rules against it.

## Economic / mathematical mechanism
Benchmark multiple ML methods for expected stock risk-premium forecasting. Nonlinear interactions in trees and neural networks can capture conditional return effects omitted by linear specifications.

## What the authors report (NOT our results)
The authors report economic gains from ML-based cross-sectional asset-pricing forecasts and emphasize momentum, liquidity and volatility predictors. Results concern the studied asset-pricing data, not guaranteed intraday signal profitability.

## Data and implementation requirements
Point-in-time company fundamentals and characteristics, survivorship-safe stock universe, returns, factor benchmark and rebalancing costs; reporting date and availability lag are essential.

## Limitations and replication hazards
Feature release-time leakage, multiple model search, survivorship, unrealistic frictionless portfolios, capacity and variation in business-cycle samples; overfitting especially with highly persistent firm characteristics.

## Candidate falsifiable hypothesis (our proposal, UNTESTED)
Interpretable nonlinear interactions between lagged momentum, liquidity, and volatility improve strictly chronological cross-sectional return predictions vs regularized linear models after turnover costs.

## Proposed validation / first test (NOT executed)
Use date-stamped filings, nested walk-forward hyperparameter selection, nested purging where needed, risk-adjusted benchmark, calibration and uncertainty, robust net return assessment.

## Knowledge graph
- **Primary:** [[02 - Trading Methodologies/04 Machine Learning/README|04 Machine Learning]]
- **Related:** [[02 - Trading Methodologies/05 Deep Learning/README|05 Deep Learning]]
- **Related:** [[02 - Trading Methodologies/12 Cross Asset and Macro/README|12 Cross Asset and Macro]]

## What this paper does NOT show
- That the reported pattern still exists after 2025-2026, under your broker/exchange, or with your current dataset.
- That reported prediction metrics or theoretical existence are the same as causal, executable after-cost trading alpha.
- That paper parameters may be retuned on a test set and still called independent out-of-sample validation.

## Next action
Retrieve and audit the full published paper or author manuscript before freezing an executable reproduction spec. No backtest performed.
