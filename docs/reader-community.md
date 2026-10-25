# Reader community and form confirmations

Successful new registrations and accepted membership, report, research-quota,
Newsfeed, course and feedback submissions send a Chinese/English receipt from
the public info mailbox. The fixed receipt provides WeChat `macroGate` and
WhatsApp `+1 (740) 875-3400`. Owner notifications retain their existing routing.
Receipts use a separate private `_form-acknowledgements/v1` ledger. A receipt
failure does not undo a saved application or account. Pending/unknown outcomes
are not automatically resent. Existing expiry reminders retain their schedule.

The floating feedback entry is available through the common site runtime and
shared app bootstrap, including preserved English and extended-locale pages.
Guests supply a reply email; accounts use their real account address, while
legacy generated-email accounts may supply a real address. Feedback records
are private under `_feedback/v1`, with category, bounded message and page path
without query parameters. Owner notification and customer receipt follow the
same accepted-submission flow.

## Report discussions

`GET /api/report-discussion?source=catalog&report_id=...` reads discussions.
Authenticated users can post genuine comments; authors and administrators can
delete ordinary-report comments. Existing hot-report comment storage is reused.
AI starters have a visible AI label and do not increase the human-comment count.
Source text, generation evidence and author identifiers stay private.

The `New report discussion starters` workflow runs twice an hour. Its first run
only records the complete live primary catalog as the historical baseline.
Later runs queue newly discovered primary-catalog reports whose date is not
before activation. Historical reports retain a comment area but receive no AI
backfill. Each run attempts at most 20 new reports. This first version does not
automatically generate starters for externally searched report sources.

Each target requires a private eligibility marker and a signed operation at
`POST /api/ops/report-discussions/generate`. The Worker verifies the actual
report and uses report-bound extracted text. A source file must match its
manifest ID, size and SHA-256; the text-index fallback requires an exact report
ID. Missing text waits for later publication. The generated discussion includes
an internally checked source quotation; it cannot introduce unsupported numeric
figures. Provider-call reservations are durable and unknown outcomes are not
implicitly repeated. Neither reading a report nor submitting a human comment
starts paid generation.

## Download-to-registration path

After the PDF response has been fully received and handed to the browser's save
mechanism, an inline invitation appears once per report per session. The site
does not claim to observe completion of the operating system's save dialog.
Guests can register in the existing modal, then remain on the current report.
Registered users receive continuation actions. Up to three related reports use
links without shared passwords. Existing download permissions are unchanged;
copy describes AI research allowance, check-in and report vouchers without
promising automatic full-text access.

Existing `download_success`, `account_auth` and `report_open` events record the
funnel. Invitation actions use placement `post_download`; registration is
counted only after the actual successful registration event. Dismissals and
repeat suppression are session-local. Passwords and delivery URLs are not added
to analytics.

### Aggregate journey measurement

`scripts/summarize_portal_growth_range.py` emits `post_download_diagnostics`
in the private aggregate growth review. The JSON and Markdown contain counts
only; raw session, visitor, account and report identifiers never enter this
diagnostic output. Controlled `post_download_*` actions and the
`post_download` placement remain identifiable in the general journey table.

`post_download_shown` means the invitation was rendered. It is not exposure.
`post_download_viewed` means at least 25% of the card entered the viewport while
the tab was visible, or a direct card interaction established visibility. A
missing IntersectionObserver never creates a synthetic exposure. The ordered
signup path is:

1. `download_success`.
2. `account_auth / post_download_viewed / placement=post_download`.
3. `account_auth / post_download_signup_click / placement=post_download`.
4. `account_auth / register / status=success / placement=post_download`.

Every step must share an explicit `session_id` and have a strictly increasing
valid `client_ts`. The successful registration event need not carry a report
ID. The supplementary `post_download_registered` UI event does not replace
successful registration. Server arrival order, visitor hashes, matching IPs
and missing client times cannot establish a sequence. Equal timestamps are
reported as `ambiguous_timestamp_sessions`; rates involving these ambiguous
stages remain null. A later step may be present without its predecessors,
which is an incomplete observed path, not proof of conversion.

`state_paths` separates explicit guest signup from signed-in continuation
(`continue_reading`, `discussion`, `research`, and `related_open`). It uses
`access_state=guest|signed_in` on both exposure and action; missing or
unrecognized values remain `unknown`. Related-report clicks retain event type
`report_open`. `by_download_access` also separates the controlled successful
download actions `password_download`, `account_download`, and
`account_or_password_download`; absent or unrecognized actions stay `unknown`.
It never reads a URL password or infers authentication from download method.
A session may have several access/state paths, so cohort counts are not added.

