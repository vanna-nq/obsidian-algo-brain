---
type: paper
paper_id: PAPER-022
status: metadata-and-abstract-screened
reviewed_on: 2026-10-13
category: "05 Deep Learning"
year: 2019
doi: "10.1080/14697688.2019.1622295"
source_url: "https://doi.org/10.1080/14697688.2019.1622295"
independent_backtest: false
---
# PAPER-022 — Universal Features of Price Formation in Financial Markets: Perspectives from Deep Learning

**Authors:** Justin Sirignano; Rama Cont  
**Publication:** Quantitative Finance 19(9), 1449–1459 (2019)  
**Verified source:** https://doi.org/10.1080/14697688.2019.1622295  
**Evidence level:** Publication metadata and publisher / author abstract or accessible summary screened. Full-text derivations, exact formulas and study tables have **NOT** been independently audited here.

## Core contribution / mathematical mechanism
Learns a cross-asset statistical relation between order-flow history and direction of short-term stock price moves.

## Source-supported result or scope
Study finds stable out-of-sample directional accuracy across US stocks using billions of high-frequency quote/trade observations.

## Risks and limitations
Predictive accuracy is not net trading profitability; execution latency, unseen market conditions, data overlap and spread matter.

## Required data for replication
Billions of synchronized trade/quote records, venue timestamps, reliable bid/ask data and large model training resources.

## Falsifiable follow-up experiment (proposed only)
Evaluate one global model against per-symbol and simple OFI models using fresh temporal holdouts and executable fills.

## Methodology cross-link
- [[02 - Trading Methodologies/05 Deep Learning/README|Deep Learning]]

## Research discipline
- Claims above reflect literature, NOT replicated returns, verified strategy edges or successful live execution.
- Before implementation, read the full paper, identify exact sample/version and executable timestamp semantics, preregister the test, and preserve positive and negative findings.
- Any profitability claim must be assessed against spread, commissions, slippage, short costs, financing, data availability and strictly chronological holdouts.
