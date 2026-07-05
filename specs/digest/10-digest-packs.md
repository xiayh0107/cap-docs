# Digest Packs

> Status: draft · Stability: evolving · Depends on: [Field Model and Assembly](05-field-model-and-assembly.md)

Digest packs distribute reusable source-reading logic. They are how CAP-Digest
grows without putting every source type into the core standard.

## Purpose

A digest pack may provide:

- field definitions;
- renderers;
- redactors;
- source-type detection;
- domain caveat taxonomies;
- conformance fixtures;
- examples;
- implementation notes.

Digest packs should be focused. A pack for "tabular data" is coherent. A pack
for "all enterprise analytics" is probably too broad.

## Directory Structure

```text
pack-name/
  CAP.md
  fields/
  renderers/
  redactors/
  references/
  fixtures/
  assets/
```

Only `CAP.md` is required.

## CAP.md Frontmatter

```yaml
---
name: table-basic
description: Use this pack for tabular sources when an agent needs shape, column, type, missingness, sample, or provenance context.
cap: 2026-07-04-draft
source_types:
  - table
provides:
  - fields
  - renderers
  - fixtures
---
```

Required fields:

| Field | Meaning |
|---|---|
| `name` | Pack name. Lowercase letters, numbers, and hyphens recommended. |
| `description` | Trigger description for hosts and assemblers. |
| `cap` | CAP-Digest version targeted by the pack. |
| `source_types` | Source types covered. |

Optional fields:

| Field | Meaning |
|---|---|
| `compatibility` | Runtime or language requirements. |
| `provides` | Exported capability categories. |
| `trust_notes` | Security and privacy considerations. |
| `metadata` | Pack-specific metadata. |

## Progressive Disclosure

Digest packs SHOULD load progressively:

| Tier | Loaded | When |
|---|---|---|
| Catalog | name, description, source types | startup or discovery |
| Instructions | CAP.md body | pack activation |
| Resources | fields, renderers, references, fixtures | only when needed |

This prevents pack catalogs from consuming the entire model context.

## Description Quality

The `description` field decides whether a pack is relevant. It SHOULD include:

- source types;
- user intents;
- included field families;
- boundaries and exclusions when important.

Good:

```text
Use this pack for tabular sources when an agent needs shape, column types,
missingness, representative examples, or provenance. Do not use it for chart
image interpretation or SQL query execution.
```

Weak:

```text
Helps with data.
```

## fields/

Field files are implementation-defined in v0.1, but each exported field should
map to CAP-Digest `Field`.

Recommended metadata per field:

```yaml
id: f1:table@shape#base
label: Shape
timing: assemble
trust: code
exec: local_cheap
levels:
  - level: 1
    estimatedCost: 24
    priorValue: 1.0
```

## renderers/

Renderers define stable output for extracted values. They MUST follow CAP
escaping and redaction order.

## redactors/

Redactors define privacy policy fragments. They should compose with host policy.
They MUST NOT silently disable host redaction.

## references/

References contain domain-specific notes loaded only when needed. They should be
small and targeted.

## fixtures/

Fixtures support conformance and regression testing:

```text
fixtures/
  basic-table/
    source.json
    policy.json
    expected-digest.txt
    expected-manifest.json
```

## Trust and Activation

Project-local packs can affect what context enters a model. Hosts SHOULD apply
workspace trust policy before implicit activation.

If a pack includes executable code, hosts SHOULD require stricter review than
for instruction-only packs.

## Pack Conformance

A pack is conforming when:

- its `CAP.md` frontmatter is valid;
- its fields have stable IDs;
- its fixtures pass against at least one assembler;
- its redaction behavior is documented;
- it does not require hidden external state for core examples.

