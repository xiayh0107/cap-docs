# cap-core-v1.0.0

This package is the CAP-Core v1.0.0 stable release artifact set.

## Included

- stable scope, conformance, schema, fixture, security, bridge, registry, and
  maintenance documents;
- Core v1.0 schema package under `schemas/core/`;
- positive and negative fixture suites under `fixtures/core/`;
- conformance, inspection, L3, second-implementation, and L4 comparison reports;
- CAPP and review decision records.

## Reproduce

```bash
python reference/python/scripts/validate_schema_fixtures.py
python reference/python/scripts/validate_fixtures.py --scope core --report core-fixtures.json
python reference/python/scripts/validate_core_fixtures.py --target-level L4 --report core-conformance-report.json
python reference/python/scripts/render_core_inspection_report.py --fixture remote-service-binding --json-report core-inspection.json --text-report core-inspection.txt
python reference/python/scripts/package_core_release_artifacts.py --release cap-core-v1.0.0 --stable
python reference/python/scripts/validate_core_release_manifest.py release-artifacts/cap-core-v1.0.0
```
