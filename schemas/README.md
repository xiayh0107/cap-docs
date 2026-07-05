# Schemas

> Status: draft · Last updated: 2026-07-05

This directory holds machine-readable JSON schemas for the CAP-Digest artifact
family. Schemas use JSON Schema Draft 2020-12.

## v1 schemas

- `cap.digest.v1.schema.json` — digest object envelope.
- `cap.manifest.v1.schema.json` — DigestManifest structure.
- `cap.contract_response.v1.schema.json` — structured model contract response.
- `cap.validation_result.v1.schema.json` — mechanical validation result for a ContractResponse.
- `cap.gate_result.v1.schema.json` — gate decisions for follow-up requests.
- `cap.digest_patch.v1.schema.json` — typed digest patch operations.
- `cap.field.v1.schema.json` — serialized field definition.
- `cap.field_catalog.v1.schema.json` — field catalog aggregate.
- `cap.digest_pack.v1.schema.json` — Digest Pack `CAP.md` frontmatter.
- `cap.pack_conformance_report.v1.schema.json` — Digest Pack conformance report.

## Source basis

The schema dialect follows [JSON-SCHEMA-2020-12] in `../REFERENCES.md`. Schema
versioning and feature-state rules follow `specs/digest/11-versioning-conformance-governance.md`.
