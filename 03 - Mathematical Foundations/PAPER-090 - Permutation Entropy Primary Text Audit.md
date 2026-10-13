---
type: source_method_audit
paper_id: "PAPER-090"
experiment_id: "EXP-F001"
status: "primary-article-math-checked-pdf-visual-not-verified"
audited_on: 2026-10-13
predictive_model_executed: false
---
# PAPER-090 — Permutation Entropy: mathematical method audit

## Evidence and provenance
- Publisher metadata: https://doi.org/10.1103/PhysRevLett.88.174102, *Physical Review Letters* 88, 174102 (2002), Christoph Bandt and Bernd Pompe.
- Core section II definitions checked against the **publisher-article text reproduced in a publicly visible author-uploaded full-text transcription**: https://www.researchgate.net/publication/11364831_Permutation_Entropy_A_Natural_Complexity_Measure_for_Time_Series (published article printed pp. 174102-1 to 174102-4, especially pp. 174102-1 and 174102-2).
- A distinct author's Dec 17 2001 manuscript has also been located at https://edocs.tib.eu/files/e01fn13/733610978.pdf, but PDF bytes and visual equations could not be reliably inspected in this session; the arXiv address **cond-mat/0109023 is NOT this paper** and must never be used as its source.
- **Status nuance:** Core mathematical definitions confirmed from reproduced article text, but do **not** claim a PDF page-render/verbatim notation audit or an independent implementation check. All gold-market applications below are our ideas, not Bandt–Pompe results.

## Paper's exact mathematical construction (section II; typeset for clarity)
Let a time series have N observations `x_1,...,x_N`. For a fixed embedding order `m>=2`, each contiguous vector `(x_i,...,x_{i+m-1})` maps to the permutation of time indices that sorts its values from low to high. Assuming no equal-valued observations, there are `m!` possible patterns `pi`.

For each pattern:
```text
p(pi) = count of contiguous length-m windows whose ordinal type is pi / (N-m+1)
H(m)  = - sum over all pi [p(pi) * log_2 p(pi)]      [0 log 0 := 0]
0 <= H(m) <= log_2(m!)
h_m   = H(m) / (m-1)  [the paper's per-symbol quantity]
```
For display, the published article also reports a **different normalization**, `H(m)/log_2(m!)`, ranging from 0 to 1. Do **not** confuse these two quantities. Fix one convention for the proposed forecasting feature and document it.

The authors illustrate `m=2` with counts (4,2) in six adjacent pairs of (4,7,9,10,6,11,3), giving H(2) approximately **0.918 bits**; for `m=3`, they report H(3) approximately **1.522 bits** from pattern counts 2,2,1 across five triples. This is a source-text example, **not** a calculation on GC.F.

Authors suggest practical dimensions roughly **m=3 through 7** for their experiments. Their patterns use *neighboring values* (effectively delay 1); larger delay is a generalization, not needed for the proposed first test. The original paper studies deterministic dynamical examples and speech, **not forecasting gold volatility**.

## Tie handling — unresolved on real data
- Section II explicitly assumes equal values are rare and suggests small random perturbations to break ties when necessary.
- GC price levels and especially GC discrete/tick-size-constrained returns can produce equal values and zero returns. Actual tie rate cannot be known until market-data preview.
- Random jitter would introduce seed/scale sensitivity; stable chronological-index tie-breaks are reproducible but **a methodological adaptation**, not identical to the author's proposed perturbation.
- Do not select a tie convention by which variant predicts best. First count ties and decide protocol on training data before forecast scoring, then assess tie-sensitivity in a **preregistered** robustness check.

## Proposed HYP-F001 specification is an adaptation
- Bandt–Pompe introduces ordinal entropy on raw observed sequences; using **log returns rather than price levels** is a deliberate change of input variables. Monotonic-transform invariance of price levels does **not** imply that transforming price to returns preserves ordinal patterns.
- Proposed market feature, not paper result: 120 completed 5m returns, m=3 and lag 1, giving **118** overlapping ordinal windows and **six** possible types if no data gaps.
- Use normalized `H(3)/log_2(6)` as the *proposed* feature, with the chosen ties and missing-gap treatment documented. This was not prescribed in the original paper.
- Prospective target is next 12-bar realized log-return variance. Forecast target, model class, split, session segmentation, minimum effect and baselines remain **unfrozen** pending real GC dataset inspection.
- A good empirical entropy estimate is NOT the same as information about the *future*, nor evidence of net trading performance.

## Mathematical and causal controls for next stage
1. No entropy window can cross an unexplained missing-bar interval or discontinuous contract roll unless a fully documented adjustment makes it valid.
2. Each entropy value stamped at time t must use 120 completed historical returns through t, not bars that close after the decision time.
3. The 120-return window contains 118 highly overlapping triples; estimates and out-of-sample losses are serially dependent. Use appropriate blocked inference.
4. Each predicted RV target must be strictly after the feature timestamp. A 12-bar forward target requires purge/embargo around train/test boundaries.
5. For zero realized variance, the proposed QLIKE expression using `log(y/f)` is undefined. Freeze an explicit zero-target policy before evaluating any predictions.
6. Finance-focused claims require an independent chronological holdout, strong HAR/EWMA/time-of-day comparators, and a *separate* after-cost executable strategy evaluation.

## Source audit verdict
**CORE_METHOD_REVIEWED_FROM_REPRODUCED_PRIMARY_TEXT; PDF_VISUAL_NOT_CONFIRMED.** Sufficient to specify the concept, **not** sufficient to call an exact original-paper replication or to start model testing without an actual dataset preview.

Links: [[06 - Experiments and Backtests/EXP-F001 - Permutation Entropy Data and Method Audit|EXP-F001]] · [[04 - Market Data/DATA-F001 - Gold GC 5m Intake Checklist|Gold dataset intake]].
