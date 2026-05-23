# Hermes Finance Home Instructions

- Always read `{{HERMES_FINANCE_VAULT}}/index.md` before finance/trading/research work.
- Keep the LLMWiki clean: raw sources in `raw/`, synthesized notes indexed, decisions logged, secrets excluded.
- Direct trading MCPs are live-fire once enabled; no order without live-state verification, risk checks, decision record, and required operator approval.
- Credentials start empty in `{{HERMES_FINANCE_HOME}}/.env`; never copy secrets from other profiles.
- Never read, source, grep, or reuse `~/.hermes/.env`, `~/.hermes/config.yaml`, default Hermes logs, or default Hermes credentials. Hermes Finance must use only `{{HERMES_FINANCE_HOME}}/.env` for secrets.
- For Telegram, use the finance-local `tg` helper on PATH. If `TELEGRAM_BOT_TOKEN` and `TELEGRAM_HOME_CHANNEL` are absent from `{{HERMES_FINANCE_HOME}}/.env`, report that Telegram is not configured; do not fall back to default Hermes.
