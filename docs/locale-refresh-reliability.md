# Locale refresh reliability

## Incident: 2026-09-08

Run `34169047186`
stopped during multilingual preparation. The upload and cutover jobs did not run.
The initial translation pass left eight source units. The next pass repaired five
but rejected three valid Japanese labels as unchanged source text:

- `三井E`
- `__KC_PH_000__ 三井E`
- `国内RevPar`

The first label is an HTML entity boundary fragment of `三井E&amp;S`.
Both translation providers returned valid same-form Japanese. Retrying the same
quality rule could not resolve it. The subsequent Chinese parity error required
locale sitemaps before rendering had completed; it did not establish a Chinese
content change.

The failed run restored the previous successful translation checkpoint and saved
its own completed rows. It was not a lost-cache incident. Across the latest 25
runs inspected on September 8, the automatic-refresh subset contained nine
successes, one failure and one cancellation. Other failed runs were separate
source tests, materialization and shadow-route defects.

## Invariants and recovery

- Japanese same-form financial labels and observed entity fragments are accepted
  only by bounded vocabulary/pattern checks. General unchanged Chinese prose,
  changed placeholders and invalid translations still fail validation.
- Backfill keeps its existing three-round bound. Continuation requires observed
  progress in the current translation inventory and a changed saved checkpoint;
  pruning obsolete cache entries must not erase evidence of useful progress.
- Each child invocation must create fresh diagnostics. Preflight results cannot
  qualify a complete build. Provider errors and unobserved requests remain stops.
- After an incomplete build, Chinese parity checks every original file's bytes
  and the complete original path inventory. This evidence is marked
  `publishable=false` and does not emit the publication approval hash.
- A completed build still requires the normal full parity gate, complete locale
  sitemaps and all existing static/shadow/live release checks.
- The Actions summary distinguishes a complete candidate from a cached,
  incomplete candidate. Diagnostic artifacts and saved translations survive
  failure. Inspect the specific pending units before repeating a deterministic
  quality failure.

## Verification

Regression tests cover the incident's actual labels and HTML fragmentation,
unchanged Chinese rejection, residual progress with cache pruning, stale child
reports, failed-build Chinese mutation detection and publication gating.
Run the workflow's `Validate public source` commands before merging. Then dispatch
`neutral-edge-cutover.yml` with `operation=migrate`, `translation_scope=incremental`
from current `main`, and verify preparation, cutover and live release output.

Use an independent worktree/branch for workflow changes. Merge against current
`main`; do not reset or stage changes in another task's working directory.

## Incident: 2026-09-09 — character allowance versus request bytes

Run `34292953933` stopped in the multilingual canary before upload or cutover.
DeepSeek returned incomplete translations; DeepL repaired the Korean and Japanese
rows but the local allowance check blocked the 32-row Arabic repair before its
POST. The diagnostics recorded 12,854 remaining characters. That repair contained
3,724 source Unicode code points, or 4,606 after XML protection, but its
ASCII-escaped JSON request occupied 13,951 bytes.

