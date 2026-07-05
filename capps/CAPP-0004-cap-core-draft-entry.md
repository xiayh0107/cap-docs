# CAPP-0004: CAP-Core Draft Entry

> Status: proposed - Created: 2026-07-05 - Layer: CAP-Core

## Abstract

This CAPP records the proposal that CAP-Core should proceed from reserved
planning material to a draft specification track, beginning with
`specs/core/RFC-0001.md`.

## Motivation

CAPP-0001 reserved CAP-Core because the repository needed to separate
CAP-Digest from a broader machine-operable assembly protocol. The first
CAP-Core writing cycle now has enough non-normative material to test that
broader layer without changing CAP-Digest:

- a research source map with baseline reviewed source records;
- a reviewed RFC-0001 outline;
- a boundary matrix;
- primitive reuse and gap review;
- external-standard binding policy;
- ontology and lifecycle drafts;
- security and policy draft;
- conformance and fixture plan;
- one end-to-end example assembly;
- open questions with owners and deferral decisions.

## Specification

CAP-Core work may proceed to a draft specification track under `specs/core/`
with these constraints:

- `specs/core/RFC-0001.md` is a draft proposal only.
- CAP-Core remains non-normative until a future CAPP accepts schemas, fixtures,
  and conformance language.
- CAP-Core must remain distinct from CAP-Digest terminology and conformance.
- CAP-Core must bind to external standards instead of redefining workflow,
  runtime, policy, provenance, attestation, SBOM, transport, or observability
  systems.
- CAP-Core fixtures and schemas must live in explicitly Core-scoped paths before
  any Core primitive becomes normative.

## Rationale

The writing plan's entry criteria for drafting RFC-0001 have been met in draft
form:

| Entry criterion | Evidence |
|---|---|
| At least one reviewed source per major adjacent category | `specs/core/RESEARCH-SOURCES.md` |
| Ontology names reviewed against CAP-Digest terminology | `specs/core/PRIMITIVE-REUSE.md` |
| Every proposed Core primitive has reuse or gap statement | `specs/core/PRIMITIVE-REUSE.md` |
| End-to-end example assembly without new runtime semantics | `specs/core/EXAMPLE-ASSEMBLY-0001.md` |
| Open questions have owners or deferral decisions | `specs/core/OPEN-QUESTIONS.md` |

Proceeding to a draft RFC is useful because it forces the object model,
lifecycle, and boundary decisions into one reviewable document. Keeping it
non-normative prevents accidental standardization before fixtures exist.

## Compatibility

This CAPP does not change CAP-Digest schemas, fixtures, packs, or reference
implementation behavior. Existing CAP-Digest documents remain the current
normative draft material.

## Security and Privacy

The proposal strengthens the CAP-Core draft by requiring explicit policy
decision records, secret-reference-only handling, resource/network constraints,
evidence integrity metadata, and clear separation from CAP-Digest evidence.

No new execution behavior is introduced by this CAPP.

## Reference Implementation

No runtime reference implementation is required for this CAPP. The smallest
future reference implementation should be a validator/renderer for Core records,
not an execution engine.

## Conformance Fixtures

No Core conformance fixture is accepted by this CAPP. The proposed first fixture
family is `fixtures/core/local-analysis/`, described in
`specs/core/CONFORMANCE-DRAFT.md`.
