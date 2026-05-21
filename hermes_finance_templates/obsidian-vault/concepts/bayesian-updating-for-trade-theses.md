---
id: bayesian-updating-for-trade-theses
title: Bayesian Updating For Trade Theses
type: concept
tags: [research, trading, risk]
status: active
created: 2026-05-20
updated: 2026-05-20
source_quality: paper-synthesis
---

# Bayesian Updating For Trade Theses

Bayesian updating is the default math for transforming new evidence into a changed trade probability. It prevents two common agent failures: treating every headline as decisive, and refusing to update when the world changes.

## Odds form

Use odds form because it handles sequential evidence cleanly:

```text
odds = p / (1 - p)
posterior_odds = prior_odds * LR_1 * LR_2 * ... * LR_n
posterior_probability = posterior_odds / (1 + posterior_odds)
```

Where:

```text
LR_i = P(evidence_i | thesis true) / P(evidence_i | thesis false)
```

A source can be bullish but weak. Example:

```text
prior p = 0.30
prior odds = 0.30 / 0.70 = 0.4286
headline LR = 1.25
posterior odds = 0.5357
posterior p = 0.349
```

That headline moved fair probability from 30% to 35%, not to 70%.

## Avoid double-counting correlated evidence

If five articles cite the same official statement, they are not five independent likelihood ratios. Treat them as one source event plus confirmation of distribution.

```text
independent_LR_product = LR_primary * LR_independent_secondary
not = LR_same_story^5
```

Hermes Finance should ask:

- Does this source add new information?
- Does it share origin with another source?
- Is it a price reaction masquerading as evidence?
- Does it affect resolution criteria or only narrative?

## Beta-binomial calibration for repeated strategy claims

When evaluating a strategy with `w` wins and `l` losses, use a Beta prior:

```text
p ~ Beta(alpha, beta)
posterior = Beta(alpha + w, beta + l)
posterior_mean = (alpha + w) / (alpha + beta + w + l)
```

A neutral prior is `Beta(1,1)`. A skeptical prior for noisy markets can be `Beta(2,3)` or stronger. This matters for small samples: a strategy with 3 wins and 0 losses is not proven.

```text
Beta(1,1) + 3W 0L -> mean = 4/5 = 80%
Beta(5,5) + 3W 0L -> mean = 8/13 = 61.5%
```

Use skeptical priors for new alpha.

## Likelihood ratio operating table

```text
LR 1.0  = no information
LR 1.2  = weak nudge
LR 1.5  = useful but not decisive
LR 2.0  = strong evidence
LR 3.0+ = very strong evidence; verify source and independence
LR <1   = evidence against thesis
```

A low-quality source should rarely receive LR above 1.2. A direct official source can receive higher LR, but only if the market resolution criteria truly depend on it.

## Polymarket workflow

1. Start with base rate or market-implied prior.
2. Read resolution criteria.
3. Build evidence table with source independence.
4. Convert each independent evidence item to a conservative LR.
5. Update probability.
6. Compare posterior fair probability with executable ask/bid.
7. Size after a model-error haircut.

## Hyperliquid workflow

For perps, translate signals into expected return distributions rather than binary outcomes. A Bayesian update can still adjust thesis probability:

```text
expected_return = P(trend_regime)*trend_return + P(chop_regime)*chop_return + P(crash_regime)*crash_return
```

Regime probabilities update after volatility, funding, orderbook, macro, or flow evidence.

## Sources

- Gneiting and Raftery, "Strictly Proper Scoring Rules, Prediction, and Estimation" (2007): https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf
- Wolfers and Zitzewitz, "Interpreting Prediction Market Prices as Probabilities": https://users.nber.org/~jwolfers/papers/InterpretingPredictionMarketPrices.pdf

Related: [[claim-evidence-probability-ev]], [[source-quality]], [[source-triangulation]], [[prediction-market-calibration]], [[decision-record-template]].
