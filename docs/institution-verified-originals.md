# Reviewed institution originals

`fetch_institution_latest_pdfs.py --verified-originals-manifest PATH` optionally
recovers an already admitted IMF report from the existing private `OriginalCache`.
It is disabled by default. The production workflow does not pass this option or
expose a recovery input. This change contains synthetic tests, not a real-report
allowlist or PDFs.

Use this entry point only with originals downloaded from the official site and
reviewed against their frozen source identity. A review must establish the actual
PDF's identity, official download URL, bytes, SHA-256 and page count. Approval is
represented by the explicit allowlist; the loader does not itself perform a human
identity review or fetch the review receipt. A valid cache read demonstrates the
approved original's bytes, not a successful live source request.

## Manifest contract

The UTF-8 JSON object has exactly `schema` (integer `1`), `institution` (`imf`),
`frozen_pending_sha256` and `records` (1–100 entries, no duplicate identities).
Each record has these exact fields:

| Field | Required value |
| --- | --- |
| `item` | All seven frozen pending fields: `guid`, `title`, `source_url`, `date`, `pdf_candidates`, `scrape_url`, `coveo_unique_id`. |
| `official_landing_url`, `official_pdf_url` | Reviewed official HTTPS URLs without credentials; default port or 443. The supported eLibrary journal landing and PDF paths must match. Unsupported routes are rejected. |
| `doi` | Reviewed DOI. |
| `sha256`, `size`, `pages` | Exact original-byte digest, byte count and parsed PDF page count. |
| `binding` | Existing `OriginalCache` binding: deterministic source filename, matching hash/size, institution scope, MinerU endpoint/options and their canonical digest. |
| `verification` | Exactly `method: official_browser_download`, `review: approved`, `receipt_sha256`, and a timezone-aware `reviewed_at`. |

`frozen_pending_sha256` is **historical snapshot provenance only**. It records the
queue snapshot used for review; the loader validates its format, not that snapshot's
contents. It is not compared with the current queue file, whose retry counters and
timestamps change. `receipt_sha256` likewise identifies the separately reviewed
receipt. The enforcement boundary is exact equality of every `item` field in the
allowlist, selected report and already admitted pending record, plus the original
cache binding and payload checks. A snapshot hash never authorizes a new item or
substitutes for these comparisons.

The original publication timestamp and source page remain unchanged. The manifest
records the actual official download URL separately; cover dates and download
dates cannot replace publication metadata. Reviewed metadata may be committed,
but PDF bytes and storage credentials must remain outside Git.

## Recovery and completion

The loader validates the complete allowlist before reading storage. Recovery is
limited to entries present in the queue when the run began and selected by the
ordinary retry limits. Unlisted reports follow ordinary intake. The helper only
calls `OriginalCache.get`; it never uploads, creates a MinerU task/ledger, removes
pending entries or writes seen state.

The existing cache verifies object metadata, content type, length and SHA-256.
Recovery also checks the deterministic filename, configured byte limit, genuine
unencrypted PDF parsing and approved page count before atomically materializing
the file. Missing objects, changed source fields, invalid metadata and altered
bytes are rejected; the report remains queued and is not marked successful by a
fallback request. An invalid allowlist aborts before recovery starts.

Accepted files enter the normal fetch manifest and MinerU/extraction/translation
path. Each row carries `acquisition_method: verified_original_cache` and the
complete `verified_original_*` proof group. Partial or unknown proof fields are
rejected by the source-health contract. The source summary reports the recovered
count and explicitly leaves live PDF access unverified. Cache recovery changes
`ok`/`empty` to `degraded`; it cannot erase an existing source error. Discovery
failure with only cached recoveries stays `error`, while accepted-source processing
can continue independently.

The fetcher's seen file is provisional. The existing workflow durably commits
downloaded seen state only after complete translated source coverage and private
translated handoff; pending retirement still depends on that durable seen state.
Extraction or translation failure therefore leaves the original pending for retry.

Run the offline contract tests with
`python3 -B scripts/test_institution_verified_originals.py`. They cover default-off
behavior, exact identity, cache tampering, admission, provenance, preserved errors,
complete recovery markers and retained pending state after downstream failure.
