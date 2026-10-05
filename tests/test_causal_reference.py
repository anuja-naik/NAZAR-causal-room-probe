from __future__ import annotations

import unittest

import numpy as np

from tools.causal_reference import (
    benjamini_hochberg,
    fit_response_score,
    surrogate_test,
)
from tools.synthetic_demo import make_synthetic_scenario


class CausalReferenceTests(unittest.TestCase):
    def test_score_is_positive_for_constructed_delayed_response(self) -> None:
        stimulus, flows, _ = make_synthetic_scenario(seed=7, n_bins=480, block_bins=5)
        score = fit_response_score(
            stimulus,
            flows["synthetic_responsive_flow"],
            max_lag_bins=20,
            ridge_alpha=1.0,
        )
        self.assertGreater(score.partial_r2, 0.5)
        self.assertIsNotNone(score.peak_lag_bins)

    def test_empirical_p_uses_plus_one_correction(self) -> None:
        stimulus, flows, surrogates = make_synthetic_scenario(
            seed=11, n_bins=480, block_bins=5
        )
        result = surrogate_test(
            stimulus,
            flows["synthetic_responsive_flow"],
            surrogates[:19],
            max_lag_bins=20,
        )
        self.assertEqual(result.surrogate_count, 19)
        self.assertGreaterEqual(result.empirical_p, 1.0 / 20.0)
        self.assertLessEqual(result.empirical_p, 1.0)

    def test_null_fixture_does_not_outscore_causal_fixture(self) -> None:
        stimulus, flows, surrogates = make_synthetic_scenario(
            seed=7, n_bins=480, block_bins=5
        )
        causal = surrogate_test(
            stimulus,
            flows["synthetic_responsive_flow"],
            surrogates[:39],
            max_lag_bins=20,
        )
        null = surrogate_test(
            stimulus,
            flows["synthetic_null_flow"],
            surrogates[:39],
            max_lag_bins=20,
        )
        self.assertLess(causal.empirical_p, null.empirical_p)

    def test_bh_adjustment_preserves_original_order(self) -> None:
        adjusted = benjamini_hochberg([0.01, 0.04, 0.03, 0.20])
        np.testing.assert_allclose(adjusted, [0.04, 0.0533333333333, 0.0533333333333, 0.20])

    def test_invalid_inputs_fail_clearly(self) -> None:
        with self.assertRaises(ValueError):
            fit_response_score([0, 1, 0], [1, 2, 3], max_lag_bins=5)
        with self.assertRaises(ValueError):
            fit_response_score([0, np.nan, 1, 0], [1, 2, 3, 4], max_lag_bins=1)
        with self.assertRaises(ValueError):
            benjamini_hochberg([0.1, 1.1])


if __name__ == "__main__":
    unittest.main()
