# Wi‑Fi Ear — status and draft interface

**Status: concept and interface draft only.** There is no selected board, firmware, capture binary, USB‑C implementation, or hardware measurement in this repository.

## Proposed role

The ear is a small passive radio front-end connected to the phone through USB‑C OTG. An ESP32‑C5 / ESP32‑S3 class board is proposed; the exact board must be finalized after capture and Android-compatibility testing. The ear’s role is limited to radio capture, timestamps/channel/RSSI/frame metadata, flow/bin handling, and channel control. It is **not** the analysis brain. The phone performs the causal statistics, localization, optical analysis, evidence fusion, and UI.

## Proposed capture boundary

The concept calls for metadata such as timestamp, channel, RSSI, transmitter/receiver addressing, frame length, and retry status, with approximately 100 ms aggregation per flow. It excludes payload decryption and drops probe requests. The final capture policy and legal review must be completed before any real use.

The draft schema in `../schemas/ear-record.draft.schema.json` describes a possible **per-flow bin** for phone-side analysis, not a wire protocol. It uses an opaque session-scoped `flow_id` rather than a persistent raw address. How raw addresses are transiently observed and transformed is deliberately unresolved; the final design must minimize retention and must not become a general-purpose tracking tool.

## Survey and lock concepts

- **Survey:** hop channels and identify candidate flows using coarse activity/uplink/volume/burst characteristics. This is only prioritization, not a camera verdict.
- **Lock:** hold a candidate channel for higher-quality continuous measurement during the controlled challenge.

Exact dwell time, candidate filters, channel list, buffering, timestamp synchronization, and behavior on loss/reconnect remain open and must be validated with E10.

## No firmware claim

The repository intentionally contains no `firmware/` source and no flashable binary. H0–H6 of the Finale plan is the hardware/OTG bring-up stage. A replay or synthetic stream must be visibly marked and never represented as a live ear capture.
