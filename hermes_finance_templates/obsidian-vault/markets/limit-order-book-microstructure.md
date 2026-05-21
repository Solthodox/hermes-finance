---
id: limit-order-book-microstructure
title: Limit Order Book Microstructure
type: market
tags: [trading, execution, market-data]
status: active
created: 2026-05-20
updated: 2026-05-20
source_quality: paper-synthesis
---

# Limit Order Book Microstructure

Limit order book microstructure is the study of how prices form at the bid/ask level. Hermes Finance needs this because many apparent edges disappear after spread, queue priority, adverse selection, and market impact.

## Basic book variables

```text
best_bid = highest buy limit price
best_ask = lowest sell limit price
mid = (best_bid + best_ask) / 2
spread = best_ask - best_bid
microprice = (ask_price * bid_size + bid_price * ask_size) / (bid_size + ask_size)
```

Microprice leans toward the side with less liquidity. If ask size is thin and bid size is large, microprice moves upward.

## Spread components

Observed spread compensates liquidity providers for:

- order processing costs;
- inventory risk;
- adverse selection;
- tick-size constraints;
- latency/cancel risk;
- capital lockup.

For Hermes Finance, spread is not noise. It is the market charging for immediacy.

## Adverse selection

A market order is often most tempting when the book is stale. If you buy the ask right before bad news or informed flow, you paid spread and received negative information selection.

Glosten-Milgrom intuition:

```text
spread widens when probability of informed trading rises
```

Kyle intuition:

```text
price_impact = lambda * signed_order_flow
```

Where `lambda` is market depth/adverse selection sensitivity.

## Queue priority

A posted limit order is not guaranteed to fill. Expected value of a passive order:

```text
EV_passive = P(fill_good) * edge - P(fill_bad) * adverse_selection_loss - opportunity_cost
```

A passive order that fills only when the market moves against you is not free edge.

## Avellaneda-Stoikov market-making intuition

In a stylized market-making model, optimal quotes depend on reservation price and inventory:

```text
reservation_price = mid - inventory * gamma * sigma^2 * time_remaining
optimal_spread increases with volatility and risk_aversion
```

If inventory is long, quote lower to reduce inventory. If volatility rises, widen spreads. Hermes can apply the same idea to discretionary execution: do not cross wide spreads in volatile markets unless edge is large.

## Polymarket application

Prediction market orderbooks are often thin. Required checks:

```text
executable_ask_for_size = weighted average ask through desired shares
raw_edge = fair_probability - executable_ask
edge_after_slippage = fair_probability - executable_average_price
```

Do not use top-of-book price for a size that consumes multiple levels.

## Hyperliquid application

For perps:

- verify tick size;
- inspect depth around entry and stop levels;
- avoid market orders in thin books unless risk repair requires immediacy;
- verify reduce-only protective orders after fills;
- treat funding and liquidation cascades as microstructure risks.

## Sources

- Kyle, "Continuous Auctions and Insider Trading" (1985), market impact model reference.
- Glosten and Milgrom, "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders" (1985): https://web.stanford.edu/~milgrom/publishedarticles/Bid%20Ask%20and%20Transaction%20Prices.pdf
- Avellaneda and Stoikov, "High-frequency trading in a limit order book" (2008): https://math.nyu.edu/~avellane/HighFrequencyTrading.pdf

Related: [[liquidity-and-slippage]], [[orderbook-and-spread-analysis]], [[polymarket-clob]], [[optimal-execution-and-slippage]], [[execution-checklist]].
