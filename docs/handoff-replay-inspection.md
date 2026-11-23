# Exact handoff replay inspection

`Inspect exact handoff replay identities` reads explicitly named immutable
Extended handoff receipts from the existing private R2 store. Dispatch it on
reviewed `main` with `receipt_hashes` containing 1–20 lowercase SHA-256 values,
separated by commas or newlines. Only the repository owner can run the storage
inspection. It has its own inspection concurrency group, so it does not wait
for or alter the production publication or translation queues.

The script reads only each requested `publication-handoffs/<hash>/receipt.json`,
with a 64 KiB limit, and verifies the exact content hash, receipt schema, locale
and candidate hashes, and producer identity. The one-day artifact contains
only the receipt hash, source generation, candidate map, and producer run,
attempt, and commit. It contains no raw receipts, account data, source text,
provider endpoints, or credentials. A missing or invalid receipt fails the
entire inspection without publishing a partial artifact.

Use the resulting metadata to preserve the original `extended_handoff`,
`extended_source_generation`, `extended_locales`, and `extended_candidate_ids`
when preparing a fresh publication on current `main`. Inspection itself does
not dispatch, cancel, approve, or publish anything. The normal publisher must
still validate all candidate quality, provenance, approvals, and live-state
conditions. Receipt identity is not proof that a candidate should be deployed.
