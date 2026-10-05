# Project and implementation disclosure

**Snapshot date:** 2026-10-04  
**Purpose:** iQOO Hackathon 2026 Grand Finale pre-event groundwork

## Source of the project concept

The sole project-specific source used for NAZAR’s problem framing, terminology, technical mechanism, innovation position, and proposed architecture in this repository is the complete NAZAR specification supplied in the project request. This repository does not claim ownership of the underlying concept or make a patent, priority, or novelty determination. The submitting team should identify the concept author(s) and confirm permission/ownership before public release; no names or ownership documents were supplied here.

## What this repository adds

This pre-event snapshot contains:

- Written architecture, limits, privacy/ethics boundaries, experiment plans, and a 48-hour implementation plan derived from the supplied specification.
- Draft JSON Schemas for a proposed ear metadata record and evidence-chain envelope. They are design artifacts, not a frozen device protocol.
- A small Python/NumPy reference analysis for a lagged stimulus–traffic model, empirical surrogate comparison, and false-discovery-rate adjustment.
- A reproducible synthetic trace generator and tests for the reference statistics.
- A SHA-256 hash-chain utility and tests. It checks chain integrity only; it is **not** a public-key signature verifier or the Android hardware-keystore implementation.

These utilities are limited, inspectable pre-event groundwork. They are not an Android product, live radio sniffer, camera detector, or end-to-end implementation.

## What is not in this snapshot

- No Android app, integrated pipeline, AR experience, or event demo.
- No ESP32 firmware, selected ear board, USB-OTG capture session, or real RF trace.
- No measured E01/E02/E03/E04/E06/E07/E08/E10/E11/E11e/E12 result.
- No real lens dataset, trained/quantized classifier, model weights, or measured classifier score.
- No camera images, occupant data, real room maps, personally identifying data, or signed evidence bundle.
- No experimental proof that encrypted traffic responds to NAZAR’s light challenge.

All generated numerical examples are synthetic and labelled as such. Empty templates are not results. No performance number in this repository should be read as a real-world detection claim.

## Before the event / during the event

The repository distinguishes pre-event research, synthetic software checks, draft schemas, and experiment protocols from all Finale implementation and physical validation. The complete Android application and integrated pipeline are intended to be built during the 48-hour event. Do not backdate commits, invent trial results, or present simulated traces as live captures.

## Attribution and third-party material

No third-party source code, model, dataset, photo, or firmware is copied into this repository. NumPy is an external runtime dependency and is disclosed in `THIRD_PARTY_NOTICES.md`. Candidate components named by the concept (Android platform APIs, ARCore, ESP32-class hardware/tooling, and a possible MobileNetV3-Small or custom small CNN) are **not bundled or used by the included scripts**; future selection and license review remain open.
