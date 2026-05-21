---
id: backtesting-overfitting-and-research-hygiene
title: Backtesting Overfitting And Research Hygiene
type: playbook
tags: [research, strategy, risk]
status: active
created: 2026-05-20
updated: 2026-05-20
source_quality: paper-synthesis
---

# Backtesting Overfitting And Research Hygiene

Backtesting is where trading agents hallucinate profits with math. Hermes Finance must treat every backtest as a hypothesis test under severe selection bias, not as proof of edge.

## Common false edges

- Lookahead bias: using data not known at decision time.
- Survivorship bias: excluding dead assets/markets.
- Multiple testing: trying many strategies and reporting the winner.
- Parameter mining: tuning thresholds until history looks good.
- Leakage: labels or future prices sneak into features.
- Cost omission: ignoring spread, fees, slippage, funding, failed fills.
- Regime overfit: strategy works only in one historical regime.
- Capacity overfit: trade size assumes impossible liquidity.

## Minimum viable backtest rules

```text
train_period != validation_period != test_period
features_timestamp <= decision_timestamp
execution_price = executable bid/ask, not midpoint
costs = fees + spread + slippage + funding + failed_fill_penalty
parameters chosen before test period
all tried variants logged
```

## Walk-forward protocol

```text
for each window:
    fit parameters on training window
    validate on next window
    trade/evaluate on unseen forward window
    roll forward
aggregate all forward windows
```

Do not tune on the final test set.

## Multiple testing haircut

If Hermes tries 100 variants and one has Sharpe 2, that is not impressive by itself. Expected maximum Sharpe rises with the number of trials. Record:

```text
number_of_trials:
parameter_grid:
selection_rule:
best_metric:
median_metric:
out_of_sample_metric:
```

## Deflated Sharpe intuition

The Deflated Sharpe Ratio adjusts for:

- non-normal returns;
- skew/kurtosis;
- sample length;
- number of trials;
- selection bias.

Operating rule:

```text
if strategy only survives on naive Sharpe, reject
if costs make Sharpe collapse, reject
if out-of-sample Sharpe << in-sample Sharpe, assume overfit
```

## Purging and embargo

When labels overlap through time, train/test leakage can occur even if timestamps differ. Use purging and embargo around test periods when signals have holding periods.

```text
purge training samples whose labels overlap test labels
embargo samples immediately after test period
```

## Paper-to-live transition

A strategy is not live-ready until it has:

- cost model;
- order sizing rule;
- risk limits;
- kill-switch;
- monitoring plan;
- postmortem schema;
- small-capital pilot.

## Sources

- Bailey and López de Prado, "The Deflated Sharpe Ratio" (2014): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551
- Bailey et al., backtest overfitting / probability of backtest overfitting: https://arxiv.org/pdf/1408.1159
- "All that Glitters Is Not Gold" backtest vs out-of-sample performance: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2745220

Related: [[research-eval-harness]], [[source-quality]], [[trade-journal-dataset]], [[time-series-momentum-and-trend-following]], [[mean-reversion-cointegration-and-spreads]].
