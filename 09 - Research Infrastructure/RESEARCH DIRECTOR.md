---
type: research_director
status: "active-manually-operated"
papers: 104
mechanism_families: 16
hypotheses: 15
---
# Research Director

**Purpose:** Coordinate theory, controlled synthetic studies and real-market research; prevent the 104-paper library from becoming disconnected summaries. The Director is an Obsidian workflow, NOT a live autonomous agent.

## Currently approved scientific program

| Task | Track | State | Next allowable action |
|---|---|---|---|
| [[06 - Experiments and Backtests/EXP-S001 - Permutation Entropy Synthetic Invariants|EXP-S001]] | synthetic mathematics | FROZEN, pending execution | Run its five preregistered unit tests, capture raw output and hashes; stop |
| [[06 - Experiments and Backtests/EXP-F001 - Permutation Entropy Data and Method Audit|EXP-F001]] | GC.F empirical | BLOCKED, no raw bar preview | Obtain a verified LSE/Veron 5m data preview, roll calendar and source fingerprint |
| [[05 - Strategy Hypotheses/HYP-F002 - Roughness of Volatility|HYP-F002]] | mathematical | PROPOSED | Wait until the current test is recorded |
| [[05 - Strategy Hypotheses/HYP-F003 - Intraday Extremum Hazard and Seasonality|HYP-F003]] | empirical | PROPOSED | Wait; first verify sessions, bar labeling and causal extremes |

A blocked *empirical* task does not block an independent synthetic mathematics unit test; it also does not count as passed.

## Decision procedure
1. Consult [[06 - Experiments and Backtests/EVIDENCE LEDGER|Evidence Ledger]] for prior positives, negatives and blocked requirements.
2. Retrieve canonical source papers from [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]] and mathematical relationships from [[03 - Mathematical Foundations/KNOWLEDGE GRAPH|Knowledge Graph]]. Link exact definitions, not loose analogies.
3. Choose exactly **one** falsifiable task with observable, expected result, null or oracle, failure rule and stop condition.
4. Freeze research spec *before* coding or running. For market studies, preview exact real dataset first. For synthetic studies, freeze generator, N, seed, first-value preview and oracle expectations.
5. Execute within a **verified** environment. Record actual outputs and tool evidence, including negative results. No fabricated file hashes or unexecuted metrics.
6. Append an evidence ledger entry and update the task status. New variants after execution require a new experiment ID.
7. Only then pick the next task based on scientific information gained, mathematical novelty, data feasibility, falsifiability and unresolved risks—not promised profitability.

## Research tracks
- **Theoretical:** theorem, derivation, counterexample and exactly stated assumptions.
- **Synthetic:** simulation or computational invariant against a known oracle. Passing this does not imply market predictability.
- **Empirical:** real exchange/source data, timestamp and adjustment audit, causal model tests against controls.
- **Trading applications (optional):** costs, fills and risk only when the research objective genuinely requires them.

## Research environments
- **Veron:** one verifiable request at a time, using only functions actually in its tool contract. Don't assume agent-only Python, file-write, LSE-import or blueprint tools.
- **LSE Terminal:** historic datasets, verified previews, licensed exports and provenance where its current functions support them.
- **Python sandbox/local Jupyter:** reproducible synthetic mathematics or offline analysis; mark such execution as neither Veron nor LSE.
- **GitHub/Obsidian:** durable hypotheses, source citations, scripts, summaries, decision history and evidence ledger. No private tokens, licensed raw data or local Obsidian plugin auth in the repo.

## Navigation
[[05 - Strategy Hypotheses/RESEARCH INTELLIGENCE INDEX|Research Intelligence Index]] · [[06 - Experiments and Backtests/EVIDENCE LEDGER|Evidence Ledger]] · [[09 - Research Infrastructure/RESEARCH EXECUTION CONTRACT|Execution Contract]]
