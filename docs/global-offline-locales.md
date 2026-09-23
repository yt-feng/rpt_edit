# Global offline SEO/GEO locales

## Scope and publication boundary

The pinned model's public language/script table contains 38 variants: the
Simplified Chinese root plus 37 mirrors. The existing production default remains
Korean, Japanese and Arabic. `portal_language_registry.py` adds 34 further targets;
registry membership does not mean a language is published, reviewed or indexed.
The model-card introduction says 33 languages while its detailed table lists 38
variants. Low-resource output must pass the same checks as all other output.

Every emitted mirror has an independent canonical, native `lang`/direction,
reciprocal language alternates only to emitted peers, localized structured
metadata, feeds and sitemap entries. Existing source-report links and dates are
preserved. RTL applies to Arabic, Persian, Urdu, Hebrew and Uyghur. No new schema
or `llms.txt` promise substitutes for accurate, attributable page text.

## Zero additional paid translation API requests

Use only the existing immutable Hy-MT2 1.8B Q8_0 model and portable CPU runtime on
standard public Ubuntu Actions runners. All model/runtime checksums remain pinned.
Traditional Chinese additionally uses pinned OpenCC 0.1.7 dictionaries locally;
Simplified-to-Traditional conversion is deterministic and avoids paraphrasing.
The new language adapter has no DeepSeek/DeepL fallback. New dynamic detail-page
locales read only generated overlays and never call the legacy paid translation
endpoint. An unavailable overlay shows a native explanation and a Chinese link.
Existing three-language behavior and private access controls are unchanged.

No DeepSeek key, provider credential or larger/GPU runner is required by either
new workflow. Standard public-runner compute is distinct from GitHub artifact or
cache storage billing: bounded storage is implemented, but an account-wide zero
bill is not promised. This does not disable unrelated existing research APIs.

## Qualification

`portal-global-locale-preflight.yml` runs deterministic and real-model checks for
all 37 mirrors in bounded CPU groups. Samples cover site prose, financial rates
and a protected citation. The report records both qualified and blocked locales;
`semantic_review` stays pending and `production_ready` stays false. Wrong-script,
unchanged prose, damaged identifiers or quantity changes cannot become releases.
Three samples cannot establish native-speaker quality for an entire site.

## Incremental preparation

`portal-global-locale-prepare.yml` is a separate preparation lane. On its six-hour
schedule it rotates through at most six of the 34 new targets, with two concurrent
standard CPU jobs and a 300-second translation budget per target. Manual runs can
select `all`, `new`, or a canonical comma-separated set and a 30–1200-second budget.
It reuses validated, exact-source translation rows across runs. Each locale cache
is capped at 8 MiB; a source package expires after one day, readiness reports after
three. Source-generation work has an independent timeout. Checkpointed runs are
successful preparation progress, not completed translations or publications.

The source is the repository's public projection rendered by the existing site
generator. This lane does not fetch private chart/Hot overlays, rerun original
article generation, write R2, deploy Workers, update the active-release pointer,
or submit URLs to search engines. Its source manifest says so explicitly.
Fully translated candidates must still pass the production profile, route and
publication checks, plus appropriate semantic review, before activation. No
untranslated sitemap or empty language shell is activated by this workflow.

For an already prepared, complete Chinese production source, the existing
builder accepts an explicit cohort:

```sh
python scripts/build_portal_locales.py --root "$CANDIDATE" \
  --site-url https://kcdesk.com --provider hymt --locales en,fr,de,es \
  --cache-in "$CHECKPOINT" --cache-out "$CHECKPOINT" \
  --hot-report-index "$PUBLIC_HOT_INDEX" --translation-scope incremental \
  --index-start-date 2026-09-23 --offline-time-budget-seconds 300 \
  --checkpoint-on-budget
```

A selected cohort containing new targets rejects paid providers and source
fallback. Incomplete work cannot add locale pages or sitemap entries. Do not
turn the production default into `all` before its candidates are complete: that
would unnecessarily hold the established Chinese/Korean/Japanese/Arabic lane.

## Source references

- https://huggingface.co/tencent/Hy-MT2-1.8B-GGUF
- https://github.com/yichen0831/opencc-python
- https://docs.github.com/en/billing/concepts/product-billing/github-actions
- https://developers.google.com/search/docs/specialty/international/localized-versions
