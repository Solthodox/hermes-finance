---
id: market-microstructure-and-execution-source-cards
title: Market Microstructure and Execution Source Cards
type: raw-source
tags: [research, execution, trading, source-quality]
status: seed
created: 2026-05-23
updated: 2026-05-23
source_quality: canonical-literature
---

# Market Microstructure and Execution Source Cards

Immutable seed capture for market microstructure and execution theory. Use this before updating [[limit-order-book-microstructure]], [[optimal-execution-and-slippage]], [[orderbook-and-spread-analysis]], [[liquidity-and-slippage]], and [[open-orders-verification]].

## Glosten-Milgrom intuition

Canonical idea:
- Bid/ask spreads compensate liquidity providers for adverse selection against better-informed traders.

Hermes Finance operating rule:
- Wide spreads are not just friction; they are information. Crossing a wide spread without a strong thesis destroys edge.

## Kyle model intuition

Canonical idea:
- Price impact reflects how market makers infer informed orderflow from aggregate trading pressure.

Hermes Finance operating rule:
- Large orders relative to displayed depth should be split, rested, or rejected unless urgency dominates impact cost.

## Avellaneda-Stoikov market making intuition

Canonical reference:
- Avellaneda and Stoikov (2008), high-frequency market-making model.

Core idea:
- Optimal quotes depend on inventory, risk aversion, volatility, and order arrival intensity.

Hermes Finance operating rule:
- If inventory is already skewed, new orders must account for inventory risk; do not quote/add exposure as if flat.

## Almgren-Chriss execution intuition

Canonical reference:
- Almgren and Chriss (2000), optimal execution of portfolio transactions.

Core idea:
- Execution trades off market impact against timing risk.

Hermes Finance operating rule:
- For larger exits, choose explicit urgency: immediate risk reduction, passive unwind, or staged execution. Do not default to market orders.

Related: [[execution-checklist]], [[fees-spread-and-edge-hurdle]], [[post-trade-protection]], [[orderbook-snapshot-dataset]].
