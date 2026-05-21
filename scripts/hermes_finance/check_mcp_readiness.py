#!/usr/bin/env python3
from __future__ import annotations
import os
import re
import shutil
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
    'alpaca': ['ALPACA_API_KEY','ALPACA_SECRET_KEY'],
    'obsidian': ['OBSIDIAN_API_KEY'],
}
COMMANDS = {
    'finance_vault': ['npx'],
    'coingecko': ['npx'],
    'firecrawl': ['npx'],
    'exa': ['npx'],
    'alphavantage': ['uvx'],
    'polymarket': ['npx'],
    'hyperliquid': ['uvx'],
    'alpaca': ['uvx'],
    'obsidian': ['uvx'],
}

def load_env() -> dict[str,str]:
    out = {}
    if ENV.exists():
        for raw in ENV.read_text(encoding='utf-8').splitlines():
            line = raw.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k,v = line.split('=',1)
            out[k.strip()] = v.strip().strip('"\'')
    return out

def enabled_map() -> dict[str,bool]:
    txt = CONFIG.read_text(encoding='utf-8') if CONFIG.exists() else ''
    out = {}
    current = None
    for line in txt.splitlines():
        m = re.match(r'^  ([A-Za-z0-9_]+):\s*$', line)
        if m:
            current = m.group(1); out.setdefault(current, True); continue
        if current:
            m = re.match(r'^    enabled:\s*(true|false)\s*$', line, re.I)
            if m:
                out[current] = (m.group(1).lower() == 'true')
    return out

def main() -> int:
    env = load_env()
    enabled = enabled_map()
    print(f'Hermes Finance MCP readiness ({HOME})')
    failures = 0
    for name in sorted(COMMANDS):
        bins = COMMANDS[name]
        missing_bins = [b for b in bins if shutil.which(b) is None]
        req = REQUIRED.get(name, [])
        missing_keys = [k for k in req if not env.get(k)]
        status = 'enabled' if enabled.get(name, False) else 'disabled'
        bits = [status]
        bits.append('bins ok' if not missing_bins else 'missing bins: ' + ','.join(missing_bins))
        if req:
            bits.append('creds ok' if not missing_keys else 'missing creds: ' + ','.join(missing_keys))
        else:
            bits.append('no creds required')
        if enabled.get(name, False) and (missing_bins or missing_keys):
            failures += 1
            verdict = 'BLOCK'
        elif missing_bins or missing_keys:
            verdict = 'pending'
        else:
            verdict = 'ready'
        print(f"- {name}: {verdict} ({'; '.join(bits)})")
    return 1 if failures else 0

if __name__ == '__main__':
    raise SystemExit(main())
