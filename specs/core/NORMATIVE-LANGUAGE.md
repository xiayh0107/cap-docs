# CAP-Core Normative Language Policy

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

This policy controls how future CAP-Core documents may use requirement
keywords. It does not make current Core drafts normative.

## Keyword Use

Future candidate or accepted Core text may use `MUST`, `MUST NOT`, `SHOULD`,
`SHOULD NOT`, and `MAY` only when the requirement is testable or has a dated
deferral. Draft proposal text should use descriptive language such as "is
intended to", "records", "declares", or "candidate check".

## Testability Rule

Every future `MUST`-level requirement needs at least one of:

- JSON Schema coverage;
- validator coverage with a stable error or warning code;
- positive and negative fixture coverage;
- an explicit deferral naming the missing test path.

Untestable prose belongs in rationale, examples, notes, or open questions.

## Core vs Profile vs Binding

Core requirements apply only to minimal Core records. Profiles may add stricter
constraints under profile-owned identifiers, fixture mappings, and validator
checks. Bindings may reference external standards, but external standard
semantics stay outside Core unless a CAPP explicitly moves a repeated pattern
into Core.

## Non-Normative Markers

Examples, rationale, decision notes, open questions, fixture READMEs, and
reference implementation comments should say "non-normative" when they could be
mistaken for a requirement.

## Current Audit

The current Core pages use draft/candidate-prep status blocks. The systematic
negative suite and validator use stable error codes for candidate review, but
the reports still identify themselves as draft-track material.
