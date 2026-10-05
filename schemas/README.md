# Draft schemas

These JSON Schemas are pre-event design artifacts, not finalized wire, storage, or signing specifications. They contain no real captured data.

- `ear-record.draft.schema.json`: possible per-flow metadata-bin record for a future phone/ear data path. Session-scoped `flow_id` is a privacy-oriented draft; raw address processing and retention remain unresolved.
- `evidence-record.draft.schema.json`: possible evidence-chain envelope and top-level fields drawn from the supplied concept.

Before implementation, freeze timestamp semantics, field units, null/unknown handling, canonical serialization, version migration, cryptographic signing rules, and privacy retention. Keep schema changes versioned and do not treat a valid JSON instance as proof that its contents are true.
