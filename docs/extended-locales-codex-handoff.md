# Additional locales: local Codex handoff

## Current operator scope (2026-09-26; supersedes historical batch instructions below)

- Translate only newly published public detail pages on the current Asia/Shanghai
  date, starting 2026-09-25. Do not backfill previous dates, the homepage, About,
  institution/topic directories or historical related lists. A sitemap lastmod
  alone is not publication evidence; verify the page's own Article/Report date.
- 24 means **at most 24 website detail pages per batch**, not PDF pages and not
  a target to fill. Empty today-only selections skip inference. Completed-content
  receipts in private R2 advance later same-day batches without translating them
  again. Unknown publication dates remain excluded, not guessed.
- The operator increased per-language translation budget to **14400 seconds
  (four hours)**. Workflow job timeout is 270 minutes, leaving setup/persistence
  time. Finish early when done; still save timeout checkpoints and keep incomplete
  candidates unpublished. Keep at most two simultaneous languages.
- English is excluded from full reading pages and Charts; any future English
  surface is text-only summary/commentary Blog, never original/full report text.
  There are 33 non-English expansion targets; all are now requested by default.
- Follow successful default-branch `Neutral edge catalog refresh` runs to prepare
  new candidates, defaulting to `all-supported` (33 non-English locales). Completed
  locales are omitted from the matrix for the selected batch. The workflow
  hook becomes active only after its normal PR review and merge to main.
- Do not monitor runs. Stop after dispatch. Do not rerun the old mixed-directory
  generation `f334aac3023978818d18a4d28ed16cb2541a7b9b6ea803021f1fcd0502c812aa`.
- Publication integration/approved-page carry-forward remains separate work;
  automatic translation does not bypass approval, activate pages or imply live.

## Objective and boundaries

Finish the additional public reading-page locales for KC桌面, building on draft PR #180 and the separately merged manifest-size repair in PR #179. The established Chinese and ko/ja/ar application pages, authentication, report URLs, document access rules and crawler-training policy must remain intact.

Use only the already-pinned Hy-MT2 CPU runtime on standard public-repository Linux Actions runners. No DeepSeek, DeepL, OpenAI API or other paid translation fallback. The developer's local Codex session is for code, review and orchestration; it is not a new production translation provider. Do not set fake Actions environment variables to execute the translator locally.

The 38-entry model language/variant registry gives 34 expansion targets after excluding the four established site languages. Model support is not a guarantee of publication-quality output. Keep failures explicit and unpublished; script detection and financial-quantity tests are not human linguistic review.

## Source already in this draft

- `portal_extended_locales.py`: bounded public HTML extraction, preserved source identities, candidate rendering, language navigation labels and target selection.
- `build_portal_extended_locales.py`: strict offline translation, per-language checkpoint, complete-page-only output and non-indexable candidate manifest.
- `collect_portal_extended_sources.py`: bounded public canonical source collection, plus collection from an inactive local Chinese site tree.
- `assemble_portal_extended_locales.py`: matching-generation, explicit-approval assembly into a fresh inactive tree. It does not upload or deploy.
- Language registry, model adapter and setup-action changes: added targets without selecting a new model or relaxing quantity checks. Traditional Chinese keeps a distinct namespace.
- Edge static host: language headers and canonical-path handling for added locale prefixes, without changing authentication or object publication.
- `portal-extended-locales-check.yml`: credential-free contract checks and optional four-language CPU canary. No translation artifacts are uploaded; model receipts are disabled for the new canary. Existing model/runtime caches contain public dependencies only.

## Mandatory local sequence

### A. Reconcile without losing anyone's work

Read the repository's existing instructions. Inspect `git status --short`, current branch, remotes and `gh auth status`. Use a separate clean worktree when needed; do not run destructive reset, clean or force-push commands. Fetch current main and PR #180. Confirm the branch includes PR #179's manifest codec fix. Inspect the current CI state before treating any earlier passing run as current.

Run the new regressions and the existing offline, financial-quantity, title, manifest and edge-host tests. Never merge this draft solely because the core tests are green.

### B. Implement and review R2 persistence (not included here)

The earlier connector write of `scripts/portal_extended_r2.py` was explicitly rejected; it was not submitted again using another endpoint or encoding. This handoff does not contain that blocked module. Implement storage through the operator's normal, authorized development and review process, retaining platform and repository approval requirements.

Reuse the established R2 client patterns and existing Actions secret names; check names/existence, never dump secret values. Prefer a private staging bucket or a verified unserved prefix. A hidden key name does not make a public bucket private. Do not enable bucket-wide public access. Do not add a public arbitrary-key R2 proxy.

