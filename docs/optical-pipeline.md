# Optical confirmation — proposed pipeline

**Status:** design notes only. No Camera2 integration, captured frames, lens dataset, trained classifier, or optical-performance result is included.

## Role in NAZAR

RF response narrows attention to a candidate flow/region; it does not establish that a camera lens is present. Optical inspection is an independent evidence path and is also important when a camera does not transmit over observable Wi‑Fi (for example, an SD-card-only device).

## Proposed sequence

1. **Guide the scan to a candidate region.** Use the rough RF hotspot as a scan aid, without claiming precise coordinates.
2. **Acquire paired frames.** Alternate phone flash OFF and ON and capture synchronized frames. The proposed contrast is `D = I_on − I_off` after alignment.
3. **Compensate for motion.** Use phone pose/IMU/AR information and optical flow/geometric warping so that the phone’s movement is not mistaken for a flash reflection.
4. **Extract candidate reflections.** Suppress stable background where feasible, then keep candidate patches rather than processing/storing unnecessary full-room imagery.
5. **Check multi-view persistence.** Observe whether a candidate remains geometrically consistent across viewpoints. Ordinary specular highlights may move or disappear; a true lens may be more stable, but this is an experimental hypothesis, not a guarantee.
6. **Rank locally.** A possible quantized MobileNetV3-Small or custom small CNN may rank 32×32 candidate patches across lens, screw, LED, glass, chrome, water droplet, and clutter classes. The classifier is advisory; it must not independently set the RF causal verdict or overrule evidence tiers.
7. **Inspect possible IR sources.** A self-emitting IR point that does not follow the phone’s stimulus may be reported as a separate candidate signal, not as proof of a camera.

## Important negative classes

The supplied concept specifically calls out screws, LEDs, glass, chrome, water droplets, and clutter. Water is important because droplets can behave like small optical elements. A polished demo must include difficult negatives, especially in bathroom-like scenes, rather than evaluating only clean lens examples.

## Privacy-by-design constraints

- Do not identify, recognize, or track people.
- Blank/mask people before retaining any necessary evidence image, as proposed in the concept.
- Prefer local candidate crops and short-lived processing over saving room video.
- Keep original images out of experiment commits unless collection, consent, minimization, and release are reviewed.
- A candidate classification is not legal or factual proof that a camera exists.

## Required validation

- E06: whether ON/OFF differencing isolates flash-dependent reflections under controlled conditions.
- E07: whether a labelled lens-vs-clutter dataset can support a small local classifier; dataset provenance and train/test separation must be documented.
- E08: whether multi-view geometric persistence helps distinguish lens candidates from ordinary reflections.

No dataset size, accuracy target, or classifier threshold is claimed here because none was supplied or measured. Model and data cards should be completed before any trained model is presented.
