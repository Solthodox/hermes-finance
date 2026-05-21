<p align="center">
  <img src="assets/banner.png" alt="Hermes Finance" width="100%">
</p>

# Hermes Finance ☤

<p align="center">
  <a href="https://solthodox.github.io/hermes-finance/docs/"><img src="https://img.shields.io/badge/Docs-Hermes--Finance-FFD700?style=for-the-badge" alt="Documentation"></a>
  <a href="https://discord.gg/NousResearch"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://github.com/Solthodox/hermes-finance/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://nousresearch.com"><img src="https://img.shields.io/badge/Built%20by-Nous%20Research-blueviolet?style=for-the-badge" alt="Built by Nous Research"></a>
  <a href="README.zh-CN.md"><img src="https://img.shields.io/badge/Lang-中文-red?style=for-the-badge" alt="中文"></a>
</p>

**The pragmatic, analytic finance AI agent forked from Hermes Agent by [Nous Research](https://nousresearch.com).** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM.

Use any model you want — [Nous Portal](https://portal.nousresearch.com), [OpenRouter](https://openrouter.ai) (200+ models), [NVIDIA NIM](https://build.nvidia.com) (Nemotron), [Xiaomi MiMo](https://platform.xiaomimimo.com), [z.ai/GLM](https://z.ai), [Kimi/Moonshot](https://platform.moonshot.ai), [MiniMax](https://www.minimax.io), [Hugging Face](https://huggingface.co), OpenAI, or your own endpoint. Switch with `hermes-finance model` — no code changes, no lock-in.

<table>
<tr><td><b>A real terminal interface</b></td><td>Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output.</td></tr>
<tr><td><b>Lives where you do</b></td><td>Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity.</td></tr>
<tr><td><b>A closed learning loop</b></td><td>Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. <a href="https://github.com/plastic-labs/honcho">Honcho</a> dialectic user modeling. Compatible with the <a href="https://agentskills.io">agentskills.io</a> open standard.</td></tr>
<tr><td><b>Scheduled automations</b></td><td>Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended.</td></tr>
<tr><td><b>Delegates and parallelizes</b></td><td>Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns.</td></tr>
<tr><td><b>Runs anywhere, not just your laptop</b></td><td>Seven terminal backends — local, Docker, SSH, Singularity, Modal, Daytona, and Vercel Sandbox. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand, costing nearly nothing between sessions. Run it on a $5 VPS or a GPU cluster.</td></tr>
<tr><td><b>Research-ready</b></td><td>Batch trajectory generation, Atropos RL environments, trajectory compression for training the next generation of tool-calling models.</td></tr>
</table>

---

## Quick Install

### Linux, macOS, WSL2, Termux

```bash
curl -fsSL https://raw.githubusercontent.com/Solthodox/hermes-finance/main/scripts/install.sh | bash
```

### Windows (native, PowerShell) — Early Beta

> **Heads up:** Native Windows support is **early beta**. It installs and runs, but hasn't been road-tested as broadly as our Linux/macOS/WSL2 paths. Please [file issues](https://github.com/Solthodox/hermes-finance/issues) when you hit rough edges. For the most battle-tested Windows setup today, run the Linux/macOS one-liner above inside **WSL2**.

Run this in PowerShell:

```powershell
irm https://raw.githubusercontent.com/Solthodox/hermes-finance/main/scripts/install.ps1 | iex
```

The installer handles everything: uv, Python 3.11, Node.js, ripgrep, ffmpeg, **and a portable Git Bash** (MinGit, unpacked to `%LOCALAPPDATA%\hermes-finance\git` — no admin required, completely isolated from any system Git install).  Hermes Finance uses this bundled Git Bash to run shell commands.

If you already have Git installed, the installer detects it and uses that instead.  Otherwise a ~45MB MinGit download is all you need — it won't touch or interfere with any system Git.

> **Android / Termux:** The tested manual path is documented in the [Termux guide](https://solthodox.github.io/hermes-finance/docs/getting-started/termux). On Termux, Hermes Finance installs a curated `.[termux]` extra because the full `.[all]` extra currently pulls Android-incompatible voice dependencies.
>
> **Windows:** Native Windows is supported as an **early beta** — the PowerShell one-liner above installs everything, but expect rough edges and please file issues when you hit them. If you'd rather use WSL2 (our most battle-tested Windows path), the Linux command works there too. Native Windows install lives under `%LOCALAPPDATA%\hermes-finance`; WSL2 installs under `~/.hermes-finance` on Linux/macOS-style setups.  The only Hermes Finance feature that currently needs WSL2 specifically is the browser-based dashboard chat pane (it uses a POSIX PTY — classic CLI and gateway both run natively).

After installation:

```bash
source ~/.bashrc    # reload shell (or: source ~/.zshrc)
hermes-finance      # start chatting!
```

---

## Hermes Finance Distribution

This repository is **Hermes Finance**: an open-source, finance-specialized Hermes distribution with:

- an isolated `HERMES_HOME`;
- a pragmatic, analytic finance persona;
- finance/trading/research skills;
- MCP defaults for vault access, CoinGecko, Firecrawl, Exa, Alpha Vantage, Polymarket, Hyperliquid, Alpaca, and optional Obsidian REST API;
- a seed Obsidian LLMWiki with trading math, execution, calibration, and risk notes.

Hermes Finance is meant to install cleanly for any operator without bundling private memory, addresses, balances, or personal credentials.

### Install Hermes Finance

From this repository root:

```bash
python3 -m venv venv
venv/bin/python -m pip install --upgrade pip setuptools wheel
venv/bin/python -m pip install -e '.[mcp]'
venv/bin/python scripts/install-hermes-finance-profile.py
```

Defaults:

- home: `~/.hermes-finance`
- wrapper: `~/.local/bin/hermes-finance`
- vault root: `$OBSIDIAN_VAULT`, otherwise `~/Vault`
- finance wiki folder: `<vault root>/Hermes-Finance`

If your vault lives elsewhere:

```bash
venv/bin/python scripts/install-hermes-finance-profile.py --vault-root "$HOME/Documents/Obsidian Vault"
```

Or install into an exact folder:

```bash
venv/bin/python scripts/install-hermes-finance-profile.py --vault "$HOME/Documents/Obsidian Vault/Projects/Hermes-Finance"
```

After install:

```bash
hermes-finance
```

Credentials start empty in `~/.hermes-finance/.env`. Check readiness with:

```bash
~/.hermes-finance/scripts/check_mcp_readiness.py
~/.hermes-finance/scripts/enable_ready_mcps.py --dry-run
```

Direct trading MCPs are live-fire once enabled. They remain disabled by default and require explicit operator action.

## Getting Started

```bash
hermes-finance      # Interactive CLI — start a conversation
hermes-finance model        # Choose your LLM provider and model
hermes-finance tools        # Configure which tools are enabled
hermes-finance config set   # Set individual config values
hermes-finance gateway      # Start the messaging gateway (Telegram, Discord, etc.)
hermes-finance setup        # Run the full setup wizard (configures everything at once)
hermes-finance claw migrate # Migrate from OpenClaw (if coming from OpenClaw)
hermes-finance update       # Update to the latest version
hermes-finance doctor       # Diagnose any issues
```

📖 **[Full documentation →](https://solthodox.github.io/hermes-finance/docs/)**

## CLI vs Messaging Quick Reference

Hermes has two entry points: start the terminal UI with `hermes`, or run the gateway and talk to it from Telegram, Discord, Slack, WhatsApp, Signal, or Email. Once you're in a conversation, many slash commands are shared across both interfaces.

| Action | CLI | Messaging platforms |
|---------|-----|---------------------|
| Start chatting | `hermes` | Run `hermes gateway setup` + `hermes gateway start`, then send the bot a message |
| Start fresh conversation | `/new` or `/reset` | `/new` or `/reset` |
| Change model | `/model [provider:model]` | `/model [provider:model]` |
| Set a personality | `/personality [name]` | `/personality [name]` |
| Retry or undo the last turn | `/retry`, `/undo` | `/retry`, `/undo` |
| Compress context / check usage | `/compress`, `/usage`, `/insights [--days N]` | `/compress`, `/usage`, `/insights [days]` |
| Browse skills | `/skills` or `/<skill-name>` | `/<skill-name>` |
| Interrupt current work | `Ctrl+C` or send a new message | `/stop` or send a new message |
| Platform-specific status | `/platforms` | `/status`, `/sethome` |

For the full command lists, see the [CLI guide](https://solthodox.github.io/hermes-finance/docs/user-guide/cli) and the [Messaging Gateway guide](https://solthodox.github.io/hermes-finance/docs/user-guide/messaging).

---

## Documentation

Documentation lives at **[solthodox.github.io/hermes-finance/docs](https://solthodox.github.io/hermes-finance/docs/)**:

| Section | What's Covered |
|---------|---------------|
| [Quickstart](https://solthodox.github.io/hermes-finance/docs/getting-started/quickstart) | Install → setup → first conversation in 2 minutes |
| [CLI Usage](https://solthodox.github.io/hermes-finance/docs/user-guide/cli) | Commands, keybindings, personalities, sessions |
| [Configuration](https://solthodox.github.io/hermes-finance/docs/user-guide/configuration) | Config file, providers, models, all options |
| [Messaging Gateway](https://solthodox.github.io/hermes-finance/docs/user-guide/messaging) | Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant |
| [Security](https://solthodox.github.io/hermes-finance/docs/user-guide/security) | Command approval, DM pairing, container isolation |
| [Tools & Toolsets](https://solthodox.github.io/hermes-finance/docs/user-guide/features/tools) | 40+ tools, toolset system, terminal backends |
| [Skills System](https://solthodox.github.io/hermes-finance/docs/user-guide/features/skills) | Procedural memory, Skills Hub, creating skills |
| [Memory](https://solthodox.github.io/hermes-finance/docs/user-guide/features/memory) | Persistent memory, user profiles, best practices |
| [MCP Integration](https://solthodox.github.io/hermes-finance/docs/user-guide/features/mcp) | Connect any MCP server for extended capabilities |
| [Cron Scheduling](https://solthodox.github.io/hermes-finance/docs/user-guide/features/cron) | Scheduled tasks with platform delivery |
| [Context Files](https://solthodox.github.io/hermes-finance/docs/user-guide/features/context-files) | Project context that shapes every conversation |
| [Architecture](https://solthodox.github.io/hermes-finance/docs/developer-guide/architecture) | Project structure, agent loop, key classes |
| [Contributing](https://solthodox.github.io/hermes-finance/docs/developer-guide/contributing) | Development setup, PR process, code style |
| [CLI Reference](https://solthodox.github.io/hermes-finance/docs/reference/cli-commands) | All commands and flags |
| [Environment Variables](https://solthodox.github.io/hermes-finance/docs/reference/environment-variables) | Complete env var reference |

---

## Migrating from OpenClaw

If you're coming from OpenClaw, Hermes Finance can automatically import your settings, memories, skills, and API keys.

**During first-time setup:** The setup wizard (`hermes-finance setup`) automatically detects `~/.openclaw` and offers to migrate before configuration begins.

**Anytime after install:**

```bash
hermes-finance claw migrate              # Interactive migration (full preset)
hermes-finance claw migrate --dry-run    # Preview what would be migrated
hermes-finance claw migrate --preset user-data   # Migrate without secrets
hermes-finance claw migrate --overwrite  # Overwrite existing conflicts
```

What gets imported:
- **SOUL.md** — persona file
- **Memories** — MEMORY.md and USER.md entries
- **Skills** — user-created skills → `~/.hermes-finance/skills/openclaw-imports/`
- **Command allowlist** — approval patterns
- **Messaging settings** — platform configs, allowed users, working directory
- **API keys** — allowlisted secrets (Telegram, OpenRouter, OpenAI, Anthropic, ElevenLabs)
- **TTS assets** — workspace audio files
- **Workspace instructions** — AGENTS.md (with `--workspace-target`)

See `hermes-finance claw migrate --help` for all options, or use the `openclaw-migration` skill for an interactive agent-guided migration with dry-run previews.

---

## Contributing

We welcome contributions! See the [Contributing Guide](https://solthodox.github.io/hermes-finance/docs/developer-guide/contributing) for development setup, code style, and PR process.

Quick start for contributors — clone and go with `setup-hermes.sh`:

```bash
git clone https://github.com/Solthodox/hermes-finance.git
cd hermes-finance
./setup-hermes.sh     # installs uv, creates venv, installs .[all], symlinks ~/.local/bin/hermes-finance
./hermes-finance      # auto-detects the venv, no need to `source` first
```

Manual path (equivalent to the above):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[all,dev]"
scripts/run_tests.sh
```

> **RL Training (optional):** The RL/Atropos integration (`environments/`) — see [`CONTRIBUTING.md`](https://github.com/Solthodox/hermes-finance/blob/main/CONTRIBUTING.md#development-setup) for the full setup.

---

## Community

- 💬 [Discord](https://discord.gg/NousResearch)
- 📚 [Skills Hub](https://agentskills.io)
- 🐛 [Issues](https://github.com/Solthodox/hermes-finance/issues)
- 🔌 [HermesClaw](https://github.com/AaronWong1999/hermesclaw) — Community WeChat bridge: Run Hermes Finance and OpenClaw on the same WeChat account.

---

## License

MIT — see [LICENSE](LICENSE).

Built by [Nous Research](https://nousresearch.com).
