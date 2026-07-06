# Field Model and Assembly

> Status: draft · Stability: stable · Depends on: [Core Data Model](03-core-data-model.md)

Fields are the heart of CAP-Digest. A field is the smallest unit that can be
selected, rendered, cited, rejected, or requested.

## Field Responsibilities

A field definition covers:

- stable identity;
- applicability to source types;
- extraction logic;
- rendering logic;
- cost estimation;
- value prior;
- execution class;
- trust class;
- available levels;
- timing.

Fields MUST NOT hide source access behind model-visible text. If the model needs
more data, it asks for field IDs and the gate decides.

## Serialized Field Object

A serialized CAP-Digest field object uses schema `cap.field.v1`. A field object
MUST be valid against `schemas/cap.field.v1.schema.json` when that schema is
available.

Minimal field object:

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
selectionHints:
  priorValue: 1.0
  intentTags: [shape, structure]
contracts:
  extractor: table.shape
  renderer: table_shape_base_v1
```

The `contracts` object contains symbolic implementation references. It MUST NOT
contain shell commands, source code, network locations, or model-visible
instructions. A host MAY bind symbolic references such as `table.shape` or
`table_columns_compact_v1` to local implementation functions, but the field file
itself is not executable.

## Field Catalog

A Field Catalog is a machine-readable set of field definitions applicable to a
source type. It uses schema `cap.field_catalog.v1`.

```json
{
  "schema": "cap.field_catalog.v1",
  "catalogId": "table-basic",
  "sourceType": "table",
  "versions": {
    "cap": "2026-07-05-draft",
    "fields": "f1",
    "catalog": "v1"
  },
  "fields": []
}
```

A Field Catalog MUST contain only unique field IDs. If two packs or built-in
providers export the same field ID, the assembler MUST fail closed or require an
explicit host override. Silent last-writer-wins behavior is not CAP-Digest
conforming.

## Field ID Grammar

Field IDs in scheme `f1` MUST match:

```text
^f1:[a-z][a-z0-9_]*@[a-z][a-z0-9_]*(?:[-_][a-z0-9_]+)*#[a-z0-9]+(?:[-_][a-z0-9]+)*$
```

The grammar is:

```text
f1:<source-family>@<field-name>#<variant>
```

Examples:

```text
f1:table@shape#base
f1:table@columns#compact
f1:table@sample#k10
f1:table@missingness#full
```

Rules:

- Field IDs MUST be stable within a field ID scheme version.
- Field IDs MUST be unique within a DigestManifest.
- Field IDs MUST NOT contain spaces.
- Renaming a field ID is a compatibility change.
- A new field variant SHOULD use a new `#variant` rather than changing the
  meaning of an existing field ID.

## Timing

CAP-Digest uses two timing classes:

| Timing | Meaning |
|---|---|
| `assemble` | Field may be included in the initial digest. |
| `interactive` | Field is only available through gated follow-up. |

Fields that may trigger expensive scans, remote queries, privacy-sensitive
samples, or long-running computation SHOULD default to `interactive`.

## Execution Class

Execution class expresses operational risk:

| Class | Description | Default policy |
|---|---|---|
| `local_cheap` | Cheap local metadata. | May run automatically. |
| `local_scan` | Local scan, sample, or computation. | Requires budget and timeout. |
| `remote_query` | Network, database, or remote API. | Requires explicit policy. |
| `unsafe` | Unknown or high-risk execution. | Deny by default. |

Hosts may define stricter policies. Unknown execution classes MUST fail closed.

## Trust Class

Trust class expresses instruction risk:

| Class | Description |
|---|---|
| `code` | Implementation-authored structural text. |
| `derived` | Computed summaries derived from source values. |
| `data` | Source-provided values or strings. |

`data` trust content MUST be escaped in digest text and SHOULD be wrapped in
data fences.

## Levels

Field levels are discrete:

```json
[
  {
    "level": 1,
    "estimatedCost": 60,
    "description": "Column names and types only."
  },
  {
    "level": 2,
    "estimatedCost": 180,
    "description": "Column names, types, and examples."
  }
]
```

Levels allow predictable testing. Implementations SHOULD avoid hidden continuous
optimizers that produce hard-to-replay selections.

Level rules:

- `level` MUST be a positive integer.
- `estimatedCost` MUST be a non-negative integer.
- `estimatedCost` MUST be non-decreasing as `level` increases unless the field
  declares `nonMonotonic: true` and explains the reason in `description` or
  pack documentation.
- `selectionHints.priorValue` SHOULD be positive when present.
- If a higher level is selected for a field, lower-level candidates for the same
  field SHOULD be recorded as rejected with `rejectedReason="level_superseded"`
  when they were explicit candidates.

## Candidate Expansion

The allocator operates on candidates. A candidate is a `(fieldId, level)` pair
expanded from a field catalog.

For each field:

