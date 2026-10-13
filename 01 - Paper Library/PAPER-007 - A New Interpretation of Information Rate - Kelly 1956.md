---
type: paper
paper_id: PAPER-007
status: abstract-screened-not-replicated
primary_methodology: "06 Information Theory"
year: 1956
doi: "10.1002/j.1538-7305.1956.tb03809.x"
source_url: "https://doi.org/10.1002/j.1538-7305.1956.tb03809.x"
review_date: 2026-10-13
---
# PAPER-007 — A New Interpretation of Information Rate

**Authors:** John L. Kelly Jr.  
**Publication:** Bell System Technical Journal 35(4), 917-926 (1956)  
**DOI:** https://doi.org/10.1002/j.1538-7305.1956.tb03809.x  
**Source:** https://doi.org/10.1002/j.1538-7305.1956.tb03809.x  
**Evidence access:** Theoretical foundational, publisher abstract reviewed.

> **Research status: AUTHOR CLAIMS / THEORY ONLY.** Source metadata and abstract or author materials reviewed. No independent implementation, full-paper equation audit, dataset verification, or backtest was executed for this note. If replicating, obtain the full version of record and verify all detailed rules against it.

## Economic / mathematical mechanism
An informative signal about a wager's outcome can increase asymptotic log wealth growth when the bettor optimizes fractions with known probabilities and odds. Under specified fair-odds conditions, the value of information relates to information transmission rate.

## What the authors report (NOT our results)
Mathematical theory for wagering and channel information; it supplies neither a market-return forecast nor proof that a KL-divergence signal gate produces trading alpha.

## Data and implementation requirements
Causal, calibrated conditional outcome probability, real payoff distributions, transaction costs, dependence, capital limits, drawdown tolerance and uncertainty estimates.

## Limitations and replication hazards
Full-Kelly sizing is highly fragile to probability errors, time-varying payoffs, model misspecification and correlated bets. KL information gain is not identical to expected after-cost trade profit.

## Candidate falsifiable hypothesis (our proposal, UNTESTED)
A carefully calibrated forecast with independently tested incremental information can improve after-cost log-growth relative to a no-gate forecast under capped fractional Kelly sizing.

## Proposed validation / first test (NOT executed)
Train M0/M1 on chronological data, measure strictly out-of-sample calibration, log loss, realised net utility, sensitivity to costs and miscalibration; check no trades when information-cost threshold fails.

## Knowledge graph
- **Primary:** [[02 - Trading Methodologies/06 Information Theory/README|06 Information Theory]]
- **Related:** [[02 - Trading Methodologies/04 Machine Learning/README|04 Machine Learning]]
- **Related:** [[02 - Trading Methodologies/08 Regime Detection/README|08 Regime Detection]]

## What this paper does NOT show
- That the reported pattern still exists after 2025-2026, under your broker/exchange, or with your current dataset.
- That reported prediction metrics or theoretical existence are the same as causal, executable after-cost trading alpha.
- That paper parameters may be retuned on a test set and still called independent out-of-sample validation.

## Next action
Retrieve and audit the full published paper or author manuscript before freezing an executable reproduction spec. No backtest performed.
