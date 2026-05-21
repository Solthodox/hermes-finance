---
name: polymarket-precision
description: Research Polymarket opportunities with probability calibration, CLOB checks, risk gates, and direct-MCP safety.
tags: [crypto, polymarket, trading, prediction-markets, risk]
---

# Polymarket Precision

Use for Polymarket research, recommendations, signal files, CLOB debugging, or direct MCP operations.

## Interactive rule

For user-initiated trade ideas, present the thesis, fair probability, live ask/bid, EV, size, invalidation, and proposed action; then wait for explicit user approval before writing signals or placing orders.

## Required checks

1. Verify live positions and open orders.
2. Read market rules/resolution source and deadline.
3. Inspect orderbook spread/depth and adjust max price for normal tick drift only when EV survives.
4. Classify category: geopolitics, politics, crypto, sports, macro, other.
5. Enforce no-reentry on manually closed thesis clusters unless the user explicitly reopens the idea.
6. Log a decision record in `{{HERMES_FINANCE_VAULT}}/decisions/` for executable recommendations.

If the operator maintains a deterministic Polymarket execution repo, register it under `{{USER_REPOS_DIR}}` and prefer those risk-gated scripts for scheduled execution. Direct MCP order tools are live-fire and require the same risk gates.
