# CAP-Core

> Status: CAP-Core v1.0.0 stable · Last updated: 2026-07-07

CAP-Core is the CAP layer for reviewable machine-operable object records:
artifacts, capabilities, bindings, assemblies, policy decisions, runs, and run
evidence. CAP-Core v1.0.0 is limited to the minimal control-plane object
contract and conformance evidence.

## Current status

CAP-Core v1.0.0 stable is accepted by CAPP-0007. The release artifact is
`release-artifacts/cap-core-v1.0.0/` and the repository tag is
`cap-core-v1.0.0`.

CAP-Core v1.0.0 does not define runtime execution, workflow engines, policy
language semantics, credential exchange, scientific correctness, or CAP-Digest
behavior changes.

Start here:

1. [CAP-Core Status and Roadmap](00-status-and-roadmap.md) — shared status language and CAPP gate reminder.
2. [CAP-Core Normative Language Policy](NORMATIVE-LANGUAGE.md) — future requirement-keyword policy.
3. [CAP-Core v1.0 Stable Scope](STABLE-SCOPE-v1.0.md) — stable minimal Core boundary.
4. [CAP-Core v1.0 Conformance](CONFORMANCE-v1.0.md) — stable L0-L4 conformance.
5. [CAP-Core v1.0 Schema Package](SCHEMA-PACKAGE-v1.0.md) — stable schema package contract.
6. [CAP-Core v1.0 Fixture Suite](FIXTURES-v1.0.md) — stable fixture index.
7. [CAP-Core v1.0 Security Requirements](SECURITY-v1.0.md) — stable security baseline.
8. [CAP-Core v1.0 Maintenance Policy](MAINTENANCE-v1.0.md) — errata and patch policy.
9. [CAP-Core v1.0 Validator Codes](VALIDATOR-CODES-v1.0.md) — stable finding-code registry.
10. [CAP-Core v1.0 Inspection Report](INSPECTION-REPORT-v1.0.md) — stable renderer/report format.
11. [CAP-Core v1.0 RunEvidence](RUN-EVIDENCE-v1.0.md) — stable evidence limits and overclaim rules.
12. [CAP-Core v1.0 Policy and Service Boundary](POLICY-SERVICE-v1.0.md) — stable policy/service checks.
13. [CAP-Core v1.0 CAP-Digest Bridge Boundary](CAP-DIGEST-BRIDGE-v1.0.md) — bridge profile boundary.
14. [CAP-Core v1.0 Profile and Binding Registry](PROFILE-BINDING-REGISTRY-v1.0.md) — registry snapshot.
15. [CAP-Core Implementer Guide](IMPLEMENTATION-GUIDE.md) — validation, renderer, and interop commands.
16. [CAP-Core Interoperability Harness](INTEROPERABILITY-HARNESS.md) — implementation report and comparison path.

Historical and design documents:

1. [CAP-Core RFC-0001](RFC-0001.md) — first integrated draft proposal retained as an overview.
2. [RFC-0001 Core Object Model](RFC-0001-core-object-model.md) — split draft for minimal Core objects.
3. [RFC-0002 Binding Model](RFC-0002-binding-model.md) — split draft for generic bindings and binding roles.
4. [RFC-0003 Scientific Computation Profile](RFC-0003-scientific-computation-profile.md) — split profile draft.
5. [RFC-0004 CAP-Digest Bridge Profile](RFC-0004-cap-digest-bridge-profile.md) — split bridge profile draft.
6. [CAP-Core Schema Candidate Rules](SCHEMA-CANDIDATE-RULES.md) — candidate-prep object rules and error codes.
7. [Secret Reference and Service Binding Safety](SECRET-SERVICE-BINDING-SAFETY.md) — opaque secret and service rules.
8. [CAP-Core Inspection Report](INSPECTION-REPORT.md) — renderer report format and command.
9. [Profile and Binding Registry Draft](PROFILE-AND-BINDING-REGISTRY.md) — profile/binding family registry.
10. [CAP-Core Profile Governance](PROFILE-GOVERNANCE.md) — profile lifecycle and extension rules.
11. [Terminology Collision Audit](TERMINOLOGY-COLLISION-AUDIT.md) — CAP-Core/CAP-Digest term boundaries.
12. [CAP-Core RFC-0001 Outline](RFC-0001-outline.md) — reviewed structure for the
   first CAP-Core RFC.
