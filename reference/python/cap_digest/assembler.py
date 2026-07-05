from __future__ import annotations

import html
from dataclasses import dataclass
from typing import Any

SENSITIVE_PATTERNS = ("password", "secret", "token", "api_key", "credential", "private_key")


@dataclass(frozen=True)
class DigestResult:
    text: str
    manifest: dict[str, Any]


def _is_sensitive_name(name: str, patterns: list[str] | tuple[str, ...] = SENSITIVE_PATTERNS) -> bool:
    lower = name.lower()
    return any(pattern in lower for pattern in patterns)


def _escape_data(value: Any) -> str:
    return html.escape(str(value), quote=False)


def _column_line(column: dict[str, Any], patterns: list[str]) -> tuple[str, bool]:
    name = column["name"]
    typ = column["type"]
    examples = column.get("examples", [])[:2]
    if _is_sensitive_name(name, patterns):
        return f'{name} <{typ}> e.g. <data>[masked: sensitive name]</data>', True
    rendered = ", ".join(f"<data>{_escape_data(v)}</data>" for v in examples)
    return f"{name} <{typ}> e.g. {rendered}", False


def assemble_table(source: dict[str, Any], policy: dict[str, Any]) -> DigestResult:
    label = source["label"]
    rows = source["rows"]
    cols = source["cols"]
    budget = policy["budget"]
    tokenizer = policy.get("tokenizer", "heuristic_v1")
    fingerprint = policy.get("fingerprint", f"structure_v1:{label}-{rows}x{cols}")
    patterns = policy.get("redaction", {}).get("sensitiveNamePatterns", list(SENSITIVE_PATTERNS))

    column_lines: list[str] = []
    redacted = False
    for column in source["columns"]:
        line, masked = _column_line(column, patterns)
        column_lines.append(line)
        redacted = redacted or masked

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
            '- [cap_caveat_redacted] f1:table@columns#compact: values in "api_token" were masked',
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
                "warnings": ["values in api_token masked"] if redacted else [],
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


def validate_response(digest_text: str, manifest: dict[str, Any], response: dict[str, Any]) -> dict[str, Any]:
    selected = {row["fieldId"] for row in manifest["fields"] if row.get("selected") is True}
    errors: list[dict[str, str]] = []

    evidence = set(response.get("evidence", []))
    for claim in response.get("claims", []):
        evidence.update(claim.get("evidence", []))

    for field_id in sorted(evidence):
        if field_id not in selected:
            errors.append({"code": "unknown_or_unselected_evidence", "fieldId": field_id})
        elif field_id not in digest_text:
            errors.append({"code": "evidence_not_in_digest_text", "fieldId": field_id})

    return {"ok": not errors, "errors": errors}
