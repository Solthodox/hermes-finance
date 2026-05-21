---
name: portfolio-risk
description: Apply portfolio exposure, sizing, drawdown, liquidity, correlation, and kill-switch checks before finance decisions.
tags: [finance, portfolio, risk, trading]
---

# Portfolio Risk

Use for any task that can affect exposure, position size, leverage, cash, or risk concentration.

## Mandatory checks

- Verify live positions, balances, open orders, and pending automation before changing exposure.
- Classify exposure by venue, asset, thesis, event, strategy, and liquidity regime.
- Check max order size, max market exposure, daily loss, total exposure, and leverage budget.
- Treat stale snapshots as invalid. If the data is not live, say so and do not execute.
- For correlated theses, size the cluster, not just the individual instrument.
- If any protective order is missing after a Hyperliquid fill, prioritize risk repair over new trades.

Write durable risk lessons to `{{HERMES_FINANCE_VAULT}}/risk/` and exposure snapshots to `{{HERMES_FINANCE_VAULT}}/entities/current-portfolio-state.md` only with dates and stale caveats.
