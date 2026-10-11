# Customer content API implementation contract

The public usage guide is `portal_suite/site_src/developer-api.html`. This note
documents the Worker boundary and its offline regression coverage. Existing web
download and English editorial access policies are separate from these API routes.

## Account and key authorization

`createCustomerContentApi(adapters)` returns `matches(path)` and
`handle(request, env, executionContext)`. It handles public `/api/...` paths;
the Worker integration normalizes its direct endpoint aliases before calling it.
Unmatched paths return `null` so the owning router can issue its normal 404.

| Route | Method | Authorization / response |
| --- | --- | --- |
| `/api/admin/content-api/grant?email=...` | GET | Existing super administrator session; `{ok,email,grant,keys}` |
| `/api/admin/content-api/grant` | POST | Same administrator; `{email,enabled,access_mode,report_ids,scopes,expires_at,...limits}`; returns `{ok,email,grant}` |
| `/api/account/content-api` | GET | Existing user session; `{ok,grant,keys}` |
| `/api/account/content-api/keys` | POST | User session; `{name,scopes?,expires_at?}`; returns 201 `{ok,key,secret}` |
| `/api/account/content-api/keys/{id}` | DELETE | Owner session; returns `{ok:true}` |

All management writes reject a foreign `Origin`. Keys cannot authenticate account
management or administrator routes. Key secrets use 32 cryptographically random
bytes and are returned only at creation; storage contains a SHA-256 digest.
The random lookup ID adds another 12 bytes but is not treated as the secret.
Neither responses nor exceptions are logged by this module.

Each content request re-reads the current account, account grant and key record.
Disabled accounts, changed account identities, revoked keys, expired keys,
expired/disabled grants and scope reductions fail closed. Disabling a grant
revokes every prior key; re-enabling does not resurrect them. Membership changes
are checked by the owning content adapters on each call.

Grant access modes:

- `membership`: retain existing account access and limited download accounting.
- `granted_corpus`: explicit independent API authorization for `report_ids`, or
  the full API corpus when that list is empty. This does not upgrade web access.

Scopes are `reports:read`, `reports:download`, and `artifacts:read`. The current
grant and key must both contain the required scope. The latter two scopes can be
used independently; the server does not require an extra list scope to download
an already-known, authorized identifier.

Enabled grants require an expiry within 366 days. Keys default to the earlier of
90 days or the grant expiry; callers can shorten that period. Key names have at
most 80 characters. There are at most five active keys per account, and at most
500 explicitly granted report IDs. Expired/revoked metadata is pruned when the
stored key history reaches 100 entries. Request JSON is limited to 16 KiB.

## Content adapter boundary

Adapters receive `(env, query, context)`. The context includes current `user`,
`grant`, and public `key` metadata. Required account adapters are `bucket(env)`,
`currentUser(env,request)`, `requireAdmin(env,request)`, and
`findAccount(env,{id?,email})`. Users must expose string `id` and `email` plus a
normalized boolean `disabled`. Account lookup must verify both requested identity
fields when both are supplied.

| Content route suffix after `/api/content/v1` | Adapter | Query / result |
| --- | --- | --- |
| `/reports` | `listReports` | `{date?,cursor,limit}` → `{items,next_cursor}` |
| `/reports/{id}` | `getReport` | `{reportId}` → public row or null; route wraps `{ok,report}` |
| `/reports/{id}/download` | `downloadReport` | `{reportId}` → file Response |
| `/reports/{id}/artifacts` | `listArtifacts` | `{reportId,kind?,language?,cursor,limit}` → `{items,next_cursor}` |
| `/reports/{id}/artifacts/{artifactId}` | `downloadArtifact` | `{reportId,artifactId}` → file Response |

The module enforces report-ID filters before exact content calls and again on
listing results. Adapters enforce membership and resolve only trusted catalog
rows or report-bound publication manifests. No API request accepts an R2 key,
bucket prefix, provider URL, local path, workflow ID or draft locator.

Lists default to 25 records and accept at most 100. Cursors are opaque and bounded
to 512 characters. Empty results are 200 with `items:[]` and `next_cursor:null`.
Known public fields are selected explicitly; arbitrary adapter properties are
not serialized. A descriptor has `id,report_id,kind,language,mime_type,size`, with
optional `filename,sha256,text_scope,page_number`. An existing chart's list size
may be `null`; its download still requires the actual known byte count. Published
content can be text, image, chart, metadata, translation, article or PDF.
Availability of a kind or language is not guaranteed for every report, and
fallback research text is identified as an excerpt rather than full text.

