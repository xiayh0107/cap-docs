# Changelog

All notable changes to this repository will be documented here.

This project currently tracks a draft CAP-Digest profile with CAP-Core reserved for future work.

## Unreleased

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

### Changed

- Future normative changes should go through the CAPP process when they alter behavior, schemas, digest grammar, security requirements, deprecations, or governance.
- `05-field-model-and-assembly.md` now defines serialized fields, field catalogs, field ID grammar, level rules, candidate expansion, and implementation contracts.
- `06-digest-text-format.md` now defines a minimal grammar, parser behavior, data fence rules, and manifest/text consistency checks.
- `09-followup-contract-and-gate.md` now defines ValidationResult, GateResult, reserved error codes, and typed digest patch semantics.
- `10-digest-packs.md` now defines pack frontmatter schema, status lifecycle, deterministic discovery, trust/activation policy, and pack conformance reports.
- `cap.digest_patch.v1.schema.json` now uses typed patch operations instead of free-form text append.

### Security

- Added project-level security reporting guidance for CAP-Digest redaction, escaping, guarded extraction, and gate validation issues.

## 2026-07-05-draft

### Added

- Initial CAP-Digest draft specification under `specs/digest/`.
- Reserved CAP-Core placeholder under `specs/core/`.
- Non-normative notes documenting the CAP-Digest / CAP-Core split and retained research context.