The adapter compared JSON bytes plus the 1,000-character margin against the
character allowance. [DeepL counts source Unicode code points](https://developers.deepl.com/docs/resources/usage-limits),
so the encoded-byte estimate incorrectly rejected the request. The first fix
reserved the protected XML text's Unicode length as a conservative character
upper bound; the 120,000-byte body limit remains a separate check. Actual returned
billing still settles reservations, and uncertain responses retain their reserved
characters. The request cap, quota margin, translation quality and publication
gates are unchanged.

Regression coverage includes a 32-row multilingual canary with a small remaining
allowance, Unicode and XML boundaries, concurrent and uncertain reservations,
true quota exhaustion, and the unchanged encoded request-body boundary.

## Follow-up: 2026-09-09 — five deterministic residuals

Run `34318194995` passed all three canary samples (32/32 each), then saved
1,050 newly completed translation units. Five residuals remained after a second
round made no progress: Korean `GRM (US$/bbl)` and `-200mm SOI ASP`, Japanese
`300mm SOI ASP` and `-200mm SOI ASP`, and one Arabic paragraph about seismic
survey fleets. The run checkpointed with `ready=false`; cutover did not run.

The chart labels are measurement/acronym identities. A closed grammar now
preserves them only in `chart:metrics`, while the same strings in prose remain
subject to translation checks. The Arabic source was echoed unchanged by
DeepSeek and failed protected-placeholder validation in DeepL. Its exact
paragraph now has a reviewed Arabic rendering with all three quantities
preserved. Existing valid translations retain priority; different text or
contexts continue through normal translation. No quality gate is disabled.

## Follow-up: 2026-09-09 — exclude XML protection markup from quota

Run `34320977236` exposed a second allowance overestimate in the earlier fix.
The remaining 31-row Japanese repair had 5,281 original source code points but
7,010 after XML protection, against a remaining allowance of 7,529. Including the
1,000-character margin, the original text fitted while the XML estimate did not.

[DeepL excludes XML tags when tag handling is enabled](https://developers.deepl.com/docs/best-practices/estimating-character-usage).
Character reservations therefore now count the original source code points,
including all placeholder text conservatively, without counting generated tags
or entity-escape expansion. The independent request-byte limit, actual billed
settlement, unknown-response reservations and 1,000-character margin remain.
Tests compare the original source count against parsed XML text nodes and cover
a multilingual canary whose source fits but whose XML representation does not.

The rerun also restored the preceding locale checkpoint correctly but still
generated 313 missing units: both runs translated 449 Chinese report titles
anew, and changed wording in those titles changed their derived HTML/LLMS source
keys. Chinese titles now have a separate source/model/prompt-keyed checkpoint,
restored before title translation and saved immediately after it, including when
the translation step fails. It only fills missing titles; it never restores a
whole old catalog over refreshed report metadata. Successful title results are
saved atomically as they complete. The initial checkpoint can reuse published
Chinese titles only when the report ID and full normalized original title both
match; existing titles and checkpoint entries retain priority. The new title
checkpoint is validated before CI saves it. Multilingual cache restore also selects the
newest cumulative checkpoint across code revisions, with existing compatibility
and per-entry quality validation retained.

## Incident: 2026-09-10–11 — literal labels stranded in the checkpoint

Run `34418515695` stopped its Korean canary after completing 23 of 26 rows,
below the required 24. The remaining rows were geography codes
`EU/JN/UK/AU/CA/SZ` and metric labels `AST2600 ASP (US$)` and
`AST2700 ASP (US$)`. The providers had preserved valid source identities.

Run `34546744028` subsequently saved 769 of 808 missing translations but did
not publish: `LOCALE_READY=false`, with Korean 2, Japanese 1 and Arabic 36
remaining. The Korean company name `Arm Holdings plc` and the geography codes
were then the entire Korean sample in run `34547101625`. Both providers
preserved them, and the canary failed again. Japanese `S&P 500指数` was also
stranded because protecting its numeric component left `S&P 指数`, a form the
same-name check did not recognize. A smaller residual inventory magnified these
classification defects; repeating the same provider calls could not repair them.

The company classifier now allows case-insensitive legal suffixes only alongside
a named token and a terminal legal form. Geography lists use a closed vocabulary
in `chart:geographies`; the two observed metric models extend the existing
`chart:metrics` grammar. These fields preserve the source code without inferring
its expansion. Japanese index labels use the same visible-text normalization
for validation, deduplication and cache provenance, after structural placeholder
checks.

Missing legal-company-name and accepted Japanese identity rows are now initialized before
the paid queue. Existing valid localized names keep priority, source keys remain
stable, and complete source/context checks prevent a sentence containing a name
from inheriting its exemption. Repeated refreshes therefore reuse these rows
without asking a provider to echo them. Diagnostics count initialized identity
rows per locale as `identity_seeded_units`.
Title-case chart keywords without a legal suffix still go to translation;
capitalization alone does not justify initializing an unchanged cache row.

The pull-request audit now runs the literal, canary, DeepL character-accounting
and Chinese-title-cache regression suites before merge. The full refresh still
requires complete translations, Chinese parity, static validation and successful
cutover. A green checkpoint run remains an incomplete release; verify cutover
and the active public release independently.
