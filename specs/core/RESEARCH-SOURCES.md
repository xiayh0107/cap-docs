# CAP-Core Research Sources

> Status: planning · Non-normative · Last updated: 2026-07-05

This file lists the source categories that must be reviewed before CAP-Core
RFC-0001 is drafted. It is a source map plus a baseline review record, not a
completed literature review.

## How to use this file

For each source category, the CAP-Core author should answer:

1. What problem does the existing standard or system solve?
2. What should CAP-Core reuse or bind to?
3. What must CAP-Core avoid reimplementing?
4. What gap remains after reuse?
5. Does the gap belong in Core, Profile, Binding, or outside CAP?

## Source categories

| Area | Sources to review | Expected CAP-Core use |
|---|---|---|
| Agent connection | MCP, A2A, ACP candidates | Binding or interop layer; not Core object model replacement. |
| Procedure packaging | OpenAI/Codex Skills, Anthropic Skills, GitHub Copilot Skills | Human-maintained instruction packaging; not executable contract. |
| Agent frameworks | LangGraph, DSPy, Semantic Kernel, AutoGen, CrewAI | Practice examples; avoid framework-specific core semantics. |
| Workflow | CWL, WDL, Nextflow, Snakemake | Workflow profile or binding; do not define a workflow language. |
| Research object packaging | RO-Crate, Workflow Run RO-Crate, BagIt | Archive/profile binding; do not replace packaging standards. |
| Provenance | W3C PROV, Workflow Run RO-Crate, MLflow, DataLad | Evidence binding and vocabulary reuse; do not invent full provenance ontology. |
| Runtime and packaging | OCI Image Spec, WASI, Nix, Conda-lock | Runtime/environment binding; do not define runtime format. |
| Scheduling and execution | Kubernetes, Slurm/HPC, Temporal, Prefect, REAPI | Runtime/resource binding; do not define scheduler. |
| Policy and authorization | OPA/Rego, Cedar, OAuth/OIDC, SPIFFE/SPIRE | Policy binding and decision records; do not define policy language. |
| Supply-chain evidence | in-toto, DSSE, Sigstore, SLSA, SPDX, CycloneDX | Evidence envelope and binding; do not define attestation or SBOM format. |
| Observability | OpenTelemetry traces/logs/metrics | Evidence input; do not define tracing protocol. |
| Data plane | Arrow, Arrow Flight, object stores, content-addressed storage | Artifact data-plane binding; Core should remain control-plane. |
| Metadata/schema | JSON Schema, JSON-LD, SHACL, CodeMeta, Bioschemas | Schema and semantic binding candidates. |

## Candidate source labels

Use stable labels in future drafts:

```text
[MCP]
[A2A]
[SKILLS-OPENAI]
[SKILLS-ANTHROPIC]
[CWL]
[RO-CRATE]
[WORKFLOW-RUN-RO-CRATE]
[W3C-PROV]
[OCI-IMAGE]
[WASI]
[KUBERNETES]
[REAPI]
[TEMPORAL]
[PREFECT]
[OPA]
[CEDAR]
[IN-TOTO]
[SIGSTORE]
[SPDX]
[CYCLONEDX]
[OPENTELEMETRY]
[ARROW-FLIGHT]
[JSON-SCHEMA]
[JSON-LD]
```

## Minimum review record per source

Each reviewed source should eventually have a short record:

```markdown
### [SOURCE-LABEL]

- Source URL:
- Version/date reviewed:
- What it solves:
- What CAP-Core should reuse:
- What CAP-Core should not repeat:
- Gap relevant to CAP-Core:
- Proposed location: Core / Profile / Binding / External / Out of scope
```

## Baseline reviewed source records

These records satisfy the first writing-plan gate: at least one reviewed source
exists for each major adjacent category. "Reviewed" means the source was checked
for CAP-Core boundary placement on 2026-07-05, not that CAP-Core accepts the
source as normative.

### [MCP]

- Source URL: https://modelcontextprotocol.io/specification/2025-06-18
- Version/date reviewed: 2025-06-18 specification, reviewed 2026-07-05.
- What it solves: Standardized connection between LLM applications and external
  tools, data sources, prompts, and resources.
- What CAP-Core should reuse: Discovery and invocation binding references for
  interactive tools or resources.
