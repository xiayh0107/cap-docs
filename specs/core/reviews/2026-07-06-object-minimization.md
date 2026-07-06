# CAP-Core Object Minimization Review

> Status: decision note - Non-normative - Issue: #24 - Date: 2026-07-06

This review decides which CAP-Core draft objects should stay in Core, move to a
profile, move to a binding role, bind to an external standard, or leave
RFC-0001 entirely before any future normative promotion.

No object is promoted to normative CAP-Core by this note. Any promotion still
requires a future CAPP with schema, fixture, compatibility, and security
evidence.

## Decision summary

| Candidate | Decision | Location | Rationale |
|---|---|---|---|
| `Assembly` | keep | Core | Central pre-run contract linking artifacts, capability, bindings, policy, state, and unresolved items. It should be the root review object. |
| `Artifact` | keep | Core | Primary referenced object for data, code, config, environment, results, logs, reports, and documents. |
| `ArtifactRef` | keep | Core | Minimal reference and integrity hook. Bytes, storage, and transfer remain external. |
| `Profile` | keep/split | Core mechanism, profile-owned semantics | Core should define how profiles are referenced; domain and runtime semantics belong to profiles. |
| `Capability` | keep/defer details | Core minimal declaration, external catalog binding | A small operation contract is useful, but tool metadata, MCP descriptions, and workflow tasks stay external or profile-bound. |
| Generic `Binding` | keep | Core | A single typed edge is the best minimal mechanism for connecting Core objects to external systems without copying them. |
| `RuntimeBinding` | split/defer top-level | Binding role plus external runtime profile | Keep as `Binding.type = runtime`; do not make a separate top-level object yet. Runtime semantics stay with OCI, WASI, Kubernetes, Slurm, REAPI, local hosts, or profiles. |
| `ResourceBinding` | keep as role | Binding role / Core envelope | Resource constraints are needed for review, but scheduler-specific semantics stay external. |
| `ServiceBinding` | keep as role | Binding role | Record service dependencies and secret references, never service protocol semantics or secret values. |
| `PolicyBinding` | keep as role | Binding role plus minimal decision record | Core needs visible authorization outcome and constraints. Policy language, identity, and consent systems remain external. |
| `EvidenceBinding` | keep as role | Binding role | Use for references to provenance, attestations, SBOMs, telemetry, logs, and host evidence. External standards own those formats. |
| `DigestBinding` | keep as role | Binding role / Digest bridge profile | Needed to link RunEvidence to CAP-Digest views while keeping RunEvidence and DigestEvidence distinct. |
| `TransportBinding` | defer | Optional Binding role | Useful for host/tool reachability, but transport protocol semantics are external. |
| `DataPlaneBinding` | defer | Optional Binding role / external | Core may reference a data plane, but bytes and transfer protocols are external. |
| `SchemaBinding` | defer | Optional Binding role / profile | Useful for validation hooks. Do not require one semantic stack. |
| `Run` | keep | Core | Minimal execution/observation instance linked to Assembly and evidence. Strict state machine remains deferred. |
| `RunEvidence` | keep/defer details | Core envelope plus external evidence bindings | Keep a small envelope for subject, materials, products, records, completeness, and integrity. Detailed provenance, signatures, SBOMs, and telemetry remain external. |

## Remove from RFC-0001

The integrated RFC draft should not define these as Core primitives:

- separate required top-level classes for every binding subtype;
- workflow language semantics;
- runtime, container, scheduler, sandbox, or transport protocol semantics;
- policy language, identity protocol, or consent framework semantics;
- provenance ontology, attestation format, SBOM format, or telemetry protocol;
- secret values or secret management behavior;
- CAP-Digest field selection, digest text grammar, or DigestEvidence semantics.

## Answers to review questions

| Question | Answer |
|---|---|
| Is `Assembly` the correct root object? | Yes. `Assembly` is the root review object. `Artifact` remains a primary referenced object, not the root. |
| Should `Binding` remain a generic typed edge? | Yes. Start with one generic `Binding` and named roles. |
| Should binding subtypes be separate top-level objects? | No for RFC-0001. Defer until fixtures show generic `Binding` is ambiguous. |
| Is `Capability` too close to tool metadata? | It is close, so keep only a minimal contract in Core and bind tool/catalog metadata externally. |
| Does `RunEvidence` duplicate external standards? | It can if over-expanded. Keep only an envelope and bind to W3C PROV, Workflow Run RO-Crate, in-toto, Sigstore, SBOM, and telemetry records externally. |
| Which objects move to profiles? | Domain semantics, scientific computation details, workflow profiles, CAP-Digest bridge rules, schema constraints, and runtime-specific interpretations. |
| Which objects move to bindings? | Runtime, resource, service, policy, evidence, digest, transport, data-plane, and schema details. |
| Which objects should be removed entirely? | Any execution engine, workflow language, policy engine, provenance ontology, secret manager, SBOM/attestation format, or Digest text details. |

## Follow-up

This review supports splitting the integrated RFC into a smaller Core object
model, a binding model, and profile documents. The split decision is recorded in
`2026-07-06-rfc-split-decision.md`; implementation is tracked in #29.
