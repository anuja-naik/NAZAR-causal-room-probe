# AI/ML boundaries

NAZAR deliberately does **not** make every decision with AI. The causal question—whether an observed wireless flow responds to a measured challenge—must be answered by an auditable statistical procedure, not by a black-box classifier. A model can rank candidates or help explain results; it cannot invent evidence or change the result tier.

## Proposed model roles from the concept

| Component | Proposed approach in the supplied concept | Allowed role | Status here |
|---|---|---|---|
| Causal RF detector | GLM/linear response model, ridge kernel fitting, surrogate/permutation statistics, FDR; proposed SPRT | Authoritative test of stimulus-linked flow response | Partial NumPy reference only on synthetic traces; no calibrated detector |
| Flow preclassifier | GBDT or 1D-CNN | Prioritize flows for review from coarse activity/uplink/volume/burst behavior; never call a flow a camera | Not implemented; no dataset/model |
| Lens candidate ranker | MobileNetV3-Small or custom small CNN on candidate patches | Rank lens vs. screw/LED/glass/chrome/water/clutter candidates | Not selected, trained, or evaluated; see `../models/MODEL_CARD.md` |
| Hiding-spot suggestion | YOLO-nano class detector | Suggest scan areas/objects, not declare a hidden camera | Proposed only; not part of the current repository or validated Finale result |
| Person blanking | Lightweight segmentation | Mask people before retaining necessary image evidence; no identity recognition | Safeguard requirement only; no implementation |
| Report-language assistance | Small local LLM | Explain a result in plain language / proposed languages; cannot decide evidence tier or make legal conclusions | Proposed only; no model or inference code |

## Decision hierarchy

```text
measured stimulus + flow metadata
              ↓
transparent statistical test (authoritative for causal response)
              ↓
independent optical observations + rough spatial agreement
              ↓
explicit evidence tier and coverage state
              ↓
optional local-language explanation (presentation only)
```

A classifier must not replace the surrogate test, second challenge, null control, or transparent tier logic. A local language model must not interpret raw room imagery independently, invent confidence, change a tier, identify a suspect, or generate legal conclusions. Human-readable text must preserve the underlying numeric result and uncertainty.

## Hardware and privacy constraints

The phone’s CPU is the proposed path for auditable statistics. A Snapdragon NPU may be used for a local optical model if the actual device verifies that execution; otherwise report CPU fallback / NPU not verified. Do not claim NPU acceleration from an intended model format alone. Keep inference offline, minimize stored crops, and blank people before retaining any required image evidence.

No model weights, training data, model hash, accuracy result, or NPU measurement exists in this repository.
