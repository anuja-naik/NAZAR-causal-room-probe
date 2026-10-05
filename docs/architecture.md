# Proposed architecture

**Status:** design derived from the supplied NAZAR concept. No integrated hardware/software pipeline exists in this repository. Component choices and interfaces below remain subject to Finale bring-up and measurement.

## System boundary

The phone is the instrument and decision point. A small external “Wi-Fi Ear” is proposed only because the phone’s ordinary Android Wi-Fi interface may not expose the required passive 802.11 capture mode. The ear supplies metadata; all stimulus control, statistics, optical analysis, evidence fusion, and reporting remain phone-side. No server or cloud inference is required by the concept.

```mermaid
flowchart TD
    subgraph PHONE[ iQOO phone — proposed analysis and user interface ]
      ST[Fresh random stimulus\ntorch and/or display]
      ALS[Ambient-light sensor\nmeasured s(t)]
      TIME[Time alignment and\n100 ms flow bins]
      STAT[Causal statistics\nlag model + surrogates + FDR]
      LOC[RSSI + phone pose/orientation\nrough regionalization]
      CAM[Camera + flash + IMU\npaired optical scan]
      OPT[Motion alignment + ON/OFF difference\nmultiview persistence + local classifier]
      FUSE[Evidence tiers + coverage map]
      SIGN[Hash chain + proposed\nhardware-backed signature]
      REPORT[Offline report / verifier export]
      ST --> ALS --> TIME --> STAT
      TIME --> LOC --> CAM --> OPT --> FUSE
      STAT --> FUSE
      OPT --> FUSE --> SIGN --> REPORT
    end
    subgraph EAR[ Proposed USB-C OTG Wi-Fi Ear ]
      CAP[802.11 metadata capture]
      BIN[Timestamp / channel / RSSI / frame metadata\nflow aggregation and channel control]
      CAP --> BIN
    end
    BIN -->|USB-C metadata stream; no payload| TIME
```

The diagram represents the **proposed** system, not a compiled app or validated interface.

## Component responsibilities

| Component | Proposed responsibility | Current repository status |
|---|---|---|
| Stimulus engine | Generate a fresh random light code; optionally accept a judge/manual light change; log requested and measured timing | Protocol described; no phone code |
| Ambient-light sensor | Measure actual output and produce `s(t)`; derive level and transition signals | No hardware traces or calibration |
| Wi-Fi Ear | Passive 802.11 metadata capture; channel survey/lock; timestamps, channel, RSSI, frame length, direction/addressing metadata, retry; approximately 100 ms per-flow bins | Draft interface only; no board chosen or firmware |
| Causal statistics | Fit lagged transition/level response plus drift; compare actual code against surrogates; FDR across flows; repeat with a fresh code | Small synthetic-only reference script; not the live detector |
| RF localization | Combine RSSI observations with phone pose/orientation; report a region/hotspot, not metric certainty | Mathematical proposal only |
| Optical pipeline | Paired flash ON/OFF images; motion compensation; candidate extraction; multi-view persistence; local classification; possible IR inspection | Design only; no optical code or images |
| Evidence and UI | Four evidence tiers, scanned/uncertain coverage, record inputs and limitations, chain/hash and eventual phone-backed signature; optional local-language explanation only after the tier is fixed | Draft schema and hash-chain utility only; no app or signature implementation |

## Phone as instrument

The concept assigns the phone multiple load-bearing roles:

- display/torch as controlled illumination;
- ambient-light sensor as the measurement of delivered stimulus;
- CPU as the auditable statistical-analysis path;
- camera, flash, and IMU for optical inspection and motion compensation;
- optional local accelerator for a small optical model, if verified on the chosen device;
- hardware-backed keystore for a future evidence signature;
- USB-C OTG as the connection to the proposed ear.

These are intended uses, not claims that every device/API has been tested. In particular, do not claim NPU use unless it is verified on the Finale device.

## Proposed data path

1. A room-probe session creates a fresh code and a session identifier.
2. The phone records the measured stimulus and timing; the ear reports passive metadata.
3. The phone aligns those streams, groups metadata into per-flow bins, and performs candidate pre-filtering.
4. For a locked candidate channel, the phone tests the measured transition and level signals against traffic time series over the proposed response window.
5. A second fresh code and null-control observations provide additional evidence. RF response is not itself a camera verdict.
6. The phone estimates a rough region from RSSI/pose, then requests an optical scan.
7. Optical, RF, and coverage observations feed a bounded evidence tier and a human-readable report.
8. A future Android implementation may hash-chain the evidence and sign it with a hardware-backed key. Offline verification should distinguish chain integrity from signature validity.

## Trust boundaries and non-goals

- The RF path is passive metadata analysis only: no Wi-Fi password cracking, packet payload decryption, credential collection, camera takeover, or camera-feed access.
- The phone is the trusted analysis endpoint in the proposed design; the ear is not the intelligence/decision engine.
- A hash chain detects changes within a presented chain; it does not prove who captured the data. A signature and documented capture process would be separate requirements.
- A replay/fallback trace must be visibly marked `REPLAY`/`SIMULATED`; it must never be presented as live measurement.
- No cloud service, people identification, face recognition, or person tracking is part of the concept.
- Tier 4 describes only observed responses and tested coverage; it never establishes that a room is safe.

## Proposed operating modes

The supplied concept describes four intended modes: **Full Probe** (RF + optical + localization + evidence), **Optical Only** (ear unavailable), **RF Confirmation** (repeat a challenge for a candidate flow), and **Replay / Demo** (recorded traces, visibly labelled replay/simulated). Degraded-state behavior is summarized in `failure-modes.md`.

## Unresolved integration decisions

- Exact ESP32-class board, capture mode, regulatory/legal review, and stable OTG interface.
- Time-base synchronization and timestamp uncertainty between phone sensor samples and ear records.
- Whether to stream packet events or pre-aggregated bins, while preserving the required per-flow time series and avoiding unnecessary retention.
- Candidate-flow prefilter and survey dwell/hop schedule.
- Stimulus chip duration, intensity limits, measurement calibration, and human-driven input protocol.
- Response kernel regularization and surrogate construction matched to the real stimulus sequence.
- Optical frame timing, motion compensation, thresholding, and negative-class dataset.
- Localization coordinate representation, uncertainty reporting, and coverage-area calculation.
- Evidence field definitions, canonical serialization, signing-key lifecycle, and user export controls.

No unresolved item is silently assumed to be solved by the prototype scripts.
