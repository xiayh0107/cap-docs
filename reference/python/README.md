# CAP-Digest Python Reference Implementation

This is an experimental executable companion for the CAP-Digest draft. It is not the specification and is not intended as a production SDK.

Current scope:

- source type: `table`;
- fields: shape, compact columns, sample rows metadata;
- redaction: sensitive-name masking;
- tokenizer: `heuristic_v1` placeholder;
- fingerprint: fixture-provided `structure_v1` value;
- validation: evidence IDs must exist, be selected, and appear in digest text.

Run tests:

```bash
cd reference/python
python -m unittest discover tests
```

Run fixture validation from the repository root:

```bash
python reference/python/scripts/validate_fixtures.py
```
