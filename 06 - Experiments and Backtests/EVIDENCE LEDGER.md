---
type: scientific_evidence_ledger
status: "active-executed-synthetic-evidence"
updated_on: 2026-10-13
---
# Evidence Ledger — Algo Brain

This ledger is **manually maintained in GitHub commits**, not automatically synchronized with Veron or LSE. An execution claim requires actual tool evidence.

| Experiment | Track | Spec / observable | Current state | Evidence | Scientific verdict |
|---|---|---|---|---|---|
| [[06 - Experiments and Backtests/EXP-F001 - Permutation Entropy Data and Method Audit|EXP-F001]] | primary-source mathematics and empirical GC audit | Bandt–Pompe method, GC.F 5m file preview | Core mathematical text reviewed; original PDF visual verification and raw data unavailable | [[03 - Mathematical Foundations/PAPER-090 - Permutation Entropy Primary Text Audit|Math note]] · [[04 - Market Data/DATA-F001 - Gold GC 5m Intake Checklist|Data gate]] | **BLOCKED** for market-data analysis |
| [[06 - Experiments and Backtests/EXP-S001 - Permutation Entropy Synthetic Invariants|EXP-S001]] | synthetic mathematics | Author toy counts, monotonic, periodic, Gaussian IID and tied inputs | **EXECUTED in OpenAI Python3 sandbox; 6/6 assertions passed** | [[06 - Experiments and Backtests/EXP-S001 - Execution Evidence|Executed evidence]]; [[06 - Experiments and Backtests/EXP-S001.py|exact Python source]]; [[06 - Experiments and Backtests/EXP-S001-results.json|raw JSON]] | **PASS — numerical invariants only** |

## Evidence quality policy
- **Theory proven / method checked** is not **empirical market predictability**.
- **Synthetic oracle PASS** establishes only numerical correctness under stated tests.
- **Observed real-market significance** still requires a frozen sample, null and uncertainty estimate.
- **Profitable backtest** (if ever relevant) needs independent evidence and fills/costs.
- Include negative findings, contradictions and BLOCKED results here; do not turn an untested paper combination into a "validated" model.
- Results must link exact source code/version/hash, command, environment, original output, numerical checks and immutable experiment ID.
- Never silently rewrite a failure or the preregistered threshold. Amend with a new ID if needed.

[[09 - Research Infrastructure/RESEARCH DIRECTOR|Research Director]] · [[Templates/Research Evidence Record Template|Evidence Template]]

## EXP-S001 scientific conclusion — recorded after execution
- Frozen spec commit: e20e7b65adaca1f0c73781bcebec3750023a3439; no numeric threshold was changed post hoc.
- Executed 6/6 assertions (two paper examples plus four synthetic controls). IID Gaussian normalized entropy = **0.9999421146838567**, passing the preregistered 0.995 lower bound. Monotone/constant = 0, three-cycle = log2(3).
- Assistant sandbox, **not** Veron or LSE; Python 3.13.5, standard library only, synthetic seed 20261013, N=30,002.
- [[06 - Experiments and Backtests/EXP-S001 - Execution Evidence|Execution evidence and limitations]]. No market data, forecasts, Sharpe, alpha or strategy implication established. EXP-F001 remains BLOCKED.
