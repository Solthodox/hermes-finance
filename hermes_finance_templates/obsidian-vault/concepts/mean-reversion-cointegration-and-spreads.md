---
id: mean-reversion-cointegration-and-spreads
title: Mean Reversion Cointegration And Spreads
type: concept
tags: [strategy, trading, market-data]
status: active
created: 2026-05-20
updated: 2026-05-20
source_quality: paper-synthesis
---

# Mean Reversion Cointegration And Spreads

Mean reversion trades the hypothesis that price deviations from a stable anchor will partially reverse. The danger is confusing a temporary deviation with a permanent repricing.

## Z-score spread model

For a spread `s_t` with rolling mean `mu` and standard deviation `sigma`:

```text
z_t = (s_t - mu) / sigma
```

Simple rule:

```text
if z_t > +entry_threshold: short spread
if z_t < -entry_threshold: long spread
exit when z_t crosses 0 or stop when model breaks
```

But rolling mean and standard deviation are unstable if regime changes.

## Ornstein-Uhlenbeck intuition

A mean-reverting process can be modeled as:

```text
dX_t = theta * (mu - X_t) dt + sigma dW_t
```

Half-life of mean reversion:

```text
half_life = ln(2) / theta
```

If half-life is long relative to trade horizon or capital lockup, the trade is not operationally attractive.

## Cointegration

Two price series can be non-stationary individually but have a stationary linear combination:

```text
spread_t = y_t - beta * x_t
```

If `spread_t` is stationary, it may be tradable as a relative-value spread. If not, z-scores are fake precision.

## Failure modes

- Structural break: relationship permanently changes.
- Crowding: many traders exit the same spread.
- Carry/funding: cost of waiting exceeds reversion edge.
- Liquidity asymmetry: one leg exits, the other gaps.
- Data snooping: pair selected because it looked good historically.

## Prediction market application

Mean reversion can appear in overreaction to headlines, but binary markets have terminal resolution. A mispriced market does not have to mean-revert before settlement. Use mean reversion only when there is a plausible flow or attention mechanism, not as a chart-only signal.

## Hyperliquid application

Pairs or relative-value trades require both legs to be executable and monitored. For small accounts, complexity often exceeds edge. If used, define:

```text
spread_definition:
entry_z:
exit_z:
stop_z:
max_holding_time:
funding_cost_limit:
leg_liquidity_check:
```

## Sources

- Engle and Granger, "Co-integration and Error Correction" (1987), model reference.
- Lo and MacKinlay, random walk and predictability research references.
- Gatev, Goetzmann, and Rouwenhorst, pairs trading literature reference.

Related: [[volatility-forecasting-and-regime-detection]], [[backtesting-overfitting-and-research-hygiene]], [[liquidity-and-slippage]], [[expected-value]], [[no-trade-decision]].
