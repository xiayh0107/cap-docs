from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_digest import parse_digest_text, validate_manifest_text_consistency  # noqa: E402


class DigestTextTest(unittest.TestCase):
    def test_basic_table_digest_text_is_consistent(self) -> None:
        fixture = ROOT / "fixtures" / "basic-table"
        text = (fixture / "expected-digest.txt").read_text(encoding="utf-8")
        manifest = json.loads((fixture / "expected-manifest.json").read_text(encoding="utf-8"))
        parsed = parse_digest_text(text)
        self.assertEqual(set(parsed.field_ids), {"f1:table@shape#base", "f1:table@columns#compact"})
        self.assertEqual(validate_manifest_text_consistency(parsed, manifest), [])

    def test_duplicate_field_id_is_rejected(self) -> None:
        text = """cap digest text=v1 fields=f1 fp=x tokenizer=t budget=1/10
# source: table label=x

<field id="f1:table@shape#base" trust="code" level="1">
a
</field>

<field id="f1:table@shape#base" trust="code" level="1">
b
</field>
"""
        with self.assertRaises(ValueError):
            parse_digest_text(text)


if __name__ == "__main__":
    unittest.main()
