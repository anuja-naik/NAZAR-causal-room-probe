"""Verify a draft NAZAR SHA-256 hash chain from a JSON array file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from tools.evidence_chain import verify_chain


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chain_json", type=Path, help="JSON file containing an array of chain entries")
    args = parser.parse_args()

    try:
        chain = json.loads(args.chain_json.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 2

    result = verify_chain(chain)
    print(f"Hash chain integrity: {'PASS' if result.valid else 'FAIL'}")
    print(f"Entries checked: {result.checked_entries}")
    print("Signature: NOT CHECKED (this utility has no public-key verifier)")
    for error in result.errors:
        print(f"- {error}")
    return 0 if result.valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
