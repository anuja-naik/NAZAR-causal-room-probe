# Proposed operating modes and failure handling

**Status:** behavior requirements for a future app; no app or device-level fallback is implemented here.

## Conceptual modes

| Mode | Intended behavior | Required disclosure |
|---|---|---|
| Full Probe | RF challenge/response, rough regionalization, optical check, evidence/coverage | Report each unavailable or incomplete stage |
| Optical Only | Use optical inspection and possible IR clues when the ear is unavailable | State that RF confirmation/localization was unavailable; do not infer no camera from that |
| RF Confirmation | Focus on a responding flow and repeat a fresh challenge/null control | A responding flow is not itself an optical camera confirmation |
| Replay / Demo | Replay a previously captured phone-side trace if live hardware is unavailable | Persistent `REPLAY`/`SIMULATED` label; never present as live measurement |

## Failure and degraded behavior

- **Ear disconnected:** stop RF claims and offer optical-only mode if the user continues. Preserve the failure in the session record.
- **No RF response:** do not declare the room clear. Continue optical scanning if appropriate; non-transmitting, SD-card-only, 4G, or otherwise unobserved cameras remain possible.
- **Weak/inconsistent light-to-traffic relationship:** return inconclusive/negative for the tested conditions; report the data. Do not silently substitute another camera/run or lower the threshold after looking at outcomes.
- **Poor or uneven illumination:** the optical flash may improve contrast in some scenes, but performance is unvalidated. Ask for a controlled scan condition and report limits.
- **Poor AR tracking:** widen the region/uncertainty. An IMU/dead-reckoning fallback is proposed only as a degraded estimate, not a precise localization.
- **Low battery:** prioritize preserving the session/evidence record and reduce expensive optional stages; the exact policy is unimplemented.
- **NPU unavailable:** use CPU only if feasible and explicitly state that NPU execution was not verified. Never claim hardware acceleration based on model availability alone.
- **Dropped ear records or clock mismatch:** mark bins/timing uncertain and avoid a definitive causal result until data quality is adequate.
- **Optical candidate without RF response:** report a candidate/possible non-transmitting device and recommend physical inspection; do not promote it to a confirmed transmitting-camera tier.
- **Replay fallback:** retain provenance labels through plots, exports, and the demo. A replay is a demonstration aid, not experimental evidence from the current room.

The final implementation must make degraded states visible and must not convert missing inputs into a positive safety claim.
