# Roadmap

This roadmap keeps CAP-Digest executable and records CAP-Core's path from draft
preparation through the accepted v1.0.0 stable release.

## Phase 0 — Repository governance baseline

Goal: make the repository contribution-ready.

- [x] Add license.
- [x] Add contributing guide.
- [x] Add security policy.
- [x] Add code of conduct.
- [x] Add citation metadata.
- [x] Add changelog.
- [x] Add status table.
- [x] Add pull request template and issue templates.
- [x] Add CI skeleton.

## Phase 1 — CAPP process

Goal: make normative change control explicit.

- [x] Add `capps/README.md`.
- [x] Draft CAPP-0001 for the CAP-Digest / CAP-Core split.
- [x] Draft CAPP-0002 for initial schemas and fixtures.
- [x] Draft CAPP-0003 for the `table-basic` digest pack.
- [x] Propose CAPP-0004 for CAP-Core draft entry.
- [x] Use CAPP status in future normative changes.

## Phase 2 — First machine-readable contract

Goal: move CAP-Digest beyond prose-only specification.

- [x] Add initial `cap.manifest.v1.schema.json`.
- [x] Add initial `cap.contract_response.v1.schema.json`.
- [x] Add initial `cap.digest_patch.v1.schema.json`.
- [x] Add initial `cap.digest.v1.schema.json`.
- [x] Tighten schemas after the first fixture/reference implementation pass.

## Phase 3 — First conformance fixture

Goal: make one independent implementation comparison possible.

- [x] Add `fixtures/basic-table/`.
- [x] Include source, policy, expected digest, expected manifest, and expected validation output.
- [x] Add negative validation cases.
- [x] Add follow-up fixture.

## Phase 4 — Reference implementation alpha

Goal: provide an executable companion for the draft.

- [x] Add `reference/python/` skeleton.
- [x] Implement minimal table assembler.
- [x] Implement manifest generation.
- [x] Implement evidence validation.
- [x] Add follow-up gate implementation.
- [x] Emit full conformance report.

## Phase 5 — Digest pack ecosystem seed

Goal: test the pack model with one focused source-reading pack.

- [x] Add `packs/table-basic/` skeleton.
- [x] Add pack metadata and initial field definitions.
- [x] Add executable pack loading in the reference implementation.
- [x] Add pack-driven fixture.

## Phase 6 — CAP-Digest 0.1.0-alpha

Exit criteria:

- [x] Docs links pass.
- [x] Schemas validate.
- [x] `basic-table` fixture passes.
- [x] Reference implementation passes tests.
- [x] CAPP statuses are updated.
- [x] Changelog and status are updated.
- [x] `0.1.0-alpha` release checklist is prepared.
- [x] Release tag created.

## Phase 7 - CAP-Core draft track

Goal: test CAP-Core as a draft assembly contract without making it normative.

- [x] Add CAP-Core writing plan.
- [x] Add research source map with baseline reviewed source records.
- [x] Add boundary matrix, ontology draft, lifecycle draft, and example assembly.
- [x] Add primitive reuse review and external-standard binding policy.
- [x] Add security/policy draft and conformance fixture plan.
- [x] Add `specs/core/RFC-0001.md` as a draft proposal.
- [x] Add CAPP-0004 to record whether CAP-Core should proceed to a draft specification.
- [x] Draft Core JSON schema sketches under a Core-scoped schema path.
- [x] Add `fixtures/core/local-analysis/`.
- [x] Add a Core validator/renderer reference prototype.
- [x] Mark CAPP-0004 implemented for CAP-Core draft entry.
- [x] Add a second Core fixture, `fixtures/core/build-test/`, before any
  normative promotion.
- [x] Resolve artifact-set and policy-decision schema boundaries as Core-scoped
  schema sketches.
- [x] Split CAP-Core RFC-0001 into Core object-model, binding-model, scientific
  computation profile, and CAP-Digest bridge profile drafts.

CAP-Core now has a complete draft-track artifact set. Do not treat the Core
schemas, runtime binding, RunEvidence, service binding, or policy model as
stable normative requirements until a later CAPP promotes them beyond draft
track.

## Phase 8 - CAP-Core candidate normative preparation

