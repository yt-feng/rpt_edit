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

### Inspect an existing OCR checkpoint

Run **Inspect Market Views incident R2 caches**
(`market-views-r2-cache-inspect.yml`) on `main`. Fill all four inputs to inspect
one exact source cohort; leaving all inputs empty retains the October 1–3
incident inventory. For the retained 261007 cohort:

| Input | Exact value |
| --- | --- |
| `source_run_id` | `37695511597` |
| `date_folder` | `261007` |
| `expected_reports` | `44` |
| `manifest_sha256` | `d16c57d614166f46f244b4a9ae65ffecce774be8cb1a52f52cdf968574e4a961` |

The workflow authenticates the completed original Daily run on the same
repository's `main`, downloads `selected-macro-manifest-<source_run_id>` only,
and verifies the retained manifest's raw SHA-256, date, count and source
bindings. It derives the production OCR checkpoint key from those actual
bindings and checks the exact temporary source handoff at
`_private-workflow-handoff/market-ocr-synthesis/<source_run_id>/<date_folder>/shard_0.tar.gz`.
It makes one R2 `HEAD` per object, with no alternate-run discovery. It does not
download PDFs, read either archive, parse reports, call a model, or write/delete
R2 objects.

Check the `market-views-r2-cache-inventory-<inspection_run_id>` artifact:
`success=true` permits reading the independent `ocr_checkpoint` and
`ocr_source_handoff` presence results. The durable checkpoint may survive after
the temporary source handoff has been cleaned up. Each `present=true` establishes
presence and stored size/hash metadata only. `archive_bytes_verified` remains `false`; this is
neither archive integrity/completeness nor article, draft or Blog delivery
acceptance. A verified absence reports `present=false`; a missing source
artifact, mismatched manifest, permission error or transport failure stops the
check and must not be treated as an absent cache or an instruction to regenerate.

### Restore OCR sources after the temporary handoff expires

Use **Recover historical OCR sources from verified cache only**
([`recover-ocr-cache-sources.yml`](../.github/workflows/recover-ocr-cache-sources.yml))
on `main` when the exact durable checkpoint is present but the original complete
source handoff is absent. The recovery also requires the original
`selected-macro-pdfs-<source_run_id>` artifact, including its selected manifest
and every original PDF. The lightweight manifest alone cannot supply those PDFs.

Pass the four exact source inputs from the inspection above, plus
`archive_sha256` and `archive_size_bytes` from that checkpoint's inspection
receipt. The producer verifies the downloaded archive bytes against both pins;
the inspector's stored metadata is not sufficient. It verifies original PDF
hashes, manifest bindings and complete cached page/chunk/model-prompt identities
before rebuilding the default `source_mode=synthesis` package. Source reconstruction performs no OCR,
MinerU or model calls. Missing, corrupt, mismatched or unresolved cache entries
stop recovery instead of silently enabling a new processing request.

The receipt retains the original Daily `source_run_id` and execution SHA. Its
separate `cache_recovery` envelope binds the actual recovery run/SHA, fixed
workflow, original manifest hash, derived checkpoint identity and pinned archive
size/hash. The package is written only to
`_private-workflow-handoff/market-ocr-cache-recovery/<recovery_run_id>/<date_folder>/shard_0.tar.gz`.
It does not replace the old Daily namespace or claim to have run as that Daily.
Consumers require the exact main/manual producer and both successful source
reconstruction and archive-readback gates before reading this new handoff.
Ordinary same-run Daily OCR receipts keep their existing path and contract.

For new scheduled Daily runs, the same page-only contract is automatic when
MinerU recovery actually failed and OCR was attempted but full synthesis did
not produce an archived article source. The always-run outcome step exports
`mineru_recovery_failed`, `ocr_attempted`, and `article_source_ready` using step
outcomes. The separate `recover-ocr-page-sources` job rejects replay runs and
primary-ready/zero-source cases, uses the current run's PDF artifact, and
verifies the exact private durable-cache archive before checking all pages.
No additional OCR or synthesis requests are made.

