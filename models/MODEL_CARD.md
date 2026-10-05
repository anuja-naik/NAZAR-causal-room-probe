# Model card — proposed optical candidate ranker

**Model status: not built, not trained, and not evaluated.** No model file or weights are present in this repository.

## Proposed role

A small local model may rank cropped optical candidates produced by the proposed flash ON/OFF and multi-view pipeline. The concept suggests MobileNetV3-Small or a custom small CNN, with a candidate patch around 32 × 32 pixels. The model is not the causal RF decision-maker and must not independently promote a candidate to a confirmed-camera tier.

## Proposed label space

- lens;
- screw;
- LED;
- glass;
- chrome;
- water droplet;
- clutter.

These are proposed categories from the supplied concept. The data collection protocol, annotations, class definitions, and model choice are not yet set.

## Training/evaluation data

- Dataset: none included.
- Training, validation, and test split: not defined.
- Sample counts: not available.
- Metrics or thresholds: none measured.
- Known domain gaps: bathrooms/water, surface materials, lighting, focus, view angle, occlusion, device camera/flash variation, and motion.

Do not report an accuracy, recall, or confidence number until the dataset provenance, independent split, sample count, per-class results, and test conditions are documented. Avoid splitting near-duplicate crops from the same physical scene across train and test in a way that leaks scene identity.

## Intended safeguards

- Run locally where feasible; do not upload room images for inference.
- Prefer candidate crops, not full-room video storage.
- Blank people before retaining an image for evidence.
- Expose candidate status and uncertainty; require independent evidence and human inspection.
- Record model/version/hash and whether the model actually ran on NPU or CPU. Do not claim NPU use without device verification.

## Release gate

Before adding weights: choose a model, document code and weight licenses/attribution, publish a data card, freeze a test protocol, evaluate difficult negatives, and record model hash. Any trained weights are Finale work unless separately disclosed and authorized.