- What CAP-Core should not repeat: JSON-RPC transport, tool protocol, prompt
  protocol, or host-client connection behavior.
- Gap relevant to CAP-Core: MCP does not define a cross-standard artifact,
  runtime, policy, run, and evidence assembly object.
- Proposed location: Binding / External.

### [A2A]

- Source URL: https://github.com/a2aproject/A2A
- Version/date reviewed: Repository current as of 2026-07-05.
- What it solves: Agent-to-agent communication and interoperability between
  agentic applications.
- What CAP-Core should reuse: Optional inter-agent transport or collaboration
  binding.
- What CAP-Core should not repeat: Agent message transport, agent card
  discovery, or multi-agent protocol semantics.
- Gap relevant to CAP-Core: Agent communication does not by itself assemble
  artifacts, capabilities, runtime/resource bindings, policy decisions, and run
  evidence.
- Proposed location: Binding / External.

### [SKILLS-OPENAI]

- Source URL: https://developers.openai.com/codex/skills
- Version/date reviewed: Codex Skills documentation, reviewed 2026-07-05.
- What it solves: Progressive disclosure of reusable instructions, scripts,
  references, and assets for agent tasks.
- What CAP-Core should reuse: Procedure-package references when an assembly needs
  human-maintained operational knowledge.
- What CAP-Core should not repeat: Skill file layout, skill selection rules, or
  agent instruction loading behavior.
- Gap relevant to CAP-Core: A skill is not a machine-verifiable capability,
  runtime, policy, or evidence contract.
- Proposed location: Profile / Binding / External.

### [SKILLS-ANTHROPIC]

- Source URL: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Version/date reviewed: Agent Skills documentation, reviewed 2026-07-05.
- What it solves: Reusable agent procedures with optional scripts and resources.
- What CAP-Core should reuse: Skill package references as procedure or operator
  guidance attached to a capability.
- What CAP-Core should not repeat: Skill packaging semantics or agent-specific
  loading behavior.
- Gap relevant to CAP-Core: Skills guide an agent but do not define the
  complete object assembly contract for execution and evidence.
- Proposed location: Profile / Binding / External.

### [CWL]

- Source URL: https://www.commonwl.org/v1.2/
- Version/date reviewed: CWL v1.2.1 standards, reviewed 2026-07-05.
- What it solves: Portable command-line tool and workflow descriptions,
  including document schema and execution semantics for workflow composition.
- What CAP-Core should reuse: Workflow profile or binding when an Assembly points
  at a batch workflow.
- What CAP-Core should not repeat: Workflow language, step execution semantics,
  command-line binding semantics, or workflow engine behavior.
- Gap relevant to CAP-Core: CWL does not cover the full agent-facing assembly
  contract across policy decisions, live service bindings, and CAP-Digest views.
- Proposed location: Profile / Binding / External.

### [RO-CRATE]

- Source URL: https://www.researchobject.org/ro-crate/specification
- Version/date reviewed: RO-Crate specification site, reviewed 2026-07-05.
- What it solves: Packaging research data and metadata for distribution,
  reuse, publishing, preservation, and archiving.
- What CAP-Core should reuse: Archive/package binding and metadata profile.
- What CAP-Core should not repeat: RO-Crate packaging model or schema.org-based
  metadata conventions.
- Gap relevant to CAP-Core: RO-Crate is stronger for static packaging than live
  runtime/resource/policy binding.
- Proposed location: Profile / Binding / External.

### [WORKFLOW-RUN-RO-CRATE]

- Source URL: https://www.researchobject.org/workflow-run-crate/
- Version/date reviewed: Workflow Run RO-Crate working group site, reviewed
  2026-07-05.
- What it solves: RO-Crate profiles for capturing provenance of computational
  workflow executions.
- What CAP-Core should reuse: RunEvidence provenance profile and archive binding.
- What CAP-Core should not repeat: Workflow-run provenance vocabulary or crate
  layout.
- Gap relevant to CAP-Core: It does not define a general pre-run policy and
  resource assembly contract for non-workflow agent actions.
- Proposed location: Profile / Binding / External.

### [BAGIT]

- Source URL: https://www.rfc-editor.org/rfc/rfc8493.html
- Version/date reviewed: RFC 8493, reviewed 2026-07-05.
- What it solves: Hierarchical file package conventions for storage and transfer
  of arbitrary digital content.
