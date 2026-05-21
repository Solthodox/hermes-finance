#!/usr/bin/env python3
"""Load hermes-finance .env, verify required vars, and exec an MCP server.

Usage:
  mcp_env_exec.py --require KEY [--require OTHER] -- command arg ...
"""
from __future__ import annotations

import os
import re
import shlex
import sys
from pathlib import Path

HOME = Path('{{HERMES_FINANCE_HOME}}')
ENV_PATH = HOME / '.env'


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for raw in path.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        key = key.strip()
        value = value.strip()
        if not key or not re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', key):
            continue
        if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
            try:
                value = shlex.split(value)[0]
            except Exception:
                value = value[1:-1]
        os.environ[key] = value


def main(argv: list[str]) -> int:
    load_env(ENV_PATH)
    required: list[str] = []
    command: list[str] = []
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == '--':
            command = argv[i + 1:]
            break
        if arg == '--require':
            i += 1
            if i >= len(argv):
                print('mcp_env_exec: --require needs a variable name', file=sys.stderr)
                return 64
            required.append(argv[i])
        else:
            print(f'mcp_env_exec: unknown argument before --: {arg}', file=sys.stderr)
            return 64
        i += 1
    if not command:
        print('mcp_env_exec: missing command after --', file=sys.stderr)
        return 64
    missing = [key for key in required if not os.environ.get(key, '').strip() or os.environ.get(key, '').strip().startswith('${')]
    if missing:
        print(
            'mcp_env_exec: missing required credential(s): ' + ', '.join(missing) +
            f'. Fill {ENV_PATH} and enable the MCP server in config.yaml only when ready.',
            file=sys.stderr,
        )
        return 78
    expanded = [os.path.expandvars(part) for part in command]
    os.execvp(expanded[0], expanded)
    return 127


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
