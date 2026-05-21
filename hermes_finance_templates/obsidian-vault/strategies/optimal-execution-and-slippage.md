---
id: optimal-execution-and-slippage
title: Optimal Execution And Slippage
type: strategy
tags: [strategy, execution, risk]
status: active
created: 2026-05-20
updated: 2026-05-20
source_quality: paper-synthesis
---

# Optimal Execution And Slippage

Optimal execution is the discipline of turning a good trade idea into an actual fill without donating the edge to spread, slippage, or market impact.

## Implementation shortfall

Execution quality should be measured against the decision price:

```text
implementation_shortfall = realized_execution_cost - paper_decision_cost
```

For a buy:

```text
shortfall = average_fill_price - decision_mid_or_signal_price
```

A strategy can have positive paper EV and negative realized EV if implementation shortfall is too high.

## Almgren-Chriss intuition

Almgren-Chriss separates market impact into permanent and temporary components:

```text
execution_price = unaffected_price + permanent_impact + temporary_impact + noise
```

Fast execution reduces price risk but increases impact. Slow execution reduces impact but increases timing risk. The optimal schedule trades off:

```text
expected_cost + risk_aversion * variance_of_cost
```

For small Hermes accounts, the exact continuous-time solution is less important than the operating lesson: urgency has a price.

## Slippage budget

Every recommendation should include:

```text
max_acceptable_price:
max_slippage:
min_depth:
time_in_force:
when_to_cancel:
```

If the order cannot fill within the slippage budget, the trade is not the same trade.

## Limit vs market decision

Use marketable orders only when:

- risk repair is urgent;
- spread is tight relative to edge;
- size is small relative to displayed depth;
- failing to fill is worse than paying spread.

Use passive/limit orders when:

- edge is price-sensitive;
- book is wide;
- urgency is low;
- thesis horizon is long enough to wait.

## Weighted executable price

For a buy consuming asks:

```text
avg_price = sum(price_i * quantity_i_filled) / sum(quantity_i_filled)
```

Use average executable price, not best ask, in EV.

## Polymarket execution rules

- Always inspect market rules before execution.
- Use current ask/bid, not stale research price.
- Check depth for the exact order size.
- Add only a small price buffer for normal tick drift when EV survives.
- If spread is wide, prefer no trade or smaller passive order.
- Never re-enter a user-closed thesis cluster without approval.

## Hyperliquid execution rules

- Bracket entries should include protective stop and take-profit plan.
- Verify all reduce-only orders after fill.
- Round every price to tick size.
- Reduce notional when volatility or spread rises.
- Avoid compounding into liquidation cascades.

## Sources

- Almgren and Chriss, "Optimal Execution of Portfolio Transactions" (2000): https://quantitativebrokers.com/s/Optimal-Execution-of-Portfolio-Transaction-_-AlmgrenChriss-1999.pdf
- Avellaneda and Stoikov, "High-frequency trading in a limit order book" (2008): https://math.nyu.edu/~avellane/HighFrequencyTrading.pdf

Related: [[limit-order-book-microstructure]], [[liquidity-and-slippage]], [[execution-checklist]], [[polymarket-clob]], [[open-orders-verification]].
