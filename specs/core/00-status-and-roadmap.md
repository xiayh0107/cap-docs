# CAP-Core Status and Roadmap

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

This page standardizes how CAP-Core pages describe their status. It does not
promote any Core schema, fixture, or validator behavior.

## Status Terms

| Term | Meaning | Current examples |
|---|---|---|
| Draft proposal | Design text under review. It may change without compatibility promises. | `RFC-0001.md`, `RFC-0001-core-object-model.md` |
| Draft profile proposal | Profile-owned constraints over Core records. It does not change minimal Core. | `RFC-0003-scientific-computation-profile.md`, `RFC-0004-cap-digest-bridge-profile.md` |
| Candidate-prep draft | Executable review material prepared for a future CAPP decision. | `schemas/core/`, `fixtures/core/`, `reference/python/cap_core/` |
| Candidate normative | A future state allowed only after the promotion CAPP accepts gates. | Not active |
| Normative | Accepted specification text or schema with explicit governance status. | Not active for CAP-Core |

## Current Scope

CAP-Core draft-track material covers the Core object model, profile drafts,
binding envelope, schema sketches, fixtures, validator, renderer, conformance
report, and interop harness. These assets are reviewable evidence only.

CAP-Digest remains the active digest profile. CAP-Core bridge material can
reference CAP-Digest views, but it does not alter digest text grammar,
DigestManifest semantics, or follow-up gate behavior.

## Stability Boundaries

- Core object schemas are candidate-prep sketches, not stable requirements.
- Core fixtures are executable examples and negative checks, not a release
  corpus.
- Validator and renderer outputs are reference behavior for review, not the
  specification itself.
- Profiles and bindings may add stricter rules only in their own namespace.
- Any candidate normative wording is gated by `capps/CAPP-0005-cap-core-candidate-normative-track.md`.

## Roadmap Link

Phase 8 is tracked by GitHub issue #30. The exit criteria are recorded in
`ROADMAP.md`, this status page, the Core conformance draft, and the candidate
readiness report.
