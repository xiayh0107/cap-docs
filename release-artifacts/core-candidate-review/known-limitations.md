# CAP-Core Candidate Review Known Limitations

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

- No CAP-Core candidate normative release is published by this package.
- Schemas remain v1 draft sketches and can change through CAPP review.
- The reference implementation validates records and renders reports; it does
  not execute workflows, evaluate policy, fetch secrets, or call services.
- Interop evidence currently includes the reference implementation and the
  external harness path. A second implementation report can be added later
  using `specs/core/INTEROPERABILITY-HARNESS.md`.
- Security checks cover inline secret-looking values, service binding freshness,
  network declaration, and overclaim boundaries. They do not verify real
  credential managers, remote service correctness, signatures, SBOMs, or
  provenance graphs.
- The Scientific Computation Profile and CAP-Digest Bridge Profile remain
  profile drafts. They do not add requirements to CAP-Digest.
