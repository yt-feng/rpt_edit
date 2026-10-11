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

## Article images and covers

Both the translated-report uploader and the OCR/XHS uploader use the same image
admission and free-illustration path. Valid original report figures remain first
choice. Known contact-card pixels (including renamed copies and cover crops),
unreadable files, generated PDF-page title cards and the historical
navy/gold/cream placeholder are excluded from body illustrations and covers.
A PDF first page with a title overlay is not an extracted source chart. White-background research charts remain valid.
The trailing contact card has its own role and never counts toward the body-image
minimum.

When original figures are insufficient, `free_editorial_images.py` searches
Wikimedia Commons using a fixed, locally selected generic topic. It never sends
the report title or body to the public search API. The search itself is limited
to the supported CC0/CC-BY category union; short topic terms avoid accidentally
requiring unrelated subjects in the same photograph. Count-only diagnostics
distinguish an empty result from rejected license, format or URL candidates. Only explicit CC0 or CC BY
2.0/2.5/3.0/4.0 images with consistent license metadata are accepted. Author,
original file page and license accompany the image in the article; metadata is
sanitized rather than inserted as arbitrary HTML. Downloads have host, redirect,
byte, pixel and decode checks, a bounded request budget, cache and circuit breaker.

The old anonymous Pollinations endpoint is no longer called. Its production
responses included HTTP 402 and 502, and the XHS uploader discarded the fallback
and stopped filling images. Both uploaders now accept the Commons result. When
Commons is unavailable or has no eligible photo, an original topic illustration
is generated locally and clearly labelled as an illustration, not a photograph,
report figure or data chart. No blank title card or QR code substitutes for it.
The illustration varies its subject geometry, composition, count, placement and
palette across articles and image positions, including within the same topic.
Its article-and-position seed and saved provider selection keep retries stable.
Photo URL and decoded-image identities are deduplicated across the batch; an
exhausted eligible photo pool uses a distinct illustration instead of repeating
one picture. These are supplemental visuals, never manufactured report charts.

Covers prefer a validated original report chart, then the article's valid
supplemental image. When OCR has no retained source charts, the licensed-photo
and varied-illustration chain supplies the missing visuals.
They are normalized to a 1200 x 675 JPEG. A crop rejection first removes explicit
crop fields while retaining each article's own cover; further normalization is
per article. It never replaces a whole group with one generic blank cover.
HTML fitting retains at least one body image whenever images were supplied;
credits travel with the image through compression.

## Media verification and existing draft repair

`draft/get` verification compares the expected cover ID and ordered body/footer
image identities in addition to the editorial contract. Read-only audits remain
read-only. Uploaders can explicitly repair media at the same draft ID and article
index when titles, authors and prose still match; uncertain writes are followed
by readback rather than duplicate draft creation.

`wechat-draft-image-repair.yml` accepts an exact successful source run and its
unexpired draft diagnostic artifact. Source validation uses a bounded, authenticated
GitHub REST read and does not require the self-hosted runner to have `gh` installed.
Audit mode performs no uploads or updates.
Apply mode checks the live draft against its saved prose identity, inspects actual
WeChat CDN image bytes, replaces defective covers/body images and fills missing
body illustrations, then reads back the saved media. A second fresh read before
each update protects intervening edits. Legacy images without an exact source
reference remain usable existing body images, not proven PDF charts. Repair
records whether the selected cover used a retained source reference, another
retained body image or a new illustration; existing usable images do not trigger
extra filler just to reach a count. It never adds, deletes, publishes or
regenerates an article. Only recognized generated image credits are excluded from prose identity;
image-credit text and license/source links are checked separately on readback.
A WeChat 40007 response isolates an invalid historical receipt. Only a complete
current-draft listing with one exact, ordered whole-group match of title, author,
prose and source URL, followed by a fresh `draft/get`, can bind it to another
existing ID. Missing or ambiguous matches remain unresolved while other valid
groups continue. Such a completed maintenance run explicitly reports
`partial=true`, `fully_repaired=false` and `ok=false`; workflow completion is not
full repair acceptance. It never recreates a missing draft. Sanitized progress
permits a later rerun to repair only what remains.

An existing ID whose title, prose or source URL differs from the saved receipt,
or whose article order changed, is unresolved at group level; that group receives
no media calls, and later valid groups still run. There is an explicit author-only
admission: when the original saved receipt ID still resolves
and its ordered titles, prose, source URLs and count match exactly, media repair
preserves the live author values instead of restoring saved authors. Successful
groups record `resolution=author_change_preserved`. This allowance never applies
to 40007 catalog rebinding. Update preparation and readback still compare authors
strictly against the initial live values, so another author edit stops the group.
One deleted article is also preserved at that same original live ID: the current
group must contain exactly one fewer article and match exactly one ordered
subsequence of the receipt by title, prose and source URL. Live authors remain
unchanged. Ambiguous deletions, reordered or added articles, multiple removals
and changed prose/source are not admitted, and 40007 catalog recovery never uses
this rule. The deleted article is not recreated; updates use current live indices.
The group records `resolution=single_removed_article_preserved`, original/current
counts and the zero-based removed original index. `preserved_removed_article_count`
counts that deliberately retained deletion separately from unresolved work.
Sanitized diagnostics record per-field match booleans and
SHA-256 values only for mismatched fields, plus article counts and positions;
they never include titles, article text, source URLs or draft IDs. This separates
source-URL differences from prose differences without assuming either is an
edit or a harmless server normalization. A fresh-read mismatch during image
preparation stops updates to that group and preserves any intervening edit.
For that comparison, all articles' `draft/update` writable fields are compared
strictly: title, author, digest, content, source URL, thumbnail media ID and the
two comment settings. A changed field stops that group; prose and media checks
remain in force. Response-only fields such as `thumb_url` and `url` are not an
optimistic concurrency lock: they are absent from the update payload and do not
override the thumbnail's media-ID binding. Their changes are logged separately
with standard field names, writable/read-only classification and hashes only.
`updated_articles` counts confirmed `draft/update` responses separately from
examined/changed article counts; final `fully_repaired` still requires complete
coverage of the current articles and the existing media readback checks; an
explicitly preserved deletion is not an unfinished article.
The observed WeChat refusal `53407` with the fixed message
`定时发布中，无法删除或修改` means that group is locked for scheduled publication.
Repair records `scheduled_publish_locked` with the remaining article count and
continues other independent groups. It neither retries that write nor cancels
or changes the publication schedule. Already confirmed members retain their
verified counts; the locked members remain unresolved, not repaired or uncertain
writes. This exception requires both the code and the observed message prefix.
Other error codes, different messages and uncertain transport failures still
stop execution; they are not treated as successful or safely rejected writes.
After an update, a fresh `draft/get` must pass both the unchanged prose/source
identity and the full media contract. Only that updated article then adopts the
validated server representation as its next comparison baseline. This permits
the server's equivalent HTML normalization without accepting edits to the other
articles. The repair reader emits counts rather than raw media IDs.
If a group stops partway through, `remaining_articles` and
`unresolved_article_count` count only its unfinished members, so examined plus
unresolved plus preserved removals equals the original expected total.
`uncertain_article_count` is an explicit
subset of unresolved: an update was confirmed but its readback was unavailable
or failed validation. Such an article is never reported as verified or unwritten.
The final `progress.json` is synchronized with the terminal result, including
partial status and any uncertain updates.

New draft payloads carry the images and attribution into the existing Blog
archive path. Repairing an already saved WeChat draft is a distinct operation:
it does not by itself prove that an older public Blog archive has been updated.

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
