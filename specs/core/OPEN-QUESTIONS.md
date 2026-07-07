# CAP-Core Open Questions

> Status: triaged for candidate prep · Non-normative · Last updated: 2026-07-07

This file records unresolved CAP-Core design questions. These questions should
be resolved, narrowed, or explicitly deferred before `RFC-0001.md` advances
beyond draft proposal status.

## Positioning

1. Is CAP-Core best described as an **Object Assembly Contract**, an
   **Execution Contract**, an **Artifact Graph**, or a
   **Machine-Operable Context Layer**?
2. Should CAP-Core define a control-plane contract only, leaving all data-plane
   transfer to external systems?
3. Should CAP-Core define a minimal state machine, or only record lifecycle
   checkpoints?

## Ontology

4. Is `Artifact` the root object, or is `Assembly` the root object?
5. Should `Capability` be a first-class Core object, or a profile-bound object
   referenced from external catalogs?
6. Is `Profile` a constraint set, a schema bundle, a compatibility label, or all
   three?
7. Should `Binding` be a generic typed edge, or should each binding type be a
   separate object?

## External standards

8. What is the minimal binding shape that can reference MCP, A2A, CWL, RO-Crate,
   OCI, WASI, Kubernetes, REAPI, W3C PROV, in-toto, Sigstore, SPDX, CycloneDX,
   OPA, Cedar, and OpenTelemetry without reimplementing them?
9. Should CAP-Core require JSON-LD compatibility, or only allow JSON-LD profiles?
10. Should CAP-Core define an external standard registry, or rely on URI-based
    references and profiles?

## Policy and security

11. Should CAP-Core define a `PolicyDecision` object, or only a `PolicyBinding`
    reference to an external decision?
12. How should CAP-Core represent secrets without becoming a secret manager?
13. How should CAP-Core represent user consent and delegated authority without
    becoming an authorization framework?
14. Which security properties are Core conformance requirements, and which are
    profile hardening requirements?

## Run and evidence

15. What is the smallest useful `Run` object?
16. What is the smallest useful `RunEvidence` envelope?
17. Should RunEvidence reuse W3C PROV directly, map to it, or allow multiple
    evidence profiles?
18. How does CAP-Core link RunEvidence to CAP-Digest DigestEvidence without
    confusing execution evidence with model-visible evidence?

## Conformance

19. What is the first CAP-Core conformance fixture?
20. Should conformance begin with parsing object graphs or producing a complete
    assembly example?
21. What is the smallest reference implementation that proves CAP-Core adds value
    without implementing a full agent runtime?

## Current dispositions

These dispositions are the writing-plan gate for the first RFC-0001 draft. They
are not final technical decisions.

