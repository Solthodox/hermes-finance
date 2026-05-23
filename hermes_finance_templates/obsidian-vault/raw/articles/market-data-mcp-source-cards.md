---
id: market-data-mcp-source-cards
title: Market Data MCP Source Cards
type: raw-source
tags: [research, market-data, mcp, source-quality]
status: seed
created: 2026-05-23
updated: 2026-05-23
source_quality: primary-docs
---

# Market Data MCP Source Cards

Immutable seed capture for market-data MCP setup and safety. Use this as raw source context before updating [[coingecko-mcp]], [[alpha-vantage-mcp]], [[alphavantage-mcp-setup]], [[exa-mcp]], [[firecrawl-mcp]], and [[mcp-readiness-check]].

## CoinGecko MCP

Source URL: https://docs.coingecko.com/reference/mcp-server

Observed from official docs:
- Official CoinGecko MCP provides crypto price and market data for AI agents.
- Keyless remote server exists for quick tests and basic queries.
- Authenticated remote server and local server paths exist for Demo/Pro API keys.
- Local server uses `npx -y @coingecko/coingecko-mcp` with either `COINGECKO_DEMO_API_KEY` or `COINGECKO_PRO_API_KEY` plus `COINGECKO_ENVIRONMENT`.
- Public/keyless mode is useful for smoke tests but should not be assumed reliable for heavy production use.

Operational implication:
- Hermes Finance can enable CoinGecko by default for low-risk market-data checks.
- If rate limits matter, require explicit API key setup and mark output source/timestamp in downstream notes.

## Alpha Vantage MCP

Source URL: https://mcp.alphavantage.co/

Observed from official docs:
- Official Alpha Vantage MCP exposes stock and financial-market data through MCP.
- Remote endpoint format: `https://mcp.alphavantage.co/mcp?apikey=YOUR_API_KEY`.
- Local stdio option uses `uvx marketdata-mcp-server YOUR_API_KEY`.
- Docs describe progressive tool discovery to reduce token/tool overhead.

Operational implication:
- Treat Alpha Vantage as a credentialed MCP: disabled until `ALPHA_VANTAGE_API_KEY` exists.
- Use it for equities, ETFs, FX, macro series, technical indicators, and cross-checks against Yahoo-style fallbacks.

## Exa MCP

Source URL: https://github.com/exa-labs/exa-mcp-server

Seed use:
- Search/research MCP for high-recall web and company/domain discovery.
- Useful for finding primary sources, filings, API docs, and market commentary.

Operational implication:
- Never treat search snippets as evidence. Ingest URLs, then promote only verified claims into curated notes.

## Firecrawl MCP

Source URL: https://github.com/mendableai/firecrawl-mcp-server

Seed use:
- Web extraction/crawling for article capture, docs ingestion, and structured snapshots.
- Useful for turning fragile web pages into stable raw material under `raw/articles/`.

Operational implication:
- Firecrawl output is a capture tool, not an authority. Source quality comes from the captured source, not from the crawler.

## Minimum acceptance checks

Before relying on a market-data MCP:
1. Confirm server starts.
2. Confirm credential environment is isolated to `{{HERMES_FINANCE_HOME}}/.env`.
3. Run one harmless read-only query.
4. Save query timestamp, source, and raw response path when used in a decision.

Related: [[market-research-dataset]], [[source-quality]], [[mcp-readiness-check]], [[yahoo-finance-fallback]].
