---
type: paper
paper_id: PAPER-023
status: metadata-and-abstract-screened
reviewed_on: 2026-10-13
category: "05 Deep Learning"
year: 2019
doi: "10.48550/arXiv.1904.04912"
source_url: "https://arxiv.org/abs/1904.04912"
independent_backtest: false
---
# PAPER-023 — Enhancing Time Series Momentum Strategies Using Deep Neural Networks

**Authors:** Bryan Lim; Stefan Zohren; Stephen Roberts  
**Publication:** arXiv:1904.04912 (preprint) (2019)  
**Verified source:** https://arxiv.org/abs/1904.04912  
**Evidence level:** Publication metadata and publisher / author abstract or accessible summary screened. Full-text derivations, exact formulas and study tables have **NOT** been independently audited here.

## Core contribution / mathematical mechanism
Introduces Deep Momentum Networks to jointly learn trend extraction and position sizes, using differentiable portfolio objectives and turnover-aware regularization.

## Source-supported result or scope
Authors report LSTM-based improvements on 88 futures before costs and some robustness under modest assumed costs.

## Risks and limitations
Learned direct Sharpe objectives are sensitive to backtest splitting, contract construction, hyperparameter tuning and differentiable cost approximations.

## Required data for replication
Continuous and tradable futures, lagged signals, margin and realistic rolling/turnover costs.

## Falsifiable follow-up experiment (proposed only)
Test fixed Sharpe-optimized network against simpler moving-average trend baselines with nested chronological selection and no overlapping labels.

## Methodology cross-link
- [[02 - Trading Methodologies/05 Deep Learning/README|Deep Learning]]

## Research discipline
- Claims above reflect literature, NOT replicated returns, verified strategy edges or successful live execution.
- Before implementation, read the full paper, identify exact sample/version and executable timestamp semantics, preregister the test, and preserve positive and negative findings.
- Any profitability claim must be assessed against spread, commissions, slippage, short costs, financing, data availability and strictly chronological holdouts.
