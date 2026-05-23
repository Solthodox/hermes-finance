---
id: index
title: Hermes Finance Index
type: index
tags: [llmwiki, obsidian, research]
status: seed
created: 2026-05-20
updated: 2026-05-23
source_quality: seed-synthesis
---

# Hermes Finance Index

This is the routing table for Hermes Finance. It indexes 125 notes plus itself. Read this first, then follow only the links needed for the current decision or research task.

## Start here

- [[agent-operating-manual]] — operating discipline and trading guardrails.
- [[llmwiki-standard]] — how this vault stays clean.
- [[risk-management-framework]] — capital preservation rules.
- [[research-to-trade-pipeline]] — evidence to execution pipeline.
- [[decision-record-template]] — use before trade execution.
- [[mcp-readiness-check]] — verify tools and credentials.
- [[SCHEMA]] — schema and taxonomy.
- [[log]] — append-only vault history.

## _meta

- [[ingestion-playbook]] — Procedure for turning raw articles, papers, API dumps, and trade logs into durable notes.
- [[lint-checklist]] — Checklist for keeping the vault navigable, cited, indexed, and free of stale operational clutter.
- [[source-quality]] — Ranks evidence by proximity to primary data, recency, incentives, reproducibility, and adversarial robustness.

## raw

- [[market-data-mcp-source-cards]] — Primary-source setup and safety notes for CoinGecko, Alpha Vantage, Exa, and Firecrawl MCP usage.
- [[trading-venue-api-source-cards]] — Primary-source setup and safety notes for Polymarket CLOB and Hyperliquid API usage.
- [[position-sizing-and-portfolio-theory-source-cards]] — Canonical literature cards for Kelly sizing, Markowitz allocation, Black-Litterman intuition, and robust portfolios.
- [[market-microstructure-and-execution-source-cards]] — Canonical literature cards for spreads, adverse selection, price impact, market making, and optimal execution.
- [[raw-data-dictionary]] — Data dictionary for seed JSON/CSV fixtures under `raw/api-dumps/` and `raw/assets/`.

## concepts

- [[airdrops-research]] — A disciplined process for finding and triaging airdrop opportunities without overfitting social hype.
- [[claim-evidence-probability-ev]] — Connects claims to evidence, converts evidence into calibrated probabilities or return distributions, and prices expected value after costs.
- [[bayesian-updating-for-trade-theses]] — Bayesian odds, likelihood ratios, evidence independence, and Beta-binomial calibration for updating trade probabilities.
- [[commodities-and-oil]] — Energy and commodity drivers relevant to inflation, geopolitics, currencies, and sector trades.
- [[comps-analysis]] — Comparable company and transaction multiple analysis with quality controls.
- [[crypto-equity-correlation]] — Tracks when crypto behaves as high-beta risk asset vs idiosyncratic network/flow trade.
- [[dcf-modeling]] — Discounted cash flow model steps, assumptions, sensitivity tables, and sanity checks.
- [[defillama-research]] — TVL, yield, protocol revenue, stablecoin flows, bridges, unlocks, and chain-level activity checks.
- [[earnings-analysis]] — How to analyze earnings calls, estimates, guidance, revisions, margins, and market reaction.
- [[financial-statements-quality]] — Accounting red flags, cash conversion, working capital, share-based compensation, and non-GAAP adjustments.
- [[geckoterminal-onchain-data]] — Onchain pool prices, liquidity, volume, and token metadata through CoinGecko tooling.
- [[jupiter-routing]] — Solana swap routing, quote freshness, slippage controls, token accounts, and failed-route handling.
- [[liquidity-pools]] — AMM liquidity, slippage, routing, LP concentration, impermanent loss, and pool-manipulation hazards.
- [[llmwiki-standard]] — Karpathy-style LLMWiki rules for raw immutable sources, synthesized wiki notes, schema, index, log, ingest, query, and lint operations.
- [[mean-reversion-cointegration-and-spreads]] — Mean reversion, z-scores, OU half-life, cointegration, and spread-trading failure modes.
- [[macro-calendar]] — Process for CPI, FOMC, payrolls, GDP, auctions, and other calendar risk.
- [[options-implied-volatility]] — Volatility basics for event pricing, skew, term structure, and avoiding option-premium traps.
- [[time-series-momentum-and-trend-following]] — Cross-sectional/time-series momentum, EMA/breakout signals, volatility scaling, and no-signal diagnostics.
- [[rates-and-dollar]] — How rates, real yields, dollar liquidity, and policy expectations affect risk assets.
- [[rugcheck-process]] — Checklist for token safety before any small-cap onchain trade.
- [[sec-filings]] — Primary-source workflow for 10-K, 10-Q, 8-K, S-1, proxy, and insider filings.
- [[stablecoin-and-bridge-risk]] — Stablecoin depeg, bridge exploit, chain halt, and custody risks that affect crypto portfolio safety.
- [[token-contract-risk]] — Contract-level token risks: mint authority, blacklist, transfer taxes, ownership, proxies, and liquidity locks.
- [[wallet-clustering]] — How to interpret wallet clusters, copy-trade candidates, sybil behavior, and common attribution mistakes.
- [[yahoo-finance-fallback]] — Fallback source for basic market data when primary paid APIs are unavailable, with quality caveats.

