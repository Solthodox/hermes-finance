---
name: trading-pitfalls
description: Catalog of every known failure mode across Polymarket and Hyperliquid trading. Load before any trading decision to avoid repeating mistakes. Organized by platform with detection methods and fixes.
tags: [crypto, trading, pitfalls, safety, checklist, polymarket, hyperliquid]
---

# Trading Pitfalls — Complete Failure Mode Catalog

**Load this skill before any trading session.** Every entry here is a mistake that was made, debugged, and documented. The cost of not reading this is real money.

---

## Polymarket Failure Modes

### P1: NegRisk Markets Fail Silently with FAK Orders
- **Symptom:** FAK order returns `"no orders found to match"` even with orderbook depth.
- **Root cause:** `negRisk: true` markets use a different CLOB mechanism that FAK doesn't support.
- **Detection:** Filter `ev.negRisk` from Gamma API before trading. Hardcode `negRisk: false` in order params.
- **Cost if missed:** Wasted cycle, missed opportunity, agent thinks it traded but didn't.

### P2: Wide Spreads Cause FAK Rejection
- **Symptom:** FAK returns `"invalid price (0.006), min: 0.01 - max: 0.99"`.
- **Root cause:** Best bid < 0.01 or best ask > 0.99 makes the effective price fall below CLOB minimum.
- **Detection:** Before trading, verify `bestBid >= 0.01 && bestAsk <= 0.99`.
- **Cost if missed:** Blocked trade, silent failure.

### P3: Ask Price Drift Between Snapshot and Execution
- **Symptom:** Trader output: `Skip <market>: best ask X.XX above max Y.YY`.
- **Root cause:** Seconds/minutes pass between orderbook snapshot and signal file execution. Price ticks up.
- **Detection:** Always add 0.01-0.02 buffer to maxPrice above observed best ask.
- **Cost if missed:** Signal written but rejected, cycle wasted.

### P4: Stale Position Data from Context Script
- **Symptom:** `polymarket_decision_context.sh` shows a position, but `check_positions.ts` doesn't.
- **Root cause:** Data API lags behind on-chain reality. User closed position via web UI.
- **Detection:** ALWAYS run `check_positions.ts` first. Reconcile against context script output.
- **Cost if missed:** Trading into a thesis the user already exited. Violates hard rule.

### P5: Re-entering a Cluster the User Exited
- **Symptom:** Opening YES on a related market after user closed a position in the same cluster.
- **Root cause:** Treating each slug as independent when they share domain (e.g., Iran geopolitics).
- **Detection:** Count positions by tag/domain overlap. If 3+ in same cluster, no new entries.
- **Cost if missed:** User anger, capital deployed against user's judgment.

### P6: Concentration Risk Across Correlated Markets
- **Symptom:** 3+ positions in same domain (e.g., Iran, UK politics) — single news event moves all against you.
- **Detection:** Before trading, classify market domain. If it makes you 3+ deep in that cluster, reduce or pass.
- **Cost if missed:** Correlated losses, exceeds effective position limits.

### P7: Trade-History Netting Regression
- **Symptom:** After closing, a position still shows in `check_positions.ts` with doubled units or muddy avg price.
- **Root cause:** CLOB trade history must be sorted chronologically and net BUY minus SELL per condition/outcome.
- **Detection:** After any manual close, run `check_positions.ts`; fully closed markets should disappear. If they do not, fix side/timestamp parsing before trading again.
- **Cost if missed:** Inflated deployed cost, wrong concentration view, accidental re-entry into closed thesis.

### P8: Crypto Early Entry (<0.60) — Statistically Negative EV
- **Symptom:** Trading crypto markets at entry price < 0.60.
- **Root cause:** Crypto markets are too efficient — hedge funds price them before you. -33.4% ROI across 133 resolved positions.
- **Detection:** Before trading, check category. If crypto AND entry < 0.60 → SKIP.
- **Cost if missed:** Expected loss of ~1/3 of capital over time.

### P9: Contrarian Sports — Paying the Vig
- **Symptom:** Taking contrarian side on sports markets.
- **Root cause:** Sports books are efficient. Taking the other side is paying the vig. -3.9% ROI.
- **Detection:** If category is sports AND strategy is contrarian → SKIP.
- **Cost if missed:** Slow bleed, negative EV.

