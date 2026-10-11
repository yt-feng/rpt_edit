# WeChat generation and recovery

Last reviewed: 2026-10-11.

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

## Institution discovery and consulting figure diagnostics

Institution search feeds may advertise a future publication date or an explicit
`Coming Soon:` launch title before its PDF exists. These entries are recorded as
`publication_pending`, excluded from current download-failure counts, and kept
out of the seen state so the next scheduled run can reconsider them. A changed
release date/title is not a completed download. An actual required-source 403
or unresolved released PDF remains a visible source-health failure; deferral
does not assert that blocked IMF downloads are working.

Consulting uses the same immutable, source-bound MinerU result cache as the
institution route for the normal `vlm/en/ocr=true` options. Cache identity
includes scope, original source name, complete PDF bytes, task lineage and
parsing options, so a consulting result cannot alias an institution or Dropbox
result. The existing complete-member and fresh task-state gates still apply;
changing or expiring a result URL does not require another provider submission
when its exact completed result has already been saved. Unsupported options
retain their previous uncached route.

`consulting-mineru-figure-probe.yml` diagnoses one existing admitted result
without consuming failed-run artifacts. It authenticates the completed original
main run, its `fetch-and-build` job, actual checkout SHA, the complete logged
source inventory, and recorded batch keys. Its currently supported source
retrieval is the exact original `web-assets.bcg.com` PDF URL; downloaded bytes
must match the existing ledger's SHA-256 and size before inspecting a result.
The selected root must still be complete. It reads a matching result cache or,
if absent, downloads that already-completed provider result once, then emits
only bounded geometry, pixel-difference counts and binding hashes. It performs
no provider submissions, model calls, ledger/cache writes, article generation,
draft updates or publication. A diagnostic result is not a production figure
acceptance and cannot relax the original figure pixel/source checks.

## Institution source health and accepted backlog recovery

The Institution fetcher reserves exit `2` for a completed discovery run that
downloaded zero PDFs while a required source was unhealthy. The workflow passes
both the fetcher's exit status and `tee`'s exit status to
`institution_source_health.py`. The helper validates the complete manifest,
requested institution inventory, run date, source status, trusted required-source
flags and per-source download counts. Only this exact known failure may continue
to the existing private Institution backlog consumer. Unknown exits, incomplete
manifests and log-write failures stop the build. The helper performs no source
requests and changes no seen-state, source cache or dependency holds.

The separate `source-health` job fails visibly whenever a checked required source
remains unhealthy. WeChat upload and handoff cleanup depend on accepted generation
and delivery results, independently of that health job; recovered private sources
can therefore reach WeChat even during an unrelated discovery outage. Failure
notification includes the source-health result. This does not resolve a source's
HTTP 403 or label zero new PDFs as a healthy no-update result.

The consulting figure probe now classifies failed GitHub reads by fixed operation
(`run_metadata`, `job_metadata`, `job_logs`) and HTTP status, authentication error
or `network_stop`. It never emits the CLI error response, signed URL or private
body, and never retries or changes transport. This distinction must be available
before diagnosing a failed cloud probe as a permission or connectivity problem.
For `gh` 2.97+ compatibility, the probe detects local CLI support and uses
`--allow-escape-sequences` only for job-log bytes captured into a pipe, never
terminal output; exact-byte hashing and source authentication remain unchanged.
The classified probe initially stopped at GitHub job-log reading; the later
successful probe below establishes the pixel diagnosis separately from production
acceptance.

### Consulting catalog color-profile diagnosis

