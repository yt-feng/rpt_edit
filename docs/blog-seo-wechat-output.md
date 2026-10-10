# Blog SEO and WeChat Output Contract

Last updated: 2026-10-10

This document records the public Blog title contract and the private-runtime
boundary used by WeChat publishing.

## Publication data flow

The daily source workflows generate temporary WeChat draft payloads. After a
draft has been accepted, `update_blog_archive_from_wechat_drafts.py` passes the
payload through the Blog HTML allow-list, derives a content fingerprint, merges
duplicates, and commits only normalized public records under
`portal_suite/data/blog_archive/YYYYMMDD/<fingerprint>.json`. The archive record
contains the editorial title, digest, sanitized HTML, normalized source label,
publication dates, and stable slug. It never contains the temporary payload
path, private object locator, API credential, or deployment hostname.

`neutral-edge-cutover.yml` reads the archive into the static build, hashes the
output, incrementally updates the inactive A/B storage slot, verifies the full
slot, and atomically switches the edge Worker. Unchanged objects are not written
again. The routine schedule is 09:30, 13:30, 17:30, and 21:30
Asia/Shanghai. The source workflows normally run at 02:00 (primary report
batch), 06:00 (institutions), 06:30 (consulting), and 06:45 (ARK), so later edge
refreshes naturally pick up the committed articles.

Archive writes are fingerprint-idempotent. Each workflow pushes with a rebase
retry helper, allowing concurrent source jobs to preserve one another's
shards. A missed day can be recovered by rerunning its source workflow or by
materializing its retained draft payload and running the archive updater;
rebuilding the edge release never deletes older archive shards.

### MinerU and OCR provenance through delivery

Normal Daily processing prefers MinerU. If article shards are incomplete, the
workflow first resumes accepted MinerU tasks and verified durable results; an
actual recovery failure enables the ordinary OCR backup. Both verified source
editions enter `recover-report-article-delivery.yml`, which generates only
missing source-bound articles and then uses the same WeChat upload and public
archive contracts. The OCR input is complete, hash-bound page text, not an
already synthesized Market Views summary. OCR text, reconstructed figures and
translation caches keep their own provenance namespace.

The private handoff binds the original run and execution SHA, recovery run and
SHA, selected manifest, source bytes and expected report count. Generated
articles and accepted draft groups have additional body and group identities.
Public Blog records keep only the sanitized publication fields and safe
discovery provenance; original PDFs, raw OCR/MinerU output, provider responses,
private handoff locations and draft media IDs do not cross that boundary.

The recovery receipt accounts for all sources as accepted articles or explicit
title-policy exclusions. Body-generation failures are errors, not exclusions.
Accepted drafts must pass remote count/title/editorial-footer readback before
their payloads enter the archive. Retrying a website release reuses the archive
and publication request rather than repeating draft creation.

### What establishes public acceptance

After a recovered archive commit, the publication watcher stores a request
containing only public slugs and content hashes. It accepts a successful main
release only when that release contains the archive commit and every requested
live article has its exact canonical URL and complete body/reference digest.
Leading title normalization is allowed by the shared renderer; the remaining
body and final source footer stay inside the digest. Publication state survives
reruns, and a superseded queued release is followed only when its successor
contains the same archive commit.

The normal primary upload requests an incremental refresh after its archive
commit. A dispatch acknowledgement or green source run is not proof that Blog
pages are live. The final cutover must also pass its immutable runtime/static
binding and public acceptance. The catalog inherits the active published
catalog before the additive source scan, verifies inherited IDs before upload,
and switches the runtime and static catalog atomically.

For the 2026-10-10 verification, release run `38036944110` was independently
checked against all 118 accepted Chinese articles from source cohorts 261004,
261008 and 261009. HTTP status, canonical URL and complete body/reference hashes
matched for 118/118; the edge identity stayed unchanged across the check. This
is Chinese article acceptance. It does not establish real OCR fallback delivery,
missing historical cohorts, or all supported language publications. Track those
as separate source/locale receipts; see
[WeChat generation and recovery](wechat-pipeline-recovery.md).

## Public Blog title contract

Every rendered article title ends exactly once with ` | KC桌面`. The suffix
is applied by the static renderer, not persisted as part of the ingestion
identity. This keeps article fingerprints and URLs stable if an upstream title
already contains the suffix.

The same normalized title is used in:

- Blog cards and article headings;
- the HTML document title;
- Open Graph and Twitter metadata;
- `BlogPosting.headline` in JSON-LD.

The Blog landing page uses `KC桌面` naturally in its visible introduction,
description metadata, Open Graph metadata, and Blog JSON-LD. It must not repeat
the term mechanically inside article bodies.

