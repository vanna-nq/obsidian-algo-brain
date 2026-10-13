---
type: paper
paper_id: PAPER-020
status: metadata-and-abstract-screened
reviewed_on: 2026-10-13
category: "04 Machine Learning"
year: 2017
doi: "10.1016/j.ejor.2016.10.031"
source_url: "https://doi.org/10.1016/j.ejor.2016.10.031"
independent_backtest: false
---
# PAPER-020 — Deep Neural Networks Gradient-Boosted Trees Random Forests: Statistical Arbitrage on the S&P 500

**Authors:** Christopher Krauss; Xuan Anh Do; Nicolas Huck  
**Publication:** European Journal of Operational Research 259(2), 689–702 (2017)  
**Verified source:** https://doi.org/10.1016/j.ejor.2016.10.031  
**Evidence level:** Publication metadata and publisher / author abstract or accessible summary screened. Full-text derivations, exact formulas and study tables have **NOT** been independently audited here.

## Core contribution / mathematical mechanism
Compares deep neural nets, gradient boosting, random forests and ensembles for ranking stocks on next-day market-relative returns.

## Source-supported result or scope
Authors report strong historical gross, pre-cost predictions and ensemble returns on their 1992–2015 data, with noted decay over time.

## Risks and limitations
Author result explicitly before transaction costs; short-stock borrow, bid-ask, capacity, constituent membership and multiple testing are major threats.

## Required data for replication
Point-in-time S&P membership, adjusted lagged stock returns, open-to-open next-day fills, commissions and borrow costs.

## Falsifiable follow-up experiment (proposed only)
Test ensemble rank utility versus linear/logistic ranking on post-publication universe after turnover, borrow and impact.

## Methodology cross-link
- [[02 - Trading Methodologies/04 Machine Learning/README|Machine Learning]]

## Research discipline
- Claims above reflect literature, NOT replicated returns, verified strategy edges or successful live execution.
- Before implementation, read the full paper, identify exact sample/version and executable timestamp semantics, preregister the test, and preserve positive and negative findings.
- Any profitability claim must be assessed against spread, commissions, slippage, short costs, financing, data availability and strictly chronological holdouts.
