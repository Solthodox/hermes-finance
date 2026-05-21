---
id: prediction-market-calibration
title: Prediction Market Calibration
type: market
tags: [polymarket, trading, risk]
status: active
created: 2026-05-20
updated: 2026-05-20
source_quality: paper-synthesis
---

# Prediction Market Calibration

Prediction market prices are useful probability signals, but Hermes Finance must not treat them as pure truth. A market price is a risk-adjusted, fee-affected, liquidity-constrained, sometimes-manipulated exchange rate between cash and state-contingent payoff.

## First-order interpretation

For a binary contract paying `$1` if an event happens and `$0` otherwise:

```text
no_fee_fair_price = P(event)
```

If YES ask is 0.42 and fair probability is 0.50:

```text
EV_per_share = 0.50 - 0.42 = 0.08
ROI_on_cash = 0.08 / 0.42 = 19.0%
```

This is the clean model. Real Polymarket trades are dirtier.

## Why market price can differ from probability

Observed price can deviate because of:

- spread and fees;
- limited depth;
- non-risk-neutral traders;
- correlated inventory constraints;
- entertainment demand and longshot bias;
- hedging demand;
- slow information incorporation;
- market-rule ambiguity;
- manipulation attempts in thin markets;
- inability to short or borrow cheaply;
- capital lockup until resolution.

A good trader asks: "is this mispricing exploitable after execution?" not merely "is the market wrong?"

## Calibration bins

Track prediction quality with bins:

```text
0.00-0.10 forecast bin -> realized frequency?
0.10-0.20 forecast bin -> realized frequency?
...
0.90-1.00 forecast bin -> realized frequency?
```

If Hermes calls many outcomes 70% and only 50% happen, it is overconfident. If 70% forecasts happen 80%, it may be underconfident or finding edge.

## Brier and log-loss for postmortems

For every resolved binary decision:

```text
brier = (p_forecast - outcome)^2
log_loss = -ln(p_forecast) if outcome=1
log_loss = -ln(1 - p_forecast) if outcome=0
```

Postmortems should record:

```text
forecast_probability:
market_price:
closing_price_if_available:
outcome:
brier:
log_loss:
edge_estimate:
realized_edge:
error_source:
```

## Favorite-longshot and category effects

Prediction markets can show category-dependent bias. A 5% entertainment longshot can be overpriced, while a neglected geopolitical tail can be underpriced. Therefore calibration must be segmented:

```text
calibration_by_category = {
  geopolitics,
  elections,
  crypto_price,
  sports,
  macro,
  pop_culture,
  protocol_events
}
```

Do not average categories and conclude the agent is calibrated.

## Market scoring rule intuition

Automated market makers such as LMSR use a cost function:

```text
C(q) = b * ln(sum_i exp(q_i / b))
price_i = exp(q_i / b) / sum_j exp(q_j / b)
```

The liquidity parameter `b` controls how much price moves after trades. Even though Polymarket uses a CLOB, LMSR is useful conceptually: market prices aggregate expressed beliefs subject to liquidity and inventory costs.

## Practical Polymarket calibration protocol

Before recommending a trade:

1. Compare market-implied probability to base rate.
2. Compare to source-driven Bayesian posterior.
3. Check if the edge survives spread/depth.
4. Check category calibration: crypto/sports require stronger evidence; geopolitics may have better discretionary edge.
5. Check resolution ambiguity. If rules are ambiguous, lower confidence even when evidence is strong.
6. Record the forecast so future Hermes can score itself.

## Sources

- Wolfers and Zitzewitz, "Prediction Markets" (Journal of Economic Perspectives, 2004): https://www.nber.org/system/files/working_papers/w10504/w10504.pdf
- Wolfers and Zitzewitz, "Interpreting Prediction Market Prices as Probabilities": https://users.nber.org/~jwolfers/papers/InterpretingPredictionMarketPrices.pdf
- Hanson, "Combinatorial Information Market Design" / market scoring rules: https://mason.gmu.edu/~rhanson/mktscore.pdf
- Berg, Nelson, and Rietz, prediction market accuracy evidence: https://biz.uiowa.edu/faculty/trietz/papers/forecasting.pdf

Related: [[polymarket-platform]], [[market-rules-and-resolution]], [[claim-evidence-probability-ev]], [[bayesian-updating-for-trade-theses]], [[trade-journal-dataset]].