The admitted-source probe `38119748871` completed after the CLI compatibility
repair. It authenticated the original 20-page PDF and existing provider result,
with zero new provider submissions, model calls or cache writes. Repeating
MinerU's whole-document PDFium import/save produced exactly the provider's page
pixels. Compared with the admitted original, the first selected page had
49.60944% changed pixels, with a maximum channel difference of 17; geometry,
text, content streams, drawings, fonts and display-operation diagnostics agreed.
The original catalog contains `OutputIntents`, while the provider copy omits it.
Optional-content restoration was not applicable. Source PDF SHA-256:
`498dcdbfc5b65076fbfb54a0da1fa5a6a4b2265d99bfd9c0adc3f70b53dca176`.
Provider embedded PDF SHA-256:
`1fcd2966e9fab237dcf9082aaeba51eb773de39fbc08aff6f879e94fb73e574b`.

Follow-up probe `38120439688` completed successfully: restoring only the
authenticated original catalog's `OutputIntents` into an in-memory provider
copy passed the full 20-page drawing graph (158 objects and 80 streams). All six
selected pages, zero-based indices `0, 6, 7, 8, 9, 10`, had equal geometry and
exactly equal 300-dpi RGB pixels: zero changed pixels and zero channel delta.
Graph receipt SHA-256:
`8bde1232509aad4318f4da2e59c03410a96ca8abffb26518b4fba6655615a7f1`.
The original and cached provider bytes were not modified. The historical report
is diagnostic evidence, not evidence that it should be published as a new report.

`mineru_pdf_output_intents.py` uses this same catalog-copy operation for source
figure recovery. It requires both admitted PDF hashes, a missing provider color
configuration, and a complete original-to-restored drawing graph including the
ICC stream. Existing provider configurations and combined optional-content
configurations are not overwritten. `mineru_figure_sources.py` then checks exact
geometry and RGB equality for every selected page, including previously carried
pages if restoration first becomes necessary later in the report. Published
figures remain lossless crops of the authenticated original. Neither PDF nor its
result cache is replaced by the temporary restored document.

The v2 figure receipt admits only the existing optional-content policy or the
explicit `authenticated-outputintents-restoration-v1` policy, with bound original,
provider, restored-document and profile hashes, the drawing-graph receipt and
the complete verified-page list. Unknown policies or altered source/page fields
reject. Self-created ICC fixtures exercise actual PDFium profile loss, later-page
restoration, strict source-crop replay and rejection of changed text, drawings,
resources, pixels, existing profiles and tampered receipts. The diagnostic still
reports a graph rejection separately even if pixels agree; this cannot grant
production acceptance. Article generation and WeChat delivery are separate
acceptance steps and are not performed by this historical-source probe.

The consulting probe additionally runs the real `create_chart_source_assets`
producer with Consulting's normal eight-image limit and the real
`validate_figure_sources` consumer against the same already authenticated PDF
and completed-result ZIP. In a disposable private report it reproduces the
normal Markdown normalization, status/sidecar binding and source-image mapping.
After the first validation it removes only that temporary raw extraction and
runs the consumer again, proving that the retained page carriers and source
figures survive the normal private-handoff shape. The probe exports only counts,
hashes, policy names and fixed results in `production_figure_consumer`; no source
text, paths, images or PDF bytes are exported, and no additional network, model,
submission or external-cache operations are performed. A verified producer plus
raw-free consumer replay is source-figure acceptance only, not a new article or
WeChat delivery. The probe's successful exit means diagnostic completion;
acceptance requires `production_figure_consumer.status=verified` and both
`production_consumer_verified` and `private_handoff_replay_verified` to be true.

Formal-consumer probe `38121492186` completed but rejected the same source with
`figure_source_pixels_mismatch`; the catalog diagnostic identified the narrower
cause `output_intent_encrypted`. The production helper had incorrectly treated
pypdf's `is_encrypted` as requiring a password. That flag remains true for a
permission-protected PDF which opens normally with an empty password; MuPDF had
reported the admitted original as already readable, and the earlier diagnostic
had already copied its catalog successfully. The helper now explicitly permits
only successful empty-password access for either input. Documents requiring a
nonempty password still reject; it never requests a password or changes either
input. Synthetic permission-protected inputs cover this library distinction,
strict graph/pixel checks and both real consumer validations. The admitted source,
profile and exact-pixel requirements remain unchanged.

