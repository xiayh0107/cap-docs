# CAPP-0007: CAP-Core v1.0.0 Stable Release

> Status: accepted - Created: 2026-07-07 - Layer: CAP-Core

## Abstract

This CAPP accepts publication of CAP-Core v1.0.0 stable with release artifact
`release-artifacts/cap-core-v1.0.0/` and tag `cap-core-v1.0.0`.

## Motivation

Stable-track issue #62 and child issues #63-#87 completed the governance,
scope, conformance, schema, fixture, validator, renderer, security,
interoperability, release-candidate, and maintenance gates needed for a stable
CAP-Core v1.0.0 release.

## Specification

Publish CAP-Core v1.0.0 for the minimal Core object set frozen in
`specs/core/STABLE-SCOPE-v1.0.md`. The stable release includes:

- stable v1.0 documents under `specs/core/`;
- schemas under `schemas/core/`;
- positive and negative fixtures under `fixtures/core/`;
- conformance, inspection, L3, interop, and L4 comparison reports;
- maintenance and compatibility policy;
- release artifact package and tag.

## Rationale

The release is limited to structural Core records and conformance evidence. It
does not define runtime execution or external policy/service semantics.

## Compatibility

Compatibility is governed by `specs/core/SCHEMA-PACKAGE-v1.0.md` and
`specs/core/MAINTENANCE-v1.0.md`. v1.0.x updates may clarify or correct without
breaking stable required fields, enum meanings, report shapes, or security
findings.

## Security and Privacy

Security requirements are defined in `specs/core/SECURITY-v1.0.md`. Inline
secret values, missing policy evidence, stale service bindings, undeclared
network access, RunEvidence/DigestEvidence collapse, and evidence overclaims are
stable findings.

## Reference Implementation

The Python reference implementation emits v1.0 conformance reports, inspection
reports, interop reports, and stable finding codes. It remains an executable
companion, not the specification itself.

## Conformance Fixtures

Stable fixtures are indexed by `specs/core/FIXTURES-v1.0.md` and packaged under
the release artifact.

## CAP-Digest Impact

CAP-Digest behavior is unchanged. DigestBinding remains a CAP-Digest bridge
profile boundary and does not alter digest text grammar, DigestManifest
semantics, or follow-up gates.

## Release Plan

- Artifact: `release-artifacts/cap-core-v1.0.0/`
- Tag: `cap-core-v1.0.0`
- Correction path: `specs/core/MAINTENANCE-v1.0.md`
