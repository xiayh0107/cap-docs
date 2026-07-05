# Security Policy

CAP-Digest treats digest creation as potential data disclosure. Please report issues that could weaken redaction, escaping, guarded extraction, gate enforcement, or fixture/reference implementation safety.

## Supported versions

This repository is currently a draft. Security-sensitive reports should target the current `main` branch unless a release tag explicitly says otherwise.

## What to report

Please report:

- redaction bypasses;
- data escaping bypasses;
- digest text structures that allow source data to forge CAP tags;
- fixture data that accidentally exposes real secrets or personal data;
- reference implementation behavior that touches source data unsafely;
- gate validation bugs that allow unknown evidence or unapproved follow-up requests;
- schema ambiguities that could make unsafe behavior appear conforming.

## What is out of scope

These are usually not CAP-Digest security vulnerabilities by themselves:

- a model reasons incorrectly;
- source data is false;
- a cited field does not semantically entail a model claim;
- non-normative research notes contain tentative or rejected ideas;
- a malicious host intentionally ignores CAP-Digest policy.

CAP-Digest makes the context surface inspectable, bounded, and enforceable. It does not make model reasoning or source data true.

## Reporting process

Until a private disclosure channel is configured, open a GitHub issue only for non-sensitive reports. For sensitive issues, contact the repository owner privately before publishing details.

A good report includes:

- affected file or component;
- minimal reproduction;
- expected behavior;
- actual behavior;
- possible impact;
- whether real sensitive data is involved.

## Security review triggers

The following changes require explicit security/privacy review:

- redaction rule changes;
- data escaping changes;
- digest grammar changes;
- follow-up gate validation changes;
- pack executable-code support;
- remote or lazy source support;
- changes to trust or execution classes.
