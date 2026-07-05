# CAP-Core RFC-0001 Outline

> Status: outline · Non-normative · Last updated: 2026-07-05

This file is an outline for a future CAP-Core RFC-0001. It is not the RFC and
contains no normative CAP-Core requirements.

Working title:

> CAP-Core RFC-0001: Machine-Operable Object Assembly Contract

## 1. Abstract

Explain CAP-Core in one paragraph:

- CAP-Core is a cross-layer assembly contract for machine-operable agent tasks.
- It describes artifacts, capabilities, runtime/resource/service bindings,
  policy bindings, runs, and evidence.
- It binds to existing standards rather than replacing them.
- CAP-Digest remains the context evidence profile for model-visible views.

## 2. Status of this document

State that the document is a draft proposal and not yet a stable standard.
Clarify the relationship to CAP-Digest and to the reserved status of CAP-Core.

## 3. Motivation and problem statement

Questions to answer:

- What does an agent need to know before acting on a machine-operable object?
- Why are text, screenshots, tool calls, and raw API schemas insufficient?
- Why are MCP, Skills, A2A, workflow engines, and provenance formats necessary
  but not sufficient alone?
- What failure modes appear when artifact, capability, runtime, policy, and
  evidence are defined in separate systems with no common assembly contract?

## 4. Scope and non-goals

CAP-Core should include:

- identity and references for artifacts;
- capability declarations at the contract level;
- bindings to runtime, resource, service, policy, and evidence systems;
- assembly and run lifecycle records;
- profile and binding extension points.

CAP-Core should exclude:

- transport protocols;
- full agent runtimes;
- workflow languages;
- container formats;
- policy languages;
- SBOM formats;
- model reasoning guarantees;
- CAP-Digest field selection and digest text details.

Use `BOUNDARY-MATRIX.md` as the working source for this section.

## 5. Relationship to CAP-Digest

Include a diagram:

```text
CAP-Core
  Artifact graph
  Capability contract
  Runtime / resource / service binding
  Policy binding
  Run lifecycle
  RunEvidence
    |
    | produces or references
    v
CAP-Digest
  SourceRef / Field Catalog / Digest / DigestManifest / DigestEvidence
```

Rules to define:

- CAP-Digest may render a CAP-Core Artifact, Run, or Evidence object into
  model-visible context.
- CAP-Core must not depend on digest text as its only evidence format.
- DigestEvidence and RunEvidence are distinct.

## 6. Terminology

Candidate terms:

| Term | Draft meaning |
|---|---|
| Artifact | Data, code, model, config, result, log, image, environment reference, or document. |
| ArtifactRef | Stable or scoped reference to an Artifact. |
| Profile | Domain or execution-specific interpretation of Core objects. |
| Capability | Declared operation that can act on artifacts under constraints. |
| RuntimeBinding | Binding between a Capability and a concrete execution environment. |
| ResourceBinding | Budget and resource envelope for a Run. |
| ServiceBinding | External service, API, database, object store, or model service binding. |
| PolicyBinding | Authorization and policy decision reference for an Assembly or Run. |
| Assembly | A resolved contract connecting artifacts, capabilities, bindings, and policy. |
| Run | One execution or observation instance created from an Assembly. |
| RunEvidence | Records, logs, signatures, provenance, outputs, and attestations from a Run. |
| Binding | A typed edge between a CAP-Core object and an external standard or host object. |

Use `ONTOLOGY-DRAFT.md` as the working source for this section.

## 7. Layer model

Proposed layers:

```text
External Standards
  MCP, A2A, Skills, CWL, RO-Crate, OCI, WASI, Kubernetes, REAPI,
  W3C PROV, in-toto, Sigstore, SPDX, CycloneDX, OPA, Cedar, OpenTelemetry

CAP-Core
  Artifact, Capability, Binding, PolicyBinding, Assembly, Run, RunEvidence

Profiles and Bindings
  domain profiles, workflow profiles, runtime bindings, evidence bindings

CAP-Digest
  model-visible context evidence views
```

## 8. Core object model

For each object, RFC-0001 should define:

