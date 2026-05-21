---
id: volatility-forecasting-and-regime-detection
title: Volatility Forecasting And Regime Detection
type: risk
tags: [risk, market-data, portfolio]
status: active
created: 2026-05-20
updated: 2026-05-20
source_quality: paper-synthesis
---

# Volatility Forecasting And Regime Detection

Volatility forecasting tells Hermes Finance how much notional to risk and when a strategy's historical behavior is no longer relevant. The point is not to predict volatility perfectly; it is to avoid sizing a high-volatility regime as if it were quiet.

## Realized volatility

For returns `r_t` over a window:

```text
realized_variance = sum(r_t^2)
realized_volatility = sqrt(realized_variance)
annualized_volatility = window_vol * sqrt(periods_per_year)
```

For crypto, annualization can be misleading because trading is continuous. Use operational horizons too:

```text
4h_vol, 1d_vol, 7d_vol, 30d_vol
```

## EWMA volatility

Exponentially weighted moving variance:

```text
sigma_t^2 = lambda * sigma_{t-1}^2 + (1 - lambda) * r_t^2
```

Lower `lambda` reacts faster; higher `lambda` is smoother.

## Range-based estimators

When OHLC data is available, high-low range can estimate volatility. Parkinson estimator:

```text
sigma^2 = (1 / (4 ln 2)) * [ln(high / low)]^2
```

Range-based estimators can extract more intraperiod information than close-to-close returns, but they can be distorted by bad candles or illiquid wicks.

## GARCH intuition

ARCH/GARCH models capture volatility clustering:

```text
sigma_t^2 = omega + alpha * r_{t-1}^2 + beta * sigma_{t-1}^2
```

Volatility tends to persist. A large shock today increases expected volatility tomorrow.

## Regime features

Hermes should track:

- realized volatility percentile;
- funding-rate extremes;
- spread/depth deterioration;
- correlation spike across assets;
- liquidation cascade signs;
- macro event calendar;
- news intensity;
- strategy signal frequency.

A regime change should reduce size before it creates losses.

## Volatility targeting

Position notional should shrink as volatility rises:

```text
target_notional = risk_budget / stop_distance
stop_distance = k * volatility_estimate
```

If volatility doubles and `k` is constant, stop distance doubles and notional halves.

## Kill-switch triggers

Pause or reduce automation when:

```text
realized_vol > 95th percentile
spread > normal_spread * 3
depth < normal_depth / 3
correlation_spike = true
protective_orders_missing = true
api_state_stale = true
```

## Sources

- Engle, ARCH model reference (1982).
- Bollerslev, GARCH model reference (1986): https://public.econ.duke.edu/~boller/Published_Papers/ectrev_86.pdf
- Parkinson, "The Extreme Value Method for Estimating the Variance of the Rate of Return" (1980): https://www.cmegroup.com/trading/fx/files/a_estimation_of_security_price.pdf
- Andersen et al., realized volatility research: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=267792

Related: [[leverage-budget]], [[drawdown-control]], [[robust-portfolio-construction]], [[time-series-momentum-and-trend-following]], [[kill-switch-policy]].
