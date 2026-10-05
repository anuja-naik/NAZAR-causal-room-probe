# E10 — USB-C OTG ear stability

**Status:** planned; no ear hardware/firmware is included.

## Question

Can the selected Android phone maintain stable communication with the selected ESP32-class ear while it streams the required metadata and channel-control status?

## Procedure outline

After board selection, record phone/OS, board, firmware commit, cable/adapter, power mode, session duration, reconnects, dropped records, timestamp continuity, channel transitions, and thermal/battery observations. Exercise survey and lock modes separately. Do not include packet payload or credentials in the test log.

## Interpretation

Report measured stability and failure modes for that hardware combination only. E10 is an integration gate, not evidence that the causal detector works. No OTG run has been performed in this repository.
