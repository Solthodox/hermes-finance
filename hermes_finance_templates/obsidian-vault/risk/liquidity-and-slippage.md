---
id: liquidity-and-slippage
title: Liquidity And Slippage
type: risk
tags: [risk, execution, trading]
status: active
created: 2026-05-20
updated: 2026-05-20
source_quality: paper-synthesis
---

# Liquidity And Slippage

Liquidity is the amount of risk the market can absorb near current prices. Slippage is the price paid for demanding liquidity. Hermes Finance must compute executable edge, not paper edge.

## Top-of-book is not executable size

For a buy order walking the ask book:

```text
avg_exec_price(size) = sum(price_i * filled_qty_i) / size
slippage = avg_exec_price(size) - best_ask_at_decision
edge_after_slippage = fair_value - avg_exec_price(size)
```

For a sell:

```text
avg_exec_price(size) = sum(price_i * filled_qty_i) / size
slippage = best_bid_at_decision - avg_exec_price(size)
edge_after_slippage = avg_exec_price(size) - fair_value_to_exit
```

If `edge_after_slippage <= 0`, the trade is not valid at that size.

## Spread hurdle

For immediate entry and exit, the spread is a round-trip tax:

```text
round_trip_spread_cost ≈ ask - bid
required_edge > spread + fees + expected_slippage + model_error
```

A 4 cent edge in a binary market with a 3 cent spread and uncertain rules is probably not enough.

## Market impact model

A simple impact approximation:

```text
impact_cost = k * (order_size / visible_depth)^alpha
```

Where `alpha` is often between 0.5 and 1 in rough models. Hermes does not need exact `k`; it needs the habit of shrinking size when size/depth rises.

## Liquidity checklist

- Is depth real or stale?
- Is the market one-sided?
- Does desired size consume multiple levels?
- Are there recent trades or just posted quotes?
- Does liquidity vanish during news?
- Can exit liquidity disappear before resolution?
- Is capital locked until settlement?

## Polymarket

Prediction markets often have asymmetric liquidity. A position can be easy to enter and hard to exit. Always record:

```text
best_bid:
best_ask:
spread:
depth_to_size:
avg_entry_price_for_size:
expected_exit_route:
resolution_date:
```

## Hyperliquid

Perp liquidity can look deep until volatility spikes. For leveraged positions, slippage affects both entry and liquidation/stop behavior. If spread/depth deteriorates, reduce notional or skip.

## Sources

- Almgren and Chriss, optimal execution and market impact: https://quantitativebrokers.com/s/Optimal-Execution-of-Portfolio-Transaction-_-AlmgrenChriss-1999.pdf
- Avellaneda and Stoikov, limit order book quoting: https://math.nyu.edu/~avellane/HighFrequencyTrading.pdf
- Kyle, continuous auctions / price impact reference.

Related: [[limit-order-book-microstructure]], [[optimal-execution-and-slippage]], [[orderbook-and-spread-analysis]], [[execution-checklist]], [[fees-spread-and-edge-hurdle]].
