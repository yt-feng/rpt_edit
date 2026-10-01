# Extended reading locales: shared portal UI, 2026-10-01

## Verified starting point

- Worktree branch: `codex/extended-locales-standard-ui-20261001`, based on
  current main `781b1215a536f5416b46ff934a6787391a519214`. The primary dirty
  checkout is untouched.
- Public state at 07:23 UTC: `/fr/` HTTP 200 with `Content-Language: fr`,
  `/en/` HTTP 404. The public assembly ledger contains 33 locales, each with
  24 detail pages (792 total), and no `ui_version` yet.
- Current production slot `b`, release `75851e95c44230ff2f3fc301c88008e0`,
  tree `5319648e68cc81bcd3505148c116e2eadfdf923d4f158070ed001c5aad7899cc`.
  This is the old presentation, not acceptance of these changes.

## Implementation

The publication composer now adds presentation **after** unchanged R2 candidate
checksum, checkpoint replay and exact-source validation. It preserves approved
article blocks, notices, quantities, dates, schema, URLs and carry-forward page
sets. The candidate renderer is unchanged, so old approved R2 bytes remain
reproducible. No inference, translation-provider call or historical backfill is
introduced; no generated translation content is committed or uploaded as an
Actions artifact/cache.

All 33 additional non-English locales share the existing portal/Blog styles,
topbar, account entry, full root search template and article layout. Localized
cards provide phrase search, date/type filtering and pagination. The source
catalog retains its original institution/industry/PDF filters, membership and
external-document handlers. Dynamic report/doc links use real root routes on
these pages; Chinese/ko/ja/ar route behavior is unchanged. Only approved locale
alternates appear. CSS/JS URLs carry content hashes for cache refresh.

The controls intentionally reuse source labels where there is no approved UI
translation. This is layout/function parity, **not** a claim that every control
or historical catalog title has been translated. English is excluded entirely
from this renderer; any future English surface remains text-only summaries and
secondary analysis/commentary, never original report text or charts.

New composed receipts declare `portal-shared-v1`. Pre-cutover verification checks
every declared page and the shared assets' bytes/checksums. Live acceptance
requires the full search shell, account controls, article structure and loaded
assets. Old exact-version recovery retains its original presentation; malformed
or unknown presentation receipts fail. Recovery was regenerated from the normal
production approval, acceptance and rollback gates.

## Local verification (not deployment)

- Extended Python suite: 158 tests, one PyYAML-dependent skip locally.
- Cutover workflow 39; committed-slot 24; restore 3; delegated-review 13;
  quantity integrity 13; recovery-workflow 8; offline-locale 10; offline-caller
  16; title 25 tests passed.
- Node UI tests cover phrase/Unicode matching, filters and generated report/doc
  URLs, including unchanged ko/ja/ar behavior. Existing hot-report, text-only
  access and PDF-upload suites pass.
- Public identity check passes; app budget passes (636259 raw / 138352 gzip
  bytes). Changed Python modules parse as Python 3.11. Diff whitespace clean.
- Supported in-app browser: desktop and 390px mobile French previews; actual
  approved French article preview; synthetic Persian RTL preview. No horizontal
  page overflow. Source query `Space Exploration` returns two matching preview
  reports. Localized search/empty/clear works; account modal opens without
  submitting credentials. Report URLs are root `/report.html`, not fake locale
  routes. Local preview lacks production API/config, so this does not establish
  authenticated delivery or complete live-catalog availability.

## Release handoff

Use the normal reviewed PR and production `neutral-edge-cutover.yml` flow.
For this presentation-only release use `operation=migrate` and
`translation_scope=incremental`, with no new extended candidate inputs: the
existing checksum-verified active approval ledger supplies the retained pages.
Do not rerun original article generation, model batches or paid providers.
Stop after dispatch; do not monitor. Live UI acceptance remains the Action's
transactional gate and must not be claimed from local tests or dispatch alone.

## Dispatch checkpoint, 07:27 UTC

PR #195 passed extended regression `36830215728`, public identity and release
guards `36830215701`, locale manifest regression `36830215889`, and API cost
controls `36830215628`. The optional model canary was skipped because this
presentation change needs no new inference.

PR #195 merged as `1b8bd957443fc915d5d9a8ad2da30aa8eebe5d09`.
Production Action `36830465900` was dispatched with `operation=migrate`,
`translation_scope=incremental`, and no new extended candidate inputs. Its
resolved source SHA matches that merge. Dispatch returned the run URL; the
immediate receipt showed `pending` behind the existing release lock. No
post-dispatch monitoring or live UI acceptance was performed. The active
production version recorded above remains the last verified baseline.

## Completed production acceptance, 2026-10-01

After the later user continuation, Action `36830465900` was verified completed
successfully on the reviewed merge SHA above. Approved R2 restore, immediate
pre-cutover committed-tree verification, deployment, live acceptance, extended
page audit and transactional outcome all passed. Cutover completed at
11:11:38 UTC. No run was cancelled or restarted during this acceptance pass.

Current public edge state is slot `a`, release
`05b97d1fc4a394a836e68e393da3a3be`, tree
`5ed5c084172bd65fdd61fab84afbc65ce62ffd57f470e854c71dd1dfa16bf855`.
The public receipt declares `portal-shared-v1`, retains all 33 locales with
24 pages each (792), and records 33 verified checkpoint replays with zero
additional translation calls and zero paid-provider requests. This is retained
approved content, not evidence that later daily articles are fully translated.

A separate live audit using `--locales all-supported --require-standard-ui`
passed all 33 homepages, their sitemaps, 66 detail samples and the seven shared
assets. Browser acceptance passed French desktop/mobile home and article,
Persian RTL mobile home and article, real language-switch navigation, local
search/empty/clear, source-title phrase search and the existing account modal.
The full catalog loaded 14639 reports; `Space Exploration` returned 18 reports
with real root `/report.html` URLs. Desktop 1280px and mobile 390px checks had
no horizontal page overflow. No credentials were submitted. The temporary
viewport override was reset and the temporary tab closed.

English remains excluded: `/en/` returned HTTP 404 and no English alternate
was present on the tested Persian home. The future text-only summary and
secondary-commentary contract remains unchanged; no original English report
text or charts are introduced. Source-label UI fallback is still present, as
described above; this release completes shared layout/function integration,
not full UI-string translation or authenticated delivery acceptance.

Content-free hashes, all per-locale counts, checkpoint replay identities and
live URL/sample results are in
[extended-locales-ui-evidence-20261001.json](extended-locales-ui-evidence-20261001.json).
The implementation is merged and deployed; this acceptance record is a
separate documentation-only checkpoint.
