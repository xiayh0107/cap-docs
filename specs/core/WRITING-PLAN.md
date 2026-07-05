# CAP-Core Writing Plan

> Status: planning · Non-normative · Last updated: 2026-07-05

This document defines how CAP-Core should be researched and written. It did not
start the CAP-Core specification by itself. The completion record below shows
that the first writing cycle has moved CAP-Core from reserved planning material
to a non-normative draft proposal.

## Purpose

CAP-Core was to be drafted only after the project could answer one question with
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
| Boundary matrix | `specs/core/BOUNDARY-MATRIX.md` | No until accepted | Decide Core/Profile/Binding/external split. |
| Primitive reuse review | `specs/core/PRIMITIVE-REUSE.md` | No | Record reuse or gap statement for each proposed primitive. |
| Binding policy | `specs/core/BINDING-POLICY.md` | No | Define how CAP-Core references external standards. |
| Security and policy draft | `specs/core/SECURITY-POLICY-DRAFT.md` | No | Sketch policy records, secret handling, and evidence integrity. |
| Conformance draft | `specs/core/CONFORMANCE-DRAFT.md` | No | Sketch schemas, fixtures, and conformance levels. |
| Example assembly | `specs/core/EXAMPLE-ASSEMBLY-0001.md` | No | Test the object model end to end. |
| RFC-0001 draft | `specs/core/RFC-0001.md` | Draft only | First integrated CAP-Core proposal. |
| Draft-entry CAPP | `capps/CAPP-0004-cap-core-draft-entry.md` | Proposed | Records whether CAP-Core should proceed to draft specification. |

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

## Entry criteria review

The first RFC-0001 draft was created only after these checks were recorded:

| Criterion | Evidence |
|---|---|
| At least one source for each major adjacent category | `RESEARCH-SOURCES.md` baseline reviewed source records. |
| Ontology names reviewed against CAP-Digest terminology | `PRIMITIVE-REUSE.md` CAP-Digest separation and rejected names. |
| Every proposed Core primitive has a reuse or gap statement | `PRIMITIVE-REUSE.md` primitive review table. |
| At least one end-to-end example assembly is described | `EXAMPLE-ASSEMBLY-0001.md`. |
| Open questions have owners or deferral decisions | `OPEN-QUESTIONS.md` current dispositions table. |

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

## Completion record

As of 2026-07-05, the writing plan is complete for the first CAP-Core writing
cycle:

| Done item | Evidence |
|---|---|
| RFC-0001 has a reviewed outline | `RFC-0001-outline.md` is marked `reviewed outline` and lists the review inputs. |
| CAP-Core terms are separated from CAP-Digest terms | `PRIMITIVE-REUSE.md` separates Core terms from Digest terms. |
| External-standard reuse policy is explicit | `BINDING-POLICY.md` and `RESEARCH-SOURCES.md`. |
| First example assembly is written | `EXAMPLE-ASSEMBLY-0001.md`. |
| CAPP/Core RFC decision records whether to proceed | `capps/CAPP-0004-cap-core-draft-entry.md` proposes proceeding to draft specification. |

Completion does not mean CAP-Core is accepted or normative. It means the first
writing cycle has produced the planned draft artifacts and the next work should
move through CAPP review, schema sketches, fixtures, and validator work.
