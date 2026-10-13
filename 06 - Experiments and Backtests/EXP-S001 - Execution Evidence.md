---
type: research_evidence
experiment_id: "EXP-S001"
track: "synthetic-mathematics"
status: "PASS-NUMERICAL-INVARIANTS-ONLY"
spec_commit_sha: "e20e7b65adaca1f0c73781bcebec3750023a3439"
source_sha256: "f536590f555505e9a4bb7a624933ed5f5b096f97f3f196f0af727a8a823bd7bf"
results_sha256: "29c44ed4fa362b45f14e1379435707cf69d01a031f89ca879d887fa22f2b50f5"
seed: 20261013
sample_length: 30002
execution_environment: "OpenAI assistant isolated Linux container, NOT Veron and NOT LSE"
backtest_executed: false
---
# EXP-S001 — Actual Execution Evidence

**Scope:** Numerical correctness of ordinal-pattern entropy for author hand-counted samples and fixed synthetic processes. Frozen protocol [[06 - Experiments and Backtests/EXP-S001 - Permutation Entropy Synthetic Invariants|EXP-S001]]. Frozen spec GitHub commit e20e7b65adaca1f0c73781bcebec3750023a3439 **preceded execution**. No empirical dataset accessed, no fitted forecast, no trading system or profitability claim.

## Reproducibility / artifacts
- [[06 - Experiments and Backtests/EXP-S001.py|Python 3 source]] — **exact bytes compared to executed source Git blob** SHA-1 470fcff3d914a1edf3c11b664ceabce2e91084cd.
- [[06 - Experiments and Backtests/EXP-S001-results.json|Original executed JSON results]] — **exact bytes compared to executed output Git blob** SHA-1 40cb8a56b49505934350d5d27c674d2fe43b344f.
- SHA256 source: f536590f555505e9a4bb7a624933ed5f5b096f97f3f196f0af727a8a823bd7bf.
- SHA256 JSON: 29c44ed4fa362b45f14e1379435707cf69d01a031f89ca879d887fa22f2b50f5.
- **Runtime:** Python 3.13.5, Linux x86_64, standard library, fixed random.Random(20261013), 30,002 observations (30,000 m=3 windows).
- **Exact replay:** download source to an empty directory, run command `python3 EXP-S001.py` (writes `EXP-S001-results.json`).
- The real run was performed in an **OpenAI isolated Linux container**; no Veron or LSE Terminal function was invoked.

## Actual recorded output

| Check (all predefined) | Observed H in bits | Expected oracle or threshold | Result |
|---|---:|---|---|
| Paper toy sequence m=2 | 0.9182958340544896 | binary entropy from counts [4,2] | PASS |
| Paper toy sequence m=3 | 1.5219280948873621 | entropy from counts [2,2,1] | PASS |
| Strict monotone N=30,002 | 0.0 | exactly 0 | PASS |
| Period-3 [0,2,1] N=30,002 | 1.584962500721156 | log2(3) and [10000,10000,10000] | PASS |
| IID Gaussian N=30,002 | 2.5848128693495833 | normalized H >= 0.995, six patterns, no ties | PASS (normalized = 0.9999421146838567) |
| All zero N=30,002 | 0.0 | exactly 0 under stable chronological tie order | PASS |

The Gaussian ordinal counts were [5036,4930,4929,5087,5087,4931] in fixed lexicographic order of the six permutation patterns; all 30,000 windows accounted for. All-tie input recorded 30,000 tied windows, demonstrating this is an explicit policy choice, not an original-paper replication.

## Scientific verdict
**PASS — synthetic numerical invariants.** Six assertions satisfied the original, pre-execution thresholds. **No evidence** that permutation entropy predicts volatility, that market data follow any specific physical model, or that any strategy is profitable. The original paper's full publisher PDF visual audit remains unconfirmed; the source's printed examples/math were previously checked from reproduced article text.

## Technical caveat
The executed Python source redundantly constructs and discards one IID Gaussian array (resetting the seed on each draw) before generating the actual **correct stateful** seeded array used in the assertion. This does not alter the recorded input or result, but wastes CPU. The original executed script is preserved unchanged for exact replay; a refactor, if wanted, requires a new version and evidence.

## Explicit stop and next step
**STOP EXP-S001.** Do not add other parameter searches or controls under the same experiment ID. The empirical [[06 - Experiments and Backtests/EXP-F001 - Permutation Entropy Data and Method Audit|EXP-F001]] remains BLOCKED pending true GC.F 5m dataset preview. A separate Veron execution of numerical mechanics may be designed only after confirming its actual callable functions and freezing a new task.

[[06 - Experiments and Backtests/EVIDENCE LEDGER|Evidence Ledger]] · [[09 - Research Infrastructure/RESEARCH DIRECTOR|Research Director]]
