---
id: yahoo-finance-fallback
title: Yahoo Finance Fallback
type: concept
tags: [tradfi, macro, market-data]
status: seed
created: 2026-05-20
updated: 2026-05-20
source_quality: seed-synthesis
---

# Yahoo Finance Fallback

Fallback source for basic market data when primary paid APIs are unavailable, with quality caveats.

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

[[source-triangulation]], [[expected-value]], [[risk-management-framework]]

## Source notes

Seeded from Hermes Finance setup plan and reviewed public documentation where applicable; replace or extend with raw source captures during future ingest.
