# NAZAR — Causal Room Probe

**A phone challenges a room with a fresh light pattern, then tests which encrypted Wi‑Fi flow responds.**

NAZAR is a **causal challenge–response sensing concept** for hidden-camera investigation—not merely an “AI hidden-camera detector.” Its primary idea is to create a stimulus known to the phone, measure the actual light, and ask whether a candidate wireless traffic stream changes after that stimulus. The intended workflow then seeks independent optical confirmation, estimates a rough region, records tested coverage, and produces an evidence bundle whose integrity can be checked.

> **Repository status:** pre-event research and validation groundwork. This is **not** a completed product. The complete Android app, integrated RF/optical pipeline, event-built ear firmware, and end-to-end demo are intended for the 48-hour Grand Finale—not represented as already built here.

## The problem

Privacy-sensitive rooms need more than a list of suspicious devices or a flashlight reflection. Magnetometer/RF alerts can flag ordinary electronics, LAN scans miss devices on independent networks, and reflective screws, taps, glass, or water can fool a simple optical check. NAZAR targets the missing chain: **controlled stimulus → responding device → approximate region → independent optical check → bounded, verifiable evidence**.

## The idea in 30 seconds

A camera that sees a changing scene may change its encoded video traffic. NAZAR generates a fresh, unpredictable light challenge, measures what light was actually produced, and compares that signal with per-flow Wi‑Fi metadata. The analysis does not read or decrypt payloads; for encrypted flows, the content remains untouched. A lag-tolerant statistical model tests whether the actual challenge explains a flow better than surrogate codes; a second fresh code and a covered-lens null control are intended to strengthen the causal argument. A responding region is then checked optically rather than treating RF alone as proof of a camera.

**Stimulus → camera sees scene change → encoder may react → encrypted traffic metadata may change → causal test → second challenge → rough region → optical check → evidence record.**

## Why it is different

Many simple approaches ask whether a device or signal *looks suspicious*. NAZAR asks a more testable question:

> **Does this flow respond, with an appropriate delay, to a fresh stimulus controlled by the phone?**

The proposed contribution is the **integrated workflow**: secret light challenge and measured stimulus, causal RF statistics with null controls, independent optical confirmation, conservative spatial/coverage reporting, and tamper-evident evidence. The repository does **not** claim that each underlying technique is new, or that the integrated system already works in a real room.

## Proposed mechanism

1. **Challenge and measure.** Generate a fresh random light sequence using the phone display and/or torch. Measure actual illumination with the ambient-light sensor; do not assume a requested torch state equals delivered light. Retain both the measured level `s(t)` and its transition signal `|Δs(t)|`. A judge-controlled light change is also a proposed stimulus mode.
2. **Observe metadata, not content.** A proposed USB‑C OTG “Wi‑Fi Ear” (ESP32‑C5 / ESP32‑S3 class; board not selected) passively captures 802.11 metadata such as timestamps, channel, RSSI, frame length, direction/addressing metadata, and retry flag. The concept excludes payload decryption and drops probe requests. The ear is a radio front-end; the phone remains the analysis device. Candidate survey and channel-lock modes are proposed.
3. **Test for a delayed response.** Aggregate traffic into approximately 100 ms bins per flow. The proposed model relates traffic `x_f(t)` to lagged light transitions, lagged light level, slow drift, and noise. A response kernel spans approximately 0–3 seconds and may be estimated with ridge regression. Compare the actual-code score with roughly 200 surrogate codes; correct across tested flows with FDR; repeat with a second fresh code. Sequential stopping (SPRT) is a proposal, not an implemented feature.
4. **Seek independent confirmation.** Use RSSI together with phone pose/orientation for **rough regionalization only**. In that region, alternate phone flash ON/OFF, align frames for motion, inspect the difference, and look for candidates that persist geometrically across viewpoints. A small local classifier may rank lens-like patches against clutter such as screws, LEDs, glass, chrome, and water; it is not the causal decision-maker.
5. **Report bounded evidence.** Combine RF, optical, localization, and coverage observations into transparent result tiers. A result must say what responded, where the evidence points, what was checked, and what remains untested. A hash chain and, during the Finale, a phone-backed signature are proposed for evidence integrity. This is not a claim of court-admissible evidence.

### Result language is deliberately conservative

The four proposed levels are:

- **Tier 1 — Confirmed transmitting camera:** causal RF response, second-code confirmation, optical lens confirmation, and spatial agreement.
- **Tier 2 — Transmitting device, region identified:** repeated causal response and region, but no optical confirmation yet.
- **Tier 3 — Suspected optical lens / possible non-transmitting camera:** optical evidence without an RF response; physical inspection is recommended.
- **Tier 4 — No responding device found in tested coverage:** never “room is safe.” Report the tested coverage and its gaps.

These are **proposed evidence states**, not outputs of a finished app.

## What is actually in this repository

| Present in this pre-event snapshot | Not present / not claimed |
|---|---|
| Architecture, threat/ethics/privacy notes, limitations, event plan, and experiment protocols | Complete Android application or user-facing product |
| Draft ear-stream and evidence-record schemas | ESP32 capture firmware, USB‑C integration, or a selected board |
| A small NumPy reference analysis for lagged stimulus/traffic scoring, empirical surrogate tests, and Benjamini–Hochberg adjustment | Live RF capture or physical light-to-traffic measurements |
| A deterministic **synthetic-only** demo and unit tests | Real camera trials, covered-lens result, optical dataset, trained lens classifier, or accuracy claim |
| A reference SHA‑256 hash-chain builder/verifier, explicitly not a digital-signature verifier | Android hardware-keystore signing or a signed real evidence bundle |
| Empty experiment templates; no empirical results or user images | Integrated localization, optical pipeline, AR UI, or the Finale demo |

