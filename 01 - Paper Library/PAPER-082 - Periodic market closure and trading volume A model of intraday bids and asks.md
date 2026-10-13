---
type: paper
paper_id: PAPER-082
status: primary-source-abstract-screened
category: "11 Intraday Price Structure"
year: 1992
reviewed_on: 2026-10-13
doi: "10.1016/0165-1889(92)90045-G"
source_url: "https://doi.org/10.1016/0165-1889(92)90045-G"
replicated: false
---
# PAPER-082 — Periodic market closure and trading volume: A model of intraday bids and asks

**Authors:** William A. Brock; Allan W. Kleidon  
**Publication:** Journal of Economic Dynamics and Control 16(3–4), 451–489 (1992)  
**Primary research source:** https://doi.org/10.1016/0165-1889(92)90045-G
**DOI:** https://doi.org/10.1016/0165-1889(92)90045-G

> **Evidence classification: peer-reviewed publication or conference source record and abstract reviewed, not a full-text audit.** These are summaries of the authors' claims and contributions, not strategy endorsements. No new executable strategy, live results or independently verified historical returns.

## Mechanism / mathematical idea
Models why opening and closing market periods attract concentrated trading demand and less elastic liquidity supply, affecting quotes/spreads.

## Author-reported finding or theoretical scope
Theoretical predictions of distinctive open/close demand, volume and trading costs, consistent with historical evidence.

## Required data / feasibility gate
Clock-aligned regular-session bars and quotes, spread and volume records, auction windows, timezone/DST and half-day schedules.

## Critique / potential failure
High volume at open/close does not imply directional predictability, and old specialist market mechanics differ from electronic markets.

## Falsifiable follow-up (proposal only)
Check whether pre-defined time-of-day liquidity metrics forecast execution cost and range expansion in SPY/ES without using today's future volume.

## Exact next validation sequence (not executed)
1. Obtain full published paper; preserve version and check formula definitions, all timing and data sources.
2. Preview raw dataset, chronological coverage, missing bars, corporate actions and event timestamps **before** proposing implementation.
3. Freeze the experiment objective, baselines, constraints, sample and metrics before writing any backtest.
4. Enforce causality, next-tradable fills, funding, spread, slippage/impact, margin and walk-forward selection.
5. Save executed code and metrics; preserve negative outcomes. Do not promote findings without independent OOS evidence.

## Knowledge graph
- [[02 - Trading Methodologies/11 Intraday Price Structure/README|Intraday Price Structure]]
- [[01 - Paper Library/RESEARCH CATALOG|Research Catalog]]
