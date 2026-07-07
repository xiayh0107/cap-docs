# CAP-Core and CAP-Digest Terminology Collision Audit

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

This audit records terms that could be confused across CAP-Core and CAP-Digest.

| Term | CAP-Core use | CAP-Digest use | Resolution |
|---|---|---|---|
| Artifact | Core object for data, code, config, environment, result, log, report, model, document, or collection. | Not a Digest term. | Use `Artifact`, not `Field`, for Core package objects. |
| ArtifactRef | Embedded Core reference to an artifact location. | `SourceRef` points to a digest source. | Keep names separate. |
| Field | Not a Core object. | Digest unit selected for model-visible context. | Do not promote Field into Core schema. |
| SourceRef | External source identity for Digest. | Not a Core object. | Use ArtifactRef or Binding target in Core. |
| Evidence | Generic word only. | Digest evidence describes what supports a digest field. | Qualify as RunEvidence or DigestEvidence. |
| RunEvidence | Core envelope for run observations, records, logs, provenance refs, and limitations. | Not a Digest replacement. | Validator rejects DigestEvidence-as-RunEvidence. |
| DigestEvidence | Digest-layer evidence for model-visible context. | CAP-Digest governed. | Bridge through DigestBinding only. |
| Gate | Not a Core lifecycle concept. | Follow-up gate in CAP-Digest. | Avoid using Gate for policy or runtime decisions in Core. |
| Capability | Operation shape declaration. | Not authorization and not a tool call record. | PolicyDecision authorizes; Binding references tools/transports. |
| Binding | Core typed edge to runtime, resource, service, policy, evidence, digest, transport, data-plane, or schema. | Not a Digest primitive. | External standard semantics remain outside Core. |
| Manifest | Avoid as a Core object name unless qualified. | DigestManifest is CAP-Digest governed. | Use ArtifactSet, Assembly, or conformance report in Core. |
| PolicyDecision | Core policy result record. | Digest uses policy inputs for field selection and gate checks. | Keep policy language external in Core. |

Validator messages now use explicit terms such as
`digest_evidence_used_as_run_evidence`,
`digest_binding_collapses_evidence_layers`, and
`capability_implies_authorization`.
