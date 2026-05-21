---
id: robust-portfolio-construction
title: Robust Portfolio Construction
type: risk
tags: [risk, portfolio, trading]
status: active
created: 2026-05-20
updated: 2026-05-20
source_quality: paper-synthesis
---

# Robust Portfolio Construction

Robust portfolio construction exists because naive optimization is a machine for amplifying estimation error. Hermes Finance should use portfolio math to reduce fragility, not to produce false precision.

## Markowitz core

Mean-variance optimization chooses weights `w` to trade expected return against variance:

```text
portfolio_return = w^T mu
portfolio_variance = w^T Sigma w
objective = maximize w^T mu - lambda * w^T Sigma w
```

Where:

- `mu` is expected returns;
- `Sigma` is covariance matrix;
- `lambda` is risk aversion.

The problem: `mu` is extremely noisy. Small expected-return errors can create extreme weights.

## Estimation error rule

Expected returns are usually less reliable than volatilities and correlations. Therefore:

```text
trust_order = constraints > volatility > correlation > expected_return
```

Hermes should prefer robust constraints over optimizer outputs:

- max venue exposure;
- max thesis cluster exposure;
- max single-market exposure;
- liquidity caps;
- leverage caps;
- drawdown-based size cuts.

## Covariance shrinkage

Sample covariance is unstable when assets are many or history is short. Shrinkage blends sample covariance with a structured target:

```text
Sigma_shrunk = delta * F + (1 - delta) * S
```

Where:

- `S` is sample covariance;
- `F` is a target such as constant-correlation or diagonal covariance;
- `delta` is shrinkage intensity.

Interpretation: do not fully trust noisy historical covariance.

## Risk parity intuition

Risk contribution of asset `i`:

```text
marginal_risk_i = (Sigma w)_i / sqrt(w^T Sigma w)
risk_contribution_i = w_i * marginal_risk_i
```

Risk parity tries to equalize risk contributions, not dollars. For Hermes Finance, exact risk parity is less important than the principle: a small notional can dominate risk if volatility or leverage is high.

## Black-Litterman intuition

Black-Litterman starts from market-implied equilibrium returns, then blends subjective views with uncertainty:

```text
posterior_expected_returns = blend(prior_equilibrium, views, view_confidence)
```

This maps well to agent trading: a thesis should have a confidence level. Low-confidence views should barely move allocations.

## Correlation and cluster risk

Do not rely only on statistical correlation. Event correlation is often invisible until stress:

```text
cluster_exposure = sum(position_loss_if_thesis_breaks)
```

Examples:

- Polymarket Iran/Hormuz/oil/geopolitics positions can all lose on one headline.
- Hyperliquid BTC and ETH longs can be one risk-on bet.
- Solana meme coins can be one liquidity-regime bet.

Hard rule: size clusters, not only instruments.

## Robust sizing algorithm

```text
for each proposed_trade:
    estimate standalone EV
    estimate standalone max loss
    map to clusters: venue, asset, thesis, time horizon, liquidity regime
    compute current cluster exposure
    compute stressed cluster loss
    apply volatility/liquidity haircut
    size = min(kelly_fractional_size, cluster_cap_remaining, liquidity_cap, daily_loss_remaining)
    reject if stressed loss violates drawdown guard
```

## Sources

- Markowitz, "Portfolio Selection" (1952): https://finance.martinsewell.com/capm/Markowitz1952.pdf
- Ledoit and Wolf, "Honey, I Shrunk the Sample Covariance Matrix" (2003): http://www.ledoit.net/honey.pdf
- Black and Litterman, "Global Portfolio Optimization" (1992), model reference.
- Boyd et al., "Markowitz Portfolio Construction at Seventy": https://web.stanford.edu/~boyd/papers/pdf/markowitz.pdf

Related: [[risk-management-framework]], [[correlation-and-cluster-risk]], [[fractional-kelly]], [[volatility-forecasting-and-regime-detection]], [[portfolio-exposure-ledger]].
