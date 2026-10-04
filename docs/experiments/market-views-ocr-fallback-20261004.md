# Archived Market Views OCR fallback experiment

Archive status: preserved and unchanged. The original patch has not been deployed
as written; current cloud fallback development selectively reused source ideas
and added stronger validation, cloud dependencies and rollout controls.
The production architecture remains **MinerU API + GitHub Actions**. This archive
does not introduce a dependency on the user's computer.

`market-views-ocr-fallback-20261004.patch` restores the original eight-file experiment
against commit `b45c436515be3ecbea7c75dba4cd19deed9095db`. The temporary patch had
disappeared; this copy was recovered by replaying the original fourteen recorded
file edits, in timestamp order, in an isolated directory. Production source files
were not changed when this archive was recovered. The patch contains source code only, without PDF bytes,
credentials, provider responses, or signed result URLs.

The experiment adds a schema-2 source receipt, readable native text with full-page
Tesseract OCR at 300 dpi (`eng+chi_sim`) for unsupported pages, original page
images and extraction provenance, verified all-white pages, and preserved
duplicate-file aliases with one summary per unique PDF content. Its proposed
workflow dependencies install Tesseract language data on GitHub Actions runners.
The archived test suite contains 23 extraction tests; earlier fixture checks
passed, but complete real-report acceptance did not finish.

Do not enable this patch without addressing the real-report findings:

- 21 of 54 examined reports had a first-page native text layer consisting of a
  short opaque character string. The character-count check incorrectly accepted
  that text as readable; native readability needs a stronger gate.
- OCR on an actual financial table lost decimal points and altered some numbers.
  Preserving the page image and provenance does not establish numerical accuracy.
  Table extraction needs an accuracy check before those values reach summaries.
- The full 54-report extraction was interrupted, so this archive does not prove
  a complete source handoff, generated Market Views PDF, or publication.

Any future rollout should first verify these cases in cloud CI and then verify
the exact issue date, complete original-file coverage, generated PDF contents,
private archive, and public catalogue entry. Keep MinerU as the primary route and
document the actual fallback deployment state in `docs/pipeline-overview-v2.md`.

Patch SHA-256: `bae288911461600b80459c40df9c57f71b4963a8c4cf62bb4f5aa98c1258729d`.

## Current cloud implementation and acceptance

The current extension in `scripts/extract_native_market_sources.py` keeps the
original patch separate and adds explicit OCR switches, full cloud source context,
readable-language checks and consumer verification. `scripts/ocr_numeric_evidence.py`
compares positioned numeric reads and original punctuation pixels, retaining
uncertain fields as explicit markers. `scripts/audit_market_views_ocr_receipt.py`
can emit sanitized coverage and numeric/value-position fixture acceptance after
checking the complete private source contract. Raw text and page images remain
private.

The manual recovery can run with `enable_ocr=true` and `generate_pdf=false` to
review the complete private source handoff without model calls. Real Tesseract
regressions are mandatory in cloud CI; missing language models fail instead of
producing a skipped green check. Daily backup remains off unless
`MARKET_VIEWS_OCR_BACKUP_ENABLED=true` is set after full real-report, PDF and
publication acceptance. This development record does not establish that any
missing October issue has been delivered.