### P10: Mechanical YES/NO Alternation
- **Symptom:** Systematically alternating YES → NO → YES across trades.
- **Root cause:** Old agent.ts behavior. Each trade must have independent thesis.
- **Detection:** Review signal rationale. If it's just "alternating from last trade" → remove.
- **Cost if missed:** No edge trades, guaranteed negative EV over time.

### P11: Over-Trading to Be Active
- **Symptom:** Writing signals when edge is weak, just to avoid empty signal file.
- **Root cause:** Agent feels pressure to produce output. Empty signal file is valid and preferred.
- **Detection:** For each signal, ask: "Would I trade this if my own money and no reporting obligation?"
- **Cost if missed:** Death by a thousand paper cuts. Small negative EV accumulates.

### P12: Early Exit (Kills Asymmetric Upside)
- **Symptom:** Closing a position at small profit/loss before catalyst event.
- **Root cause:** Profit-lock paradox — the +81.6% ROI contrarian cohort only works because positions are HELD through catalysts.
- **Detection:** Before exiting early, check: has the catalyst event occurred? Is the thesis invalidated?
- **Cost if missed:** Converting 5:1 payoff opportunities into 1.2:1 outcomes.

---

## Hyperliquid Failure Modes

### H1: Naked Positions (Missing TP/SL)
- **Symptom:** `stop_cloid: null` or `tp1_cloid: null` in state file.
- **Root cause:** Order placement failed silently. Position is unprotected.
- **Detection:** After EVERY run, check state file for null stop_cloid/tp1_cloid. Priority is placing protection.
- **Cost if missed:** Full position loss on adverse move.

### H2: triggerPx Must Be Float, Not String
- **Symptom:** `ValueError: Unknown format code 'f' for object of type 'str'`.
- **Root cause:** SDK's `float_to_wire()` applies `f"{x:.8f}"` to triggerPx. String input breaks format.
- **Detection:** In `src/execution_engine.py`, ensure `triggerPx` is passed as raw float, never `str()`.
- **Cost if missed:** TP/SL order fails, position left naked.

### H3: TP/SL limit_px Strict Inequality
- **Symptom:** `"Invalid TP/SL price. asset=N"`.
- **Root cause:** For LONG: limit_px must be strictly LESS than triggerPx. Setting equal fails.
- **Detection:** Derive limit_px with 0.5% directional slippage, then round to tick size.
- **Cost if missed:** Protective order rejected, position naked.

### H4: Unified Account — Balance in spot_user_state
- **Symptom:** `user_state` shows $0, thinking account is empty. Actually $400 in spot clearinghouse.
- **Root cause:** Unified accounts show balance in `spot_user_state`, not `user_state` (perp).
- **Detection:** Check `spotClearinghouseState` for balance. `user_state` is meaningless for unified accounts.
- **Cost if missed:** Agent thinks it can't trade, capital sits idle. Or worse: sends usdClassTransfer (disabled).

### H5: API Wallet Not Approved
- **Symptom:** `"User or API Wallet 0x73cb... does not exist."`
- **Root cause:** User hasn't authorized the agent wallet in Hyperliquid UI (Approve Agent).
- **Detection:** Check connectivity first — agent does this automatically. If fails, guide user to https://app.hyperliquid.xyz/API.
- **Cost if missed:** All trades fail until user manually approves.

### H6: Exchange Constructor Takes wallet= Not private_key=
- **Symptom:** Import error or wrong constructor arg.
- **Root cause:** `Exchange(wallet=Account.from_key(key))`, NOT `Exchange(private_key=key)`.
- **Detection:** In client.py, verify constructor usage matches pattern.
- **Cost if missed:** Agent fails to initialize, cron cycles wasted.

### H7: Capital Idle — Operator Failure
- **Symptom:** `no_signals_this_run` across 2+ consecutive cycles, no operator intervention.
- **Root cause:** The agent is a tool, not a replacement for judgment. Operator must step in.
- **Detection:** Monitor cron output. If 2+ consecutive no-signal cycles → diagnose with curl diagnostic.
- **Cost if missed:** $400 sitting idle for days. Opportunity cost.

