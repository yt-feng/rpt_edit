# Global offline SEO/GEO locales

## Scope and verified boundaries

The canonical registry contains the Simplified Chinese root and 37 supported
mirror variants (34 additions to ko/ja/ar). Registration does not imply that a
language is translated, published, reviewed or indexed.

The preparation cohort contains 35 mirrors / 32 additions. Kazakh (`kk`) and
Mongolian (`mn`) remain registered for diagnostics but are held from preparation
and R2 candidate upload. Both the pinned 1.8B model and a separately evaluated
official 7B Q4_K_M model produced wrong or mixed scripts for these configurations.
The 7B experiment is not a production dependency. Do not accept its superficially
successful script checks as proof of correct language output.

`ready` and `ready-new` select the explicit preparation cohort. Explicit held
targets fail before translation. A manual preflight with `targets=all` still
checks all 37 mirrors and returns failure for rejected outputs. Ordinary PR
checks validate the eligible cohort plus tests proving the held languages
cannot be prepared or uploaded as publication candidates.

Qualification covers public prose, financial rates and protected references.
It does not establish native-speaker semantic accuracy across all site content;
`semantic_review` stays pending and `production_ready` stays false.

## No additional paid translation requests

Inference uses the existing immutable Hy-MT2 1.8B Q8_0 model and portable CPU
runtime on standard public Ubuntu GitHub Actions runners. All model/runtime
checksums remain pinned. OpenCC 0.1.7 performs exact local Simplified-to-Traditional
conversion without a model call. English content requiring translation still
uses the pinned local model.

The new language path injects no DeepSeek/DeepL key and has no paid fallback.
Missing dynamic overlays show a native explanation and a Chinese entry instead
of silently invoking the legacy paid translator. Existing research APIs unrelated
to this multilingual lane are not disabled.

## Cloudflare storage

Generated public source projections, accepted translation checkpoints and
complete candidate trees are stored in the existing Cloudflare R2 bucket under
`portal-global-locales/v1/`. Stable object keys avoid accumulating a full new
website artifact for each run. This lane does not store translated website trees
or translation checkpoints in GitHub artifacts or Actions caches.

GitHub continues to hold source code, ordinary logs, small diagnostic receipts,
and fixed-key public model/runtime dependency caches. Public standard-runner
compute is free; storage and operations still follow each platform's billing
rules. No account-wide or Cloudflare storage zero-cost claim is made.

R2 reads and writes verify byte counts, SHA-256 metadata and upload readback.
Only genuine missing-object responses become empty caches; permission/service
failures remain errors. Archive unpacking rejects traversal, symlinks, duplicate
members, noncanonical paths and size expansion. Checkpoints are capped at 8 MiB,
compressed handoffs at 256 MiB and source trees at 2 GiB. Model/provider/language
identity must match before a checkpoint is accepted.

## Incremental preparation and publication

`portal-global-locale-prepare.yml` runs separately from production deployment.
Its six-hour schedule rotates at most six eligible new locales, with two standard
CPU jobs in parallel and a 300-second per-locale inference budget. Manual runs
select `ready`, `ready-new`, or eligible canonical codes and a 30-1200-second
budget. Exact-source accepted translations survive the next run through R2.

Public source preparation uses a bounded 32768-entry short-string normalization
cache and a 900-second subprocess timeout. It builds only repository public
inputs, without private chart/Hot overlays or original article-generation reruns.
Original English legal pages remain root documents, not generated `/en` mirrors.

A budget checkpoint is progress, not a complete translation. No incomplete
candidate is uploaded as a full site or activated. Complete R2 candidates remain
`production_ready: false` and need the existing production-profile assembly,
route/content acceptance and rollback gates before activation. The established
Chinese/ko/ja/ar production defaults and shared production lock are unchanged.

For an already prepared complete Chinese production source, the builder accepts
an explicit cohort, for example:

```sh
python scripts/build_portal_locales.py --root "$CANDIDATE" \
  --site-url https://kcdesk.com --provider hymt --locales en,fr,de,es \
  --cache-in "$CHECKPOINT" --cache-out "$CHECKPOINT" \
  --hot-report-index "$PUBLIC_HOT_INDEX" --translation-scope incremental \
  --index-start-date 2026-09-23 --offline-time-budget-seconds 300 \
  --checkpoint-on-budget
```

## SEO/GEO identity

Emitted mirrors receive independent canonicals, native HTML language/direction,
localized titles, descriptions, structured metadata, feeds and sitemap entries.
Source-report links, financial quantities and publication dates are preserved.
No model-generated conclusion is inferred merely from a report title.

Only emitted eligible peers enter reciprocal hreflang clusters. Cantonese keeps
its `yue` URL and HTML language identity, and its own plain sitemap; it is not
mislabeled as Mandarin or inserted as an unsupported three-letter Google hreflang.
Traditional Chinese retains its distinct `zh-Hant` identity with case-insensitive
metadata comparison. Unsupported scripts, damaged placeholders, missing link
delimiters or numerical changes remain blocked, not repaired by inventing text.

## Sources

- Official model: https://huggingface.co/tencent/Hy-MT2-1.8B-GGUF
- Google language alternatives: https://developers.google.com/search/docs/specialty/international/localized-versions
- GitHub Actions billing: https://docs.github.com/en/billing/concepts/product-billing/github-actions
- Cloudflare R2 pricing: https://developers.cloudflare.com/r2/pricing/
