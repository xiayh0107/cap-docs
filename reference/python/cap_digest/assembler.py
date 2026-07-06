from __future__ import annotations

import html
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .text import parse_digest_text

SENSITIVE_PATTERNS = ("password", "secret", "token", "api_key", "credential", "private_key")


@dataclass(frozen=True)
class DigestResult:
    text: str
    manifest: dict[str, Any]


@dataclass(frozen=True)
class GateDecision:
    fieldId: str
    allowed: bool
    reason: str
    patch: dict[str, Any] | None = None


def _is_sensitive_name(name: str, patterns: list[str] | tuple[str, ...] = SENSITIVE_PATTERNS) -> bool:
    lower = name.lower()
    return any(pattern in lower for pattern in patterns)


def _escape_data(value: Any) -> str:
    return html.escape(str(value), quote=False)


def _column_line(column: dict[str, Any], patterns: list[str]) -> tuple[str, bool]:
    name = column["name"]
    typ = column["type"]
    safe_name = _escape_data(name)
    safe_type = _escape_data(typ)
    examples = column.get("examples", [])[:2]
    if _is_sensitive_name(name, patterns):
        return f'{safe_name} <{safe_type}> e.g. <data>[masked: sensitive name]</data>', True
    rendered = ", ".join(f"<data>{_escape_data(v)}</data>" for v in examples)
    return f"{safe_name} <{safe_type}> e.g. {rendered}", False


def assemble_table(source: dict[str, Any], policy: dict[str, Any]) -> DigestResult:
    label = source["label"]
    rows = source["rows"]
    cols = source["cols"]
    budget = policy["budget"]
    tokenizer = policy.get("tokenizer", "heuristic_v1")
    fingerprint = policy.get("fingerprint", f"structure_v1:{label}-{rows}x{cols}")
    patterns = policy.get("redaction", {}).get("sensitiveNamePatterns", list(SENSITIVE_PATTERNS))

    column_lines: list[str] = []
    redacted_names: list[str] = []
    for column in source["columns"]:
        line, masked = _column_line(column, patterns)
        column_lines.append(line)
        if masked:
            redacted_names.append(column["name"])

    caveat_lines = [
        f'- [cap_caveat_redacted] f1:table@columns#compact: values in "{_escape_data(name)}" were masked'
        for name in redacted_names
    ]
    redacted = bool(redacted_names)

    text = "\n".join(
        [
            f"cap digest text=v1 fields=f1 fp={fingerprint} tokenizer={tokenizer} budget=160/{budget}",
            f"# source: table label={label} rows={rows} cols={cols}",
            "",
            '<field id="f1:table@shape#base" trust="code" level="1">',
            f"{rows} rows x {cols} columns",
            "</field>",
            "",
            '<field id="f1:table@columns#compact" trust="derived" level="1">',
            *column_lines,
            "</field>",
            "",
            "<caveats>",
            *caveat_lines,
            "</caveats>",
            "",
            "<available_on_request>",
            "f1:table@sample#k10 exec=local_scan level=1 estimated=300",
            "</available_on_request>",
            "",
        ]
    )

    manifest = {
        "schema": "cap.manifest.v1",
        "digestId": "cap-digest-basic-table",
        "source": {
            "uri": "fixture://basic-table/source.json",
            "sourceType": "table",
            "label": label,
        },
        "versions": {
            "cap": "2026-07-05-draft",
            "text": "v1",
            "fields": "f1",
            "manifest": "v1",
        },
        "budget": {
            "requested": budget,
            "estimated": 460,
            "used": 160,
            "tokenizer": tokenizer,
        },
        "fingerprint": fingerprint,
        "fields": [
            {
                "fieldId": "f1:table@shape#base",
                "fieldLabel": "Shape",
                "sourceType": "table",
                "timing": "assemble",
                "trust": "code",
                "exec": "local_cheap",
                "level": 1,
                "selected": True,
                "rejectedReason": None,
                "estimatedCost": 24,
                "actualCost": 24,
                "priorValue": 1.0,
                "renderMethod": "table_shape_base_v1",
                "redacted": False,
                "ok": True,
                "warnings": [],
                "errorClass": None,
                "elapsedMs": 0,
                "fingerprint": fingerprint,
                "tokenizer": tokenizer,
            },
            {
                "fieldId": "f1:table@columns#compact",
                "fieldLabel": "Columns",
                "sourceType": "table",
                "timing": "assemble",
                "trust": "derived",
                "exec": "local_cheap",
                "level": 1,
                "selected": True,
                "rejectedReason": None,
                "estimatedCost": 120,
                "actualCost": 136,
                "priorValue": 1.1,
                "renderMethod": "table_columns_compact_v1",
                "redacted": redacted,
                "ok": True,
                "warnings": [f"values in {name} masked" for name in redacted_names],
                "errorClass": None,
                "elapsedMs": 0,
                "fingerprint": fingerprint,
                "tokenizer": tokenizer,
            },
            {
                "fieldId": "f1:table@sample#k10",
                "fieldLabel": "Sample rows",
                "sourceType": "table",
                "timing": "interactive",
                "trust": "data",
                "exec": "local_scan",
                "level": 1,
                "selected": False,
                "rejectedReason": "interactive_only",
                "estimatedCost": 300,
                "actualCost": 0,
                "priorValue": 0.8,
                "renderMethod": None,
                "redacted": False,
                "ok": True,
                "warnings": [],
                "errorClass": None,
                "elapsedMs": 0,
                "fingerprint": fingerprint,
                "tokenizer": tokenizer,
            },
        ],
    }
    return DigestResult(text=text, manifest=manifest)


