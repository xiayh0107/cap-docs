from __future__ import annotations

from typing import Any


def validation_result(digest_id: str, fingerprint: str, response: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "cap.validation_result.v1",
        "digestId": digest_id,
        "fingerprint": fingerprint,
        "ok": True,
        "errors": [],
        "warnings": [],
        "normalizedResponse": response,
    }


def gate_requests(manifest: dict[str, Any], validation: dict[str, Any], policy_ref: str | None = None) -> dict[str, Any]:
    requests = validation.get("normalizedResponse", {}).get("requests", [])
    rows = {row["fieldId"]: row for row in manifest.get("fields", [])}
    decisions = []
    overall = "approved" if requests else "denied"

    for index, request in enumerate(requests):
        field_id = request.get("fieldId")
        row = rows.get(field_id)
        if row is None:
            decision = "unknown_field"
            problems = [{"code": "gate_unknown_field", "message": "Unknown field.", "fieldId": field_id}]
        elif row.get("timing") != "interactive":
            decision = "not_available"
            problems = [{"code": "gate_not_available", "message": "Field is not available through follow-up.", "fieldId": field_id}]
        else:
            decision = "approved"
            problems = []

        if decision != "approved":
            overall = "denied"

        decisions.append({
            "requestIndex": index,
            "request": request,
            "decision": decision,
            "approvedLevel": request.get("level") if decision == "approved" else None,
            "approvedBudget": request.get("budget") if decision == "approved" else None,
            "requiresUserConfirmation": False,
            "problems": problems,
        })

    return {
        "schema": "cap.gate_result.v1",
        "digestId": manifest["digestId"],
        "fingerprint": manifest["fingerprint"],
        "overallDecision": overall,
        "remainingBudget": None,
        "policyRef": policy_ref,
        "requests": decisions,
        "patch": None,
    }
