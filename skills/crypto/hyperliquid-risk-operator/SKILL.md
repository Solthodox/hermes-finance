---
name: hyperliquid-risk-operator
description: Operate Hyperliquid research and direct tools with leverage, liquidation, order, tick-size, and bracket-order discipline.
tags: [crypto, hyperliquid, trading, perpetuals, risk]
---

# Hyperliquid Risk Operator

Use for Hyperliquid market research, agent diagnostics, strategy tuning, or direct MCP operations.

## Required checks before any order

- Connectivity and account/agent wallet validity.
- Live balances, positions, leverage, margin, open orders, and fills.
- Asset metadata, size decimals, tick size, and order constraints.
- Bracket/protective order plan before or at entry.
- Max loss, liquidation distance, funding, correlation, and daily loss guard.
- Decision record in `{{HERMES_FINANCE_VAULT}}/decisions/`.

Known hazards: `triggerPx` must be float, tick-size rounding is venue-specific, TP/SL strict inequalities matter, and failed protective orders leave naked positions.
