# Original-source support for numeric article titles

The retained-title inspection of run `38059753648` found one unique base-valid
saved candidate for ordinal 38. Its additional numeric token was absent from the
filename, 2,200-character selector excerpt and complete generated article, but
present in the authenticated OCR source. This observation alone did not authorize
the claim: matching a number somewhere in a report does not establish its subject,
metric, unit or period. The inspection made zero provider requests and zero object
writes. Production revalidation and downstream WeChat/Blog acceptance remain
separate checks.

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
