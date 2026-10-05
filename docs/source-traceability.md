# Concept source traceability

**Sole project-specific source:** the complete NAZAR concept/specification supplied in the repository request. This index helps evaluators distinguish its proposed claims from repository artifacts.

| Concept element from supplied brief | Where represented here | Repository status |
|---|---|---|
| Secret random light pattern and measured actual stimulus | `README.md`, `docs/architecture.md`, `docs/causal-detector.md` | Design only; no phone stimulus engine |
| Challenge-response question rather than suspicious-device classification | `README.md`, `docs/prior-art-and-positioning.md` | Core concept preserved; no real sensing result |
| Wi-Fi Ear, ESP32-C5/S3 class, metadata-only capture, no payload decryption, probe-request drop | `docs/architecture.md`, `ear/README.md`, `schemas/ear-record.draft.schema.json`, `ethics/PRIVACY.md` | Proposed hardware/interface only; no firmware |
| Survey/lock channel approach; approximately 100 ms per-flow bins | `docs/architecture.md`, `docs/causal-detector.md`, `ear/README.md` | Proposed; not measured |
| Lagged transition and level model; 0–3 s response; ridge regression; surrogate codes; FDR; second code; proposed SPRT | `docs/causal-detector.md`, `tools/causal_reference.py` | Partial offline reference on synthetic traces only; no live detector or calibrated test |
| Covered-lens null control | `experiments/E02-covered-lens-null.md` | Planned experiment, not run |
| RSSI + phone pose/orientation and rough region only | `docs/localization.md` | Mathematical proposal only; no localization implementation/result |
| Optical flash ON/OFF, motion compensation, multi-view persistence, local candidate model, difficult negatives | `docs/optical-pipeline.md`, `docs/ml-boundaries.md`, `experiments/E06-optical-on-off.md`, `experiments/E07-lens-dataset.md`, `experiments/E08-multiview-persistence.md`, `models/MODEL_CARD.md` | Design and experiment plans only; no images, dataset, weights, or classifier |
| Four evidence tiers and coverage; no “room is safe” statement | `README.md`, `docs/evidence-format.md`, `docs/limitations.md` | Proposed semantics; not a finished UI |
| Hash chain, hardware-backed phone signature, standalone verification | `docs/evidence-format.md`, `tools/evidence_chain.py` | Hash-chain reference only; no signature or Android keystore code |
| Offline phone-first processing; privacy/person blanking; legal/ethical review | `docs/architecture.md`, `ethics/PRIVACY.md`, `ethics/ETHICS.md`, `ethics/LEGAL_NOTES.md` | Design commitments; no finished safeguards in an app |
| Seven-item Phase‑1 MVP and H0–H48 progression | `docs/48-hour-plan.md`, `docs/demo-script.md` | Future build plan only |

Repository additions not claimed by the concept as tested product behavior are explicitly called **draft**, **reference**, **synthetic**, or **planned**. No experimental outcome is inferred from this table.
