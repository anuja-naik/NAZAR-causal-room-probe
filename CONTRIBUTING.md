# Contributing to the pre-event repository

This repository documents and tests pre-event groundwork; it is not the Finale product. Contributions should preserve that boundary.

## Before proposing a change

- Keep NAZAR’s core mechanism intact: a fresh measured light challenge, a causal response test on encrypted-traffic metadata, independent optical confirmation, conservative localization, and evidence/coverage reporting.
- Label proposed, synthetic, replayed, and physically measured material distinctly. Never turn a synthetic fixture into a reported experiment.
- Do not add an Android product, ear firmware, trained model, or integrated pipeline under the pre-event snapshot. Those are intended Finale work.
- Do not add packet payloads, decrypted traffic, credentials, probe-request captures, faces, identity data, or room imagery without an approved and documented need. The concept excludes payload decryption and drops probe requests.
- Do not add third-party code, weights, datasets, images, or generated assets without recording their source, version, license, and required notices.
- Do not publish raw experiment files until permission, privacy review, and a data-retention decision are recorded.

## Checks

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m tools.synthetic_demo --seed 7 --surrogates 200
```

A passing synthetic test is not evidence of physical sensing performance. The repository has no selected project license yet; see `LICENSE_STATUS.md` before redistribution.
