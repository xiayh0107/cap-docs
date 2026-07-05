# CAP-Core Research Sources

> Status: planning · Non-normative · Last updated: 2026-07-05

This file lists the source categories that must be reviewed before CAP-Core
RFC-0001 is drafted. It is a source map, not a completed literature review.

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

## Initial hypothesis

CAP-Core likely should be a **machine-operable object assembly contract** rather
than a tool protocol, workflow language, runtime, or provenance standard. This
hypothesis remains unaccepted until RFC-0001 is drafted and reviewed.
