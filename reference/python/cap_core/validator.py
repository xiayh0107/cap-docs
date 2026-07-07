from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


CORE_VALIDATOR_VERSION = "0.1.0-candidate-prep"
CORE_FIXTURE_NAMES = ("local-analysis", "build-test", "remote-service-binding")

CORE_REQUIRED_FIELDS: dict[str, tuple[str, ...]] = {
    "cap.core.artifact_set.v1": ("schema", "artifacts"),
    "cap.core.artifact.v1": ("schema", "id", "kind", "ref"),
    "cap.core.capability.v1": ("schema", "id", "name", "inputs", "outputs", "requiredBindings"),
    "cap.core.binding.v1": ("schema", "id", "type", "target", "status"),
    "cap.core.assembly.v1": ("schema", "id", "artifacts", "capability", "bindings", "policyBinding", "state"),
    "cap.core.policy_decision.v1": (
        "schema",
        "id",
        "policyBinding",
        "policySystem",
        "policyRef",
        "principal",
        "action",
        "resource",
        "decision",
        "decisionTime",
    ),
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
POLICY_DECISIONS = {"allowed", "denied", "allowed_with_constraints", "needs_confirmation", "stale_context"}
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


def load_core_fixture(root: Path, name: str) -> dict[str, Any]:
    fixture = root / "fixtures" / "core" / name
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


def load_local_analysis_fixture(root: Path) -> dict[str, Any]:
    return load_core_fixture(root, "local-analysis")


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
    if schema == "cap.core.policy_decision.v1" and "decision" in record and record.get("decision") not in POLICY_DECISIONS:
        errors.append({"code": "invalid_policy_decision", "path": f"{path}.decision", "message": "Invalid policy decision."})
    _scan_for_secret_values(record, path, errors)
    return errors


def validate_negative_case(case: dict[str, Any], path: str) -> CoreValidationResult:
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []

    if case.get("schema") != "cap.core.negative_case.v1":
        return validate_negative_record(case, path)

    case_name = case.get("case")
    record = case.get("record")
    records = case.get("records")
    if isinstance(record, dict):
        errors.extend(validate_core_record(record, f"{path}.record"))
    if isinstance(records, dict):
        for name, value in records.items():
            if isinstance(value, dict) and "schema" in value:
                errors.extend(validate_core_record(value, f"{path}.records.{name}"))
            elif isinstance(value, list):
                for index, item in enumerate(value):
                    if isinstance(item, dict) and "schema" in item:
                        errors.extend(validate_core_record(item, f"{path}.records.{name}[{index}]"))

    if case_name == "assembly-action-without-capability" and isinstance(record, dict):
        if "executableAction" in record and "capability" not in record:
            errors.append(
                {
                    "code": "assembly_action_without_capability",
                    "path": f"{path}.record",
                    "message": "Executable Assembly actions must be declared through Capability.",
                }
            )
            errors = _drop_error(errors, "missing_required_field", f"{path}.record.capability")
    elif case_name == "capability-implies-authorization" and isinstance(record, dict):
        if any(key in record for key in ("authorization", "authorized", "permissions")):
            errors.append(
                {
                    "code": "capability_implies_authorization",
                    "path": f"{path}.record",
                    "message": "Capability declarations must not imply authorization.",
                }
            )
    elif case_name == "duplicate-object-id" and isinstance(records, dict):
        ids = _collect_ids(records)
        duplicates = sorted(item for item in set(ids) if ids.count(item) > 1)
        if duplicates:
            errors.append(
                {
                    "code": "duplicate_object_id",
                    "path": f"{path}.records",
                    "message": f"Duplicate Core object id(s): {', '.join(duplicates)}.",
                }
            )
    elif case_name == "external-standard-copied-inline" and isinstance(record, dict):
        if _contains_key(record, "inlineExternalStandardSchema"):
            errors.append(
                {
                    "code": "external_standard_copied_inline",
                    "path": f"{path}.record",
                    "message": "External standard schemas must be referenced or profiled, not copied into Core records.",
                }
            )
    elif case_name == "missing-policy-decision" and isinstance(records, dict):
        if "policy_decision" not in records and "policy-decision" not in records:
            errors.append(
                {
                    "code": "missing_policy_decision",
                    "path": f"{path}.records",
                    "message": "Executable Assembly requires an explicit PolicyDecision for candidate conformance.",
                }
            )
    elif case_name == "remote-evidence-overclaim" and isinstance(record, dict):
        _append_overclaim_errors(record, f"{path}.record", errors)
    elif case_name == "run-evidence-overclaims-correctness" and isinstance(record, dict):
        _append_overclaim_errors(record, f"{path}.record", errors)
    elif case_name == "run-without-assembly-reference" and isinstance(record, dict):
        if record.get("schema") == "cap.core.run.v1" and "assemblyId" not in record:
            errors.append(
                {
                    "code": "run_without_assembly_reference",
                    "path": f"{path}.record.assemblyId",
                    "message": "Run must reference an Assembly.",
                }
            )
            errors = _drop_error(errors, "missing_required_field", f"{path}.record.assemblyId")
    elif case_name == "runtime-oci-missing-image-reference" and isinstance(record, dict):
        if record.get("type") == "runtime" and record.get("standard") == "OCI":
            target = record.get("target", "")
            if not isinstance(target, str) or not target.startswith("oci://") or "@sha256:" not in target:
                errors.append(
                    {
                        "code": "runtime_binding_missing_image_reference",
                        "path": f"{path}.record.target",
                        "message": "OCI runtime binding must use a content-addressed OCI image reference.",
                    }
                )
    elif case_name == "stale-service-binding" and isinstance(record, dict):
        if record.get("type") == "service" and record.get("status") == "stale":
            errors.append(
                {
                    "code": "stale_service_binding",
                    "path": f"{path}.record.status",
                    "message": "Stale service bindings are not acceptable for executable candidate checks.",
                }
            )
    elif case_name == "unanchored-reproducible-artifact" and isinstance(record, dict):
        integrity = record.get("ref", {}).get("integrity") if isinstance(record.get("ref"), dict) else None
        if record.get("metadata", {}).get("reproducible") is True and not integrity:
            errors.append(
                {
                    "code": "unanchored_reproducible_artifact",
                    "path": f"{path}.record.ref.integrity",
                    "message": "Artifacts marked reproducible need an integrity anchor or external evidence.",
                }
            )
    elif case_name == "undeclared-network-access" and isinstance(record, dict):
        if record.get("type") == "service" and record.get("constraints", {}).get("networkDeclaredByPolicy") is False:
            errors.append(
                {
                    "code": "undeclared_network_access",
                    "path": f"{path}.record.constraints.networkDeclaredByPolicy",
                    "message": "Remote service access must be declared by policy and resource constraints.",
                }
            )
    elif case_name == "unresolved-artifact-reference" and isinstance(records, dict):
        assembly = records.get("assembly")
        artifact_ids = set(records.get("artifactIds", []))
        if isinstance(assembly, dict):
            missing = [artifact for artifact in assembly.get("artifacts", []) if artifact not in artifact_ids]
            if missing:
                errors.append(
                    {
                        "code": "unresolved_artifact_reference",
                        "path": f"{path}.records.assembly.artifacts",
                        "message": f"Assembly references unknown artifact(s): {', '.join(missing)}.",
                    }
                )

    errors = _dedupe_diagnostics(errors)
    warnings = _dedupe_diagnostics(warnings)
    return CoreValidationResult(ok=not errors, errors=errors, warnings=warnings, summary={"case": case_name})


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

    errors.extend(validate_core_record(fixture["source_artifacts"], "source-artifacts"))
    for index, artifact in enumerate(artifacts):
        errors.extend(validate_core_record(artifact, f"source-artifacts.artifacts[{index}]"))
    for name, record in (
        ("capability", capability),
        ("assembly", assembly),
        ("policy-decision", policy_decision),
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
    _require_subset(run.get("serviceBindings", []), binding_ids, "run.serviceBindings", errors)

    service_bindings = [binding for binding in binding_records if binding.get("type") == "service"]
    policy_network = policy_decision.get("conditions", {}).get("network")
    for binding in service_bindings:
        if binding.get("status") == "stale":
            errors.append({"code": "stale_service_binding", "path": f"assembly.bindingRecords.{binding.get('id')}.status", "message": "Service binding is stale."})
        target = binding.get("target", "")
        if isinstance(target, str) and target.startswith(("http://", "https://")) and policy_network not in {"allowlist", "enabled"}:
            errors.append(
                {
                    "code": "undeclared_network_access",
                    "path": f"assembly.bindingRecords.{binding.get('id')}.target",
                    "message": "Remote service access must be declared by policy conditions.",
                }
            )

    if run_evidence.get("runId") != run.get("id"):
        errors.append({"code": "run_evidence_mismatch", "path": "run-evidence.runId", "message": "RunEvidence must reference Run."})
    _append_overclaim_errors(run_evidence, "run-evidence", errors)
    _require_subset(run_evidence.get("materials", []), artifact_ids, "run-evidence.materials", errors)
    _require_subset(run_evidence.get("products", []), artifact_ids, "run-evidence.products", errors)
    _require_subset(run_evidence.get("digestViews", []), binding_ids, "run-evidence.digestViews", errors)
    if service_bindings and run_evidence.get("records", {}).get("remoteLimitations"):
        warnings.append(
            {
                "code": "remote_unverifiable_surface",
                "path": "run-evidence.records.remoteLimitations",
                "message": "Remote service surfaces are recorded but not semantically verified by Core.",
            }
        )

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


def validate_core_negative_suite(root: Path) -> dict[str, Any]:
    suite = root / "fixtures" / "core" / "negative"
    expected = _load_json(suite / "expected-validation.json")["cases"]
    cases = []
    problems = []
    for filename, expected_codes in sorted(expected.items()):
        record = _load_json(suite / filename)
        validation = validate_negative_case(record, filename)
        actual_codes = sorted({error["code"] for error in validation.errors})
        ok = actual_codes == sorted(expected_codes) and not validation.ok
        if not ok:
            problems.append(f"{filename}: expected {sorted(expected_codes)}, got {actual_codes}")
        cases.append(
            {
                "name": filename,
                "ok": ok,
                "expectedErrorCodes": sorted(expected_codes),
                "actualErrorCodes": actual_codes,
            }
        )
    return {"ok": not problems, "cases": cases, "problems": problems}


def build_core_conformance_report(root: Path, target_level: str = "L3") -> dict[str, Any]:
    fixtures = []
    for name in CORE_FIXTURE_NAMES:
        fixture = load_core_fixture(root, name)
        validation = validate_core_fixture(fixture)
        fixtures.append(
            {
                "name": name,
                "path": f"fixtures/core/{name}",
                "ok": validation.ok,
                "summary": validation.summary,
                "errors": validation.errors,
                "warnings": validation.warnings,
                "checks": [
                    _report_check("schema", validation.errors, {"unknown_schema", "missing_required_field", "invalid_binding_type", "invalid_binding_status", "invalid_run_state", "invalid_policy_decision"}),
                    _report_check("ref-closure", validation.errors, {"unknown_reference", "invalid_reference_list", "missing_required_binding_type", "digest_binding_not_in_assembly"}),
                    _report_check("policy", validation.errors, {"policy_binding_mismatch", "missing_policy_decision", "undeclared_network_access"}),
                    _report_check("binding", validation.errors, {"stale_service_binding", "secret_value_in_core_record"}),
                    _report_check("run-evidence", validation.errors, {"run_evidence_mismatch", "digest_binding_evidence_mismatch", "run_evidence_overclaims_correctness"}),
                    {
                        "category": "security",
                        "ok": not validation.errors,
                        "errorCodes": sorted({error["code"] for error in validation.errors if error["code"] in {"secret_value_in_core_record", "undeclared_network_access", "run_evidence_overclaims_correctness"}}),
                        "warningCodes": sorted({warning["code"] for warning in validation.warnings}),
                    },
                ],
            }
        )
    negative_suite = validate_core_negative_suite(root)
    ok = all(fixture["ok"] for fixture in fixtures) and negative_suite["ok"]
    return {
        "schema": "cap.core.conformance_report.v1",
        "validator": {
            "name": "cap_core.reference_validator",
            "version": CORE_VALIDATOR_VERSION,
        },
        "status": "draft-track-candidate-prep",
        "targetLevel": target_level,
        "ok": ok,
        "fixtures": fixtures,
        "negativeSuites": [
            {
                "name": "fixtures/core/negative",
                "ok": negative_suite["ok"],
                "cases": negative_suite["cases"],
                "problems": negative_suite["problems"],
            }
        ],
        "unsupportedFeatures": [
            "workflow execution",
            "external policy evaluation",
            "secret retrieval",
            "remote service semantic verification",
            "cryptographic attestation verification",
        ],
    }


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


def _drop_error(errors: list[dict[str, str]], code: str, path: str) -> list[dict[str, str]]:
    return [error for error in errors if not (error.get("code") == code and error.get("path") == path)]


def _dedupe_diagnostics(items: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    result: list[dict[str, str]] = []
    for item in items:
        key = (item.get("code", ""), item.get("path", ""))
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


def _contains_key(value: Any, key: str) -> bool:
    if isinstance(value, dict):
        return key in value or any(_contains_key(child, key) for child in value.values())
    if isinstance(value, list):
        return any(_contains_key(child, key) for child in value)
    return False


def _collect_ids(value: Any) -> list[str]:
    ids: list[str] = []
    if isinstance(value, dict):
        if isinstance(value.get("id"), str):
            ids.append(value["id"])
        for child in value.values():
            ids.extend(_collect_ids(child))
    elif isinstance(value, list):
        for child in value:
            ids.extend(_collect_ids(child))
    return ids


def _append_overclaim_errors(record: dict[str, Any], path: str, errors: list[dict[str, str]]) -> None:
    records = record.get("records", {})
    if isinstance(records, dict) and records.get("semanticCorrectnessVerifiedByCore") is True:
        errors.append(
            {
                "code": "run_evidence_overclaims_correctness",
                "path": f"{path}.records.semanticCorrectnessVerifiedByCore",
                "message": "RunEvidence must not claim Core verified semantic correctness.",
            }
        )


def _report_check(category: str, errors: list[dict[str, str]], codes: set[str]) -> dict[str, Any]:
    error_codes = sorted({error["code"] for error in errors if error["code"] in codes})
    return {"category": category, "ok": not error_codes, "errorCodes": error_codes, "warningCodes": []}
