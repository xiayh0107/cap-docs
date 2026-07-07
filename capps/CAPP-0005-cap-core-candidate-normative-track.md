# CAPP-0005: CAP-Core Candidate Normative Track

> Status: draft - Created: 2026-07-07 - Layer: CAP-Core

## Motivation

CAP-Core has completed its draft-track asset set: split draft RFCs, Core schema
sketches, two executable fixture families, and a validator/renderer prototype.
Those assets are enough to prepare candidate review, but they are not enough to
declare stable CAP-Core conformance.

This CAPP defines the gates that must be satisfied before any later proposal may
promote CAP-Core from draft-track to candidate normative status. It does not
promote CAP-Core by itself.

## Proposal

CAP-Core may enter a candidate normative track only after the repository records
evidence for governance, schema stability, fixture coverage, validator output,
security review, and interoperability.

The minimal Core object set for candidate review is:

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

The CAP-Digest Bridge remains a profile that connects Core RunEvidence to
CAP-Digest views. It is not part of the minimal Core object model and cannot
change CAP-Digest behavior.

## Candidate Entry Gates

- CAP-Core conformance levels L0-L4 are defined with machine-testable criteria.
- Core schema versioning and compatibility rules are documented.
- All minimal Core object schemas have positive and negative fixture coverage.
- At least one non-local fixture covers remote service binding without secrets.
- The Core validator emits a stable machine-readable conformance report.
- The Core renderer emits a stable human-readable inspection report.
- A security, privacy, and trust review covers policy decisions, secret
  references, service bindings, and RunEvidence overclaim boundaries.
- Blocking open questions are triaged in `specs/core/OPEN-QUESTIONS.md`.
- Independent implementation evidence exists: either two implementations, or
  the reference implementation plus an external interoperability harness.

## Required Evidence

| Evidence | Required artifact |
|---|---|
| Conformance levels | `specs/core/CONFORMANCE-DRAFT.md` |
| Schema compatibility | `specs/core/VERSIONING-AND-COMPATIBILITY.md` |
| Security review | `specs/core/SECURITY-PRIVACY-TRUST.md` |
| Non-local fixture | `fixtures/core/remote-service-binding/` |
| Negative suite | `fixtures/core/negative/` |
| Validator report | `schemas/core/cap.core.conformance_report.v1.schema.json` |
| CI coverage | `.github/workflows/core-draft.yml` |
| Open question triage | `specs/core/OPEN-QUESTIONS.md` |

## Compatibility Impact

This CAPP does not change CAP-Digest behavior and does not freeze any Core
schema. Existing CAP-Core files remain draft-track. Future candidate normative
changes must describe compatibility impact against the schema versioning rules.

## Security and Privacy Impact

Candidate promotion is blocked until Core can show fail-closed policy handling,
opaque secret references, explicit service-binding boundaries, and RunEvidence
that does not overclaim remote or semantic correctness.

## Acceptance Criteria

- The gates above are represented in issues or documents.
- No Core schema, RunEvidence, binding, service binding, or policy model is
  described as stable before the gates are met.
- Any future candidate promotion proposal cites this CAPP and includes evidence
  for every gate.

## Non-Goals

- This CAPP does not publish a CAP-Core candidate normative release.
- This CAPP does not freeze object schemas.
- This CAPP does not add CAP-Core concepts to CAP-Digest normative behavior.
