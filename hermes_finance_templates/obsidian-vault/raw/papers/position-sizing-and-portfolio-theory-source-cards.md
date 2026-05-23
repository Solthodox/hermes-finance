---
id: position-sizing-and-portfolio-theory-source-cards
title: Position Sizing and Portfolio Theory Source Cards
type: raw-source
tags: [research, risk, portfolio, source-quality]
status: seed
created: 2026-05-23
updated: 2026-05-23
source_quality: canonical-literature
---

# Position Sizing and Portfolio Theory Source Cards

Immutable seed capture for sizing and allocation literature. Use this before updating [[fractional-kelly]], [[robust-portfolio-construction]], [[position-sizing]], [[correlation-and-cluster-risk]], and [[drawdown-control]].

## Kelly criterion

Primary reference:
- Kelly, J. L. (1956), "A New Interpretation of Information Rate".

Core idea:
- For favorable repeated bets, maximize expected logarithmic wealth, not expected dollar return.
- Full Kelly is extremely sensitive to probability/payoff estimation error.

Hermes Finance operating rule:
- Treat calculated Kelly as an upper bound.
- Use fractional Kelly after cutting for estimation error, liquidity, correlation, execution cost, and psychological tolerance.

## Markowitz portfolio selection

Primary reference:
- Markowitz, H. (1952), "Portfolio Selection".

Core idea:
- Portfolio risk depends on covariance, not only single-asset variance.
- Diversification fails when correlations rise under stress.

Hermes Finance operating rule:
- Do not size each trade independently. Cluster exposures by thesis, venue, asset, geography, liquidity regime, and event driver.

## Black-Litterman intuition

Canonical reference:
- Black and Litterman allocation framework, originally developed at Goldman Sachs.

Core idea:
- Combine market-implied equilibrium returns with explicit subjective views and confidence levels.

Hermes Finance operating rule:
- Represent discretionary theses as uncertain views, not point forecasts. Lower confidence should mechanically shrink size.

## Robust portfolio construction

Working principle:
- Fragile optimizers overreact to noisy expected returns and unstable covariance matrices.
- Shrinkage, caps, stress tests, and simple budgets usually outperform beautiful but brittle allocations in live operations.

Related: [[risk-management-framework]], [[position-sizing]], [[expected-value]], [[daily-loss-guard]].
