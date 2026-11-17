# Neutral catalog and language publication

Ordinary refreshes publish new Chinese content using the last verified core
translations, then queue a language update. Existing Korean, Japanese, Arabic,
extended-language and English content remains available. Translation freshness
may differ across languages; this is an intentional publication policy.

## Why previous repairs did not resolve the whole workflow

Several independent defects accumulated in one long release transaction:

- R2 same-object throttling and interrupted response bodies had inconsistent
  retry handling across readers, uploaders and the final guard.
- Large multilingual builds amplified memory and elapsed time. A small daily
  content change still traversed the cumulative static site.
- Scheduled installs could change the SDK between releases. The November 11
  incident involved botocore retry behavior and a different SDK in CI.
- Production artifact, chart overlay and validation consumers used different
  limits. A build could succeed before a later reader rejected its output.
- Shadow application routes replaced the normal bounded retry transport with
  a single request, while the error still claimed retries had occurred.
- The recorded publisher spent 21 minutes scanning brand rules and 27 minutes
  checking unchanged objects, versus 75 seconds uploading changed files. Both
  checks now use bounded parallel workers without reducing their coverage.
- Repairing the first failed phase exposed later defects. Passing that phase
  or merging its fix was insufficient evidence of a successful publication.

The November 16 candidate contained 63,367 cumulative files. Its uploader
changed 4,070 files, reused 59,297 and deleted 58 stale files. Changed files
include regenerated indexes and translated variants, not just new reports.

## Publication modes

| Mode | Chinese source | Core translations | Extended languages and English |
| --- | --- | --- | --- |
| `catalog` | Fresh catalog/build with published-report inheritance | Exact published files retained, without model inference | Existing composition, exact handoff approvals and live checks |
| `locales` | Exact active Chinese snapshot captured after acquiring the publication lock | Translation/build using that snapshot and reusable checkpoints | Existing published batches carried forward |
| Internal `full` | Existing complete build | Existing complete build | Existing approval and publication path |

First activation, historical translation, shadow/rehearsal and explicit catalog
recovery retain the complete path. Live incremental handoffs can publish their
approved additional-language or English content while retaining core translations.

Retained files are streamed and hashed against the captured active static
manifest. Approved extended-language composition may update retained HTML
hreflang links. A source-bound normalized digest and the exact assembled link
cluster allow that change while preserving the body and every other head field;
older receipts continue to require exact bytes. Translation provenance and coverage remain those of the original
translation. Only the manifest's Chinese lazy-JavaScript binding changes to
the freshly built Chinese asset. Chinese discovery advertises only retained,
indexable counterparts that actually exist. A private receipt preserves the
original manifest bytes and binds recovery to the exact published version.

The language follow-up restores the latest active Chinese files instead of
rebuilding them from an older queued commit. Before translation it removes
only the existing, explicitly permitted core-language discovery markup;
Chinese parity proves that page content and protected assets survive unchanged.
If historical core pages are already published, the follow-up keeps their
admitted page set and ledger, pauses new historical admission, and verifies
that no published page or historical quota accounting was lost. Catalog-only
work does not overwrite a newer unfinished translation checkpoint with its
older published translation cache.

## Recovery and validation

- Release and CI use the same pinned R2 SDK/transport constraints.
- Local pre-upload validation invokes the same locale-runtime consumer contract
  used by shadow acceptance, including its byte limits.
- Transient HTTP and interrupted-body failures have bounded retries. Permanent
  permission, content, checksum and size errors remain failures.
- Final object checks retain streaming SHA/length validation. Recovery reuses
  each body already verified during the extended-page audit.
- Retained-mode recovery verifies its receipt and original active manifest;
  it never invents a translation preflight report for a build that did not run.
- Publication, full locale coverage, application routes, English access checks,
  exact-version approvals, Chinese parity and rollback gates remain in place.

## Operational boundary

This is a catalog-first, two-phase cycle. The existing production lock still
serializes whole publications, including a language follow-up, so a later
catalog refresh can wait behind one already running. Fully concurrent preparation
would require immutable staging and a checked merge into the latest Chinese
release; mutable A/B slots must not be treated as immutable cached evidence.

A dispatched job is accepted work, not a successful release. A successful
release requires the exact run's cutover and live acceptance to succeed.
Routine progress polling is unnecessary; do not describe a passed preflight,
merged patch, or queued recovery as full production recovery.
