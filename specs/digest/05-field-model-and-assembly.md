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
    "priorValue": 0.7,
    "description": "Column names and types only."
  },
  {
    "level": 2,
    "estimatedCost": 180,
    "priorValue": 1.2,
    "description": "Column names, types, and examples."
  }
]
```

Levels allow predictable testing. Implementations SHOULD avoid hidden continuous
optimizers that produce hard-to-replay selections.

## Field Extraction

Extraction takes a source and level and returns an implementation-local value.

Requirements:

- Extraction MUST run under the guard appropriate for the execution class.
- Warnings MUST be captured as caveats or manifest warnings.
- Errors MUST be captured in the manifest.
- Timeout MUST leave the host usable.
- A failed field MUST NOT be rendered as a normal value.

## Rendering

Rendering takes an extracted and redacted value and returns digest text inside a
field block.

Rendering MUST:

- be deterministic under fixed source, budget, policy, and version;
- avoid unbounded output;
- escape data-trust strings;
- preserve enough structure for field-level evidence;
- report truncation as a caveat.

## Cost Estimation

Cost estimation is used for planning. It does not need to be perfect, but it
must be recorded.

Recommended cost fields:

- estimated tokens;
- actual tokens;
- estimator label;
- tokenizer label;
- overflow caveat if actual cost exceeds plan materially.

## Value Prior

The value prior estimates the usefulness of a field for model reasoning.
CAP-Digest does not standardize exact scoring, but recommends these principles:

- identity and provenance are high value;
- caveats and warnings are high value;
- field IDs and schema details are high value;
- representative examples can be high value but privacy-sensitive;
- decorative prose is low value;
- information already obvious from the user prompt is lower value.

Intent-specific adjustment MAY increase value for fields matching the current
question.

## Recommended Assembly Algorithm

CAP-Digest allows multiple allocators if the DigestManifest explains the result.
The recommended baseline allocator:

```text
Input: field catalog, budget, intent, policy

1. Validate fields.
2. Remove fields blocked by policy.
3. Estimate cost for candidate levels.
4. Adjust prior value by intent.
5. Sort candidates by:
   a. value / cost descending
   b. field ID ascending
   c. level ascending
6. Select candidates while budget remains.
7. Record selected and rejected candidates.
8. Extract selected fields under guard.
9. Redact extracted data.
10. Render field blocks.
11. Compute actual cost.
12. Emit digest and DigestManifest.
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

