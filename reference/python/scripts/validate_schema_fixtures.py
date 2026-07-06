from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
except ImportError as exc:  # pragma: no cover - exercised in environments without dependencies.
    raise SystemExit(
        "Missing dependency: jsonschema. Install reference dependencies with "
        "`python -m pip install -e reference/python`."
    ) from exc


ROOT = Path(__file__).resolve().parents[3]


@dataclass(frozen=True)
class SchemaTarget:
    fixture_path: Path
    schema_path: Path
    pointer: tuple[str | int, ...] = ()
    note: str = ""
    expected_valid: bool = True

    @property
    def display_path(self) -> str:
        rel = self.fixture_path.relative_to(ROOT).as_posix()
        if not self.pointer:
            return rel
        return f"{rel}#{format_pointer(self.pointer)}"


DOCUMENTED_NO_SCHEMA: dict[str, str] = {
    "fixtures/basic-table/source.json": "fixture input source; source schema is not defined for alpha",
    "fixtures/basic-table/policy.json": "fixture harness policy; policy schema is not defined for alpha",
    "fixtures/core/local-analysis/expected-validation.json": "Core validator expected-output harness",
    "fixtures/core/local-analysis/negative/digest-evidence-as-run-evidence.json": (
        "negative layer-boundary case using a digest evidence schema not defined in this repo"
    ),
    "fixtures/core/local-analysis/policy-decision.json": "Core policy decision envelope has no schema sketch yet",
    "fixtures/core/local-analysis/source-artifacts.json": "artifact-set wrapper has no schema; nested artifacts are validated",
    "fixtures/followup-basic/expected-gate.json": "legacy compact gate summary used by reference tests",
    "fixtures/followup-basic/policy.json": "fixture harness policy; policy schema is not defined for alpha",
    "fixtures/followup-basic/source.json": "fixture input source; source schema is not defined for alpha",
    "fixtures/pack-table-basic/expected-pack.json": "legacy pack-loader summary; no cap.pack_validation.v1 schema yet",
    "fixtures/security-adversarial/policy.json": "fixture harness policy; policy schema is not defined for alpha",
    "fixtures/security-adversarial/source.json": "fixture input source; source schema is not defined for alpha",
}


def rel(path: str) -> Path:
    return ROOT / path


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def schema_registry() -> Registry:
    resources = []
    for path in sorted((ROOT / "schemas").rglob("*.json")):
        schema = load_json(path)
        schema_id = schema.get("$id")
        if isinstance(schema_id, str):
            resources.append((schema_id, Resource.from_contents(schema)))
    return Registry().with_resources(resources)


def validator_for(schema_path: Path, registry: Registry) -> Draft202012Validator:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, registry=registry)


def get_pointer(document: Any, pointer: tuple[str | int, ...]) -> Any:
    current = document
    for part in pointer:
        current = current[part]
    return current


def format_pointer(pointer: tuple[str | int, ...]) -> str:
    if not pointer:
        return ""
    return "".join(f"/{str(part).replace('~', '~0').replace('/', '~1')}" for part in pointer)


def format_error_path(path: Any) -> str:
    parts = list(path)
    if not parts:
        return "$"
    rendered = "$"
    for part in parts:
        if isinstance(part, int):
            rendered += f"[{part}]"
        else:
            rendered += f".{part}"
    return rendered


def add(targets: list[SchemaTarget], fixture: str, schema: str, pointer: tuple[str | int, ...] = (), note: str = "") -> None:
    targets.append(SchemaTarget(rel(fixture), rel(schema), pointer, note))


