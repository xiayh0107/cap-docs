from __future__ import annotations

import json
import sys
from argparse import ArgumentParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_core import compare_core_interop_reports  # noqa: E402


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--expected", type=Path, required=True)
    parser.add_argument("--actual", type=Path, required=True)
    parser.add_argument("--report", type=Path, default=None)
    args = parser.parse_args()

    comparison = compare_core_interop_reports(load_json(args.expected), load_json(args.actual))
    payload = json.dumps(comparison, indent=2, sort_keys=True) + "\n"
    if args.report is not None:
        args.report.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0 if comparison["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
