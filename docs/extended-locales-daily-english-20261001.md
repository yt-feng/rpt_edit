# Daily reading locales and English editorial access

## Latest bounded inspection: publication review pending; GitHub connection stopped

On the next continuation, the initial GitHub reads succeeded. PR #199 was
OPEN/UNSTABLE at exact head `f3d297f001567baef0bd82cc0f9e67bf54215122`, base
`8f0591de260c17b2c51b5e15909a6fe9e9ab9d5e`. Its API cost control check
`36932015952` had succeeded; offline regression `36932015946`, locale manifest
`36932015880` and public identity `36932015913` were still in progress.
Publication-branch R2 staging `36932057105` was in progress at that exact PR
head. Main incremental run `36932060676` was pending at the exact base above.
These are bounded snapshots, not monitoring, and are not terminal results.

The original main CPU run `36801745121` still had real active job handles:
`locale (bn)` job `110177656037`, and `locale (ta)` job `110177655990`.
Of its 33 locale jobs, 24 had succeeded, one Khmer job had failed with the
previously confirmed timeout, two were running and six were queued
(`uk,bo,kk,mn,ug,yue`). Job success is not a count of approved/live new pages;
per-page R2 candidate evidence and new-day production coverage were not read in
this continuation. Existing checkpoints and running jobs were not canceled.
An initial listing showed release run `36893120105` had succeeded on main
`1c1c704f2eb678dce59e83967553e03b1df053e0`; its exact activated release/tree
and live page counts were not inspected here.

A subsequent exact merge-gate read failed with `connect: no route to host`.
The chained command stopped before any additional API call. In compliance with
the operator instructions, ALL GitHub/Git network operations stopped: no
transport/remote changes, proxy/DNS/route inspection or alternate connection
path was attempted. No PR merge, publication opt-in change, new dispatch or
production activation occurred in this continuation. English remains unaccepted
for production. Resume from verified current GitHub state on a later user turn;
do not assume any of these formerly running handles has finished or restart one
merely because observation failed. This evidence record is saved locally only.

## Current checkpoint: English CPU merged; publication and recovery ready for review

PR #198 passed regression, API cost controls and public identity and was merged
normally at `2026-10-01T21:51:52Z`. Main merge commit:
`8f0591de260c17b2c51b5e15909a6fe9e9ab9d5e`; reviewed CPU head:
`cc4d0e0e81e989d531ede7d582a5f7c0d0314428`.
The isolated publication branch has implementation commit
`c0d76c42b111d475fa2040593f4c0f1c2aa553d9` and a normal merge of this main
baseline, `a93ecd53bf84fe92b9ae0c7dfe7197d04c7d96f3`.

One bounded merge-gate check confirmed R2 staging run `36929230502` succeeded
on the reviewed CPU head. Its new English same-capture/incomplete-candidate
probe at `2026-10-01T21:32:34.0346865Z` recovered source generation
`21ed924ede84a9305da72831c7c2d9262aec4e6987cfc75f3d8ed25d99b93fc7`
and immutable checkpoint
`0d7eba10d545e3f8d7a2ba6187a1ac22cbda069429013128c77dc797aefd9974`.
Same-capture restoration, immutable checkpoint restoration, timeout cursor
restoration and incomplete-candidate refusal all passed. Ready candidates 0,
translation calls 0, paid-provider requests 0 and deployed false. This is
isolated synthetic storage evidence, NOT an English production translation.
The earlier source/checkpoint and 33-locale cursor probes also passed.
API Worker deployment `36929237340` succeeded on foundation main
`a5c851494cf6100b1792806bae29df1092d3e185`. This is an API deployment result,
not English-page publication or live authenticated reading acceptance.
Source-admission run `36929217861` succeeded on that same foundation; its
success alone does not establish a newly translated or published page count.

Publication is now implemented in `portal_english_publication.py`, with a
separate complete-candidate handoff and exact required-reviewer integration:

- Reconstruct every body from the immutable admitted KC editorial source and
  verified Hy-MT2 candidate. The full body stays in private R2; only title,
  preview and date reach public HTML/JSON-LD. No report originals, charts,
  documents, source digest or full-body JS state is copied to English pages.
- Retain ALL previously approved English batches and rerender safe previews
  without inference. New KC commentary must still match the current inactive
  Chinese source section. Empty days create neither fictitious pages nor a
  navigation link. Non-English sitemap/hreflang and training policy stay intact.
- Bind the exact private ledger to the 32-hex active site release only AFTER
  the existing required environment approval, exact SHA/tree/handoff checks
  and committed-slot verification. Carry-forward may reuse an unchanged
  approved ledger, but cannot admit new unapproved content.
- Verify public English bytes, language headers, API/static ledger identity and
  anonymous full-read denial after cutover. Rollback restores the corresponding
  previous site-selected ledger, including the pre-English 404 state.
- Regenerate the original recovery workflow through its generator. Recovery
  keeps the uploaded static bytes and original candidate commit, restores the
  complete R2 evidence and requires fresh protected approval; no models or
  public uploads. English pre-deployment failures and verified English rollback
  now have bounded recovery classifications; missing/order-invalid proof fails.
- English joins the SAME two-worker CPU queue. New publication opt-ins
  `PORTAL_ENGLISH_AUTO_PUBLISH` and `PORTAL_ENGLISH_AUTO_REVIEW` remain disabled
  until the publication code itself passes normal review/merge. Existing
  required reviewers are never removed or bypassed.

