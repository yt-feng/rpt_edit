# Saved title evidence diagnostics

The read-only revalidation run `38058997093` used the unchanged private generation
archive `4e645b5f6ed6bb0536b9fe8f2a6a99ab3b8dab851dba0297981a5e9755f89ab7`.
It confirmed 43 bound articles, four completed title responses for ordinal 38,
zero pending requests, zero provider requests and zero object writes. The English
word-boundary repair removed the long-English defect, but the saved candidates
still failed other existing gates. No apply or downstream delivery was authorized
by that result.

The additional `saved_candidate_evidence_diagnosis` field is observational. It
preserves the same source authentication, complete source inventory, archive,
context, old Progress identity and response hashes. Its source evidence is the
exact `source_ocr.md` bytes already verified against the incident file pin; an
unverified source never reaches this diagnostic.

Each saved response/candidate ordinal reports fixed quality codes and counts for
raw text, cleaning without the length limit, and normal 35-character cleaning.
Required-acronym and numeric-token losses distinguish normalization from length
truncation. It also reports the number of base-valid candidates and whether the
existing selector's anchor came from a saved candidate or a fallback.

For additions relative to the unchanged newest-first faithful candidate, fixed
categories distinguish numbers, known names and contrast terms. The diagnostic
uses the existing token extractors and hook-support helpers to count support in
four evidence windows: filename alone, the selector's unchanged 2,200-character
article excerpt, the complete saved article, and the verified source Markdown.
This distinguishes a genuinely unsupported claim from evidence outside the
selector window. Titles, terms, numbers, names, source filenames, body sentences,
exception text and provider responses are never emitted.

Larger evidence windows are only observations. They do not select a different
title, reorder candidates, add an alias, weaken a quality gate, replace the
selector's evidence, authorize a fifth request, or authorize publication. A
synthetic regression demonstrates the possible shape of a base-valid anchor
rejected for a number beyond the excerpt; the next real inspection must determine
whether this explains ordinal 38. Actual 44-report delivery and WeChat/Blog
acceptance remain pending while revalidation is not ready.
