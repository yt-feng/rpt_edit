# Publication handoff, 2026-09-29

The operator now requests activation of the additional non-English detail pages.
This is distinct from the prior read-only recovery test. English remains excluded.
No historic URL discovery or fresh full-batch translation is authorized by this
resume: only the exact already-started 24-page generation is eligible.

Production baseline checked: `6b0be8ab66d1a7d541df1270e169ac42ee77a337`.
PR #182 head before this work: `c85ae7004f995339bf55ae6d196cf65035be195f`.
The isolated existing worktree was fast-forwarded, then merged with current main;
the primary checkout's uncommitted work was not changed.

## Stage 1: durable recovery

`publication-resume` requires an explicit immutable daily generation and an
existing checksum-verified checkpoint for every requested locale. It discovers
no URLs, preserves the 24-page bound, and saves accepted progress and candidates
to private R2. Unlike `recovery-test`, it advances completed receipts only after
the complete candidate has been verified and persisted. It does not publish.
The operator's original two-concurrent-worker limit is restored; a 33-language
matrix is not promised to finish within one day at the maximum per-job budget.

Generation: `2b9081823e32528f402348f968d0771468dab06ea116b1a293fdf90a6621718b`.
Outstanding durable locales: `km,my,fa,gu,he,mr,bn,ta,mn,yue,de,kk`.
The other 21 locales already have complete R2 candidates from `36216968278`.
Read-only recovery `36336380713` proved 24/24 for the twelve above, but wrote
neither checkpoints nor candidates. It is not durable-completion evidence.

## Stage 2: inactive publication integration

The publication composer reads carry-forward approvals only from the captured
active release's checksum-verified R2 manifest and assembly ledger. Each new
locale also requires an explicit immutable generation/candidate map. It restores
the complete original candidate and checkpoint and reproduces the approved HTML
byte-for-byte with a cache-only translator. Cache misses are errors, not invented
translations or newly accepted source fallbacks.

After verifying unchanged source content (including links, dates, quantities and
metadata), it renders against the final inactive HTML. The new exact generation,
checkpoint and complete candidate are persisted privately; the unchanged raw
source-HTML SHA assembler verifies that new generation. No inference is used by
publication and no source SHA check is removed. Changed source content requires
a newly reviewed candidate rather than being silently reused.

Assembly now follows the established ko/ja/ar build and Chinese parity check.
It preserves their bodies and existing application assets, adds only coherent
per-page alternates, and merges approved batches across languages and dates.
The root sitemap retains its entries and adds the extended sitemap; robots
retains crawler policy and adds one sitemap line. Detailed page counts are kept
per locale. No fake language homepage is generated. Remote validation checks the
full declared detail-page set; live audit samples actual sitemap URLs. Acceptance
and rollback cover inherited pages as well as explicitly requested additions.

Local validation before dispatch: 304 Python tests passed, one skipped because
PyYAML is unavailable; 65 edge-host Node tests passed. The three changed workflows
parse with Ruby YAML and all 69 shell blocks pass `bash -n`. Public identity scan
passed on 6,035 files. Further runner and production evidence remains required;
local tests are not deployment.

## Publication gates still to satisfy

- Complete the twelve-locale durable resume, then obtain the exact candidate IDs.
- Pass PR checks on the new source revision and use the normal reviewed merge.
- Exercise the newly implemented inactive assembly on the real stored corpus.
- Preserve exact-source, complete-candidate, protected-Chinese, inactive-object,
  environment approval, atomic switch, acceptance and rollback gates.
- The initial check found only the existing protected multilingual environment.
  After the operator explicitly delegated environment setup and this release's
  approval operation, `portal-extended-locales-production` was created at
  `2026-09-29T12:12:17Z` with required reviewer `yt-feng`, matching the existing
  environment. The same-run identity variables and deployment review still must
  be recorded before activation; the gate has not been removed or bypassed.

No new language is claimed live by this checkpoint.

## Stage 3: release recovery parity

The first publication-integration CI (`36565103623`, source `3e22ffd1`)
failed the generated-recovery workflow equality test, not translation/R2 tests.
Regenerated recovery from the current release gates and fixed the related
immutable-candidate path: recovery verifies/downloads the extended ledger and
objects, derives their original identity without assembly or inference, and
requires a fresh exact-set environment approval before switching. Extended live
acceptance and rollback remain identical to the ordinary production workflow.
122 targeted Python regressions pass, including identity preservation, rejected
corruption/incomplete ledgers, and generated shell/Python parsing.

Current main `29a693066f418adf4e654c60ab5d33fa05bfca8c` was merged normally.
Durable resume `36565145888` has completed `km`; `my` and `fa` were running at
this check, with the remaining nine queued. This is not a publication claim.

The follow-up `publication-check` operation verifies complete R2 receipts and
replays their exact checkpoints against the current public source HTML. All
writes go to a unique `_extended-locales/staging/publication-RUN-ATTEMPT` prefix;
it cannot write the production candidate namespace, publish a static slot, or
invoke inference. Snapshot URLs are limited to the stored source pages and
their existing ko/ja/ar counterparts. No generated content becomes an Actions
artifact. This check is independent of, and cannot substitute for, production
approval and acceptance. A new full committed-object regression also caught and
fixed validation of localized sitemap paths: validate the source route after
the declared locale prefix, rather than rejecting the locale prefix itself.

Source `4cb023f0038ed7483ec4fe854b87bed86a3db3f9` passed 88 targeted local
checks and dispatched French staging publication check `36566608873`.
The added all-33 synthetic composition test passes too: each namespace contains
an indexable reading page, no invented homepage, no English original namespace,
and zero inference calls. This is routing/storage coverage, not a claim of
human-reviewed translation quality or live publication.