- What CAP-Core should reuse: Archival or transfer-package binding where simple
  payload integrity is sufficient.
- What CAP-Core should not repeat: Bag layout, tag files, manifests, or payload
  transfer conventions.
- Gap relevant to CAP-Core: BagIt intentionally does not define payload internal
  semantics, execution, policy, or run evidence.
- Proposed location: Binding / External.

### [OCI-IMAGE]

- Source URL: https://specs.opencontainers.org/image-spec/
- Version/date reviewed: OCI Image Format Specification site, reviewed
  2026-07-05.
- What it solves: Container image manifests, indexes, layers, descriptors, and
  configuration.
- What CAP-Core should reuse: Runtime/environment references and content digest
  anchors.
- What CAP-Core should not repeat: Image format, layer model, descriptor schema,
  or distribution behavior.
- Gap relevant to CAP-Core: OCI defines image artifacts, not the whole
  capability, policy, resource, and run evidence assembly.
- Proposed location: Runtime Binding / External.

### [WASI]

- Source URL: https://wasi.dev/
- Version/date reviewed: WASI documentation, reviewed 2026-07-05.
- What it solves: Standards-track system interfaces for software compiled to
  WebAssembly.
- What CAP-Core should reuse: Runtime binding for WebAssembly component or
  sandboxed execution profiles.
- What CAP-Core should not repeat: WASI APIs, capability model, or component
  execution semantics.
- Gap relevant to CAP-Core: WASI does not describe artifact assembly, policy
  decisions, or evidence envelopes across other runtime types.
- Proposed location: Runtime Binding / External.

### [KUBERNETES]

- Source URL: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
- Version/date reviewed: Kubernetes resource management docs, reviewed
  2026-07-05.
- What it solves: Container orchestration and resource requests/limits for pods
  and containers.
- What CAP-Core should reuse: Runtime/resource binding targets for cluster jobs
  or services.
- What CAP-Core should not repeat: Scheduler behavior, pod spec semantics,
  cluster policy, or object API.
- Gap relevant to CAP-Core: Kubernetes is an execution substrate, not a
  cross-standard object assembly record.
- Proposed location: Runtime Binding / Resource Binding / External.

### [SLURM]

- Source URL: https://slurm.schedmd.com/documentation.html
- Version/date reviewed: Slurm 26.05 documentation site, reviewed 2026-07-05.
- What it solves: Cluster resource management and job scheduling for HPC.
- What CAP-Core should reuse: HPC runtime and resource binding references.
- What CAP-Core should not repeat: Queueing, allocation, job submission, or
  scheduler semantics.
- Gap relevant to CAP-Core: Slurm does not define domain artifact profiles,
  policy evidence, or CAP-Digest model-visible views.
- Proposed location: Runtime Binding / Resource Binding / External.

### [REAPI]

- Source URL: https://github.com/bazelbuild/remote-apis
- Version/date reviewed: Remote Execution API repository, reviewed 2026-07-05.
- What it solves: Remote caching and execution APIs, primarily for build/test
  actions.
- What CAP-Core should reuse: Remote execution binding for action-like runs.
- What CAP-Core should not repeat: CAS, action cache, execution API, or worker
  pool behavior.
- Gap relevant to CAP-Core: REAPI is not a general agent assembly contract and
  does not cover CAP-Digest or broad domain profiles.
- Proposed location: Runtime Binding / External.

### [OPA]

- Source URL: https://openpolicyagent.org/docs
- Version/date reviewed: OPA documentation, reviewed 2026-07-05.
- What it solves: Policy-as-code and Rego policy evaluation.
- What CAP-Core should reuse: Policy decision binding and audit references.
- What CAP-Core should not repeat: Rego, policy evaluation engine, deployment
  model, or policy authoring semantics.
- Gap relevant to CAP-Core: OPA can answer policy questions but does not define
  CAP artifact, capability, run, or evidence records.
- Proposed location: Policy Binding / External.

### [CEDAR]

- Source URL: https://docs.cedarpolicy.com/
- Version/date reviewed: Cedar policy language guide, reviewed 2026-07-05.
- What it solves: Authorization policies and authorization decisions.
- What CAP-Core should reuse: Policy decision binding for principal-action-
  resource authorization.
- What CAP-Core should not repeat: Cedar policy language or evaluation engine.
- Gap relevant to CAP-Core: Cedar is an authorization system, not an assembly
  or provenance model.
