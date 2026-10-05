# E01 — Encrypted-traffic response to measured light

**Status:** planned; not run.  
**Priority:** first physical validation question.

## Question

Does the selected Wi‑Fi camera’s observable traffic volume change in relation to a controlled light stimulus that the camera can see?

## Setup

Use a camera and test network the team is authorized to operate, a phone measuring actual light output, and the proposed ear capture path once available. Record camera/network configuration, channel, physical layout, light level, bin width, and time alignment. Capture metadata only; do not decrypt payloads or collect credentials.

## Procedure outline

1. Fix the camera and test environment; record its operating mode and any available variable-bitrate setting.
2. Run a fresh random light sequence while recording measured `s(t)` and per-flow traffic metadata.
3. Repeat with a no-stimulus/background condition and with a new challenge sequence.
4. Preserve the traffic trace even if it shows no response.
5. Predeclare the lag grid, traffic metric, surrogate generation, number of surrogates/repeats, and multiple-testing family before analyzing results.

## Record

Stimulus and traffic traces, actual timing and dropped-bin information, flow/channel, camera/network setup, response score/lag, surrogate count and empirical p-value, FDR q-value, trial count, deviations, and whether the trace is live/replay.

## Interpretation

A positive-looking association is only an initial response observation. It is not a camera verdict and must be followed by E02, a second fresh-code check, and independent optical confirmation. If no reproducible response is observed, report it and downgrade the RF claim rather than selecting a more favorable run without disclosure.

No numeric acceptance threshold or sample size is specified by the supplied concept; preregister these before the experiment.