**What has been validated here:** 11 unit tests pass for the included reference code (Python 3.13.14 / NumPy 2.3.5 in the recorded local run). They exercise lagged scoring on an injected synthetic response, surrogate-score calculation, FDR adjustment, input checks, and hash-chain tamper detection. The seeded demo also distinguishes its deliberately stimulus-coupled synthetic trace from its deliberately uncoupled synthetic trace under the simulator’s assumptions. This is software-level checking only—not physical validation of NAZAR’s sensing hypothesis. No real-world experimental result was supplied with the concept brief, so none is reported as completed.

## Pre-event work vs. Grand Finale work

| Before the event (this repository) | Intended during the 48-hour Grand Finale |
|---|---|
| Freeze the concept, assumptions, limitations, protocols, and data/evidence drafts | Build the Android skeleton and bring up the phone–ear link |
| Check reference statistics on synthetic positive/null traces | Implement live stimulus measurement, ear parsing, binning, plots, causal analysis, surrogate testing, and second challenge |
| Specify E01/E02/E03/E04/E06/E07/E08/E10/E11/E11e/E12; record results only when actually run | Run and log real trials, including the covered-lens null; downgrade the RF claim if it is weak or inconsistent |
| Document privacy, ethics, attribution, and implementation boundaries | Integrate four-tier/coverage UI, optical ON/OFF inspection, rough regionalization, and evidence export/verification |
| No product app, firmware, model weights, or captured dataset | Freeze new features in the last hours; rehearse and report only measured results |

See [`DISCLOSURE.md`](DISCLOSURE.md), [`docs/48-hour-plan.md`](docs/48-hour-plan.md), and [`experiments/RESULTS.md`](experiments/RESULTS.md).

## Run the pre-event reference checks

Python 3.10+ and NumPy are required. No Android SDK, ESP-IDF, network access, or camera hardware is needed for these checks.

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m tools.synthetic_demo --seed 7 --surrogates 200
```

The demo labels every output `SYNTHETIC_ONLY`. It shows that the reference analysis can distinguish a deliberately constructed stimulus-coupled trace from a deliberately uncoupled trace under the simulation assumptions. It says **nothing** about whether a real camera will modulate its traffic strongly or reproducibly enough. The simulator is not a substitute for E01/E02. See [`VALIDATION.md`](VALIDATION.md) for the exact software-only test record.

## Repository map

```text
docs/          Proposed architecture, statistics, optics, localization, evidence, plans
ethics/        Privacy, ethics, legal-review notes, and threat boundaries
experiments/   Protocols, status matrix, and blank result templates
schemas/       Draft-only ear and evidence JSON Schemas
ear/           Hardware/protocol status; no firmware
models/        Model card only; no weights or trained model
tools/         Synthetic statistical reference and hash-chain integrity utility
tests/         Unit tests for those pre-event utilities
```

> The directory labels above are descriptive: this repository intentionally contains **no `android/` application**, no `ear/firmware/`, and no model weights. The app, ear firmware, optical model, and integrated pipeline are Finale work.

## Technical boundaries and known risks

- The key open question is empirical: **does the selected camera produce a sufficiently strong and repeatable traffic response to controlled scene changes?** E01/E02 are the first physical tests.
- Variable-bitrate behavior, frame timing, networking, channel changes, and background traffic may weaken or confound a response. A lack of RF response does not rule out SD-card-only, 4G, offline, or otherwise non-responsive cameras.
- Optical reflections from water, screws, chrome, glass, and clutter can look lens-like. ON/OFF differencing, motion compensation, multi-view persistence, and a classifier are proposals to evaluate, not proven safeguards.
- RSSI/pose supports only a rough region in the proposed scope; no centimeter-level accuracy is claimed.
- “No responding device found” applies only to tested conditions and measured coverage. No universal detection rate, guarantee, or room-safety statement is made.
- Passive radio metadata collection requires a written legal/ethical review before any real deployment. Operate only where authorized.

More detail: [`docs/limitations.md`](docs/limitations.md), [`docs/failure-modes.md`](docs/failure-modes.md), [`docs/ml-boundaries.md`](docs/ml-boundaries.md), [`ethics/PRIVACY.md`](ethics/PRIVACY.md), and [`ethics/LEGAL_NOTES.md`](ethics/LEGAL_NOTES.md).

## Prior art and attribution posture

The supplied concept brief acknowledges that related optical, RF, and light-stimulus work exists and names Blink/Flicker and MotionCompass, but it does not include full bibliographic references. NAZAR is therefore positioned as an integration and workflow contribution, **not** as the invention of hidden-camera detection or of its individual sensing techniques. See [`docs/prior-art-and-positioning.md`](docs/prior-art-and-positioning.md) for the citation gap and no-overclaim policy.

No third-party code, model weights, images, or datasets are bundled. The reference scripts use NumPy, declared and attributed in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). The concept owner/team has not supplied a repository license choice; see [`LICENSE_STATUS.md`](LICENSE_STATUS.md).

## Closing statement

**NAZAR does not merely look for suspicious signals. It challenges the room with a secret light pattern and asks which device responds—then independently looks for the lens and records what was actually checked.**