Absent action stages are `unavailable` with null counts and rates. Events
without explicit sessions or valid client times are counted as context gaps,
not filled in from older records. Historical windows therefore cannot become
zero-exposure or zero-conversion claims. These are observed session paths,
not unique registered accounts, paid membership, revenue or causal uplift.
The ordered funnel's download denominator includes only explicit sessions with
an observed post-download event. A review spanning launch does not include
older uninstrumented downloads as presumed unexposed sessions; overall download
totals remain in the separate `download_diagnostics` section.

## Delivery password context

Delivery links keep their explicit password and URL encoding. Device/session
password recovery is scoped to the report ID; the old global last-used value
and history entries without a matching report ID cannot fill another report.
After a 401 rejection, only the exact submitted value is cleared from matching
storage/history and suppressed for that report for the current page lifetime.
Focus, page restoration and URL fallbacks cannot revive it. A newer replacement
entered while the request is pending is preserved. A later confirmed password
download can validate that same value again; initialization, pending preparation
and account-authorized downloads do not establish password validity.

Delivery-link generation requires a successful API response containing a
password. An HTTP error, missing password or network failure is surfaced as a
generation failure, never replaced with a locally cached administrator key.
The regression suite uses synthetic values and reports no delivery credentials.

## Independent original-name Course directory

`/course-full.html` is a separate account-area entry; the existing
`/courses.html` and its membership rules stay unchanged. The new page is
`noindex,nofollow,noarchive` and excluded from public sitemaps. Its static HTML
and JavaScript contain no original inventory. The existing account control
handles sign-in; `GET /api/course/full/access` must return `allowed: true`
before the page requests or displays directory metadata.

Access requires a currently valid full membership that has remained continuous
for two calendar months, calculated at the same Beijing-time instant with
month-end clamping. Account age and advance payment alone do not establish
tenure. Renewals without a gap preserve the recorded start; lapses, revocations
and subsequent reactivation reset it. Matching current immutable grant audits
can recover a conservative legacy start. Unproven history shows
`needs_history_verification`, with dates and a support entry; it is not silently
treated as two completed months. The existing super-admin route can record a
dated verification with its audit reason.

`GET /api/course/full/directory` provides original filenames and folder labels,
search, folder/type filters and pagination after a fresh eligibility check.
Names render as plain text. Each Request submits only the selected
`directory_item_id` and page path to
`POST /api/course/full/directory-request`; the server resolves the canonical
title from the private catalog, not from user-supplied text. Owner notifications
go to the fixed public info mailbox and accepted requests receive the bilingual
confirmation. Real account email is authoritative; generated-email accounts
can supply a reply address. The account/item pair is deduplicated for 24 hours.
There is no direct file-download endpoint, and original titles stay out of
analytics events. Logout or identity changes clear loaded metadata.

Publish the verified complete original inventory with the
`Original-name course directory private publish` GitHub workflow. It runs only
on `main` with `PORTAL_AUTOMATION_ENABLED=true`, reads the encrypted bundle
`.course-directory/course-full-v1.json.aesgcm`, and uses the separate
`COURSE_FULL_DIRECTORY_BUNDLE_KEY_B64` secret plus the existing R2 credentials.
`scripts/publish_course_full_directory.py` decrypts and validates exact metadata
fields, writes a content-addressed private revision, then conditionally updates
`_course-directory/full-v1/directory.json`; both writes are read back and hash
checked. Logs contain counts, byte size and digest, not source rows. Keep
plaintext inventory and source/download URLs out of the repository and public
static assets. Without a valid complete private catalog, the API returns 503
and the page says temporarily unavailable; it never substitutes the existing
sanitized directory or claims completion from an empty result.

## Release checks

Run the reader/form Node suites, collector tests, lazy-asset fingerprint tests,
public identity check and existing app loading budget. Reader modules are lazy
loaded and content-fingerprinted through their parent loaders. Deploy the API
Worker with the existing emergency workflow, then publish static assets through
the complete incremental neutral-edge release. Do not overwrite individual
objects in an active manifest-bound static slot. After both releases, dispatch
the starter workflow once and verify its baseline reports zero attempts.

For the independent Course entry, also run `course-full-frontend`,
`course-full-directory` and `course-membership-continuity` Node tests plus
`scripts/test_publish_course_full_directory.py`. Verify the private inventory
source and its full item count before dispatching its publication workflow;
deployment of the empty page shell alone does not publish the original catalog.
