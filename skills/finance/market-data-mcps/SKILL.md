---
name: market-data-mcps
description: Choose and operate configured market-data/research MCPs without leaking credentials or trusting stale data.
tags: [finance, market-data, mcp, research]
---

# Market Data MCPs

Configured in `{{HERMES_FINANCE_HOME}}/config.yaml`:

- `coingecko` and `finance_vault` are enabled by default.
- `firecrawl`, `exa`, `alphavantage`, `polymarket`, `hyperliquid`, `alpaca`, and `obsidian` are configured but disabled until credentials are filled in `{{HERMES_FINANCE_HOME}}/.env` and enabled explicitly.
  Use `{{HERMES_FINANCE_HOME}}/scripts/enable_ready_mcps.py --dry-run` to see what can be enabled, and run it without `--dry-run` for research/data MCPs after credentials are present. Trading MCPs require `--include-trading`.

## Tool choice

- Crypto spot/onchain metadata: CoinGecko / GeckoTerminal first, then DEX-specific APIs.
- TradFi market data: Alpha Vantage when enabled; Yahoo-style data only as a fallback.
- Web research: Exa for source discovery; Firecrawl for page extraction/deep research.
- Vault operations: filesystem vault access by default; Obsidian MCP only if Local REST API is deliberately enabled.

Never store API keys or private keys in Obsidian, chat notes, or decision records.
