---
id: SCHEMA
title: Hermes Finance LLMWiki Schema
type: schema
tags: [llmwiki, obsidian, research]
status: seed
created: 2026-05-20
updated: 2026-05-20
source_quality: seed-synthesis
---

# Hermes Finance LLMWiki Schema

This vault follows the LLMWiki pattern: raw material is immutable, wiki pages are curated syntheses, `index.md` is the routing table, and `log.md` is append-only operational history.

## Directory contract

- `raw/`: immutable source captures, API dumps, papers, articles, screenshots, and exports.
- `_meta/`: schema, lint, ingestion, and source-quality guidance.
- `entities/`: accounts, repos, wallets, venues, agents, and named systems.
- `concepts/`: durable explanatory notes.
- `playbooks/`: step-by-step procedures.
- `strategies/`: trading/research strategies and boundary rules.
- `risk/`: limits, sizing, failure modes, and portfolio controls.
- `tools/`: APIs, MCPs, scripts, and local repositories.
- `markets/`: venue-specific and market-structure notes.
- `decisions/`: trade and research decision records.
- `postmortems/`: outcome reviews.
- `datasets/`: schemas and pointers for structured evidence.

## Required frontmatter

Every Markdown note must include `id`, `title`, `type`, `tags`, `status`, `created`, `updated`, and `source_quality`.

## Tag taxonomy

`#finance`, `#trading`, `#risk`, `#polymarket`, `#hyperliquid`, `#crypto`, `#onchain`, `#tradfi`, `#macro`, `#research`, `#tool`, `#llmwiki`, `#decision`, `#postmortem`, `#strategy`, `#execution`, `#market-data`, `#source-quality`, `#portfolio`, `#mcp`, `#obsidian`, `#entity`, `#dataset`

## Operations

- Ingest: save raw material under `raw/`, then synthesize into the smallest relevant wiki page.
- Query: read `index.md`, then only the linked notes needed for the task.
- Lint: check frontmatter, index coverage, valid tags, and resolvable wikilinks.
- Log: append durable vault events to `log.md`; do not rewrite history.

Related: [[llmwiki-standard]], [[ingestion-playbook]], [[lint-checklist]], [[source-quality]].
