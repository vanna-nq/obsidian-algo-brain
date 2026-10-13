---
type: paper
paper_id: PAPER-035
status: metadata-and-abstract-screened
reviewed_on: 2026-10-13
category: "11 Intraday Price Structure"
year: 2021
doi: "10.1016/j.jfineco.2021.04.029"
source_url: "https://doi.org/10.1016/j.jfineco.2021.04.029"
independent_backtest: false
---
# PAPER-035 — Hedging Demand and Market Intraday Momentum

**Authors:** Guido Baltussen; Zhi Da; Sten Lammers; Martin Martens  
**Publication:** Journal of Financial Economics 142(1), 377–403 (2021)  
**Verified source:** https://doi.org/10.1016/j.jfineco.2021.04.029  
**Evidence level:** Publication metadata and publisher / author abstract or accessible summary screened. Full-text derivations, exact formulas and study tables have **NOT** been independently audited here.

## Core contribution / mathematical mechanism
Studies cross-market continuation into the last 30 minutes and links effect to options-dealer short-gamma hedging and leveraged ETF rebalancing demands.

## Source-supported result or scope
Across more than 60 global futures markets over 1974–2020, authors report last-half-hour return predictability and evidence consistent with gamma-hedging demand.

## Risks and limitations
Dealer hedging proxies and historical results require careful identification; not all momentum can be causally attributed to gamma; real futures closing times differ.

## Required data for replication
Intraday futures with actual local exchange hours, option exposure/LETF flow measures, roll/tick fees and close-price execution quality.

## Falsifiable follow-up experiment (proposed only)
Test strictly lagged rest-of-day return and measured hedging-demand interaction for held-out closing half-hours, controlling for volatility/news.

## Methodology cross-link
- [[02 - Trading Methodologies/11 Intraday Price Structure/README|Intraday Price Structure]]

## Research discipline
- Claims above reflect literature, NOT replicated returns, verified strategy edges or successful live execution.
- Before implementation, read the full paper, identify exact sample/version and executable timestamp semantics, preregister the test, and preserve positive and negative findings.
- Any profitability claim must be assessed against spread, commissions, slippage, short costs, financing, data availability and strictly chronological holdouts.
