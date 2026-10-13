---
type: experiment
experiment_id: "EXP-S001"
track: "synthetic-mathematics"
status: "FROZEN-NOT-EXECUTED"
seed: 20261013
sample_length: 30002
embedding_dimension: 3
delay: 1
---
# EXP-S001 — Permutation Entropy Synthetic Invariants

## Objective
Verify a deterministic implementation of permutation entropy with *known synthetic oracles*, before using the feature for market research. This is **not** a Veron backtest, not an empirical financial claim, and not an alpha test.

Sources: [[01 - Paper Library/PAPER-090 - Permutation Entropy A Natural Complexity Measure for Time Series|PAPER-090]] and [[03 - Mathematical Foundations/PAPER-090 - Permutation Entropy Primary Text Audit|mathematical audit]].

## Frozen calculation
For every overlapping length-m consecutive sequence, sort indices by increasing sample value. Ties are broken by the *earlier time index* as an explicitly disclosed deterministic **adaptation** (the published article suggests perturbing ties). Count ordinal types, divide by N-m+1; Shannon entropy in bits is minus the sum of p*log2(p), and display-normalized value equals H/log2(m!). Set m=3, delay=1 except the paper's m=2 toy check.

## Five frozen controls
1. **Paper example** [4,7,9,10,6,11,3]: at m=2 nonzero permutation counts are 4,2 and entropy is the binary entropy of (4/6,2/6). At m=3 nonzero counts are 2,2,1 and entropy is the Shannon entropy of (2/5,2/5,1/5). Exact count multisets required.
2. **Increasing integers:** N=30,002, x_i=i: H3 exactly 0.
3. **Three-cycle:** N=30,002, repeated [0,2,1] (all triples have three distinct values): 30,000 windows, 10,000 each of three permutation types, H3=log2(3) bits, H3/log2(6)=log2(3)/log2(6).
4. **Gaussian IID:** N=30,002, Python standard-library random.Random(20261013).gauss(0,1): normalized H3 >=0.995 with six nonzero pattern types, zero exact-valued ties.
5. **Constant series:** N=30,002, all zeros: stable chronological tie ordering yields H3 exactly 0 (implementation convention only).

## Frozen success and stop
The exact-count controls must match; each analytical H oracle within absolute 1e-12; the seeded IID condition above must pass. If any assertion fails, record FAIL and STOP, do not change parameters. If all pass, mark **PASS (synthetic numerical correctness only)**. Stop after these checks—no market-price simulation or forecasts in this experiment.

## Reproducibility requirements
Python3 standard library only; preserve source file, SHA256, exact run command, Python version, synthetic first 12 values, ordinal counts, entropy/normalized entropy, each test verdict, and output JSON with SHA. A result in an assistant sandbox must be explicitly named **assistant sandbox, NOT Veron or LSE**. Frozen spec committed before any execution.

[[06 - Experiments and Backtests/EVIDENCE LEDGER|Evidence Ledger]] · [[09 - Research Infrastructure/RESEARCH DIRECTOR|Research Director]]
