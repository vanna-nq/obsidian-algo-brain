---
type: paper
paper_id: PAPER-026
status: metadata-and-abstract-screened
reviewed_on: 2026-10-13
category: "07 Volatility and Derivatives"
year: 2009
doi: "10.1093/rfs/hhp008"
source_url: "https://doi.org/10.1093/rfs/hhp008"
independent_backtest: false
---
# PAPER-026 — Expected Stock Returns and Variance Risk Premia

**Authors:** Tim Bollerslev; George Tauchen; Hao Zhou  
**Publication:** Review of Financial Studies 22(11), 4463–4492 (2009)  
**Verified source:** https://doi.org/10.1093/rfs/hhp008  
**Evidence level:** Publication metadata and publisher / author abstract or accessible summary screened. Full-text derivations, exact formulas and study tables have **NOT** been independently audited here.

## Core contribution / mathematical mechanism
Relates the gap between model-free option-implied future variance and realized market variance to future aggregate equity returns.

## Source-supported result or scope
Authors report predictive power at an intermediate, roughly quarterly, horizon, especially with high-frequency realized variance estimates.

## Risks and limitations
Overlapping prediction windows, look-ahead in implied volatility, realized-variance measurement and regime variation; not an intraday trading rule.

## Required data for replication
Timestamped S&P option quotes and high-frequency SPX returns, reliable realized variance, dividend/rate curves, quarterly future returns.

## Falsifiable follow-up experiment (proposed only)
Use a frozen variance-risk-premium estimate to forecast untouched next-quarter equity returns with Newey-West or overlap-robust inference.

## Methodology cross-link
- [[02 - Trading Methodologies/07 Volatility and Derivatives/README|Volatility and Derivatives]]

## Research discipline
- Claims above reflect literature, NOT replicated returns, verified strategy edges or successful live execution.
- Before implementation, read the full paper, identify exact sample/version and executable timestamp semantics, preregister the test, and preserve positive and negative findings.
- Any profitability claim must be assessed against spread, commissions, slippage, short costs, financing, data availability and strictly chronological holdouts.
