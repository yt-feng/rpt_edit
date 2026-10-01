# Daily reading locales and English editorial access

## Reconciled baseline

Work continues from reviewed main `1c1c704f2eb678dce59e83967553e03b1df053e0`
in the existing clean isolated worktree. The dirty primary checkout is untouched.
All 33 non-English locale roots already use `portal-shared-v1`; the preceding
production acceptance retained 24 approved articles per locale (792 total).
That does not prove daily-new-content coverage.

Current daily producer `36801745121` is still working, not stopped: completed
locale jobs exist, two CPU jobs are active, and the remaining matrix jobs are
queued under the two-worker limit. One Khmer job failed; failure diagnosis and
durable recovery remain open. Refresh-triggered run `36907095539` is pending
behind it. Do not cancel or restart solely because the aggregate run says queued.

## Daily production policy restored

The repository lacked the opt-in variables used by its existing reviewed
handoff/reviewer code. The operator's request authorizes daily updates for the
already-live locale set. The following values were set and read back:

- `PORTAL_EXTENDED_INCREMENTAL_LOCALES=all-supported`
- `PORTAL_EXTENDED_AUTO_PUBLISH_LOCALES=all-supported`
- `PORTAL_EXTENDED_AUTO_REVIEW=true`

The environment still requires reviewer `yt-feng`; the existing
`GH_DISPATCH_TOKEN` name is present. No credential value was read or printed.
The 13 delegated-review regressions pass. Exact source/candidate/tree approval,
already-live locale limits, cutover acceptance and rollback remain required.
This is configuration, **not** a claim that a new daily batch is live.

The source-day queue and independent bounded cursors are implemented below.
Actual staging recovery and automatic production updates still require runtime
evidence; configuration and local tests alone do not prove those outcomes.

## Daily queue implementation, not yet merged

The fast `Extended locale source admission` workflow follows successful source
refreshes independently of the slow CPU matrix lock. It admits only the current
Shanghai source day, verifies the page-owned publication date, and freezes its
bounded <=500-page inventory privately in R2 before publishing a queue pointer.
No public model inference, translation artifact/cache or historical fetch occurs
in this admission step.

Each of the 33 locale cursors selects at most 24 unfinished/changed pages from
the immutable inventory. A locale that completed the first 24 can select its
next 2 while another locale resumes its first 24. Jobs carry their own exact
source generation; checkpoint memos still reuse validated unchanged units.
Hot newly admitted days have priority. Older work is only an already-admitted
R2 snapshot, never new discovery of historical URLs. Queue capacity is bounded
at 32 unfinished source days; overflow is explicit and discards nothing.

Continuation compares durable completed-page receipts against the admitted
inventory. Partial success can advance healthy locales, but unchanged failures
cannot self-dispatch forever. The two-CPU-worker/four-hour-per-locale limits,
complete-candidate requirement, approved-page carry-forward, normal release
lock and exact cutover/rollback are unchanged.

Delayed consumers now carry a checksum-bound admission proof. Before delegated
approval, the reviewer verifies the original capture's real main/public run,
attempt/SHA, successful source job, source day and exact inventory subset via
GitHub and R2. Merely labeling an old source as new cannot receive approval.
Existing reviewer identity and exact candidate/tree checks are not bypassed.

The roundtrip operation adds a separate unserved private staging probe for
source/admission/checkpoint recovery and independent cursor simulation. It
uses synthetic storage fixtures, zero model calls and no ready candidates;
synthetic completion metadata cannot be published. This probe has passed with
the in-memory R2 harness; a real Actions/R2 result is still required.

Local checks: queue/provenance/staging 16, daily incremental 21, handoff 10,
delegated review 15, publication/carry-forward 15, restore 3, R2 6 and financial
quantity 13 passed. Workflow syntax also passes the non-browser YAML parser.
Local PyYAML is absent; the Linux CI job installs it for the broader checks.

The exact Khmer failure in producer `36801745121`, job `110177654930`, is a
four-hour budget timeout (exit 75): 23/24 pages completed, checkpoint/candidate
storage steps passed, zero unit failures and zero paid-provider requests.
It is not an R2 or English-filter failure. Its durable partial checkpoint must
be resumed against the same source; an incomplete 23/24 candidate is not live.

