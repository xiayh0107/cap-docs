# Digest Packs (Planned)

> Status: planned · Last updated: 2026-07-05

This directory will hold reusable **digest packs** — distributable bundles of
source-reading logic for CAP-Digest. It currently contains **no packs**; the
structure below is a planning sketch aligned with
`specs/digest/10-digest-packs.md`.

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

## Planned initial packs

- `table-basic/` — fields, renderers, and redactors for tabular sources (data
  frames, query results), aligned with the `fixtures/basic-table/` conformance
  case.

Packs will be added when the field model in
`specs/digest/05-field-model-and-assembly.md` and the pack format in
`specs/digest/10-digest-packs.md` reach a stable draft. A pack here is a
**Digest Pack** (source-reading logic); it is distinct from any future CAP-Core
profile/skill binding.