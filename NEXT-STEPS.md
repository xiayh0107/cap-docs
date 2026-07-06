# Next Steps Execution Plan

> Status: planning · Last updated: 2026-07-06

This document captures the next execution plan after the recent CAP-Digest and
CAP-Core draft-track updates.

The project has entered a new phase:

- CAP-Digest has enough schema, fixture, reference implementation, security, and
  governance coverage to prepare a `0.1.0-alpha` release.
- CAP-Core has a non-normative draft-track artifact set, including RFC-0001,
  schemas, fixtures, and a prototype reader/renderer, but it is not ready for
  normative promotion.

The next phase should therefore focus on **release discipline** and
**conformance hardening**, not broad feature expansion.

## Operating principles

1. **Freeze before expanding.** CAP-Digest should reach `0.1.0-alpha` before new
   source types or large protocol additions are accepted.
2. **Conformance before ecosystem growth.** A deterministic conformance report is
   more valuable than adding another half-specified fixture or pack.
3. **CAP-Core remains draft-track.** CAP-Core may be reviewed, minimized, and
   tested, but should not be promoted to normative status until a future CAPP
   explicitly accepts that promotion.
4. **No layer mixing.** CAP-Digest release work must not introduce CAP-Core
   runtime binding, RunEvidence, service binding, or policy model requirements.
5. **Every step should be executable.** Each issue derived from this plan should
   include commands, acceptance criteria, and non-goals.

## Priority 0 — Release CAP-Digest 0.1.0-alpha

Goal: publish the first alpha release of CAP-Digest using the already prepared
release checklist.

Scope:

- create or use a release branch;
- run pre-tag validation commands from `RELEASE-CHECKLIST.md`;
- generate `conformance-report.json`;
- update release notes and status files if needed;
- tag the release as `cap-digest-0.1.0-alpha`;
- publish GitHub release notes.

Do not add new source types, new Core primitives, or new schema families during
this freeze.

## Priority 1 — Harden conformance after alpha

Goal: make it possible for an external implementer to clone the repository,
run one command, and receive a deterministic conformance report.

Scope:

- validate every fixture JSON object against its intended schema;
- validate conformance reports against their schema;
- make fixture compatibility policy executable in CI;
- upload or store conformance report artifacts;
- document how implementation authors should compare their outputs.

## Priority 2 — Package release artifacts

Goal: make releases consumable without asking readers to infer which files
matter.

Scope:

- package schema files;
- package fixture families;
- package reference conformance report;
- include release notes and known limitations;
- document what is normative, draft, experimental, and non-normative.

## Priority 3 — Review CAP-Core object minimization

Goal: prevent CAP-Core from becoming an over-broad universal graph.

Review questions:

- Is `Assembly` the correct root object?
- Should `Binding` remain generic, or should runtime/resource/service/policy
  bindings be separate top-level objects?
- Is `Capability` too close to tool metadata?
- Is `RunEvidence` too close to PROV, in-toto, or RO-Crate?
- Which Core objects can be deferred to profiles or bindings?

## Priority 4 — Validate the CAP-Core local-analysis fixture

Goal: test whether CAP-Core adds value beyond a simple combination of existing
standards.

Review questions:

- Does `fixtures/core/local-analysis/` prove that Core connects artifact,
  capability, runtime, resource, policy, run, and evidence concerns?
- Does it avoid defining workflow, runtime, policy, or provenance semantics?
- Does it cleanly bridge to CAP-Digest without confusing RunEvidence and
  DigestEvidence?
- What conformance level does it actually test?

## Priority 5 — Decide CAP-Core RFC split

Goal: decide whether CAP-Core RFC-0001 should remain a single document or split
into a small family of RFCs.

Candidate split:

```text
RFC-0001 Core object model
RFC-0002 Binding model
RFC-0003 Scientific computation profile
RFC-0004 CAP-Digest bridge profile
```

A split should happen only if it reduces coupling and makes review easier.

## Suggested execution order

```text
1. Release CAP-Digest 0.1.0-alpha
2. Harden fixture/schema/conformance validation
3. Package release artifacts
4. Review CAP-Core object minimization
5. Validate CAP-Core local-analysis fixture
6. Decide CAP-Core RFC split
```

## Exit criteria for this plan

This plan is complete when:

- `cap-digest-0.1.0-alpha` is tagged and released;
- conformance validation is deterministic and documented;
- release artifacts are packaged or clearly identified;
- CAP-Core object minimization has a documented review outcome;
- the local-analysis fixture has a review outcome;
- the CAP-Core RFC split decision is recorded.
