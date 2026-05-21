#!/usr/bin/env python3
from __future__ import annotations
import argparse
import re
from pathlib import Path

VAULT = Path('{{HERMES_FINANCE_VAULT}}')

def main() -> int:
    ap = argparse.ArgumentParser(description='Search Hermes Finance Obsidian vault markdown files.')
    ap.add_argument('query', help='case-insensitive regex or plain text')
    ap.add_argument('--limit', type=int, default=40)
    args = ap.parse_args()
    try:
        rx = re.compile(args.query, re.I)
    except re.error:
        rx = re.compile(re.escape(args.query), re.I)
    hits = 0
    for p in sorted(VAULT.rglob('*.md')):
        text = p.read_text(encoding='utf-8', errors='replace')
        for n, line in enumerate(text.splitlines(), 1):
            if rx.search(line):
                print(f'{p.relative_to(VAULT)}:{n}: {line[:240]}')
                hits += 1
                if hits >= args.limit:
                    return 0
    if hits == 0:
        print('no matches')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
