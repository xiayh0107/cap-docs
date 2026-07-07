# CAP-Core v1.0.x Maintenance Policy

> Status: stable v1.0 - Normative maintenance policy - Last updated: 2026-07-07

## Errata

Errata may clarify wording, correct examples, or fix manifest/report mistakes
without changing v1.0 semantics. Errata should be recorded in `CHANGELOG.md`
and linked from release notes.

## Patch Releases

v1.0.x patch releases may:

- fix documentation errors;
- add non-breaking optional metadata;
- correct fixture mistakes with an errata note;
- tighten tests for existing requirements;
- fix reference implementation defects.

v1.0.x patch releases must not remove required fields, change stable enum
meanings, weaken security findings, or change CAP-Digest behavior.

## Fixture Corrections

Fixture corrections require a dated note describing the previous behavior,
corrected behavior, affected conformance level, and whether reports changed.

## Security Corrections

Security corrections follow `SECURITY.md`. If a correction changes stable
validator behavior, publish an errata note and a patch release.

## Future Versions

v1.1 feature work or v2.0 breaking changes require new CAPPs. Profile-specific
work should stay profile-owned unless a CAPP moves repeated semantics into
minimal Core.
