# Roadmap

This roadmap keeps CAP-Digest executable while keeping CAP-Core non-normative
until schemas, fixtures, and conformance work justify normative Core text.

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
- [ ] Use CAPP status in future normative changes.

## Phase 2 — First machine-readable contract

Goal: move CAP-Digest beyond prose-only specification.

- [x] Add initial `cap.manifest.v1.schema.json`.
- [x] Add initial `cap.contract_response.v1.schema.json`.
- [x] Add initial `cap.digest_patch.v1.schema.json`.
- [x] Add initial `cap.digest.v1.schema.json`.
- [ ] Tighten schemas after the first fixture/reference implementation pass.

## Phase 3 — First conformance fixture

Goal: make one independent implementation comparison possible.

- [x] Add `fixtures/basic-table/`.
- [x] Include source, policy, expected digest, expected manifest, and expected validation output.
- [ ] Add negative validation cases.
- [ ] Add follow-up fixture.

## Phase 4 — Reference implementation alpha

Goal: provide an executable companion for the draft.

- [x] Add `reference/python/` skeleton.
- [x] Implement minimal table assembler.
- [x] Implement manifest generation.
- [x] Implement evidence validation.
- [ ] Add follow-up gate implementation.
- [ ] Emit full conformance report.

## Phase 5 — Digest pack ecosystem seed

Goal: test the pack model with one focused source-reading pack.

- [x] Add `packs/table-basic/` skeleton.
- [x] Add pack metadata and initial field definitions.
- [ ] Add executable pack loading in the reference implementation.
- [ ] Add pack-driven fixture.

## Phase 6 — CAP-Digest 0.1.0-alpha

Exit criteria:

- [ ] Docs links pass.
- [ ] Schemas validate.
- [ ] `basic-table` fixture passes.
- [ ] Reference implementation passes tests.
- [ ] CAPP statuses are updated.
- [ ] Changelog and status are updated.
- [ ] Release tag created.

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

CAP-Core now has a complete draft-track artifact set. Do not treat the Core
schemas, runtime binding, RunEvidence, service binding, or policy model as
stable normative requirements until a later CAPP promotes them beyond draft
track.
