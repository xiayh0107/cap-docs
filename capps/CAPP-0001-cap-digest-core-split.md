# CAPP-0001: CAP-Digest / CAP-Core Split

> Status: draft · Created: 2026-07-05 · Layer: repository governance

## Abstract

This CAPP records the repository-level decision to treat the current drafted specification as **CAP-Digest**, a context evidence layer, while reserving **CAP-Core** for future research and specification work.

## Motivation

Earlier drafts risked conflating two different layers:

1. CAP-Digest: safely rendering source objects into model-readable context with stable evidence anchors and gated follow-up.
2. CAP-Core: a future upper layer for machine-operable artifact graphs, capability/runtime binding, policy decisions, run lifecycle, and RunEvidence.

Keeping these separate prevents CAP-Digest from becoming an over-broad protocol before it has executable fixtures and a reference implementation.

## Specification

The repository maintains these layer rules:

- `specs/digest/` is the current normative CAP-Digest draft.
- `specs/core/` is reserved and non-normative until a future CAPP starts CAP-Core work.
- `notes/` is non-normative.
- `schemas/`, `fixtures/`, `packs/`, and `reference/` support CAP-Digest unless explicitly documented otherwise.
- Every pull request must classify whether it changes CAP-Digest, CAP-Core research material, or repository maintenance.

CAP-Core concepts must not be added to CAP-Digest as normative requirements unless a future CAPP explicitly defines the boundary and compatibility impact.

## Rationale

CAP-Digest can become useful quickly if it is small, testable, and grounded in source object reading. CAP-Core is a larger research problem that must account for existing standards such as MCP, Skills, CWL, RO-Crate, OCI, WASI, Kubernetes, REAPI, Sigstore, in-toto, SPDX, CycloneDX, OPA, and Cedar.

## Compatibility

This CAPP formalizes the current repository structure. It does not change CAP-Digest artifact behavior.

## Security and Privacy

The split reduces overclaiming. CAP-Digest security claims remain limited to context artifacts, redaction, escaping, evidence anchors, and gated follow-up. CAP-Core security is not specified yet.

## Reference Implementation

No reference implementation is required for this governance CAPP.

## Conformance Fixtures

No conformance fixtures are required for this governance CAPP.
