---
id: claim-evidence-probability-ev
title: Claim Evidence Probability EV
type: concept
tags: [research, trading, risk]
status: active
created: 2026-05-20
updated: 2026-05-20
source_quality: paper-synthesis
---

# Claim Evidence Probability EV

A trade thesis is a chain from claim to evidence to probability to expected value. Hermes Finance must make every link explicit, because most bad trades hide the weak link: a true claim that is already priced, a strong source that does not resolve the market, or a good probability estimate with bad execution costs.

## Minimal equation

For any trade:

```text
EV = P(win) * payoff_if_right - P(loss) * loss_if_wrong - costs
```

For a binary YES bought at executable price `c` with fair probability `p`:

```text
EV_per_share = p * (1 - c) - (1 - p) * c
             = p - c
ROI_on_cash  = (p - c) / c
```

This makes Polymarket edge visually simple: if fair probability is 47% and ask is 39%, raw expected value is 8 cents/share before costs. But the hard part is estimating `p` honestly.

## Evidence ladder

Convert evidence to probability using a ladder:

```text
claim -> source -> mechanism -> base rate -> likelihood ratio -> updated probability -> executable EV
```

Each source should be tagged by:

- proximity to primary data;
- timestamp and freshness;
- incentive to mislead;
- independence from other sources;
- relevance to the exact market resolution criteria;
- whether it changes probability or only explains price action.

## Bayesian update form

Use odds form when evidence arrives sequentially:

```text
prior_odds = prior_probability / (1 - prior_probability)
posterior_odds = prior_odds * likelihood_ratio
posterior_probability = posterior_odds / (1 + posterior_odds)
```

A likelihood ratio answers: "how much more likely would I see this evidence if the claim is true than if it is false?"

```text
LR = P(evidence | thesis true) / P(evidence | thesis false)
```

Example: if base probability is 25% and a source has LR=2:

```text
prior_odds = 0.25 / 0.75 = 0.333
posterior_odds = 0.333 * 2 = 0.666
posterior_probability = 0.666 / 1.666 = 40%
```

The update is large but not magic. Starting priors matter.

## Proper scoring mindset

Hermes Finance should care about calibration, not vibes. For binary forecasts:

```text
Brier score = (forecast_probability - outcome)^2
log loss    = -[ outcome*ln(p) + (1-outcome)*ln(1-p) ]
```

Brier is intuitive and bounded; log loss punishes confident wrong forecasts heavily. A super-smart trader is not one who says "high conviction" often; it is one whose 70% forecasts happen about 70% of the time, whose 30% forecasts happen about 30% of the time, and whose sizing respects uncertainty.

## Edge decomposition

Expected edge can come from several places:

```text
edge = information_edge + model_edge + behavioral_edge + execution_edge - cost_drag - error_margin
```

- Information edge: you know relevant facts earlier or more accurately.
- Model edge: you interpret common information better.
- Behavioral edge: market overreacts, underreacts, or misprices tails.
- Execution edge: better limit placement, patience, or liquidity use.
- Cost drag: spread, fees, funding, slippage, failed fills.
- Error margin: haircut for model uncertainty.

If the edge disappears after a conservative error margin, no trade.

## Required decision record fields

Every executable thesis needs:

```text
market/instrument:
time horizon:
resolution/execution rule:
prior/base rate:
evidence table:
fair probability or return distribution:
current executable price:
EV after costs:
size:
invalidation:
post-entry monitoring:
approval:
```

## Sources

- Gneiting and Raftery, "Strictly Proper Scoring Rules, Prediction, and Estimation" (2007): https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf
- Brier score background: https://apps.dtic.mil/sti/pdfs/ADA454828.pdf
- Wolfers and Zitzewitz, "Interpreting Prediction Market Prices as Probabilities" (NBER): https://users.nber.org/~jwolfers/papers/InterpretingPredictionMarketPrices.pdf

Related: [[source-quality]], [[source-triangulation]], [[bayesian-updating-for-trade-theses]], [[prediction-market-calibration]], [[expected-value]].
