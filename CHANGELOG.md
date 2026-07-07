# Changelog

All notable changes to this repository will be documented here.

This project currently tracks a draft CAP-Digest profile and CAP-Core v1.0.0
stable artifacts.

## Unreleased

### Added

- Added CAP-Core v1.0.0 stable release materials: CAPP-0007, stable scope,
  conformance, schema package, fixture index, validator code registry,
  inspection report format, security requirements, policy/service boundary,
  RunEvidence requirements, CAP-Digest bridge boundary, registry snapshot,
  maintenance policy, RC1 package, final release package, interop reports, and
  release manifest validation.
- Added post-release maintenance tracking for CAP-Core v1.0.x errata/patch
  releases, external L4 interoperability feedback, Core v1.0.0 scope
  guardrails, and a separate CAP-Digest stable planning route.
- Added CAPP-0006 and a CAP-Core candidate normative review-entry agenda for
  issue #61, preserving CAP-Digest behavior during review.
- Added CAP-Core candidate-prep schema rules, normative-language policy,
  status map, secret/service binding safety model, inspection report schema,
  interoperability report schemas, profile/binding registry, profile
  governance, terminology collision audit, implementer guide, candidate review
  package, and readiness report.
- Added Core inspection and interoperability CLI scripts plus tests for renderer
  diagnostics, Digest bridge separation, and report comparison.
- Added CAP-Core Phase 8 candidate-prep assets: CAPP-0005, L0-L4 conformance
  levels, schema versioning rules, security threat model, remote-service-binding
  fixture, systematic negative suite, Core conformance report schema, Core
  validator report command, and Core draft CI workflow.
- Added a second CAP-Core executable draft fixture, `fixtures/core/build-test/`,
  covering a software build/test scenario with Core validation and negative
  fixture coverage.
- Added Core-scoped schema sketches for artifact sets and policy decisions.
- Split the CAP-Core RFC-0001 material into object-model, binding-model,
  scientific-computation-profile, and CAP-Digest bridge profile drafts.
- Added a CAP-Core policy/artifact-set boundary decision note.

### Changed

- Expanded Core fixture validation, schema-fixture validation, tests, and
  conformance reporting to cover the Core fixture suites.
- Updated Core documentation to keep artifact-set, policy-decision, binding,
  and profile boundaries explicit through the v1.0 stable release.
- Synced project status, Core README, FAQ, maintenance guidance, release
  checklist status, and citation metadata with the post-alpha CAP-Core
  draft-track state.

## cap-digest-0.1.0-alpha - 2026-07-06

### Added

- Repository governance baseline: license, contributing guide, security policy, code of conduct, citation metadata, status, roadmap, issue templates, pull request template, and CI skeleton.
- CAPP process directory and initial proposal drafts.
- Initial machine-readable schema skeletons for CAP-Digest artifacts.
- Initial `basic-table` conformance fixture.
- Initial `table-basic` digest pack skeleton.
- Initial Python reference implementation skeleton.
- Reference source registry in `REFERENCES.md`.
- Draft field, field catalog, validation result, gate result, digest pack, and pack conformance schemas.
- Draft `catalog-table-basic`, `followup-basic`, and `pack-table-basic` fixture families.
- CAP-Core writing plan completion set: RFC-0001 draft proposal, reviewed source
  map, boundary matrix, primitive reuse review, binding policy, ontology draft,
  lifecycle draft, security/policy draft, conformance plan, example assembly,
  open-question dispositions, and CAPP-0004 draft-entry proposal.
- CAP-Core executable draft-track assets: schema sketches under `schemas/core/`,
  `fixtures/core/local-analysis/`, negative Core fixtures, and a Python
  validator/renderer prototype.
- CAP-Digest follow-up fixture, negative validation cases, table-basic pack
  loading, pack fixture, and conformance report generation.
- CAP-Digest security adversarial fixtures and alpha release checklist.

### Changed

- Future normative changes should go through the CAPP process when they alter behavior, schemas, digest grammar, security requirements, deprecations, or governance.
- `05-field-model-and-assembly.md` now defines serialized fields, field catalogs, field ID grammar, level rules, candidate expansion, and implementation contracts.
- `06-digest-text-format.md` now defines a minimal grammar, parser behavior, data fence rules, and manifest/text consistency checks.
- `09-followup-contract-and-gate.md` now defines ValidationResult, GateResult, reserved error codes, and typed digest patch semantics.
- `10-digest-packs.md` now defines pack frontmatter schema, status lifecycle, deterministic discovery, trust/activation policy, and pack conformance reports.
- `cap.digest_patch.v1.schema.json` now uses typed patch operations instead of free-form text append.
- CAPP-0002 and CAPP-0003 are implemented by the current schema, fixture,
  reference implementation, and pack assets.
- `11-versioning-conformance-governance.md` now defines CAPP status lifecycle,
  release lifecycle, version bump rules, compatibility rules, and alpha release
  readiness criteria.

### Security

- Added project-level security reporting guidance for CAP-Digest redaction, escaping, guarded extraction, and gate validation issues.

## 2026-07-05-draft

### Added

- Initial CAP-Digest draft specification under `specs/digest/`.
- Reserved CAP-Core placeholder under `specs/core/`.
- Non-normative notes documenting the CAP-Digest / CAP-Core split and retained research context.
