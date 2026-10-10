# Retained title revalidation without model requests

Read-only production inspection `38057694359` confirmed the report-38 failure
from generation run `38056186143`: all 12 actual model candidates had no English
word of ten letters; deleting spaces introduced such a word in all 12. Examples
of the same generic defect are `Apple Watch` becoming `AppleWatch` and
`AMD Instinct` becoming `AMDInstinct`. Both title cleaners now retain one space
between ASCII letters or digits. Other Chinese/punctuation spacing stays compact.
The long-English, English-ratio, source-anchor, acronym, numeric, sensitive-word
and length gates are unchanged.

The repaired cleaner changes the normal generation contract. Ordinary generation
therefore must not reopen report 38 against its old four-request checkpoint.
`revalidate-saved-article-titles.yml` instead authenticates the original Daily,
successful OCR-page source job, and exact failed standalone recovery job. It
accepts only the separately diagnosed archive SHA/size, context, old generation
contract, report-38 body/prompt/source hashes and progress receipt hash.

The reader verifies the retained progress schema, exact source identity, every
response hash, one completed body and at most four completed title requests. Any
pending request blocks revalidation. Actual saved title responses alone supply
candidates, in the same newest-repair-first order used by generation. An old
emergency selected title is never added as a model candidate. Selection,
neutralization, title-quality, required-acronym, article-quality and editorial
binding gates must all pass; deterministic quality fallbacks do not grant reuse.

`inspect` downloads through the bounded read-only R2 adapter and builds a local
candidate. It makes zero provider requests and zero object writes. Its public
artifact includes only fixed categories, counts and hashes. If the candidates
remain unready, the original archive is untouched and no new title request is
allowed.

`apply` repeats those checks under the same source concurrency key as normal
article recovery, rechecks the pinned remote archive, and writes only after full
44-article validation. Only report 38's H1/title/decision/binding may change;
the remainder of its Markdown, all source/prompt/assets, the other 43 articles,
and all old Progress identities/request/response bytes are preserved. A private
`title-revalidation` proof binds the old contract, context, source, response IDs
and hashes, validator files, body-without-H1 hash, before/after status and article
hashes, and complete receipt. The proof stays outside the article handoff.

Successful apply archives the full private generation checkpoint and separately
the complete article handoff. These are two verified object writes and zero
model requests. A write failure reports an unknown completed-write count and its
attempt count; it does not resubmit any model request. The operator then dispatches
the existing standalone **Recover report article delivery** workflow with the
same original/source run IDs, date, count and `upload_wechat=true`. Its complete
receipt path reuses all 44 articles and proceeds to WeChat readback and Blog
publication. Keeping that standalone workflow preserves the historical locale
admission contract. Full WeChat/Blog/locale acceptance remains separate from
successful revalidation and must be checked from their own receipts.