## datasets

- [[market-research-dataset]] — Schema for source snapshots, probabilities, EV estimates, and outcomes.
- [[orderbook-snapshot-dataset]] — Schema for saving orderbook snapshots used in decisions so spread/slippage assumptions can be audited.
- [[prediction-calibration-dataset]] — Dataset structure for comparing predicted probabilities to realized binary outcomes.
- [[trade-journal-dataset]] — Schema for recording decisions, fills, exits, errors, and postmortems for later calibration.
- [[whale-flow-dataset]] — Schema for whale trades, wallet labels, market categories, and outcome attribution.

## decisions

- [[decision-record-template]] — Template for recording a trade recommendation, live state, evidence, EV, sizing, approvals, and invalidation rules.

## entities

- [[cron-job-map]] — Map of scheduled jobs, intended autonomy boundaries, delivery channels, and risk posture.
- [[current-portfolio-state]] — Pointer page for live portfolio checks; never trust this page as a current balance unless the snapshot is freshly dated.
- [[hermes-finance-fork]] — Identity, paths, runtime, home, vault, skills, and MCP configuration for this fork.
- [[hyperliquid-agent-repo]] — Local repo inventory and operational notes for the deterministic Hyperliquid trading agent.
- [[polymarket-agent-repo]] — Local repo inventory and operational notes for the deterministic Polymarket trading agent.
- [[solana-sniper-repo]] — Local repo inventory and operational notes for Solana copy-trading/sniping tools.
- [[tracked-whales]] — Watchlist structure for wallets/traders worth monitoring, with evidence requirements and anti-copy-trade cautions.

## markets

