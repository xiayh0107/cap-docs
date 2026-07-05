# CAP-Core (Reserved)

> Status: reserved · Last updated: 2026-07-05

CAP-Core is the **reserved** upper layer of CAP: a future specification for
assembling machine-operable research/engineering objects into a runnable,
traceable, policy-governed artifact graph. It is **not yet drafted**. This
directory is a placeholder so that future CAP-Core work has a home distinct from
the CAP-Digest profile.

## Current status

CAP-Core remains reserved. The files added here are planning and research
coordination documents only; they are non-normative and do not define CAP-Core
conformance.

Start here:

1. [CAP-Core Writing Plan](WRITING-PLAN.md) — how to research and write CAP-Core.
2. [CAP-Core RFC-0001 Outline](RFC-0001-outline.md) — proposed structure for the
   first future CAP-Core RFC.
3. [CAP-Core Research Sources](RESEARCH-SOURCES.md) — source categories to review
   before drafting.
4. [CAP-Core Open Questions](OPEN-QUESTIONS.md) — questions to resolve or defer
   before RFC-0001.

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

These items are **concepts**, not commitments. They will be re-evaluated when
CAP-Core work formally starts.

## Why it is reserved, not started

A cognitive correction (see `notes/2026-07-05-cognitive-error-and-framework.md`)
clarified that the existing `cap-docs` material defines a context evidence layer
(CAP-Digest), not a full assembly protocol. Rather than retroactively inflate
CAP-Digest into CAP-Core, the two are kept separate. CAP-Core will be drafted
only after a fresh, framework-correct research pass; until then this directory
holds no normative content.

## Related reading

- `specs/digest/` — the current, draft CAP-Digest profile.
- `notes/2026-07-05-cognitive-error-and-framework.md` — the cognitive correction
  that established the CAP-Digest / CAP-Core split.
- `notes/2026-07-05-deep-research-v2-knowledge-notes.md` — retained knowledge
  notes (standard ecosystem, concept boundaries, MVP trade-offs) to seed a
  future CAP-Core research pass.
