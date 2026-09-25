# Extended locales R2 progress

This checkpoint records implementation and verification state only. Generated
source, translations, checkpoints, candidate HTML and credentials stay out of
Git.

## 2026-09-25 Four-hour, today-only incremental scope

Implementation commit: `e64a21707d598dfe9898ad738b6ef790349d5c7d`.

The operator superseded the former 40-minute/mixed-24-page batch with up to four
hours per language and **new content only, no historical backfill**. The current
workflow defaults to 14400 translation seconds and a 270-minute job limit; the
30-minute difference covers setup and durable checkpoint/candidate persistence.

Selection now uses the current Asia/Shanghai date and the page's own publication
date (Article/BlogPosting/NewsArticle/Report). Only detail pages published on that
date enter the batch. Homepage/About/institution/topic directories and historical
recommendation lists are not translated. A refreshed sitemap date is not enough
to admit an old report. Unknown dates are skipped. 24 is a maximum, not a required
count. No new content means no model job. The launch floor is 2026-09-25.

The new incremental orchestration reuses the existing R2 client and secret names:
private per-locale daily completion receipts skip unchanged pages; immutable,
SHA-verified memo snapshots seed exact source/model/locale units across source
generations. Reused units are validated again and only used rows enter the new
generation-bound checkpoint. Incomplete candidates never advance completion
receipts. Later same-day invocations deterministically take the next pending
up-to-24 pages; previous dates are not revisited.

An automatic workflow_run hook follows successful same-repository/default-branch
`Neutral edge catalog refresh` runs. It defaults to French; explicit non-English
expansion uses `PORTAL_EXTENDED_INCREMENTAL_LOCALES`. This becomes active only
after PR review/merge to main. It creates private noindex candidates, not a live
release. Fixed-source release integration and approved-page carry-forward remain
separate, uncompleted publication work.

Cancellation was requested for old run `36085380192`; no terminal-state polling.
The former mixed-directory source generation will not be resumed. Local checks:
265 Python tests passed, 1 skipped (PyYAML unavailable); both changed YAML files
and all 15 shell blocks parsed using Ruby YAML and bash -n. A read-only live
sitemap sample timed out locally; no networking changes or retries were made,
so the real today-only page count remains for the dispatched runner to establish.

## 2026-09-25 French budget exhaustion and fixed-generation continuation

Run `36076945440` used code SHA
`8c62f69998acdcaf1ebda703b97e18cc124f2221`. Source restore, checkpoint restore,
pinned model setup, bounded translation, checkpoint persistence and candidate
persistence all succeeded. Only the final incomplete-status step failed, with
exit code 75 after the configured 2400-second budget. This is not a storage or
English-exclusion error and must not be relabeled a completed candidate.

- French completed pages: **1/24**; failure_count=0, budget_exhausted=true.
- New model calls: 322; cache hits: 40; exact-source fallback units: 251
  (271 uses). These are unit-level statistics, not completed-page counts.
- Restored checkpoint: 81,992 bytes, SHA-256
  `cba1d08b0c9ef8dd1ec2396874b0ef94e17d86b31c4ff3f68094c34819a3036c`.
- Saved checkpoint: 181,254 bytes, SHA-256
  `a25949c64d512c8e7f1422f0f15741b00c18e7e50dfdca06a1fc717511e8c297`.
- Candidate `9503241e9996397d775c5ea9752b2973f1c1ca2cfe584b8c08a28f86f5de873b`
  remains private, incomplete, ready=false; manifest SHA-256
  `d38cd42fba9af9ed8c3cf6aa7195a9538054bc5aaa6b5e80642d8e5e1631d9a0`.
- Source remains
  `f334aac3023978818d18a4d28ed16cb2541a7b9b6ea803021f1fcd0502c812aa`.

Latest main checked: `e17250b8` (archive/catalog-only changes since the prior
check). PR #182 still points at the source above. No translator, model, approval
or completeness gate change is needed for this outcome. Dispatch one further
French-only 2400-second batch with the same source and source-fallback policy,
restoring the durable unit checkpoint; do not restart source collection, expand
the language set, monitor, auto-repeat or claim publication. Another budget
exhaustion must remain explicitly incomplete and may require a further resume.

## 2026-09-25 English summary-only scope correction

The operator excluded English from full reading-page expansion: English remains
available for text-only summary/interpretation use: no original/full report text,
no embedded charts and no English Charts entry. This change does not create an
English summary publisher or modify the Chinese/ko/ja/ar chart surfaces. `ADDITIONAL` now
contains 33 non-English targets; selection, generation and candidate verification
reject English, including old English candidates. Workflow defaults and bounded
model-canary targets now start with French; the model language registry is intact.

Cancellation was requested for English run `36075707981`; its terminal state was
not polled. The next dispatch is French only, 24 pages, 2400 seconds, restoring the
existing fixed R2 source/checkpoint with exact-source fallback enabled. No monitor
or production deployment is requested. Earlier evidence below remains historical.

Local verification of this scope correction: 248 Python tests passed, 1 skipped
(PyYAML unavailable). Contracts cover explicit/all-supported English exclusion,
zero-inference/no-output rejection, old English candidate rejection and approval
rejection before any R2 access, while preserving English model/summary capability.

