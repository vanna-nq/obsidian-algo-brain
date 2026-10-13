---
type: paper
paper_id: PAPER-009
status: abstract-screened-not-replicated
primary_methodology: "08 Regime Detection"
year: 1989
doi: "10.2307/1912559"
source_url: "https://ideas.repec.org/a/ecm/emetrp/v57y1989i2p357-84.html"
review_date: 2026-10-13
---
# PAPER-009 — A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle

**Authors:** James D. Hamilton  
**Publication:** Econometrica 57(2), 357-384 (1989)  
**DOI:** https://doi.org/10.2307/1912559  
**Source:** https://ideas.repec.org/a/ecm/emetrp/v57y1989i2p357-84.html  
**Evidence access:** Econometric methodological peer-reviewed, abstract reviewed.

> **Research status: AUTHOR CLAIMS / THEORY ONLY.** Source metadata and abstract or author materials reviewed. No independent implementation, full-paper equation audit, dataset verification, or backtest was executed for this note. If replicating, obtain the full version of record and verify all detailed rules against it.

## Economic / mathematical mechanism
Latent Markov regime states govern parameters of a time series with occasional shifts. Maximum-likelihood procedures infer transition probabilities and filtered likelihood-based state beliefs.

## What the authors report (NOT our results)
Original empirical application analyzes US GNP growth and recession-state shifts, not a backtested intraday trading strategy. Value here is the statistical framework for regime uncertainty.

## Data and implementation requirements
Long, consistently sampled historical time series, known publication timestamps for macro releases, robust treatment of revised data and low-frequency regime changes.

## Limitations and replication hazards
Smoothed posterior uses FUTURE observations and therefore leaks information in backtests. State labels can flip, estimated regimes are uncertain, historical transition rates can change, and monthly/quarterly models may not suit 2-minute execution.

## Candidate falsifiable hypothesis (our proposal, UNTESTED)
Real-time filtered state probability may improve a frozen strategy's risk management versus observable volatility controls, without retrospectively smoothing states.

## Proposed validation / first test (NOT executed)
Refit model using only past training data; use one-sided filtered probabilities, walk-forward probability calibration, trading value after costs, no hindsight event classification.

## Knowledge graph
- **Primary:** [[02 - Trading Methodologies/08 Regime Detection/README|08 Regime Detection]]
- **Related:** [[02 - Trading Methodologies/07 Volatility and Derivatives/README|07 Volatility and Derivatives]]
- **Related:** [[02 - Trading Methodologies/02 Trend and Momentum/README|02 Trend and Momentum]]

## What this paper does NOT show
- That the reported pattern still exists after 2025-2026, under your broker/exchange, or with your current dataset.
- That reported prediction metrics or theoretical existence are the same as causal, executable after-cost trading alpha.
- That paper parameters may be retuned on a test set and still called independent out-of-sample validation.

## Next action
Retrieve and audit the full published paper or author manuscript before freezing an executable reproduction spec. No backtest performed.
