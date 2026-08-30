# Engagement, Analytics, and Course Access

This document defines the production contract for daily engagement rewards,
attribution analytics, and the gated Course page. Public source must keep using
the neutral Portal Suite identity and the existing contact placeholders.

## Daily rewards

The active policy is defined in [Reward Engagement v2](reward-engagement-v2-architecture.md).
The first check-in gives a 72-hour welcome report credit, the first three-day
streak gives a second 72-hour credit, and ordinary later check-ins award points
rather than a daily report. The Worker is the only authority for UTC+8 dates,
balances, streaks, credits, and claims; the browser never submits a date or a
points balance.

API contract:

- `GET /rewards`: current balance, effective streak, credits, today's check-in
  and claim state.
- `POST /rewards`: idempotent daily check-in.
- `POST /rewards/claim`: `{ "reward_kind": "daily|points", "report_id": "..." }`.

## Course gate

`courses.html` is visible in the top navigation. Its static HTML contains only
the sanitized promotional heading and an empty mount point; anonymous and
ineligible visitors do not load or render the featured course-material carousel.
After `GET /course/access` succeeds, the browser materializes the catalog and
the cover-only carousel. The Worker
accepts a full membership entitlement or an unlimited full-site administrator
grant, and requires it to be lifetime or to expire at least 30 * 24 hours after
the server check. Filtered grants, finite-download grants, and trials do not
unlock Course. Privileged operational accounts remain eligible.

The gated API catalog contains 44 hand-authored, topic-based entries spanning
financial modeling, capital markets, private investing, investment research,
capital-markets law, legal professional skills, reference libraries, career
development, and general professional education. Every entry has a neutral
`id`, `category`, `title`, `summary`, and `audience`. These public-facing fields
must describe subject matter only. They must never be copied from an upstream
directory name, file name, provider label, community name, instructor name, or
private storage locator. Investment-bank names may be retained when they are
material to the subject matter.

During the frontend rollout, an eligible response includes both `courses`, a
title-only string array for the previous client, and `course_catalog`, the 44
structured entries used by the current client. An anonymous response contains
neither field, while an authenticated but ineligible response contains empty
arrays. This keeps catalog details behind the same server-side membership gate
throughout a Worker-first or static-site-first deployment.

Contact details are returned only in the successful authenticated response and
come from the private release injection process; do not place a real personal
address in public source. Raw inventory documents, exact resource counts,
storage paths, and source file names remain outside the repository and are
never serialized by this API.

### Featured course materials

The Course page includes a member-gated, cover-only carousel for the 20-item
`str-01` strategic-analysis collection. Sanitized display metadata lives in
`portal_suite/site_src/data/course-materials.json`; it contains no R2 locator or
private WebDAV root. The 720 by 405 WebP covers are ordinary static teaser
assets. The carousel uses native CSS scroll snap, keyboard and button controls,
mobile touch scrolling, a six-second cycle, and disables automatic motion when
the visitor requests reduced motion.

Membership unlocks only the cover preview, never the PDF. The legacy
`GET /course/material?id=maifu-NN` route always returns a private 404 and does
not read the private PDF object, including for eligible members. Each carousel
item instead submits `POST /course/material-request` with only the material ID.
The Worker authenticates the user, applies the same 30-day Course entitlement
check, resolves the canonical title/topic/page count from the private stable
manifest, and sends a request to the fixed `info@kcdesk.com` recipient. Browser
supplied titles, storage locators, and recipients are ignored. Requests are
persisted privately and deduplicated per account and material for 24 hours;
different decks remain independently requestable.

`.github/workflows/course-materials-private-publish.yml` fetches the exact 20
source PDFs from the configured private Jianguoyun WebDAV directory, verifies
each byte count, SHA-256 digest and page count, and uploads only content-matched
objects. It never lists or deletes course objects and writes the private stable
manifest only after every PDF has passed read-after-write verification. The
private directory publisher independently HEAD-verifies all 20 objects before
merging the sanitized rows into the member directory and Course Chat indexes;
therefore a missing or mismatched PDF cannot produce a visible-but-broken
course release. These private PDF objects are retained only for manual request
fulfilment; publishing them does not create a browser-readable route.

