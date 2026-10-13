---
type: paper
paper_id: PAPER-025
status: metadata-and-abstract-screened
reviewed_on: 2026-10-13
category: "06 Information Theory"
year: 2000
doi: "10.1103/PhysRevLett.85.461"
source_url: "https://doi.org/10.1103/PhysRevLett.85.461"
independent_backtest: false
---
# PAPER-025 — Measuring Information Transfer

**Authors:** Thomas Schreiber  
**Publication:** Physical Review Letters 85(2), 461–464 (2000)  
**Verified source:** https://doi.org/10.1103/PhysRevLett.85.461  
**Evidence level:** Publication metadata and publisher / author abstract or accessible summary screened. Full-text derivations, exact formulas and study tables have **NOT** been independently audited here.

## Core contribution / mathematical mechanism
Develops transfer entropy as a directional information-theoretic dependence measure conditioning on a receiving process's history.

## Source-supported result or scope
Theoretical and numerical tool to distinguish information flow patterns from shared-history effects; it does not automatically prove causal intervention or arbitrage.

## Risks and limitations
Spurious links from nonstationarity, common drivers, lag misalignment, estimator bias and data snooping.

## Required data for replication
Synchronized multi-asset return innovations, lag design, point-in-time conditioning information and surrogate nulls.

## Falsifiable follow-up experiment (proposed only)
Pre-register lags and estimate OOS conditional transfer entropy, then ask if it improves forecast log-loss and after-cost policy utility.

## Methodology cross-link
- [[02 - Trading Methodologies/06 Information Theory/README|Information Theory]]

## Research discipline
- Claims above reflect literature, NOT replicated returns, verified strategy edges or successful live execution.
- Before implementation, read the full paper, identify exact sample/version and executable timestamp semantics, preregister the test, and preserve positive and negative findings.
- Any profitability claim must be assessed against spread, commissions, slippage, short costs, financing, data availability and strictly chronological holdouts.
