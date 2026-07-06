# CAP-Core

> Status: draft proposal area · Non-normative · Last updated: 2026-07-05

CAP-Core is the upper layer of CAP proposed for assembling machine-operable
research/engineering objects into a runnable, traceable, policy-governed
artifact graph. It now has a first draft proposal, but it remains distinct from
CAP-Digest and has no stable conformance language.

## Current status

CAP-Core remains non-normative. This directory contains a first draft proposal
for CAP-Core RFC-0001 plus supporting planning and construction documents. The
repository also contains Core-scoped schema sketches, a local-analysis fixture,
and a validator/renderer prototype. None of these assets define stable CAP-Core
conformance.

Start here:

1. [CAP-Core Writing Plan](WRITING-PLAN.md) — how to research and write CAP-Core.
2. [CAP-Core RFC-0001](RFC-0001.md) — first integrated draft proposal.
3. [CAP-Core RFC-0001 Outline](RFC-0001-outline.md) — reviewed structure for the
   first CAP-Core RFC.
4. [CAP-Core Boundary Matrix](BOUNDARY-MATRIX.md) — Core/Profile/Binding/Digest/external split.
5. [CAP-Core Primitive Reuse Review](PRIMITIVE-REUSE.md) — primitive-by-primitive reuse/gap review.
6. [CAP-Core External Standard Binding Policy](BINDING-POLICY.md) — how Core binds to external standards.
7. [CAP-Core Ontology Draft](ONTOLOGY-DRAFT.md) — candidate Core objects and relationships.
8. [CAP-Core Lifecycle Draft](LIFECYCLE-DRAFT.md) — candidate assembly/run lifecycle checkpoints.
9. [CAP-Core Security and Policy Draft](SECURITY-POLICY-DRAFT.md) — policy/security record model.
10. [CAP-Core Conformance Draft](CONFORMANCE-DRAFT.md) — schema sketch and fixture plan.
11. [Example Assembly 0001](EXAMPLE-ASSEMBLY-0001.md) — first scientific-analysis example.
12. [CAP-Core Research Sources](RESEARCH-SOURCES.md) — reviewed source basis for
   RFC drafting.
13. [CAP-Core Open Questions](OPEN-QUESTIONS.md) — questions to resolve or defer
   before RFC-0001 advances.
14. [CAP-Core review decisions](reviews/) — non-normative decision notes for
    object minimization, fixture value, and RFC split planning.

Executable draft assets:

- `schemas/core/` — CAP-Core JSON Schema sketches.
- `fixtures/core/local-analysis/` — first Core fixture with positive and negative cases.
- `reference/python/cap_core/` — validator/renderer prototype.

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
