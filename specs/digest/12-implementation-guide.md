# Implementation Guide

> Status: draft · Stability: evolving · Depends on: [Architecture](04-architecture.md)

This guide describes how to build a CAP-Digest implementation without inventing
missing policy at the implementation stage.

## Reference Implementation

The repository includes an experimental, non-normative Python companion under
[`reference/python/`](../../reference/python/). It exists to make fixtures
executable and to show one conservative implementation path. It is not the
specification and must not be treated as the only valid implementation.

Run the same checks used by CI from the repository root:

```bash
python -m unittest discover reference/python/tests
python reference/python/scripts/validate_fixtures.py
python reference/python/scripts/validate_fixtures.py --report conformance-report.json
```

The fixture validator currently covers:

- [`fixtures/basic-table/`](../../fixtures/basic-table/) for Level 0/1 assembly,
  redaction, manifest, and evidence validation;
- [`fixtures/digest-text-negative/`](../../fixtures/digest-text-negative/) for
  parser and manifest/text negative cases;
- [`fixtures/followup-basic/`](../../fixtures/followup-basic/) for Level 2 gate
  decisions and digest patches;
- [`fixtures/pack-table-basic/`](../../fixtures/pack-table-basic/) for Level 3
  pack metadata loading;
- [`fixtures/security-adversarial/`](../../fixtures/security-adversarial/) for
  escaping, masking, and failed-field security cases.

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

## Conformance Levels

| Level | Required behavior | Current fixture |
|---|---|---|
| Level 0: Digest Producer | Produce digest text and a DigestManifest for one source type | `fixtures/basic-table/` |
| Level 1: Safe Assembler | Redact before rendering, escape data, record selected/rejected fields, validate evidence | `fixtures/basic-table/`, `fixtures/security-adversarial/` |
| Level 2: Follow-Up Gate | Validate requests, check fingerprint/budget/policy, return gate result and patch | `fixtures/followup-basic/` |
| Level 3: Digest Pack Host | Discover and load Digest Pack metadata fail-closed | `fixtures/pack-table-basic/` |

Implementations MAY defer Level 2 follow-up support if they do not serialize
`<available_on_request>` fields as actionable requests. If follow-up is
deferred, interactive fields MUST remain unselected, model requests MUST NOT be
executed, and the implementation should document that only Level 0/1 is claimed.

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

## Extension Paths

### Add A New Source Type

1. Add a source fixture under `fixtures/<source-type>-basic/`.
2. Define a stable source fingerprint strategy, or explicitly record that the
   source is unfingerprintable.
3. Add source-specific field definitions to a built-in catalog or Digest Pack.
4. Extend the assembler to produce digest text and manifest rows.
5. Add validation to `reference/python/scripts/validate_fixtures.py` or an
   equivalent conformance runner.

### Add A New Field

1. Choose a Field ID that matches `f1:<source-family>@<field-name>#<variant>`.
2. Define timing, trust, execution class, level, estimated cost, and prior value.
3. Add extraction, redaction, rendering, and validation behavior.
4. Record selected and rejected outcomes in `DigestManifest.fields[]`.
5. Add positive and negative fixtures when the field affects evidence,
   redaction, escaping, or follow-up behavior.

### Add A New Fixture

Each fixture should include enough files to make expected behavior reproducible:

- source input and policy when executable;
- expected digest text or expected validation outputs;
- README explaining what is intentionally covered and what is not;
- tests or `validate_fixtures.py` checks that fail on regression.

### Add A New Digest Pack

1. Add `packs/<pack-name>/CAP.md` with `cap.digest_pack.v1` frontmatter.
2. Add field files under `packs/<pack-name>/fields/`.
3. Document renderers and redactors without silently loading executable code.
4. Add a fixture under `fixtures/pack-<pack-name>/`.
5. Default third-party and executable pack behavior should be fail-closed until
   host/user activation and review policy allow it.

### Update Schemas Safely

1. Decide whether the change needs a CAPP and version bump using
   [Versioning, Conformance, and Governance](11-versioning-conformance-governance.md).
2. Update the schema and at least one fixture that exercises the changed shape.
3. Update reference validation or document why the schema remains prose-only.
4. Run JSON parse, fixture validation, and link checks before merging.

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

The Tiny Table example maps directly to
[`fixtures/basic-table/`](../../fixtures/basic-table/). Reproduce it first
before adding new source types or packs.

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
cap digest text=v1 fields=f1 fp=structure_v1:orders-1000x4 tokenizer=heuristic_v1 budget=160/500
# source: table label=orders rows=1000 cols=4

<field id="f1:table@shape#base" trust="code" level="1">
1000 rows x 4 columns
</field>

<field id="f1:table@columns#compact" trust="derived" level="1">
order_id <chr> e.g. <data>A001</data>, <data>A002</data>
customer_id <chr> e.g. <data>C001</data>, <data>C002</data>
amount <dbl> e.g. <data>12.5</data>, <data>19.0</data>
api_token <chr> e.g. <data>[masked: sensitive name]</data>
</field>

<caveats>
- [cap_caveat_redacted] f1:table@columns#compact: values in "api_token" were masked
</caveats>

<available_on_request>
f1:table@sample#k10 exec=local_scan level=1 estimated=300
</available_on_request>
```

The example above is intentionally small. A real implementation should match the
fixture outputs before claiming Level 0/1 conformance.

## Common Failure Outputs

| Failure | DigestManifest representation | Digest text representation |
|---|---|---|
| Sensitive-name redaction | `redacted=true`, warning such as `values in api_token masked` | masked value and caveat |
| Field rejected by budget | `selected=false`, `rejectedReason=over_budget`, `actualCost=0` | absent field block, optionally listed as available-on-request |
| Interactive field deferred | `selected=false`, `rejectedReason=interactive_only` | listed under `<available_on_request>` |
| Renderer failure | `ok=false`, `selected=false`, `errorClass=renderer_error` | no normal field block for the failed value |
| Evidence cites unknown field | `ValidationResult.errors[].code=evidence_unknown_field` | no digest text change |
| Evidence cites rejected field | `ValidationResult.errors[].code=evidence_rejected_field` | no digest text change |

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
