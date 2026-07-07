# CAP-Core Conformance Draft

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

This document sketches how CAP-Core conformance should be tested after
RFC-0001. It is not an accepted conformance program.

## Implementation checkpoint

As of 2026-07-06, the first draft-track assets exist:

- schema sketches under `schemas/core/`;
- positive and negative fixture cases under `fixtures/core/local-analysis/` and
  `fixtures/core/build-test/`;
- a validator/renderer prototype under `reference/python/cap_core/`;
- tests in `reference/python/tests/test_core_local_analysis.py`.

These assets make the draft executable. They still do not create stable
CAP-Core conformance requirements.

## Conformance principle

CAP-Core conformance should begin with reading and writing reviewable records,
not with executing tasks. A conforming implementation should prove it can
preserve the assembly contract and evidence links before it claims runtime
behavior.

## Candidate levels L0-L4

These levels remain candidate-prep only until a promotion CAPP accepts them.

| Level | Name | Definition | Non-goals |
|---:|---|---|---|
| L0 | Structural Core Package / Object Reader | Reads Core records, validates schema names and required fields, preserves unknown profile fields, and inventories object IDs. | Producing assemblies or executing runs. |
| L1 | Bound Assembly Package | Validates `ArtifactSet`, `Capability`, `Binding`, `Assembly`, and graph closure for artifacts, bindings, and policy binding. | Evaluating authorization or executing capability. |
| L2 | Policy-Aware Assembly | Adds `PolicyDecision` validation, fail-closed missing policy behavior, secret-value rejection, and network/resource policy checks. | Defining a policy language or identity framework. |
| L3 | Run-Evidence Producer | Adds `Run` and `RunEvidence` linkage, output/log/material references, DigestBinding separation, and overclaim warnings. | Proving scientific correctness or verifying all attestations. |
| L4 | Interoperable Runner / Cross-implementation Conformance | Compares fixture reports across two implementations or one implementation plus an external harness. | Mandating one runtime, scheduler, transport, or service API. |

## Level Matrix

| Level | Required schemas | Fixture coverage | Validator checks | Required report fields |
|---:|---|---|---|---|
| L0 | `ArtifactSet`, `Artifact`, `Capability`, `Binding` | At least one positive Core fixture. | required fields, schema support, duplicate ID inventory. | validator version, target level, fixture id, schema checks. |
| L1 | L0 + `Assembly` | Positive assembly fixture and graph-closure negative cases. | artifact refs, binding refs, capability refs, required binding roles. | ref-closure checks, object counts, error codes. |
| L2 | L1 + `PolicyDecision` | Policy positive fixture plus missing-policy, secret-value, and undeclared-network negatives. | fail-closed policy, policy binding match, secret scan, network constraints. | policy checks, security warnings, unsupported features. |
| L3 | L2 + `Run`, `RunEvidence`, DigestBinding profile | Run/evidence positive fixtures plus DigestEvidence/RunEvidence and overclaim negatives. | run assembly link, evidence refs, digest bridge separation, overclaim warnings. | run/evidence checks, digest bridge checks, warning codes. |
| L4 | All candidate schemas | Cross-implementation fixture corpus. | report comparison and unsupported feature reconciliation. | implementation identity, fixture matrix, interoperability result. |

Implementations may claim only the highest level whose required checks and
fixtures pass. Reading or writing records is separate from actual runtime
execution.

## Schema sketch

The first machine-readable sketch should be JSON Schema, with optional JSON-LD or
SHACL profiles later. JSON Schema is a validation path, not a semantic ontology.

Candidate schema files:

```text
schemas/core/cap.core.artifact.v1.schema.json
schemas/core/cap.core.artifact_set.v1.schema.json
schemas/core/cap.core.capability.v1.schema.json
schemas/core/cap.core.binding.v1.schema.json
schemas/core/cap.core.assembly.v1.schema.json
schemas/core/cap.core.policy_decision.v1.schema.json
schemas/core/cap.core.run.v1.schema.json
schemas/core/cap.core.run_evidence.v1.schema.json
```

Minimum shared object fields:

```text
id
type
version
profiles
bindings
metadata
```

Minimum binding fields:

```text
id
type
target
standard
standardVersion
profile
constraints
integrity
freshness
status
evidenceRefs
```

## Fixture families

