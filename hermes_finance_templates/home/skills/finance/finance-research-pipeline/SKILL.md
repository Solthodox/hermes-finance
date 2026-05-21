---
name: finance-research-pipeline
description: Turn financial questions into evidence-backed probabilities, EV, sizing, decision records, and postmortems.
tags: [finance, research, trading, ev, risk]
---

# Finance Research Pipeline

Use this whenever the user asks for market research, trade ideas, portfolio decisions, or investment theses.

## Required flow

1. Read `{{HERMES_FINANCE_VAULT}}/index.md` and choose the smallest relevant notes.
2. Frame the question: asset/market, time horizon, venue, resolution criteria, and decision needed.
3. Gather primary or near-primary evidence first; rank sources with [[source-quality]].
4. Convert evidence to base rates and an explicit fair probability or expected return distribution.
5. Compute EV after fees, spread, slippage, funding, borrow, and model error.
6. Size with [[position-sizing]] and [[fractional-kelly]], then cap by [[risk-management-framework]].
7. If execution is possible, write/update a decision record in `{{HERMES_FINANCE_VAULT}}/decisions/` before any order.
8. After close or invalidation, write a postmortem.

No-trade is a valid output when evidence is weak, stale, contradictory, already priced, or too expensive to execute.
