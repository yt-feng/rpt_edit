# Chart Search Architecture

Last updated: 2026-08-29

## Goal

Make the charts already extracted from reports searchable by facts such as company,
metric, period, geography, unit, and visible trend. The pipeline uses an
OpenAI-compatible multimodal endpoint to turn each selected MinerU chart into a
small structured description. Report PDFs and raw extraction folders remain private.

## Daily Incremental Flow

```mermaid
flowchart LR
  M["MinerU report folders"] --> C["Selected source_image files"]
  C --> H["SHA-256 content hash"]
  H -->|"known hash"| S["Reuse checkpoint"]
  H -->|"new hash"| V["Multimodal description"]
  V --> S
  S --> I["Report-level chart index"]
  C --> A["Immutable chart image by opaque hash"]
  I --> R["Private object storage"]
  A --> R
  R --> B["Static release build"]
  B --> Q["Normal search + lazy chart-search data"]
  B --> G["Public Charts gallery"]
  G --> P["Opaque image API"]
  P --> A
```

The daily PDF workflow dispatches `portal-chart-search-index.yml` before deleting
its short-lived private shard handoff. The chart workflow downloads those shards,
loads the previous checkpoint and index from private object storage, processes only
unknown content hashes, and publishes the new index. The parent captures the exact run
ID returned by `workflow dispatch` and waits for that ID before cleanup; display titles
are not used for child correlation because repeated recovery runs intentionally share a
title. The R2 index and immutable images are the durable derived assets; the short-lived
handoff and GitHub summary artifacts are only transport and diagnostics. The regular edge
refresh then:

1. downloads the latest chart index;
2. merges report-level chart text into `data/search_index.json`;
3. publishes `data/chart_search_index.json` for a chart-specific search view.

The static release also publishes `charts.html`, `assets/charts.js`, and
`assets/charts.css`. The page flattens only valid chart records, supports
company/metric/period/geography/unit/trend search, filters by chart type and date,
and links each result back to `report.html?id=<report_id>`. It never embeds the
private R2 object key.

If chart search is temporarily disabled, the document and publishing workflows keep
working. Enable the daily dispatch with repository variable
`CHART_SEARCH_ENABLED=true` after the private API configuration is present.

## Valid-chart Gate

`is_chart=true` by itself is not sufficient for publication. Analysis version
`chart-search-v2` asks the vision model for:

- `content_kind`: chart, data table, data map, flow diagram, other data visual,
  or invalid;
- `quality_score`: 0–100;
- `has_data_evidence`: visible quantitative or structural evidence;
- `invalid_reason`: a bounded reason code for rejected images.

The deterministic publisher requires an allowed content kind, score of at least
60, visible data/relationship evidence, a title and description, and at least one
structured metric/entity/period/geography/unit field. It rejects cover/title
pages, tables of contents, author or analyst biographies, contact pages,
disclaimers and legal notices, references, pure-text blocks, end pages, decorative
images, photos, and unreadable crops.

The analysis-version change intentionally re-examines old hashes when they are
encountered again. A successful reanalysis replaces the same deterministic chart ID.
If reanalysis fails, is deferred, or no longer passes the publication gate, the last
successfully published record remains available; an incomplete retry cannot erase a
durable Chart asset.

## Model Configuration

The public repository contains no endpoint or credential. Actions reads:

| Setting | Type | Purpose |
| --- | --- | --- |
| `VISION_INDEX_API_KEY` | GitHub Actions secret | API bearer credential. |
| `VISION_INDEX_API_BASE_URL` | GitHub Actions secret | Credential-free HTTPS OpenAI-compatible base URL. |
| `VISION_INDEX_MODEL` | Repository variable | Model name; defaults to `qwen3-vl-flash`. |
| `VISION_INDEX_MAX_IMAGES_PER_RUN` | Repository variable | Whole-run ceiling for new API calls; defaults to `0` so no selected daily chart is silently dropped. |
| `VISION_INDEX_MAX_PER_REPORT` | Repository variable | Per-report image ceiling; defaults to `0` so every retained MinerU image is examined. |
| `VISION_INDEX_MIN_INTERVAL_SECONDS` | Repository variable | Minimum delay between requests; defaults to 0.4 seconds. |
| `VISION_INDEX_CHECKPOINT_BATCH_SIZE` | Repository variable | Maximum calls between private R2 state uploads; defaults to 20. |

