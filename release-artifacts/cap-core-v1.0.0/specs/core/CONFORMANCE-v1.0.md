# CAP-Core v1.0 Conformance

> Status: stable v1.0 - Normative - Last updated: 2026-07-07

This document defines CAP-Core v1.0 conformance levels. Implementations claim
only the highest level whose required checks, fixtures, and reports pass.

## Shared Rules

Implementations claiming any level MUST preserve unknown profile fields, MUST
report unsupported features, and MUST NOT execute an Assembly merely because it
is structurally valid. Reports use `cap.core.conformance_report.v1`.

## Levels

| Level | Stable definition | Required evidence |
|---:|---|---|
| L0 | Structural Core Package / Object Reader. The implementation MUST read Core records, validate schema names and required fields, preserve unknown profile fields, and inventory object IDs. | At least one positive fixture and schema checks. |
| L1 | Bound Assembly Package. The implementation MUST validate ArtifactSet, Artifact, Capability, Binding, Assembly, graph closure, and required binding roles. | Positive fixtures plus reference-closure negative cases. |
| L2 | Policy-Aware Assembly. The implementation MUST validate PolicyDecision records, fail closed when required policy evidence is missing, reject inline secret-looking values, and report service/network boundary findings. | Policy, secret, stale service, and undeclared network cases. |
| L3 | Run-Evidence Producer. The implementation MUST validate Run and RunEvidence links, output/log/material refs, limitations, DigestBinding separation, and overclaim findings. | L3 conformance report with RunEvidence checks. |
| L4 | Interoperable Core Implementation. The implementation MUST provide cross-implementation comparison evidence for pass/fail status and stable finding codes. | Interop report and comparison report. |

## Report Fields

Stable reports include implementation identity, version, target level, fixture
identity, object summary, schema checks, reference closure checks, policy
checks, binding checks, RunEvidence checks, security findings, unsupported
features, and stable error/warning codes.

## Claim Templates

Use one of:

```text
Implementation <name> claims CAP-Core v1.0 L0 conformance for structural object reading.
Implementation <name> claims CAP-Core v1.0 L1 conformance for bound assembly validation.
Implementation <name> claims CAP-Core v1.0 L2 conformance for policy-aware assembly validation.
Implementation <name> claims CAP-Core v1.0 L3 conformance for run-evidence producer validation.
Implementation <name> claims CAP-Core v1.0 L4 conformance for interoperable report comparison.
```

Each claim MUST cite a report path, fixture suite version, unsupported feature
list, and implementation version.

## Non-Requirements

No level requires live runtime execution, external policy evaluation, secret
retrieval, live service calls, cryptographic attestation verification, or proof
of scientific correctness.