Goal: prepare CAP-Core for candidate normative review without promoting it.
Tracker: [#30](https://github.com/xiayh0107/cap-docs/issues/30).

- [x] Draft CAPP-0005 for candidate normative promotion gates.
- [x] Define candidate-prep conformance levels L0-L4.
- [x] Define Core schema versioning and compatibility rules.
- [x] Add a non-local `fixtures/core/remote-service-binding/` fixture.
- [x] Add a systematic `fixtures/core/negative/` suite.
- [x] Add a Core security, privacy, and trust threat model.
- [x] Add a stable draft Core conformance report format.
- [x] Wire Core draft checks into CI.
- [x] Triage CAP-Core open questions for candidate-prep blockers.
- [x] Promote the eight Core object schema sketches to candidate-prep review
  rules with negative coverage and validator error codes.
- [x] Define normative-language, status, secret-reference, profile governance,
  registry, terminology, renderer, interop, and implementer-guide documents.
- [x] Prepare candidate review artifacts and a dated readiness report.

Exit criteria:

- CAPP-0005 promotion gates are either satisfied or explicitly deferred.
- All minimal Core object schemas have positive and negative fixture coverage.
- Core draft CI emits validator and fixture reports.
- Security, service binding, policy, and RunEvidence boundaries are reviewed.
- Candidate review artifacts and readiness report are recorded before any
  normative promotion.

## Phase 9 - CAP-Core candidate normative review and v1.0 stable release

Goal: run candidate normative review and publish CAP-Core v1.0.0 stable after
all stable-track gates pass.
Trackers: [#61](https://github.com/xiayh0107/cap-docs/issues/61) and
[#62](https://github.com/xiayh0107/cap-docs/issues/62).

- [x] Open the candidate review decision issue.
- [x] Propose CAPP-0006 for CAP-Core candidate normative review entry.
- [x] Accept CAPP-0006 and record the candidate review disposition.
- [x] Freeze v1.0 scope, conformance, schema, fixture, validator, renderer,
  security, policy/service, RunEvidence, bridge, and registry baselines.
- [x] Add v1.0 release-gate manifest validation.
- [x] Record second implementation L0-L2 evidence, L3 evidence, and L4
  comparison evidence.
- [x] Prepare `cap-core-v1.0.0-rc1` and complete RC blocker triage.
- [x] Accept CAPP-0007 for CAP-Core v1.0.0 stable release.
- [x] Publish `release-artifacts/cap-core-v1.0.0/` and tag `cap-core-v1.0.0`.
- [x] Establish v1.0.x maintenance and errata policy.

CAP-Core v1.0.0 remains limited to the minimal Core control-plane object
contract. CAP-Digest behavior is unchanged.

## Phase 10 - Post-release maintenance

Goal: maintain CAP-Core v1.0.x without expanding the v1.0.0 stability claim,
and keep any future CAP-Digest stable work on an independent track.

Trackers:

- [#88](https://github.com/xiayh0107/cap-docs/issues/88) - Maintain
  CAP-Core v1.0.x errata and patch releases.
- [#89](https://github.com/xiayh0107/cap-docs/issues/89) - Collect external
  CAP-Core L4 interoperability feedback.
- [#90](https://github.com/xiayh0107/cap-docs/issues/90) - Guard CAP-Core
  v1.0.0 stable scope boundaries.
- [#91](https://github.com/xiayh0107/cap-docs/issues/91) - Keep CAP-Digest
  stable planning independent from Core v1.0.0.
- [#92](https://github.com/xiayh0107/cap-docs/issues/92) - Digest stable track:
  plan CAP-Digest stable independently from Core v1.x.

- [x] Record the initial v1.0.x maintenance audit and defer a patch release
  because no open errata require one.
- [x] Close the initial external implementation feedback window with no
  external reports received; do not make broader ecosystem L4 claims.
- [x] Keep runtime execution, policy language semantics, credential exchange,
  scientific correctness, and CAP-Digest behavior outside the Core v1.0.0
  stability claim.
- [x] Route any CAP-Digest stable effort through Digest-specific gates,
  fixtures, review records, and release artifacts.

Initial maintenance audit:
`specs/core/reviews/2026-07-07-post-release-maintenance-audit.md`.
