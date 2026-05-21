---
name: finance-obsidian-vault
description: Maintain Hermes Finance's Obsidian LLMWiki vault cleanly: index-first reads, raw/source separation, lintable notes, and decision logging.
tags: [obsidian, llmwiki, note-taking, finance]
---

# Finance Obsidian Vault

Vault path: `{{HERMES_FINANCE_VAULT}}`.

## Session start

Read `{{HERMES_FINANCE_VAULT}}/index.md` first. Use it as the table of contents and only open the notes needed for the current task.

## Write protocol

- Raw captures go under `raw/` and are not rewritten.
- Synthesized notes go under the relevant content directory with frontmatter, H1, summary, tags from `SCHEMA.md`, wikilinks, and source notes.
- Every new or renamed note must be added to `index.md`.
- Append vault events to `log.md`; do not rewrite history.
- Decisions go under `decisions/`; outcomes and errors go under `postmortems/`.
- Never store secrets, private keys, seed phrases, API keys, or full auth tokens in Obsidian.

Run `{{HERMES_FINANCE_HOME}}/scripts/finance_vault_lint.py` after substantive vault edits.
