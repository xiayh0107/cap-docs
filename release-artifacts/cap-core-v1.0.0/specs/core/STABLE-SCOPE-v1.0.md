# CAP-Core v1.0 Stable Scope

> Status: stable v1.0 - Normative scope baseline - Last updated: 2026-07-07

This document freezes the CAP-Core v1.0 scope. Any change to this scope after
v1.0.0 requires a CAPP or an explicit v1.0.x errata decision.

## Minimal Core Objects

CAP-Core v1.0 defines the minimal control-plane object contract for:

- `ArtifactSet`
- `Artifact` and embedded `ArtifactRef`
- `Capability`
- `Binding`
- `Assembly`
- `PolicyDecision`
- `Run`
- `RunEvidence`

`DigestBinding` is a CAP-Digest bridge profile binding. It is used by v1.0
fixtures and conformance reports, but it is not promoted into the minimal Core
object set.

## Scope

CAP-Core v1.0 covers structural records, object identity, reference closure,
binding envelopes, policy decision records, run records, evidence envelopes,
stable validation findings, conformance reports, inspection reports, fixture
suites, and profile extension boundaries.

## Non-Goals

CAP-Core v1.0 does not define:

- runtime execution behavior;
- workflow engine semantics;
- scheduler semantics;
- policy language or identity-provider semantics;
- credential exchange or secret-manager protocols;
- scientific correctness or reproducibility scoring;
- CAP-Digest text grammar, DigestManifest semantics, or follow-up gate behavior;
- detailed schemas for external standards such as OCI, W3C PROV, Sigstore,
  SPDX, CycloneDX, OPA, Cedar, Kubernetes, Slurm, MCP, or A2A.

## Profile and Binding Boundaries

Profiles may add stricter domain constraints without changing minimal Core.
External binding families remain referenced or profiled; their schemas and
semantics are not copied into Core.

## Stable Change Rule

Post-v1.0 scope changes require CAPP review. Additive profile guidance can be
documented without changing minimal Core only when it preserves the object set,
report formats, and compatibility rules.
