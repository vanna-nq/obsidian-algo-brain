---
type: paper
paper_id: PAPER-034
status: metadata-and-abstract-screened
reviewed_on: 2026-10-13
category: "11 Intraday Price Structure"
year: 2010
doi: "10.1111/j.1540-6261.2010.01573.x"
source_url: "https://doi.org/10.1111/j.1540-6261.2010.01573.x"
independent_backtest: false
---
# PAPER-034 — Intraday Patterns in the Cross-section of Stock Returns

**Authors:** Steven L. Heston; Robert A. Korajczyk; Ronnie Sadka  
**Publication:** Journal of Finance 65(4), 1369–1407 (2010)  
**Verified source:** https://doi.org/10.1111/j.1540-6261.2010.01573.x  
**Evidence level:** Publication metadata and publisher / author abstract or accessible summary screened. Full-text derivations, exact formulas and study tables have **NOT** been independently audited here.

## Core contribution / mathematical mechanism
Identifies return continuation at identical half-hour-of-day slots across trading days and very short-term liquidity-driven reversals.

## Source-supported result or scope
Authors find repeating half-hour return patterns persisting many sessions and distinct sub-hour reversal effects associated with liquidity and bid-ask bounce.

## Risks and limitations
This is a stock cross-section time-of-day phenomenon, not necessarily SPY HOD/LOD timing; avoid time-zone/DST and bid-ask bounce errors.

## Required data for replication
Intraday stock trades/quotes, precise HH:MM mapping across exchange days, historical liquidity/volume and execution costs.

## Falsifiable follow-up experiment (proposed only)
Measure out-of-sample recurrence at matched intraday time slots and compare with intraday seasonal and liquidity nulls.

## Methodology cross-link
- [[02 - Trading Methodologies/11 Intraday Price Structure/README|Intraday Price Structure]]

## Research discipline
- Claims above reflect literature, NOT replicated returns, verified strategy edges or successful live execution.
- Before implementation, read the full paper, identify exact sample/version and executable timestamp semantics, preregister the test, and preserve positive and negative findings.
- Any profitability claim must be assessed against spread, commissions, slippage, short costs, financing, data availability and strictly chronological holdouts.
