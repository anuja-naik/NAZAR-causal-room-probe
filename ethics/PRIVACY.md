# Privacy design

NAZAR’s purpose is defensive privacy investigation. Its proposed operation should collect the minimum information needed to test whether a flow responds to a controlled light stimulus and to document a bounded result.

## Intended privacy constraints

- **No payload inspection or decryption.** The RF path uses metadata only; it does not decrypt traffic or access camera feeds.
- **Drop probe requests.** The supplied concept explicitly excludes probe requests to avoid turning the ear into a general-purpose people-tracking sensor.
- **No credential collection or network intrusion.** No password cracking, credential theft, device takeover, exploit, or persistence.
- **Offline by design.** Core stimulus, sensing, analysis, optical inspection, and report generation are intended to run on the phone without cloud inference.
- **No person identity.** No face recognition, identity recognition, or person tracking. The proposed optical pipeline blanks people before retaining any necessary image evidence.
- **Minimize optical retention.** Process locally; retain only necessary candidate evidence; avoid storing continuous room video.
- **Limit RF retention.** Use session-scoped flow identifiers where practical. The concept names transmitter/receiver addresses as capture metadata; the final implementation must document whether those are transiently observed, transformed, or retained. No raw-address retention policy has been validated yet.
- **Report uncertainty and coverage.** Do not turn “no response” into “safe.” Record the scope and gaps of the check.

## Before collecting real data

1. Obtain permission to inspect the space and test devices.
2. Complete the legal/ethical review for passive radio metadata collection.
3. Decide whether each field is necessary and how long it is retained.
4. Keep data local; exclude raw captures/images from public Git by default.
5. Document whether a trace is live, replayed, or synthetic.
6. Remove room/person/device identifiers from any shareable artifact unless explicitly required and approved.

These safeguards are design requirements, not implemented controls in a product app. The repository contains no real RF data, room images, or personal data.
