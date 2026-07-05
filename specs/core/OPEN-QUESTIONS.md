# CAP-Core Open Questions

> Status: planning · Non-normative · Last updated: 2026-07-05

This file records unresolved CAP-Core design questions. These questions should
be resolved, narrowed, or explicitly deferred before drafting `RFC-0001.md`.

## Positioning

1. Is CAP-Core best described as an **Object Assembly Contract**, an
   **Execution Contract**, an **Artifact Graph**, or a **Machine-Operable Context
   Layer**?
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

## Deferral rule

If a question requires designing a workflow engine, policy engine, runtime,
transport, SBOM format, or provenance ontology, it should be deferred to an
external-standard binding or a profile unless RFC-0001 proves that Core must
include a minimal abstraction.
