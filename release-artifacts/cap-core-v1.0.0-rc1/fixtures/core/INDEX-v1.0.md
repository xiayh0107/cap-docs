# CAP-Core v1.0 Positive Fixture Index

> Status: stable v1.0 fixture index - Last updated: 2026-07-07

| Fixture | Purpose | Objects covered | Expected result |
|---|---|---|---|
| `local-analysis/` | Local scientific analysis package. | ArtifactSet, Artifact, Capability, Binding, Assembly, PolicyDecision, Run, RunEvidence, DigestBinding profile. | `expected-validation.json` passes with no warnings. |
| `build-test/` | Software build/test package. | Same minimal Core object set plus schema and transport bindings. | `expected-validation.json` passes with no warnings. |
| `remote-service-binding/` | Non-local service dependency with opaque secret ref. | Same minimal Core object set plus service binding and remote limitations. | `expected-validation.json` passes with `remote_unverifiable_surface` warning. |

These fixtures are the stable positive baseline for CAP-Core v1.0 L0-L3
conformance checks. They do not execute workflows or call services.