### Private file directory

Eligible members can browse the concrete resource inventory through
`GET /course/directory`. The endpoint calls `courseAccessForUser` before it
reads directory storage. An anonymous request receives `401`; an authenticated
account that does not meet the Course gate receives `403`. Neither response
contains `items`, `facets`, entity names, counts, or generation metadata.

The accepted query parameters are:

- `q`: an 80-character, Unicode-normalized search across the display name,
  neutral folder labels, category, derived file type, and allowed notable
  entities;
- `course_id`, `category`, and `file_type`: exact filters;
- `page` and `page_size`: bounded pagination, with a maximum page size of 100.

An eligible response contains `items`, `total`, `page`, `page_size`,
`has_more`, private `facets`, and `generated_at`. Each item is reconstructed by
the Worker from an allow-list and contains only `id`, `course_id`, `category`,
`name`, `folders`, `extension`, `size_label`, `date`, and `entities`. The
response never includes an upstream path, provider field, original directory
root, R2 object key, download locator, or encrypted-bundle metadata. Large
investment banks, law firms, exchanges, and regulators may remain in a display
name or entity list when they materially identify the indexed content; source
course, community, and instructor brands remain redacted.

The validated index is a single private R2 JSON object at a neutral internal
key. A Worker isolate retains the parsed allow-listed representation for five
minutes, keyed by its R2 binding, so the roughly forty-thousand-row index is not
read and parsed for every keystroke. The object is capped at 16 MiB and 45,000
rows. Directory responses use `private, no-store` and never put the index in
static-site assets or browser storage.

Course Chat does not load this full directory. The private publisher first
derives a bounded candidate set strictly from the already sanitized rows.
Every row with a non-empty allowed `entities` list is retained, followed by at
most 30 entity-free representative rows per course in source order. The result
must cover all 44 courses and is capped at 5,000 rows and 2 MiB. It cannot add
fields or values that were absent from the sanitized directory.

The live lookup is a private R2 v2 direct-bucket index rooted at
`_course-directory/v2/chat-lookup/manifest.json`; the former
`_course-directory/v1/chat-index.json` remains only as a rollback-compatible
object. The stable manifest points at four revisioned immutable objects:
token table/data and item table/data. A table slot is exactly 12 bytes
(`uint64` big-endian offset plus `uint32` big-endian length). The slot is
selected with the first 64 bits of SHA-256 over the exact UTF-8 key modulo the
bucket count. Its compact JSON collision bucket must contain the exact key
before the value can be used.

Questions are normalized with NFKC and lowercase, then bounded to eight Latin
tokens or Chinese 2/3/4-character grams. A token posting contains at most 48
pre-ranked safe item IDs; at most 12 items are fetched. Institution
attractiveness, useful file type, date, and stable title order are applied at
publish time, preserving compelling institution, law-firm, exchange, and
regulator materials without exposing a private source brand. Twelve sanitized
defaults are embedded in the manifest for empty or missed queries. With the
manifest cached, one request performs at most 40 small R2 range reads and never
parses the complete candidate set on a cold isolate.

### Encrypted directory publishing

The plaintext inventory and mapping inputs stay outside Git. The repository may
track only a sanitized AES-256-GCM bundle at
`.course-directory/course-directory-v1.json.aesgcm`. Its JSON envelope is:

```json
{
  "format": "course-directory-aes-256-gcm-v1",
  "nonce": "base64-encoded 12-byte nonce",
  "ciphertext": "base64-encoded ciphertext and authentication tag"
}
```

