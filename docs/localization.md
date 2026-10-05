# RF localization — proposed regionalization

**Scope:** a rough region or hotspot to guide optical inspection. Metric/centimeter-level localization is explicitly out of scope for the Phase‑1 concept.

## Proposed observations

After a responding flow has been identified, the phone records RSSI at multiple positions and orientations. Phone pose (proposed via ARCore) and heading/orientation help interpret measurements and body-shadowing effects. A path-loss approximation from the concept is:

```text
RSSI = P₀ − 10 n log₁₀(d) + B(θ) + ε
```

where `d` is distance, `B(θ)` represents orientation/body-shadowing effects, and `ε` captures noise and environmental variation.

## Intended output

The output is a coarse hotspot/region (for example, “likely upper shelf / north wall”) and an uncertainty note. A 2D room sketch or AR pointer may be used during the Finale. The application should not imply centimeter accuracy or a guaranteed bearing.

A coverage display should separate scanned from uncertain/untested areas. A future report should state the fraction or representation of the tested coverage only when the app can compute it defensibly; it must not infer that unvisited space is safe.

## Confounds and fallbacks

- Walls, reflections, other transmitters, channel hopping, phone orientation, and the user’s body can alter RSSI.
- Poor AR tracking should widen the region/uncertainty; an IMU/dead-reckoning fallback is only a proposed degraded mode.
- If the ear is disconnected, RF regionalization is unavailable; the proposed fallback is optical-only inspection with that limitation stated.
- No RF response does not establish that no camera exists.

## Validation boundary

The concept proposes RSSI plus phone pose for rough regionalization. No location data, indoor map, calibration, distance estimate, or localization error measurement is included in this repository. Any Finale result should report the actual setup and uncertainty, not a fabricated accuracy score.