File adapters return status 200 with a known `Content-Length`, no content encoding,
and at most 256 MiB. Only content type, length, attachment disposition and ETag are
forwarded. The module enforces the declared length while streaming and cancels
on mismatch; a failure after headers have been delivered aborts the stream.
It does not buffer and validate a complete PDF or verify arbitrary content hashes.

For web access with a limited download allowance, an adapter sets
`context.commitDownload = async () => ...`. The module reserves API bytes first,
then awaits this callback before exposing the stream. The callback must throw a
`CustomerContentApiError` on denial, not return a failed Response or boolean.
Thus API byte-limit rejection cannot consume a web trial download. Public errors
are fixed codes; arbitrary adapter error messages never become response text.

## Usage accounting

Limits apply to the account across all its keys, not to each key separately.
Defaults are 30 requests per minute, 1,000 requests per UTC day and 1 GiB of file
bytes per UTC day. Administrator maxima are 600/minute, 100,000/day and 100 GiB/day.
UTC days reset at 00:00 UTC (08:00 Beijing time); minute windows are fixed UTC
minutes. Request count includes authenticated, scoped attempts that later return
content-not-found or another content error. Syntax/authentication/scope failures
are rejected before the usage reservation.

Byte usage counts reserved file bytes, including interrupted streams and later
membership-commit failures; it is deliberately conservative and is not a billing
meter. JSON directory/descriptor responses do not count as file bytes. R2 account
state and usage mutations use ETag compare-and-set with at most four attempts.
Concurrency cannot exceed the shared allowance by racing independent keys.
After an uncertain write outcome, the request fails closed without an automatic
client retry or a compensating write. These counters do not perform payments.

Only this module's authorization data is stored beneath
`_customer-content-api/v1/`. Deliverable copies belong to the separate
`_customer-content-data/v1/` namespace. Existing `_workflow-cache/mineru-results/`
ZIPs contain source/provider lineage and are never exposed directly. Existing
public chart records pass through `publicChartGalleryRecord`; process metadata
must be published with its own field allowlist.

## Validation

`node --test portal_suite/tests/customer-content-api.test.mjs portal_suite/tests/customer-content-worker.test.mjs`

The first suite exercises key secrecy/revocation, current grant intersection,
account identity changes, corpus boundaries, request validation, simultaneous
ETag reservations, byte accounting and transfer cancellation. The second invokes
the actual Worker router and current session/account/content adapters against
synthetic R2 records: super grant, key creation, catalog, PDF, Chinese text,
English translation, chart metadata/image delivery, existing membership changes,
per-report purchases, web trial accounting, route aliases and account disable.
Every network request in that suite fails the test. It does
not claim that synthetic tests prove production objects have been published.

## Publishing existing outputs

`Publish customer API content` runs after the existing Daily report workflow,
or manually with that workflow's completed main-branch run ID. It downloads the
current public catalog before binding reports; the repository's older catalog
is not used for production binding. A unique normalized title and matching source
date are required to attach artifacts to an existing report. Otherwise the
publisher creates a separate processed-content record without claiming an
original PDF is available.

The publisher selects existing parsed Markdown, Chinese/English translations,
article drafts, podcast text scripts, source images and typed figure/translation
metadata. Translated PDFs require matching translation status. It does not expose
whole workflow archives, provider credentials, local paths, task logs or raw
runtime state. It does not generate missing content or perform paid model calls.

Source handoffs are hash-verified before bounded archive extraction. Artifact
bytes are copied into immutable report-bound objects and verified by readback;
conditional writes merge manifests and the index without losing concurrent
additions. Markdown image references use the delivered filenames; clients can
save related artifacts together using their `filename` fields.

The final receipt distinguishes unique report IDs from repeated report/artifact
publications across processing and translation handoffs. A successful receipt
proves publication of that selected source run, not all historical pipeline
outputs. Future Daily runs publish automatically; retained historical runs can
be selected explicitly without re-parsing or re-translating them.

Offline publisher validation: `python3 -B scripts/test_publish_customer_content.py`.