### H8: Price Not Rounded to Tick Size
- **Symptom:** `"Price must be divisible by tick size. asset=N"` or `"Order has invalid price."`
- **Root cause:** BTC tick=$1.00, ETH=$0.10, SOL=$0.001. Prices must be multiples.
- **Detection:** Use `MarketDataProvider._derive_tick_size()` and `round_price()` before placing orders.
- **Cost if missed:** Order rejected, position left naked or entry missed.

### H9: Weekend Trading Disabled by Default
- **Symptom:** No signals on Saturday/Sunday despite price action.
- **Root cause:** `ALLOW_WEEKEND_TRADING` defaults to `false` in config.py. Must be set to `true` in cron script.
- **Detection:** Verify cron script passes `ALLOW_WEEKEND_TRADING=true`.
- **Cost if missed:** Missing 2/7 days of trading opportunities.

### H10: Post-Trade Protection Regression
- **Symptom:** Fresh position from signal scan has no TP/SL after `execution_success`.
- **Root cause:** Regression would mean the post-trade reconciliation path stopped calling `position_manager.manage()` after execution.
- **Detection:** After `execution_success`, logs must show `post_trade_position_management_action` or live open orders for TP/SL. If not, abort new entries and fix `src/agent.py`.
- **Cost if missed:** Fresh position unprotected until next cron cycle.

### H11: Over-Sizing Without Approval
- **Symptom:** Scaling position 0.02→0.10 ETH (5x) without user approval.
- **Root cause:** Operator error — treating parameter flexibility as permission to scale.
- **Detection:** Base unit is 0.02 ETH (~$45 notional at 3x). Changes require explicit user approval.
- **Cost if missed:** Previously corrected by user. Don't repeat.

---

## Cross-Platform Failure Modes

### X1: Stale Cached State
- **Symptom:** Making decisions on data loaded >5 minutes ago.
- **Root cause:** Orderbooks, positions, and balances change. Cache lies.
- **Detection:** Reload state before every trading decision. Context script data may be stale.
- **Cost if missed:** Trading on phantom positions, wrong balances, outdated prices.

### X2: Bypassing Risk Gates for a "Good" Trade
- **Symptom:** The trade looks great, but risk gate rejects it → tempted to override or increase limits.
- **Root cause:** Every blown account started with "just this one time."
- **Detection:** If risk gate rejects → accept it. Report why. Never override for a single trade.
- **Cost if missed:** Risk gates exist because someone already lost money this way.

### X3: Not Having All Information Before Deciding
- **Symptom:** Making a trade call before fetching orderbook, positions, balance, and news.
- **Root cause:** Impatience. The market will be there in 30 seconds.
- **Detection:** Pre-trade checklist: positions ✓, orderbook ✓, balance ✓, news ✓, thesis ✓ → THEN decide.
- **Cost if missed:** Incomplete information → bad decisions → losses.

### X4: DeepSeek World Knowledge Gap
- **Symptom:** Confidently stating a fact (price, event, news) without verifying via tool call.
- **Root cause:** DeepSeek V4 Pro has SimpleQA 57.9% — significant knowledge gaps.
- **Detection:** If you didn't fetch it this session via a tool call, you don't know it. Verify.
- **Cost if missed:** Trading on hallucinated facts.

### X5: Cron Job Code/Config Modification
- **Symptom:** Editing source code, scripts, or config during a trading cron run.
- **Root cause:** Trading crons are read-only for code. Mention needed changes in report instead.
- **Detection:** Hard boundary rule. If you're about to edit a file during cron → STOP.
- **Cost if missed:** Partially-modified scripts, broken subsequent cycles, unpredictable behavior.

---

## Quick Pre-Trade Checklist

Before ANY trade signal, verify:
- [ ] Live positions checked (not stale context data)
- [ ] Category classified (geopolitical/political/crypto/sports)
- [ ] Edge computed (fair_probability - live_ask)
- [ ] Risk gates checked (order size, position size, daily loss)
- [ ] Portfolio concentration ≤2 per domain cluster
- [ ] Not re-entering user-closed cluster
- [ ] maxPrice includes 0.01-0.02 buffer above observed ask
- [ ] negRisk filtered out AND spread checks passed (bid ≥0.01, ask ≤0.99)
- [ ] Crypto at <0.60? → SKIP
- [ ] Contrarian sports? → SKIP
- [ ] Mechanical alternation? → SKIP
- [ ] Thesis written in rationale field with specific edge calculation