## English access implementation, not deployed

English is a separate text-only secondary-commentary product. It must not
reuse the full-reading renderer, report directory, chart pages or original
report bodies. Public HTML, JSON-LD and catalogues contain only preview text.
Full translated secondary commentary resides under private
`_english-commentary/v1/bodies/<sha256>.json` and is served only by the new
Worker access boundary.

Initial product rule: each registered account has 3 distinct full-commentary
reads, lifetime. Rereading an unlocked article does not spend another read.
Active existing website memberships (the established >=1 month membership
authority) have unlimited commentary reads; report/download trial quotas are
unchanged. Disabled or revoked sessions are checked by existing authentication.
Anonymous visitors see only previews and sign-in; exhausted accounts are
directed to the existing membership-request flow. No new payment system.

The new gateway allows only an approved versioned ledger and checksum-matched
text-only bodies. Unknown fields, original/report kinds, quoted-original blocks,
charts, images, embedded URLs, HTML and original-language prose fail closed.
Free grants use conditional R2 writes; concurrent requests cannot exceed 3.
Missing/corrupt content and permission/auth/membership errors cannot reset
allowances or return private text. Replies are private/no-store. Request bodies,
objects, field sizes, catalogue pages and quota retries are bounded.

14 synthetic gateway regressions currently pass, including concurrency,
membership expiry, anonymous requests, tampering and actual Worker route wiring.
Only code/tests exist at this checkpoint: the English source whitelist,
Hy-MT2 CPU builder, candidate/approval/cutover integration, public preview UI,
membership UX and live authenticated acceptance are still required. No English
page or translated commentary was fabricated, generated locally or published.
The gateway plus existing membership-request and Newsfeed worker suites passed
29 tests together. The API is noindex/private/no-store; the future public
English preview HTML remains the SEO surface.

A live receipt refresh in this pass hit a DNS-resolution timeout. No local
network state was inspected or changed. The preceding verified production
baseline remains evidence; this failed check is not current live acceptance.

## Review and runtime dispatch checkpoint

PR #196 is open, not merged.
Implementation checkpoints: gateway `5face1c2e6f74bf58de77076b77d76a564163765`,
daily queue `1be22201461f008961f5d8c55476cb31bfd71512`, and staging-lock isolation
`460f6b62379d61864698355b16e44acd78907f6f`.

Credential-free CI on that source started as extended regression `36924368147`,
public identity `36924367976`, and API cost controls `36924367909`; all were
running at the immediate receipt, not yet accepted as passing.

Private R2 roundtrip/staging Action
`36924379228`
was dispatched from `codex/extended-locales-daily-english-20261001` with
`operation=roundtrip`. It performs zero model inference and cannot activate
pages. Dispatch returned its run URL; no post-dispatch monitoring was performed.
Actual private R2 results and CI conclusions remain open. No new production
cutover was dispatched and no English page is claimed live by this checkpoint.

Next required implementation remains the English editorial-only source
extraction, pinned Hy-MT2 candidate builder, preview/paywall frontend and
version-bound private-body publication/rollback integration. Then obtain
normal PR/CI/staging evidence and prove daily/live access outcomes. The full
33-locale daily-update plus English product objective is not complete.

## Staging dependency correction

Run `36924379228` completed with failure before the new queue probe could access
R2: `portal_extended_daily_queue.py` imported `requests`, but the roundtrip job
installed only boto3. The existing storage roundtrip step succeeded; the new
admission/recovery probe has not passed. Install requests in this isolated job
and assert its dependency list in the workflow regression. This correction does
not change storage validation, candidate approval, translation or production.

Corrected dependency commit: `40e3670e`.
The new isolated run is `36925028114`,
dispatched on the corrected branch. This entry records dispatch, not a passing
result, and does not claim a production update.

## English editorial capture and CPU candidate checkpoint

The current public Chinese Blog mixes translated report prose and explicitly
marked `KC评论` sections. `portal_english_commentary.py` now accepts only those
marked sections inside a same-day, own-canonical, KC-authored Chinese BlogPosting.
It rejects original/report routes, BBG scripts, unmarked body paragraphs, source
cards, report digests, charts, quotations/embeds and hidden content. Missing or
unsafe comments do not authorize whole-page fallback. The source admission
collector projects the English input from the same fetched bytes, with no second
crawl and no historical discovery; it saves immutable private R2 editorial
sources and provenance-bound admission receipts. English-only capture failures
remain explicitly incomplete without stalling the 33 non-English consumers.

