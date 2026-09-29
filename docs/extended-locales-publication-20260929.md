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

## Publication gates still to satisfy

- Assemble against the exact final inactive Chinese source bytes, with existing
  ko/ja/ar alternates preserved after their build.
- Carry forward approved language pages and sitemap/hreflang across refreshes.
- Detail-only source batches must not require or invent language homepages.
- Preserve exact-source, complete-candidate, protected-Chinese, inactive-object,
  environment approval, atomic switch, acceptance and rollback gates.
- The repository currently has a protected `portal-multilingual-production`
  environment. `portal-extended-locales-production` is not yet configured; do not
  let its first workflow reference silently create an unprotected environment.

No new language is claimed live by this checkpoint.
