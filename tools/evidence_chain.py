"""Reference hash-chain utility for draft NAZAR evidence records.

This is integrity plumbing only. It does not implement public-key signing,
Android Keystore, capture attestation, or legal evidence handling.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

SCHEMA_VERSION = "nazar-evidence-chain-draft-0"
_HASH_RE = re.compile(r"^[0-9a-f]{64}$")
_BODY_KEYS = {"schema_version", "sequence", "previous_hash", "record"}
_ENTRY_KEYS = _BODY_KEYS | {"record_hash"}


@dataclass(frozen=True)
class VerificationResult:
    valid: bool
    checked_entries: int
    errors: tuple[str, ...]


def canonical_json_bytes(value: Any) -> bytes:
    """Return the draft canonical encoding used by this reference utility."""

    try:
        text = json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise ValueError(f"value is not canonical-JSON encodable: {exc}") from exc
    return text.encode("utf-8")


def _digest_body(body: Mapping[str, Any]) -> str:
    return hashlib.sha256(canonical_json_bytes(body)).hexdigest()


def make_entry(
    sequence: int, previous_hash: str | None, record: Mapping[str, Any]
) -> dict[str, Any]:
    """Create one draft chain entry; this does not validate the evidence schema."""

    if not isinstance(sequence, int) or isinstance(sequence, bool) or sequence < 0:
        raise ValueError("sequence must be a non-negative integer")
    if sequence == 0 and previous_hash is not None:
        raise ValueError("the first entry must have previous_hash=None")
    if sequence > 0 and (
        not isinstance(previous_hash, str) or not _HASH_RE.fullmatch(previous_hash)
    ):
        raise ValueError("non-first entries require a lowercase SHA-256 previous_hash")
    if not isinstance(record, Mapping):
        raise ValueError("record must be a mapping/object")

    body = {
        "schema_version": SCHEMA_VERSION,
        "sequence": sequence,
        "previous_hash": previous_hash,
        "record": dict(record),
    }
    return {**body, "record_hash": _digest_body(body)}


def build_chain(records: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Build an in-memory chain from records, for tests or local tooling."""

    chain: list[dict[str, Any]] = []
    previous_hash: str | None = None
    for sequence, record in enumerate(records):
        entry = make_entry(sequence, previous_hash, record)
        chain.append(entry)
        previous_hash = entry["record_hash"]
    return chain


def verify_chain(chain: Any) -> VerificationResult:
    """Verify draft hashes and links; report errors without checking signatures."""

    if not isinstance(chain, list):
        return VerificationResult(False, 0, ("chain must be a JSON array",))

    if not chain:
        return VerificationResult(False, 0, ("chain must contain at least one entry",))

    errors: list[str] = []
    previous_hash: str | None = None
    checked = 0
    for index, entry in enumerate(chain):
        checked += 1
        prefix = f"entry {index}"
        if not isinstance(entry, dict):
            errors.append(f"{prefix}: must be a JSON object")
            previous_hash = None
            continue
        if set(entry) != _ENTRY_KEYS:
            missing = sorted(_ENTRY_KEYS - set(entry))
            extra = sorted(set(entry) - _ENTRY_KEYS)
            errors.append(f"{prefix}: invalid keys (missing={missing}, extra={extra})")
            previous_hash = None
            continue
        if entry.get("schema_version") != SCHEMA_VERSION:
            errors.append(f"{prefix}: unsupported schema_version")
        if (
            not isinstance(entry.get("sequence"), int)
            or isinstance(entry.get("sequence"), bool)
            or entry.get("sequence") != index
        ):
            errors.append(f"{prefix}: sequence must equal its zero-based array index")
        if entry.get("previous_hash") != previous_hash:
            errors.append(f"{prefix}: previous_hash does not match prior record_hash")
        if not isinstance(entry.get("record"), dict):
            errors.append(f"{prefix}: record must be a JSON object")

        stored_hash = entry.get("record_hash")
        if not isinstance(stored_hash, str) or not _HASH_RE.fullmatch(stored_hash):
            errors.append(f"{prefix}: record_hash must be lowercase SHA-256 hex")
            previous_hash = None
            continue

        body = {key: entry[key] for key in ("schema_version", "sequence", "previous_hash", "record")}
        try:
            expected_hash = _digest_body(body)
        except ValueError as exc:
            errors.append(f"{prefix}: {exc}")
            previous_hash = None
            continue
        if stored_hash != expected_hash:
            errors.append(f"{prefix}: record_hash does not match canonical body")
        previous_hash = stored_hash

    return VerificationResult(not errors, checked, tuple(errors))