The first fixture is local scientific analysis, aligned with
`EXAMPLE-ASSEMBLY-0001.md`. The second fixture is software build/test, which
checks that the object model is not tied to one scientific-analysis domain.

Current paths:

```text
fixtures/core/local-analysis/
fixtures/core/build-test/
fixtures/core/remote-service-binding/
fixtures/core/negative/
```

Candidate files:

```text
source-artifacts.json
capability.json
assembly.json
policy-decision.json
run.json
run-evidence.json
digest-view-ref.json
expected-validation.json
```

The fixture should test:

- dataset, script, config, environment, and output artifact references;
- one `run-analysis` capability;
- runtime binding to local process or OCI reference without defining runtime
  execution semantics;
- resource binding for CPU, memory, timeout, network, and storage;
- policy binding with `allowed_with_constraints` and network disabled;
- run record with completed or failed status;
- RunEvidence references to logs, outputs, timestamps, and optional provenance;
- DigestBinding to a CAP-Digest view without treating DigestEvidence as
  RunEvidence.

The build/test fixture adds:

- source repository, project config, environment, test report, and log
  artifacts;
- one `run-build-test` capability;
- runtime, resource, policy, evidence, digest, data-plane, transport, and schema
  bindings;
- policy decision with network disabled;
- negative cases for invalid run state, invalid policy decision, secret values
  in service bindings, and DigestEvidence/RunEvidence layer confusion.

## Negative fixture ideas

Negative fixtures should prove that validators reject or flag unsafe claims:

| Fixture | Expected result |
|---|---|
| Secret value embedded in `ServiceBinding` | Invalid or security warning. |
| Run without an Assembly reference | Invalid. |
| Runtime binding claims OCI but lacks image reference | Invalid or incomplete. |
| Policy decision missing for executable action | Invalid for Level 1/2. |
| DigestEvidence used as RunEvidence | Invalid naming/layer violation. |
| Unanchored artifact marked reproducible | Invalid or overclaim warning. |
| External standard copied inline as Core schema | Boundary warning. |

The systematic suite under `fixtures/core/negative/` maps these cases to L0-L3
candidate checks. The remote-service fixture adds service-specific negatives for
opaque secret references, missing policy decisions, undeclared network access,
stale service bindings, and remote evidence overclaims.

## Reference implementation scope

The smallest useful implementation is a validator and renderer:

```text
read Core records
validate required fields
preserve profile extension fields
check boundary/layer naming
render review summary
link RunEvidence and DigestBinding references
```

It should not:

- execute workflows;
- invoke tools;
- schedule jobs;
- evaluate policies;
- verify all signatures;
- fetch large artifacts;
- generate CAP-Digest content.

Those behaviors belong to host systems or external bindings.

## Fixture acceptance gates

Before any Core primitive becomes normative, the fixture plan should prove:

- the primitive appears in at least one positive fixture;
- invalid use is covered by at least one negative fixture or documented deferral;
- the primitive has a reuse/gap statement in `PRIMITIVE-REUSE.md`;
- the primitive does not duplicate a CAP-Digest term with a different meaning;
- the primitive can be serialized without depending on one runtime or workflow
  engine.

## Core conformance report

The candidate-prep validator report is `cap.core.conformance_report.v1` and is
schema-backed by `schemas/core/cap.core.conformance_report.v1.schema.json`.
Reports include validator identity, target level, fixture identity, schema
checks, reference-closure checks, policy checks, binding checks, RunEvidence
checks, security warnings, unsupported features, and stable error/warning codes.

## Interoperability Harness

L4 candidate-prep review uses `specs/core/INTEROPERABILITY-HARNESS.md`.
Implementation reports use `cap.core.interop_report.v1`; comparison reports use
`cap.core.interop_comparison.v1`. The harness compares fixture pass/fail status
and stable error codes, not runtime execution behavior.

## Inspection Renderer

Human review uses `specs/core/INSPECTION-REPORT.md`. The JSON report schema is
`cap.core.inspection_report.v1`, and the text renderer displays object graph,
binding, policy, run/evidence, limitation, warning, and error summaries.

## First draft conclusion

RFC-0001 and the split Core drafts may cite this conformance strategy as
candidate-prep evidence. They still must not claim stable CAP-Core conformance
until a future CAPP accepts the levels, schemas, fixtures, validator behavior,
and interoperability evidence.