| # | Owner | Current disposition | RFC-0001 treatment |
|---:|---|---|---|
| 1 | Core editor | Prefer **Machine-Operable Object Assembly Contract**. | Use this as the RFC title hypothesis. |
| 2 | Core editor | Yes: Core is a control-plane contract. | State that large bytes and transfer semantics remain external. |
| 3 | Core editor | Define lifecycle checkpoints first; defer strict state machine. | Use checkpoint names and leave mandatory states open. |
| 4 | Core editor | Treat `Assembly` as the central contract; `Artifact` remains a primary referenced object. | Define both, with `Assembly` linking artifacts to capability and bindings. |
| 5 | Core editor | Keep `Capability` first-class in Core, but allow external catalogs. | Define minimal capability shape and external catalog binding. |
| 6 | Core editor | Treat `Profile` as schema constraint plus compatibility label. | Do not put domain semantics in Core. |
| 7 | Core editor | Use generic `Binding` with named binding roles in the first draft. | Defer separate top-level binding objects until fixtures show the need. |
| 8 | Core editor | Use a minimal binding envelope: type, target, standard, version/profile, constraints, integrity, status. | Put detailed external semantics in binding profiles. |
| 9 | Core editor | Allow JSON-LD profiles; do not require JSON-LD for all Core objects. | Keep JSON Schema as the first schema-sketch path. |
| 10 | Core editor | Use URI/source-label references first; defer registry design. | Do not define a CAP-Core registry in RFC-0001. |
| 11 | Core editor | Include `PolicyBinding` and a minimal embedded `decision` record. | Do not define a policy language. |
| 12 | Core editor | Represent secret requirements by reference only. | Ban secret values from Core records. |
| 13 | Core editor | Record consent/delegation evidence as policy decision references. | Bind to OAuth/OIDC, workload identity, or host policy systems. |
| 14 | Core editor | Core requires explicit policy decision records and no implicit secret disclosure. | Profile hardening may add stronger controls. |
| 15 | Core editor | Smallest `Run`: id, assembly, state, timestamps, outputs/log refs, evidence refs. | Use checkpoint model in RFC-0001. |
| 16 | Core editor | Smallest `RunEvidence`: subject run, materials, products, records, external evidence refs, completeness. | Keep distinct from DigestEvidence. |
| 17 | Core editor | Allow W3C PROV / Workflow Run RO-Crate profiles; do not require PROV as the only form. | Bind or map to provenance standards. |
| 18 | Core editor | Link through `DigestBinding` or digest view references. | State that DigestEvidence proves model-visible context, not run execution. |
| 19 | Core editor | First fixture family: local scientific analysis assembly. | Plan fixture under `fixtures/core/local-analysis/` after schema sketch review. |
| 20 | Core editor | Begin with parsing object graphs and producing one complete assembly example. | Levels 0-2 cover reader, assembly producer, run recorder. |
| 21 | Core editor | Minimal reference implementation is a validator/renderer, not a runtime. | Defer execution engine behavior out of scope. |

## Candidate-prep triage

This table classifies each question for candidate normative preparation. The
promotion gates in `capps/CAPP-0005-cap-core-candidate-normative-track.md`
must cite all blocking items before any future candidate promotion.

| # | Classification | Owner / follow-up | Evidence or disposition |
|---:|---|---|---|
| 1 | Closed | Core editor | RFC split uses "Machine-Operable Object Assembly Contract". |
| 2 | Closed | Core editor | Core remains a control-plane contract; data-plane binding is external. |
| 3 | Blocking | #41 | Minimal run lifecycle states must be candidate-defined. |
| 4 | Closed | Core editor | `Assembly` is the review root; `Artifact` remains referenced. |
| 5 | Blocking | #37 | Capability must stay first-class without implying authorization. |
| 6 | Deferred-to-profile | #55 | Profiles own domain constraints and compatibility labels. |
| 7 | Blocking | #38 | Binding role taxonomy must stabilize before candidate review. |
| 8 | Deferred-to-binding | #52 | External standards need registry/profile guidance, not Core reimplementation. |
| 9 | Non-blocking | Future profile CAPP | JSON-LD compatibility can remain profile-optional. |
| 10 | Deferred-to-binding | #52 | Registry draft may use URI/profile references first. |
| 11 | Blocking | #40 | `PolicyDecision` fail-closed semantics must stabilize. |
| 12 | Blocking | #46 | Secret reference and service binding safety model required. |
| 13 | Non-blocking | Security/profile docs | Consent/delegation evidence can bind to external policy systems. |
| 14 | Blocking | #45 | Security invariants must map to fixture or validator coverage. |
| 15 | Blocking | #41 | Minimal `Run` states and references are candidate inputs. |
| 16 | Blocking | #42 | Minimal `RunEvidence` envelope and overclaim boundary required. |
| 17 | Deferred-to-binding | #52 | PROV/RO-Crate remain evidence profiles. |
| 18 | Blocking | #51 | CAP-Digest bridge tests must preserve evidence separation. |
| 19 | Closed | Core editor | First fixture exists at `fixtures/core/local-analysis/`. |
| 20 | Closed | Core editor | L0-L3 begin with object graph validation and complete assembly examples. |
| 21 | Closed | Core editor | Reference scope is validator/renderer, not runtime. |

## Deferral rule

If a question requires designing a workflow engine, policy engine, runtime,
transport, SBOM format, or provenance ontology, it should be deferred to an
external-standard binding or a profile unless RFC-0001 proves that Core must
include a minimal abstraction.