1. The assembler expands every available level into a candidate.
2. The assembler removes candidates blocked by host policy.
3. The assembler MAY adjust `selectionHints.priorValue` by intent.
4. The assembler chooses at most one level for a given `fieldId`.
5. Every candidate considered SHOULD be represented in the DigestManifest as
   selected or rejected.

If a field has `timing="interactive"`, its candidates MUST NOT be selected into
the initial digest unless host policy explicitly allows initial interactive
materialization. The usual rejection reason is `interactive_only`.

## Field Extraction

Extraction takes a source and level and returns an implementation-local value.

Requirements:

- Extraction MUST run under the guard appropriate for the execution class.
- Warnings MUST be captured as caveats or DigestManifest warnings.
- Errors MUST be captured in the DigestManifest.
- Timeout MUST leave the host usable.
- A failed field MUST NOT be rendered as a normal value.

Recommended implementation contract:

```python
@dataclass
class ExtractResult:
    value: object
    warnings: list[str]
    elapsed_ms: int

def extractor(source: object, *, level: int, policy: dict) -> ExtractResult: ...
```

The Python type above is illustrative. The normative requirement is the shape:
value, warnings, and elapsed time must be available to the assembler.

## Redaction

Redaction takes an extracted value and returns a value safe for rendering.

```python
@dataclass
class RedactResult:
    value: object
    redacted: bool
    warnings: list[str]

def redactor(value: object, *, field: dict, policy: dict) -> RedactResult: ...
```

Redaction MUST happen before rendering. A redactor MUST NOT silently disable host
policy. Pack-provided redaction notes are advisory unless the host explicitly
binds them.

## Rendering

Rendering takes an extracted and redacted value and returns digest text inside a
field block.

Rendering MUST:

- be deterministic under fixed source, budget, policy, and version;
- avoid unbounded output;
- escape data-trust strings;
- preserve enough structure for field-level DigestEvidence;
- report truncation as a caveat.

Recommended implementation contract:

```python
@dataclass
class RenderResult:
    field_block: str
    actual_cost: int
    warnings: list[str]

def renderer(value: object, *, field: dict, level: int, policy: dict) -> RenderResult: ...
```

## Cost Estimation

Cost estimation is used for planning. It does not need to be perfect, but it
must be recorded.

Recommended cost fields:

- estimated tokens;
- actual tokens;
- estimator label;
- tokenizer label;
- overflow caveat if actual cost exceeds plan materially.

In CAP-Digest v1, token cost is the primary unit. If an implementation uses a
heuristic estimator, it MUST identify it in the DigestManifest.

## Value Prior and Intent Adjustment

The value prior estimates the usefulness of a field for model reasoning.
CAP-Digest does not standardize exact scoring, but recommends these principles:

- identity and provenance are high value;
- caveats and warnings are high value;
- field IDs and schema details are high value;
- representative examples can be high value but privacy-sensitive;
- decorative prose is low value;
- information already obvious from the user prompt is lower value.

Intent-specific adjustment MAY increase value for fields matching the current
question. An implementation that uses intent adjustment SHOULD record the
adjustment method in the allocation plan or DigestManifest.

## Recommended Assembly Algorithm

CAP-Digest allows multiple allocators if the DigestManifest explains the result.
The recommended baseline allocator:

```text
Input: field catalog, budget, intent, policy

1. Validate fields.
2. Expand fields into (fieldId, level) candidates.
3. Remove candidates blocked by policy.
4. Estimate cost for candidate levels.
5. Adjust prior value by intent.
6. Sort candidates by:
   a. value / cost descending
   b. field ID ascending
   c. level ascending
7. Select candidates while budget remains, selecting at most one level per field.
8. Record selected and rejected candidates.
9. Extract selected fields under guard.
10. Redact extracted data.
11. Render field blocks.
12. Compute actual cost.
13. Emit digest and DigestManifest.
```

## Determinism

Implementations SHOULD be deterministic for fixed inputs.

Determinism requires:

- stable field ordering;
- stable tie breakers;
- stable random seeds if sampling is used;
- stable string sorting;
- stable numeric formatting;
- stable caveat ordering;
- versioned digest and manifest formats.

If deterministic output is impossible because the source is live or remote, the
digest MUST say so through caveats or source metadata.

## Minimal Digest Guarantee

If all fields fail, a CAP-Digest assembler SHOULD still return a minimal digest:

```text
cap digest text=v1 fields=f1 fp=unfingerprintable tokenizer=unknown budget=0/2000
# source: unknown

<caveats>
- [cap_caveat_field_error] all fields failed during guarded extraction
</caveats>
```

This makes failure inspectable rather than silent.

## Source Basis

This section is based on the repository-local CAP-Digest field model and on
schema-driven interoperability practice from [JSON-SCHEMA-2020-12]. The
symbolic-contract boundary is intentionally narrower than Skills and MCP tools:
Digest Pack field definitions declare source-reading contracts but do not define
executable tools. See [MCP-TOOLS], [GITHUB-SKILLS], [OPENAI-SKILLS], and
[ANTHROPIC-SKILLS] in [References](../../REFERENCES.md).
