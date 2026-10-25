# Reader community and form confirmations

Successful new registrations and accepted membership, report, research-quota,
Newsfeed, course and feedback submissions send a Chinese/English receipt from
the public info mailbox. The fixed receipt provides WeChat `macroGate` and
WhatsApp `+1 (740) 875-3400`. Owner notifications retain their existing routing.
Receipts use a separate private `_form-acknowledgements/v1` ledger. A receipt
failure does not undo a saved application or account. Pending/unknown outcomes
are not automatically resent. Existing expiry reminders retain their schedule.

The floating feedback entry is available through the common site runtime.
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

## Release checks

Run the reader/form Node suites, collector tests, lazy-asset fingerprint tests,
public identity check and existing app loading budget. Reader modules are lazy
loaded and content-fingerprinted through their parent loaders. Deploy the API
Worker with the existing emergency workflow, then publish static assets through
the complete incremental neutral-edge release. Do not overwrite individual
objects in an active manifest-bound static slot. After both releases, dispatch
the starter workflow once and verify its baseline reports zero attempts.