- [[agent-wallet-mode]] — How agent wallets sign for Hyperliquid accounts and what addresses must match before live orders.
- [[avoiding-crypto-prediction-markets]] — Why many crypto price prediction markets are efficient, correlated with spot, and poor for discretionary edge.
- [[avoiding-sports-markets]] — Why sports markets often lack edge after vig and expert bookmakers, unless a specific structural inefficiency is identified.
- [[binary-market-arbitrage]] — Ways to inspect yes/no mispricings, related-market inconsistencies, and basket constraints without assuming free money.
- [[bracket-orders]] — Atomic entry plus take-profit and stop-loss pattern for reducing naked-position risk.
- [[clob-trade-netting]] — How to reconstruct true ownership and PnL from chronological BUY/SELL events rather than stale UI snapshots.
- [[dead-mans-switch]] — Kill-switch ideas for stale sessions, broken bots, naked positions, repeated API failures, and missing protective orders.
- [[early-geopolitical-strategy]] — Strategy for geopolitics and policy markets before consensus fully prices new evidence.
- [[ema20-breakout-strategy]] — Current swing strategy concept using EMA trend, breakout window, volume confirmation, and protective orders.
- [[endgame-scalping]] — Late-stage prediction market playbook for high-probability outcomes where liquidity and rule certainty dominate.
- [[favorite-longshot-bias]] — Bias pattern where tails can be overpriced or underpriced depending on trader attention, entertainment value, and liquidity.
- [[funding-rates]] — How funding can create carry opportunities or silently eat expected value.
- [[geopolitical-contrarian-strategy]] — Polymarket strategy cluster for asymmetric geopolitical bets priced below fair probability with strong catalyst research.
- [[hyperliquid-account-architecture]] — Main account, agent/API wallets, unified account caveats, vaults, and what must be verified before trading.
- [[hyperliquid-direct-mcp-safety]] — Safety protocol for direct Hyperliquid MCP usage: live account verification, leverage budget, open-order reconciliation, bracket protection.
- [[hyperliquid-exchange]] — Overview of Hyperliquid perps, account state, order lifecycle, margin, funding, and venue-specific risks.
- [[leverage-and-liquidation]] — Liquidation math, maintenance margin, isolated vs cross exposure, and why small stop failures can become account-level events.
- [[manual-close-and-no-reentry-rule]] — If the user closes a thesis manually, do not re-enter the cluster without explicit approval and fresh evidence.
- [[market-rules-and-resolution]] — Rules-first approach to market analysis: read criteria, source-of-truth, deadlines, ambiguity, and resolution gameability.
- [[momentum-political-strategy]] — Momentum rules for political markets with high probability, clear catalysts, and disciplined smaller sizing.
- [[neg-risk-markets]] — Explains neg-risk market structure, token relationships, resolution constraints, and why naïve single-token analysis can be wrong.
- [[no-signal-diagnostic]] — How to diagnose quiet strategy cycles instead of assuming no opportunity exists.
- [[open-orders-verification]] — Always reconcile open orders before placing or modifying trades to avoid duplicate exposure.
- [[order-types]] — Market, limit, trigger, reduce-only, post-only, IOC/ALO/GTC semantics and when each is appropriate.
- [[orderbook-and-spread-analysis]] — Checklist for live orderbook inspection, spread buffers, depth, hidden liquidity, and stale best-price hazards.
- [[limit-order-book-microstructure]] — Bid/ask mechanics, microprice, adverse selection, queue priority, and Avellaneda-Stoikov/Kyle/Glosten-Milgrom intuition.
- [[perpetuals-basics]] — Perp contract fundamentals: leverage, margin, funding, liquidation, index prices, and mark prices.
- [[polymarket-clob]] — Orderbook mechanics for prediction markets: token IDs, tick sizes, bids/asks, depth, partial fills, and CLOB API risks.
- [[polymarket-direct-mcp-safety]] — Safety protocol for direct Polymarket MCP order placement: explicit approval, live positions, max loss, and logged decision record.
- [[polymarket-platform]] — Core platform model: binary outcome tokens, UMA-style resolution, CLOB execution, fees, and portfolio accounting.
- [[post-trade-protection]] — After any fill, verify protective orders exist, sizes match, and stop/take-profit prices obey exchange constraints.
- [[prediction-market-calibration]] — How to compare market-implied odds with base rates, expert forecasts, and resolution criteria.
- [[tick-size-rounding]] — Venue-specific tick sizes must be derived and applied to every limit and trigger order.
- [[triggerpx-float-bug]] — Known bug pattern: triggerPx must be numeric float, not string, in Hyperliquid SDK signing path.
- [[whale-tracking]] — Framework for using large trader flows as evidence without blindly copy-trading or confusing liquidity provision with conviction.

## playbooks

- [[agent-operating-manual]] — Default operating manual for Hermes Finance: preserve capital, verify live state, log durable knowledge, and separate research from execution.
- [[citation-policy]] — Rules for citing sources, marking stale claims, distinguishing primary data from commentary, and avoiding source laundering.
- [[research-to-trade-pipeline]] — A repeatable pipeline from question framing through evidence gathering, fair odds, expected value, sizing, execution, and review.
- [[source-triangulation]] — How to corroborate a market claim across primary sources, APIs, independent reporting, orderflow, and historical base rates.
- [[backtesting-overfitting-and-research-hygiene]] — Lookahead, survivorship, data snooping, walk-forward validation, deflated Sharpe, and paper-to-live rules.

## postmortems

- [[postmortem-template]] — Template for reviewing closed trades, missed trades, bad fills, rule violations, and process improvements.

## risk

