# Project Status

> Last updated: 2026-07-06

This repository contains one alpha CAP-Digest draft profile and one
non-normative CAP-Core draft proposal area.

| Area | Path | Status | Normative? | Notes |
|---|---|---:|---:|---|
| CAP-Digest overview and specification | `specs/digest/` | alpha draft | yes | Current active specification work; `cap-digest-0.1.0-alpha` is tagged. |
| CAP-Core | `specs/core/` | draft proposal + executable fixture prototypes | no | Integrated RFC-0001 overview, split draft RFCs, schema sketches, local-analysis and build-test fixtures, and validator/renderer; no stable conformance. |
| Design and research notes | `notes/` | analysis | no | Non-normative material only. |
| JSON schemas | `schemas/` | draft | yes when marked active | CAP-Digest schemas and CAP-Core schema sketches. |
| Conformance fixtures | `fixtures/` | draft | yes when marked active | CAP-Digest basic, negative, follow-up, pack, and security fixtures plus CAP-Core local-analysis fixture. |
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
CAP-Digest 0.1.0-alpha release tagged as cap-digest-0.1.0-alpha
CAP-Core draft-track reader/assembly/run-evidence validator for local-analysis and build-test
```

The first fixture paths are:

```text
schemas/cap.manifest.v1.schema.json
fixtures/basic-table/
fixtures/digest-text-negative/
fixtures/followup-basic/
fixtures/pack-table-basic/
fixtures/security-adversarial/
RELEASE-CHECKLIST.md
reference/python/
schemas/core/
fixtures/core/local-analysis/
fixtures/core/build-test/
reference/python/cap_core/
```