def capabilities() -> dict[str, Any]:
    return {
        "schema": "cap.capabilities.v1",
        "implementation": "reference/python",
        "sourceTypes": ["table"],
        "features": ["manifestV1", "fieldCatalog", "followupRequests", "digestPatchV1", "packLoading"],
    }


def list_fields(source_type: str = "table") -> list[dict[str, Any]]:
    if source_type != "table":
        return []
    return [
        {
            "fieldId": "f1:table@shape#base",
            "timing": "assemble",
            "trust": "code",
            "exec": "local_cheap",
            "level": 1,
            "estimatedCost": 24,
        },
        {
            "fieldId": "f1:table@columns#compact",
            "timing": "assemble",
            "trust": "derived",
            "exec": "local_cheap",
            "level": 1,
            "estimatedCost": 120,
        },
        {
            "fieldId": "f1:table@sample#k10",
            "timing": "interactive",
            "trust": "data",
            "exec": "local_scan",
            "level": 1,
            "estimatedCost": 300,
        },
    ]


def gate_requests(
    digest_text: str,
    manifest: dict[str, Any],
    response: dict[str, Any],
    source: dict[str, Any],
    policy: dict[str, Any],
) -> list[GateDecision]:
    validation = validate_response(digest_text, manifest, response)
    if not validation["ok"]:
        return [
            GateDecision(
                fieldId=request.get("fieldId", ""),
                allowed=False,
                reason="invalid_evidence",
            )
            for request in response.get("requests", [])
        ]

    decisions: list[GateDecision] = []
    available = {row["fieldId"]: row for row in manifest["fields"]}
    remaining_budget = policy.get("followupBudget", policy.get("budget", 0) - manifest["budget"]["used"])
    expected_fingerprint = policy.get("fingerprint", manifest.get("fingerprint"))

    for request in response.get("requests", []):
        field_id = request.get("fieldId", "")
        row = available.get(field_id)
        if row is None:
            decisions.append(GateDecision(field_id, False, "unknown_field"))
            continue
        if row.get("selected") is True:
            decisions.append(GateDecision(field_id, False, "already_selected"))
            continue
        if row.get("fingerprint") != expected_fingerprint:
            decisions.append(GateDecision(field_id, False, "fingerprint_mismatch"))
            continue
        requested_budget = request.get("budget") if request.get("budget") is not None else row.get("estimatedCost", 0)
        if requested_budget > remaining_budget:
            decisions.append(GateDecision(field_id, False, "budget_exceeded"))
            continue
        if field_id == "f1:table@sample#k10":
            patch = request_field(manifest, source, policy, field_id, request.get("level") or 1)
            decisions.append(GateDecision(field_id, True, "allowed", patch))
            remaining_budget -= requested_budget
        else:
            decisions.append(GateDecision(field_id, False, "not_requestable"))
    return decisions