## 2026-09-25 architecture and source-fallback correction

The current architecture audit is in `extended-locales-architecture-audit.md`.
PR #180 and #181 have merged; PR #182 carries the next translation correction.
Main was refreshed to `681eae64969bfe2c39aa802dc7d4f4e7eadb5424` in the isolated
`codex/extended-locales-r3-20260925` worktree. The primary dirty checkout was not edited.

Following the operator's explicit acceptance of translation imperfections for
SEO/GEO, additional locales now support the same exact-source fallback policy
as ko/ja/ar. Rejected model responses are discarded; accepted translations and
source-fallback decisions occupy separate checkpoint maps. The candidate
manifest reports both page completeness and actual translation completeness.
The outer repeated retry was removed; fallback mode uses one model attempt per
new unit and reuses decisions on resume. Pipe validation, model request deadlines
and established-locale URL assembly were repaired without changing providers.

Local verification: 287 Python tests passed, 1 skipped (PyYAML absent); all 27
edge-static-host tests passed. Public identity audit and `git diff --check` passed.
No production deployment is claimed. Fixed-source publication integration,
carry-forward across later batches and deterministic archive cursors remain
explicitly documented gaps. The requested stop point is dispatching the next
24-page French candidate (2400 seconds, fixed existing source, source fallback
enabled), without watching Actions or installing a monitor.

The remaining sections are earlier checkpoint evidence, not the latest PR status.

## Committed implementation

- Branch: `codex/extended-locales-r2-20260924`
- Implementation head: `d9cf575de6817ef5afcacd0e60b25470c1cf1261`
- PR: `#180`, ready for review; the branch contains the R2 persistence layer,
  resumable per-locale checkpoints, bounded two-at-a-time Actions execution,
  candidate assembly gates, locale response headers and regression coverage.
- Production translation remains pinned to the existing Hy-MT2 CPU action. No
  paid-provider or manual-translation fallback is present.
- The latest source generation is
  `f334aac3023978818d18a4d28ed16cb2541a7b9b6ea803021f1fcd0502c812aa`; its
  restored corpus is 461,257 bytes with SHA-256
  `36693cde44ad685bef6cdc89e90cd23d64f5ef21975f4f85175452b0ccf53857`.

## Checks passed

- Local suite: `278` tests passed, `1` skipped; `git diff --check` and Python
  syntax compilation passed.
- PR #180 audit, regression, locale, workflow and Ubuntu 22.04/24.04 real CPU
  checks passed at the implementation head.
- R2 private round-trip Actions run `36002784789` passed on
  `85ab68a06242140967d490d73f768726209422d5`. Its isolated prefix was
  `_extended-locales/staging/roundtrip-36002784789-1`; the 79-byte readback
  receipt SHA-256 was
  `ed595ebe90a93c9db028b0a0d06ebf1418f5a32c4236c14bcc6e52ef9557a4ec`.
  The deliberate permission probe was classified as `R2PermissionError`.

## Candidate runs completed, but not publishable

- `en`, Actions run `36035913434`: `1/24` pages completed, 23 failed closed;
  candidate `e0202939a30ffd63774511aad7481add6691f48b549350c98d7a3333ce6d016e`,
  manifest SHA-256
  `f47511af4d8d849c1acc65758a65b4dfd7fbac2c90b869683f1538b693d81549`,
  `ready=false`, `paid_provider_requests=0`.
- `hi`, latest Actions run `36044306006`: `0/24` pages completed, 24 failed
  closed with `offline-quantity-validation`,
  `offline-target-script-validation` and `table-structure-validation`.
  `budget_exhausted=false`, `paid_provider_requests=0`. The resumable
  checkpoint read/write remained 58,963 bytes with SHA-256
  `d495e462a04acf1068ccdf0c552053df0d5e7b3e49e04e61bba6c173b6222b28`.
  The incomplete candidate was
  `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`, with
  manifest SHA-256
  `da31b53ecd05b2c3b14b6cb79b7c2d2168efe76ddd5389989b8e4f0ea52b0830`,
  `ready=false`, `uploaded_object_count=1`.
- These runs are completed evidence, not successful publication runs. No
  incomplete candidate receives a ready receipt or enters assembly.

## Production boundary

- Existing production release path was previously verified by successful
  neutral cutover run `36011627290` on `ceb7eddf9f06bd84359e9440eccd3574c536f1d1`.
  Live edge state reported release
  `7fccdbdcb150731382c30397e74ed9a2` and tree SHA
  `966625402781f142b94d7db608508c0f79de4f0ae463f3eb2cbc9d974aaa113d`.
- Existing `/`, `/ko/`, `/ja/` and `/ar/` pages were live; `/en/`, `/fr/`,
  `/pt/` and `/zh-Hant/` remained 404 because they are not approved releases.
- No new locale has been assembled, approved, switched, indexed or published.
  Existing Chinese, Korean, Japanese and Arabic behavior, permissions, source
  checks, publishing locks, approval and rollback paths remain unchanged.