After PR #352, formal-consumer probe run `38121962962`
verified the same admitted source and completed-result ZIP on main
`e97b3eabedc0d970e6bc9287eae97180b3565e1a`. Its canonical read-only evidence is
`consulting-figure-probe.json` in successful artifact
`consulting-figure-probe-38121962962`; the sanitized completed-job log matches it.
`production_figure_consumer.status=verified` and both verification flags are true:
all 6/6 selected pages and original-PDF crops passed strict RGB and full drawing
graph checks, the real status/sidecar consumer accepted all six references, and
the second validation passed after deleting only the temporary raw extraction.
Original PDF and ZIP hashes stayed unchanged; provider submissions, model calls,
canonical-ledger writes and cache writes were all zero. This accepts the source
figure chain, not a complete new article or WeChat delivery. The historical 2014
source was used only for verification and was not published as a new report.

## BCG discovery evidence boundaries

BCG sitemap `lastmod` is page modification time, so a refreshed page does not
prove a newly published report. A BCG-owned `/publications/YYYY/` URL with an
explicit year earlier than the `since_days` window's starting year is skipped as
`publication_year_before_window` and remains unseen. Current-year paths, missing
URL years and old years mentioned only in article text are not rejected by this
guard. It does not infer a publication month/day or restore exact publication-date
extraction; the sitemap's legacy date field must not be treated as that evidence.

BCG PDF selection permits only its own archive-confirmed download hosts
(`web-assets.bcg.com`, `media-publications.bcg.com`, `www.bcg.com` and the official
apex). If a page offers only PDFs on external hosts, such as a cited company's
results deck, it remains unseen with `main_pdf_missing`; the external file cannot
stand in for the BCG report. An ordinary page with no PDF candidates retains its
existing no-PDF handling. Other institutions' cross-domain download rules are
unchanged. A future legitimately coauthored report hosted elsewhere needs separate
source-binding evidence before that host can be admitted.

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

The completed Daily and standalone recovery publications also enter a durable
locale-source event queue before the single source writer lock. Admission
checks exact run/attempt and nested-job identities, archive ancestry and the
live canonical/body receipt; it does not regenerate articles or reupload
accepted drafts. See [durable publication ingress](extended-locale-publication-ingress.md).
A real eligible Daily nested event still needs its own admission receipt;
implementation and regression coverage are not that receipt.

SEO multilingual prose-number differences are advisory under the
[quantity policy](financial-quantity-translation.md). This does not change
original Chinese article/title source evidence, draft readback, required HTML
structure, source identity or exact publication receipts. A publishable legacy
numeric-only fallback is not relabeled a fully translated article.

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
and unchanged-package replay. Later source and article acceptance are recorded
below; that inspection alone did not establish either.

Production recovery `38049925018` subsequently verified the pinned checkpoint
download but stopped at `summary_submission_pending`, reporting zero OCR and
provider calls. This is an unresolved Market Views summary, not proof of a
missing original page cache. The pages-mode contract has local regressions for
44 real PDF fixtures, 88 pages, full article generation/replay, strict missing
page/hash/method/identity failures and the private-PDF boundary.

The subsequent pages-mode run `38053057754` accepted all 44 reports in source
job `114215930086`, with verified private archive and zero OCR/provider calls.
Its `deliver / generate` job `114216146082` then exited 2; saving generation
progress succeeded. This established the historical page-source handoff. Article
generation and draft readback were subsequently accepted through the retained
revalidation and delivery receipts below; public Blog acceptance has a separate
release-bound record.

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

### 261007 OCR source, generation and draft receipts

