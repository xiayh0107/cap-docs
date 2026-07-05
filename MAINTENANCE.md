# Maintenance Plan

This repository is maintained as a draft specification project.

## Goals

1. Keep CAP-Digest small, executable, and testable.
2. Keep CAP-Core reserved until a future research and CAPP process starts.
3. Prefer schemas, fixtures, and reference implementation checks over prose-only claims.
4. Route substantial normative changes through CAPPs.

## Weekly routine

- Triage new issues.
- Classify issues by area, type, status, and priority.
- Review pull requests for the CAP-Digest / CAP-Core boundary.
- Check whether any normative change requires a CAPP.

## Monthly routine

- Review `STATUS.md`.
- Review `ROADMAP.md`.
- Run reference implementation tests.
- Check fixture drift against schemas and spec text.
- Update CAPP statuses.

## Release routine

Before a release:

- workflows should pass;
- `CHANGELOG.md` should be updated;
- `STATUS.md` should be updated;
- active CAPP statuses should be reviewed;
- conformance fixtures should be reproducible;
- CAP-Core should remain non-normative unless its process has started.

## Change policy

Small editorial changes do not require a CAPP. A CAPP is expected for:

- new primitives;
- breaking schema changes;
- digest grammar changes;
- new normative security requirements;
- feature deprecation or removal;
- governance changes.

## Definition of done

A normative CAP-Digest change is done only when:

- affected spec text is updated;
- compatibility is considered;
- security/privacy impact is considered;
- relevant schemas or fixtures are updated;
- reference implementation impact is considered;
- changelog entries are added when appropriate.
