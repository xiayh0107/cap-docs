# CAP-Core Conformance Draft

> Status: draft - Non-normative - Last updated: 2026-07-05

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

## Candidate levels

| Level | Name | Capability |
|---:|---|---|
| 0 | Core Object Reader | Parses `ArtifactRef`, `Capability`, `Binding`, `Assembly`, `Run`, and `RunEvidence` records and preserves unknown profile fields. |
| 1 | Assembly Producer | Emits a complete pre-run `Assembly` with artifact refs, capability, profiles, runtime/resource/policy bindings, and unresolved items. |
| 2 | Run Recorder | Records a `Run` from an `Assembly` and links outputs, logs, status, and `RunEvidence`. |
| 3 | Binding Ecosystem | Validates at least one external runtime/evidence/policy binding and one CAP-Digest view reference. |

No level should become normative until a later CAPP promotes the draft fixture
files and validator behavior into stable conformance language.

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

## First draft conclusion

RFC-0001 may include this conformance strategy as a proposal. It should not
claim CAP-Core conformance exists until schemas, fixtures, and a validator are
added in a later CAPP.
