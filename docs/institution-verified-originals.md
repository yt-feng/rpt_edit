# Reviewed institution originals

`fetch_institution_latest_pdfs.py --verified-originals-manifest PATH` optionally
recovers an already admitted IMF report from the existing private `OriginalCache`.
It is disabled by default. The production workflow exposes the manual choice
`reviewed_originals`, with `none` as the default for dispatch and schedules. The
only enabled selection, `imf-20261012-reviewed`, binds 17 approved public source
metadata records to SHA-256
`250557000edbc46f0629393a7a43a139b37926cb54c58535ea498866ccd77e67`.
After resetting to current main, the workflow validates that fixed digest, copies
the metadata to `RUNNER_TEMP`, validates the copy and its complete schema, and
passes only the copied path to the fetcher. The `none` path does not read this
manifest. PDF bytes and credentials are not committed.
The reviewed set contains 25,038,788 bytes across 650 parsed pages; 16 originals
were acquired through official browser downloads and one through official HTTPS.

For the reviewed October 12 backlog, a controlled manual run can select this
allowlist with `institutions=imf`, `imf_pending_retries=17`,
`max_per_institution=17` and `max_total=17`. Those caps permit the original backlog
to be attempted; they do not promise an exact allowlist-only run. Only the listed
originals can use the private cache, while other selected reports follow ordinary
source requests. Confirm cache readback before dispatch. A missing cache object
remains an explicit failure, and cached success does not clear live source health.

Use this entry point only with originals downloaded from the official site and
reviewed against their frozen source identity. A review must establish the actual
PDF's identity, official download URL, bytes, SHA-256 and page count. Approval is
represented by the explicit allowlist; the loader does not itself perform a human
identity review or fetch the review receipt. A valid cache read demonstrates the
approved original's bytes, not a successful live source request.

## Live official downloads

The institution production and fetch-test workflows install a pinned Linux-only
browser and the existing subscription client when IMF is selected. The fetcher
first resolves the exact indexed publication's DOI through Crossref, then visits
the publisher-deposited eLibrary page using the working cloud route. It reads the
page's actual download link and checks the publication identity before downloading.
If the exact Crossref record returns 404, an English report may instead use an
actual eLibrary link in its hash-bound official IMF preview. Its independently
visible DOI, ISBN, full title, series, year and issue must all agree; this route
records `official_source_preview` provenance rather than claiming Crossref success.
There is no fixed report URL, guessed journal identifier, exported browser session,
or automatic challenge interaction in this path.

The client is started lazily once per fetch batch. Connection checks can select
among at most three strictly validated VLESS entries from the existing repository
subscription; ordinary browser requests and PDF validation remain separate gates.
Only the transient Linux runner uses this route. A missing or expired subscription,
unsupported source identity, rejected page or invalid PDF keeps ordinary source
fallbacks and durable pending intake active. It cannot mark a report as downloaded.

Each successful live download records its official URLs, DOI, metadata identity,
HTTP results, SHA-256, byte count and parsed page count in `imf_live_download`.
The source-health contract verifies that complete proof group against the archive
row. Live downloads can establish healthy source access; the reviewed private-cache
path retains its separate proof and degraded-source rules below. Existing dependency
holds and successful seen-state deduplication are checked before live downloads.

IEO implementation plans use a separate ordinary HTTPS route before the browser.
The source's complete title identifies a unique evaluation in IEO's official
directory, then an exact-title PDF in that evaluation's `Follow-up by the IMF`
section. All three responses must be successful official URLs, and the PDF must
contain the complete source title. The separate `imf_official_followup` receipt
binds source identity, all page hashes, PDF bytes and parsed pages to the archive
row. It cannot be mixed with browser or private-cache proofs. The source DOI is
retained as preview provenance; it does not assert DOI registration or a DOI printed
inside the downloaded PDF.

## Reviewed cache manifest contract

The UTF-8 JSON object has exactly `schema` (integer `1`), `institution` (`imf`),
`frozen_pending_sha256` and `records` (1–100 entries, no duplicate identities).
Each record has these exact fields:

| Field | Required value |
| --- | --- |
| `item` | All seven frozen pending fields: `guid`, `title`, `source_url`, `date`, `pdf_candidates`, `scrape_url`, `coveo_unique_id`. |
| `official_landing_url`, `official_pdf_url` | Reviewed official HTTPS URLs without credentials; default port or 443. Supported eLibrary journal or book landing and PDF paths must match. Book paths repeat the same 13-digit ISBN, also bound to the DOI. The observed IEO fiscal follow-up pair is restricted to its exact URLs and original pending GUID/source URL. Unsupported routes are rejected. |
| `doi` | Reviewed DOI. |
| `sha256`, `size`, `pages` | Exact original-byte digest, byte count and parsed PDF page count. |
| `binding` | Existing `OriginalCache` binding: deterministic source filename, matching hash/size, institution scope, MinerU endpoint/options and their canonical digest. |
| `verification` | Exactly `method` (`official_browser_download` or `official_https_download`, reflecting the actual acquisition), `review: approved`, `receipt_sha256`, and a timezone-aware `reviewed_at`. |

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

The IEO route is specifically the fiscal-policy evaluation's observed
`Follow-up by IMF` implementation-plan PDF (`fp-mip.pdf`). Its exact frozen IMF
source identity remains required. An official alternative edition must be reviewed
for identity and completeness; accepting it does not claim byte equality with a
different official edition or infer equality from page counts.

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
