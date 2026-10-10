# Financial quantity validation in localized translations

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
| `fr` | comma | narrow no-break space; existing regular-space and NBSP aliases retained |
| `es`, `de`, `id` | comma | dot |
| `en` and existing unscoped callers | existing rules retained | existing rules retained |

Only these four exact target/source language identifiers enable the new grammar.
Unknown language tags do not acquire these rules implicitly. Existing French
quarter recognition remains; no additional quarter aliases or other language
grammars are introduced in this change.

For these four locales, a comma is decimal even with three or more fractional
digits: English `0.125%` equals localized `0,125%`, while English `125%` must fail
against that same localized text. A locale-specific indivisible number token
prevents `0,000125` from being split into unrelated quantities `0` and `125`.

Complete dot groups in `es/de/id`, such as `1.234` and `1.234.567,50`, are
normalized once to `1234` and `1234567.50`. A well-formed three-digit dot group
always retains its locale meaning. It cannot simultaneously mean an English
decimal based on the source value. Unambiguous dot decimals that do not match
the grouping grammar, such as `0.125`, `12.34` and `1234.567`, retain compatibility
with prior untranslated numeric notation.

French grouping is checked before Unicode normalization can collapse different
space characters. Numeric width and Unicode decimal digits are normalized without
discarding that distinction. Explicit Arabic grouping/decimal symbols retain
their own meaning. Comma-separated or whitespace-separated decimal lists are
validated piece by piece, so a valid first number cannot hide malformed later
mixed separators. Recognized malformed localized decimal runs produce the fixed
`invalid_numeric_format` failure, even when both inputs contain the same malformed
form. Other version-like dotted text retains the existing scanner behavior.

Currency, scaled amounts, percentages, percentage-point changes and basis points
remain distinct. Added, omitted, duplicated, sign-changed or magnitude-changed
quantities continue to fail. Invalid-format diagnostics contain a fixed
`invalid_number` fact with no source text; a downstream public diagnostic that
does not recognize this fact reports its signature as unavailable.

## Cache and publication boundaries

The model identity and `extended-static-v2` checkpoint identity are not bumped.
This avoids discarding successful work or implicitly scheduling historical
translations. Reuse has several distinct gates:

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

Existing exact-source fallbacks remain terminal under their original policy.
This parser change does not erase render receipts, clear quality debt, retry old
failed units or establish that any recovered locale has been published. Existing
fallback recovery still requires its exact source/producer/checkpoint proof and
a separately verified resulting candidate.

## Validation evidence

Regressions cover bidirectional decimal/group conversions, arbitrary fractional
precision, thousandfold changes, fullwidth and Arabic numeric symbols, malformed
prefixes and mixed separators, French numeric lists, currency/rate/sign/count
preservation, same-model cache revalidation without inference, and registered
checkpoint revalidation. Existing French grouping and quarter tests remain.

Independent review additionally exercised 924 combinations across the four
locales, numeric values, quantity forms, both directions and changed magnitudes.
These deterministic checks do not assert that every model translation is correct
or that historical source fallbacks have been repaired.