13. [CAP-Core Boundary Matrix](BOUNDARY-MATRIX.md) — Core/Profile/Binding/Digest/external split.
14. [CAP-Core Primitive Reuse Review](PRIMITIVE-REUSE.md) — primitive-by-primitive reuse/gap review.
15. [CAP-Core External Standard Binding Policy](BINDING-POLICY.md) — how Core binds to external standards.
16. [CAP-Core Ontology Draft](ONTOLOGY-DRAFT.md) — candidate Core objects and relationships.
17. [CAP-Core Lifecycle Draft](LIFECYCLE-DRAFT.md) — candidate assembly/run lifecycle checkpoints.
18. [CAP-Core Security and Policy Draft](SECURITY-POLICY-DRAFT.md) — policy/security record model.
19. [CAP-Core Conformance Draft](CONFORMANCE-DRAFT.md) — schema sketch and fixture plan.
20. [CAP-Core Versioning and Compatibility](VERSIONING-AND-COMPATIBILITY.md) — schema compatibility rules.
21. [CAP-Core Security, Privacy, and Trust](SECURITY-PRIVACY-TRUST.md) — candidate-prep threat model.
22. [Example Assembly 0001](EXAMPLE-ASSEMBLY-0001.md) — first scientific-analysis example.
23. [CAP-Core Research Sources](RESEARCH-SOURCES.md) — reviewed source basis for
   RFC drafting.
24. [CAP-Core Open Questions](OPEN-QUESTIONS.md) — questions to resolve or defer
   before RFC-0001 advances.
25. [CAP-Core review decisions](reviews/) — decision notes for
    object minimization, fixture value, schema boundaries, and RFC split
    planning.

Executable assets:

- `schemas/core/` — CAP-Core v1.0 JSON Schema package.
- `fixtures/core/` — positive and negative v1.0 fixture suite.
- `reference/python/cap_core/` — validator, renderer, inspection, and interop helpers.
- `release-artifacts/cap-core-v1.0.0/` — stable release package.

## Scope

Where CAP-Digest specifies how a source object is safely turned into
model-readable context, CAP-Core specifies a structural control-plane record
set for machine-operable objects. Its stable v1.0 surface includes:

- artifact graph (inputs, derivations, outputs, dependencies);
- capability manifest (what the object can do, declared and bound);
- runtime binding references;
- resource, service, and tool binding;
- policy decision model (authorization over capability invocation);
- run records and RunEvidence envelopes;
- external standard bindings (e.g. MCP, Skills, CWL, RO-Crate, OCI, WASI,
  Kubernetes, REAPI, Sigstore, in-toto, SPDX, CycloneDX, OPA/Cedar).

External standards remain referenced or profile-owned. CAP-Core v1.0 does not
copy their schemas into minimal Core.

## Layer Rule

CAP-Digest remains a context evidence profile. CAP-Core v1.0 remains a broader
object record and conformance layer. The CAP-Digest bridge profile connects
RunEvidence to digest views, but it does not change CAP-Digest grammar,
manifest semantics, or follow-up gates.

## Related reading

- `specs/digest/` — the current CAP-Digest profile.
- `notes/2026-07-05-cognitive-error-and-framework.md` — the cognitive correction
  that established the CAP-Digest / CAP-Core split.
- `notes/2026-07-05-deep-research-v2-knowledge-notes.md` — retained knowledge
  notes (standard ecosystem, concept boundaries, MVP trade-offs).
