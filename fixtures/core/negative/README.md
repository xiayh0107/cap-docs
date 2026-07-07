# CAP-Core negative suite

This suite collects CAP-Core v1.0 negative cases that are not tied to one
positive fixture family. Each JSON case is a validator harness document with an
expected error code recorded in `expected-validation.json`.

The cases map to v1.0 conformance levels in
`specs/core/CONFORMANCE-v1.0.md` and are part of the v1.0 release package.

Current coverage includes artifact identity/integrity, capability-not-
authorization, binding role/status and secret safety, Assembly graph closure,
fail-closed policy behavior, Run lifecycle records, RunEvidence overclaim
boundaries, DigestBinding separation, and external-standard boundary checks.
