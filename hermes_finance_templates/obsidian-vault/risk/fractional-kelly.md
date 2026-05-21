---
id: fractional-kelly
title: Fractional Kelly
type: risk
tags: [risk, portfolio, trading]
status: active
created: 2026-05-20
updated: 2026-05-20
source_quality: paper-synthesis
---

# Fractional Kelly

Fractional Kelly is the capital-growth sizing rule Hermes Finance uses as an upper bound, not as an automatic bet size. The main insight is mathematical: if edge is real and bet sizing is repeated, overbetting is much more dangerous than underbetting. A trader who maximizes expected profit per trade can still destroy long-run compounded wealth.

## Core result

For a repeated bet that wins with probability `p`, loses with probability `q = 1 - p`, wins `b` units per unit risked, and risks fraction `f` of bankroll, terminal log wealth grows at:

```text
G(f) = p * ln(1 + b f) + q * ln(1 - f)
```

The unconstrained Kelly fraction is:

```text
f* = (b p - q) / b
```

Equivalent binary-price form for a Polymarket-style YES share:

```text
market_price = c
fair_probability = p
profit_if_win_per_$1_staked = (1 - c) / c
loss_if_lose_per_$1_staked = 1
full_kelly_fraction_of_bankroll = (p - c) / (1 - c)
```

Example: if a YES is offered at `c = 0.35` and true probability is `p = 0.45`, then:

```text
f* = (0.45 - 0.35) / (1 - 0.35) = 0.1538
```

Full Kelly says 15.4% of bankroll, but Hermes Finance must almost never bet full Kelly because `p` is estimated, liquidity is finite, correlation exists, and market rules can be ambiguous. A common operating haircut is 10%-25% of Kelly before hard caps.

## Why fractional Kelly beats full Kelly for an agent

Full Kelly assumes the edge estimate is correct. If `p` is noisy, the sizing error is asymmetric:

- undersizing leaves money on the table;
- oversizing increases volatility and drawdown sharply;
- betting above Kelly makes expected log growth fall;
- betting at 2x Kelly has zero expected log-growth in the simple even-money case;
- betting beyond 2x Kelly has negative expected log-growth despite positive edge.

Hermes Finance should therefore compute:

```text
raw_kelly = formula_edge_size
estimation_haircut = source_quality * model_confidence * rule_clarity
liquidity_haircut = min(1, usable_depth / desired_size)
correlation_haircut = 1 / sqrt(cluster_exposure_count)
operating_fraction = raw_kelly * 0.10_to_0.25 * estimation_haircut * liquidity_haircut * correlation_haircut
final_size = min(operating_fraction * bankroll, hard_caps, available_cash, depth_cap)
```

The formula is deliberately conservative. If a trade cannot survive conservative sizing, the edge is probably not operationally strong enough.

## Continuous-return approximation

If a strategy has expected excess return `mu` and variance `sigma^2`, log-optimal leverage is approximately:

```text
f* = mu / sigma^2
```

This is useful for Hyperliquid/perp sizing. It says leverage should drop quadratically as volatility rises. If expected return doubles but volatility also doubles, optimal leverage halves:

```text
(mu * 2) / (2 sigma)^2 = mu / (2 sigma^2)
```

This is why volatility targeting belongs upstream of leverage. A breakout signal with high volatility is not automatically a bigger trade.

## Risk of ruin and drawdown reality

Kelly maximizes asymptotic log wealth, not comfort. Full Kelly can still experience deep drawdowns. For a human-agent system with small capital and uncertain estimates, Hermes Finance should treat full Kelly as a warning label:

```text
if proposed_size > 0.25 * kelly_size: require exceptional evidence
if proposed_size > 0.50 * kelly_size: assume sizing is wrong unless proven otherwise
if proposed_size > 1.00 * kelly_size: reject by default
```

A useful no-trade rule:

```text
if edge exists only at full Kelly sizing, edge is not robust enough
```

## Polymarket application

Before using the binary Kelly formula:

1. Verify market rules and resolution source.
2. Estimate fair probability from base rates and evidence, not from market price.
3. Use current ask for buys and bid for sells; midpoint overstates executable edge.
4. Subtract fees, spread, and expected slippage.
5. Apply cluster haircut for related markets.
6. Hard-cap the order even if Kelly says bigger.

Polymarket size sanity:

```text
edge_pp = fair_probability - ask_price
if edge_pp < 0.03: usually no trade
if 0.03 <= edge_pp < 0.07: discovery/low conviction only
if edge_pp >= 0.07: evaluate Kelly, but cap by liquidity and thesis cluster
```

## Hyperliquid application

For perps, use volatility-adjusted notional:

```text
signal_strength = expected_move / recent_volatility
base_risk = account_equity * risk_per_trade
stop_distance = abs(entry - stop) / entry
notional = base_risk / stop_distance
notional = min(notional, leverage_budget, liquidity_budget, correlation_budget)
```

If stop distance widens because volatility increased, notional must shrink.

## Sources

- J. L. Kelly Jr., "A New Interpretation of Information Rate" (1956): https://www.princeton.edu/~wbialek/rome/refs/kelly_56.pdf
- Edward O. Thorp, "The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market" (2006/2007): https://gwern.net/doc/statistics/decision/2006-thorp.pdf
- MacLean, Thorp, and Ziemba, _The Kelly Capital Growth Investment Criterion_ (book reference).

Related: [[expected-value]], [[position-sizing]], [[risk-of-ruin]], [[portfolio-exposure-ledger]], [[robust-portfolio-construction]].
