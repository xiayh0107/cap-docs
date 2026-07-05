# Contributing to CAP

CAP is maintained as a specification repository. Contributions are welcome, but every change must preserve the boundary between the current CAP-Digest profile and the reserved CAP-Core layer.

## Before opening a pull request

Ask first:

> Is this refining CAP-Digest, or does it actually belong in CAP-Core?

Use this rule consistently:

- CAP-Digest changes belong under `specs/digest/`, `schemas/`, `fixtures/`, `packs/`, or `reference/`.
- CAP-Core material belongs only in `specs/core/README.md` or `notes/` until the CAP-Core process formally starts.
- Non-normative analysis belongs in `notes/`.
- Repository process, CI, and maintenance files belong at the root or under `.github/`.

## Contribution types

Common contribution types:

- editorial fixes;
- normative CAP-Digest clarifications;
- JSON schema changes;
- conformance fixtures;
- reference implementation changes;
- digest pack proposals;
- non-normative research notes;
- repository governance and CI changes.

## Normative changes and CAPPs

Substantial CAP-Digest changes should use a CAP-Digest Proposal (`CAPP`). A CAPP is expected for:

- new primitives;
- breaking schema changes;
- changes to digest text grammar;
- new normative security requirements;
- feature deprecation or removal;
- governance changes.

A CAPP should include a problem statement, specification, rationale, compatibility analysis, security/privacy analysis, and at least one reference implementation or executable fixture when applicable.

## Pull request checklist

Every pull request should explain:

- which layer it changes;
- whether it changes normative behavior;
- whether it requires a CAPP;
- compatibility impact;
- security/privacy impact;
- fixture or reference implementation impact.

## Review expectations

Maintainers may ask contributors to split a PR if it mixes normative spec changes with research notes, implementation changes, or CAP-Core concepts. Prose-only changes are welcome, but executable fixtures and schema-backed changes are preferred when changing behavior.

## Development setup

The repository is still early. Current planned executable assets are:

- JSON schemas in `schemas/`;
- conformance fixtures in `fixtures/`;
- digest packs in `packs/`;
- a minimal reference implementation in `reference/python/`.

Run local checks before opening a PR once the corresponding scripts exist:

```bash
python -m pytest reference/python/tests
python reference/python/scripts/validate_fixtures.py
```

## Licensing

By contributing, you agree that your contribution is licensed under the repository license.
