---
type: paper
paper_id: PAPER-001
status: literature-reviewed-not-replicated
title: "Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY)"
authors: ["Carlo Zarattini", "Andrew Aziz", "Andrea Barbon"]
first_version: 2024-05-10
reviewed_version: 2025-09-22
journal_or_series: "Swiss Finance Institute Research Paper Series No. 24-97"
ssrn_id: 4824172
url: "https://papers.ssrn.com/sol3/Delivery.cfm/4824172.pdf?abstractid=4824172"
markets: ["SPY", "S&P 500"]
timeframes: ["1-minute input", "30-minute decision intervals"]
methodologies: ["Trend and Momentum", "Intraday Price Structure", "Market Microstructure", "Volatility and Derivatives", "Regime Detection"]
paper_pages: 43
input_file: "4824172.pdf (user provided)"
input_file_sha256: "865010dfd938d513c1cd22a7be5932bc232afe498c3cf493d6d8bd4b0de86ebb"
research_status: "external author claim; no independent replication"
---
# PAPER-001 — Beat the Market: SPY Intraday Momentum

> **Evidence status:** Literature reviewed; original empirical claims **not** independently replicated by us. Never quote reported Sharpe/IRR as our backtest. Version reviewed: 22 Sep 2025; paper's headline test ends Apr 2024. Preserve later FAQ updates as a separate sample/version.

