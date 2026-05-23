---
id: trading-venue-api-source-cards
title: Trading Venue API Source Cards
type: raw-source
tags: [research, trading, execution, market-data, source-quality]
status: seed
created: 2026-05-23
updated: 2026-05-23
source_quality: primary-docs
---

# Trading Venue API Source Cards

Immutable seed capture for venue API facts. Use this as raw source context before editing [[polymarket-clob]], [[polymarket-direct-mcp-safety]], [[hyperliquid-exchange]], [[hyperliquid-account-architecture]], [[hyperliquid-direct-mcp-safety]], and [[open-orders-verification]].

## Polymarket CLOB

Source URL: https://docs.polymarket.com/trading/overview

Observed from official docs:
- Polymarket CLOB is hybrid-decentralized: offchain order matching, onchain settlement via Exchange contract on Polygon.
- Orders are EIP-712 signed messages.
- Authentication has L1 and L2 layers: private-key signature for deriving credentials, HMAC credentials for authenticated trading calls.
- Order creation still requires the user's key to sign the order payload even when L2 credentials authenticate the request.
- Wallet signature types include EOA, proxy, Gnosis Safe, and POLY_1271 deposit wallet. Docs recommend deposit wallets for new API users.

Operational implication:
- Any live Polymarket order path must prove: wallet type, funder address, chain ID, token IDs, market rules, open orders, and current position before signing.
- Position accounting must net chronological BUY/SELL events, not just display UI holdings.

## Hyperliquid API

Source URL: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api

Observed from official docs:
- Official docs point to the Hyperliquid Python SDK and mainnet/testnet API URLs.
- Mainnet API URL: `https://api.hyperliquid.xyz`.
- Testnet API URL: `https://api.hyperliquid-testnet.xyz`.
- SDKs exist in Python, Rust, TypeScript, and CCXT integration.

Operational implication:
- Prefer read-only testnet/smoke checks before enabling live order placement.
- Verify account address, agent/API wallet, vault address, margin mode, open orders, and reduce-only semantics before changing exposure.

## Shared venue safety checks

For every direct-trading MCP or script:
1. Start disabled by default.
2. Require credentials in isolated `.env`.
3. Require explicit include-live-trading flag or user approval before enablement.
4. Require read-only account reconciliation before any order action.
5. Log raw responses and decision records before execution.

Related: [[execution-checklist]], [[decision-record-template]], [[orderbook-snapshot-dataset]], [[trade-journal-dataset]].
