# Original-source support for numeric article titles

Last reviewed: 2026-10-11.

The retained-title inspection of run `38059753648` found one unique base-valid
saved candidate for ordinal 38. Its additional numeric token was absent from the
filename, 2,200-character selector excerpt and complete generated article, but
present in the authenticated OCR source. This observation alone did not authorize
the claim: matching a number somewhere in a report does not establish its subject,
metric, unit or period. The inspection made zero provider requests and zero object
writes. The later production revalidation receipt below distinguishes the actual
numeric-boundary fix from this additional semantic-support capability.

This document concerns source-grounded original article titles. SEO
multilingual prose follows the separate advisory
[quantity policy](financial-quantity-translation.md): a prose-number difference
does not by itself block translation or publication. That SEO policy does not
remove the title evidence, source identity, structure or publication contracts
described here.

`title_source_claim_support.py` supplies a deliberately bounded additional route
for missing numeric evidence. The normal title selector retains its candidate
order, faithful title, required-term, English ratio, coverage, name and contrast
gates. The original source is never concatenated into the ordinary evidence token
bag. The new route requires:

- A typed source context with the exact filename and source-byte SHA-256. The
  ordinary producer constructs it from its source text; retained OCR recovery
  constructs it only after the existing exact file/source receipt checks.
- A complete numeric atom, including sign, range and explicit currency/unit. Bare
  numeric mentions, ambiguous standalone scales and unrecognized formats do not
  authorize a claim. Equivalent spelling such as `percent`/`%` is explicit; this
  path does not infer company aliases or convert arbitrary financial quantities.
- A complete source sentence or line of at most 600 characters. Tables, combined
  paragraphs and cross-sentence windows cannot supply support.
- Within that same sentence: literal subject words shared by the candidate and
  filename, every required technical topic, one recognized metric, and matching
  direction, negation, forecast/uncertainty state, calendar/fiscal year, quarter
  and YoY/QoQ basis. Bound/approximation forms are currently rejected rather than
  normalized into exact values. Multiple amounts,
  comparison language and additional capitalized subjects are rejected. Each
  numeric claim uses its own title clause, so an unrelated entity in another
  clause cannot supply that claim's evidence.
- Both the candidate and original sentence must have a direct subject/topic →
  single metric → quantity structure. The entire prefix must contain exactly the
  ordered literal subject and required-topic tokens, with the same subject order
  in the filename (with only possessive or generic
  product wording); the intervening relationship words and trailing period/basis
  syntax are bounded. Reporting attribution, customers, unknown prepositions and
  a third subject fail regardless of capitalization. Co-occurrence in one sentence
  is insufficient. Inspection reports the candidate/direct-source stage separately.

This small recognizer intentionally leaves unsupported or ambiguous language
unready. It cannot infer a missing unit, translate an entity name, or establish an
unrecognized relationship. Content-free inspection exposes stage counts to
distinguish absent quantity, subject, topic, metric, state and unambiguous evidence
without disclosing the title, number or source text.

Title length handling now retreats before a whole numeric atom rather than cutting
inside it. Punctuation inside a range or thousands grouping is not a title-clause
boundary. A second raw-to-clean check rejects any newly introduced or changed
quantity; dropping an entire quantity is reported separately and remains subject
to the unchanged title quality and source gates.

`generate_wechat_article` passes its original source into every bounded title
selection round, covering both ordinary MinerU and recovered OCR sources. The new
helper is hashed by the future generation contract. Request budgets and unknown
pending-request handling are unchanged.

For the historical 44-report package, the explicit retained-response revalidator
keeps the existing archive/context/source/body/old-contract pins. It consumes only
the four already saved title responses. Inspect has zero object writes and zero
provider POSTs. Apply remains unavailable until the selected saved candidate and
the entire 44-article package validate. It changes only ordinal 38's title/H1 and
binding metadata; the other 43 articles, non-H1 body, original source, prompt,
assets and every Progress file must be byte-identical. The private proof binds the
new validator/helper digest, old source identity and saved request/response hashes;
it is excluded from the article handoff. The existing standalone delivery workflow
then performs WeChat/Blog delivery after a separately verified successful apply.

## Production revalidation receipt

PR #335 merged at `30169f6` after all seven cloud checks succeeded. Real inspect
run `38062695853`, job `114244017112`, returned `revalidation_ready=true` with
44 completed articles, 43 unchanged articles, zero provider POSTs and zero object
writes. Apply run `38062813064`, job `114244354526`, returned `applied=true` with
the same 44/43 counts and zero provider POSTs. Both private object writes were
verified: the generation checkpoint and complete article handoff. The shared
revalidation proof SHA-256 is
`26e499e12ec01b4ca2bb1c168489f9929fc9c055e6cd97accaf6d2b44d3eda9d`.

The actual selected saved proposal was response 4, candidate 3. Whole-quantity
truncation reduced it to 34 characters: one complete quantity before the length
limit, none afterwards, one whole quantity removed, and zero introduced/changed
quantities. Required terms and the original hook gates passed. The bounded
original-source semantic-support route was **not used** to admit this title;
this production recovery was enabled by preserving numeric boundaries during
length handling. Its strict additional evidence route remains available for
future eligible claims, with unsupported language staying unready.

The retained body and four title responses were reused with no extra model call;
all old Progress bytes and the other 43 bound articles were preserved. Standalone
delivery run `38062937361`, job `114244980478`, has verified 44 draft articles
in six WeChat groups with 44/44 source reports accounted for and no exclusions.
Archive commit `a1dec872d156e505094e77bd4df582a95b02db5e` is recorded. Exact
publication request SHA-256:
`e9a0235e0044d50bb711896caa981d61e10fcf653edca22815274c9b94e89eae`.

Production release run: `38072861358`; immutable release:
`a7fc76874f6643ccc275778311837bcd`. Cutover succeeded at 2026-10-10 19:42:50 UTC.
New 44-article live acceptance passed at 2026-10-10 19:44:13 UTC: all
canonicals and complete normalized body/reference hashes matched, with unchanged
edge release/tree identity before and after readback. This independent read
made zero provider calls and zero production writes. Receipt SHA-256:
`085399b6aa2ade200cd7c731d063bffd7f53ee76b114b2d6217912876522ea42`.
This public receipt is separate from title revalidation and from the earlier
118-article / 16-draft-group snapshot. Those 118 articles also passed a fresh
full readback on this same release at 2026-10-10 19:46:02 UTC; the two cohorts
therefore total 162/162 verified live articles. The hash-only request alone was
not publication proof.
