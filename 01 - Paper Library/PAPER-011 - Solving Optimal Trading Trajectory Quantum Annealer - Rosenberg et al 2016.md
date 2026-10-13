---
type: paper
paper_id: PAPER-011
status: abstract-screened-not-replicated
primary_methodology: "10 Optimization and Physics"
year: 2016
doi: "10.1109/JSTSP.2016.2574703"
source_url: "https://arxiv.org/abs/1508.06182"
review_date: 2026-10-13
---
# PAPER-011 — Solving the Optimal Trading Trajectory Problem Using a Quantum Annealer

**Authors:** Gili Rosenberg; Poya Haghnegahdar; Phil Goddard; Peter Carr; Kesheng Wu; Marcos López de Prado  
**Publication:** IEEE Journal of Selected Topics in Signal Processing (2016)  
**DOI:** https://doi.org/10.1109/JSTSP.2016.2574703  
**Source:** https://arxiv.org/abs/1508.06182  
**Evidence access:** Methodological optimization paper, author preprint and archival abstract reviewed.

> **Research status: AUTHOR CLAIMS / THEORY ONLY.** Source metadata and abstract or author materials reviewed. No independent implementation, full-paper equation audit, dataset verification, or backtest was executed for this note. If replicating, obtain the full version of record and verify all detailed rules against it.

## Economic / mathematical mechanism
Encode a discrete, multi-period optimal trading trajectory as an energy-minimization problem compatible with a quantum annealer; objective can include permanent and temporary market impact without inverting a covariance matrix.

## What the authors report (NOT our results)
Numerical demonstrations and formulation highlight feasibility at the hardware scale studied; they do NOT establish quantum advantage over best classical solvers or profitable strategy alpha.

## Data and implementation requirements
Portfolio target, trade horizon, discrete lot encoding, calibrated expected impact/temporary cost, position bounds and risk objective, precision/resource constraints.

## Limitations and replication hazards
Quadratic binary encodings need coefficient scaling and embedding; hardware size/noise, energy penalties, expensive impact miscalibration and poor solver baseline may dominate results.

## Candidate falsifiable hypothesis (our proposal, UNTESTED)
A transparent QUBO/Ising formulation can find more efficient discrete trade schedules than a naive heuristic at equal risk and computation budget, without requiring quantum hardware.

## Proposed validation / first test (NOT executed)
Implement exact small-case solver and classical simulated annealing/MIP baselines first; compare objective residuals, constraint violations, wall-clock runtime and sensitivities; quantum benchmarking only if evidence justifies.

## Knowledge graph
- **Primary:** [[02 - Trading Methodologies/10 Optimization and Physics/README|10 Optimization and Physics]]
- **Related:** [[02 - Trading Methodologies/07 Volatility and Derivatives/README|07 Volatility and Derivatives]]
- **Related:** [[02 - Trading Methodologies/12 Cross Asset and Macro/README|12 Cross Asset and Macro]]

## What this paper does NOT show
- That the reported pattern still exists after 2025-2026, under your broker/exchange, or with your current dataset.
- That reported prediction metrics or theoretical existence are the same as causal, executable after-cost trading alpha.
- That paper parameters may be retuned on a test set and still called independent out-of-sample validation.

## Next action
Retrieve and audit the full published paper or author manuscript before freezing an executable reproduction spec. No backtest performed.
