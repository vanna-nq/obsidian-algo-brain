---
type: paper
paper_id: PAPER-029
status: metadata-and-abstract-screened
reviewed_on: 2026-10-13
category: "08 Regime Detection"
year: 2002
doi: "10.1093/rfs/15.4.1137"
source_url: "https://doi.org/10.1093/rfs/15.4.1137"
independent_backtest: false
---
# PAPER-029 — International Asset Allocation With Regime Shifts

**Authors:** Andrew Ang; Geert Bekaert  
**Publication:** Review of Financial Studies 15(4), 1137–1187 (2002)  
**Verified source:** https://doi.org/10.1093/rfs/15.4.1137  
**Evidence level:** Publication metadata and publisher / author abstract or accessible summary screened. Full-text derivations, exact formulas and study tables have **NOT** been independently audited here.

## Core contribution / mathematical mechanism
Solves dynamic international portfolio-choice problem where state-dependent expected returns, volatility and correlations change under regimes.

## Source-supported result or scope
Authors conclude diversification can remain valuable despite higher correlations in volatile bear regimes, with benefits depending on available asset choices and hedging.

## Risks and limitations
Latent-state estimation instability, nontradable backtested assets, currency and funding exposures, estimation error in crisis covariance.

## Required data for replication
Country-equity and FX time series, short rates, costs, one-sided filtering and dynamic correlation estimates.

## Falsifiable follow-up experiment (proposed only)
Compare ex-ante regime-aware risk allocation with constant-weight and equal-vol portfolios on unseen crises net of currency hedging costs.

## Methodology cross-link
- [[02 - Trading Methodologies/08 Regime Detection/README|Regime Detection]]

## Research discipline
- Claims above reflect literature, NOT replicated returns, verified strategy edges or successful live execution.
- Before implementation, read the full paper, identify exact sample/version and executable timestamp semantics, preregister the test, and preserve positive and negative findings.
- Any profitability claim must be assessed against spread, commissions, slippage, short costs, financing, data availability and strictly chronological holdouts.