- [[correlation-and-cluster-risk]] — Prevents hidden overexposure to one macro event, political thesis, asset, exchange, or liquidity regime.
- [[daily-loss-guard]] — Defines hard daily loss caps, cool-down requirements, and escalation rules.
- [[drawdown-control]] — Defines how to slow down, pause, or cut size after realized losses or evidence of model decay.
- [[execution-checklist]] — Final pre-trade checklist: live state, open orders, market rules, EV, size, kill-switch, and logging.
- [[expected-value]] — A trade is acceptable only when probability-weighted payoff remains positive after fees, spreads, slippage, borrow/funding, and model error.
- [[fees-spread-and-edge-hurdle]] — Sets minimum edge thresholds after transaction costs and spread crossing.
- [[fractional-kelly]] — Uses Kelly as an upper bound and then cuts size for estimation error, liquidity, psychological risk, and correlated exposure.
- [[kill-switch-policy]] — Conditions that require disabling automation or direct order tools immediately.
- [[leverage-budget]] — Limits gross, net, and per-position leverage so liquidation risk never hides behind nominal margin.
- [[liquidity-and-slippage]] — Analyzes orderbook depth, spread, fill probability, market impact, and stale snapshot risk before execution.
- [[robust-portfolio-construction]] — Markowitz, covariance shrinkage, risk contribution, Black-Litterman intuition, and robust cluster sizing.
- [[volatility-forecasting-and-regime-detection]] — Realized/EWMA/range/GARCH volatility, regime features, vol targeting, and kill-switch triggers.
- [[portfolio-exposure-ledger]] — A durable ledger schema for tracking current and stale-prone exposures by account, venue, thesis, and strategy.
- [[position-sizing]] — Converts edge and risk into notional size while respecting account caps, market depth, max loss, and thesis confidence.
- [[risk-management-framework]] — Preserve capital with hard risk limits, small initial sizing, correlated exposure controls, and explicit stop conditions.
- [[risk-of-ruin]] — Explains how losing streaks, fat tails, leverage, and correlation can bankrupt a strategy with positive average edge.
- [[stale-state-policy]] — Rules for rejecting old balances, old orderbooks, old market rules, and old news.

## strategies

- [[automation-boundaries]] — Boundaries between deterministic scheduled agents, interactive recommendations, direct MCP tools, and research-only workflows.
- [[optimal-execution-and-slippage]] — Implementation shortfall, Almgren-Chriss execution tradeoffs, slippage budgets, and limit-vs-market rules.
- [[manual-approval-protocol]] — When Hermes Finance must ask the operator before moving money or modifying live exposure.
- [[no-trade-decision]] — No-trade is an active decision when edge is unclear, costs are high, state is stale, or portfolio risk is full.
- [[post-entry-monitoring]] — What to monitor after entry: price, news, rule changes, liquidity, protective orders, and thesis health.
- [[small-bet-discovery]] — Rules for tiny exploratory bets when evidence is promising but uncertainty remains high.
- [[thesis-invalidation]] — Defines what evidence would prove a trade idea wrong before or after entry.

## tools

- [[alpha-vantage-mcp]] — Official market data MCP for real-time and historical equity, FX, crypto, macro, and technical indicators.
- [[alphavantage-mcp-setup]] — Credential and setup notes for enabling official Alpha Vantage market data tools.
- [[autoresearch-loop]] — Karpathy-style automated improvement loop adapted for financial research: propose, test, score, keep or discard.
- [[coingecko-mcp]] — Official crypto market data MCP for prices, market cap, OHLCV, onchain GeckoTerminal data, trends, and metadata.
- [[dexscreener-api]] — DEX pair discovery, liquidity snapshots, price action, and social metadata for token research.
- [[exa-mcp]] — Research MCP for web search, code search, company research, and source discovery.
- [[firecrawl-mcp]] — Scraping/search/deep-research MCP for turning messy web pages into cleaner structured evidence.
- [[hyperliquid-mcp-risk-review]] — Direct Hyperliquid MCP capabilities and the specific risk review required before using order tools.
- [[mcp-readiness-check]] — How to verify binaries, credentials, enabled flags, and tool discovery without placing trades.
- [[obsidian-mcp]] — Optional Local REST API MCP for reading, searching, patching, and appending Obsidian notes.
- [[polymarket-mcp-direct]] — Direct Polymarket MCP capabilities and the safety gates required before order placement.
- [[research-eval-harness]] — How to score research outputs for correctness, source quality, prediction calibration, and decision usefulness.
- [[solana-sniper-tool]] — Local Solana sniper repository capabilities, safety checks, wallet verification, and why rug filters matter.
- [[web-source-snapshotting]] — When to preserve raw web pages, API responses, and screenshots so future reasoning can audit the evidence trail.
