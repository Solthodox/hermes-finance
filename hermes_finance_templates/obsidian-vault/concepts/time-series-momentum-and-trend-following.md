---
id: time-series-momentum-and-trend-following
title: Time Series Momentum And Trend Following
type: concept
tags: [strategy, trading, market-data]
status: active
created: 2026-05-20
updated: 2026-05-20
source_quality: paper-synthesis
---

# Time Series Momentum And Trend Following

Trend following is the hypothesis that assets with positive recent excess returns are more likely to keep moving in the same direction over a target horizon. Hermes Finance should understand both the evidence and the failure modes: trend works episodically, suffers whipsaws, and must be volatility-scaled.

## Cross-sectional vs time-series momentum

Cross-sectional momentum ranks assets against each other:

```text
buy past winners, sell past losers
```

Time-series momentum evaluates each asset against its own past:

```text
if past_return(asset, lookback) > 0: long
if past_return(asset, lookback) < 0: short
```

Hermes Hyperliquid swing logic is closer to time-series momentum.

## Simple signal forms

```text
return_signal = sign(close_t / close_{t-L} - 1)
ema_signal = sign(close_t - EMA_N(close))
breakout_signal = close_t > max(high_{t-L:t-1})
```

A robust system should avoid requiring too many highly correlated confirmations. EMA trend and breakout can be related; volume confirmation may reduce false positives but also reduce trade frequency.

## Volatility scaling

Momentum positions should usually be scaled by realized volatility:

```text
target_notional = target_risk / realized_volatility
```

If realized volatility doubles, notional halves. Without volatility scaling, a trend system accidentally bets largest when risk is highest.

## Expected failure modes

- Choppy regimes: repeated false breakouts.
- Late entries: signal fires after most move is done.
- Crowded exits: everyone stops out at similar levels.
- Funding drag: perp carry consumes edge.
- Volatility shocks: stops too tight in high-vol regimes, too loose in quiet regimes.

## Diagnostic for no-signal streaks

If no signals occur across repeated cycles, diagnose each condition separately:

```text
trend_condition = close > EMA20
breakout_condition = close > rolling_high_lookback
volume_condition = current_volume > avg_volume * threshold
```

Do not blindly loosen all parameters. Identify which gate is binding and whether market regime justifies loosening it.

## Research evidence

Academic momentum evidence is strongest at portfolio scale and across diversified assets. Single-asset discretionary use needs more caution. The lesson for Hermes is not "always buy breakouts"; it is "trend is a known anomaly, but execution, volatility, and regime filters decide whether it is tradable."

## Sources

- Jegadeesh and Titman, "Returns to Buying Winners and Selling Losers" (1993): https://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf
- Moskowitz, Ooi, and Pedersen, "Time Series Momentum" (2012): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2089463

Related: [[ema20-breakout-strategy]], [[volatility-forecasting-and-regime-detection]], [[no-signal-diagnostic]], [[backtesting-overfitting-and-research-hygiene]], [[post-entry-monitoring]].