- purpose;
- required fields;
- optional fields;
- identity and versioning rules;
- relationship to other Core objects;
- external standards it may bind to;
- what must remain profile-specific.

Candidate objects:

```text
Artifact
ArtifactRef
Profile
Capability
RuntimeBinding
ResourceBinding
ServiceBinding
PolicyBinding
Assembly
Run
RunEvidence
EvidenceEnvelope
Binding
```

Use `ONTOLOGY-DRAFT.md` and `EXAMPLE-ASSEMBLY-0001.md` to test whether this set
is too broad or too small.

## 9. Assembly lifecycle

Draft lifecycle:

```text
1. discover artifacts and capabilities
2. resolve profiles
3. assemble candidate contract
4. bind runtime/resource/service references
5. request policy decision
6. create assembly record
7. start run
8. observe run
9. finalize run
10. produce RunEvidence
11. optionally render CAP-Digest views
```

Open question: should CAP-Core define a state machine, or only record lifecycle
checkpoints?

Use `LIFECYCLE-DRAFT.md` as the working source for this section.

## 10. External standard binding policy

RFC-0001 should include a table:

| Area | Reuse candidate | CAP-Core behavior |
|---|---|---|
| Agent connection | MCP / A2A | Bind or reference; do not replace. |
| Procedure packaging | Skills | Bind human-maintained instructions; do not treat as executable contract. |
| Workflow | CWL / WDL / Nextflow | Profile or binding; do not define new workflow language. |
| Research object | RO-Crate | Archive/profile binding; do not replace packaging. |
| Runtime | OCI / WASI / Kubernetes / REAPI / Nix | Runtime binding; do not define runtime. |
| Provenance | W3C PROV / Workflow Run RO-Crate | Evidence binding; do not invent full provenance model. |
| Supply chain | in-toto / Sigstore / SPDX / CycloneDX | Evidence binding; do not define signing or SBOM format. |
| Policy | OPA / Cedar / OAuth/OIDC | Policy binding; do not define policy language. |
| Observability | OpenTelemetry | Evidence input; do not define tracing protocol. |

Use `RESEARCH-SOURCES.md` as the source list and `BOUNDARY-MATRIX.md` as the
boundary decision record.

## 11. Security and policy model

Topics to cover:

- principal identity;
- authorization boundaries;
- capability scope;
- secret handling;
- network and data locality constraints;
- delegation and revocation references;
- audit and evidence completeness;
- failure and denial records;
- distinction between policy decision and model request.

RFC-0001 should define records and bindings, not a new policy engine.

## 12. Profiles

Define why profiles exist:

- scientific computation profile;
- ML experiment profile;
- batch workflow profile;
- notebook analysis profile;
- data validation profile;
- software build/test profile.

Core should define profile mechanics, not domain semantics.

## 13. Conformance strategy

Candidate conformance levels:

```text
Level 0: Core Object Reader
  parses Artifact, Capability, and Binding objects

Level 1: Assembly Producer
  emits Assembly with profile/runtime/resource/policy bindings

Level 2: Run Recorder
  records Run and RunEvidence envelope

Level 3: Binding Ecosystem
  validates at least one external standard binding and one CAP-Digest view
```

Do not accept conformance levels until fixtures exist.

## 14. Example assembly

Use `EXAMPLE-ASSEMBLY-0001.md` as the first concrete example.

```text
dataset + script + environment reference + config
  -> capability: run analysis
  -> runtime binding: local or OCI reference
  -> resource binding: CPU/memory/time
  -> policy binding: no network, user/session authorization
  -> run
  -> run evidence
  -> CAP-Digest view
```

## 15. Compatibility and versioning

Define:

- Core schema versioning;
- profile versioning;
- binding versioning;
- external standard version references;
- compatibility with CAP-Digest versions.

## 16. Open questions

Initial open questions live in `OPEN-QUESTIONS.md` and should be resolved or
deferred before RFC-0001 is drafted.

## 17. Source basis

RFC-0001 should cite stable source labels from `RESEARCH-SOURCES.md` and should
separate:

- established standards;
- observed industrial practice;
- CAP design hypotheses;
- unresolved research questions.
