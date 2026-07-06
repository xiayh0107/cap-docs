from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


CORE_REQUIRED_FIELDS: dict[str, tuple[str, ...]] = {
    "cap.core.artifact.v1": ("schema", "id", "kind", "ref"),
    "cap.core.capability.v1": ("schema", "id", "name", "inputs", "outputs", "requiredBindings"),
    "cap.core.binding.v1": ("schema", "id", "type", "target", "status"),
    "cap.core.assembly.v1": ("schema", "id", "artifacts", "capability", "bindings", "policyBinding", "state"),
    "cap.core.run.v1": ("schema", "id", "assemblyId", "state", "startedAt", "inputs", "outputs", "evidenceRefs"),
    "cap.core.run_evidence.v1": (
        "schema",
        "id",
        "runId",
        "subject",
        "materials",
        "products",
        "records",
        "completeness",
    ),
}

BINDING_TYPES = {"runtime", "resource", "service", "policy", "evidence", "digest", "transport", "data-plane", "schema"}
BINDING_STATUSES = {"candidate", "resolved", "denied", "stale", "unavailable", "deferred"}
RUN_STATES = {"planned", "starting", "running", "waiting", "completed", "failed", "cancelled", "stale"}
SECRET_VALUE_KEYS = {"secretvalue", "password", "plaintextsecret", "privatekey", "apikey"}


@dataclass(frozen=True)
class CoreValidationResult:
    ok: bool
    errors: list[dict[str, str]]
    warnings: list[dict[str, str]]
    summary: dict[str, Any]

    def as_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "errors": self.errors,
            "warnings": self.warnings,
            "summary": self.summary,
        }


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_local_analysis_fixture(root: Path) -> dict[str, Any]:
    fixture = root / "fixtures" / "core" / "local-analysis"
    return {
        "fixture": fixture,
        "source_artifacts": _load_json(fixture / "source-artifacts.json"),
        "capability": _load_json(fixture / "capability.json"),
        "assembly": _load_json(fixture / "assembly.json"),
        "policy_decision": _load_json(fixture / "policy-decision.json"),
        "run": _load_json(fixture / "run.json"),
        "run_evidence": _load_json(fixture / "run-evidence.json"),
        "digest_view_ref": _load_json(fixture / "digest-view-ref.json"),
    }


def validate_core_record(record: dict[str, Any], path: str) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    schema = record.get("schema")
    if isinstance(schema, str) and schema.startswith("cap.digest."):
        errors.append(
            {
                "code": "digest_evidence_used_as_run_evidence",
                "path": path,
                "message": "CAP-Digest evidence cannot be used as CAP-Core RunEvidence.",
            }
        )
        return errors
    required = CORE_REQUIRED_FIELDS.get(schema)
    if required is None:
        errors.append({"code": "unknown_schema", "path": path, "message": f"Unknown Core schema {schema!r}."})
        return errors
    for field in required:
        if field not in record:
            errors.append({"code": "missing_required_field", "path": f"{path}.{field}", "message": "Missing required field."})
    if schema == "cap.core.binding.v1":
        if record.get("type") not in BINDING_TYPES:
            errors.append({"code": "invalid_binding_type", "path": f"{path}.type", "message": "Invalid binding type."})
        if record.get("status") not in BINDING_STATUSES:
            errors.append({"code": "invalid_binding_status", "path": f"{path}.status", "message": "Invalid binding status."})
    if schema == "cap.core.run.v1" and "state" in record and record.get("state") not in RUN_STATES:
        errors.append({"code": "invalid_run_state", "path": f"{path}.state", "message": "Invalid run state."})
    _scan_for_secret_values(record, path, errors)
    return errors


