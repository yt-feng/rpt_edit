# Neutral Runtime-Data Versioning

Last updated: 2026-08-31

## Why Neutral remains paused

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

This incomplete rollback boundary is why Neutral is deliberately hard-paused.
It must not be re-enabled merely because one source-inspection run is green.

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

## Migration sequence before Neutral can be enabled

1. Keep `neutral-edge-cutover.yml` limited to `inspect-source`.
2. Deploy and verify the Portal Worker runtime-selection code independently.
   With an older active release that has no versioned snapshot, it reads the
   active HTTPS static JSON and does not modify the shared namespace. The
   manual Portal Worker workflow captures the exact currently active Worker
   version before deployment, verifies the live API afterward, and restores
   and re-verifies that exact version if deployment or smoke verification
   fails.
3. Run local and source-inspection tests, including the runtime versioning,
   publisher interruption, legacy fallback, release switch, and rollback cases.
4. In a controlled future release, let the publisher prepare the inactive
   static slot and its matching immutable runtime snapshot.
5. Verify both manifests and their matching release ID before any Edge deploy.
6. Switch the Edge Worker, then verify state, fixed no-query routes, API health,
   catalog/search behavior, and release-specific assets.
7. Exercise an automated rollback rehearsal: restore the previous Edge Worker
   version and verify that the Portal Worker resolves the previous runtime
   release as well.
8. Only after the rehearsal is green may a separate change restore Neutral
   deployment operations. Scheduled publication must remain absent until that
   change is reviewed and accepted.

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
- State failure never returns last-known A or B. It uses same-origin HTTPS;
  HTTPS failure does not fall through to shared data.
- A true old deployment with no state URL can still read the shared prefix, but
  no publisher writes that prefix.
- Neutral remains hard-paused while these contracts are only local/source-level
  evidence; no code change in this document authorizes a production release.