The plaintext inside the envelope is a gzip-compressed schema-version-1 JSON
index, encrypted with associated data `course-directory-v1`. The 32-byte key is
base64-encoded in the `COURSE_DIRECTORY_BUNDLE_KEY_B64` GitHub Secret; it must
never be written to the bundle, source tree, workflow input, artifact, or log.
The same private redaction list is stored in
`COURSE_DIRECTORY_REDACT_TERMS` and is supplied both to the publishing workflow
and to the Worker deployment.

After the private builder emits the flat sanitized index, create the tracked
envelope with the public neutral helper:

```sh
node scripts/encrypt_member_course_directory.mjs \
  --input /private/path/course-directory.json \
  --output .course-directory/course-directory-v1.json.aesgcm
```

The helper reads `COURSE_DIRECTORY_BUNDLE_KEY_B64` by default. It also accepts
`--key-file /private/path/key` for either a raw 32-byte key or its base64 text.
It prints only the output basename, format, encrypted size, and ciphertext
digest. `.gitignore` excludes every other file in `.course-directory`, so a
plaintext index, private map, or key cannot be staged from that directory.

`.github/workflows/course-directory-private-publish.yml` performs the release:

1. decrypt the tracked ciphertext inside the ephemeral runner;
2. cap decompression, validate identifiers and display fields, reject every
   configured redaction marker and path separator, and rebuild every row from
   the API allow-list;
3. derive the bounded Course Chat subset and the v2 token/item direct indexes
   from those rebuilt rows without reading any separate private mapping;
4. upload the revisioned lookup objects, rollback-compatible Chat subset, and
   full sanitized directory as private `no-store` objects;
5. verify every uploaded object's own SHA-256 metadata, then atomically replace
   the stable v2 manifest as the final write.

Each object replacement is atomic, and the workflow reports success only after
all metadata checks pass. A failure before the final manifest write leaves the
previous complete lookup revision live. The Worker rollout follows this
publisher, so it cannot depend on a Chat index that the release did not verify.
The workflow never uploads plaintext directory or lookup data as an Actions
artifact and never prints private item counts or digests.

## Analytics collection

`assets/analytics.js` is the common client for application, legal, generated
report-index, SEO report, and Blog pages. It emits one page view per page/path
and supplies the same context to application events:

- persistent anonymous visitor ID;
- 30-minute session ID, landing path, and first-seen/returning state;
- referrer and referrer host;
- UTM source, medium, campaign, term, and content;
- language, screen, navigation type, and coarse device hint.

The browser records only `pathname`; UTM values have dedicated bounded fields.
The Worker independently removes query strings and fragments from path,
landing, and referrer values, so password or download-token parameters cannot
enter the archive. The public endpoint accepts only same-origin requests,
bounded JSON bodies, and an event-type allow-list.

The Worker adds country/colo, a keyed IP hash, coarse device classification,
and available Cloudflare bot-management hints. Raw IP addresses are never
written, and the IP hash is omitted if its deployment secret is unavailable.
Every event remains mirrored under the primary and backup private R2 analytics
prefixes.

## Per-day administrator summary

`GET /account-admin/analytics-day-summary?date=YYYY-MM-DD` is super-user only.
Large days are scanned in bounded R2 batches. An incomplete response returns a
private opaque `job_id`; the caller repeats the request with the date and job
ID until `has_more` is false. Completed summaries are cached privately by date.
`refresh=1` starts a clean rescan.

The public response includes event/page-view counts, unique visitor/session
counts, top paths, referrer hosts, countries, devices, bot hints, event types,
and UTM dimensions. It never returns visitor IDs, IP hashes, or the internal
deduplication set. The Activity page implements the polling and progress UI.

## Verification

Coverage is provided by:

- `portal_suite/tests/engagement-rewards.test.mjs`
- `portal_suite/tests/analytics-attribution.test.mjs`
- `.github/workflows/course-directory-private-publish.yml`
- the existing portal frontend, export-pagination, Blog build, and SEO suites.
