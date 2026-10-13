---
type: research_execution_contract
status: "operational"
---
# Research Execution Contract

**One verifiable experiment at a time.** Every task needs exact data/timeframe (or fully specified synthetic inputs), mathematical rationale, objective, comparator, frozen criteria, stop condition and recorded tool evidence.

**Real-market data gate:** Before code, inspect source, symbols, frequency, exact bars/dates/time zone, row counts, session/roll adjustments, gaps and SHA where available. Previous discussion is not a fresh dataset preview.

**Synthetic gate:** Freeze generator, sample length, PRNG seed, controls, known analytical invariants, tie handling and thresholds before execution. Preview deterministic generator setup before source execution. No claim about live markets follows from synthetic tests.

**Veron:** Only its audited callable functions. No assumed write_workspace_file, run_python, import_lse_data, build_ml_dataset, generate_ml_blueprint or run_ml_blueprint. Obtain actual receipts. Prior SPX500 1h walk-forward audit verified rolling/sliding train windows and independent fold accounting; do not generalize that implementation to other tools.

**LSE Terminal:** Use actual available market dataset previews and export capabilities; respect limits, entitlements and data licenses. GitHub connection does not expose the user's Linux filesystem.

**Distinct outcomes:** (a) numerical implementation correctness, (b) simulated dynamical behavior, (c) empirically supported market claim, and (d) viable after-cost trading result. Each needs its own evidence.

**Record every execution:** source and frozen-spec commit, exact Python command or Veron function, dependency/version, seed or data SHA, preview, observed metrics, uncertainty where relevant, failure cases, final verdict and next allowed action.

**Naming:** EXP-S for synthetic experiments; EXP-F for market/data experiments; HYP-F for hypotheses. One record per experiment in [[06 - Experiments and Backtests/EVIDENCE LEDGER|Evidence Ledger]]. Preserve rejected tests.
