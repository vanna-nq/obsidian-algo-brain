---
type: paper
paper_id: PAPER-008
status: abstract-screened-not-replicated
primary_methodology: "07 Volatility and Derivatives"
year: 2009
doi: "10.1093/rfs/hhn038"
source_url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1359527"
review_date: 2026-10-13
---
# PAPER-008 — Variance Risk Premiums

**Authors:** Peter Carr; Liuren Wu  
**Publication:** Review of Financial Studies 22(3), 1311-1341 (2009)  
**DOI:** https://doi.org/10.1093/rfs/hhn038  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1359527  
**Evidence access:** Empirical peer-reviewed, journal/SSRN abstracts reviewed.

> **Research status: AUTHOR CLAIMS / THEORY ONLY.** Source metadata and abstract or author materials reviewed. No independent implementation, full-paper equation audit, dataset verification, or backtest was executed for this note. If replicating, obtain the full version of record and verify all detailed rules against it.

## Economic / mathematical mechanism
Contrast option-implied risk-neutral expected variance (approximated by a portfolio of options) with subsequently realized variance. The difference reflects compensation for bearing variance risk under specific conventions.

## What the authors report (NOT our results)
Authors synthesize variance-swap rates using a large option dataset for five stock indexes and 35 individual stocks, and study historical variance premia. This does not directly validate a short-term direction signal.

## Data and implementation requirements
Option chain, exact strikes and expirations, bid/ask, risk-free and dividend inputs, synchronized underlying prices, forward variance and realized-variance convention, accurate term alignment.

## Limitations and replication hazards
Variance premium SIGN conventions differ across papers (realized minus implied vs implied minus realized). Do not silently mix. Option skew/illiquidity, jump risk, sell-volatility tails, model assumptions and margin can swamp theoretical premia.

## Candidate falsifiable hypothesis (our proposal, UNTESTED)
A lagged, executable option-implied variance premium contains incremental information about future volatility regime beyond recent realized volatility and VIX alone.

## Proposed validation / first test (NOT executed)
Timestamp option quotes, use an unambiguous ex-ante term/maturity, strictly future realized-variance target, and evaluate forecasting plus tradable implementation separately with hedging costs.

## Knowledge graph
- **Primary:** [[02 - Trading Methodologies/07 Volatility and Derivatives/README|07 Volatility and Derivatives]]
- **Related:** [[02 - Trading Methodologies/08 Regime Detection/README|08 Regime Detection]]
- **Related:** [[02 - Trading Methodologies/03 Market Microstructure/README|03 Market Microstructure]]

## What this paper does NOT show
- That the reported pattern still exists after 2025-2026, under your broker/exchange, or with your current dataset.
- That reported prediction metrics or theoretical existence are the same as causal, executable after-cost trading alpha.
- That paper parameters may be retuned on a test set and still called independent out-of-sample validation.

## Next action
Retrieve and audit the full published paper or author manuscript before freezing an executable reproduction spec. No backtest performed.
