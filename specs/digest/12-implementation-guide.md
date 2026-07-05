# Implementation Guide

> Status: draft · Stability: evolving · Depends on: [Architecture](04-architecture.md)

This guide describes how to build a CAP-Digest implementation without inventing
missing policy at the implementation stage.

## Minimum Viable Implementation

A useful CAP-Digest v0 implementation needs:

1. A `SourceRef` type.
2. A `Field` type.
3. A small built-in field catalog for one source type.
4. An assembler that selects fields under token budget.
5. A digest text writer.
6. A DigestManifest writer.
7. Redaction before rendering.
8. Evidence validation.

Follow-up can be added after the first digest producer works.

## Suggested API

```text
capabilities() -> CapabilityDocument
list_fields(source, intent = null, policy = null) -> FieldCatalog
assemble(source, budget, intent = null, policy = null) -> Digest
validate_response(digest, response) -> ValidationResult
gate_requests(digest, requests, policy = null) -> GateDecision[]
request_field(digest, field_id, level = null, budget = null, policy = null) -> Digest | DigestPatch
```

## Implementation Checklist

### Source Layer

- Define source references.
- Avoid serializing the full source by default.
- Compute a fingerprint or mark the source unfingerprintable.
- Record source type and label.

### Field Layer

- Define field IDs.
- Define levels.
- Assign trust and execution class.
- Estimate cost.
- Validate level monotonicity if your allocator assumes it.
- Keep field discovery cheap.

### Assembly Layer

- Sort candidates deterministically.
- Record selected fields.
- Record rejected fields.
- Run extraction under guard.
- Record warnings and errors.
- Redact before rendering.
- Escape data fences.
- Measure actual cost if possible.

### Digest Layer

- Emit version line.
- Emit source line.
- Emit field blocks.
- Emit caveats.
- Emit available-on-request section.
- Emit contract section when requested.

### DigestManifest Layer

- Store source metadata.
- Store field rows.
- Store selected and rejected status.
- Store estimated and actual cost.
- Store redaction and errors.
- Store tokenizer identity.

### Gate Layer

- Parse model response.
- Validate evidence field IDs.
- Validate request field IDs.
- Check fingerprint.
- Check budget.
- Check execution class.
- Check privacy policy.
- Return structured decisions.

## Common Mistakes

### Mistake: Treating CAP-Digest As A Pretty Summary

If output has no field IDs and no DigestManifest, it is not CAP-Digest.

### Mistake: Only Recording Selected Fields

Rejected fields matter. They explain budget tradeoffs and power follow-up.

### Mistake: Redacting After Rendering

Rendering can transform values. Redact first.

### Mistake: Letting The Model Call Extractors

Models request fields. Gates approve. Extractors are not model tools.

### Mistake: Hiding Failures

If a field fails, record it. Silent omission produces misleading context.

### Mistake: Relying On Prompt Instructions For Security

The contract block helps the model cooperate. The gate enforces policy.

## Example: Tiny Table Implementation

Field catalog:

```json
[
  {
    "id": "f1:table@shape#base",
    "label": "Shape",
    "timing": "assemble",
    "trust": "code",
    "exec": "local_cheap",
    "levels": [{"level": 1, "estimatedCost": 24, "priorValue": 1.0}]
  },
  {
    "id": "f1:table@columns#compact",
    "label": "Columns",
    "timing": "assemble",
    "trust": "derived",
    "exec": "local_cheap",
    "levels": [{"level": 1, "estimatedCost": 120, "priorValue": 1.1}]
  },
  {
    "id": "f1:table@sample#k10",
    "label": "Sample rows",
    "timing": "interactive",
    "trust": "data",
    "exec": "local_scan",
    "levels": [{"level": 1, "estimatedCost": 300, "priorValue": 0.8}]
  }
]
```

Digest:

```xml
cap digest text=v1 fields=f1 fp=structure_v1:ab12cd34 tokenizer=heuristic_v1 budget=138/500
# source: table label=orders rows=1000 cols=4

<field id="f1:table@shape#base" trust="code" level="1">
1000 rows x 4 columns
</field>

<field id="f1:table@columns#compact" trust="derived" level="1">
order_id <chr>
customer_id <chr>
amount <dbl>
api_token <chr> values masked
</field>

<caveats>
- [cap_caveat_redacted] f1:table@columns#compact: values in "api_token" were masked
</caveats>

<available_on_request>
f1:table@sample#k10 exec=local_scan level=1 estimated=300
</available_on_request>
```

The example above is intentionally small. A real implementation should ensure
the closing tags are well-formed and include a contract block only when the host
asks for structured model output.

## Release Path

Recommended implementation order:

1. Produce digest and DigestManifest for one simple source type.
2. Add redaction and caveats.
3. Add rejected fields.
4. Add deterministic fixtures.
5. Add contract validation.
6. Add gated follow-up.
7. Add digest pack support.
8. Publish conformance report.