## Source / provenance
- **Authors:** Carlo Zarattini, Andrew Aziz, Andrea Barbon.
- **Series:** Swiss Finance Institute Research Paper No. 24-97; original May 2024, revised Sep 2025.
- **SSRN PDF:** https://papers.ssrn.com/sol3/Delivery.cfm/4824172.pdf?abstractid=4824172
- **Uploaded source fingerprint:** SHA-256 \`865010dfd938d513c1cd22a7be5932bc232afe498c3cf493d6d8bd4b0de86ebb\` (43 PDF pages).
- **Original data:** IQFeed SPY and VIX 1-minute OHLCV; May 2007 through April 2024; backtests in MATLAB R2023a (paper p.6).
- **Related implementations (author resources, NOT necessarily identical versions):**
  - https://concretumgroup.com/coding/
  - https://www.concretumgroup.com/python-backtesting-beat-the-market-an-effective-intraday-momentum-strategy-for-the-sp500-etf-spy/
  - https://concretumgroup.com/backtesting-7-years-of-free-data-beat-the-market-an-effective-intraday-momentum-strategy-for-the-sp500-etf-spy/ — **extended version includes an overnight-gap reversal component**; DO NOT confuse its performance with the original paper.

## Research question and economic mechanism
Can departures outside a time-of-day-conditioned *Noise Area* around the day's open/previous close predict continued SPY price movement within the same regular trading session? Authors attribute persistence to demand/supply imbalances, slow incorporation of information, and potentially dealer hedging effects. Those mechanisms are hypotheses, **not directly measured causal mechanisms** in the SPY OHLCV backtest. Paper pp.3-9, 23-24.

## Reconstructable mathematical definitions (paper pp.6-7, 13, 15, 21)
For trading day t, minute-of-day h, and previous 14 trading sessions i=1,...,14:

\`\`\`text
move[t-i,h] = abs( Close[t-i,h] / Open[t-i,09:30] - 1 )
sigma_open[t,h] = (1/14) * sum_i move[t-i,h]

UB[t,h] = max(Open[t,09:30], Close[t-1,16:00]) * (1 + VM*sigma_open[t,h])
LB[t,h] = min(Open[t,09:30], Close[t-1,16:00]) * (1 - VM*sigma_open[t,h])
Base paper: VM = 1, lookback = 14 previous sessions.
\`\`\`

The sigma above is **not** the 14-day *daily-return standard deviation* used below for sizing. It is an average ABSOLUTE open-relative move specific to the clock time. Use completed prior sessions only. Gap handling anchors the band to both today's open and yesterday's close.

**Trading rules (paper pp.9-10, 13):**
1. SPY regular session, 09:30–16:00 New York time; first possible trading decision 10:00.
2. Evaluate position changes only on HH:00 and HH:30. Above UB = long; below LB = short; inside Noise Area = no new position.
3. Original base comparator uses opposite-band stop and may reverse if opposite boundary is crossed.
4. Refined model uses \`long_stop = max(UB, session_VWAP)\`, \`short_stop = min(LB, session_VWAP)\`, using regular-hours VWAP. Close at a stop or session end. Treat stop sampling/execution timing as **replication ambiguity** until inspecting released code: prose discusses semi-hourly-only decisions/stops yet also says exit as soon as bands/VWAP cross.
5. Flatten all positions by market close. No overnight SPY exposure.

**Daily volatility targeting (paper p.15):**
\`\`\`text
daily_vol_14[t] = sample_std( prior 14 daily SPY returns )
leverage[t] = min(4, 0.02 / daily_vol_14[t])
shares[t] = floor( AUM[t-1] * leverage[t] / Open[t,09:30] )
\`\`\`
Paper targets 2% *daily* market volatility and caps leverage at 4x. Exact treatment of zero volatility, minimum leverage, fractional share rounding, margin financing, leverage restrictions and any dividends must be established before reproduction.

## Authors' historical performance — distinguish variants (paper Table 3, p.15)
| SPY configuration | Total return | CAGR/IRR | Ann. vol | Sharpe | Max DD | Daily hit |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Opposite-band stop, 100% exposure | 178% | 6.2% | 10.9% | 0.61 | 21% | 54% |
| Current-band + VWAP stop, 100% exposure | 380% | 9.7% | 7.7% | 1.24 | 12% | 43% |
| Current-band + VWAP, dynamically sized up to 4x | **1,985%** | **19.6%** | 14.3% | **1.33** | **25%** | 43% |
| SPY buy-and-hold | 227% | 7.2% | 20.2% | 0.45 | 56% | 54% |

Initial portfolio = $100,000. Cost assumptions = $0.0035/share commissions and $0.001/share slippage; authors present a small real-trading slippage study of 1,000+ trades in April 2024 (paper pp.10,24-25). Numbers above are **author-reported net-of-cost historical simulations** and are not an audit of financing, borrow, impact or live fills. Dynamic sizing substantially magnifies total return and drawdown; do NOT conflate that with unlevered signal quality. Tables 1–4 and Appendix A1.

## Conditioning analyses / subsidiary findings (authors' claims)
- **VIX regime:** Sharpe rose as VIX rose across some thresholds; above VIX 40 ~3.5, with uncertainty in very high-VIX tails (paper pp.17-18, Fig.8). Do not interpret this as a preregistered causal effect.
- **Prior-day NR4:** 660 observations, mean 22 bps/day, t=5.14, Sharpe 3.2 (paper p.19, Table 5); possible multiple-testing and overlapping-definition concerns. Triangle: 664 observations, 14 bps/day, t=3.19.
- **Weekdays:** Wednesday mean 18 bps/day, t=3.42 (paper p.21, Table 6), possible FOMC/selection effects; not sufficient for a live weekday rule.
- **Volatility multiplier:** paper presents VM=1; retrospective VM ~1.5 had higher Sharpe (paper pp.21-22); do not optimize on the same sample then call it OOS.
- **Gamma explanation:** lagged 5-day SPY RSI associated negatively with next-day strategy profitability (reported slope -3.25, p=0.001; paper pp.23-24). **RSI is NOT an observed dealer gamma imbalance**; interpretation as dealer gamma is speculative.
- **Expanded futures tests:** FAQ Q13 (p.35) reports testing 33 futures markets Jan 2007-Sep 2024, diversified portfolio Sharpe 1.65. 21 commodity instruments are anonymized as "***" in its table; do not claim named contract-level replicability for them.
- **FAQ revisions:** Q22, p.40 shows updated SPY sample May 2007–Dec 2024, dynamically sized current-band+VWAP **2,382% / Sharpe 1.35**, vs p.15's **1,985% / Sharpe 1.33** on earlier sample. Different windows; maintain separate versions. Q24 reports later monthly update through Aug 2025 (pp.41-42).

## Replication gaps, failure modes, and critique
1. **Execution causality:** determine whether HH:00 signals use already closed minute bars, and fill at next available price; no contemporaneous open+close access. Semi-hourly decision logic and trailing-stop triggering descriptions need reconciliation with released code.
2. **Dynamic leverage:** 2% daily vol target implies variable gross exposure and up to 4x; include spread, impact, costs, leverage/margin charges, execution participation and short availability.
3. **Data specifications:** replicate true SPY NYSE regular sessions, DST, half-days, previous-session close, splits/dividends, corporate actions, VWAP session reset, missing bars, and quote/trade eligibility.
4. **Leakage/selection:** parameter sweeps of sigma lookback, VM, regime and pattern filters after examining historical sample are not valid independent OOS confirmations. Q6's 90-day optimum is *retrospective*.
5. **Regime inference:** VIX opening value must be timestamp-available; RSI is only a proxy. No direct L1/L2, option-position, or dealer gamma identification in these data.
6. **Independent test:** run a frozen baseline before extensions, score chronological OOS and costs/stress robustness; separate paper reproduction from hypothesis discovery.
7. **Reproducibility:** author code exists; full original IQFeed dataset is not public under the paper's data agreements (FAQ Q2). Public alternative-data implementations and extensions are not identical to original evidence.

## Interesting *untested* research hypotheses
- **H1:** Time-of-day-specific opening-distance thresholds have predictive value beyond a generic opening-range breakout under identical execution rules and costs.
- **H2:** The improvement from VWAP+same-side band is robust beyond this published SPY sample, not just an ex-post stop-selection effect.
- **H3:** Conditioning on pre-specified previous-day NR4 improves OOS risk-adjusted returns after correcting for filter selection.
- **H4:** Lagged options gamma data explains intraday trend persistence incrementally to RSI, VIX, and realized volatility.
- **H5:** The methodology may transfer to liquid equity index futures with appropriate session, tick-cost and contract-roll modeling, but must be tested contract by contract.

## Links to methodology indexes
- [[02 - Trading Methodologies/02 Trend and Momentum/README|Trend and Momentum]] — primary.
- [[02 - Trading Methodologies/11 Intraday Price Structure/README|Intraday Price Structure]] — dynamic noise boundary and gap effects.
- [[02 - Trading Methodologies/03 Market Microstructure/README|Market Microstructure]] — hypothesized flow and dealer mechanics.
- [[02 - Trading Methodologies/07 Volatility and Derivatives/README|Volatility and Derivatives]] — sizing, VIX, dealer gamma hypothesis.
- [[02 - Trading Methodologies/08 Regime Detection/README|Regime Detection]] — VIX and volatility conditions.

## Next research step — NOT EXECUTED
Before testing: verify whether vetted, adjusted, full-session **SPY 1-minute OHLCV** is available and list data coverage. If unavailable, do **not** silently substitute SPX500 1-hour, GC 5-minute, or NVDA/SMH 5-minute as a replication. No code, backtest, independent performance metric or validation has yet been produced for PAPER-001.
