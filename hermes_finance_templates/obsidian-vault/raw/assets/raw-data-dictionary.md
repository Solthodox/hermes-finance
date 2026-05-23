---
id: raw-data-dictionary
title: Raw Data Dictionary
type: raw-source
tags: [llmwiki, dataset, research, source-quality]
status: seed
created: 2026-05-23
updated: 2026-05-23
source_quality: seed-synthesis
---

# Raw Data Dictionary

This page describes non-Markdown sample data stored under `raw/api-dumps/` and `raw/assets/`. These files are seed fixtures for Hermes Finance ingestion, not live balances or private history.

## Files

- `raw/api-dumps/coingecko-mcp-market-snapshot.example.json` — expected shape for a CoinGecko market snapshot used by [[market-research-dataset]].
- `raw/api-dumps/alphavantage-daily-adjusted.example.json` — expected shape for an Alpha Vantage equity time-series response used by [[market-research-dataset]].
- `raw/api-dumps/polymarket-clob-trades.example.json` — synthetic trade-history fixture for testing [[clob-trade-netting]].
- `raw/api-dumps/hyperliquid-clearinghouse-state.example.json` — synthetic account-state fixture for [[hyperliquid-account-architecture]].
- `raw/assets/trade-journal.seed.csv` — empty/safe CSV header plus one fake example row for [[trade-journal-dataset]].
- `raw/assets/prediction-calibration.seed.csv` — fake probability/outcome rows for [[prediction-calibration-dataset]].

## Rules

- Do not put secrets, private keys, wallet balances, or live positions in seed data.
- Mark synthetic fixtures explicitly with `fixture: true` or equivalent.
- Raw files should be immutable after ingestion. If a source changes, add a new dated capture instead of overwriting old evidence.

Related: [[ingestion-playbook]], [[lint-checklist]], [[source-quality]].