def build_targets() -> list[SchemaTarget]:
    targets: list[SchemaTarget] = []

    add(targets, "fixtures/basic-table/expected-manifest.json", "schemas/cap.manifest.v1.schema.json")
    add(
        targets,
        "fixtures/basic-table/expected-validation.json",
        "schemas/cap.contract_response.v1.schema.json",
        ("response",),
    )
    add(
        targets,
        "fixtures/basic-table/expected-validation.json",
        "schemas/cap.validation_result.v1.schema.json",
        ("validation",),
    )
    negative_validation = load_json(rel("fixtures/basic-table/negative-validation.json"))
    for index, _case in enumerate(negative_validation["cases"]):
        add(
            targets,
            "fixtures/basic-table/negative-validation.json",
            "schemas/cap.contract_response.v1.schema.json",
            ("cases", index, "response"),
        )
        add(
            targets,
            "fixtures/basic-table/negative-validation.json",
            "schemas/cap.validation_result.v1.schema.json",
            ("cases", index, "validation"),
        )

    add(targets, "fixtures/catalog-table-basic/field-catalog.json", "schemas/cap.field_catalog.v1.schema.json")

    add(targets, "fixtures/followup-basic/request-approved.json", "schemas/cap.contract_response.v1.schema.json")
    add(targets, "fixtures/followup-basic/response.json", "schemas/cap.contract_response.v1.schema.json")
    add(
        targets,
        "fixtures/followup-basic/expected-validation-approved.json",
        "schemas/cap.validation_result.v1.schema.json",
    )
    add(targets, "fixtures/followup-basic/expected-gate-approved.json", "schemas/cap.gate_result.v1.schema.json")
    add(targets, "fixtures/followup-basic/expected-gate-stale.json", "schemas/cap.gate_result.v1.schema.json")
    add(targets, "fixtures/followup-basic/expected-patch.json", "schemas/cap.digest_patch.v1.schema.json")

    add(
        targets,
        "fixtures/pack-table-basic/expected-pack-report.json",
        "schemas/cap.pack_conformance_report.v1.schema.json",
    )

    add(
        targets,
        "fixtures/security-adversarial/renderer-failure-manifest.json",
        "schemas/cap.manifest.v1.schema.json",
    )

    core_artifacts = load_json(rel("fixtures/core/local-analysis/source-artifacts.json"))
    for index, _artifact in enumerate(core_artifacts["artifacts"]):
        add(
            targets,
            "fixtures/core/local-analysis/source-artifacts.json",
            "schemas/core/cap.core.artifact.v1.schema.json",
            ("artifacts", index),
        )
    add(targets, "fixtures/core/local-analysis/capability.json", "schemas/core/cap.core.capability.v1.schema.json")
    add(targets, "fixtures/core/local-analysis/assembly.json", "schemas/core/cap.core.assembly.v1.schema.json")
    assembly = load_json(rel("fixtures/core/local-analysis/assembly.json"))
    for index, _binding in enumerate(assembly["bindingRecords"]):
        add(
            targets,
            "fixtures/core/local-analysis/assembly.json",
            "schemas/core/cap.core.binding.v1.schema.json",
            ("bindingRecords", index),
        )
    add(targets, "fixtures/core/local-analysis/digest-view-ref.json", "schemas/core/cap.core.binding.v1.schema.json")
    add(targets, "fixtures/core/local-analysis/run.json", "schemas/core/cap.core.run.v1.schema.json")
    add(targets, "fixtures/core/local-analysis/run-evidence.json", "schemas/core/cap.core.run_evidence.v1.schema.json")
    add(
        targets,
        "fixtures/core/local-analysis/negative/secret-value-in-service-binding.json",
        "schemas/core/cap.core.binding.v1.schema.json",
        note="schema-valid but semantically rejected by the Core validator",
    )
    targets.append(
        SchemaTarget(
            rel("fixtures/core/local-analysis/negative/run-without-assembly.json"),
            rel("schemas/core/cap.core.run.v1.schema.json"),
            expected_valid=False,
            note="negative fixture must fail required assemblyId validation",
        )
    )

    return targets


def validate_targets(targets: list[SchemaTarget]) -> list[str]:
    registry = schema_registry()
    validators: dict[Path, Draft202012Validator] = {}
    problems: list[str] = []

    for target in targets:
        validator = validators.setdefault(target.schema_path, validator_for(target.schema_path, registry))
        document = get_pointer(load_json(target.fixture_path), target.pointer)
        errors = sorted(validator.iter_errors(document), key=lambda error: list(error.absolute_path))
        if target.expected_valid and errors:
            for error in errors:
                problems.append(
                    f"{target.display_path}: schema mismatch against "
                    f"{target.schema_path.relative_to(ROOT).as_posix()} at {format_error_path(error.absolute_path)}: "
                    f"{error.message}"
                )
        elif not target.expected_valid and not errors:
            problems.append(
                f"{target.display_path}: expected schema failure against "
                f"{target.schema_path.relative_to(ROOT).as_posix()}, but validation passed"
            )

    return problems


def validate_inventory(targets: list[SchemaTarget]) -> list[str]:
    handled = {target.fixture_path.relative_to(ROOT).as_posix() for target in targets}
    handled.update(DOCUMENTED_NO_SCHEMA)
    fixture_json = {path.relative_to(ROOT).as_posix() for path in (ROOT / "fixtures").rglob("*.json")}
    missing = sorted(fixture_json - handled)
    stale = sorted(path for path in DOCUMENTED_NO_SCHEMA if not (ROOT / path).exists())
    problems = [f"{path}: fixture JSON is not mapped to a schema or documented no-schema reason" for path in missing]
    problems.extend(f"{path}: documented no-schema entry points to a missing file" for path in stale)
    return problems


def main() -> int:
    targets = build_targets()
    problems = validate_inventory(targets)
    problems.extend(validate_targets(targets))

    for target in targets:
        schema_name = target.schema_path.relative_to(ROOT).as_posix()
        expectation = "expected-invalid" if not target.expected_valid else "ok"
        suffix = f" ({target.note})" if target.note else ""
        print(f"{expectation}: {target.display_path} -> {schema_name}{suffix}")
    for path, reason in sorted(DOCUMENTED_NO_SCHEMA.items()):
        print(f"skip: {path} ({reason})")

    if problems:
        print("\nSchema fixture validation failed:", file=sys.stderr)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1

    print(f"schema fixture validation ok: {len(targets)} checked, {len(DOCUMENTED_NO_SCHEMA)} documented no-schema")
    return 0


if __name__ == "__main__":
    sys.exit(main())
