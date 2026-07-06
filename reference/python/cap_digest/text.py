from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

FIELD_RE = re.compile(r'<field\s+([^>]+)>\n(.*?)\n</field>', re.DOTALL)
ATTR_RE = re.compile(r'(\w+)="([^"]*)"')
FIELD_ID_RE = re.compile(
    r"^f1:[a-z][a-z0-9_]*@[a-z][a-z0-9_]*(?:[-_][a-z0-9_]+)*#[a-z0-9]+(?:[-_][a-z0-9]+)*$"
)
DATA_TAG_RE = re.compile(r"</?data>")


@dataclass(frozen=True)
class ParsedDigestText:
    version_line: str
    source_line: str
    field_ids: list[str]
    fields: dict[str, dict[str, str]]


def parse_digest_text(text: str) -> ParsedDigestText:
    lines = text.splitlines()
    if not lines or not lines[0].startswith("cap digest text=v1 fields=f1 "):
        raise ValueError("text_unknown_version")
    if len(lines) < 2 or not lines[1].startswith("# source:"):
        raise ValueError("text_missing_source_line")
    if len(re.findall(r"<field\b", text)) != len(re.findall(r"</field>", text)):
        raise ValueError("text_unclosed_field")

    field_ids: list[str] = []
    fields: dict[str, dict[str, str]] = {}
    for match in FIELD_RE.finditer(text):
        attrs = dict(ATTR_RE.findall(match.group(1)))
        field_id = attrs.get("id")
        if not field_id:
            raise ValueError("text_field_missing_id")
        if not FIELD_ID_RE.fullmatch(field_id):
            raise ValueError("text_invalid_field_id")
        if field_id in fields:
            raise ValueError("text_duplicate_field_id")
        if "trust" not in attrs or "level" not in attrs:
            raise ValueError("text_field_missing_required_attr")
        body = match.group(2)
        if "<field" in body or "</field>" in body:
            raise ValueError("text_nested_field")
        _validate_data_fences(body)
        field_ids.append(field_id)
        fields[field_id] = attrs

    if not fields:
        raise ValueError("text_no_field_blocks")

    return ParsedDigestText(
        version_line=lines[0],
        source_line=lines[1],
        field_ids=field_ids,
        fields=fields,
    )


def _validate_data_fences(body: str) -> None:
    open_fence = False
    for match in DATA_TAG_RE.finditer(body):
        tag = match.group(0)
        if tag == "<data>":
            if open_fence:
                raise ValueError("text_nested_data")
            open_fence = True
            continue
        if not open_fence:
            raise ValueError("text_unopened_data")
        open_fence = False
    if open_fence:
        raise ValueError("text_unclosed_data")


def validate_manifest_text_consistency(parsed: ParsedDigestText, manifest: dict[str, Any]) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    selected = {row["fieldId"] for row in manifest.get("fields", []) if row.get("selected") is True}
    text_ids = set(parsed.field_ids)

    for field_id in sorted(selected - text_ids):
        problems.append({"code": "evidence_missing_from_text", "fieldId": field_id})
    for field_id in sorted(text_ids - selected):
        problems.append({"code": "text_field_missing_from_manifest", "fieldId": field_id})

    return problems
