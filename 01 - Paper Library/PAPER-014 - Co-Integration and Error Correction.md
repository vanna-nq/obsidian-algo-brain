---
type: paper
paper_id: PAPER-014
status: metadata-and-abstract-screened
reviewed_on: 2026-10-13
category: "01 Statistical Arbitrage"
year: 1987
doi: "10.2307/1913236"
source_url: "https://doi.org/10.2307/1913236"
independent_backtest: false
---
# PAPER-014 — Co-Integration and Error Correction

**Authors:** Robert F. Engle; Clive W. J. Granger  
**Publication:** Econometrica 55(2), 251–276 (1987)  
**Verified source:** https://doi.org/10.2307/1913236  
**Evidence level:** Publication metadata and publisher / author abstract or accessible summary screened. Full-text derivations, exact formulas and study tables have **NOT** been independently audited here.

## Core contribution / mathematical mechanism
Defines cointegration and error-correction representations for integrated time series; proposes testing and estimation tools.

## Source-supported result or scope
A stationary combination of individually integrated asset prices is a potential equilibrium spread, NOT proof it survives trading costs.

## Risks and limitations
Integrate spreads only after out-of-sample stability and correctly designed stationarity tests; avoid arbitrary log-price vs price mixing.

## Required data for replication
Rolling cointegrating-vector estimates, adjusted stock/futures series, delisting/borrow, bid-ask and funding; train-only unit-root/cointegration testing.

## Falsifiable follow-up experiment (proposed only)
Test whether pre-registered formation-window cointegration improves OOS pair trading versus distance pairing and shuffled-pair controls.

## Methodology cross-link
- [[02 - Trading Methodologies/01 Statistical Arbitrage/README|Statistical Arbitrage]]

## Research discipline
- Claims above reflect literature, NOT replicated returns, verified strategy edges or successful live execution.
- Before implementation, read the full paper, identify exact sample/version and executable timestamp semantics, preregister the test, and preserve positive and negative findings.
- Any profitability claim must be assessed against spread, commissions, slippage, short costs, financing, data availability and strictly chronological holdouts.
