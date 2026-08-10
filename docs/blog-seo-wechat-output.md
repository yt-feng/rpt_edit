# Blog SEO and WeChat Output Contract

Last updated: 2026-08-10

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

`neutral-edge-cutover.yml` reads the archive into the static build, uploads an
immutable release to private object storage, verifies the route, and switches
the edge release. The routine schedule is 09:30, 13:30, 17:30, and 21:30
Asia/Shanghai. The source workflows normally run at 02:00 (primary report
batch), 06:00 (institutions), 06:30 (consulting), and 06:45 (ARK), so later edge
refreshes naturally pick up the committed articles.

Archive writes are fingerprint-idempotent. Each workflow pushes with a rebase
retry helper, allowing concurrent source jobs to preserve one another's
shards. A missed day can be recovered by rerunning its source workflow or by
materializing its retained draft payload and running the archive updater;
rebuilding the edge release never deletes older archive shards.

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

## Public footer and private website value

Every WeChat article ends with `更新信息参见` plus the runtime
`PUBLIC_SITE_HOST`. The production value is assembled at runtime so the
private deployment identity is not committed in plain text. It is a fixed
editorial value and is never replaced from `PORTAL_SITE_URL`.

The WeChat workflow still reads the production site origin from the
`PORTAL_SITE_URL` secret and validates that it is an origin-only HTTPS URL for
private `content_source_url` fields.

For each draft, the uploader creates two payloads:

1. a public template containing the fixed public-host footer;
2. an in-memory submission clone in which only private source-URL placeholders
   are replaced by the validated production hostname.

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
