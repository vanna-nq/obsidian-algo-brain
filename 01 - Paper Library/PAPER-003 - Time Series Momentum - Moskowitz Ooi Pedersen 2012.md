---
type: paper
paper_id: PAPER-003
status: abstract-screened-not-replicated
primary_methodology: "02 Trend and Momentum"
year: 2012
doi: "10.1016/j.jfineco.2011.11.003"
source_url: "https://doi.org/10.1016/j.jfineco.2011.11.003"
review_date: 2026-10-13
---
# PAPER-003 — Time Series Momentum

**Authors:** Tobias J. Moskowitz; Yao Hua Ooi; Lasse Heje Pedersen  
**Publication:** Journal of Financial Economics 104(2), 228-250 (2012)  
**DOI:** https://doi.org/10.1016/j.jfineco.2011.11.003  
**Source:** https://doi.org/10.1016/j.jfineco.2011.11.003  
**Evidence access:** Empirical peer-reviewed, publisher abstract reviewed.

> **Research status: AUTHOR CLAIMS / THEORY ONLY.** Source metadata and abstract or author materials reviewed. No independent implementation, full-paper equation audit, dataset verification, or backtest was executed for this note. If replicating, obtain the full version of record and verify all detailed rules against it.

## Economic / mathematical mechanism
An asset's own lagged cumulative return predicts continuation; positions follow the sign of the past return rather than cross-sectionally sorting all assets. Futures enable both long and short exposures with volatility-aware risk budgets.

## What the authors report (NOT our results)
The authors examine 58 liquid equity-index, bond, currency and commodity futures. They report continuation at 1–12-month horizons and partial longer-horizon reversal, with diversified crisis-period performance. Not an intraday result.

## Data and implementation requirements
Continuous back-adjusted futures prices with transparent roll conventions, executable front-month quotes, funding, margin, and per-contract specifications; monthly-to-yearly lookbacks.

## Limitations and replication hazards
Historical trends vary by era and contract; returns depend on roll convention, gross vs net treatment, volatility targeting, capacity, and regime shifts; copying a monthly horizon into a 3-minute chart is unjustified.

## Candidate falsifiable hypothesis (our proposal, UNTESTED)
A prespecified multi-market sign-of-past-return futures portfolio outperforms an equally risked passive baseline after realistic contract roll and transaction costs on unseen years.

## Proposed validation / first test (NOT executed)
Freeze lookback and vol-target ex ante, split chronology, use real contract rolls, evaluate crisis and low-trend regimes, turnover, drawdowns and sensitivity to carry.

## Knowledge graph
- **Primary:** [[02 - Trading Methodologies/02 Trend and Momentum/README|02 Trend and Momentum]]
- **Related:** [[02 - Trading Methodologies/12 Cross Asset and Macro/README|12 Cross Asset and Macro]]
- **Related:** [[02 - Trading Methodologies/08 Regime Detection/README|08 Regime Detection]]

## What this paper does NOT show
- That the reported pattern still exists after 2025-2026, under your broker/exchange, or with your current dataset.
- That reported prediction metrics or theoretical existence are the same as causal, executable after-cost trading alpha.
- That paper parameters may be retuned on a test set and still called independent out-of-sample validation.

## Next action
Retrieve and audit the full published paper or author manuscript before freezing an executable reproduction spec. No backtest performed.
