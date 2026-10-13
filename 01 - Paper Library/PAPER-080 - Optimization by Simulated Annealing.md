---
type: paper
paper_id: PAPER-080
status: primary-source-abstract-screened
category: "10 Optimization and Physics"
year: 1983
reviewed_on: 2026-10-13
doi: "10.1126/science.220.4598.671"
source_url: "https://www.science.org/doi/10.1126/science.220.4598.671"
replicated: false
---
# PAPER-080 — Optimization by Simulated Annealing

**Authors:** Scott Kirkpatrick; C. Daniel Gelatt Jr.; Mario P. Vecchi  
**Publication:** Science 220(4598), 671–680 (1983)  
**Primary research source:** https://www.science.org/doi/10.1126/science.220.4598.671
**DOI:** https://doi.org/10.1126/science.220.4598.671

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Introduces temperature-based stochastic optimization inspired by physical annealing for difficult combinatorial problems.

## Author-reported finding or theoretical scope
A classical optimization method drawing on statistical mechanics; NOT evidence that Ising objectives contain financial predictability or quantum advantage.

## Required data / feasibility gate
Exact risk/cost/constraint objective in discrete positions, sampling budget, annealing schedule, exact and mixed-integer baselines.

## Critique / potential failure
Temperature schedules and penalty scaling change solution feasibility; minimizing a misestimated objective may worsen true portfolio performance.

## Falsifiable follow-up (proposal only)
Implement simulated annealing on a fixed cardinality-constrained portfolio QUBO and compare feasible optimum gaps to MILP, exhaustive small cases and heuristics.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/10 Optimization and Physics/README|Optimization and Physics]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