The client rejects non-HTTPS bases, embedded URL credentials, query strings, and
fragments. Authentication/configuration failures such as HTTP 401/403 stop the run
immediately. Throttling, server failures, network timeouts, and malformed server/model
JSON remain retryable and can never quarantine an image. Logs and private checkpoints
store only bounded, provider-neutral reason codes (for example `transport`,
`http_transient`, or `model_json`), never response bodies, request endpoints, or model
output.

## Incremental, Deduplication, and Resume Rules

- The SHA-256 of the extracted source image is the model-cache key.
- A successful description, including `is_chart=false`, is reused on later runs.
- Duplicate images across reports cause one model call but can create multiple report
  associations.
- Every run is append-only across dates and within the same date. Its candidate set may
  be a partial handoff: reports and charts absent from the new input remain in the
  previously published index. A successful description overwrites only its own stable
  report/chart ID, so repeated runs remain idempotent without treating a recent input as
  a complete historical inventory.
- A report first seen before catalog matching uses a date/title-derived temporary
  `report_ref`. Once a non-empty catalog `report_id` becomes available, final
  normalization collapses the temporary and canonical refs into one report. Charts are
  deduplicated by immutable `image_id` and chart ID while every other unique historical
  image remains attached to the canonical report.
- Each success or failure is atomically checkpointed locally. The workflow limits
  each model batch to 20 calls by default and uploads the private R2 state after
  every batch, so a runner timeout loses at most the active batch rather than the
  whole day.
- Failed images receive a bounded next-retry timestamp; they do not discard successful
  descriptions from the same run. Three consecutive transient failures across images
  open a circuit breaker. The workflow uploads the private state before exiting, so a
  service-wide outage does not spend calls across the full input set.
- Manual recovery can set `retry_errors_now=true` to bypass only the checkpoint's
  next-retry timestamp. It does not bypass per-request retries, the circuit breaker,
  configuration validation, failure classification, or the complete-index publish gate.
- `max_images` counts only new model calls. Cache hits are unlimited, so a backfill can
  relink already-described charts without consuming its call budget.
- The daily job makes as many calls as needed by default. Only deterministic single-image
  failures (local decode/input failures or an explicit image-content 4xx response) count
  toward quarantine, at most once per workflow execution. A hash that has the same stable
  image failure in three separate workflow runs is quarantined in the private state;
  transient failures remain retryable forever. Successful charts and the public index
  continue to publish. A manual
  historical backfill can revisit the retained source artifact if the quarantined
  image later needs another parser/model attempt.
- Immutable images are uploaded by hash before the index that references them.
- Cleanup is off by default. Every publish still applies schema hygiene to the public
  index: only `chart-search-v2` records with valid image IDs remain, and every matching
  immutable image present in the current asset handoff is uploaded. With cleanup off,
  the publisher does not evict images, delete objects, list the prefix for a budget
  check, or remove otherwise-valid v2 records to meet a storage ceiling.
- Repository variable `CHART_CLEANUP_ENABLED=true` explicitly opts a workflow run into
  cleanup. Only in that mode does `CHART_STORAGE_BUDGET_BYTES` apply; it defaults to
  100 GiB (`107,374,182,400` bytes) and includes state, index, and images. Production
  keeps cleanup disabled; 100 GiB is the future capacity-review threshold, not an active
  retention window.
- Cleanup mode deletes objects not referenced by the live index first. If referenced
  images still exceed the remaining budget, the publisher keeps images with the most
  recent report-reference date; R2 `LastModified` is the tie-breaker. Any evicted image
  is removed from the index in the same operation, report/chart counts and search text
  are recomputed, and a final prefix-size check enforces the configured ceiling.