This same-run source uses `daily_cache_origin` instead of historical
`cache_recovery`. It binds the Daily run ID/SHA, selected manifest, checkpoint
identity and archive SHA/bytes in
`_private-workflow-handoff/market-ocr-pages-daily/<run_id>/<date_folder>/shard_0.tar.gz`.
Source consumers require the exact failed upstream recovery job and successful
page verification/archive gates, then route through the same article delivery,
WeChat draft readback, public Blog and configured translation workflow. The
original PDFs remain only in the private validated source package. Reruns reuse
that source receipt byte-for-byte; missing/partial pages fail before any model
call. The two origin envelopes are mutually exclusive and cannot be exchanged.
The old summary pending marker remains untouched, and Market Views PDF delivery
is still checked independently. The automatic route needs production acceptance
on an eligible Daily; local tests alone do not establish delivery.

`source_mode=pages` is an independent recovery contract for article generation
when every original page is cached but a Market Views summary is missing or its
submission outcome is unknown. It does not call the synthesis builder, OCR,
MinerU or a model, and does not interpret, clear or resubmit summary/final
pending records. It requires every selected PDF's exact manifest/SHA, actual
PDF page count, production extraction-cache key and full ordered page evidence:
text SHA, allowed extraction method, consistent empty flag and at least one
nonempty page per report. All reports pass before any source handoff is written.

The independent `ocr_pages_receipt.json` has `source_kind=ocr-pages`; it contains
no summarized-report claim, synthesized sections or reconstructed charts. Its
private namespace is
`_private-workflow-handoff/market-ocr-pages-cache-recovery/<recovery_run_id>/<date_folder>/shard_0.tar.gz`.
Two separate successful pages-mode step gates, the exact producer/run/SHA and
the strict pages receipt are all required by consumers. Synthesis-only gates
cannot authorize this source kind, and this receipt cannot be used by the
Market Views synthesized-PDF publisher.

For independent downstream PDF SHA/page-count verification, this source
package has one narrow private-handoff exception: the exact receipt-bound
`originals/RNNN.pdf` inventory may be included after the full pages receipt is
validated. It stays in the same private R2 bucket. The default archive filter
continues excluding original PDFs; there is no general include-PDF CLI input.
Article staging copies page evidence and full `source_ocr.md` only, marks
`image_source_kind=ocr_pages_text_only`, and supplies no fabricated figures.
Original PDFs are absent from article checkpoints and public Blog output.

Rerun the same GitHub recovery run to resume: an existing complete package is
downloaded, revalidated and reused with its receipt bytes unchanged; archival
readback verifies it instead of overwriting it. This preserves the generation
context and accepted-draft checkpoints. A different recovery run or changed
receipt cannot inherit an earlier context merely because the date/count match.
This same-run exact-byte reuse applies independently within each source mode;
changing mode never reuses the other mode's source namespace or article context.

`recover_articles=true` (the default) then invokes the existing article recovery
workflow with the original run and the new handoff run as separate inputs.
That later stage may generate missing articles from verified full page text,
then performs WeChat draft readback, Blog archival and public-body acceptance.
The source producer's zero-call guarantee does not mean article generation is
already complete. Use `recover_articles=false` for source reconstruction only.

Inspection run `38047483613` found the 261007 durable checkpoint present at
2,397,894 bytes, with stored SHA-256
`3a3cf282b6ea83f1b65368c364be027b3daa808c99a2d1fc31def54b289c9f73`,
and the original temporary source handoff absent. This establishes the reason
for the recovery path, not complete cache contents or delivery. Offline
consumer regressions cover full OCR page/figure use, dual identity rejection
and unchanged-package replay; the real 44-source reconstruction and subsequent
article, draft and Blog acceptance remain pending.

Production recovery `38049925018` subsequently verified the pinned checkpoint
download but stopped at `summary_submission_pending`, reporting zero OCR and
provider calls. This is an unresolved Market Views summary, not proof of a
missing original page cache. The pages-mode contract has local regressions for
44 real PDF fixtures, 88 pages, full article generation/replay, strict missing
page/hash/method/identity failures and the private-PDF boundary.

The subsequent pages-mode run `38053057754` accepted all 44 reports in source
job `114215930086`, with verified private archive and zero OCR/provider calls.
Its `deliver / generate` job `114216146082` then exited 2; saving generation
progress succeeded. This proves the historical page-source handoff, while
article generation, draft readback and public Blog acceptance remain incomplete.

### Inspect retained generation before recovery

`recovered-article-generation-inspect.yml` is a manual, main-only, read-only
incident diagnostic with no user-supplied scope. It pins original Daily
`37695511597`, recovery run `38053057754`, those two exact source/generation jobs,
date `261007`, 44 reports and the frozen manifest digest. REST must prove the
source gates succeeded, generation failed and private checkpoint saving
succeeded before the inspector reads the exact `generation.tar.gz` object.
This workflow does not call delivery `prepare`, acquire a claim, change pending
markers, write/delete R2 objects, generate articles or contact model providers.

