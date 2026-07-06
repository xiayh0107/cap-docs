# Digest Packs

> Status: draft · Last updated: 2026-07-06

This directory holds reusable **Digest Packs**: distributable bundles of
source-reading logic for CAP-Digest. Pack assets are draft unless a CAPP marks a
specific pack active.

## Planned layout

Each pack is a focused, progressively-disclosed bundle:

```text
packs/
└── <pack-name>/
    ├── CAP.md            # pack metadata: name, version, source types, status
    ├── fields/           # field definitions (id, timing, exec/trust class, levels)
    ├── renderers/        # value -> digest text renderers
    ├── redactors/        # redaction policies applied before rendering
    └── fixtures/         # pack-specific examples and test sources
```

## Current packs

- `table-basic/` — fields, renderers, and redactors for tabular sources (data
  frames, query results), aligned with the `fixtures/basic-table/` conformance
  case.

The reference implementation validates `table-basic` metadata through
`fixtures/pack-table-basic/`.

A pack here is a **Digest Pack** (source-reading logic); it is distinct from any
CAP-Core profile or skill binding.
