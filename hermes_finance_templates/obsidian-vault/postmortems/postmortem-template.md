---
id: postmortem-template
title: Postmortem Template
type: template
tags: [postmortem, risk, trading]
status: seed
created: 2026-05-20
updated: 2026-05-20
source_quality: seed-synthesis
---

# Postmortem Template

Template for reviewing closed trades, missed trades, bad fills, rule violations, and process improvements.

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

[[decision-record-template]], [[manual-close-and-no-reentry-rule]], [[drawdown-control]]

## Source notes

Seeded from Hermes Finance setup plan and reviewed public documentation where applicable; replace or extend with raw source captures during future ingest.
