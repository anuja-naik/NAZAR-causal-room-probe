from __future__ import annotations

import copy
import unittest

from tools.evidence_chain import build_chain, verify_chain


class EvidenceChainTests(unittest.TestCase):
    def test_generated_chain_passes_integrity_check(self) -> None:
        chain = build_chain(
            [
                {"kind": "illustrative-test-record", "value": 1},
                {"kind": "illustrative-test-record", "value": 2},
            ]
        )
        result = verify_chain(chain)
        self.assertTrue(result.valid, result.errors)
        self.assertEqual(result.checked_entries, 2)

    def test_one_byte_content_change_breaks_chain_hash(self) -> None:
        chain = build_chain([{"note": "before"}])
        tampered = copy.deepcopy(chain)
        tampered[0]["record"]["note"] = "Before"  # One ASCII byte differs from "before".
        result = verify_chain(tampered)
        self.assertFalse(result.valid)
        self.assertTrue(any("record_hash" in error for error in result.errors))

    def test_previous_link_change_is_detected(self) -> None:
        chain = build_chain([{"n": 1}, {"n": 2}])
        tampered = copy.deepcopy(chain)
        tampered[1]["previous_hash"] = "0" * 64
        result = verify_chain(tampered)
        self.assertFalse(result.valid)
        self.assertTrue(any("previous_hash" in error for error in result.errors))

    def test_extra_unhashed_field_is_rejected(self) -> None:
        chain = build_chain([{"n": 1}])
        chain[0]["signature"] = "not-a-real-signature"
        result = verify_chain(chain)
        self.assertFalse(result.valid)
        self.assertTrue(any("invalid keys" in error for error in result.errors))

    def test_empty_chain_is_rejected(self) -> None:
        result = verify_chain([])
        self.assertFalse(result.valid)
        self.assertEqual(result.checked_entries, 0)
        self.assertIn("chain must contain at least one entry", result.errors[0])

    def test_non_finite_json_values_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            build_chain([{"measurement": float("nan")}])


if __name__ == "__main__":
    unittest.main()
