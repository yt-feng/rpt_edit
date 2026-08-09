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

## WeChat editorial label

Generated prompts request `KC评论`. The upload-time sanitizer also converts
the historical label to `KC评论`, and the HTML renderer owns the final label.
This makes old drafts and newly generated drafts produce the same visible
heading without duplicated prefixes.

## Private website value

Public source and archived Blog payloads contain only the neutral site-host
placeholder. The WeChat workflow reads the production site origin from the
`PORTAL_SITE_URL` secret and validates that it is an origin-only HTTPS URL.

For each draft, the uploader creates two payloads:

1. a public template that retains the placeholder and can feed the Blog
   archive;
2. an in-memory submission clone in which only the placeholder is replaced by
   the validated production hostname.

Only the second payload is sent to the WeChat API. It is never written to the
repository, logs, summaries, or public artifacts. Static-site deployment uses
the validated build origin to resolve the same placeholder in the generated
Blog body. The committed archive remains unchanged, while the deployed article
shows the live hostname.

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
