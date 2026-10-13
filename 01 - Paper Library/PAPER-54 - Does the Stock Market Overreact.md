---
type: paper
paper_id: PAPER-54
status: publisher-abstract-verified-not-fulltext-audited
reviewed_on: 2026-10-13
primary_methodology: "09 Mean Reversion"
year: 1985
doi: "10.1111/j.1540-6261.1985.tb05004.x"
source_url: "https://doi.org/10.1111/j.1540-6261.1985.tb05004.x"
replicated: false
---
# PAPER-54 — Does the Stock Market Overreact?

**Authors:** Werner F. M. De Bondt; Richard Thaler  
**Venue/year:** The Journal of Finance 40(3), 793–805 (1985)  
**Verified primary source:** https://doi.org/10.1111/j.1540-6261.1985.tb05004.x  
**DOI:** https://doi.org/10.1111/j.1540-6261.1985.tb05004.x

> **Evidence status: Source-verified literature screen, NOT a full-paper methods audit, executable ruleset, or independent replication.** The publisher/author abstract and bibliographic record support the claim below. Obtain and audit the full article before translating details to code.

## What this paper contributes
Tests whether extreme historical loser portfolios subsequently outperform winners over multi-year horizons, consistent with investor overreaction.

## Grounded finding / scope (authors, not our result)
Historical US monthly-return sample exhibits long-horizon reversal patterns and especially strong January outcomes for old losers; it does NOT test short-lived intraday mean reversion.

## Required data and feasible replication
CRSP-style survivorship-safe long stock history, delistings, market caps, monthly rebalancing, robust size/value factor comparisons.

## Challenges, alternatives and invalid inference
Size, liquidity, tax/calendar effects and distressed-stock exposures can mimic mispricing; translating years-long reversal to 2-minute charts is unjustified.

## Candidate falsifiable experiment — proposed only
Precommit prior 3-year loser/winner ranking and next 3-year return windows, report post-1985 subperiods, factors, costs, tail exposure and calendar robustness.

**Mandatory validation gates:** source-version check → dataset preview/coverage → timestamp/corporate-action audit → frozen objective and null → train-only estimation → strictly causal next-tradable fills → all-in transaction/friction costs → independent forward holdout → sensitivity and regime breakdown. No results produced here.

## Knowledge graph
- **Primary methodology:** [[02 - Trading Methodologies/09 Mean Reversion/README|Mean Reversion]]
- **Research index:** [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
- **Status:** PAPER SOURCE ONLY; do not promote to Validated Models.
