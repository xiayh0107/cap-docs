# Schemas

> Status: draft · Last updated: 2026-07-06

This directory holds machine-readable JSON schemas for CAP-Digest plus
Core-scoped schema sketches for CAP-Core. These schemas are draft assets unless
a CAPP marks a specific schema as active.

Schemas use JSON Schema Draft 2020-12. The schema dialect follows
[JSON-SCHEMA-2020-12] in `../REFERENCES.md`.

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
- `cap.validation_result.v1.schema.json` — mechanical validation result for a
  ContractResponse.
- `cap.gate_result.v1.schema.json` — gate decisions for follow-up requests.
- `cap.field.v1.schema.json` — serialized field definition.
- `cap.field_catalog.v1.schema.json` — field catalog aggregate.
- `cap.digest_pack.v1.schema.json` — Digest Pack `CAP.md` frontmatter.
- `cap.pack_conformance_report.v1.schema.json` — Digest Pack conformance report.
- `cap.conformance_report.v1.schema.json` — the fixture/check report emitted by
  the reference implementation.

## CAP-Core draft schema sketches

Core schema sketches live under `schemas/core/`:

- `cap.core.artifact.v1.schema.json` — Artifact / ArtifactRef envelope.
- `cap.core.artifact_set.v1.schema.json` — fixture and assembly artifact-set wrapper.
- `cap.core.capability.v1.schema.json` — Capability declaration.
- `cap.core.binding.v1.schema.json` — generic typed Binding envelope.
- `cap.core.assembly.v1.schema.json` — pre-run Assembly contract.
- `cap.core.policy_decision.v1.schema.json` — minimal policy decision record.
- `cap.core.run.v1.schema.json` — Run record.
- `cap.core.run_evidence.v1.schema.json` — RunEvidence envelope.

These sketches align with `specs/core/RFC-0001.md` and
the split draft RFCs under `specs/core/`. They are exercised by
`fixtures/core/local-analysis/` and `fixtures/core/build-test/`. They are not
stable CAP-Core conformance requirements.

Schema versioning and feature-state rules will follow
`specs/digest/11-versioning-conformance-governance.md`.
