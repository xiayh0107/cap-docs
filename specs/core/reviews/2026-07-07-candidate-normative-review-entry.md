# CAP-Core Candidate Normative Review Entry

> Status: proposed review agenda - Non-normative - Date: 2026-07-07

This review agenda supports GitHub issue #61 and CAPP-0006. It records the
decision inputs and acceptance checks for opening CAP-Core candidate normative
review. It does not promote CAP-Core by itself.

## Decision Inputs

| Input | Evidence |
|---|---|
| Gate definition | `capps/CAPP-0005-cap-core-candidate-normative-track.md` |
| Review-entry proposal | `capps/CAPP-0006-cap-core-candidate-normative-review-entry.md` |
| Readiness recommendation | `specs/core/reviews/2026-07-07-candidate-readiness.md` |
| Candidate package | `release-artifacts/core-candidate-review/` |
| Core schemas | `schemas/core/` |
| Fixture suite | `fixtures/core/` |
| Reference implementation | `reference/python/cap_core/` |
| CI evidence | commit `b4ce530`, workflows `docs`, `schemas`, `conformance`, `core-draft`, `reference` |
| Conformance report | `release-artifacts/core-candidate-review/reports/core-conformance-report.json` |
| Interop report | `release-artifacts/core-candidate-review/reports/core-interop-reference.json` |

## Review Questions

- Do CAPP-0005 gates have sufficient evidence to start candidate normative
  review?
- Are any blockers present that should keep CAP-Core draft-track?
- Is the reference implementation plus external interop harness enough for
  review entry, with a second implementation report treated as non-blocking?
- Are CAP-Core and CAP-Digest boundaries clear enough to avoid accidental
  digest behavior changes?
- Are security and secret/service binding boundaries explicit enough for
  candidate review?

## Decision Options

| Option | Meaning |
|---|---|
| Accept review entry | Move CAP-Core into candidate normative review while keeping assets non-stable. |
| Keep draft-track | Do not enter candidate review; keep CAPP-0006 proposed or defer it. |
| Request evidence | Keep review open and require named evidence, such as a second implementation report. |
| Split blockers | Open focused CAPPs or issues for blocking concerns. |

## Required Non-Goals

- No stable CAP-Core release.
- No stable schema guarantee.
- No normative RunEvidence or Binding requirements outside candidate review.
- No CAP-Digest grammar, manifest, or follow-up gate changes.

## Proposed Initial Finding

Initial finding: the repository is ready to open candidate normative review
because Phase 8 evidence satisfies CAPP-0005 gates and the readiness report
records no blockers. The review should remain open until maintainers explicitly
accept, defer, or revise CAPP-0006.
