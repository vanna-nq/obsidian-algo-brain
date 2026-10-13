---
type: paper
paper_id: PAPER-002
status: abstract-screened-not-replicated
primary_methodology: "01 Statistical Arbitrage"
year: 2006
doi: "10.1093/rfs/hhj020"
source_url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1095996"
review_date: 2026-10-13
---
# PAPER-002 — Pairs Trading: Performance of a Relative-Value Arbitrage Rule

**Authors:** Evan Gatev; William N. Goetzmann; K. Geert Rouwenhorst  
**Publication:** Review of Financial Studies 19(3), 797-827 (2006)  
**DOI:** https://doi.org/10.1093/rfs/hhj020  
**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1095996  
**Evidence access:** Empirical peer-reviewed, SSRN abstract and publication metadata reviewed.

> **Research status: AUTHOR CLAIMS / THEORY ONLY.** Source metadata and abstract or author materials reviewed. No independent implementation, full-paper equation audit, dataset verification, or backtest was executed for this note. If replicating, obtain the full version of record and verify all detailed rules against it.

## Economic / mathematical mechanism
Select stock pairs by small distance between historically normalized price paths; enter a relative-value trade when their spread separates and close when convergence occurs. Mispricing of close substitutes is the proposed source of return.

## What the authors report (NOT our results)
Using US stock histories, the authors report average annualized excess returns up to ~11% for self-financing pairs in their historical sample, and bootstrap evidence that the effect differs from simple short-term reversal. This is a historical author result, not a return expectation.

## Data and implementation requirements
Daily total-return-adjusted equities, delisting-aware universe, pairs formation window, tradable short leg, borrow/commissions and market-impact data; matched formation/trading periods.

## Limitations and replication hazards
Pair relationships may disintegrate; pair formation and survival bias, short borrow and hard-to-borrow exposure, correlated portfolio tail events, stale prices and execution costs may erase apparent convergence profits.

## Candidate falsifiable hypothesis (our proposal, UNTESTED)
On a held-out universe and recent sample, pairs selected via formation-period price-distance show post-cost positive spread reversion beyond a sector-neutral placebo.

## Proposed validation / first test (NOT executed)
Pre-register pair selection and entry/exit z-thresholds; trade at next tradable timestamp; chronological out-of-sample evaluation, delisting and corporate-action handling, pair-overlap and funding constraints.

## Knowledge graph
- **Primary:** [[02 - Trading Methodologies/01 Statistical Arbitrage/README|01 Statistical Arbitrage]]
- **Related:** [[02 - Trading Methodologies/09 Mean Reversion/README|09 Mean Reversion]]
- **Related:** [[02 - Trading Methodologies/12 Cross Asset and Macro/README|12 Cross Asset and Macro]]

## What this paper does NOT show
- That the reported pattern still exists after 2025-2026, under your broker/exchange, or with your current dataset.
- That reported prediction metrics or theoretical existence are the same as causal, executable after-cost trading alpha.
- That paper parameters may be retuned on a test set and still called independent out-of-sample validation.

## Next action
Retrieve and audit the full published paper or author manuscript before freezing an executable reproduction spec. No backtest performed.