Local validation: 663 Portal tests (662 passed, one optional PyYAML-dependent
test skipped locally; Linux CI installs PyYAML), 52 exact candidate-restoration
tests, 39 cutover-workflow tests, 24 committed-slot tests, 13 quantity-integrity
tests, 39 offline model/runtime tests, 7 translation-comparison tests, 16 offline
caller tests and 92 JavaScript gateway/UI/edge tests passed. English publication
23 and generated recovery-workflow 9 are included in the Portal suite. All four
changed workflows parse with Ruby YAML; generated recovery matches its current
production gates. Public identity passed on 6230 files. Legacy translation
tests use mocks/synthetic fixtures, not real paid or production model calls.

English is still NOT online. Real complete CPU commentary, protected publication
on reviewed main and live signed-in allowance/member acceptance remain required.
The last accepted 33-language baseline has 24 approved details each (792 total);
that historical baseline is not proof of today's coverage. This checkpoint has
not inspected or claimed new completed-page counts. The dirty primary checkout
is untouched. Dispatch receipts are reported separately; no Actions monitoring
or workflow cancellation is part of this stage.

## Earlier checkpoint: reviewed foundation merged; English CPU stage submitted

PR #196 was merged through the normal passing-check flow at
`2026-10-01T21:22:05Z`; main merge commit is
`a5c851494cf6100b1792806bae29df1092d3e185`.
Its head was `7db183a750b41e43979c39f98db4e0dc1d5523fe`.
The main source-admission hook and the 33 independent daily cursors are now
merged. This activates the code path, not a claim that today's translations have
all completed or reached production. Existing approved pages remain intact.

One bounded result inspection confirmed these completed checks on that head:

- offline regression `36926892315`: success;
- API cost controls `36926892309`: success;
- public identity `36926892350`: success;
- dispatched credential-free regression `36926924838`: success;
- isolated private R2 staging `36926954981`: success.

The English staging result at `2026-10-01T21:12:13.3915043Z` restored editorial
source generation
`b0ab22c6138f275704edfc27e5fee9ca80187197dccc6181e2dbcc3fabde165c`
and English checkpoint checksum
`047e8ee6657c345a233ea85f8d2f1b35d8e6608c78fdf59010d8a2012eee00b6`.
Editorial source SHA-256 was
`dbc729da4c3f8ec73e68e7751357a9bbcbb4c914c291b186e1a9b67e46c54cc8`.
Source/checkpoint restoration passed; ready candidates 0, translation calls 0,
paid-provider requests 0 and deployed false. It was synthetic storage evidence,
not a locally produced or approved English translation.

The next isolated branch is `codex/english-commentary-cpu-release-20261001`.
CPU/persistence implementation commit:
`2fdd95e86cc53c5c715edb0fae9c869a8c62330f`.
English now joins the SAME max-parallel-2 CPU matrix; its own private source
generation, completion cursor and checkpoint namespace are independent of the
33 non-English locales. English inference requires reviewed main/public Linux
Actions and the existing fixed Hy-MT2 runtime. Source fallback is never enabled.
No English translation failure changes the non-English approval locale set or
prevents otherwise-ready non-English candidates entering the existing release
handoff.

Candidate readback verifies original capture producer/day/HTML hashes, exact
admitted editorial subset, model identity, private body quantity/script checks,
all object checksums and preview-only public HTML before writing READY.
Timeouts persist incomplete candidates and immutable memo snapshots, leave
the cursor unfinished and never create READY. An unchanged failure cannot
self-dispatch indefinitely. Complete candidates remain noindex and unpublished.

Before marking English work complete, the ready candidate is durably retained
in a separate private pending-publication queue. Finished source days can then
leave the bounded translation queue without deleting their sources, checkpoints
or unpublished candidates. A completed day without that verified durable work
cannot be dropped. Seed recovery follows the content-addressed checkpoint
snapshot, not a mutable per-generation latest pointer.

Local targeted contracts: English source/build 18, English pipeline 21, daily
incremental 28 and source queue 16 passed (83 total). Broader offline, financial
quantity, carry-forward/approval/restore and existing locale regressions passed.
JavaScript preview/auth/gateway/edge suites: 92 passed. Public identity passed
on 6226 files. Changed YAML was parsed with Ruby; one optional local PyYAML test
was skipped because that dependency is absent, while Linux CI installs it.

The expanded staging operation now checks same-capture source admission,
immutable empty-checkpoint recovery, timeout cursor recovery and refusal to
restore an incomplete candidate, with zero inference and zero ready candidates.
It still needs a new Actions result on this CPU-stage commit.

English is NOT online. Normal protected publication still must assemble safe
previews, preserve previously approved English batches, populate the private
ledger/body release manifest selected by the active site version, and bind its
approval/cutover/rollback to the exact prepared tree. No production approval,
release manifest or original-report English page is fabricated by this stage.
The dirty primary checkout and the last accepted production version are untouched.

The sections below retain earlier implementation checkpoints; their old open-PR
or running-workflow statements are historical, not fresh runtime status.

## Reconciled baseline

Work continues from reviewed main `1c1c704f2eb678dce59e83967553e03b1df053e0`
in the existing clean isolated worktree. The dirty primary checkout is untouched.
All 33 non-English locale roots already use `portal-shared-v1`; the preceding
production acceptance retained 24 approved articles per locale (792 total).
That does not prove daily-new-content coverage.

At the pre-merge snapshot, daily producer `36801745121` was still working: completed
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

## Daily queue implementation (subsequently merged in PR #196)

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

At this earlier checkpoint, PR #196 was open, not merged.
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
English editorial/checkpoint probe needed its own runtime evidence at that
checkpoint; it subsequently passed as recorded above. PR #196 was then open,
with base `1c1c704f2eb678dce59e83967553e03b1df053e0`. Its subsequent merge is
recorded at the top; no English production activation is claimed.
