# CAP-Core PolicyDecision and ArtifactSet Boundary Decision

> Status: decision note - Non-normative - Issue: #28 - Date: 2026-07-06

## Decision

Add draft schema sketches for both `ArtifactSet` and `PolicyDecision`.

This resolves the previous ambiguity where `source-artifacts.json` and
`policy-decision.json` were fixture records but not schema-backed Core draft
records.

## Boundary Outcomes

| Shape | Decision | Location | Rationale |
|---|---|---|---|
| `ArtifactSet` | keep as Core draft wrapper | Core / fixture packaging | Multiple fixtures need a stable way to package artifact arrays without making storage or transfer semantics part of Core. |
| `Artifact` entries | keep | Core | Already schema-backed and referenced by Assembly, Run, and RunEvidence. |
| `PolicyDecision` | keep as minimal Core draft record | Core object model | Assemblies need a visible allow/deny/constrained decision record before a run. |
| Policy language | external | External / Binding | OPA, Cedar, IAM, OAuth/OIDC, SPIFFE/SPIRE, and host policy systems own evaluation semantics. |
| Artifact storage and bytes | external | Data-plane binding | Filesystems, object stores, archives, and content-addressed stores own transfer and storage. |

## Added schema sketches

```text
schemas/core/cap.core.artifact_set.v1.schema.json
schemas/core/cap.core.policy_decision.v1.schema.json
```

These schemas remain draft-track. They do not create stable CAP-Core
conformance.

## Fixture Updates

The schema validation map now validates:

- `fixtures/core/*/source-artifacts.json` against `cap.core.artifact_set.v1`;
- nested artifacts against `cap.core.artifact.v1`;
- `fixtures/core/*/policy-decision.json` against
  `cap.core.policy_decision.v1`;
- expected-invalid policy decision negative fixtures against the same schema.
