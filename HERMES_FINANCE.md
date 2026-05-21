# Hermes Finance

Hermes Finance is an open-source, finance-specialized Hermes runtime fork. It ships an isolated agent home, a pragmatic/analytic finance persona, finance/trading skills, MCP configuration, helper scripts, and a seed Obsidian LLMWiki so any operator can run a dedicated financial research and risk agent without polluting their default Hermes profile.

## What it installs

The installer renders repository templates into user-specific locations:

- isolated `HERMES_HOME` with config, SOUL, memories, skills, helper scripts, cron state, and empty credential placeholders;
- a `hermes-finance` command wrapper;
- a Hermes-Finance wiki folder inside the user's Obsidian vault;
- finance/trading/research skills;
- MCP definitions for finance vault access, CoinGecko, Firecrawl, Exa, Alpha Vantage, Polymarket, Hyperliquid, Alpaca, and optional Obsidian Local REST API;
- helper scripts for vault linting/search, MCP readiness, credential-gated MCP startup, and safe MCP enablement.

## Source of truth

The repository is the source of truth:

- Home template: `hermes_finance_templates/home`
- Obsidian wiki template: `hermes_finance_templates/obsidian-vault`
- Installer: `scripts/install-hermes-finance-profile.py`
- Runtime wrapper template logic: `scripts/install-hermes-finance-profile.py`

The installed home (`~/.hermes-finance` by default) is runtime state plus user credentials. Do not commit secrets or user-specific runtime state back into the project.

## Install

From the repository root:

```bash
python3 -m venv venv
venv/bin/python -m pip install --upgrade pip setuptools wheel
venv/bin/python -m pip install -e '.[mcp]'
venv/bin/python scripts/install-hermes-finance-profile.py
```

Defaults:

- home: `~/.hermes-finance`
- wrapper: `~/.local/bin/hermes-finance`
- vault root: `$OBSIDIAN_VAULT` if set, otherwise `~/Vault`
- wiki folder: `<vault root>/Hermes-Finance`
- optional local repos directory referenced by skills: `$HERMES_FINANCE_REPOS_DIR` if set, otherwise `~/repos`

If your Obsidian vault is somewhere else:

```bash
venv/bin/python scripts/install-hermes-finance-profile.py --vault-root "$HOME/Documents/Obsidian Vault"
```

Or install into an exact folder:

```bash
venv/bin/python scripts/install-hermes-finance-profile.py --vault "$HOME/Documents/Obsidian Vault/Projects/Hermes-Finance"
```

The installer preserves an existing `~/.hermes-finance/.env` by default. Use `--reset-env` only when intentionally replacing credentials with the empty template.

## Configure credentials

Credentials start empty. Edit:

```text
~/.hermes-finance/.env
```

Then check readiness:

```bash
~/.hermes-finance/scripts/check_mcp_readiness.py
```

Enable ready research/data MCPs:

```bash
~/.hermes-finance/scripts/enable_ready_mcps.py --dry-run
~/.hermes-finance/scripts/enable_ready_mcps.py
```

Direct trading MCPs are live-fire once enabled. They require an explicit flag:

```bash
~/.hermes-finance/scripts/enable_ready_mcps.py --include-trading
```

## Run

```bash
hermes-finance
```

The wrapper sets `HERMES_HOME` to the isolated home and unsets common inherited provider/trading credential variables. Put credentials in `~/.hermes-finance/.env` instead of relying on your shell environment.

## Obsidian wiki

The installed wiki follows a Karpathy-style LLMWiki layout:

- `SCHEMA.md`
- `index.md`
- `log.md`
- `raw/`
- `_meta/`
- `entities/`
- `concepts/`
- `playbooks/`
- `strategies/`
- `risk/`
- `tools/`
- `markets/`
- `decisions/`
- `postmortems/`
- `datasets/`

The seed wiki includes math-heavy notes on Kelly sizing, Bayesian updating, prediction-market calibration, limit-order-book microstructure, optimal execution, robust portfolio construction, volatility/regime detection, momentum, mean reversion, and backtest overfitting.

Run the vault linter after edits:

```bash
~/.hermes-finance/scripts/finance_vault_lint.py
```

## Safety model

- No credentials are bundled.
- No user-specific addresses, balances, positions, or trading history are bundled.
- Trading MCPs are disabled by default.
- The wrapper clears inherited secrets before launching the agent.
- No trade should be placed during setup, diagnostics, smoke tests, or research-only tasks.
- The agent instructions require live-state verification, risk checks, decision records, and operator approval before interactive execution.

## Customization

After installation, customize:

- `~/.hermes-finance/.env` for credentials;
- `~/.hermes-finance/config.yaml` for model/provider and MCP enablement;
- the installed Obsidian wiki for operator-specific risk limits, watchlists, accounts, and postmortems;
- `~/.hermes-finance/memories/USER.md` for operator preferences.

Keep durable generic improvements in the repository templates. Keep private/user-specific facts in the installed home or local vault only.
