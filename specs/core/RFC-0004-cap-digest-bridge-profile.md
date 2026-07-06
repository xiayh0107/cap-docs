# CAP-Core RFC-0004: CAP-Digest Bridge Profile

> Status: draft profile proposal - Non-normative - Last updated: 2026-07-06

This split draft defines the draft bridge between CAP-Core RunEvidence and
CAP-Digest views. It does not change CAP-Digest normative behavior.

## Scope

The bridge profile owns:

- `Binding.type = digest`;
- `DigestBinding` constraints;
- links from RunEvidence to one or more digest views;
- rules that keep RunEvidence distinct from DigestEvidence.

## Core-to-Digest Relationship

```text
RunEvidence
  digestViews -> DigestBinding ids

DigestBinding
  target -> CAP-Digest view or manifest reference
  constraints.sourceRunEvidence -> RunEvidence id
  constraints.digestEvidenceIsRunEvidence -> false
```

CAP-Digest may render model-visible context from a Core Artifact, Assembly, Run,
or RunEvidence record. The digest view does not replace the original Core
evidence.

## Boundary Rules

- RunEvidence records what happened during or around a run.
- DigestEvidence records what the model saw or could request in a digest.
- DigestBinding may connect those layers, but must not collapse them.
- CAP-Core must not depend on digest text as its only evidence format.
- CAP-Digest field selection, digest text grammar, DigestManifest, and follow-up
  gates remain CAP-Digest concerns.

## Fixture Basis

The bridge is exercised by:

- `fixtures/core/local-analysis/digest-view-ref.json`
- `fixtures/core/build-test/digest-view-ref.json`

Both fixtures include negative cases where CAP-Digest evidence is rejected as a
substitute for CAP-Core RunEvidence.

## Coordination Rule

Any future change that alters CAP-Digest behavior, digest grammar, manifest
semantics, or DigestEvidence semantics must go through the CAP-Digest governance
process. This bridge profile can reference CAP-Digest; it cannot silently change
it.
