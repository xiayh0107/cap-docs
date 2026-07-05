# Schemas (Planned)

> Status: planned · Last updated: 2026-07-05

This directory will hold machine-readable JSON schemas for the CAP-Digest
artifact family. It currently contains **no schema files**; the list below is a
planning sketch derived from `specs/digest/`. Schemas will be added alongside a
reference implementation and conformance fixtures.

## Planned v1 schemas

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

Schema versioning and feature-state rules will follow
`specs/digest/11-versioning-conformance-governance.md`.