- A non-zero `max_images` is an explicit whole-run ceiling. If the ceiling leaves unknown
  hashes, the child run fails after uploading its private checkpoint; the parent therefore
  retains the private source handoff for a later continuation instead of deleting it.
- Any remaining transient or not-yet-quarantined stable image failure follows the same
  fail-after-private-checkpoint rule. Only a complete run (successful hashes plus any
  hashes already quarantined after three separate executions) lets the parent remove the
  source handoff and publish the updated public index.

## Public Data Contract

`data/chart_search_index.json` has schema version 1:

```json
{
  "schema_version": 1,
  "updated_at_bjt": "ISO-8601 timestamp",
  "report_count": 1,
  "item_count": 2,
  "reports": [
    {
      "report_ref": "opaque stable reference",
      "report_id": "catalog report id",
      "title": "report title",
      "date_folder": "YYMMDD",
      "chart_count": 2,
      "search_text": "bounded combined chart terms",
      "charts": [
        {
          "id": "opaque chart id",
          "image_id": "SHA-256 image id",
          "ordinal": 1,
          "analysis_version": "chart-search-v2",
          "title": "visible chart title",
          "content_kind": "chart",
          "quality_score": 92,
          "chart_type": "line",
          "description": "visible facts",
          "trend_summary": "visible trend",
          "metrics": [],
          "entities": [],
          "periods": [],
          "geographies": [],
          "units": [],
          "keywords": []
        }
      ]
    }
  ]
}
```

The frontend can return to the existing detail page with
`report.html?id=<report_id>`. The contract never contains a local source path, raw
handoff path, provider URL, API credential, or original storage key. `image_id` is an
opaque lookup id; the gateway should translate it to the private image object only
when rendering a result thumbnail.

The standalone Charts gallery admits only records whose
`analysis_version` is exactly `chart-search-v2`. Historical v1 text can remain in
the incremental private checkpoint for resume purposes, but it is not rendered in
the visual gallery. Backfilling a date re-analyzes those hashes under v2 and
publishes only records that pass the new gate.

The gallery expects this neutral gateway contract:

```text
GET /api/charts/image?id=<64-lowercase-hex-image-id>
```

The gateway must validate the identifier before constructing the fixed
`_chart-search/v1/images/<id>.jpg` key, return only `image/jpeg`, and may apply a
long immutable browser cache because the identifier is a content hash. A missing
object returns 404. The raw R2 key, bucket name, listing, and credentials never
reach the browser.

## Manual Backfill

Run **Portal chart search index** manually with:

- `date_folder`: historical `YYMMDD` folder;
- exactly one of `source_handoff_run_id` or `source_artifact_run_id`;
- `source_artifact_pattern` when the historical run used a different artifact name;
- `expected_shards`: expected count, or `0` to accept all found shards;
- `max_images`: desired ceiling for new calls.
- `retry_errors_now`: use only for an operator-triggered recovery when the retained
  handoff should retry error checkpoints before their normal backoff expires.

Repeat the same date/run with a higher ceiling if the summary reports deferred images.
Already completed hashes are skipped. Historical backfill requires a still-available
private handoff or Actions artifact containing `assets/source_image_*`; diagnostic-only
artifacts do not contain chart images. Process older dates in chronological batches so
each run persists its checkpoint before the next begins.

## Operational Verification

Each chart run uploads a small `summary.json` artifact with candidate, cache-hit,
model-call, failure, deferred, report, and chart counts. It intentionally excludes
model responses, images, source paths, and credentials. A healthy incremental run
normally shows mostly cache hits on a retry and only new hashes as model calls.
The publish log additionally reports uploaded/reused/evicted image counts, removed
index records, and whether cleanup was enabled. Stored bytes and the configured ceiling
are reported only in cleanup mode; the default non-cleanup mode marks both as unenforced.
