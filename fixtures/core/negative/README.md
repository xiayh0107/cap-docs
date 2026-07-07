# CAP-Core negative suite

This suite collects candidate-prep negative cases that are not tied to one
positive fixture family. Each JSON case is a validator harness document with a
stable expected error code recorded in `expected-validation.json`.

The cases map to candidate conformance levels in
`specs/core/CONFORMANCE-DRAFT.md`. They are draft-track fixtures and do not
define stable CAP-Core conformance by themselves.

Current coverage includes artifact identity/integrity, capability-not-
authorization, binding role/status and secret safety, Assembly graph closure,
fail-closed policy behavior, Run lifecycle records, RunEvidence overclaim
boundaries, DigestBinding separation, and external-standard boundary checks.
