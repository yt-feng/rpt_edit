# Extended locales R2 progress

This checkpoint records implementation and verification state only. Generated
source, translations, checkpoints, candidate HTML and credentials stay out of
Git.

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
