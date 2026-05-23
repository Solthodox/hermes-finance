---
id: log
title: Hermes Finance Vault Log
type: log
tags: [llmwiki, obsidian, research]
status: active
created: 2026-05-20
updated: 2026-05-23
source_quality: seed-synthesis
---

# Hermes Finance Vault Log

Append-only operational history for the vault.

## 2026-05-20

- Initialized Hermes-Finance LLMWiki vault with `SCHEMA.md`, `index.md`, this log, raw directories, and 112 seed knowledge pages.
- Seed sources: Karpathy LLMWiki standard, Hermes Finance plan, existing local Hermes finance/trading skills, and public MCP documentation for CoinGecko, Alpha Vantage, Exa, Firecrawl, Polymarket, Hyperliquid, Alpaca, and Obsidian.
- Credential policy: no secrets in vault; credentials live only in `{{HERMES_FINANCE_HOME}}/.env` when manually added.
- Added a quant/trading knowledge pack with 8 dense notes: [[bayesian-updating-for-trade-theses]], [[mean-reversion-cointegration-and-spreads]], [[time-series-momentum-and-trend-following]], [[limit-order-book-microstructure]], [[backtesting-overfitting-and-research-hygiene]], [[robust-portfolio-construction]], [[volatility-forecasting-and-regime-detection]], and [[optimal-execution-and-slippage]]. Expanded core notes including [[fractional-kelly]], [[claim-evidence-probability-ev]], [[prediction-market-calibration]], and [[liquidity-and-slippage]] with formulas, operating rules, and paper references.

## 2026-05-23

- Filled raw vault seed material: [[market-data-mcp-source-cards]], [[trading-venue-api-source-cards]], [[position-sizing-and-portfolio-theory-source-cards]], [[market-microstructure-and-execution-source-cards]], and [[raw-data-dictionary]].
- Added synthetic, non-secret fixtures under `raw/api-dumps/` for CoinGecko, Alpha Vantage, Polymarket CLOB trade netting, and Hyperliquid account-state shape checks.
- Added synthetic CSV fixtures under `raw/assets/` for trade-journal and prediction-calibration ingestion tests. All fixture rows are fake examples, not live positions or private history.

Related: [[index]], [[SCHEMA]], [[llmwiki-standard]].