- Proposed location: Policy Binding / External.

### [OAUTH2-OIDC]

- Source URLs:
  - https://datatracker.ietf.org/doc/html/rfc6749
  - https://openid.net/specs/openid-connect-core-1_0.html
- Version/date reviewed: OAuth 2.0 RFC 6749 and OpenID Connect Core 1.0,
  reviewed 2026-07-05.
- What it solves: Delegated authorization and identity claims.
- What CAP-Core should reuse: Principal, consent, delegated authority, and token
  issuer references.
- What CAP-Core should not repeat: OAuth/OIDC flows, tokens, or identity
  provider behavior.
- Gap relevant to CAP-Core: Identity/authorization protocols do not define the
  object assembly or run evidence graph.
- Proposed location: Policy Binding / External.

### [SPIFFE]

- Source URL: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/
- Version/date reviewed: SPIFFE concepts docs, reviewed 2026-07-05.
- What it solves: Workload identity through SPIFFE IDs and SVIDs.
- What CAP-Core should reuse: Workload identity references in runtime or policy
  bindings.
- What CAP-Core should not repeat: SVID format, workload API, or SPIRE
  registration/attestation behavior.
- Gap relevant to CAP-Core: Workload identity does not define artifact,
  capability, assembly, or evidence objects.
- Proposed location: Policy Binding / Runtime Binding / External.

### [W3C-PROV]

- Source URL: https://www.w3.org/TR/prov-dm/
- Version/date reviewed: W3C PROV-DM Recommendation, reviewed 2026-07-05.
- What it solves: Conceptual provenance model for entities, activities, agents,
  and derivations.
- What CAP-Core should reuse: Provenance vocabulary or mapping profile for
  RunEvidence.
- What CAP-Core should not repeat: Full provenance ontology, serializations, or
  PROV inference model.
- Gap relevant to CAP-Core: PROV does not define pre-run assembly, runtime
  resource bindings, or CAP-Digest linkage.
- Proposed location: Evidence Binding / Profile / External.

### [MLFLOW]

- Source URL: https://mlflow.org/docs/latest/ml/tracking/
- Version/date reviewed: MLflow tracking documentation, reviewed 2026-07-05.
- What it solves: Experiment/run tracking for parameters, metrics, artifacts,
  and models.
- What CAP-Core should reuse: ML experiment profile and external tracking
  binding.
- What CAP-Core should not repeat: MLflow tracking server, APIs, model registry,
  or ML-specific run semantics.
- Gap relevant to CAP-Core: MLflow is domain-specific and does not cover generic
  policy-bound artifact assembly.
- Proposed location: Profile / Evidence Binding / External.

### [IN-TOTO]

- Source URL: https://in-toto.io/docs/specs/
- Version/date reviewed: in-toto specification page, reviewed 2026-07-05.
- What it solves: Supply-chain integrity and attestation framework for software
  supply-chain claims.
- What CAP-Core should reuse: Attestation references in RunEvidence or
  EvidenceBinding.
- What CAP-Core should not repeat: Attestation envelope, statement, predicate,
  layout, or verification behavior.
- Gap relevant to CAP-Core: Supply-chain attestation is one evidence family, not
  the full assembly contract.
- Proposed location: Evidence Binding / External.

### [SLSA]

- Source URL: https://slsa.dev/spec/v1.0/provenance
- Version/date reviewed: SLSA v1.0 provenance page, reviewed 2026-07-05.
- What it solves: Build provenance and supply-chain security expectations.
- What CAP-Core should reuse: Build provenance references for code or container
  artifacts used in a run.
- What CAP-Core should not repeat: SLSA levels, provenance predicate, or build
  platform requirements.
- Gap relevant to CAP-Core: SLSA focuses on software artifact supply chain, not
  all agent task assemblies.
- Proposed location: Evidence Binding / External.

### [SPDX]

- Source URL: https://spdx.dev/
- Version/date reviewed: SPDX project site, reviewed 2026-07-05.
- What it solves: SBOM and system package/data/security references.
- What CAP-Core should reuse: SBOM or dependency inventory binding.
- What CAP-Core should not repeat: SPDX model, license metadata, or SBOM
  format.
- Gap relevant to CAP-Core: SBOMs describe components, not runtime/policy/run
  lifecycle records.
