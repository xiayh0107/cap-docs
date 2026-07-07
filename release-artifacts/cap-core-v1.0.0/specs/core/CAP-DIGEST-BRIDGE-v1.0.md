# CAP-Core v1.0 CAP-Digest Bridge Boundary

> Status: stable v1.0 profile boundary - Last updated: 2026-07-07

The CAP-Digest bridge remains a profile-level boundary for v1.0. DigestBinding
connects Core RunEvidence to a CAP-Digest view without changing CAP-Digest.

## Stable Bridge Rules

- DigestBinding is a Binding with `type: digest`.
- DigestBinding is profile-owned and not part of the minimal Core object set.
- DigestBinding target references a CAP-Digest view or manifest.
- `constraints.sourceRunEvidence` points to a RunEvidence id.
- `constraints.digestEvidenceIsRunEvidence` is `false`.
- DigestEvidence and RunEvidence remain distinct.

## CAP-Digest Non-Mutation

CAP-Core v1.0 does not change digest text grammar, DigestManifest semantics,
DigestEvidence semantics, or follow-up gate behavior. Any future change to
those surfaces follows CAP-Digest governance.
