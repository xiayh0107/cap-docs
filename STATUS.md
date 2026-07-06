# Project Status

> Last updated: 2026-07-05

This repository contains one drafted CAP-Digest profile and one non-normative
CAP-Core draft proposal area.

| Area | Path | Status | Normative? | Notes |
|---|---|---:|---:|---|
| CAP-Digest overview and specification | `specs/digest/` | draft | yes | Current active specification work. |
| CAP-Core | `specs/core/` | draft proposal + executable fixture prototype | no | RFC-0001 draft, schema sketches, local-analysis fixture, and validator/renderer; no stable conformance. |
| Design and research notes | `notes/` | analysis | no | Non-normative material only. |
| JSON schemas | `schemas/` | draft | yes when marked active | CAP-Digest schemas and CAP-Core schema sketches. |
| Conformance fixtures | `fixtures/` | draft | yes when marked active | CAP-Digest basic-table fixture and CAP-Core local-analysis fixture. |
| Digest packs | `packs/` | draft | yes when marked active | `table-basic` has field metadata, renderer notes, redactor notes, and pack fixture coverage. |
| Reference implementation | `reference/` | experimental | no | Executable companion to test fixtures; not the specification itself. |
| CAPP process | `capps/` | draft | yes for accepted CAPPs | Normative changes should route through this process when required. |

## Layer rule

Every change should answer:

> Is this refining CAP-Digest, or does it actually belong in CAP-Core?

CAP-Core content must remain non-normative until a future CAPP accepts Core
schemas, fixtures, and conformance language.

## Current implementation target

The current executable targets are:

```text
CAP-Digest Level 0/1 for one source type: table
CAP-Digest Level 2 follow-up gate for table sample rows
CAP-Digest Level 3 table-basic pack metadata loading
CAP-Core draft-track reader/assembly/run-evidence validator for local-analysis
```

The first fixture paths are:

```text
schemas/cap.manifest.v1.schema.json
fixtures/basic-table/
fixtures/followup-basic/
fixtures/pack-table-basic/
reference/python/
schemas/core/
fixtures/core/local-analysis/
reference/python/cap_core/
```
