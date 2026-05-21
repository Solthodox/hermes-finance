#!/usr/bin/env python3
"""Enable hermes-finance MCP servers only when required credentials exist.

By default this enables research/data servers only. Trading servers require
--include-trading so a credential typo cannot silently turn on live-fire tools.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

HOME = Path('{{HERMES_FINANCE_HOME}}')
CONFIG = HOME / 'config.yaml'
ENV = HOME / '.env'
REQUIRED = {
    'firecrawl': ['FIRECRAWL_API_KEY'],
    'exa': ['EXA_API_KEY'],
    'alphavantage': ['ALPHA_VANTAGE_API_KEY'],
    'polymarket': ['POLYMARKET_PRIVATE_KEY'],
    'hyperliquid': ['HYPERLIQUID_PRIVATE_KEY'],
    'alpaca': ['ALPACA_API_KEY', 'ALPACA_SECRET_KEY'],
    'obsidian': ['OBSIDIAN_API_KEY'],
}
TRADING = {'polymarket', 'hyperliquid', 'alpaca'}
ALWAYS_ENABLED = {'finance_vault', 'coingecko'}


def load_env() -> dict[str, str]:
    out: dict[str, str] = {}
    if not ENV.exists():
        return out
    for raw in ENV.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        out[key.strip()] = value.strip().strip('"\'')
    return out


def has_creds(name: str, env: dict[str, str]) -> bool:
    return all(env.get(key, '').strip() and not env.get(key, '').strip().startswith('${') for key in REQUIRED.get(name, []))


def rewrite_enabled(text: str, enabled: dict[str, bool]) -> str:
    lines = text.splitlines()
    out: list[str] = []
    current: str | None = None
    for line in lines:
        m = re.match(r'^(  )([A-Za-z0-9_]+):(\s*)$', line)
        if m:
            current = m.group(2)
            out.append(line)
            continue
        m = re.match(r'^(    enabled:\s*)(true|false)(\s*)$', line, re.I)
        if current in enabled and m:
            out.append(f"{m.group(1)}{'true' if enabled[current] else 'false'}{m.group(3)}")
            continue
        out.append(line)
    return '\n'.join(out) + '\n'


def main() -> int:
    ap = argparse.ArgumentParser(description='Enable ready hermes-finance MCP servers.')
    ap.add_argument('--include-trading', action='store_true', help='also enable Polymarket/Hyperliquid/Alpaca when credentials exist')
    ap.add_argument('--dry-run', action='store_true', help='show changes without writing config.yaml')
    args = ap.parse_args()

    env = load_env()
    text = CONFIG.read_text(encoding='utf-8')
    server_names = re.findall(r'^  ([A-Za-z0-9_]+):\s*$', text, flags=re.M)
    desired: dict[str, bool] = {}
    for name in server_names:
        if name in ALWAYS_ENABLED:
            desired[name] = True
        elif name in REQUIRED:
            ready = has_creds(name, env)
            if name in TRADING and not args.include_trading:
                desired[name] = False
            else:
                desired[name] = ready
    new_text = rewrite_enabled(text, desired)
    for name in server_names:
        if name not in desired:
            continue
        reason = 'always-on' if name in ALWAYS_ENABLED else 'credentials present' if desired[name] else 'missing credentials or trading not requested'
        print(f"{name}: {'enable' if desired[name] else 'disable'} ({reason})")
    if args.dry_run:
        return 0
    if new_text != text:
        CONFIG.write_text(new_text, encoding='utf-8')
        print(f'updated {CONFIG}')
    else:
        print('no changes')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
