# Financial quantity validation in localized translations

## Policy scope as of 2026-10-11

The quantity parser checks prose numbers, money, percentages, signs, dates,
units and occurrence counts. It is not an HTML, CSS or JavaScript rendering
check. For the `ko`/`ja`/`ar` site mirrors, all 33 non-English SEO/GEO reading
locales and English website commentary, differences are advisory. The page builder
and shared Hy-MT2 adapter explicitly select this policy; English also applies it
when verifying stored candidate bodies. A numeric-only difference does not
trigger another model call, cache eviction, source fallback or publication hold.
Known numeric data placeholders use the same advisory rule; URLs, resources and
runtime placeholders remain mandatory.

The parser grammar below remains useful for bounded diagnostics and strict
callers. Report translation, Chinese editorial and callers that do not explicitly
select advisory behavior retain the adapter's strict default. English website
commentary opts in without changing the shared default or allowing source-language
fallback. In this document, parser “failure” means a
blocking result only for those strict callers; SEO callers record counts and
fixed codes. Diagnostic samples are bounded hashes, never source/model text.
The same model/cache identities remain reusable in both policies. Strict callers
revalidate any cache they consume, including a row first produced in advisory
mode. Advisory callers retain structural, link, placeholder, table, Unicode,
nonempty-content and target-script checks.

### Publication and old checkpoints

Historical approved pages are replayed from their authenticated pinned cache
without inference. Current SEO advisory validation is tried first; the frozen
quantity parser is only an exact historical compatibility path. Full approved
HTML inventory and bytes must still match. Changing prose numbers does not
permit replacing an already approved page or rebinding it to a different source.

A numeric-origin source fallback remains source text: `translation_complete`
and `translation_ready` remain false. A separately verified `publication_ready`
may permit this intact SEO page. Its complete fallback count, hash inventory,
fixed numeric error categories and exact source/manifest/proof identity must
agree. Missing or mixed structural evidence does not receive this exception.
Old immutable manifests/proofs are read under this policy, not rewritten merely
to add a flag. Automatic recovery excludes numeric-only fresh inference and
retains accepted-ledger/cache-only completion. The explicit `repair_portal_extended_checkpoint.py` entry retains its current
strict parser/adapter contract for exact manual checkpoint recovery. The French
legacy recovery entry preserves its source/receipt identity contract while using
the SEO advisory numeric policy.

## Parser semantics for diagnostics and strict callers

The quantity gate compares structured multisets, retaining the magnitude,
currency, quantity kind, sign and occurrence count. It validates materialized
Hy-MT2 output before a new cache entry is written and also validates reused
translation units. It does not infer an intended value from the source merely
because one interpretation would make a candidate pass.

## Supported locale number grammar

The targeted locale rules were checked against locally installed Unicode CLDR
48.0, ICU 78.3 and Unicode 17.0 through Node v24.19.0
`Intl.NumberFormat(locale, {useGrouping: true}).formatToParts(1234.50)` on
2026-10-10. CLDR is evidence for the rules, not a new runtime dependency.

| Explicit language | Decimal separator | Group separator |
| --- | --- | --- |
| `fr` | comma | narrow no-break space |
| `ru`, `pl`, `cs`, `uk`, `kk` | comma | no-break space |
| `es`, `de`, `id`, `pt`, `tr`, `it`, `vi`, `nl` | comma | dot |
| `hi`, `gu`, `te`, `mr`, `bn`, `ta` | dot | rightmost 3 digits, then groups of 2; existing Western groups of 3 also retained |
| Other supported locales, `en`, and unscoped callers | existing rules retained | existing rules retained |

Only these exact target/source language identifiers enable their grammar.
Space-group locales accept regular space, NBSP and narrow NBSP as typographic
aliases, with complete three-digit grouping checked before normalization.
Unknown language tags do not acquire these rules implicitly. Existing French
quarter recognition remains; no additional quarter aliases are introduced.
The locale inventory uses the repository's explicit `OG_LOCALES` regions,
including `pt_BR`; the grammar does not guess an alternative regional meaning.

For all 14 comma-decimal locales, a comma is decimal even with three or more fractional
digits: English `0.125%` equals localized `0,125%`, while English `125%` must fail
against that same localized text. A locale-specific indivisible number token
prevents `0,000125` from being split into unrelated quantities `0` and `125`.

Complete groups in the eight dot-group locales, such as `1.234` and `1.234.567,50`, are
normalized once to `1234` and `1234567.50`. A well-formed three-digit dot group
always retains its locale meaning. It cannot simultaneously mean an English
decimal based on the source value. Unambiguous dot decimals that do not match
the grouping grammar, such as `0.125`, `12.34` and `1234.567`, retain compatibility
with prior untranslated numeric notation.

Space grouping is checked before Unicode normalization can collapse different
space characters. Numeric width and Unicode decimal digits are normalized without
discarding that distinction. Explicit Arabic grouping/decimal symbols retain
their own meaning. Comma-separated or whitespace-separated decimal lists are
validated piece by piece, so a valid first number cannot hide malformed later
mixed separators. Recognized malformed localized decimal runs produce the fixed
`invalid_numeric_format` failure, even when both inputs contain the same malformed
form. Other version-like dotted text retains the existing scanner behavior.

