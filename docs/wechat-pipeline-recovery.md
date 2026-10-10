# WeChat generation and recovery

Last reviewed: 2026-10-10.

The source fetch, WeChat draft creation, and public website release are separate
stages. A successful upload must include a successful `draft/get` readback of
the expected article count, titles, and editorial footer. Draft creation does
not submit an article for publication unless the existing `publish` input is
explicitly enabled.

## Source selection and shared consumers

`dropbox-latest-pdf-to-xhs-sharded.yml` freezes the selected original-PDF
manifest before processing. The normal source order is:

1. Generate articles from the primary MinerU shards. `source-outcome` checks
   actual shard outcomes and complete private handoffs; a green matrix job by
   itself is insufficient.
2. If primary delivery is incomplete, `recover_daily_mineru_sources.py` resumes
   the accepted MinerU tasks and durable result caches. Full-PDF segmentation
   retains original-file, page-range, text and figure identities.
3. Only after that recovery attempt fails does the ordinary run enable the
   complete cloud OCR branch. Frozen replay has a separate provider-proven,
   no-new-submission route; replay is not an instruction to resubmit MinerU.

Both `mineru-recovery` and `ocr-synthesis` feed the reusable
`recover-report-article-delivery.yml`. This is shared article delivery, not a
PDF-only fallback. `recover_report_articles.py` authenticates the original run,
execution SHA, handoff run/SHA, date, selected count, manifest and file hashes.
MinerU consumes the verified `source_mineru.md`, including recovered segments.
OCR consumes every bound `ocr_sources/<id>/pages.json` page as `source_ocr.md`;
it does not substitute the cross-report summary for original page text. Missing
reports, altered page order/text, or inconsistent provenance stop generation.
OCR-reconstructed figures retain their own source-page and byte identities and
are never labeled as MinerU figures.

| Consumer | Primary source | Recovered source |
| --- | --- | --- |
| Chinese report articles | Complete original article shards | Complete source-bound article handoff |
| WeChat drafts and Blog archive | `push-xhs-notes-wechat-drafts` | Reusable recovery workflow's `deliver` job |
| Portal translated reports | Original shard prefix | `article_handoff_prefix` from verified recovery |
| Market Views PDF | Complete primary shards | Independently verified MinerU or OCR source edition |
| Chart index | Original handoff | Verified MinerU recovery; OCR figures are not silently promoted |

`validate-report-delivery` requires the configured article and translation
consumers to succeed. A successful Market Views PDF cannot satisfy this gate.
Recovery source cleanup waits for the PDF and configured article consumers;
the source-bound article checkpoint remains available independently.

## Verify an existing upload

Run **Verify existing WeChat drafts** with the original upload run ID and its
exact diagnostic artifact name. The job reads the archived summary and payloads,
then calls `draft/get` for each recorded ID using UTF-8 JSON decoding. It creates,
deletes, and publishes no articles. Its output artifact reports the expected and
verified article counts and fails the job if any draft does not match.

The source date folder is not necessarily the creation date: a run processing
the previous day's input can create drafts after midnight. Use the upload run
time and the draft readback timestamps when checking a day's output.

## Retry a failed upload

Accepted draft IDs are checkpointed before readback and retained even when
verification fails. All upload jobs archive diagnostics on failure; rerunning
the same GitHub run restores those receipts before uploading. Existing accepted
groups are reused, including groups split after a size rejection. An explicit
successful deletion removes that ID from the reusable receipt. Failed deletions
retain their IDs.

A failed or malformed remote duplicate lookup must stop creation. If a previous
diagnostic artifact has expired, first reconcile the existing WeChat drafts.

Recovered delivery additionally persists generation progress and accepted draft
receipts under the original run/date/manifest identity in private R2. It records
an accepted draft before the next request, reconciles an ambiguous `draft/add`,
and reuses matching receipts across recovery runs. A changed source, body or
group identity must not inherit an old acceptance. Do not regenerate or upload
already accepted articles simply because the later website release failed.

Generation must account for every selected report. The upload receipt partitions
that count into accepted articles and explicit title-policy exclusions. A body
generation failure cannot be relabeled as a title exclusion. Recovery requires
`publish=false`, exact article/group coverage and successful title/count/footer
readback before Blog archival; it does not invoke WeChat free publication.

## Recover source and website updates

BIS uses the official research feed and supports both the current publication
pages and legacy report URLs. The resolver accepts the main report PDF and
preserves numbered-series identities used by existing seen-state records.
Leave `force_reprocess=false` for ordinary recovery.

For a failed website release, dispatch `neutral-edge-cutover.yml` on current
`main` with `operation=migrate` and `translation_scope=incremental`. The publisher
limits unchanged-object HEAD checks independently of uploads and retries bounded
transient failures. Verify the live article dates and pages after cutover.

For article recovery, use the exact original Daily run, source handoff run,
source kind, date and expected selected count. First inspect existing private
source and article receipts. If a completed source handoff has been cleaned up,
inspect its durable MinerU result or source-bound OCR cache; an old successful
job does not prove the temporary handoff still exists. Never substitute a
different run's sources based only on date or count.

The reusable recovery workflow saves an immutable publication request after
committing the sanitized Blog archive. `watch_recovered_article_publication.py`
follows only a same-repository main release containing that archive commit,
persists its selected run, and checks each live canonical URL plus the complete
normalized body and references. A superseded pending release can be followed
without repeating generation or draft upload. A normal primary upload also
requests an incremental public refresh; that dispatch alone is not live Blog
acceptance.

## Acceptance ledger

Keep these receipts separate: original manifest, source extraction, generated
articles, draft readback, committed Blog archive, and live publication. Each
must be bound to the preceding exact identity. See
[Blog output contract](blog-seo-wechat-output.md) for publication and body
identity, and the locale architecture documents for multilingual publication.

The 2026-10-10 accepted Chinese snapshot contains:

| Original source date | Selected sources | Accepted draft articles | Draft groups | Explicit exclusions |
| --- | ---: | ---: | ---: | ---: |
| 261004 | 4 | 4 | 1 | 0 |
| 261008 | 40 | 38 | 5 | 2 |
| 261009 | 79 | 76 | 10 | 3 |

The recovered 261008 source run `37890955977` validated 40/40 PDFs, including a
202-page source assembled from two ranges, with zero new provider submissions.
The final public release run `38036944110` then passed independent live checks
for all 118 articles: HTTP 200, canonical identity, full body/reference digest,
and unchanged edge identity before and after the readback. Its acceptance
receipt SHA-256 is
`2d48c5caa7105d8854295888bec7af60c483919b1a8c6c7f27fe79a1eeef32c9`.

This snapshot establishes normal and recovered MinerU delivery for those three
cohorts. It does not establish a real OCR-to-draft-to-Blog production receipt,
every earlier October source cohort, or publication in every supported locale.
OCR has source-binding and consumer regression coverage, but its production
acceptance must use a real eligible retained OCR receipt without forcing a
successful MinerU batch onto the fallback path. Audit earlier dates against
their selected manifests and accepted draft/archive identities before claiming
historical completion.

**WeChat pipeline regression** checks the source resolver, UTF-8 transport,
verification failures, receipt recovery, deletion handling, diagnostic workflow
contracts, content exclusions, and static publisher behavior on relevant changes.
