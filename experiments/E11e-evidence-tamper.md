# E11e — Evidence tamper check

**Status:** planned for an eventual end-to-end bundle; the current hash-chain utility has unit tests only.

## Question

Does changing one byte in an evidence record invalidate the relevant integrity check?

## Planned test

1. Produce a test-only evidence chain and record whether the verifier checks hash consistency, chain linkage, digital signature, or each separately.
2. Verify the original test object.
3. Change one byte in a record and verify again.
4. Separately modify a previous-hash link and, if implemented, a signature-covered byte.
5. Record exact tool/version and output.

## Important boundary

The current Python utility checks only the SHA‑256 chain and has no signature. Its tests are not a phone-key signing test and do not demonstrate trusted provenance. Any demo should label the check precisely: `hash chain valid/invalid` and `signature valid/not checked/invalid`, rather than one ambiguous `verified` status.
