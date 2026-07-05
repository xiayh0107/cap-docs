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
tokens. Readers MUST preserve unknown version-line tokens if they re-emit digest
text, but MAY ignore them for interpretation unless host policy says otherwise.

## Overall Structure

```xml
cap digest text=v1 fields=f1 fp=structure_v1:ab12cd34 tokenizer=heuristic_v1 budget=1180/2000
# source: table label=mtcars rows=32 cols=11

<field id="f1:table@shape#base" trust="code" level="1">
32 rows x 11 columns
</field>

<field id="f1:table@columns#compact" trust="derived" level="2" redacted="true">
mpg <dbl> e.g. <data>21</data>, <data>22.8</data>, <data>18.7</data>
cyl <dbl> e.g. <data>6</data>, <data>4</data>, <data>8</data>
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

## Minimal Grammar

CAP-Digest text v1 is an XML-like line-oriented format. It is not general XML.
Readers MUST implement the CAP-Digest grammar rather than passing arbitrary text
through an XML parser and treating success as conformance.

```ebnf
digest            = version-line, nl,
                    source-line, nl, nl,
                    field-block, { nl, field-block },
                    [ nl, nl, caveats-section ],
                    [ nl, nl, available-section ],
                    [ nl, nl, contract-section ], [ nl ];

version-line      = "cap digest",
                    sp, "text=v1",
                    sp, "fields=f1",
                    sp, "fp=", token,
                    sp, "tokenizer=", token,
                    sp, "budget=", integer, "/", integer,
                    { sp, key, "=", token };

source-line       = "# source:", sp, source-type, { sp, key, "=", token };

field-block       = "<field", sp, field-attrs, ">", nl,
                    field-body, nl,
                    "</field>";

field-attrs       = id-attr, sp, trust-attr, sp, level-attr, { sp, optional-attr };
id-attr           = "id=\"", field-id, "\"";
trust-attr        = "trust=\"", ("code" | "derived" | "data"), "\"";
level-attr        = "level=\"", integer, "\"";
optional-attr     = key, "=\"", attr-value, "\"";

field-body        = text-line, { nl, text-line };
text-line         = plain-text-with-escaped-data-fences;

caveats-section   = "<caveats>", nl, caveat-line, { nl, caveat-line }, nl, "</caveats>";
caveat-line       = "- [", code, "]", sp, [field-id, ":", sp], message;

available-section = "<available_on_request>", nl, available-line, { nl, available-line }, nl, "</available_on_request>";
available-line    = field-id, { sp, key, "=", token };

contract-section  = "<contract>", nl, contract-body, nl, "</contract>";

field-id          = ? see Field ID grammar ?;
integer           = 1*DIGIT;
token             = 1*(ALPHA | DIGIT | "_" | "-" | "." | ":" | "/");
key               = 1*(ALPHA | DIGIT | "_" | "-");
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

The `id` attribute is the DigestEvidence anchor. A model that cites a field
should cite the field ID exactly.

Rules:

- Every selected field in the DigestManifest MUST appear as exactly one field
  block in digest text.
- A field block ID MUST match the `fields=f1` grammar.
- Field block IDs MUST be unique within a digest.
- Field blocks MUST NOT be nested.
- Unknown optional attributes MUST be preserved by rewriters, but MAY be ignored
  by readers.
- Missing required attributes, duplicate field IDs, or unclosed field blocks MUST
  cause parsing failure.

## Caveats Section

The caveats section is optional only when no caveats exist. If any field failed,
was redacted, was truncated, timed out, or was downgraded, the section MUST be
present.

Format:

```text
- [code] field_id: message
```

Digest-level caveats MAY omit `field_id`.

Caveats that reference a field ID MUST reference a field known to the
DigestManifest. Caveats for redacted fields SHOULD reference the selected field
that was redacted.

## Available-On-Request Section

This section lists interactive fields:

```xml
<available_on_request>
f1:table@sample#k10 exec=local_scan level=2 estimated=320
f1:query@run#preview exec=remote_query level=1 estimated=500 confirm=true
</available_on_request>
```

The model may request these fields, but the gate decides whether to approve.

Every field listed in `<available_on_request>` MUST correspond to a
DigestManifest field row that is not selected and is available through follow-up,
usually because `timing="interactive"` or a higher level is available.

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

Rules:

- Source-provided column names, labels, values, file names, and user strings
  SHOULD be treated as data-trust unless an implementation can prove otherwise.
- Data fences MUST NOT contain unescaped `<`, `>`, or `&`.
- A reader that detects an unclosed `<data>` fence MUST reject the digest text.
- A writer MUST escape source strings before inserting them into field blocks.

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

Within each section, sort by field ID unless the DigestManifest records another
deterministic order.

Whitespace between sections is not semantic. Whitespace inside field bodies is
field content and MUST be preserved unless a renderer version explicitly defines
normalization.

## Text Compatibility

Readers MUST reject text with an unknown required prefix unless they are in a
compatibility mode.

Readers SHOULD ignore unknown optional attributes on field blocks.

Writers MUST NOT change the meaning of `text=v1` without changing the text
format version.

Unknown sections MUST NOT be silently interpreted. A reader MAY preserve unknown
sections in compatibility mode, but a CAP-Digest validator SHOULD report them.

## Manifest/Text Consistency

A CAP-Digest implementation SHOULD provide a consistency validator between digest
text and DigestManifest. The validator MUST check at least:

1. every selected DigestManifest field row has exactly one field block in digest
   text;
2. digest text does not contain selected field blocks missing from the
   DigestManifest;
3. a rejected field is not rendered as a selected field block;
4. fields in `<available_on_request>` correspond to known unselected or
   higher-level fields;
5. caveat field IDs reference known DigestManifest fields;
6. fields with `redacted=true` in the DigestManifest have either a redaction
   caveat or a `redacted="true"` field attribute.

A model evidence validator MUST rely on parsed field IDs from digest text, not
on arbitrary substring search.

## Source Basis

This section follows CAP-Digest's existing field-block design and makes it
parseable enough for conformance tests. JSON object validation remains in
[JSON-SCHEMA-2020-12]; digest text is the model-visible representation. The
text/object consistency requirement is informed by typed metadata practices in
[IN-TOTO-ATTESTATION] and [RO-CRATE-1.2], while staying within CAP-Digest's
context evidence layer. See [References](../../REFERENCES.md).