- Proposed location: Evidence Binding / External.

### [CYCLONEDX]

- Source URL: https://cyclonedx.org/specification/overview/
- Version/date reviewed: CycloneDX specification overview, reviewed
  2026-07-05.
- What it solves: Full-stack Bill of Materials formats for software and related
  supply-chain data.
- What CAP-Core should reuse: BOM binding for components, services, models, or
  configurations.
- What CAP-Core should not repeat: BOM schema, VEX, or supply-chain metadata
  format.
- Gap relevant to CAP-Core: BOM data is an input to evidence, not a substitute
  for assembly or run evidence.
- Proposed location: Evidence Binding / External.

### [OPENTELEMETRY]

- Source URL: https://opentelemetry.io/docs/specs/otel/
- Version/date reviewed: OpenTelemetry specification site, reviewed
  2026-07-05.
- What it solves: Vendor-neutral traces, metrics, logs, baggage, and profiles.
- What CAP-Core should reuse: Observability references in RunEvidence.
- What CAP-Core should not repeat: Telemetry protocols, SDK behavior, semantic
  conventions, or collector pipelines.
- Gap relevant to CAP-Core: Telemetry is evidence input; it does not define the
  assembly object or policy decision record.
- Proposed location: Evidence Binding / External.

### [ARROW-FLIGHT]

- Source URL: https://arrow.apache.org/docs/format/Flight.html
- Version/date reviewed: Apache Arrow Flight RPC docs, reviewed 2026-07-05.
- What it solves: High-performance data service RPC over Arrow data streams.
- What CAP-Core should reuse: Data-plane binding for large tabular or columnar
  artifacts.
- What CAP-Core should not repeat: Arrow format, Flight RPC, stream tickets, or
  transfer protocol.
- Gap relevant to CAP-Core: Data transport does not define control-plane
  assembly, policy, or run evidence.
- Proposed location: Data-plane Binding / External.

### [JSON-LD]

- Source URL: https://www.w3.org/TR/json-ld11/
- Version/date reviewed: JSON-LD 1.1 Recommendation, reviewed 2026-07-05.
- What it solves: Linked Data serialization in JSON.
- What CAP-Core should reuse: Optional semantic graph profile or context mapping.
- What CAP-Core should not repeat: JSON-LD processing model or RDF mapping.
- Gap relevant to CAP-Core: JSON-LD supplies semantics but not execution,
  resource, policy, or evidence lifecycle.
- Proposed location: Profile / Binding / External.

### [JSON-SCHEMA]

- Source URL: https://json-schema.org/
- Version/date reviewed: JSON Schema project site, reviewed 2026-07-05.
- What it solves: JSON instance validation and schema vocabulary.
- What CAP-Core should reuse: First schema-sketch validation path.
- What CAP-Core should not repeat: Schema language or validator behavior.
- Gap relevant to CAP-Core: Schema validation alone does not define lifecycle,
  policy, or external binding meaning.
- Proposed location: Profile / External.

### [SHACL]

- Source URL: https://www.w3.org/TR/shacl/
- Version/date reviewed: SHACL Recommendation, reviewed 2026-07-05.
- What it solves: RDF graph validation against shapes.
- What CAP-Core should reuse: Optional validation profile when Core objects are
  represented as RDF/JSON-LD graphs.
- What CAP-Core should not repeat: Shapes language or RDF validation semantics.
- Gap relevant to CAP-Core: SHACL is validation, not a runtime or evidence
  contract.
- Proposed location: Profile / External.

### [CODEMETA]

- Source URL: https://codemeta.github.io/
- Version/date reviewed: CodeMeta project site, reviewed 2026-07-05.
- What it solves: Minimal software metadata vocabulary for research software
  discovery, citation, and interoperability.
- What CAP-Core should reuse: Code artifact metadata profile or binding.
- What CAP-Core should not repeat: Software citation metadata or CodeMeta
  crosswalks.
- Gap relevant to CAP-Core: Software metadata does not define capability
  execution, resource binding, or run evidence.
- Proposed location: Profile / Binding / External.

## Initial hypothesis

CAP-Core likely should be a **machine-operable object assembly contract** rather
than a tool protocol, workflow language, runtime, or provenance standard. This
hypothesis remains unaccepted until RFC-0001 is drafted and reviewed.
