---
type: paper
paper_id: PAPER-019
status: metadata-and-abstract-screened
reviewed_on: 2026-10-13
category: "03 Market Microstructure"
year: 2014
doi: "10.1093/jjfinec/nbt003"
source_url: "https://doi.org/10.1093/jjfinec/nbt003"
independent_backtest: false
---
# PAPER-019 — The Price Impact of Order Book Events

**Authors:** Rama Cont; Arseniy Kukanov; Sasha Stoikov  
**Publication:** Journal of Financial Econometrics 12(1), 47–88 (2014)  
**Verified source:** https://doi.org/10.1093/jjfinec/nbt003  
**Evidence level:** Publication metadata and publisher / author abstract or accessible summary screened. Full-text derivations, exact formulas and study tables have **NOT** been independently audited here.

## Core contribution / mathematical mechanism
Examines price impact of market orders, limit orders and cancellations via order-flow imbalance at best bid/ask.

## Source-supported result or scope
Empirical sample of 50 NYSE stocks supports a near-linear relation between short-horizon price changes and order-flow imbalance, with slope inversely related to depth.

## Risks and limitations
Contemporaneous order flow can explain prices without predicting future prices; same-interval regression is not a tradable causal signal.

## Required data for replication
L1 quotes plus event stream, accurate time alignment, trade execution prices and queue handling.

## Falsifiable follow-up experiment (proposed only)
Test strictly lagged OFI for incremental future-return or execution-value prediction against a matched OHLCV baseline.

## Methodology cross-link
- [[02 - Trading Methodologies/03 Market Microstructure/README|Market Microstructure]]

## Research discipline
- Claims above reflect literature, NOT replicated returns, verified strategy edges or successful live execution.
- Before implementation, read the full paper, identify exact sample/version and executable timestamp semantics, preregister the test, and preserve positive and negative findings.
- Any profitability claim must be assessed against spread, commissions, slippage, short costs, financing, data availability and strictly chronological holdouts.
