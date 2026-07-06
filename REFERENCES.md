# References

This file records external standards, official documentation, and repository-local sources used as design basis for CAP-Digest. References are grouped by whether they inform current CAP-Digest normative text or are reserved for future CAP-Core work.

## CAP-Digest reference basis

| ID | Source | Role in CAP-Digest |
|---|---|---|
| [JSON-SCHEMA-2020-12] | JSON Schema Draft 2020-12, https://json-schema.org/draft/2020-12 | Schema dialect for CAP-Digest machine-readable artifacts. |
| [MCP-RESOURCES] | Model Context Protocol resources specification, https://modelcontextprotocol.io/specification/2025-06-18/server/resources | Distinguishes readable resources from tools; informs Digest Pack boundaries. |
| [MCP-TOOLS] | Model Context Protocol tools specification, https://modelcontextprotocol.io/specification/2025-06-18/server/tools | Used as a contrast: CAP-Digest follow-up requests are not tool execution. |
| [MCP-PROMPTS] | Model Context Protocol prompts specification, https://modelcontextprotocol.io/specification/draft/server/prompts | Informs explicit context surfaces and prompt-like artifacts without adopting MCP transport. |
| [GITHUB-SKILLS] | GitHub Copilot Agent Skills documentation, https://docs.github.com/copilot/concepts/agents/about-agent-skills | Informs progressive disclosure and description-driven pack discovery. |
| [OPENAI-SKILLS] | OpenAI Codex Skills documentation, https://developers.openai.com/codex/skills | Informs skill-style packaging patterns while keeping Digest Packs distinct from Skills. |
| [ANTHROPIC-SKILLS] | Anthropic Skills repository, https://github.com/anthropics/skills | Informs directory/frontmatter packaging practice and lazy loading. |
| [KUBERNETES-OBJECTS] | Kubernetes object model documentation, https://kubernetes.io/docs/concepts/overview/working-with-objects/ | Informs submitted-intent vs observed-status separation for ContractResponse, ValidationResult, and GateResult. |
| [KUBERNETES-API] | Kubernetes API concepts, https://kubernetes.io/docs/reference/using-api/api-concepts/ | Informs explicit object shape, status, and compatibility thinking. |
| [IN-TOTO-ATTESTATION] | in-toto Attestation Framework, https://github.com/in-toto/attestation/blob/main/spec/README.md | Informs typed envelope design for validation, gate, and conformance reports. |

## CAP-Core reserved reference basis

The following sources are important for future CAP-Core research. They should not be imported into CAP-Digest as normative runtime, workflow, provenance, policy, or supply-chain requirements.

| ID | Source | Reserved role |
|---|---|---|
| [CWL-1.2] | Common Workflow Language v1.2, https://www.commonwl.org/v1.2/ | Future workflow/batch profile reference. |
| [RO-CRATE-1.2] | RO-Crate 1.2, https://www.researchobject.org/ro-crate/specification/1.2/index.html | Future research object/archive profile reference. |
| [OCI-IMAGE] | OCI Image Format Specification, https://specs.opencontainers.org/image-spec/ | Future runtime artifact packaging reference. |
| [WASI] | WebAssembly System Interface, https://wasi.dev/ | Future sandbox/runtime binding reference. |
| [REAPI] | Bazel Remote Execution API, https://github.com/bazelbuild/remote-apis | Future remote execution binding reference. |
| [SIGSTORE] | Sigstore specifications, https://docs.sigstore.dev/cosign/system_config/specifications/ | Future signing/attestation binding reference. |
| [SPDX] | SPDX specifications, https://spdx.dev/use/specifications/ | Future SBOM/license metadata reference. |
| [CYCLONEDX] | CycloneDX standard, https://cyclonedx.org/ | Future BOM/supply-chain metadata reference. |
| [OPA] | Open Policy Agent documentation, https://openpolicyagent.org/docs | Future policy decision binding reference. |
| [CEDAR] | Cedar policy language paper, https://www.amazon.science/publications/cedar-a-new-language-for-expressive-fast-safe-and-analyzable-authorization | Future authorization-policy research reference. |

## Repository-local source basis

| ID | Source | Role |
|---|---|---|
| [CAP-README] | `README.md` | Repository scope and CAP-Digest / CAP-Core split. |
| [CAP-OVERVIEW] | `specs/digest/00-overview.md` | CAP-Digest profile boundary. |
| [CAP-COGNITIVE-CORRECTION] | `notes/2026-07-05-cognitive-error-and-framework.md` | Non-normative rationale for keeping CAP-Core reserved. |
| [CAP-ROADMAP] | `ROADMAP.md` | Release and implementation roadmap. |
| [CAP-STATUS] | `STATUS.md` | Current artifact status and implementation target. |
