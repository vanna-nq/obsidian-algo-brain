---
type: data_audit
data_audit_id: "DATA-F001"
status: "BLOCKED_RAW_DATA_NOT_AVAILABLE"
dataset_symbol: "GC.F"
timeframe: "5m"
sha256: null
row_count_verified: null
dataset_preview_executed: false
---
# DATA-F001 — GC.F 5-minute futures: intake and quality gate

## What is actually known
- Earlier project discussions reported approximately **122,359** 5-minute gold-futures bars from **2025-01-01 through 2026-09-26**.
- These are *historical user/project statements*, **NOT** a dataset read this session. Do not treat the reported rows and dates as a validated file manifest.
- A search of available Project/Library materials found text notes and old LSE/Veron audit descriptions, not a mountable original GC.F 5m OHLCV file.
- The research GitHub vault contains Markdown paper and experiment notes but no confirmed licensed 5m GC.F raw dataset.
- This assistant cannot access `/home/oliverh` on the user's Linux computer from the GitHub connection. No local file preview or SHA was executed.

## Required inputs from user / actual verified terminal
- **Preferred:** attach original GC.F 5m CSV or Parquet to conversation or provide an accessible Project file.
- **Alternative:** using the local, actually authenticated research terminal, show a verified data-preview report, not merely a claimed row count.
- Avoid uploading keys, tokens, private OAuth settings, or unrelated raw data. Do not upload licensed data into a public repo.

## Mandatory preview fields
1. Exact source provider, dataset ID, exchange symbol(s), continuous futures adjustment/roll convention and entitlement.
2. Original filename/path and SHA-256, row count, column names and types, 10 initial and 10 final rows.
3. First/last UTC timestamps with original timezone, timestamp semantics **bar-open vs bar-close**, daylight-saving and exchange holiday/session rules.
4. Strict timestamp ordering, duplicates, missing expected 5-minute bars vs ordinary non-trading hours, interior gaps, non-positive prices, OHLC order violations and zero/missing volume.
5. Contract roll schedule and examples around roll discontinuities; quote units and price tick size.
6. Count zero log returns and equal observations in length-3 triples to establish tie policy, plus observed session/roll boundaries.
7. A machine-readable manifest documenting all counts and exceptions, produced directly from data, not invented from historical narrative.

## Gate
**BLOCKED.** No file hash, actual bar preview, timestamp/gap/roll verification or tie frequency has been obtained. Do not claim the 122,359 rows as observed. No predictive/backtest code is authorized by this audit.

When supplied, update status to `PREVIEWED`, attach true checksum/anomaly evidence, and request explicit approval before a separate frozen forecasting experiment.

Links: [[06 - Experiments and Backtests/EXP-F001 - Permutation Entropy Data and Method Audit|EXP-F001]] · [[03 - Mathematical Foundations/PAPER-090 - Permutation Entropy Primary Text Audit|Mathematical audit]].
