# Threat model and security boundaries

**Scope:** concept-level review, not a completed security assessment.

## Assets to protect

- occupants’ privacy and optical imagery;
- credentials and content carried by nearby wireless devices;
- integrity and provenance of stimulus/traffic/optical observations;
- integrity of a generated evidence report;
- user trust in the distinction between a candidate and a confirmed tier.

## In-scope concerns

| Concern | Design response in the concept / repository boundary |
|---|---|
| Accidental collection of communications content | No payload decryption or content access; use metadata only |
| Turning passive capture into tracking | Drop probe requests; minimize retained identifiers; review address handling |
| Unnecessary person imagery | No identity/face recognition or tracking; blank people before retaining any image evidence |
| False-positive device verdict | Use causal challenge, surrogate comparison, second code, FDR, optical confirmation, and explicit uncertainty; these remain proposed |
| Overstated coverage/safety | Four evidence tiers and scanned/uncertain coverage; no “room is safe” claim |
| Misrepresented demo trace | Label replay and synthetic traces; do not call them live |
| Evidence alteration | Proposed hash chain and phone-backed signature; current utility tests only hash-chain integrity |
| Unauthorized use | Operate only with legitimate authority; obtain legal/ethical review |

## Out-of-scope claims

This repository does not claim resistance to a deliberately adversarial camera, a compromised phone/OS, malicious ear firmware, fabricated sensor readings, all forms of evidence forgery, legal challenge, or an attacker who can alter the complete chain and recompute hashes. A signature/trusted-key scheme and threat analysis would be required for stronger integrity claims.

## Unresolved controls

- Key generation, storage, rotation, revocation, and public-key verification policy.
- Authenticity/attestation of the phone, ear firmware, model, and sensor timestamps.
- Address pseudonymization and session-linkability limits.
- Secure deletion and user-controlled export/retention.
- Tamper-evident logs for dropped frames and interrupted tests.

No red-team assessment or formal security review has been performed.
