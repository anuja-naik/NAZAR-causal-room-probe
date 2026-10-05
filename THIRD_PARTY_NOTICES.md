# Third-party notices and component inventory

This inventory applies to the current repository snapshot. It distinguishes installed dependencies from components merely proposed in the supplied concept.

## Used by the pre-event tooling

| Component | Use in this repository | License / attribution | Distribution status |
|---|---|---|---|
| NumPy | Array operations and linear algebra in `tools/causal_reference.py` and the synthetic demo | BSD 3-Clause; NumPy Developers. License text and project notice: <https://github.com/numpy/numpy/blob/main/LICENSE.txt> | Declared in `requirements.txt`; not vendored or copied into this repository. The local test run used NumPy 2.3.5. |
| Python standard library | JSON, hashing, argument parsing, tests, and other runtime support | Python Software Foundation License, as distributed with Python | Not vendored. Requires an independently installed Python interpreter. |

No third-party source files are copied into the repository. NumPy is an optional-to-install package dependency for the reference scripts; no NumPy binaries or source are redistributed here.

## Mentioned as future candidates, not included dependencies

| Candidate named or implied by the supplied concept | Current status |
|---|---|
| Android platform / Camera2 / USB-C OTG APIs | No Android project or SDK code in this snapshot. Specific API and SDK terms must be reviewed when the Finale implementation is selected. |
| ARCore | Proposed pose source in the concept; no SDK, code, or assets included. Review Google’s current terms before use. |
| ESP32-C5 / ESP32-S3 class board and firmware tooling | Board is not finalized; no firmware, SDK, or toolchain files included. Review the selected board and toolchain licenses/notices before use. |
| MobileNetV3-Small or a custom small CNN | Model choice remains open. No architecture implementation, pretrained weights, training data, or model asset is bundled. Record exact source, license, version, checksum, and any fine-tuning provenance before selecting weights. |
| Any future image dataset, optical-flow library, local language model, or report asset | Not included or selected. Add a specific attribution and license entry before adding it. |

The concept brief mentions related work by the names Blink/Flicker and MotionCompass but supplies no full citations. This repository makes no use of their code or materials; bibliographic verification is an open research task documented in `docs/prior-art-and-positioning.md`.
