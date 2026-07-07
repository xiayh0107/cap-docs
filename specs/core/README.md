# CAP-Core

> Status: candidate-prep draft proposal area · Non-normative · Last updated: 2026-07-07

CAP-Core is the upper layer of CAP proposed for assembling machine-operable
research/engineering objects into a runnable, traceable, policy-governed
artifact graph. It now has a first draft proposal, but it remains distinct from
CAP-Digest and has no stable conformance language.

## Current status

CAP-Core remains non-normative. This directory contains the integrated RFC-0001
overview, split draft RFCs, and supporting planning and construction documents.
The repository also contains Core-scoped schema sketches, local-analysis,
build-test, and remote-service-binding fixtures, a systematic negative suite,
and validator/renderer/inspection/interop prototypes. None of these assets
define stable CAP-Core conformance.

Start here:

1. [CAP-Core Status and Roadmap](00-status-and-roadmap.md) — shared status language and CAPP gate reminder.
2. [CAP-Core Normative Language Policy](NORMATIVE-LANGUAGE.md) — future requirement-keyword policy.
3. [CAP-Core Writing Plan](WRITING-PLAN.md) — how to research and write CAP-Core.
4. [CAP-Core RFC-0001](RFC-0001.md) — first integrated draft proposal retained as an overview.
5. [RFC-0001 Core Object Model](RFC-0001-core-object-model.md) — split draft for minimal Core objects.
6. [RFC-0002 Binding Model](RFC-0002-binding-model.md) — split draft for generic bindings and binding roles.
7. [RFC-0003 Scientific Computation Profile](RFC-0003-scientific-computation-profile.md) — split profile draft.
8. [RFC-0004 CAP-Digest Bridge Profile](RFC-0004-cap-digest-bridge-profile.md) — split bridge profile draft.
9. [CAP-Core Schema Candidate Rules](SCHEMA-CANDIDATE-RULES.md) — candidate-prep object rules and error codes.
10. [Secret Reference and Service Binding Safety](SECRET-SERVICE-BINDING-SAFETY.md) — opaque secret and service rules.
11. [CAP-Core Inspection Report](INSPECTION-REPORT.md) — renderer report format and command.
12. [CAP-Core Interoperability Harness](INTEROPERABILITY-HARNESS.md) — implementation report and comparison path.
13. [Profile and Binding Registry Draft](PROFILE-AND-BINDING-REGISTRY.md) — profile/binding family registry.
14. [CAP-Core Profile Governance](PROFILE-GOVERNANCE.md) — profile lifecycle and extension rules.
15. [Terminology Collision Audit](TERMINOLOGY-COLLISION-AUDIT.md) — CAP-Core/CAP-Digest term boundaries.
16. [CAP-Core Draft Implementer Guide](IMPLEMENTATION-GUIDE.md) — validation, renderer, and interop commands.
17. [CAP-Core RFC-0001 Outline](RFC-0001-outline.md) — reviewed structure for the
   first CAP-Core RFC.
18. [CAP-Core Boundary Matrix](BOUNDARY-MATRIX.md) — Core/Profile/Binding/Digest/external split.
19. [CAP-Core Primitive Reuse Review](PRIMITIVE-REUSE.md) — primitive-by-primitive reuse/gap review.
20. [CAP-Core External Standard Binding Policy](BINDING-POLICY.md) — how Core binds to external standards.
21. [CAP-Core Ontology Draft](ONTOLOGY-DRAFT.md) — candidate Core objects and relationships.
22. [CAP-Core Lifecycle Draft](LIFECYCLE-DRAFT.md) — candidate assembly/run lifecycle checkpoints.
23. [CAP-Core Security and Policy Draft](SECURITY-POLICY-DRAFT.md) — policy/security record model.
24. [CAP-Core Conformance Draft](CONFORMANCE-DRAFT.md) — schema sketch and fixture plan.
25. [CAP-Core Versioning and Compatibility](VERSIONING-AND-COMPATIBILITY.md) — schema compatibility rules.
26. [CAP-Core Security, Privacy, and Trust](SECURITY-PRIVACY-TRUST.md) — candidate-prep threat model.
27. [Example Assembly 0001](EXAMPLE-ASSEMBLY-0001.md) — first scientific-analysis example.
28. [CAP-Core Research Sources](RESEARCH-SOURCES.md) — reviewed source basis for
   RFC drafting.
29. [CAP-Core Open Questions](OPEN-QUESTIONS.md) — questions to resolve or defer
   before RFC-0001 advances.
30. [CAP-Core review decisions](reviews/) — non-normative decision notes for
    object minimization, fixture value, schema boundaries, and RFC split
    planning.

Executable draft assets:

- `schemas/core/` — CAP-Core JSON Schema sketches.
- `fixtures/core/local-analysis/` — first Core fixture with positive and negative cases.
- `fixtures/core/build-test/` — second Core fixture proving the object model outside scientific analysis.
- `fixtures/core/remote-service-binding/` — non-local service-binding fixture without credentials.
- `fixtures/core/negative/` — systematic candidate-prep negative suite.
- `reference/python/cap_core/` — validator, renderer, inspection, and interop prototype.

## Problem statement (intended scope)

Where CAP-Digest specifies how a source object is safely turned into
model-readable context, CAP-Core is intended to specify how a complete
machine-operable object is assembled, bound, executed, and evidenced. Its
anticipated concerns include:

- artifact graph (inputs, derivations, outputs, dependencies);
- capability manifest (what the object can do, declared and bound);
- runtime binding (mapping declared capabilities to concrete runtimes);
- resource, service, and tool binding;
- policy decision model (authorization over capability invocation);
- run lifecycle (launch, observe, interrupt, resume, finalize);
- RunEvidence / provenance (records of what actually happened during a run);
- external standard bindings (e.g. MCP, Skills, CWL, RO-Crate, OCI, WASI,
  Kubernetes, REAPI, Sigstore, in-toto, SPDX, CycloneDX, OPA/Cedar).

These items are draft concepts, not stable commitments. They will be
re-evaluated through CAPP review, schemas, fixtures, and implementation work.

## Why CAP-Core stays non-normative

A cognitive correction (see `notes/2026-07-05-cognitive-error-and-framework.md`)
clarified that the existing `cap-docs` material defines a context evidence layer
(CAP-Digest), not a full assembly protocol. Rather than retroactively inflate
CAP-Digest into CAP-Core, the two are kept separate. CAP-Core now has a first
draft proposal, but it remains non-normative until future CAPPs accept Core
schemas, fixtures, and conformance language.

## Related reading

- `specs/digest/` — the current, draft CAP-Digest profile.
- `notes/2026-07-05-cognitive-error-and-framework.md` — the cognitive correction
  that established the CAP-Digest / CAP-Core split.
- `notes/2026-07-05-deep-research-v2-knowledge-notes.md` — retained knowledge
  notes (standard ecosystem, concept boundaries, MVP trade-offs) to seed a
  future CAP-Core research pass.
