# CAP Proposals (CAPPs)

CAPPs are the change-control mechanism for substantial CAP-Digest, CAP-Core,
CAP pack, and repository governance changes.

Use a CAPP for:

- new primitives;
- breaking schema changes;
- new digest text grammar;
- new normative security requirements;
- feature deprecation or removal;
- governance changes.

## Status values

| Status | Meaning |
|---|---|
| `draft` | Under discussion; not accepted. |
| `proposed` | Ready for maintainer review. |
| `accepted` | Accepted but not necessarily implemented. |
| `implemented` | Implemented in spec, schemas, fixtures, or reference code. |
| `active` | Current and recommended. |
| `deferred` | Valid topic but not in the current scope. |
| `withdrawn` | Closed by author or maintainer. |

## Template

```markdown
# CAPP-0000: Title

> Status: draft · Created: YYYY-MM-DD · Layer: CAP-Digest

## Abstract
## Motivation
## Specification
## Rationale
## Compatibility
## Security and Privacy
## Reference Implementation
## Conformance Fixtures
```

## Acceptance criteria

A CAPP should not be accepted without:

- a clear problem statement;
- concrete syntax or data model changes when applicable;
- compatibility analysis;
- security and privacy analysis;
- at least one reference implementation or executable fixture when the change affects behavior.

## Current CAPPs

| CAPP | Title | Status |
|---|---|---|
| CAPP-0001 | CAP-Digest / CAP-Core split | draft |
| CAPP-0002 | Initial schemas and fixtures | draft |
| CAPP-0003 | table-basic Digest Pack | draft |
| CAPP-0004 | CAP-Core Draft Entry | proposed |
