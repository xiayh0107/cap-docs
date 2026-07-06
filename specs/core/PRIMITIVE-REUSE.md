# CAP-Core Primitive Reuse Review

> Status: draft - Non-normative - Last updated: 2026-07-05

This file records the reuse or gap statement for each proposed CAP-Core
primitive. It is the writing-plan gate that prevents a Core term from being
introduced merely because an agent might find it useful.

## Review rule

A primitive can remain in the RFC-0001 draft only when at least one of these is
true:

- an existing standard supplies the domain semantics and CAP-Core only needs a
  reference or binding;
- no reviewed source supplies the cross-layer assembly relationship that CAP-Core
  needs;
- the primitive is needed to keep CAP-Digest, external standards, policy, and run
  evidence from being conflated.

## Primitive review table

| Primitive | Existing standards or systems to reuse | Gap that remains for CAP-Core | Draft location |
|---|---|---|---|
| `Artifact` | RO-Crate, BagIt, OCI descriptors, CodeMeta, SPDX, CycloneDX, domain schemas. | A common object envelope is needed so data, code, configs, models, logs, environments, and results can be referenced in one assembly. | Core |
| `ArtifactRef` | URI schemes, content digests, OCI descriptors, object stores, DataLad/git-annex, Arrow Flight tickets. | Existing reference schemes do not provide a CAP-wide role in an assembly graph. Core needs scoped refs plus integrity hooks. | Core |
| `Profile` | JSON Schema, JSON-LD, SHACL, RO-Crate profiles, CWL, WDL, BIDS-like domain profiles. | CAP-Core needs a way to say which non-Core rules interpret an object without putting those rules into Core. | Core mechanism, profile-owned semantics |
| `Capability` | MCP tools, A2A agent cards, Skills, CWL tools, WDL tasks, service APIs. | Tool calls and workflow steps are not a neutral contract saying what operation may act on which artifacts under what constraints. | Core minimal declaration, external catalog binding |
| `Binding` | URIs, profile identifiers, registry references, host object references. | A uniform typed edge is needed to connect Core objects to external standards without copying those standards. | Core |
| `RuntimeBinding` | OCI, WASI, Kubernetes, Slurm, REAPI, Temporal, Prefect, local process hosts. | Core needs a reviewable runtime handle before execution, but must not define runtime execution behavior. | Binding role |
| `ResourceBinding` | Kubernetes resources, Slurm allocations, cloud/HPC quotas, host limits. | Assemblies need explicit CPU, memory, GPU, time, network, storage, locality, and cost constraints independent of any one scheduler. | Binding role / Core envelope |
| `ServiceBinding` | MCP resources/tools, object stores, databases, model APIs, license servers, secret stores. | A run may depend on external services; Core must record the dependency and access mode without defining the service protocol. | Binding role |
| `PolicyBinding` | OPA/Rego, Cedar, OAuth/OIDC, SPIFFE/SPIRE, IAM systems, host policy engines. | CAP-Core must record what was allowed, denied, or constrained for an Assembly or Run without defining policy language. | Binding role plus minimal decision record |
| `EvidenceBinding` | W3C PROV, Workflow Run RO-Crate, in-toto, SLSA, Sigstore, SPDX, CycloneDX, OpenTelemetry, MLflow. | Core needs a typed envelope for evidence references and completeness claims across multiple evidence families. | Binding role |
| `DigestBinding` | CAP-Digest SourceRef, DigestManifest, DigestEvidence. | Core needs an explicit bridge to model-visible digest views while keeping RunEvidence distinct from DigestEvidence. | Binding role |
| `TransportBinding` | MCP, A2A, HTTP APIs, host tool APIs, message buses. | Some capabilities are reachable through transports, but Core must not define or require a transport protocol. | Optional binding role |
| `Assembly` | Workflow manifests, RO-Crate metadata, Kubernetes Job specs, build actions, package manifests. | No reviewed source provides the complete pre-run contract linking artifacts, capability, runtime/resource/service bindings, policy decision, and unresolved items. | Core |
| `Run` | Workflow execution records, Kubernetes Jobs/Pods, Slurm jobs, Temporal workflows, Prefect flow runs, MLflow runs. | Core needs a runtime-neutral instance record that links back to the Assembly and forward to evidence. | Core |
| `RunEvidence` | W3C PROV, Workflow Run RO-Crate, in-toto/SLSA attestations, Sigstore bundles, OpenTelemetry, SBOMs. | CAP-Core needs an evidence envelope that can reference multiple evidence families and state completeness without inventing a full provenance ontology. | Core envelope plus external evidence bindings |

## Names rejected or constrained

| Candidate name | Decision | Reason |
|---|---|---|
| `Evidence` | Do not use as an unqualified Core object. | It collides with CAP-Digest evidence and provenance evidence. Use `RunEvidence`, `DigestEvidence`, or a named evidence binding. |
| `Field` | Do not use for Core object properties. | CAP-Digest owns `Field` as a context digest concept. |
| `Gate` | Do not use for Core policy. | CAP-Digest owns follow-up gates; CAP-Core should use `PolicyBinding` or `PolicyDecision`. |
| `Context Pack` | Do not use for Core. | CAP-Digest packs, Skills, and Core profiles are different objects. |
| `Execution Contract` | Avoid as the primary framing. | It implies CAP-Core defines an execution engine. |
| `Machine-Operable Context Layer` | Avoid as the primary framing. | It risks collapsing CAP-Core back into CAP-Digest context evidence. |

## CAP-Digest separation

CAP-Digest terms remain scoped to model-visible context:

| CAP-Digest term | Scope |
|---|---|
| `SourceRef` | Source object for digest rendering. |
| `Field` | Model-visible or requestable source-object field. |
| `Digest` | Rendered context text or structured digest. |
| `DigestManifest` | Record of what entered, did not enter, or changed in the digest. |
| `DigestEvidence` | Evidence that the model saw or could request specific fields. |
| `Follow-up Gate` | Gate for additional context extraction. |

CAP-Core terms remain scoped to machine-operable assembly:

| CAP-Core term | Scope |
|---|---|
| `Artifact` / `ArtifactRef` | Object identity and references. |
| `Capability` | Operation contract over artifacts. |
| `Binding` | Typed edge to external standards or host systems. |
| `Assembly` | Pre-run object/capability/binding/policy contract. |
| `Run` | Instance created from an Assembly. |
| `RunEvidence` | Records and evidence references from a Run. |

## First draft conclusion

The reviewed primitives are sufficient for an RFC-0001 draft, with one
constraint: `RuntimeBinding`, `ResourceBinding`, `ServiceBinding`,
`PolicyBinding`, `EvidenceBinding`, `TransportBinding`, and `DigestBinding`
should start as binding roles rather than separate normative object types. A
future fixture may split them into top-level objects if a generic `Binding`
becomes ambiguous.
