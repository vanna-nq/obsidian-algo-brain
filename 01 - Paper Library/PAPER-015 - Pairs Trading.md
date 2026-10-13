---
type: paper
paper_id: PAPER-015
status: metadata-and-abstract-screened
reviewed_on: 2026-10-13
category: "01 Statistical Arbitrage"
year: 2005
doi: "10.1080/14697680500149370"
source_url: "https://doi.org/10.1080/14697680500149370"
independent_backtest: false
---
# PAPER-015 — Pairs Trading

**Authors:** Robert J. Elliott; John Van Der Hoek; William P. Malcolm  
**Publication:** Quantitative Finance 5(3), 271–276 (2005)  
**Verified source:** https://doi.org/10.1080/14697680500149370  
**Evidence level:** Publication metadata and publisher / author abstract or accessible summary screened. Full-text derivations, exact formulas and study tables have **NOT** been independently audited here.

## Core contribution / mathematical mechanism
Models an equilibrium spread with mean-reverting Gaussian Markov dynamics and noisy observations to support inference about divergence and convergence.

## Source-supported result or scope
Latent spreads can be forecast and traded using model-filtered deviations under restrictive process assumptions.

## Risks and limitations
OU/Markov spread assumptions require stability; spreads can jump or permanently diverge; filtering can be sensitive to future-data leakage.

## Required data for replication
Time-stamped synchronized asset prices, realized transaction costs, rolling parameter estimation, feasible short exposure.

## Falsifiable follow-up experiment (proposed only)
Compare a filtered-mean-reversion rule to naive z-score pairs in non-overlapping OOS sessions with realistic costs.

## Methodology cross-link
- [[02 - Trading Methodologies/01 Statistical Arbitrage/README|Statistical Arbitrage]]

## Research discipline
- Claims above reflect literature, NOT replicated returns, verified strategy edges or successful live execution.
- Before implementation, read the full paper, identify exact sample/version and executable timestamp semantics, preregister the test, and preserve positive and negative findings.
- Any profitability claim must be assessed against spread, commissions, slippage, short costs, financing, data availability and strictly chronological holdouts.
