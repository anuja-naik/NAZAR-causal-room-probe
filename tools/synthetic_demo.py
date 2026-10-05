"""Generate an explicitly synthetic causal-sensing demonstration.

The traces here are constructed from known equations. They are not camera
measurements and must never be presented as a live NAZAR result.
"""

from __future__ import annotations

import argparse
import json
from typing import Any

import numpy as np

from tools.causal_reference import benjamini_hochberg, surrogate_test


def _held_binary_code(
    n_bins: int, block_bins: int, rng: np.random.Generator
) -> np.ndarray:
    bit_count = (n_bins + block_bins - 1) // block_bins
    bits = rng.integers(0, 2, size=bit_count)
    return np.repeat(bits, block_bins)[:n_bins].astype(float)


def _measured_code(
    code: np.ndarray, rng: np.random.Generator, noise_sd: float = 0.015
) -> np.ndarray:
    return np.clip(code + rng.normal(0.0, noise_sd, size=code.size), 0.0, 1.0)


def _causal_filter(signal: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    return np.convolve(signal, kernel, mode="full")[: signal.size]


def make_synthetic_scenario(
    *, seed: int = 7, n_bins: int = 1200, block_bins: int = 5
) -> tuple[np.ndarray, dict[str, np.ndarray], np.ndarray]:
    """Return a measured-looking challenge, two synthetic flows, and null codes."""

    if n_bins < 100:
        raise ValueError("n_bins must be at least 100 for this demonstration")
    if block_bins < 1:
        raise ValueError("block_bins must be at least one")

    rng = np.random.default_rng(seed)
    code = _held_binary_code(n_bins, block_bins, rng)
    measured_stimulus = _measured_code(code, rng)
    transition = np.abs(np.diff(measured_stimulus, prepend=measured_stimulus[0]))

    # The response delay and amplitude are imposed by the simulator, not measured.
    transition_kernel = np.zeros(31, dtype=float)
    transition_kernel[2:9] = np.asarray([0.04, 0.10, 0.18, 0.24, 0.20, 0.14, 0.10])
    level_kernel = np.asarray([0.15, 0.25, 0.25, 0.20, 0.15], dtype=float)
    transition_response = _causal_filter(transition, transition_kernel)
    level_response = _causal_filter(measured_stimulus, level_kernel)

    t = np.arange(n_bins, dtype=float)
    background = (
        1800.0
        + 0.9 * t
        + 280.0 * np.sin(2.0 * np.pi * t / 73.0)
        + rng.normal(0.0, 220.0, size=n_bins)
    )
    responsive = (
        background
        + 7800.0 * transition_response
        + 1700.0 * level_response
        + rng.normal(0.0, 170.0, size=n_bins)
    )

    # Independent periodic traffic, bursts, and noise: no stimulus term is used.
    null_rng = np.random.default_rng(seed + 1009)
    null_flow = (
        2050.0
        + 1.0 * t
        + 430.0 * np.sin(2.0 * np.pi * t / 61.0)
        + null_rng.normal(0.0, 260.0, size=n_bins)
    )
    burst_mask = null_rng.random(n_bins) < 0.035
    null_flow += burst_mask * null_rng.uniform(700.0, 2600.0, size=n_bins)

    # This independent held-code family is for the synthetic illustration only.
    surrogate_rng = np.random.default_rng(seed + 2027)
    surrogate_codes = np.vstack(
        [
            _measured_code(
                _held_binary_code(n_bins, block_bins, surrogate_rng), surrogate_rng
            )
            for _ in range(200)
        ]
    )

    traffic = {
        "synthetic_responsive_flow": np.maximum(responsive, 0.0),
        "synthetic_null_flow": np.maximum(null_flow, 0.0),
    }
    return measured_stimulus, traffic, surrogate_codes


def run_demo(*, seed: int = 7, surrogates: int = 200) -> dict[str, Any]:
    if surrogates < 1 or surrogates > 200:
        raise ValueError("surrogates must be between 1 and 200 in this demo")
    stimulus, flows, all_surrogates = make_synthetic_scenario(seed=seed)
    selected_surrogates = all_surrogates[:surrogates]

    p_values: list[float] = []
    analyses = []
    for flow_id, traffic in flows.items():
        result = surrogate_test(
            stimulus,
            traffic,
            selected_surrogates,
            max_lag_bins=30,
            ridge_alpha=1.0,
        )
        p_values.append(result.empirical_p)
        analyses.append(
            {
                "flow_id": flow_id,
                "partial_r2": round(result.observed.partial_r2, 6),
                "peak_lag_bins": result.observed.peak_lag_bins,
                "empirical_p": result.empirical_p,
                "surrogate_count": result.surrogate_count,
            }
        )

    q_values = benjamini_hochberg(p_values)
    for item, q_value in zip(analyses, q_values, strict=True):
        item["fdr_q"] = float(q_value)

    return {
        "status": "SYNTHETIC_ONLY",
        "disclaimer": (
            "Generated traces only; no phone, camera, Wi-Fi ear, RF capture, or "
            "physical light measurement is involved. This does not validate E01/E02."
        ),
        "seed": seed,
        "bin_ms": 100,
        "n_bins": int(stimulus.size),
        "surrogate_count": surrogates,
        "analysis": "lagged transition/level ridge reference; in-sample partial R2",
        "flows": analyses,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--surrogates", type=int, default=200)
    args = parser.parse_args()
    print(json.dumps(run_demo(seed=args.seed, surrogates=args.surrogates), indent=2))


if __name__ == "__main__":
    main()
