# WeChat generation and recovery

The source fetch, WeChat draft creation, and public website release are separate
stages. A successful upload must include a successful `draft/get` readback of
the expected article count, titles, and editorial footer. Draft creation does
not submit an article for publication unless the existing `publish` input is
explicitly enabled.

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

## Recover source and website updates

BIS uses the official research feed and supports both the current publication
pages and legacy report URLs. The resolver accepts the main report PDF and
preserves numbered-series identities used by existing seen-state records.
Leave `force_reprocess=false` for ordinary recovery.

For a failed website release, dispatch `neutral-edge-cutover.yml` on current
`main` with `operation=migrate` and `translation_scope=incremental`. The publisher
limits unchanged-object HEAD checks independently of uploads and retries bounded
transient failures. Verify the live article dates and pages after cutover.

**WeChat pipeline regression** checks the source resolver, UTF-8 transport,
verification failures, receipt recovery, deletion handling, diagnostic workflow
contracts, content exclusions, and static publisher behavior on relevant changes.
