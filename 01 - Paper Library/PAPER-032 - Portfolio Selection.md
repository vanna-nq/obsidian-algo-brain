---
type: paper
paper_id: PAPER-032
status: metadata-and-abstract-screened
reviewed_on: 2026-10-13
category: "10 Optimization and Physics"
year: 1952
doi: "10.1111/j.1540-6261.1952.tb01525.x"
source_url: "https://doi.org/10.1111/j.1540-6261.1952.tb01525.x"
independent_backtest: false
---
# PAPER-032 — Portfolio Selection

**Authors:** Harry Markowitz  
**Publication:** Journal of Finance 7(1), 77–91 (1952)  
**Verified source:** https://doi.org/10.1111/j.1540-6261.1952.tb01525.x  
**Evidence level:** Publication metadata and publisher / author abstract or accessible summary screened. Full-text derivations, exact formulas and study tables have **NOT** been independently audited here.

## Core contribution / mathematical mechanism
Foundational mean-variance portfolio choice: trade off expected return against variance and covariance-based risk for feasible portfolios.

## Source-supported result or scope
A normative allocation framework, not a predictive alpha algorithm and not empirical evidence of high Sharpe ratios.

## Risks and limitations
Expected return/covariance estimation noise, non-Gaussian tails, constraints, turnover and transaction costs dominate naive optimizer results.

## Required data for replication
Assets' point-in-time return matrices, costs, risk caps, expected-return forecasts and short/leverage rules.

## Falsifiable follow-up experiment (proposed only)
Implement shrinkage/robust allocations and compare to equal-weight/minimum-variance on untouched risk-adjusted samples.

## Methodology cross-link
- [[02 - Trading Methodologies/10 Optimization and Physics/README|Optimization and Physics]]

## Research discipline
- Claims above reflect literature, NOT replicated returns, verified strategy edges or successful live execution.
- Before implementation, read the full paper, identify exact sample/version and executable timestamp semantics, preregister the test, and preserve positive and negative findings.
- Any profitability claim must be assessed against spread, commissions, slippage, short costs, financing, data availability and strictly chronological holdouts.
