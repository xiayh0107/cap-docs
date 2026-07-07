from __future__ import annotations

import json
import sys
from argparse import ArgumentParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_core import build_core_interop_report, build_external_core_interop_report  # noqa: E402


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--implementation-name", default="cap_core.reference_validator")
    parser.add_argument("--command", default=None, help="External command template. Supports {root}, {fixture}, and {fixture_path}.")
    parser.add_argument("--report", type=Path, default=None)
    args = parser.parse_args()

    if args.command is None:
        report = build_core_interop_report(ROOT, args.implementation_name)
    else:
        report = build_external_core_interop_report(ROOT, args.implementation_name, args.command)
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report is not None:
        args.report.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0 if all(fixture["ok"] for fixture in report["fixtures"]) else 1


if __name__ == "__main__":
    sys.exit(main())
