#!/usr/bin/env python3
"""Install/update hermes-finance from codebase templates.

The repository is the source of truth. This installer renders templates into a
user-specific isolated HERMES_HOME and into the user's Obsidian vault.

Defaults:
- home: ~/.hermes-finance
- vault root: $OBSIDIAN_VAULT, else ~/Vault
- finance wiki folder: <vault root>/Hermes-Finance

No secrets are copied from any existing Hermes profile. Existing .env is
preserved unless --reset-env is passed.
"""
from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TEMPLATES = REPO / "hermes_finance_templates"
HOME_TEMPLATE = TEMPLATES / "home"
VAULT_TEMPLATE = TEMPLATES / "obsidian-vault"
DEFAULT_HOME = Path.home() / ".hermes-finance"
DEFAULT_VAULT_ROOT = Path(os.environ.get("OBSIDIAN_VAULT", Path.home() / "Vault"))
DEFAULT_WRAPPER = Path.home() / ".local" / "bin" / "hermes-finance"
DEFAULT_REPOS_DIR = Path(os.environ.get("HERMES_FINANCE_REPOS_DIR", Path.home() / "repos"))
ROOT_SKILL_DIRS = [
    REPO / "skills" / "finance",
    REPO / "skills" / "crypto",
    REPO / "skills" / "note-taking" / "finance-obsidian-vault",
    REPO / "skills" / "research" / "source-quality",
]
ROOT_HELPER_SCRIPTS_DIR = REPO / "scripts" / "hermes_finance"

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".json", ".sh", ".txt", ".ts", ".toml"}
TEXT_NAMES = {".env", ".env.example", "AGENTS.md", "SOUL.md"}

CREDENTIAL_ENV_KEYS = [
    "DEEPSEEK_API_KEY", "ZAI_API_KEY", "Z_AI_API_KEY", "GLM_API_KEY", "OPENROUTER_API_KEY",
    "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "ANTHROPIC_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN",
    "GOOGLE_API_KEY", "GEMINI_API_KEY", "EXA_API_KEY", "FIRECRAWL_API_KEY",
    "ALPHA_VANTAGE_API_KEY", "COINGECKO_DEMO_API_KEY", "COINGECKO_PRO_API_KEY",
    "POLYMARKET_PRIVATE_KEY", "POLYMARKET_FUNDER", "POLYMARKET_API_KEY",
    "POLYMARKET_API_SECRET", "POLYMARKET_PASSPHRASE", "HYPERLIQUID_PRIVATE_KEY",
    "HYPERLIQUID_ACCOUNT_ADDRESS", "HYPERLIQUID_VAULT_ADDRESS", "ALPACA_API_KEY",
    "ALPACA_SECRET_KEY", "OBSIDIAN_API_KEY",
]


def is_text_file(path: Path) -> bool:
    return path.name in TEXT_NAMES or path.suffix.lower() in TEXT_SUFFIXES


def replacements(home: Path, vault: Path, repos_dir: Path) -> dict[str, str]:
    return {
        "{{HERMES_FINANCE_HOME}}": str(home),
        "{{HERMES_FINANCE_VAULT}}": str(vault),
        "{{HERMES_FINANCE_REPO}}": str(REPO),
        "{{USER_REPOS_DIR}}": str(repos_dir),
    }


def render_text(text: str, repl: dict[str, str]) -> str:
    for key, value in repl.items():
        text = text.replace(key, value)
    return text


def copy_tree_render(src: Path, dst: Path, *, preserve_env: bool, repl: dict[str, str]) -> None:
    for item in src.rglob("*"):
        rel = item.relative_to(src)
        if any(part == "__pycache__" for part in rel.parts):
            continue
        target = dst / rel
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        if preserve_env and rel == Path(".env") and target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        if is_text_file(item):
            try:
                rendered = render_text(item.read_text(encoding="utf-8"), repl)
            except UnicodeDecodeError:
                shutil.copy2(item, target)
            else:
                target.write_text(rendered, encoding="utf-8")
                shutil.copymode(item, target)
        else:
            shutil.copy2(item, target)