For WeChat-facing titles, the original PDF filename is the highest-weight
semantic anchor. A valid title preserves the report's company, product,
technical acronym, geography, and topic, then may add only source-backed
numbers, dates, changes, comparisons, or counter-intuitive facts. Ordinary
research words such as growth, profit, record highs, guidance changes, and
`why/how` are not sensitivity violations. The deterministic guard blocks
inflammatory, adversarial, political/military, and advice-like framing, while
generic fallbacks such as `研究主题与行业变化观察` or
`某公司业务与近期数据观察` fail title quality checks.

## WeChat editorial label

Generated prompts request `KC评论`. The upload-time sanitizer also converts
the historical label to `KC评论`, including a standalone unquoted label, and
the HTML renderer owns the final label.
This makes old drafts and newly generated drafts produce the same visible
heading without duplicated prefixes.

The Blog renderer performs the same label normalization for immutable legacy
archive records. It also cleans common adjacent-punctuation artifacts at
render time; source archive JSON remains unchanged.

## Reference editorial tone

Both the primary-report generator and the institution/consulting generator
append the shared tone card from `wechat_article_quality.py` before the hard
delivery guard. The tone card was distilled from the maintained best-practice
references and defines a three-step editorial rhythm: source evidence, a plain
causal explanation, and an explicit choice of the next variable worth
watching.

`KC评论` is therefore a short editorial argument rather than a generic caveat.
It must stay next to the evidence it explains, normally use two or three
complete sentences, and may use restrained first-person wording such as
`我的理解是` or `我更关注的是`. It may not invent holdings, interviews,
historical calls, reader questions, or facts outside the source report. The
reference material supplies tone and reasoning structure only; advice-like or
sensitive source claims are not inherited.

## Public footer and private website value

Every persisted WeChat template ends with `更新信息参见` plus the neutral
`PUBLIC_SITE_HOST_PLACEHOLDER`. The production value is assembled only in the
in-memory submission clone, so the private deployment identity is not written
to the repository or public Blog archive. It is a fixed editorial value and is
never derived from `PORTAL_SITE_URL`.

The WeChat workflow still reads the production site origin from the
`PORTAL_SITE_URL` secret and validates that it is an origin-only HTTPS URL for
private `content_source_url` fields.

For each draft, the uploader creates two payloads:

1. a public template containing only the neutral footer and source-URL
   placeholders;
2. an in-memory submission clone in which the footer placeholder is replaced
   by `PUBLIC_SITE_HOST`, while source-URL placeholders are replaced by the
   validated `PORTAL_SITE_URL` hostname.

Only the second payload is sent to the WeChat API. Private source URLs are
never written to the repository, logs, summaries, or public artifacts.
Static-site deployment resolves placeholders found in legacy Blog bodies and
normalizes old labels without mutating the committed archive.

## Complete-sentence budget

The renderer never creates a sentence by cutting arbitrary characters and
adding `。`. When the visible-text budget is reached, prose keeps only the last
complete source sentence that fits. Headings and list items are atomic: they
are included whole or omitted. This prevents fragments such as `关注管理。`
from being manufactured at a body-length boundary.

## Cover handling

Report-specific XHS covers are normalized to a 1200 x 675 JPEG before material
upload. Portrait, oversized, or uncommon source dimensions are center-cropped
after high-quality resizing. Missing or unreadable sources produce a valid
generated fallback.

The workflow no longer replaces every report-specific cover in advance. If the
WeChat API rejects a cover crop, draft creation still retries with the generated
safe cover and, if required, without explicit crop fields.

Ordinary Markdown blockquotes remain ordinary quotations. Only blockquotes
that explicitly begin with the current or historical editorial-comment label
are rendered as `KC评论`; the historical label is normalized at upload time.

## Verification

Changes to this contract should run:

```text
python scripts/test_portal_blog_build.py
python scripts/test_wechat_article_quality.py
python scripts/test_wechat_output_contract.py
python scripts/test_xhs_draft_streaming.py
python scripts/check_public_identity.py
```

The identity check intentionally allows the exact Chinese editorial term while
continuing to reject the private deployment identity, deployment domain, and
repository association markers.


## Discovery provenance sidecar

The report uploaders retain optional original-basename metadata in a parallel
`source_reports` list in persisted `draft_payload_*.json` templates. It is not
sent as part of WeChat API article objects. The Blog importer requires exact
positional alignment, validates the safe name/ID fields and preserves them
outside the immutable title/content fingerprint. The site builder resolves only
unique source matches and applies editorial display overrides to copies after
persistence. See `seo-geo-architecture.md` for matching, reciprocal links,
archive identity and the unresolved-source contract.
