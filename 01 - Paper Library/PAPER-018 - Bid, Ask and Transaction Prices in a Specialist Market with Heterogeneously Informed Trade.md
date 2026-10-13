---
type: paper
paper_id: PAPER-018
status: metadata-and-abstract-screened
reviewed_on: 2026-10-13
category: "03 Market Microstructure"
year: 1985
doi: "10.1016/0304-405X(85)90044-3"
source_url: "https://doi.org/10.1016/0304-405X(85)90044-3"
independent_backtest: false
---
# PAPER-018 — Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders

**Authors:** Lawrence R. Glosten; Paul R. Milgrom  
**Publication:** Journal of Financial Economics 14(1), 71–100 (1985)  
**Verified source:** https://doi.org/10.1016/0304-405X(85)90044-3  
**Evidence level:** Publication metadata and publisher / author abstract or accessible summary screened. Full-text derivations, exact formulas and study tables have **NOT** been independently audited here.

## Core contribution / mathematical mechanism
Adverse selection makes competitive market makers quote a bid-ask spread even with zero expected economic profit.

## Source-supported result or scope
Reported transaction-price changes contain microstructure effects; returns measured at transaction prices can differ from implementable investment returns.

## Risks and limitations
Stylized dealer equilibrium rather than modern multi-venue order-driven execution; trade direction and spread cannot be recovered reliably from OHLCV.

## Required data for replication
Best bid/ask quotes, trades, spreads, aggressor inference and contemporaneous depth.

## Falsifiable follow-up experiment (proposed only)
Quantify how bid-ask bounce and adverse-selection spread alter short-horizon signal profitability relative to midquote backtests.

## Methodology cross-link
- [[02 - Trading Methodologies/03 Market Microstructure/README|Market Microstructure]]

## Research discipline
- Claims above reflect literature, NOT replicated returns, verified strategy edges or successful live execution.
- Before implementation, read the full paper, identify exact sample/version and executable timestamp semantics, preregister the test, and preserve positive and negative findings.
- Any profitability claim must be assessed against spread, commissions, slippage, short costs, financing, data availability and strictly chronological holdouts.
