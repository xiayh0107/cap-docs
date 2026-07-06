# Schemas

> Status: draft · Last updated: 2026-07-06

This directory holds machine-readable JSON schemas for CAP-Digest plus
Core-scoped schema sketches for CAP-Core. These schemas are draft assets unless
a CAPP marks a specific schema as active.

## CAP-Digest v1 schemas

- `cap.digest.v1.schema.json` — the digest text envelope (version line, source
  line, field blocks, caveats, available-on-request, contract, data fences).
  See `specs/digest/06-digest-text-format.md`.
- `cap.manifest.v1.schema.json` — the DigestManifest structure (source
  reference, version, selected/rejected fields, cost, trust/exec classes,
  redaction, warnings/errors, fingerprint, tokenizer/estimator).
  See `specs/digest/07-digest-manifest-and-evidence.md`.
- `cap.digest_patch.v1.schema.json` — a digest patch returned by the follow-up
  gate. See `specs/digest/09-followup-contract-and-gate.md`.
- `cap.contract_response.v1.schema.json` — the structured model contract
  response (cited field IDs, follow-up requests, signals).
  See `specs/digest/09-followup-contract-and-gate.md`.
- `cap.conformance_report.v1.schema.json` — the fixture/check report emitted by
  the reference implementation.

## CAP-Core draft schema sketches

Core schema sketches live under `schemas/core/`:

- `cap.core.artifact.v1.schema.json` — Artifact / ArtifactRef envelope.
- `cap.core.capability.v1.schema.json` — Capability declaration.
- `cap.core.binding.v1.schema.json` — generic typed Binding envelope.
- `cap.core.assembly.v1.schema.json` — pre-run Assembly contract.
- `cap.core.run.v1.schema.json` — Run record.
- `cap.core.run_evidence.v1.schema.json` — RunEvidence envelope.

These sketches align with `specs/core/RFC-0001.md` and
`fixtures/core/local-analysis/`. They are not stable CAP-Core conformance
requirements.

Schema versioning and feature-state rules will follow
`specs/digest/11-versioning-conformance-governance.md`.
