# CAP-Core Status and Roadmap

> Status: CAP-Core v1.0.0 stable status page - Last updated: 2026-07-07

This page standardizes how CAP-Core pages describe their status after
CAPP-0007 accepted CAP-Core v1.0.0 stable.

## Status Terms

| Term | Meaning | Current examples |
|---|---|---|
| Draft proposal | Design text under review. It may change without compatibility promises. | `RFC-0001.md`, `RFC-0001-core-object-model.md` |
| Draft profile proposal | Profile-owned constraints over Core records. It does not change minimal Core. | `RFC-0003-scientific-computation-profile.md`, `RFC-0004-cap-digest-bridge-profile.md` |
| Candidate-prep draft | Historical executable review material prepared before CAPP-0007. | `CONFORMANCE-DRAFT.md`, `SCHEMA-CANDIDATE-RULES.md` |
| Stable v1.0 | Accepted minimal Core object contract, schema package, fixtures, reports, and maintenance policy. | `STABLE-SCOPE-v1.0.md`, `CONFORMANCE-v1.0.md`, `release-artifacts/cap-core-v1.0.0/` |
| Normative | Accepted specification text or schema with explicit governance status. | CAP-Core v1.0.0 stable docs and schemas cited by CAPP-0007 |

## Current Scope

CAP-Core v1.0.0 covers the minimal Core object model, binding envelope, schema
package, positive and negative fixtures, validator codes, renderer/report
formats, conformance reports, interop evidence, and maintenance policy.

CAP-Digest remains the active digest profile. CAP-Core bridge material can
reference CAP-Digest views, but it does not alter digest text grammar,
DigestManifest semantics, or follow-up gate behavior.

## Stability Boundaries

- Core object schemas under `schemas/core/` are the v1.0 schema package.
- Core fixtures under `fixtures/core/` are the v1.0 release fixture corpus.
- Validator and renderer outputs are reference evidence for conformance and
  interoperability reports; the specification remains the accepted docs and
  schemas.
- Profiles and bindings may add stricter rules only in their own namespace.
- CAP-Core v1.0.0 still excludes runtime execution, policy language semantics,
  credential exchange, scientific correctness, and CAP-Digest behavior changes.

## Roadmap Link

Phase 9 completed the stable release path tracked by issues #61 and #62.
The accepted stable release is recorded in `capps/CAPP-0007-cap-core-v1.0.0-stable-release.md`,
`ROADMAP.md`, `STATUS.md`, and `release-artifacts/cap-core-v1.0.0/`.