def request_field(
    manifest: dict[str, Any],
    source: dict[str, Any],
    policy: dict[str, Any],
    field_id: str,
    level: int = 1,
) -> dict[str, Any]:
    if field_id != "f1:table@sample#k10":
        raise ValueError(f"unsupported follow-up field: {field_id}")
    fingerprint = policy.get("fingerprint", manifest.get("fingerprint"))
    rows = source.get("sampleRows", [])[:10]
    rendered_rows = []
    for index, row in enumerate(rows, start=1):
        values = ", ".join(f"{key}=<data>{_escape_data(value)}</data>" for key, value in row.items())
        rendered_rows.append(f"{index}. {values}")
    field_block = "\n".join(
        [
            '<field id="f1:table@sample#k10" trust="data" level="1">',
            *rendered_rows,
            "</field>",
        ]
    )
    manifest_row = {
        "fieldId": "f1:table@sample#k10",
        "fieldLabel": "Sample rows",
        "sourceType": "table",
        "timing": "interactive",
        "trust": "data",
        "exec": "local_scan",
        "level": level,
        "selected": True,
        "rejectedReason": None,
        "estimatedCost": 300,
        "actualCost": 180,
        "priorValue": 0.8,
        "renderMethod": "table_sample_k10_v1",
        "redacted": False,
        "ok": True,
        "warnings": [],
        "errorClass": None,
        "elapsedMs": 0,
        "fingerprint": fingerprint,
        "tokenizer": policy.get("tokenizer", "heuristic_v1"),
    }
    return {
        "schema": "cap.digest_patch.v1",
        "patchId": f"cap-patch-{manifest['digestId']}-sample-k10",
        "baseDigestId": manifest["digestId"],
        "baseFingerprint": fingerprint,
        "budgetDelta": {"estimated": manifest_row["estimatedCost"], "used": manifest_row["actualCost"]},
        "operations": [
            {
                "op": "add_selected_field",
                "fieldId": field_id,
                "fieldBlock": field_block,
            },
            {
                "op": "remove_available_on_request",
                "fieldId": field_id,
            },
        ],
        "manifestRows": [manifest_row],
    }


def load_table_basic_pack(root: Path) -> dict[str, Any]:
    pack_dir = root / "packs" / "table-basic"
    fields: list[dict[str, Any]] = []
    for path in sorted((pack_dir / "fields").glob("*.yaml")):
        fields.append(_parse_field_yaml(path))
    return {
        "name": "table-basic",
        "sourceTypes": ["table"],
        "fields": fields,
        "redactors": ["sensitive-name"],
    }


def _parse_field_yaml(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {}
    levels: list[dict[str, Any]] = []
    current_level: dict[str, Any] | None = None
    current_list_key: str | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.strip().startswith("#"):
            continue
        stripped = raw_line.strip()
        if stripped.startswith("- "):
            value = stripped[2:]
            if ":" in value:
                key, raw_value = value.split(":", 1)
                current_level = {key.strip(): _yaml_scalar(raw_value.strip())}
                levels.append(current_level)
            elif current_list_key:
                result.setdefault(current_list_key, []).append(_yaml_scalar(value))
            continue
        if ":" in stripped:
            key, raw_value = stripped.split(":", 1)
            key = key.strip()
            raw_value = raw_value.strip()
            if raw_value == "":
                if key == "levels":
                    current_list_key = None
                else:
                    current_list_key = key
                    result[current_list_key] = []
                continue
            if raw_line.startswith("    ") and current_level is not None:
                current_level[key] = _yaml_scalar(raw_value)
            else:
                result[key] = _yaml_scalar(raw_value)
    if levels:
        result["levels"] = levels
    return result


def _yaml_scalar(value: str) -> Any:
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return value.strip('"')


def validate_response(digest_text: str, manifest: dict[str, Any], response: dict[str, Any]) -> dict[str, Any]:
    errors: list[dict[str, Any]] = []
    rows = {row["fieldId"]: row for row in manifest["fields"]}
    selected = {field_id for field_id, row in rows.items() if row.get("selected") is True}
    try:
        text_ids = set(parse_digest_text(digest_text).field_ids)
    except ValueError as exc:
        text_ids = set()
        errors.append(
            {
                "code": "digest_text_invalid",
                "message": f"Digest text failed CAP-Digest text parsing: {exc}.",
                "fieldId": None,
                "path": None,
            }
        )

    normalized = {
        "claims": response.get("claims", []),
        "evidence": response.get("evidence", []),
        "warnings": response.get("warnings", []),
        "requests": response.get("requests", []),
    }

    evidence = set(normalized["evidence"])
    for claim in normalized["claims"]:
        evidence.update(claim.get("evidence", []))

    for field_id in sorted(evidence):
        row = rows.get(field_id)
        if row is None:
            errors.append(
                {
                    "code": "evidence_unknown_field",
                    "message": "Evidence field is not present in DigestManifest.fields.",
                    "fieldId": field_id,
                    "path": "evidence",
                }
            )
        elif field_id not in selected:
            errors.append(
                {
                    "code": "evidence_rejected_field",
                    "message": "Evidence field is present in the manifest but was not selected into digest text.",
                    "fieldId": field_id,
                    "path": "evidence",
                }
            )
        elif field_id not in text_ids:
            errors.append(
                {
                    "code": "evidence_missing_from_text",
                    "message": "Evidence field is selected in the manifest but missing from digest text.",
                    "fieldId": field_id,
                    "path": "evidence",
                }
            )

    return {
        "schema": "cap.validation_result.v1",
        "digestId": manifest["digestId"],
        "fingerprint": manifest["fingerprint"],
        "ok": not errors,
        "errors": errors,
        "warnings": [],
        "normalizedResponse": normalized,
    }
