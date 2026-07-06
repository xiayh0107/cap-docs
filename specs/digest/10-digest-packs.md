# Digest Packs

> Status: draft · Stability: evolving · Depends on: [Field Model and Assembly](05-field-model-and-assembly.md)

Digest packs distribute reusable source-reading logic. They are how CAP-Digest
grows without putting every source type into the core standard.

A Digest Pack is not a Skill, a tool registry, a workflow language, or a
CAP-Core profile. It declares how an assembler may expose a source type as
CAP-Digest fields.

## Purpose

A digest pack may provide:

- field definitions;
- symbolic renderer references;
- redaction notes;
- source-type detection notes;
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

Only `CAP.md` is required for a pack catalog entry. A pack cannot be conforming
without valid metadata and at least one verifiable contribution, such as fields
or fixtures.

## CAP.md Frontmatter

The frontmatter of `CAP.md` uses schema `cap.digest_pack.v1`.

```yaml
---
schema: cap.digest_pack.v1
name: table-basic
description: Use this digest pack for tabular sources when an agent needs shape, column names, column types, masked examples, or sample rows. Do not use it for chart image interpretation, SQL execution, or CAP-Core runtime binding.
cap: 2026-07-05-draft
source_types:
  - table
provides:
  - fields
  - redactors
  - fixtures
status: experimental
---
```

Required fields:

| Field | Meaning |
|---|---|
| `schema` | MUST be `cap.digest_pack.v1`. |
| `name` | Pack name. Lowercase letters, numbers, and hyphens recommended. |
| `description` | Trigger description for hosts and assemblers. |
| `cap` | CAP-Digest version targeted by the pack. |
| `source_types` | Source types covered. |
| `provides` | Exported contribution categories. |
| `status` | Pack status. |

Optional fields:

| Field | Meaning |
|---|---|
| `compatibility` | Runtime or implementation requirements. |
| `trust_notes` | Security and privacy considerations. |
| `metadata` | Pack-specific metadata. |

## Pack Status

| Status | Meaning | Default activation |
|---|---|---|
| `experimental` | Early pack. Shape may change. | Require explicit allow-list. |
| `draft` | Under review. Compatible changes expected. | Host policy decides. |
| `active` | Current and recommended. | May be auto-considered. |
| `deprecated` | Still recognized but should not be newly used. | MUST NOT auto-activate. |

A deprecated pack MUST document a migration path or state that none exists.

## Progressive Disclosure

Digest packs SHOULD load progressively:

| Tier | Loaded | When |
|---|---|---|
| Catalog | `CAP.md` frontmatter only | startup or discovery |
| Instructions | `CAP.md` body | pack activation |
| Resources | fields, renderers, references, fixtures | only when needed |

This prevents pack catalogs from consuming the entire model context.

## Discovery Algorithm

A host or assembler SHOULD discover packs using a deterministic process:

```text
1. Enumerate candidate directories containing CAP.md.
2. Parse only CAP.md frontmatter.
3. Validate frontmatter against cap.digest_pack.v1.
4. Build a pack catalog entry.
5. Filter by source_types exact match.
6. Score remaining packs by description relevance and status.
7. Sort by score descending, then name ascending.
8. Apply host trust policy.
9. Activate only packs allowed by policy.
```

Discovery MUST NOT execute pack code. Discovery MUST NOT load fields, redactors,
renderers, references, fixtures, or assets until the pack is activated.

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

## Activation and Trust

Project-local packs can affect what context enters a model. Hosts SHOULD apply
workspace trust policy before implicit activation.

Activation rules:

- A model MUST NOT directly activate a pack.
- A model MUST NOT directly execute pack resources.
- `experimental` packs SHOULD require explicit host or user allow-list.
- `deprecated` packs MUST NOT auto-activate.
- Third-party packs SHOULD be treated as untrusted until reviewed.
- Pack-provided redaction notes MUST NOT weaken host redaction policy.

If a pack includes executable code, hosts SHOULD require stricter review than
for instruction-only packs. CAP-Digest v0.1 does not require executable pack
loading.

## fields/

Field files are implementation-defined in v0.1, but each exported field SHOULD
validate against `cap.field.v1` when using the recommended schema.

Recommended metadata per field:

```yaml
schema: cap.field.v1
id: f1:table@shape#base
label: Shape
description: Row and column count for a tabular source.
sourceTypes:
  - table
timing: assemble
trust: code
exec: local_cheap
levels:
  - level: 1
    estimatedCost: 24
    description: Row and column count.
contracts:
  extractor: table.shape
  renderer: table_shape_base_v1
selectionHints:
  priorValue: 1.0
```

Field IDs MUST be unique within a pack.

## renderers/

Renderers define stable output for extracted values. They MUST follow CAP-Digest
escaping and redaction order.

In CAP-Digest v0.1, renderer files SHOULD be documentation or symbolic binding
notes unless the host explicitly supports executable pack resources.

## redactors/

Redactors define privacy policy fragments or notes. They should compose with
host policy. They MUST NOT silently disable host redaction.

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

Pack fixtures SHOULD be runnable without hidden credentials or network access
unless explicitly marked remote.

## Pack Conformance

A pack is conforming when:

- its `CAP.md` frontmatter is valid;
- its status allows the claimed use;
- its fields have stable IDs;
- its field files validate when a field schema is declared;
- its fixtures pass against at least one assembler;
- its redaction behavior is documented;
- it does not require hidden external state for core examples.

A pack conformance report uses schema `cap.pack_conformance_report.v1`.

Minimal report:

```json
{
  "schema": "cap.pack_conformance_report.v1",
  "pack": "table-basic",
  "packVersion": "2026-07-05-draft",
  "status": "experimental",
  "implementation": {
    "name": "cap-digest-reference",
    "version": "0.0.1"
  },
  "checks": [
    { "name": "frontmatter", "passed": true, "failures": [] },
    { "name": "fields", "passed": true, "failures": [] },
    { "name": "fixtures", "passed": true, "failures": [] }
  ]
}
```

## Source Basis

Digest Pack discovery borrows progressive-disclosure practice from
[GITHUB-SKILLS], [OPENAI-SKILLS], and [ANTHROPIC-SKILLS], but narrows it to
source-reading metadata and fixtures. MCP references [MCP-RESOURCES] and
[MCP-TOOLS] are used to preserve the boundary between readable resources and
executable tools. See [References](../../REFERENCES.md).
