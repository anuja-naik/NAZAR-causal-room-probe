"""Small offline reference for lagged stimulus/traffic scoring.

This module implements a Gaussian linear/ridge reference model for synthetic
or externally supplied, already-binned arrays. It does not capture packets,
make a camera verdict, or establish physical performance. See
``docs/causal-detector.md`` for assumptions and boundaries.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np


@dataclass(frozen=True)
class FitScore:
    """Score from one stimulus/traffic pairing."""

    partial_r2: float
    rss_null: float
    rss_full: float
    peak_lag_bins: int | None


@dataclass(frozen=True)
class SurrogateResult:
    """Observed fit compared with caller-supplied surrogate stimuli."""

    observed: FitScore
    empirical_p: float
    surrogate_count: int
    surrogate_scores: tuple[float, ...]


def _as_finite_vector(name: str, values: Iterable[float]) -> np.ndarray:
    array = np.asarray(values, dtype=float)
    if array.ndim != 1:
        raise ValueError(f"{name} must be a one-dimensional array")
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values")
    return array


def fit_response_score(
    stimulus: Iterable[float],
    traffic: Iterable[float],
    *,
    max_lag_bins: int = 30,
    ridge_alpha: float = 1.0,
) -> FitScore:
    """Fit lagged transition/level predictors and score improvement over drift.

    Inputs must already be regularly sampled and time-aligned. Predictor lags
    run from zero through ``max_lag_bins``. The baseline is an intercept plus
    a linear trend. The full model adds standardized lagged ``abs(diff(s))``
    and ``s`` predictors with ridge regularization. The returned statistic is
    in-sample partial R-squared; it is useful as a transparent reference score,
    not as a calibrated decision rule.
    """

    s = _as_finite_vector("stimulus", stimulus)
    x = _as_finite_vector("traffic", traffic)
    if s.size != x.size:
        raise ValueError("stimulus and traffic must have the same number of bins")
    if not isinstance(max_lag_bins, int) or isinstance(max_lag_bins, bool) or max_lag_bins < 0:
        raise ValueError("max_lag_bins must be a non-negative integer")
    if not np.isfinite(ridge_alpha) or ridge_alpha <= 0:
        raise ValueError("ridge_alpha must be finite and greater than zero")
    if s.size <= max_lag_bins + 3:
        raise ValueError("not enough bins for the requested lag window")

    first = max_lag_bins
    row_index = np.arange(first, s.size)
    y = x[row_index]
    trend = np.linspace(-1.0, 1.0, y.size)
    baseline = np.column_stack((np.ones(y.size), trend))

    beta_null, *_ = np.linalg.lstsq(baseline, y, rcond=None)
    residual_null = y - baseline @ beta_null
    rss_null = float(residual_null @ residual_null)

    transition = np.abs(np.diff(s, prepend=s[0]))
    lagged = [transition[row_index - lag] for lag in range(max_lag_bins + 1)]
    lagged.extend(s[row_index - lag] for lag in range(max_lag_bins + 1))
    features = np.column_stack(lagged)

    means = features.mean(axis=0)
    scales = features.std(axis=0)
    scales[scales < np.finfo(float).eps] = 1.0
    standardized = (features - means) / scales

    design = np.column_stack((baseline, standardized))
    penalty = np.eye(design.shape[1], dtype=float) * ridge_alpha
    penalty[0, 0] = 0.0  # Do not penalize the intercept.
    penalty[1, 1] = 0.0  # Do not penalize the linear drift term.
    gram = design.T @ design + penalty
    rhs = design.T @ y
    beta = np.linalg.solve(gram, rhs)
    residual_full = y - design @ beta
    rss_full = float(residual_full @ residual_full)

    if rss_null <= np.finfo(float).eps:
        score = 0.0 if rss_full <= np.finfo(float).eps else -1.0
    else:
        score = float((rss_null - rss_full) / rss_null)

    lag_count = max_lag_bins + 1
    transition_weight = np.abs(beta[2 : 2 + lag_count])
    level_weight = np.abs(beta[2 + lag_count : 2 + 2 * lag_count])
    lag_strength = transition_weight + level_weight
    peak_lag = int(np.argmax(lag_strength)) if np.any(lag_strength > 0.0) else None

    return FitScore(
        partial_r2=score,
        rss_null=rss_null,
        rss_full=rss_full,
        peak_lag_bins=peak_lag,
    )


def surrogate_test(
    stimulus: Iterable[float],
    traffic: Iterable[float],
    surrogate_stimuli: Iterable[Iterable[float]],
    *,
    max_lag_bins: int = 30,
    ridge_alpha: float = 1.0,
) -> SurrogateResult:
    """Compare an observed score with caller-supplied surrogate scores.

    Uses the conservative empirical value ``(1 + count(surrogate >= observed)) /
    (m + 1)``. The caller is responsible for constructing a scientifically
    appropriate, preregistered surrogate family.
    """

    s = _as_finite_vector("stimulus", stimulus)
    x = _as_finite_vector("traffic", traffic)
    surrogate_array = np.asarray(surrogate_stimuli, dtype=float)
    if surrogate_array.ndim != 2:
        raise ValueError("surrogate_stimuli must be a two-dimensional array")
    if surrogate_array.shape[0] == 0:
        raise ValueError("at least one surrogate stimulus is required")
    if surrogate_array.shape[1] != s.size:
        raise ValueError("each surrogate must have the same number of bins as stimulus")
    if x.size != s.size:
        raise ValueError("stimulus and traffic must have the same number of bins")
    if not np.all(np.isfinite(surrogate_array)):
        raise ValueError("surrogate stimuli must contain only finite values")

    observed = fit_response_score(
        s, x, max_lag_bins=max_lag_bins, ridge_alpha=ridge_alpha
    )
    surrogate_scores = tuple(
        fit_response_score(
            surrogate, x, max_lag_bins=max_lag_bins, ridge_alpha=ridge_alpha
        ).partial_r2
        for surrogate in surrogate_array
    )
    exceedances = sum(score >= observed.partial_r2 for score in surrogate_scores)
    empirical_p = (1 + exceedances) / (len(surrogate_scores) + 1)
    return SurrogateResult(
        observed=observed,
        empirical_p=float(empirical_p),
        surrogate_count=len(surrogate_scores),
        surrogate_scores=surrogate_scores,
    )


def benjamini_hochberg(p_values: Iterable[float]) -> np.ndarray:
    """Return Benjamini–Hochberg adjusted q-values in input order."""

    p = np.asarray(p_values, dtype=float)
    if p.ndim != 1:
        raise ValueError("p_values must be one-dimensional")
    if not np.all(np.isfinite(p)) or np.any((p < 0.0) | (p > 1.0)):
        raise ValueError("p_values must be finite and lie in [0, 1]")
    if p.size == 0:
        return np.asarray([], dtype=float)

    order = np.argsort(p, kind="stable")
    ranked = p[order]
    m = p.size
    ranks = np.arange(1, m + 1, dtype=float)
    adjusted_sorted = ranked * m / ranks
    adjusted_sorted = np.minimum.accumulate(adjusted_sorted[::-1])[::-1]
    adjusted_sorted = np.minimum(adjusted_sorted, 1.0)
    adjusted = np.empty_like(adjusted_sorted)
    adjusted[order] = adjusted_sorted
    return adjusted