PR #335 merged at `30169f6` after seven successful cloud checks. Real read-only
inspect run `38062695853`, job `114244017112`, then returned
`revalidation_ready=true`, 44 completed articles after revalidation, 43 unchanged
articles, zero provider POSTs and zero object writes. Apply run `38062813064`,
job `114244354526`, returned `applied=true` with the same 44/43 counts and zero
provider POSTs. Its two private object writes (generation checkpoint and complete
article handoff) were verified. Both operations bind proof SHA-256
`26e499e12ec01b4ca2bb1c168489f9929fc9c055e6cd97accaf6d2b44d3eda9d`.

The selected title came from saved response 4, candidate 3. Complete numeric-atom
truncation produced 34 characters, removed one whole quantity and introduced no
changed/partial quantity. The original title-hook gates passed; the optional
original-source semantic-support route did not rescue this batch. The existing
body, four saved title responses, all Progress bytes, private source and other
43 bound articles were preserved. See
[original-source title support](title-original-source-claims.md#production-revalidation-receipt)
for the exact retained-response boundary.

Standalone delivery run `38062937361`, job `114244980478`, completed its private
WeChat draft readback: `article_count=44`, `draft_count=6`,
`source_report_count=44`, `excluded=0`, `accounted=44`. Blog archive commit
`a1dec872d156e505094e77bd4df582a95b02db5e` is recorded. The successful deliver
job produced request artifact `11674476878`, with 44 unique fingerprints and
only canonical slugs/body/title hashes. Its request SHA-256 is
`e9a0235e0044d50bb711896caa981d61e10fcf653edca22815274c9b94e89eae`.
The request has been schema-validated and is not itself a live Blog receipt.

Production release run: `38072861358`; immutable release:
`a7fc76874f6643ccc275778311837bcd`. Cutover succeeded at 2026-10-10 19:42:50 UTC.
New 44-article live acceptance passed at 2026-10-10 19:44:13 UTC: every
canonical and complete normalized body/reference hash matched, and edge
release/tree identity stayed unchanged around readback. Receipt SHA-256:
`085399b6aa2ade200cd7c731d063bffd7f53ee76b114b2d6217912876522ea42`.
The earlier 118 articles also passed a fresh full readback on this same release
at 2026-10-10 19:46:02 UTC, with all canonical/body/reference hashes matching and
unchanged edge identity. New 118-article receipt SHA-256:
`4d5a67b9957007c90f6d563eba6feebb35d5154f8234e4cbbd2f5c5989bba10e`.
The two release-bound receipts together verify 162/162 live articles; accepted
drafts total 22 groups. Both checks made zero provider calls and zero production
writes. The original standalone run `38062937361` and publish job
`114251477079` completed successfully, without a rerun or duplicate draft upload.
The original source, generation, draft and archive identities remain preserved;
publication recovery does not repeat generation or WeChat upload.

The same standalone run's exact attempt-1 publication event was captured and
frozen, then admitted by source-admission run `38080940054` at
2026-10-10 19:46:24 UTC: captured/checked/admitted events were each 1,
blocked/retained events and paid-provider requests were each 0. Its resulting
current-main consumer `38081129295` was pending with zero jobs at
2026-10-10 19:48 UTC, while active translation work was retained. This verifies
standalone OCR publication admission and queue handoff, not complete multilingual
publication or a real Daily nested-event admission.

### Previously accepted delivery cohorts

The previously accepted 2026-10-10 Chinese snapshot contains 118 articles in
16 WeChat draft groups:

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

That historical snapshot establishes normal and recovered MinerU delivery for
those three cohorts. The separate 261007 section above records OCR source,
generation and draft receipts, and tracks public-release acceptance separately.
Neither receipt proves every earlier October source cohort or publication in
every supported locale.
A successful MinerU batch is never forced onto OCR just to obtain a fallback
receipt. Audit earlier dates against their selected manifests and accepted
draft/archive identities before claiming historical completion.

**WeChat pipeline regression** checks the source resolver, UTF-8 transport,
verification failures, receipt recovery, deletion handling, diagnostic workflow
contracts, content exclusions, and static publisher behavior on relevant changes.