The archive is bounded to 512 MiB compressed/expanded and 20,000 members;
checksums, duplicate paths, traversal, links and special files are rejected.
The saved context and embedded original-page receipt must match the exact
source/handoff identities. A completed-article count additionally requires the
saved OCR page bytes to match the receipt, reconstructed Markdown to match the
article source, and a valid editorial binding and recovery policy. A status file
or article filename by itself does not count as completed.

The private log remains private. The only artifact contains allowlisted failure
category, source ordinal, known exception types and fixed code sites, HTTP status,
generation phase, title-repair booleans, verified completed count, pending-marker
count and hashes. Unknown causes stay `unknown`; exception text, source filenames,
article bodies, titles, provider responses, paths, URLs and credentials are never
included. Existing provider request count/outcome stays explicitly unknown, so an
inspection is not permission to repeat an unresolved paid request. The next
recovery must use this saved diagnosis and verified completed articles; successful
inspection alone is not generation or delivery acceptance.

### Durable body and title continuation

Read-only diagnostic run `38055118845` completed successfully with zero provider
posts and zero object writes/deletions. It found 27 bound articles, followed by
`generated_article_unbound` at source ordinal 28. The rejected candidate categories
included `long_untranslated_english`, `english_heavy_fragment`, `anchor_coverage`
and `missing_anchor_segment`; required technical terms were empty. Its title repair returned
without an HTTP or exception failure, but `needs_model_repair=true` remained
while `selected_quality_issues` was empty. That combination is meaningful:
`evidence_or_emergency_fallback` requires further semantic evidence even when a
title passes surface-quality checks. Recovery must not clear the flag or promote
the old selected fallback into a purported model-returned candidate.

The reusable article workflow now supplies `--checkpoint-workspace` to enable
private durable stage progress. A request intent is archived and its size/hash
metadata verified before a model request. The returned body or title response is
then separately saved and archived before another request may start. Each request
uses one key, one HTTP attempt and no internal model fallback. Pending/ambiguous
requests remain pending across runner restoration and prevent resubmission;
changing the prompt or options cannot bypass them. Existing complete editorial
bindings still reuse the accepted article without any body or title call.

Progress binds source/handoff identities, manifest, source receipt, exact source
Markdown/provenance, generation implementation, prompt and model options. The
successful body is reused while title generation resumes from saved results.
Title proposals are bounded to four distinct new requests for an ordinary
article (initial proposal plus up to three repairs); the pinned historical
migration resumes from its actual saved raw candidates and permits up to three
new repairs. When long English company/product names caused rejection, repair explicitly uses
a Chinese name or short form supported by the evidence instead of copying the
rejected full English name; it cannot invent an alias or change the subject.
Every proposal passes the existing filename/required-term/coverage,
source-backed additions, neutral wording and quality gates. Rejected titles never
become accepted just because another attempt ran.

Historical ordinal 28 predates the body checkpoint. Its migration is restricted
to the independently inspected archive SHA
`5c94fdc2352fb0620f6fd60c208ea724874eeda23b9272cd39b2572d2e817a09`,
exact stored context, original generation contract and verified OCR source. It
requires the saved body, prompt, status and actual title-candidate history to
match that pinned failure. Arbitrary unbound or legacy partial outputs are not
adopted or silently regenerated. The migration saves an immutable private body
receipt before title work; the 27 complete articles are left byte-for-byte intact.

Stage receipts, raw model responses and legacy admission proof live alongside
`articles/` under the private generation checkpoint, never in the final article
handoff or publish-ready tree. A title failure or pending request lets independent
remaining reports finish and save their own progress, but no complete article
receipt or delivery job is admitted until every selected article binds. A failed
stage's empty pending-file glob does not establish that no request was submitted:
the authoritative pending state is inside its private progress receipt.

Offline regressions cover the 44-source pattern with 27 unchanged accepted
articles, the retained 28th body, exactly 16 new remaining bodies, zero-call full
replay, real semantic-emergency title gates, bounded repairs, persisted unknown
requests and exclusion of private progress from article handoffs. These tests do
not replace a real resumed generation, WeChat readback or public Blog receipt.

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
