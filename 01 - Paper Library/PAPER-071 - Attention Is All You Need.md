---
type: paper
paper_id: PAPER-071
status: primary-source-abstract-screened
category: "05 Deep Learning"
year: 2017
reviewed_on: 2026-10-13
source_url: "https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html"
replicated: false
---
# PAPER-071 — Attention Is All You Need

**Authors:** Ashish Vaswani; Noam Shazeer; Niki Parmar; Jakob Uszkoreit; Llion Jones; Aidan N. Gomez; Łukasz Kaiser; Illia Polosukhin  
**Publication:** Advances in Neural Information Processing Systems 30 (2017)  
**Primary research source:** https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Introduces transformer self-attention for sequence-to-sequence modelling without recurrent/convolutional sequence encoders.

## Author-reported finding or theoretical scope
Neural sequence modeling breakthrough demonstrated on machine translation, not a test of equity or futures alpha.

## Required data / feasibility gate
Lagged sequence features, causal attention mask, time-indexed targets, compute controls and finance-specific benchmark datasets.

## Critique / potential failure
Original encoder-decoder and bidirectional attention are not necessarily causal for forecasting; price targets must be masked against future observation.

## Falsifiable follow-up (proposal only)
Test a small causal transformer against LSTM and ridge on identical future return targets, with embargo for overlapping labels and net-utility evaluation.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/05 Deep Learning/README|Deep Learning]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
