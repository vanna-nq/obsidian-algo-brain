---
type: paper
paper_id: PAPER-012
status: abstract-screened-not-replicated
primary_methodology: "11 Intraday Price Structure"
year: 2018
doi: "10.1016/j.jfineco.2018.05.009"
source_url: "https://doi.org/10.1016/j.jfineco.2018.05.009"
review_date: 2026-10-13
---
# PAPER-012 — Market Intraday Momentum

**Authors:** Lei Gao; Yufeng Han; Sophia Zhengzi Li; Guofu Zhou  
**Publication:** Journal of Financial Economics 129(2), 394-414 (2018)  
**DOI:** https://doi.org/10.1016/j.jfineco.2018.05.009  
**Source:** https://doi.org/10.1016/j.jfineco.2018.05.009  
**Evidence access:** Empirical peer-reviewed, publisher abstract reviewed.

> **Research status: AUTHOR CLAIMS / THEORY ONLY.** Source metadata and abstract or author materials reviewed. No independent implementation, full-paper equation audit, dataset verification, or backtest was executed for this note. If replicating, obtain the full version of record and verify all detailed rules against it.

## Economic / mathematical mechanism
First 30-minute market return measured from the PREVIOUS close is associated with the final 30-minute return; potential mechanisms include delayed informed trading and infrequent portfolio rebalancing.

## What the authors report (NOT our results)
Empirical SPY ETF data 1993–2013 show significant intraday momentum; stronger during volatile, high-volume, recession or macro-news days, and noted across ten other actively traded ETFs. This is specifically a final-half-hour effect; it is not a universal HOD/LOD detector.

## Data and implementation requirements
Minute SPY OHLCV spanning 09:30–16:00 New York session plus prior close, opening and closing auction conditions, timestamped macro news, trading costs and availability.

## Limitations and replication hazards
Signal definition includes overnight movement; swapping for first half-hour open-to-close return changes the model. Execution at 15:30 and close can suffer closing auction costs, and post-2013 decay/extension tests matter.

## Candidate falsifiable hypothesis (our proposal, UNTESTED)
An early-session direction-and-gap signal forecasts 15:30–16:00 return in unexamined periods after close-execution costs, beyond unconditional late-day trend persistence.

## Proposed validation / first test (NOT executed)
Compare first-half-hour vs gap-only and combined components; test genuine chronological post-2013 holdout and 0DTE-era samples; simulate pre-close fills and report latency/fill robustness.

## Knowledge graph
- **Primary:** [[02 - Trading Methodologies/11 Intraday Price Structure/README|11 Intraday Price Structure]]
- **Related:** [[02 - Trading Methodologies/02 Trend and Momentum/README|02 Trend and Momentum]]
- **Related:** [[02 - Trading Methodologies/03 Market Microstructure/README|03 Market Microstructure]]

## What this paper does NOT show
- That the reported pattern still exists after 2025-2026, under your broker/exchange, or with your current dataset.
- That reported prediction metrics or theoretical existence are the same as causal, executable after-cost trading alpha.
- That paper parameters may be retuned on a test set and still called independent out-of-sample validation.

## Next action
Retrieve and audit the full published paper or author manuscript before freezing an executable reproduction spec. No backtest performed.
