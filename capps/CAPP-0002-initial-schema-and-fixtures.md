# CAPP-0002: Initial Schemas and Fixtures

> Status: implemented · Created: 2026-07-05 · Layer: CAP-Digest

## Abstract

This CAPP introduces the first machine-readable schemas and the first conformance fixture family for CAP-Digest.

## Motivation

CAP-Digest should not remain prose-only. Implementers need executable assets that answer whether a produced digest and manifest conform to the draft.

## Specification

This CAPP introduces initial draft files:

- `schemas/cap.manifest.v1.schema.json`
- `schemas/cap.contract_response.v1.schema.json`
- `schemas/cap.digest_patch.v1.schema.json`
- `schemas/cap.digest.v1.schema.json`
- `fixtures/basic-table/`

The first fixture targets a single `table` source type and tests Level 0 and Level 1 behavior:

- valid digest version line;
- selected fields with stable IDs;
- DigestManifest rows for selected and rejected fields;
- visible redaction caveats;
- escaped data fences;
- evidence validation against selected field IDs.
- negative validation cases for unknown and unselected evidence.

## Rationale

The initial scope intentionally avoids remote sources, unsafe execution, full tokenization, and CAP-Core concerns. A narrow fixture makes interoperability testable before the standard grows.

## Compatibility

These schemas are draft and may change before `0.1.0-alpha`. Breaking changes must be documented in the changelog and should update fixtures together with schemas.

## Security and Privacy

The first fixture includes a secret-like column name to test redaction behavior. Fixture data must remain synthetic and must not include real credentials or private data.

## Reference Implementation

A minimal Python reference implementation is introduced under `reference/python/` to generate and validate the basic table fixture.

## Conformance Fixtures

The initial fixture is `fixtures/basic-table/`, including
`negative-validation.json`.
