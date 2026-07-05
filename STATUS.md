# Project Status

> Last updated: 2026-07-05

This repository contains one drafted CAP-Digest profile and one non-normative
CAP-Core draft proposal area.

| Area | Path | Status | Normative? | Notes |
|---|---|---:|---:|---|
| CAP-Digest overview and specification | `specs/digest/` | draft | yes | Current active specification work. |
| CAP-Core | `specs/core/` | draft proposal | no | RFC-0001 draft and supporting planning material; no stable conformance. |
| Design and research notes | `notes/` | analysis | no | Non-normative material only. |
| JSON schemas | `schemas/` | draft/planned | yes when marked active | Initial schemas are being introduced to support conformance. |
| Conformance fixtures | `fixtures/` | draft/planned | yes when marked active | Fixtures define executable expectations for implementations. |
| Digest packs | `packs/` | draft/planned | yes when marked active | Packs distribute reusable source-reading logic for CAP-Digest. |
| Reference implementation | `reference/` | experimental | no | Executable companion to test fixtures; not the specification itself. |
| CAPP process | `capps/` | draft | yes for accepted CAPPs | Normative changes should route through this process when required. |

## Layer rule

Every change should answer:

> Is this refining CAP-Digest, or does it actually belong in CAP-Core?

CAP-Core content must remain non-normative until a future CAPP accepts Core
schemas, fixtures, and conformance language.

## Current implementation target

The current executable target is:

```text
CAP-Digest Level 0/1 for one source type: table
```

The first conformance path is:

```text
schemas/cap.manifest.v1.schema.json
fixtures/basic-table/
reference/python/
```
