# Neutral Runtime-Data Versioning

Last updated: 2026-08-31

## Why Neutral uses a staged enablement gate

Neutral is the release path that prepares a complete inactive static slot and
then changes the Edge Worker to serve that slot. It is useful because catalog,
search, report pages, Blog pages, sitemaps, and discovery files can move as one
verified release without overwriting the live static tree in place.

The former runtime-data path was not release-safe. The publisher copied
`catalog.json`, `search_index.json`, and `password_rules.json` into the shared
namespace `edge-static/runtime-data/` before the Edge switch. The Portal Worker
cached those shared objects for up to five minutes. If the new Edge release
failed verification and the Edge Worker rolled back, the shared runtime
objects did not roll back with it. The result could be an old page tree paired
with a new API catalog, search index, or password-rule set.

That incomplete rollback boundary was why Neutral was hard-paused. The release
path now separates preparation from cutover, validates the candidate through
the live Edge and Portal runtime, and restores the exact prior Worker version
and release state after a failed acceptance or a rehearsal. Automatic events
remain behind the repository variable `NEUTRAL_SCHEDULE_ENABLED`; a workflow
change alone cannot start a scheduled production cutover.

## Versioned storage contract

`scripts/publish_static_slot.py` now prepares every runtime snapshot under the
same random release ID as the static release:

```text
edge-static/runtime-data/releases/<release-id>/
  catalog.json
  search_index.json
  password_rules.json
  manifest.json
```

The three JSON objects are uploaded and verified before `manifest.json` is
committed. The manifest records the release ID, immutable prefix, every object
descriptor, and a deterministic runtime tree SHA-256. The static slot manifest
records the matching runtime prefix and tree digest. A committed release ID
cannot be reused with different runtime content, and later releases do not
delete earlier runtime snapshots needed for rollback.

Every runtime descriptor uses the same metadata that is actually uploaded:
`Content-Type: application/json`, `Cache-Control: no-store`, body SHA-256,
content length, and release ID. A retry skips an object only when all of those
values match; an object carrying another release ID is uploaded and verified
again.

The publisher no longer writes the old shared namespace. That namespace is
read-only compatibility state.

## Runtime selection and rollback

The Portal Worker derives `/.well-known/edge-state` from its configured catalog
origin (or uses `STATIC_DATA_STATE_URL` when explicitly configured). The state
endpoint supplies the active Edge release ID. The Worker then reads the matching
versioned runtime snapshot from R2.

The Portal Worker deployment explicitly enables Cloudflare's
`global_fetch_strictly_public` compatibility flag. This is required for its
same-zone HTTPS state/data fallback to re-enter the public Edge Worker. The
Edge Worker serves `/.well-known/edge-state` and `/data/*` itself and delegates
only `/api/*` to the Portal service binding, so these fallback requests do not
re-enter the Portal API path.

For a Worker with an Edge state URL, selection order is:

1. validate the active release's `manifest.json`, including schema, release,
   prefix, recomputed tree digest, complete file map, and the requested file's
   descriptor; then read and verify that versioned R2 object;
2. the configured HTTPS static URL, which is served by the same active Edge
   release and must have the same origin as the state endpoint.

The shared R2 namespace is considered only for a true old configuration with
no Edge state URL. A version-aware Worker never uses shared data as a fallback.
If state is unavailable or invalid, the release becomes unresolved and the
Worker reads only the same-origin active HTTPS JSON. If that HTTPS read also
fails, the request fails closed.

The active release lookup has a one-second fresh window, a 1.5-second full-body
timeout, and one in-flight promise shared by concurrent requests. Freshness is
measured from successful completion, not request start. A failed or malformed
state read clears the prior release and starts a four-second backoff; callers in
that window remain unresolved and use active HTTPS without generating another
state request. Catalog, search-index, and password-rule caches include the
resolved release or explicit unresolved identity, so neither unresolved nor
legacy data can masquerade as a previously cached release. If the Edge Worker
rolls back, `/.well-known/edge-state` returns the previous release and all three
caches select the previous immutable snapshot.

## Scheduled publication contract

The original cron is `30 1,5,9,13 * * *`, which is 09:30, 13:30, 17:30,
and 21:30 in Beijing. Successful default-branch completions from the approved
report, Blog, WeChat-source, and chart-index producers can also request a
refresh. Both event classes require `NEUTRAL_SCHEDULE_ENABLED=true`. Manual
`rehearse` and `migrate` remain available while the automatic gate is closed.

Every automatic request builds a candidate but does not automatically imply a
cutover. The candidate publishes `data/release-semantics.json`, a deterministic
manifest covering the stable catalog, full-text search, chart search, password
rules, runtime config, Blog archive, materialized site source, build/Edge
contract, public file paths, and canonical URL set. Volatile scan timestamps and
sitemap `lastmod` alone do not change the semantic digest. An unchanged digest
ends successfully before inactive-slot upload or Edge deployment.

The first reviewed manual `migrate` seeds this manifest on an older active
release that does not have one. After that seed, a missing or invalid active
manifest stops automatic publication. A manual rehearsal always prepares a
candidate and restores the exact prior release; an existing-manifest manual
migrate uses the same no-op comparison as automation.

Before setting the automatic gate to true:

1. deploy and verify the version-aware Portal Worker independently;
2. run the Neutral B-to-A rollback rehearsal and verify exact Worker version,
   Edge state, catalog, canonical route matrix, and Portal runtime release;
3. merge the scheduled/no-op contract while the repository variable is still
   absent or false;
4. run one manual `migrate`, verify the accepted release and immutable runtime
   through CLI HTTP checks, then set `NEUTRAL_SCHEDULE_ENABLED=true`;
5. keep route mutation, cache purge, IndexNow submission, source commits,
   PDF cleanup, shared Report Chat/Research manifests, and legacy pruning out
   of the Neutral transaction.

## Acceptance checks

- Publishing release B never changes the runtime objects selected by live
  release A before the Edge state changes.
- A partial runtime upload has no committed runtime manifest or static slot
  manifest.
- Retrying the same release with identical content skips verified objects;
  a wrong release ID or HTTP metadata forces upload, and retrying the release
  with different content fails closed.
- A partial versioned namespace is unreadable until its valid manifest exists;
  a missing, malformed, or tree-mismatched manifest goes to active HTTPS without
  reading the partial target.
- Switching A to B changes catalog/search/password cache identity to B.
- Rolling B back to A restores A without copying or overwriting runtime JSON.
- An unchanged release semantic digest performs no inactive-slot upload and no
  Edge deployment; search, chart, Blog, template, asset, canonical-path, or Edge
  contract changes each produce a changed component digest.
- Existing content-addressed report PDFs with the expected size are reused by
  HEAD verification, so a no-op refresh does not repeat their R2 upload.
- State failure never returns last-known A or B. It uses same-origin HTTPS;
  HTTPS failure does not fall through to shared data.
- A true old deployment with no state URL can still read the shared prefix, but
  no publisher writes that prefix.
- Scheduled events remain inert unless the reviewed repository variable is
  explicitly enabled after the manual migration and live acceptance sequence.