The six explicit Indian-group locales normalize a complete `12,34,567.89` to
`1234567.89`; they must not split it into `12.34` and `567.89`. Leading groups
have one or two digits and the rightmost group has three. Valid prior Western
notation such as `1,234,567.89` remains supported with the same value. Malformed
mixed or incomplete comma groups fail as a whole, independently of the source.
Native Unicode decimal digits and fullwidth numeric forms use the same grammar.

Turkish also recognizes its CLDR percent prefix (`%0,125`, `-%0,125`). A single
left-to-right pass handles prefix and suffix percentages: `5% 0,125` retains
the percent on 5, and `-%5 %0,125` preserves each percent quantity and its sign.
Signs, including space-separated signs, bind to the prefix; malformed multiple
signs fail. This prefix grammar is restricted to `tr`.

For `fa`, `ur` and `he`, the ICU-generated left-to-right mark (U+200E) in a
numeric-adjacent sign sequence is removed without discarding any sign. This
allows a currency prefix followed by the formatted negative number to retain
its currency type. Multiple signs separated by that mark fail as malformed;
other directional marks, marks inside words, and other locale grammars are
unchanged.

Currency, scaled amounts, percentages, percentage-point changes and basis points
remain distinct. Added, omitted, duplicated, sign-changed or magnitude-changed
quantities continue to fail. Invalid-format diagnostics contain a fixed
`invalid_number` fact with no source text; a downstream public diagnostic that
does not recognize this fact reports its signature as unavailable.

## Earlier strict-policy cache and publication boundaries (historical)

The model identity and `extended-static-v2` checkpoint identity are not bumped.
This avoids discarding successful work or implicitly scheduling historical
translations. The earlier strict-policy behavior below remains applicable to strict callers.
SEO publication follows the advisory policy above instead:

Reuse has several distinct gates:

1. The Hy-MT2 adapter materializes the cached translation and applies the current
   quantity gate before returning it. An old `125%` to `0,125%` cache entry is
   rejected without another model call. Direct adapter rejection leaves the cache
   bytes in place; it does not declare the cached output valid.
2. The extended-page `Memo.get` validates accepted checkpoint rows before reuse.
   Its existing handling removes an invalid exact row and discards the matching
   adapter unit when a caller is actually rebuilding that source. The quantity
   change does not dispatch a rebuild or bypass normal ownership/deadline gates.
3. `checkpoint_evidence` revalidates accepted rows under the current quantity
   gate when checking registered continuation outcomes and new handoffs.
4. A candidate manifest's `translation_complete` and the immutable quality proof
   bind exact source/manifest bytes; they do not encode a quantity-parser revision
   and do not independently revalidate the translated text. New publication
   composition performs a cache-only replay with the current validator and
   requires the complete approved byte inventory to match.
5. Already authenticated active pages retain the existing, narrower carry-forward
   exception: exact prior approved bytes may be reproduced with
   `approved-financial-quantities-pre204-v1`, bound to its frozen parser SHA and
   unchanged source content. This preserves the active site; it is not evidence
   that historical text was corrected under the new numeric grammar.

Existing exact-source fallbacks retain their source text and original outcome.
Numeric-only records are not scheduled for fresh automatic repair under the SEO
policy; publication eligibility is evaluated separately as described above.
The SEO policy does not erase immutable source, candidate, checkpoint, fallback
or quality-proof evidence. Verified numeric-only records no longer occupy the
blocking repair queue; old records drain through the existing bounded, rotating
authenticated scan without inference. Mixed or unknown structural debt remains.
This does not establish that any recovered locale has been published. Actual
translation repair still requires its exact source/producer/checkpoint proof and
a separately verified resulting candidate.

## Validation evidence

Regressions cover bidirectional decimal/group conversions, arbitrary fractional
precision, thousandfold changes, fullwidth and Arabic numeric symbols, malformed
prefixes and mixed separators, French numeric lists, currency/rate/sign/count
preservation, same-model cache revalidation without inference, and registered
checkpoint revalidation. Existing French grouping and quarter tests remain.

The initial four-locale repair passed an independent 924-case matrix. A follow-up
read-only audit covered the complete 33-locale inventory using installed CLDR
samples: it reproduced the same comma-decimal thousandfold error in the ten
additional comma locales above, plus whole-token splitting in six Indian-group
locales. Those exact failure classes are covered by this extension, including
all 33 locale samples and prior-cache rejection without model calls. The final
local CLDR matrix passed 6,897 checks: 33 locales, 11 values, six quantity forms,
both directions, thousandfold-change rejection and native percent placement.
The currency cases combine formatted numbers with explicit `USD`/`EUR` text;
they do not claim coverage of every locale-specific currency/accounting layout.
An independent review additionally passed 4,536 Indian-group checks plus 60
malformed-group cases, including native and fullwidth decimal digits.

These deterministic checks do not assert that every model translation is correct
or that historical source fallbacks have been repaired. Existing cache identities,
producer concurrency and source receipts remain unchanged. Numeric-only SEO
publication eligibility follows the new policy above; actual translation repair
still requires a verified translated result.

