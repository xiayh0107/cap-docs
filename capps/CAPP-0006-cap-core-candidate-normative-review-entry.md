# CAPP-0006: CAP-Core Candidate Normative Review Entry

> Status: proposed - Created: 2026-07-07 - Layer: CAP-Core

## Abstract

This CAPP proposes that CAP-Core enter candidate normative review using the
Phase 8 evidence package. It does not publish a stable CAP-Core release, freeze
schemas as stable, or change CAP-Digest behavior.

## Motivation

CAPP-0005 defined the gates that had to be satisfied before CAP-Core could be
reviewed for candidate normative entry. Phase 8 completed those gates: schema
candidate rules, positive and negative fixtures, validator and renderer
reports, security review, profile and binding governance, terminology audit,
interop harness, candidate review package, readiness report, and CI coverage.

The readiness report recommends entering candidate normative review while
keeping Core assets draft-track until a future CAPP accepts promotion.

## Specification

Open candidate normative review for the minimal CAP-Core candidate set:

```text
ArtifactSet
Artifact / ArtifactRef
Capability
Binding
Assembly
PolicyDecision
Run
RunEvidence
DigestBinding as a CAP-Digest bridge profile
```

The review is scoped to the evidence in:

- `capps/CAPP-0005-cap-core-candidate-normative-track.md`
- `specs/core/reviews/2026-07-07-candidate-readiness.md`
- `release-artifacts/core-candidate-review/`
- `schemas/core/`
- `fixtures/core/`
- `reference/python/cap_core/`
- CI for commit `b4ce530`

The review decision should choose one of:

- accept candidate normative review entry;
- keep CAP-Core draft-track;
- request additional evidence;
- split blocking concerns into new CAPPs or issues.

## Review Controls

Candidate review remains a governance state, not a stable release. During this
review:

- Core schemas stay draft/candidate-review artifacts;
- report schemas stay review evidence;
- fixture behavior remains candidate review coverage;
- profiles and bindings remain profile-owned or external unless accepted into
  minimal Core by a later CAPP;
- CAP-Digest grammar, DigestManifest semantics, and follow-up gate behavior do
  not change.

## Rationale

The repository now has enough executable evidence to review whether CAP-Core can
move beyond draft-track preparation. Starting review as a separate CAPP keeps
the decision explicit and avoids treating readiness evidence as automatic
promotion.

## Compatibility

This proposal has no direct data-format compatibility impact. It does not
change schemas, fixtures, validator behavior, or CAP-Digest. Any later CAPP
that accepts candidate normative text must provide compatibility analysis
against `specs/core/VERSIONING-AND-COMPATIBILITY.md`.

## Security and Privacy

The review must preserve the Phase 8 safety boundaries:

- fail-closed policy interpretation;
- opaque secret references only;
- no inline secret values in Core records;
- explicit service-binding and network limitations;
- RunEvidence does not prove semantic correctness;
- DigestEvidence remains separate from RunEvidence.

## Reference Implementation

The reference implementation remains evidence, not the specification. It covers
schema-like record validation, graph closure, stable error codes, inspection
rendering, conformance reports, and interop report generation.

## Conformance Fixtures

Candidate review uses:

- `fixtures/core/local-analysis/`
- `fixtures/core/build-test/`
- `fixtures/core/remote-service-binding/`
- `fixtures/core/negative/`

The current report package records three positive fixture families and 18
systematic negative cases.

## Non-Goals

- Do not publish stable CAP-Core.
- Do not freeze Core schemas as stable v1.
- Do not add Core concepts to CAP-Digest normative behavior.
- Do not define runtime execution, policy language, workflow engine, credential
  exchange, or scientific-correctness semantics.
