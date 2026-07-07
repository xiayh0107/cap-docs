# Project Status

> Last updated: 2026-07-07

This repository contains CAP-Digest v1.0.0 stable artifacts and CAP-Core
v1.0.0 stable artifacts.

| Area | Path | Status | Normative? | Notes |
|---|---|---:|---:|---|
| CAP-Digest overview and specification | `specs/digest/` | v1.0.0 stable | yes | CAPP-0009 accepted fixture-scoped CAP-Digest v1.0.0. Release artifact: `release-artifacts/cap-digest-v1.0.0/`; tag plan: `cap-digest-v1.0.0`. |
| CAP-Core | `specs/core/` | v1.0.0 stable | yes | CAPP-0007 accepted CAP-Core v1.0.0 stable for the minimal control-plane object contract. Release artifact: `release-artifacts/cap-core-v1.0.0/`; tag: `cap-core-v1.0.0`. |
| Design and research notes | `notes/` | analysis | no | Non-normative material only. |
| JSON schemas | `schemas/` | mixed | yes when marked active | CAP-Digest draft schemas plus CAP-Core v1.0 schemas under `schemas/core/`. |
| Conformance fixtures | `fixtures/` | mixed | yes when marked active | CAP-Digest basic, negative, follow-up, pack, and security fixtures plus CAP-Core v1.0 positive and negative fixture suites. |
| Digest packs | `packs/` | draft | yes when marked active | `table-basic` has field metadata, renderer notes, redactor notes, and pack fixture coverage. |
| Reference implementation | `reference/` | experimental | no | Executable companion to test fixtures; not the specification itself. |
| CAPP process | `capps/` | draft | yes for accepted CAPPs | Normative changes should route through this process when required. |

## Layer rule

Every change should answer:

> Is this refining CAP-Digest, or does it actually belong in CAP-Core?

CAP-Core v1.0.0 covers minimal Core records and conformance evidence only. It
does not define runtime execution, policy language semantics, credential
exchange, scientific correctness, or CAP-Digest behavior changes.

## Post-release maintenance

The initial post-release maintenance pass is recorded in
`specs/core/reviews/2026-07-07-post-release-maintenance-audit.md`. It is normal
maintenance, not expansion of the CAP-Core v1.0.0 stability claim:

- [#88](https://github.com/xiayh0107/cap-docs/issues/88) tracks v1.0.x errata
  and patch releases under `specs/core/MAINTENANCE-v1.0.md`; the initial audit
  found no open errata requiring a patch release.
- [#89](https://github.com/xiayh0107/cap-docs/issues/89) tracks real external
  implementation feedback for L4 interoperability; the initial feedback window
  closed with no external reports received.
- [#90](https://github.com/xiayh0107/cap-docs/issues/90) tracks Core v1.0.0
  boundary hygiene; the initial audit keeps out-of-scope layers excluded.
- [#91](https://github.com/xiayh0107/cap-docs/issues/91) tracks layer
  separation; #92 is the independent Digest stable tracker.

CAP-Digest v1.0.0 stable uses Digest-specific gates documented in
`specs/digest/STABLE-TRACK.md` and must not be bundled into Core v1.0.x
maintenance.

## Current implementation target

The current executable targets are:

```text
CAP-Digest Level 0/1 for one source type: table
CAP-Digest Level 2 follow-up gate for table sample rows
CAP-Digest Level 3 table-basic pack metadata loading
CAP-Digest v1.0.0 stable release package and reports
CAP-Digest 0.1.0-alpha historical release tagged as cap-digest-0.1.0-alpha
CAP-Core v1.0.0 L0-L4 conformance reports and release package
```

Key executable paths are:

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
fixtures/core/remote-service-binding/
fixtures/core/negative/
reference/python/cap_core/
release-artifacts/core-candidate-review/
release-artifacts/cap-core-v1.0.0-rc1/
release-artifacts/cap-core-v1.0.0/
release-artifacts/cap-digest-v1.0.0-rc1/
release-artifacts/cap-digest-v1.0.0/
```