def _scan_for_secret_values(value: Any, path: str, errors: list[dict[str, str]]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            normalized = key.replace("_", "").replace("-", "").lower()
            if normalized in SECRET_VALUE_KEYS:
                errors.append(
                    {
                        "code": "secret_value_in_core_record",
                        "path": f"{path}.{key}",
                        "message": "Core records may reference secrets but must not carry secret values.",
                    }
                )
            _scan_for_secret_values(child, f"{path}.{key}", errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _scan_for_secret_values(child, f"{path}[{index}]", errors)


def validate_core_fixture(fixture: dict[str, Any]) -> CoreValidationResult:
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []

    artifacts = fixture["source_artifacts"].get("artifacts", [])
    capability = fixture["capability"]
    assembly = fixture["assembly"]
    policy_decision = fixture["policy_decision"]
    run = fixture["run"]
    run_evidence = fixture["run_evidence"]
    digest_view_ref = fixture["digest_view_ref"]
    binding_records = assembly.get("bindingRecords", [])

    for index, artifact in enumerate(artifacts):
        errors.extend(validate_core_record(artifact, f"source-artifacts.artifacts[{index}]"))
    for name, record in (
        ("capability", capability),
        ("assembly", assembly),
        ("run", run),
        ("run-evidence", run_evidence),
        ("digest-view-ref", digest_view_ref),
    ):
        errors.extend(validate_core_record(record, name))
    for index, binding in enumerate(binding_records):
        errors.extend(validate_core_record(binding, f"assembly.bindingRecords[{index}]"))

    artifact_ids = _ids(artifacts)
    binding_ids = _ids(binding_records)
    assembly_bindings = set(assembly.get("bindings", []))

    _require_reference(capability.get("id"), {assembly.get("capability")}, "assembly.capability", errors)
    _require_subset(assembly.get("artifacts", []), artifact_ids, "assembly.artifacts", errors)
    _require_subset(assembly.get("bindings", []), binding_ids, "assembly.bindings", errors)
    _require_reference(assembly.get("policyBinding"), binding_ids, "assembly.policyBinding", errors)

    binding_types = {binding.get("type") for binding in binding_records if binding.get("id") in assembly_bindings}
    for required_type in capability.get("requiredBindings", []):
        if required_type not in binding_types:
            errors.append(
                {
                    "code": "missing_required_binding_type",
                    "path": "assembly.bindings",
                    "message": f"Capability requires binding type {required_type!r}.",
                }
            )

    if policy_decision.get("policyBinding") != assembly.get("policyBinding"):
        errors.append(
            {
                "code": "policy_binding_mismatch",
                "path": "policy-decision.policyBinding",
                "message": "Policy decision must target the Assembly policyBinding.",
            }
        )
    if policy_decision.get("decision") not in {"allowed", "denied", "allowed_with_constraints", "needs_confirmation", "stale_context"}:
        errors.append({"code": "invalid_policy_decision", "path": "policy-decision.decision", "message": "Invalid decision."})

    if run.get("assemblyId") != assembly.get("id"):
        errors.append({"code": "run_assembly_mismatch", "path": "run.assemblyId", "message": "Run must reference Assembly."})
    _require_subset(run.get("inputs", []), artifact_ids, "run.inputs", errors)
    _require_subset(run.get("outputs", []), artifact_ids, "run.outputs", errors)
    _require_subset(run.get("logs", []), artifact_ids, "run.logs", errors)
    _require_reference(run.get("runtimeBinding"), binding_ids, "run.runtimeBinding", errors)
    _require_reference(run.get("resourceBinding"), binding_ids, "run.resourceBinding", errors)

    if run_evidence.get("runId") != run.get("id"):
        errors.append({"code": "run_evidence_mismatch", "path": "run-evidence.runId", "message": "RunEvidence must reference Run."})
    _require_subset(run_evidence.get("materials", []), artifact_ids, "run-evidence.materials", errors)
    _require_subset(run_evidence.get("products", []), artifact_ids, "run-evidence.products", errors)
    _require_subset(run_evidence.get("digestViews", []), binding_ids, "run-evidence.digestViews", errors)

    if digest_view_ref.get("id") not in binding_ids:
        errors.append({"code": "digest_binding_not_in_assembly", "path": "digest-view-ref.id", "message": "DigestBinding must be in Assembly."})
    if digest_view_ref.get("type") != "digest":
        errors.append({"code": "invalid_digest_binding", "path": "digest-view-ref.type", "message": "Digest view ref must be digest binding."})
    if digest_view_ref.get("constraints", {}).get("sourceRunEvidence") != run_evidence.get("id"):
        errors.append(
            {
                "code": "digest_binding_evidence_mismatch",
                "path": "digest-view-ref.constraints.sourceRunEvidence",
                "message": "DigestBinding must point at RunEvidence.",
            }
        )

    summary = {
        "artifacts": len(artifacts),
        "bindings": len(binding_records),
        "assembly": assembly.get("id"),
        "capability": capability.get("id"),
        "run": run.get("id"),
        "runEvidence": run_evidence.get("id"),
        "digestBinding": digest_view_ref.get("id"),
        "policyDecision": policy_decision.get("decision"),
    }
    return CoreValidationResult(ok=not errors, errors=errors, warnings=warnings, summary=summary)


def validate_negative_record(record: dict[str, Any], path: str) -> CoreValidationResult:
    errors = validate_core_record(record, path)
    return CoreValidationResult(ok=not errors, errors=errors, warnings=[], summary={})


def render_review_summary(fixture: dict[str, Any]) -> str:
    artifacts = fixture["source_artifacts"].get("artifacts", [])
    assembly = fixture["assembly"]
    capability = fixture["capability"]
    run = fixture["run"]
    policy_decision = fixture["policy_decision"]
    run_evidence = fixture["run_evidence"]
    digest_view_ref = fixture["digest_view_ref"]
    bindings = assembly.get("bindingRecords", [])
    network = policy_decision.get("conditions", {}).get("network", "unknown")
    return "\n".join(
        [
            "CAP-Core review summary",
            f"Assembly: {assembly.get('id')}",
            f"Capability: {capability.get('id')}",
            f"Run: {run.get('id')} state={run.get('state')}",
            f"Policy: {policy_decision.get('decision')} network={network}",
            f"Artifacts: {len(artifacts)}",
            f"Bindings: {len(bindings)}",
            f"Evidence: {run_evidence.get('id')} completeness={run_evidence.get('completeness')} integrity={run_evidence.get('integrity')}",
            f"Digest view: {digest_view_ref.get('id')}",
        ]
    ) + "\n"


def _ids(records: list[dict[str, Any]]) -> set[str]:
    ids: set[str] = set()
    for record in records:
        if isinstance(record.get("id"), str):
            ids.add(record["id"])
    return ids


def _require_reference(value: Any, allowed: set[str], path: str, errors: list[dict[str, str]]) -> None:
    if not isinstance(value, str) or value not in allowed:
        errors.append({"code": "unknown_reference", "path": path, "message": f"Unknown reference {value!r}."})


def _require_subset(values: Any, allowed: set[str], path: str, errors: list[dict[str, str]]) -> None:
    if not isinstance(values, list):
        errors.append({"code": "invalid_reference_list", "path": path, "message": "Expected a list of references."})
        return
    for index, value in enumerate(values):
        if value not in allowed:
            errors.append({"code": "unknown_reference", "path": f"{path}[{index}]", "message": f"Unknown reference {value!r}."})
