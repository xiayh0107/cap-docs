# CAP-Core RFC-0001: Core Object Model

> Status: draft proposal - Non-normative - Last updated: 2026-07-07

This split draft contains only the minimal CAP-Core object model. It does not
define stable CAP-Core conformance and does not promote CAP-Core beyond
draft-track status.

## Scope

This document owns the Core control-plane objects that are needed to describe a
reviewable machine-operable assembly:

- `ArtifactSet`
- `Artifact` / `ArtifactRef`
- `Profile` reference mechanism
- `Capability` minimal declaration
- `Assembly`
- `PolicyDecision` minimal record
- `Run`
- `RunEvidence` minimal envelope

It does not define binding role semantics, scientific profile semantics,
CAP-Digest bridge rules, workflow languages, runtime execution behavior, policy
languages, provenance ontologies, SBOM formats, or telemetry protocols.

## Object Model

```text
ArtifactSet
  Artifact[]

Capability
  inputs -> Artifact roles
  outputs -> Artifact roles
  requiredBindings -> binding role names

Assembly
  artifacts -> Artifact ids
  capability -> Capability id
  bindings -> Binding ids
  policyBinding -> Binding id
  state

PolicyDecision
  policyBinding -> Binding id
  principal/action/resource
  decision
  conditions/obligations

Run
  assemblyId -> Assembly id
  inputs/outputs/logs -> Artifact ids
  runtimeBinding/resourceBinding -> Binding ids
  evidenceRefs -> RunEvidence ids

RunEvidence
  runId -> Run id
  materials/products/logs -> Artifact ids
  records
  provenanceRefs/sbomRefs/telemetryRefs
  digestViews -> DigestBinding ids
  completeness/integrity
```

## Minimal Field Intent

| Object | Required intent |
|---|---|
| `ArtifactSet` | Groups fixture or assembly artifacts without defining storage or transfer. |
| `Artifact` | Gives each machine-operable object an id, kind, and reference. |
| `ArtifactRef` | Locates or identifies an artifact through URI, scope, kind, and optional integrity. |
| `Profile` reference | Names profile semantics without putting those semantics into Core. |
| `Capability` | Declares the operation shape over artifact roles and required binding roles. |
| `Assembly` | The root pre-run review object linking artifacts, capability, bindings, and policy. |
| `PolicyDecision` | Records the policy basis and decision outcome relied on by the Assembly. |
| `Run` | Records one execution or observation instance created from an Assembly. |
| `RunEvidence` | Records or references evidence produced by or about a Run. |

## Boundary Rules

- `Assembly` is the root review object. `Artifact` remains a primary referenced
  object, not the root.
- `Capability` is a minimal operation contract. Tool metadata, MCP tool
  descriptions, workflow tasks, and service APIs remain external or profile
  bound.
- `PolicyDecision` is a minimal decision record. Core does not define a policy
  language, identity provider, or consent framework.
- `RunEvidence` is an envelope. W3C PROV, Workflow Run RO-Crate, in-toto,
  Sigstore, SPDX, CycloneDX, and OpenTelemetry remain external evidence systems.
- Core records may reference secrets but must not carry secret values.
- External ArtifactRef records use `integrityState` to distinguish verified,
  unverified, and unavailable integrity.
- RunEvidence records observations and limitations; it does not prove semantic
  correctness or scientific validity.

## Draft Schemas

The current JSON Schema sketches live under `schemas/core/`:

```text
cap.core.artifact_set.v1.schema.json
cap.core.artifact.v1.schema.json
cap.core.capability.v1.schema.json
cap.core.assembly.v1.schema.json
cap.core.policy_decision.v1.schema.json
cap.core.run.v1.schema.json
cap.core.run_evidence.v1.schema.json
```

These schemas are executable draft assets, not stable conformance requirements.
Candidate-prep rules and validator error codes are summarized in
`SCHEMA-CANDIDATE-RULES.md`.

## Fixtures

The draft object model is exercised by:

- `fixtures/core/local-analysis/`
- `fixtures/core/build-test/`
- `fixtures/core/remote-service-binding/`
- `fixtures/core/negative/`

All listed fixtures remain draft-track and non-normative.

## Deferrals

- strict run state machine;
- mandatory JSON-LD representation;
- mandatory W3C PROV representation;
- normative Core conformance levels;
- separate top-level objects for each binding role;
- runtime, scheduler, workflow, policy, or provenance semantics.
