---
type: paper
paper_id: PAPER-013
status: abstract-screened-not-replicated
primary_methodology: "12 Cross Asset and Macro"
year: 2013
doi: "10.1111/jofi.12021"
source_url: "https://doi.org/10.1111/jofi.12021"
review_date: 2026-10-13
---
# PAPER-013 — Value and Momentum Everywhere

**Authors:** Clifford S. Asness; Tobias J. Moskowitz; Lasse Heje Pedersen  
**Publication:** The Journal of Finance 68(3), 929-985 (2013)  
**DOI:** https://doi.org/10.1111/jofi.12021  
**Source:** https://doi.org/10.1111/jofi.12021  
**Evidence access:** Empirical peer-reviewed, publisher abstract reviewed.

> **Research status: AUTHOR CLAIMS / THEORY ONLY.** Source metadata and abstract or author materials reviewed. No independent implementation, full-paper equation audit, dataset verification, or backtest was executed for this note. If replicating, obtain the full version of record and verify all detailed rules against it.

## Economic / mathematical mechanism
Value and momentum factor returns occur across asset classes and share cross-market components; combining historically negatively correlated value and momentum exposures may diversify factor risk.

## What the authors report (NOT our results)
The authors report value and momentum premia across eight markets/asset classes, greater cross-asset correlation of strategy returns than of passive asset returns, and negative association between value and momentum; funding liquidity risk only partly explains this.

## Data and implementation requirements
Point-in-time value signals appropriate to each asset class, historical market/futures data with term structure, total returns, funding rates, hedging and benchmark factor data.

## Limitations and replication hazards
Portfolio factor definitions, funding constraints, factor crowding and global factor crashes make naive diversification assumptions fail. Strategies are generally slower-horizon and not HFT.

## Candidate falsifiable hypothesis (our proposal, UNTESTED)
A prespecified, risk-balanced cross-asset value-plus-momentum combination delivers better OOS diversification than either sleeve alone after financing and transaction costs.

## Proposed validation / first test (NOT executed)
Predefine equal-risk target, asset sleeves and rebalancing; rolling covariances fit on training only; stress funding shocks, carry exposure, and tail co-movements; compare to matched risk baseline.

## Knowledge graph
- **Primary:** [[02 - Trading Methodologies/12 Cross Asset and Macro/README|12 Cross Asset and Macro]]
- **Related:** [[02 - Trading Methodologies/02 Trend and Momentum/README|02 Trend and Momentum]]
- **Related:** [[02 - Trading Methodologies/10 Optimization and Physics/README|10 Optimization and Physics]]

## What this paper does NOT show
- That the reported pattern still exists after 2025-2026, under your broker/exchange, or with your current dataset.
- That reported prediction metrics or theoretical existence are the same as causal, executable after-cost trading alpha.
- That paper parameters may be retuned on a test set and still called independent out-of-sample validation.

## Next action
Retrieve and audit the full published paper or author manuscript before freezing an executable reproduction spec. No backtest performed.
