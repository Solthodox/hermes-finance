---
id: stale-state-policy
title: Stale State Policy
type: risk
tags: [risk, portfolio, trading]
status: seed
created: 2026-05-20
updated: 2026-05-20
source_quality: seed-synthesis
---

# Stale State Policy

Rules for rejecting old balances, old orderbooks, old market rules, and old news.

## Operating use

- Verify live data before using this note for a current market decision.
- Separate durable principle from stale snapshot; update the note when a repeated lesson emerges.
- Record uncertainty explicitly: confidence, base rate, source quality, and what would change the conclusion.
- If execution is involved, route through risk gates and a decision record before any order tool.

## Cleanliness rules

- Keep raw evidence in `raw/`; keep this page synthesized and current.
- Add new claims only with source notes, dates, or links to captured raw material.
- Prefer small, auditable updates over dumping transcripts or API payloads here.

## Related

[[risk-management-framework]], [[position-sizing]], [[execution-checklist]]

## Source notes

Seeded from Hermes Finance setup plan and reviewed public documentation where applicable; replace or extend with raw source captures during future ingest.
