# Digest Text Format

> Status: draft · Stability: stable · Depends on: [Field Model and Assembly](05-field-model-and-assembly.md)

Digest text is the model-visible CAP-Digest artifact. It is designed to be
readable by humans and machines, but its first obligation is stable model
consumption.

## Version Line

The first line MUST be:

```text
cap digest text=v1 fields=f1 fp=structure_v1:ab12cd34 tokenizer=heuristic_v1 budget=1180/2000
```

Fields:

| Token | Meaning |
|---|---|
| `cap digest` | Fixed prefix. |
| `text=v1` | Digest text format version. |
| `fields=f1` | Field ID scheme version. |
| `fp=` | Fingerprint algorithm and short value. |
| `tokenizer=` | Tokenizer or estimator identity. |
| `budget=used/total` | Actual rendered budget and requested budget. |

Implementations MAY include additional key-value tokens after these required
tokens. Unknown tokens MUST be ignored by readers unless policy says otherwise.

## Overall Structure

```xml
cap digest text=v1 fields=f1 fp=structure_v1:ab12cd34 tokenizer=heuristic_v1 budget=1180/2000
# source: table label=mtcars rows=32 cols=11

<field id="f1:table@shape#base" trust="code" level="1">
32 rows x 11 columns
</field>

<field id="f1:table@columns#compact" trust="derived" level="2">
mpg <dbl> e.g. <data>21, 22.8, 18.7</data>
cyl <dbl> e.g. <data>6, 4, 8</data>
</field>

<caveats>
- [cap_caveat_redacted] f1:table@columns#compact: values in "api_token" were masked
</caveats>

<available_on_request>
f1:table@missingness#full exec=local_scan level=2 estimated=240
</available_on_request>

<contract>
Reply only as JSON: {"claims":[],"evidence":[],"warnings":[],"requests":[]}
Evidence and requests must reference field IDs shown in this digest.
</contract>
```

## Source Line

The source line begins with:

```text
# source:
```

It SHOULD include:

- source type;
- label if known;
- shape or identity summary if cheap;
- fingerprint status if relevant.

It MUST NOT include sensitive source values unless they have passed redaction.

## Field Blocks

Field blocks use:

```xml
<field id="..." trust="..." level="...">
...
</field>
```

Required attributes:

- `id`
- `trust`
- `level`

Optional attributes:

- `exec`
- `cost`
- `source`
- `redacted`

The `id` attribute is the evidence anchor. A model that cites a field should cite
the field ID exactly.

## Caveats Section

The caveats section is optional only when no caveats exist. If any field failed,
was redacted, was truncated, timed out, or was downgraded, the section MUST be
present.

Format:

```text
- [code] field_id: message
```

Digest-level caveats MAY omit `field_id`.

## Available-On-Request Section

This section lists interactive fields:

```xml
<available_on_request>
f1:table@sample#k10 exec=local_scan level=2 estimated=320
f1:query@run#preview exec=remote_query level=1 estimated=500 confirm=true
</available_on_request>
```

The model may request these fields, but the gate decides whether to approve.

## Contract Section

The contract section is optional. Hosts SHOULD include it when the digest is
being sent to a model expected to produce structured output.

The contract text SHOULD be short and explicit. It SHOULD NOT include complex
policy details that belong to the gate.

## Data Fences

All source-provided strings SHOULD be wrapped:

```xml
<data>source string here</data>
```

Inside data fences, implementations MUST escape:

| Raw | Escaped |
|---|---|
| `&` | `&amp;` |
| `<` | `&lt;` |
| `>` | `&gt;` |

This prevents source data from closing tags or forging CAP-Digest structure.

## Numeric and Date Formatting

Implementations SHOULD use stable formatting:

- fixed significant digits for numeric examples;
- explicit timezone for timestamps;
- stable missing-value markers;
- no locale-dependent thousands separators by default.

## Ordering

Digest text SHOULD use stable ordering:

1. version line;
2. source line;
3. selected field blocks;
4. caveats;
5. available-on-request fields;
6. contract.

Within each section, sort by field ID unless the manifest records another
deterministic order.

## Text Compatibility

Readers MUST reject text with an unknown required prefix unless they are in a
compatibility mode.

Readers SHOULD ignore unknown optional attributes on field blocks.

Writers MUST NOT change the meaning of `text=v1` without changing the text
format version.

