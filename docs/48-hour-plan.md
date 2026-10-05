# Grand Finale: 48-hour build plan

This plan reflects the supplied Phase‑1 scope. It is a target sequence, not a claim that these tasks are already complete. Keep the phone as the primary product; the laptop/Office Kit is only for mirroring, trace transfer, or verification support.

## H0–H6 — Bring-up

**Build:** Android skeleton, ear communication, Camera2/torch control, Office Kit mirroring/export path, basic traffic plot.  
**Exit check:** obtain a raw traffic plot that visibly changes when the torch is pointed at the selected camera, if the hardware and camera support it. Record failure honestly; do not proceed by relabelling a replay as live.

## H6–H12 — Stimulus and RF stream

**Build:** fresh random code, measured-light timestamps, ear parser, approximately 100 ms bins, RSSI/direction/drop metrics, live plots.  
**Exit check:** plot the measured stimulus and traffic under controlled light-on/off conditions; also record a no-stimulus/background condition.

## H12–H24 — Causal test and null control

**Build:** lagged regression, surrogate comparison, FDR, second fresh code, covered-lens control, evidence-tier decision.  
**Exit check:** run the planned physical trials. The key desired observation is continued traffic with a reduced stimulus-linked statistic after covering the lens. If not observed or not repeatable, downgrade the RF causal claim and show the limitation.

## H24–H36 — Optical and evidence path

**Build:** synchronized flash ON/OFF frames, motion compensation, candidate extraction/classifier, rough regionalization, coverage representation, hash chain, signing/verification prototype.  
**Exit check:** demonstrate optical candidates with difficult negatives; verify chain/signature behavior separately. Tampering should change a valid/invalid integrity check, but the UI must say exactly what was checked.

## H36–H42 — Integration and communication

**Build:** null-control controls, clean evidence tiers, limitations, bilingual report template if feasible, experiment log, replay labeling. Avoid placeholder performance claims.

## H42–H48 — Freeze

No new features. Fix bugs, test the complete path, rehearse the demo three times if feasible, validate exported evidence, and prepare a clearly marked fallback recording if needed. A fallback must be labelled replay/simulated and must not be passed off as live.

## Priority order if time is lost

1. Verify physical light-to-traffic response and covered-lens null (E01/E02).
2. Ensure the first-party data path is stable and plots are truthful.
3. Preserve a basic optical inspection and conservative coverage/report state.
4. Keep evidence integrity checks distinct from cryptographic signature checks.
5. Cut polish/features before cutting provenance, limitations, or controls.

## Out of scope for this Phase‑1 build

- centimeter-level localization;
- multi-phone sweeps;
- institutional dashboards;
- broad/general detection-performance claims.

The event plan should be updated with actual time, ownership, and measured exit checks. A planned exit criterion is not a completed result.
