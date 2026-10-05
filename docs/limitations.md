# Limitations and non-claims

NAZAR is a proposed sensing workflow, not a guarantee that every hidden camera can be found. These boundaries should be visible to judges and users.

## Sensing limitations

- **Traffic response is the main technical risk.** A camera may use fixed bitrate, buffer traffic, transmit intermittently, or otherwise expose little stimulus-linked variation. Whether a selected camera’s encrypted traffic responds strongly and reproducibly is unvalidated.
- **RF visibility is conditional.** A camera may use an unobserved channel, 4G, a separate network, SD-card-only storage, or no transmission during the test. Absence of a response does not imply absence of a camera.
- **The metadata signal is indirect.** Packet sizes, volumes, timing, RSSI, and channel information are not the video itself; the proposed detector does not decrypt content.
- **Background traffic can confound.** Other devices, periodic traffic, frame/key-frame behavior, changing network conditions, and channel hopping may appear related by chance. Surrogates, FDR, repeated challenges, and controls are proposed mitigations, not a demonstrated error rate.
- **Timing matters.** Phone light-sensor and ear clocks may differ. Delay, dropped records, bin size, and channel lock need measurement.
- **The null test may not generalize.** Covering a lens is a key causal control; its effect must be observed on the actual test camera and setup.

## Optical limitations

- Flash reflections from screws, taps, chrome, glass, LEDs, water, and clutter can resemble a lens.
- Motion between ON/OFF frames can create false differences; pose/optical-flow compensation needs validation.
- A small patch classifier can fail under occlusion, focus, exposure, angle, or unseen materials. No trained model or performance score is included.
- IR points are possible clues, not proof of a camera.
- Optical-only inspection may find candidates that do not transmit, but may also generate false positives.

## Localization and coverage limitations

- RSSI is affected by multipath, walls, body shadowing, orientation, and other transmitters.
- Phase‑1 scope is rough regionalization only. No centimeter-level accuracy or general localization performance is claimed.
- Coverage is only the area/surfaces the user actually inspected. A coverage map must distinguish unknown regions and must not say “safe.”

## Privacy, legal, and evidence limitations

- Passive RF metadata collection requires a written legal/ethical review before real use. This repository is not legal advice.
- Person blanking and minimum data collection are design intentions, not implemented safeguards in this repository.
- A hash chain is not a signature. A signature is not proof that a sensor measurement is true or legally admissible.
- No identity recognition, cloud inference, packet decryption, network intrusion, or camera takeover is part of the concept.

## Claims this repository does not make

It does not claim 100% detection, universal camera coverage, a measured accuracy/confidence number, a validated dataset, a tested Android NPU, centimeter localization, legal admissibility, or that any room is safe. Quantitative claims must be linked to documented trials, dataset provenance, sample counts, conditions, and uncertainty.
