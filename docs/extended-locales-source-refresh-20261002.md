# Source-following locale correction — 2026-10-02

## Evidence and cause

Main baseline: `c3fc24e1a198bb86225427b04c7b771a4c589840`.
Production release run `37030273283` published release
`df17093f8d52e36d06c5495d5e708584`, slot `b`, tree
`fa448645fe94327d83fac18ffdb84972ac93e43a96c95215b63859ad23501d73`.
Its 33-locale audit passed with 24 detail pages per locale (792 total), still
the September 26 batch. This is not evidence of current-day coverage.

Source consumers `36974450033`, `36988463947`, and `37044089040` completed
successfully but selected zero pages. The first two selected October 2; the
last selected October 3 in Asia/Shanghai after a long production release.
The current eligible source inventory's latest ordinary Blog/report day is
October 1. October 2 BBG pages retain their separate reviewed language scope.
Unlike ko/ja/ar's source-change build, the new pipeline discarded the latest
eligible source just because its date differed from the runner's calendar day.

## Implemented correction

- Admit only the newest available eligible source day. No archive traversal to
  fill a batch. Page-owned publication dates remain mandatory; sitemap lastmod
  is only a fetch hint. Never rewrite a publication date.
- Pin the active release before and after collection. Freeze the bounded source
  inventory and its release identity in private R2, bind the exact corpus and
  capture date to a versioned receipt, and verify its checksum again on restore.
  Retain legacy receipts; refuse backward source-day movement.
- Keep explicit KC editorial extraction on the very same source bytes. English
  review checks the original source admission, including its actual capture
  job, repository, attempt and commit. Originals/charts remain excluded.
- Register admitted batches for publication in the serialized source job before
  starting concurrent locale workers. Complete but unpublished results remain
  discoverable after midnight and after completed translation cursors are
  pruned. No concurrent whole-queue writer is added to locale workers.
- Continue the existing approved-locale ledger, inactive build, required review,
  exact version checks, cutover and rollback. CPU concurrency remains two, each
  batch at most 24 detail pages, each locale at most 14,400 seconds. Production
  translations remain fixed-model Actions CPU only, with no translation bodies
  in Git, Actions artifacts or caches.

## Validation and completion boundary

Local targeted regressions: 202 Python and 16 gateway JavaScript tests passed.
They include late capture, stale lastmod, changed release, 500-source/24-batch
bounds, private checksum/permission errors, legacy admission compatibility,
cross-day pending publication, English original/chart exclusion and account
quota/member rules. Generated recovery matches the production gates; public
identity and whitespace checks pass.

A read-only live sample of the newest ordinary Blog source successfully yielded
one explicit KC-comment block, with the original October 1 date. No translation
or production write was performed by that diagnostic. Real source admission,
CPU completion and publication remain separate Actions results; a passing or
dispatched workflow is not automatically an English live-page acceptance.
