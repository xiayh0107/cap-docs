from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_digest import assemble_table, gate_requests, load_table_basic_pack  # noqa: E402


class FollowupAndPackTest(unittest.TestCase):
    def test_followup_basic_matches_fixture(self) -> None:
        fixture = ROOT / "fixtures" / "followup-basic"
        source = json.loads((fixture / "source.json").read_text(encoding="utf-8"))
        policy = json.loads((fixture / "policy.json").read_text(encoding="utf-8"))
        response = json.loads((fixture / "response.json").read_text(encoding="utf-8"))
        expected_gate = json.loads((fixture / "expected-gate.json").read_text(encoding="utf-8"))
        expected_patch = json.loads((fixture / "expected-patch.json").read_text(encoding="utf-8"))

        digest = assemble_table(source, policy)
        decisions = gate_requests(digest.text, digest.manifest, response, source, policy)

        self.assertEqual(
            {
                "schema": "cap.gate_result.v1",
                "decisions": [
                    {
                        "fieldId": decision.fieldId,
                        "allowed": decision.allowed,
                        "reason": decision.reason,
                        "patchSchema": decision.patch["schema"] if decision.patch else None,
                    }
                    for decision in decisions
                ],
            },
            expected_gate,
        )
        self.assertEqual([decision.patch for decision in decisions if decision.patch is not None], [expected_patch])

    def test_table_basic_pack_loading_matches_fixture(self) -> None:
        expected = json.loads((ROOT / "fixtures" / "pack-table-basic" / "expected-pack.json").read_text(encoding="utf-8"))
        pack = load_table_basic_pack(ROOT)
        actual = {
            "schema": "cap.pack_validation.v1",
            "pack": {
                "name": pack["name"],
                "sourceTypes": pack["sourceTypes"],
                "fieldIds": [field["id"] for field in pack["fields"]],
                "redactors": pack["redactors"],
            },
        }
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