Use distinct namespaces for immutable source generations, validated translation checkpoints, candidate objects and approval receipts. Key caches by model identity, locale, source generation/content and validator version. Upload complete files first, verify byte counts and SHA256, and only then publish a candidate manifest. Bound object count/size, validate path traversal and reject unexpected origins. Handle missing objects separately from permission/network errors. Do not recursively delete unrelated objects. Keep accepted checkpoints on R2 when an Actions job reaches its budget or fails; never promote an incomplete manifest.

No generated translations, corpus dumps or candidate HTML go into Git commits, Actions cache or Actions artifacts. Temporary runner disk is unavoidable and is discarded at job end. Public model/runtime caching remains allowed. Apply retention to candidate generations separately from durable accepted checkpoints and the active/previous release.

### C. Wire generation and resumption into CI

Create a storage-backed workflow only after B is tested. Default to 24 bounded public source pages per language, a 1..2400-second per-language budget, at most two concurrent languages, and isolated failures. The current collector handles at most 500 pages per corpus: reaching the full archive requires deterministic batches/cursors, not removal of the bound.

A timeout has exit code 75 and an incomplete manifest; save checkpoints and mark the unit pending, not complete. A source generation must remain stable across resumptions. Do not keep scraping a changing live homepage and then attempt to merge its old candidate into a different source generation. Prefer freezing the exact inactive Chinese tree, persisting that corpus to R2, and rebuilding candidates against it.

First run the credential-free canary, then R2 round-trip tests in an isolated staging namespace, then one complete locale. Expand in bounded batches after evidence is saved. Do not restart all 34 languages from scratch after one failure. Do not add an unbounded schedule or disable the production serialization lock.

### D. Complete the inactive release integration

The current assembler deliberately accepts only a fresh inactive tree and refuses an existing assembly receipt. Implement the carry-forward/update strategy before adding later language batches: retain all previously approved matching-generation locales and their reciprocal alternatives, or rebuild the complete approved set together. Never overwrite an existing locale's files or replace the root sitemap with only the last new batch.

Verify response `Content-Language`, HTML language/direction, self-canonical, reciprocal hreflang, supported language/script identifiers, valid sitemap entries, source links, preserved dates and financial values. Cantonese remains a separate BCP-47 page language but is not emitted as a claimed Google-supported hreflang code. Do not index incomplete or unreviewed translation pages. Add a real navigation entry only for successfully published language roots.

Use the existing production workflow's inactive upload, exact-generation checks, approval, serialization, atomic switch, live acceptance and rollback. Inspect the current workflow_dispatch inputs before invoking it; never guess secrets, profile names or input options. Do not rerun an old failed job and assume it uses the new commit: verify the resolved source revision.

### E. Evidence required before declaring completion

Record the exact source/merge SHA; CI run IDs and conclusions; per-language model canary results; actual source/page counts; R2 checkpoint restoration without retranslation; candidate manifest/object checksums; review approvals; previous and activated generation; live sample URLs/HTTP statuses; canonical, robots, language headers and noindex removal; rollback verification. Distinguish merged code, a running workflow and a verified production release.

Finish with a status matrix: done / waiting for runtime / requires operator permission. Preserve a small next-step checkpoint after each stage so the next local Codex session can resume without reconstructing the whole discussion.

## Useful checks from repository root

```bash
python -B scripts/test_portal_extended_locales.py
python -B scripts/test_portal_extended_hardening.py
python -B scripts/test_hymt_offline_translation.py
python -B scripts/test_compare_hymt_translation.py
python -B scripts/test_financial_quantity_integrity.py
python -B scripts/test_offline_translation_callers.py
python -B scripts/test_portal_offline_locales.py
python -B scripts/test_translate_portal_titles.py
python -B scripts/test_locale_manifest_compaction.py
python -B scripts/check_public_identity.py
for test in workers/edge-static-host/test/*.test.mjs; do node --test "$test"; done
python -B scripts/build_portal_extended_locales.py --list-locales
```

## Source references

- Model inventory: https://huggingface.co/tencent/Hy-MT2-1.8B-GGUF
- Standard public-runner billing: https://docs.github.com/en/billing/concepts/product-billing/github-actions
- R2 public-access boundaries: https://developers.cloudflare.com/r2/buckets/public-buckets/
- R2 Workers bindings: https://developers.cloudflare.com/r2/api/workers/workers-api-usage/

Cloudflare R2 storage/requests have their own pricing; zero extra DeepSeek calls is not a promise that all infrastructure usage is free.