The new candidate builder uses the existing pinned Hy-MT2 `OfflineTranslator`
and validated Memo, <=24 pages and <=14400 seconds per batch, but never enables
source-language fallback for English. Timeouts retain accepted checkpoint units
and cannot be complete candidates. Only our translated KC comments enter private
body JSON. Preview is a complete sentence of that commentary, not the original
report digest. No candidate or generated content is added to Git or Actions
artifacts/cache. The isolated roundtrip workflow adds a zero-inference English
source-restoration probe. Local editorial/source/CPU contracts: 17 passed.

The full-read API now selects an approved, checksum-bound English ledger through
the SAME active static-site release authority as the catalog. Private immutable
`ledgers/<sha>.json` and `releases/<site-release>/manifest.json` replace the
previous foundation's independent `active.json`. Missing/unapproved/cross-release
or corrupt metadata fails before quota or body access; rollback selects the old
ledger. This is implemented and locally tested, not yet a published English
release. CPU matrix/cursor, preview frontend and normal publication integration
remain required before `/en/` can be activated.

Implementation commits: editorial capture/strict CPU builder `651134ab`,
site-release-bound ledger access `9c87b918`.

## English public-preview and membership UI checkpoint

English candidates now separate `public/en/` HTML from `private/bodies/` JSON.
Only ID/title/date/preview are projected into HTML, cards, metadata and JSON-LD.
They use the same portal/Blog styles and search/date/sort/24-row pagination, but
no report/chart/original scope or source-document link. Even a complete candidate
is noindex and not a production release. No full commentary is serialized into
public files. The English route boots only the existing account/membership UI,
not the original report catalog or newsfeed.

The explicit Read action uses the existing account token with the private
no-store API. Anonymous users open the normal login; allowance exhaustion shows
the existing website membership request form. Authorized prose is inserted with
textContent, never HTML. Logout, account changes, tab hiding and pagehide clear
private text and abort/invalidate outstanding reads. There is no body cache or
automatic prefetch/free-quota consumption. The actual gateway enforces the three
distinct lifetime free reads, membership, rereads and bounded R2 concurrency.

Local checks: English source/builder 17; English public HTML 6; English client
DOM/auth/paywall 8; English gateway + version authority 23. These are synthetic
and local contract checks, not real-model semantic review or live acceptance.
The zero-inference private staging probe also restores the English checkpoint
and verifies its source-generation binding and checksum. The CPU matrix/cursor,
candidate persistence/approval and transactional publication integration still
remain to be connected; English is not online yet.

Preview/search/auth UI commit: `05d92c4d2ab3d12e8edee2eab409edcf841395ec`.
English-focused local contracts total 47 (17 source/build, 6 public HTML,
8 frontend DOM/auth/paywall, 16 gateway); existing runtime authority 7,
membership request/frontend 12, daily queue 16, incremental 21, reviewer 15,
R2 6, financial quantity 13 and shared presentation 8 also passed.
Public identity passed on 6224 files, JS syntax and changed YAML syntax passed.
No browser/live English acceptance or actual English model run is claimed.

## Verified pre-English R2 staging result

One bounded result inspection while implementing the next stage confirmed run
`36925028114` completed successfully on source
`40e3670e541a4b9e9119e83be09ecf3b25acff29`.
The queue/admission probe at `2026-10-01T20:55:54.8822124Z` reported:

- source generation: `2e7480a2fab64e8f431b87f41d09655d25c6b05aedbfb963fa7cbde7548d9e0d`;
- checkpoint checksum: `f7c97533eb7d3b8872450b011fd82da7a11d7320c08da1c6b7aa45c217e2aff9`;
- source restore, checkpoint restore, batch admission and independent cursor
  simulation: passed;
- ready candidates 0, translation calls 0, deployed false.

This was the dependency-corrected non-English queue probe. The newly added
English editorial/checkpoint probe still needs its own runtime evidence. PR #196
remains open, with base `1c1c704f2eb678dce59e83967553e03b1df053e0` at the latest
read. No merge or production activation was performed in this stage.
