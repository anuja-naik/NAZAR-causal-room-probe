# E07 — Lens-versus-clutter dataset

**Status:** planned; no dataset or trained model exists.

## Question

Can a small local classifier rank lens-like candidate patches against relevant clutter without unsupported performance claims?

## Proposed label classes

Lens, screw, LED, glass, chrome, water droplet, and clutter, as listed in the supplied concept.

## Dataset and evaluation requirements

- Record provenance, capture permission, device/lighting conditions, annotation rules, and exclusions.
- Avoid faces, occupants, and unnecessary room context; retain only authorized candidate patches.
- Split train/validation/test by physical object or scene where feasible to reduce near-duplicate leakage.
- Report sample counts and per-class results, not one unqualified accuracy number.
- Freeze thresholds on validation data; evaluate once on a separate test set.
- Disclose model architecture, quantization, weights/source/license, code version, and checksum.

No target sample count, model, threshold, or accuracy goal is set by this repository. Do not create or publish model weights until provenance and licenses are reviewed.
