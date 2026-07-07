# Repository Guidelines

## Project Structure & Module Organization

This repository contains draft CAP specifications and executable fixtures.
Primary spec text lives in `specs/digest/` for CAP-Digest and `specs/core/` for
the non-normative CAP-Core draft track. JSON Schemas are in `schemas/`, with
Core sketches under `schemas/core/`. Fixture families live in `fixtures/`.
Experimental Python helpers and tests live under `reference/python/`, including
`cap_digest/`, `cap_core/`, `scripts/`, and `tests/`. Digest Pack assets are in
`packs/`; governance proposals are in `capps/`; design notes are in `notes/`.

## Build, Test, and Development Commands

Run commands from the repository root:

```bash
python -m unittest discover reference/python/tests
python reference/python/scripts/validate_schema_fixtures.py
python reference/python/scripts/validate_fixtures.py
python reference/python/scripts/validate_fixtures.py --report conformance-report.json
python reference/python/scripts/validate_core_fixtures.py --report core-conformance-report.json
git diff --check
```

The unit tests cover the experimental reference implementation. Schema fixture
validation checks mapped fixture JSON against active schema sketches. Fixture
validation verifies expected digest, follow-up, pack, security, and Core draft
behavior. The Core report command emits the candidate-prep draft report used by
CI. `git diff --check` catches whitespace errors before commit.

## Coding Style & Naming Conventions

Use Markdown for specs and notes, JSON for schemas and fixtures, and Python 3.10+
for reference code. Keep Markdown headings descriptive and avoid presenting
CAP-Core draft-track material as stable conformance. Use snake_case for Python
names, lowercase hyphenated fixture directories such as `basic-table/`, and
schema names like `cap.core.run.v1.schema.json`. Prefer concise, explicit test
fixtures over prose-only claims.

## Testing Guidelines

Add or update tests in `reference/python/tests/` when changing reference
behavior. New fixture JSON should either be covered by
`validate_schema_fixtures.py` or documented there as intentionally no-schema.
When changing fixtures, update expected outputs and run both validation scripts.

## Commit & Pull Request Guidelines

Recent commits use short imperative summaries, for example `Fix Core progress
records` or `Complete CAP-Core follow-ups`. PRs should follow
`.github/pull_request_template.md`: include summary, change type, layer,
compatibility, security/privacy impact, and fixture/test status. Link issues
when relevant and state whether a CAPP is required.

## Security & Layer Boundaries

Never commit secrets or generated local credentials. For security-sensitive
reports, follow `SECURITY.md`. Every substantive change should preserve the
CAP-Digest / CAP-Core split: CAP-Digest is the active context evidence profile;
CAP-Core remains non-normative until a future accepted CAPP promotes it.
