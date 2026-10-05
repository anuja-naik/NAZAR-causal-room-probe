# Proposed three-minute demonstration script

**Status:** storyboard only. No hardware, app, live trace, room set, or result is included in this repository. Demonstrate only what is actually implemented at the Finale; visibly label replay or simulation.

## 0:00–0:20 — The problem

“A flashlight reflection can come from a screw, tap, glass, or water. NAZAR asks a stronger question: does a device respond to a fresh light challenge only the phone knows?”

## 0:20–0:45 — Challenge

Start a room probe. Show the fresh challenge being generated and the ambient-light sensor’s measured trace. State whether this is a live run or a replay.

## 0:45–1:10 — RF response (only if physically measured)

Show the stimulus and per-flow metadata trace. Explain that packet payload is not decrypted. If a candidate appears, show the actual response lag and the surrogate comparison; do not display a bare “AI says camera” verdict.

## 1:10–1:30 — Second code

Run a second fresh challenge and show whether the same flow responds again. If it does not, report the inconclusive outcome.

## 1:30–1:50 — Rough region

Walk/scan only if regionalization was actually integrated. Show a coarse hotspot and uncertainty, not a centimeter pin.

## 1:50–2:10 — Optical check

Demonstrate the paired flash ON/OFF scan and, if available, candidate persistence/classifier output. Include a difficult negative such as water, screw, or chrome if the set supports it.

## 2:10–2:30 — Null control

Cover the test camera’s lens while its stream continues. Run the stimulus again and show both traffic continuity and the causal statistic. If the relationship does not weaken as expected, say so; do not edit the plot or substitute a simulation without a clear replay label.

## 2:30–2:45 — Evidence integrity

Show the exported record and state whether the check verifies a hash chain, a cryptographic signature, or both. Alter one byte only if the live verifier is ready; explain the exact failure.

## 2:45–3:00 — Honest close

“NAZAR does not tell you that a room is safe. It reports what responded, where the evidence points, how strong the evidence is, and what was actually checked.”

## Presenter checklist

- State live vs replay vs synthetic before showing a trace.
- Identify which experiment, camera, setup, and number of trials produced any result.
- Show the covered-lens result, including continued traffic, not just a score.
- Mention non-transmitting cameras and untested coverage.
- Do not claim universal detection, an accuracy number without a dataset, court admissibility, or a signature that was not verified.
