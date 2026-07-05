# CAP-Core Writing Plan

> Status: planning · Non-normative · Last updated: 2026-07-05

This document defines how CAP-Core should be researched and written. It does not
start the CAP-Core specification. CAP-Core remains reserved until the entry
criteria in this plan are met.

## Purpose

CAP-Core should be drafted only after the project can answer one question with
precision:

> What cross-layer assembly contract is missing for machine-operable agent tasks,
> and which parts should CAP define instead of reusing existing standards?

CAP-Digest already covers model-visible context evidence. CAP-Core must not
repeat CAP-Digest. CAP-Core should address the broader object assembly problem:
which objects exist, what capabilities can act on them, where those capabilities
can run, what resources and services they bind to, which policies authorize the
binding, and what evidence is produced.

## Writing principles

1. **Reuse before invention.** CAP-Core should reference mature standards rather
   than redefine workflow languages, runtime formats, authorization engines,
   provenance models, supply-chain attestations, or agent transport protocols.
2. **Core before profiles.** Core should define only the minimum cross-layer
   ontology and lifecycle. Domain-specific behavior belongs in profiles.
3. **Bindings, not replacements.** CAP-Core should define how to bind to MCP,
   A2A, CWL, RO-Crate, OCI, WASI, Kubernetes, REAPI, Sigstore, in-toto, SPDX,
   CycloneDX, OPA, Cedar, and similar systems where appropriate.
4. **Evidence is layered.** CAP-Digest proves what the model saw. CAP-Core
   should specify RunEvidence and provenance only for execution/assembly events,
   not for claim truth.
5. **No normative Core without fixtures.** A CAP-Core primitive should not become
   normative until it has at least one schema sketch, example assembly, and
   conformance fixture plan.

## Non-goals for the writing phase

The writing phase MUST NOT:

- define a new workflow language;
- define a new container or sandbox format;
- define a new policy language;
- define a new SBOM format;
- define an agent-to-agent transport protocol;
- make CAP-Digest part of CAP-Core by copy-paste;
- introduce normative CAP-Core requirements before RFC-0001 is reviewed.

## Proposed writing sequence

Write CAP-Core in this order:

1. **Research basis** — source matrix, standards comparison, adoption evidence,
   and gap analysis.
2. **Problem and scope** — what CAP-Core solves, what it excludes, and why the
   problem is not covered by MCP, Skills, A2A, CWL, RO-Crate, or runtime systems
   alone.
3. **Ontology** — Artifact, Profile, Capability, RuntimeBinding,
   ResourceBinding, ServiceBinding, PolicyBinding, Assembly, Run, RunEvidence,
   and Binding.
4. **Lifecycle** — discover, describe, assemble, bind, authorize, execute,
   observe, finalize, evidence, and digest.
5. **Boundary matrix** — what belongs in Core, Profile, Binding, Digest, or
   external standard.
6. **External standard bindings** — required reference style for existing
   standards and when CAP-Core may define a binding.
7. **Security and policy model** — identity, authorization handoff, policy
   decision records, secrets, data locality, and audit boundaries.
8. **Conformance strategy** — schema sketches, example assemblies, fixture
   families, and conformance levels.
9. **RFC-0001 draft** — integrated first draft after the above documents are
   reviewed.

## Deliverables

The first CAP-Core writing cycle should produce:

| Deliverable | Path | Normative? | Purpose |
|---|---|---:|---|
| Research source map | `specs/core/RESEARCH-SOURCES.md` | No | Track source basis and what to reuse. |
| RFC-0001 outline | `specs/core/RFC-0001-outline.md` | No | Define the draft structure before writing. |
| Open questions | `specs/core/OPEN-QUESTIONS.md` | No | Prevent unresolved design choices from becoming accidental spec. |
| Boundary matrix | future `specs/core/BOUNDARY-MATRIX.md` | No until accepted | Decide Core/Profile/Binding/external split. |
| RFC-0001 draft | future `specs/core/RFC-0001.md` | Draft only | First integrated CAP-Core proposal. |

## Entry criteria for drafting RFC-0001

Do not create `specs/core/RFC-0001.md` until the following are true:

- the research source map has at least one source for each major adjacent
  category: agent connection, skills/procedure packaging, workflow, research
  object packaging, runtime, remote execution, policy, provenance, supply chain,
  and observability;
- the ontology names have been reviewed against CAP-Digest terminology;
- every proposed Core primitive has a statement of what existing standard it
  reuses or why no existing standard is sufficient;
- at least one end-to-end example assembly is described without requiring new
  runtime semantics;
- open questions have explicit owners or deferral decisions.

## First example assembly

The first example should be narrow and scientific-computing oriented:

```text
Input artifacts: dataset, notebook/script, environment reference, config
Capability: run analysis or validate result
Runtime binding: local process or OCI container reference
Resource binding: CPU/memory/time budget
Service binding: none or explicit object store reference
Policy binding: user/session authorization and network disabled by default
Run: planned -> started -> completed/failed
RunEvidence: inputs, parameters, outputs, logs, environment digest, timestamps
Digest: CAP-Digest view of the resulting run evidence
```

This example should be treated as a writing scaffold, not a normative profile.

## Definition of done for the writing plan

This plan is complete when:

- RFC-0001 has a reviewed outline;
- CAP-Core terms are separated from CAP-Digest terms;
- the external-standard reuse policy is explicit;
- the first example assembly is written;
- at least one CAPP or Core RFC decision records whether CAP-Core work should
  proceed to a draft specification.
