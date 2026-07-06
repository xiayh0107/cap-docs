# CAPP-0003: table-basic Digest Pack

> Status: implemented · Created: 2026-07-05 · Layer: CAP-Digest Pack

## Abstract

This CAPP introduces `packs/table-basic/`, the first Digest Pack for CAP-Digest. The pack covers small tabular sources and provides a seed for pack metadata, field definitions, redaction notes, and pack-driven fixtures.

## Motivation

CAP-Digest should grow through focused Digest Packs rather than expanding every source type into the core specification. A table pack is the smallest useful example because tabular objects are common, structured, and easy to test deterministically.

## Specification

The `table-basic` pack provides:

- pack metadata in `CAP.md`;
- field definitions for shape, compact columns, and sample rows;
- redaction guidance for sensitive column names;
- fixture alignment with `fixtures/basic-table/`;
- executable pack loading in the Python reference implementation;
- pack validation fixture under `fixtures/pack-table-basic/`.

The pack is source-reading logic for CAP-Digest. It is not a Skill and not a CAP-Core profile.

## Rationale

The pack tests progressive disclosure and focused pack boundaries without introducing runtime binding or external service execution.

## Compatibility

The pack is experimental and may change before `0.1.0-alpha`.

## Security and Privacy

The pack must preserve host policy. Redactors must not silently disable host redaction. Sample rows are interactive by default because they may contain sensitive data.

## Reference Implementation

The Python reference implementation can load the `table-basic` field definitions
and validate pack metadata alignment.

## Conformance Fixtures

The initial conformance targets are `fixtures/basic-table/` and
`fixtures/pack-table-basic/`.
