# CAP-Core v1.0 RunEvidence Requirements

> Status: stable v1.0 - Normative - Last updated: 2026-07-07

RunEvidence records structural evidence about a Run. They do not prove result
correctness, scientific validity, remote service correctness, or complete
provenance.

## Required Surface

RunEvidence records include run id, subject, materials, products, logs, records,
completeness, integrity, and optional attestations, provenance refs, SBOM refs,
telemetry refs, and digest views.

Implementations claiming L3 MUST validate Run/RunEvidence links, material and
product refs, logs, digest views, limitations, and overclaim findings.

## Limitations and Gaps

Remote or unverifiable surfaces SHOULD be represented in records or limitations
and reported with `remote_unverifiable_surface` when applicable.

## Evidence Separation

DigestEvidence is CAP-Digest evidence. It MUST NOT be substituted for
RunEvidence. DigestBinding may connect RunEvidence to a CAP-Digest view only
when `constraints.sourceRunEvidence` points to the RunEvidence id and
`constraints.digestEvidenceIsRunEvidence` is `false`.