def install_root_skills(home: Path, *, repl: dict[str, str]) -> None:
    skills_root = home / "skills"
    skills_root.mkdir(parents=True, exist_ok=True)
    for src in ROOT_SKILL_DIRS:
        if not src.exists():
            continue
        if src.is_dir() and (src / "SKILL.md").exists():
            rel = src.relative_to(REPO / "skills")
            copy_tree_render(src, skills_root / rel, preserve_env=False, repl=repl)
            continue
        for skill_dir in src.iterdir():
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                rel = skill_dir.relative_to(REPO / "skills")
                copy_tree_render(skill_dir, skills_root / rel, preserve_env=False, repl=repl)


def install_root_helper_scripts(home: Path, *, repl: dict[str, str]) -> None:
    scripts_root = home / "scripts"
    scripts_root.mkdir(parents=True, exist_ok=True)
    if ROOT_HELPER_SCRIPTS_DIR.exists():
        copy_tree_render(ROOT_HELPER_SCRIPTS_DIR, scripts_root, preserve_env=False, repl=repl)


def write_wrapper(path: Path, home: Path) -> None:
    unset_lines = "\n".join(f"unset {key}" for key in CREDENTIAL_ENV_KEYS)
    content = (
        "#!/usr/bin/env bash\n"
        "unset PYTHONPATH\n"
        "unset PYTHONHOME\n"
        f"# hermes-finance starts credential-empty by design. Put keys in {home}/.env.\n"
        f"{unset_lines}\n"
        f"export HERMES_HOME=\"{home}\"\n"
        f"export HERMES_OPTIONAL_SKILLS=\"{REPO}/optional-skills\"\n"
        f"exec \"{REPO}/venv/bin/hermes-finance\" \"$@\"\n"
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    os.chmod(path, 0o755)


def main() -> int:
    ap = argparse.ArgumentParser(description="Install hermes-finance home, vault wiki, wrapper, skills, MCP config, and helper scripts.")
    ap.add_argument("--home", type=Path, default=DEFAULT_HOME, help="isolated HERMES_HOME to install into")
    ap.add_argument("--vault-root", type=Path, default=DEFAULT_VAULT_ROOT, help="Obsidian vault root; Hermes-Finance folder is created inside it")
    ap.add_argument("--vault", type=Path, default=None, help="exact Hermes-Finance wiki folder; overrides --vault-root")
    ap.add_argument("--repos-dir", type=Path, default=DEFAULT_REPOS_DIR, help="optional local trading repos directory referenced by skills")
    ap.add_argument("--wrapper", type=Path, default=DEFAULT_WRAPPER, help="command wrapper path")
    ap.add_argument("--reset-env", action="store_true", help="overwrite existing .env with empty template")
    ap.add_argument("--skip-vault", action="store_true", help="install home/wrapper only")
    args = ap.parse_args()

    vault = args.vault if args.vault is not None else args.vault_root / "Hermes-Finance"
    repl = replacements(args.home.expanduser(), vault.expanduser(), args.repos_dir.expanduser())

    if not HOME_TEMPLATE.exists():
        raise SystemExit(f"missing home template: {HOME_TEMPLATE}")
    if not VAULT_TEMPLATE.exists():
        raise SystemExit(f"missing vault template: {VAULT_TEMPLATE}")

    args.home.expanduser().mkdir(parents=True, exist_ok=True)
    copy_tree_render(HOME_TEMPLATE, args.home.expanduser(), preserve_env=not args.reset_env, repl=repl)
    install_root_skills(args.home.expanduser(), repl=repl)
    install_root_helper_scripts(args.home.expanduser(), repl=repl)
    for sub in ["logs", "sessions", "state", "cache", "workspace"]:
        (args.home.expanduser() / sub).mkdir(parents=True, exist_ok=True)

    write_wrapper(args.wrapper.expanduser(), args.home.expanduser())

    if not args.skip_vault:
        vault.expanduser().mkdir(parents=True, exist_ok=True)
        copy_tree_render(VAULT_TEMPLATE, vault.expanduser(), preserve_env=False, repl=repl)

    print(f"installed hermes-finance home: {args.home.expanduser()}")
    print(f"installed wrapper: {args.wrapper.expanduser()}")
    if not args.skip_vault:
        print(f"installed/updated vault wiki: {vault.expanduser()}")
    print("credentials were not copied; fill .env manually before enabling credentialed MCPs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
