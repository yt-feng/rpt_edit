# Market Views source recovery

## Primary architecture

Market Views uses **MinerU API parsing on GitHub Actions** as its primary source
pipeline. The Daily report workflow selects the exact bank PDF batch, preserves
source/task bindings, retrieves complete MinerU results, generates report
articles and hands complete shards through private R2 to
[`market-views-latex-pdf.yml`](../.github/workflows/market-views-latex-pdf.yml).
The Market Views workflow synthesizes and renders the PDF, archives the exact
private version, commits its validated public-safe copy and exposes the dated
catalogue entry. Scheduled processing and recovery run in the cloud; the user's
computer is not a production dependency. The repository architecture map is
[Automation Pipeline Overview](pipeline-overview-v2.md).

```mermaid
flowchart TD
  A["Actions: select exact dated original PDFs"] --> B["MinerU API and durable R2 task ledger"]
  B --> C["All original task members completed"]
  C --> D["Private R2 cache; otherwise strict HTTPS with known expired-certificate recovery"]
  D --> K["Validate complete ZIP and persist verified bytes in private R2"]
  K --> E["Generate complete report articles and private R2 shards"]
  E --> F["Actions: Market Views synthesis and PDF"]
  F --> G["Exact PDF, original figures, private archive, public-safe commit"]
  G --> H["Verify dated live catalogue entry and PDF download"]
  A -. "Retained cloud original-PDF backup" .-> I["Actions backup: readable native text; opt-in cloud OCR for other pages"]
  I -. "Complete source, original-page and numeric evidence" .-> J["Separate private R2 backup handoff"]
  J -. "Verified backup only" .-> F
```

Provider completion, result retrieval, complete handoff, PDF creation, public
commit and live delivery are separate acceptance steps. A green workflow or a
MinerU `done` row does not establish that the next step succeeded. Partial
original batches do not release result rows to generation, even when the
requested subset has completed. See
[MinerU in-flight recovery](mineru-inflight-recovery.md) for the exact gates.

## Recovery within the MinerU chain

The durable client can move to another configured key only after HTTP 401 or
explicit `A0202`/`A0211` authentication rejection without a submission
acknowledgement. It saves the rejection before trying another key. Accepted
tasks retain their original credential, batch ID, PDF bytes and complete batch
membership. Polling failures, timeouts, parsing failures, conflicting
acknowledgements and ambiguous submissions do not authorize resubmission.
Changing a key cannot fix a shared result-download certificate.

The explicit cloud recovery entry is
[`market-views-mineru-recovery.yml`](../.github/workflows/market-views-mineru-recovery.yml).
It verifies the exact original artifact, manifest, PDF bytes and original task
membership. Every completed original ZIP must be retrieved and verified before retrying a
failed member. A reviewed failure code or exact message hash authorizes at most
two durable child attempts; only failed members are submitted. Original task and
source records retain their original identity and credential. Ambiguous
submissions and pending children block further submissions. Recovery releases
sources only after every original member is covered by a successful original or
child result. Its separate private receipt binds the complete source inventory,
result files, lineage, recovery run and executing commit before PDF synthesis.

The one-page cloud smoke test
[`mineru-api-smoke.yml`](../.github/workflows/mineru-api-smoke.yml) exercises a new
synthetic PDF through parsing and complete ZIP download, then verifies fixed text
and numeric evidence. It has an independent task scope and a per-run immutable
source guard; rerunning an accepted or ambiguous task cannot create another parse.

Use cloud read-only diagnostics to distinguish current credential/API health,
task state and result retrieval. The diagnostic entry is **Diagnose MinerU API
and saved results**
([`mineru-api-diagnostics.yml`](../.github/workflows/mineru-api-diagnostics.yml)).
It reads the exact retained private inspection receipt, probes each configured
credential, and checks result-host TLS/HEAD responses plus an optional four-byte
ZIP prefix. Its safe summary separates `historical_tasks`, `authentication` and
`result_download`; a prefix probe explicitly reports `full_zip_verified=false`.
It submits no parsing task, changes no canonical claim and sends no email.
Authentication, new parsing and result delivery require separate cloud probes;
a successful small download probe does not establish complete ZIP retrieval.

The existing
[`mineru-durable-inspect.yml`](../.github/workflows/mineru-durable-inspect.yml)
reads exact original tasks and preserves their complete provider response in a
separate private R2 receipt. The receipt layout, diagnostic inputs and historical
inspection identity are documented in
[MinerU in-flight recovery](mineru-inflight-recovery.md).
Public failure counts and message hashes do not establish a provider error's
cause.

## Private R2 result persistence

The private result cache in `scripts/mineru_result_cache.py` is shared by the
R2-backed Dropbox parser and the exact-task recovery path. Its immutable identity
binds the frozen PDF bytes, source options and original or recovery-child task.
It does not use a signed result URL as the identity. A successful complete ZIP is
validated, saved with its SHA-256 and read back immediately, before article or PDF
generation. A later report failure therefore retains the earlier source result.
Reruns still verify current provider task membership and the complete original
batch; a matching cache hit supplies the ZIP without another CDN download.
Corrupt or mismatched cache evidence stops processing rather than substituting
another source. Raw ZIPs remain private and outside public handoff artifacts.

### Automatic recovery for the known expired result certificate

The main daily workflow and `market-views-mineru-recovery.yml` now use
`mineru_daily_result_transport.download_result` on a result-cache miss. Normal
PKI is always attempted first. Only the exact `tls_certificate_expired` category
can enter a separate cloud-main recovery path for
`cdn-mineru.openxlab.org.cn`, leaf SHA-256
`12137420c572ee3fde42af27309c8f36efdfc4d07e76dcba801ddf6bc308aeb3`.
An independent strict handshake must reproduce depth-zero certificate expiry,
the leaf bytes must match, intermediate certificates must be currently valid,
and system and certifi roots must both verify historical server-purpose and
hostname identity. The dedicated result connection itself asserts the same leaf
fingerprint, with no redirects or API credentials.

Each attempt has a fresh lease of at most 15 minutes, bounded further by the
intermediate certificate expiry. Connections and body reads enforce it. This
policy does not extend or reuse the historical manual-seed cutoff. Once a normal
provider certificate succeeds, recovery is not used. A changed untrusted leaf,
another hostname, generic TLS error, timeout or HTTP error cannot enter it.

After full ZIP validation, `mineru_daily_result_cache.py` writes an immutable
authentication sidecar binding the source/task identity, ZIP hash/size and lease
facts, then the normal result cache persists and reads back the ZIP. The sidecar
records historical authentication and `pki_verified_now=false`; it never claims
that the vendor certificate was renewed. Its receipt-hash key permits a fresh
attempt after an interruption without overwriting earlier evidence. Cache hits
continue to work after old leases expire and require no download connection.

The one-page API smoke workflow is the only additional allowed caller. Its
synthetic source uses an independent private namespace, checks known text and
three numeric values, saves the complete ZIP, and immediately replays it from
R2 with downloading disabled. An accepted task is resumed rather than reposted.
Cloud acceptance is recorded separately from offline regressions below.

PR 259 merged at `f08dce92` on October 5 at 18:10:33 UTC after all five cloud
check jobs passed, including source recovery and API smoke contracts. Live
one-page workflow `37353991034` completed successfully at 18:11:46 UTC on that
exact main revision. All four credential slots loaded; one task was accepted,
one PDF completed and no member failed or remained pending. The known expired
leaf was freshly authenticated at 18:11:39 UTC, and the complete 16,941-byte ZIP
passed extraction, marker and three-value checks. The receipt explicitly
retains `pki_verified_now=false`; the supplier certificate remains expired.

Private R2 write/readback and the immediate original-task cache replay passed.
The initial attempt submitted exactly once; replay submitted zero times and
downloaded zero result ZIPs. Its synthetic ZIP SHA-256 is
`75c7b9781c678d8c179543fa4380512e54a17a4596ea79ed4b411bf64d363e74`.
This is live acceptance of the shared primary download mechanism and R2
continuation, distinct from a new full scheduled Daily-to-PDF publication.
The same workflow's second job attempt then passed on a fresh runner. It hit
the persisted cache before any result download, submitted zero parses, and
reproduced the first attempt's PDF/ZIP/Markdown hashes and authentication
receipt exactly. Its further original-task replay again recorded zero
submissions and zero downloads. This confirms continuation across runner loss,
not only an in-process replay.

R2 is also checked for existing source-generation checkpoints and exact final
PDFs through `market-views-r2-cache-inspect.yml`. A checkpoint identity and archive
hash are not by themselves proof that it matches the current original batch;
complete source bindings must be verified before reuse. The independent
`mineru-cloudflare-tls-probe.yml` creates an authenticated temporary Worker to
make one strict HTTPS HEAD request to the public MinerU result CDN. It does not
download a ZIP or mirror it into R2. A valid HTTP response identifies another
potential cloud retrieval path; invalid-certificate or fetch failure still
requires further resolution before any missing source can enter R2.

The manual probe accepts `default`, `gcp:asia-east1` or `azure:southeastasia`
placement for its newly created temporary Worker. Region hints use Cloudflare's
[documented placement API](https://developers.cloudflare.com/workers/configuration/placement/)
without changing the official result hostname or HTTPS verification. The
incoming request's `request.cf.colo` records ingress only. Execution location is
reported only when the platform supplies a valid `cf-placement` response header;
a requested region does not prove execution there. Every probe retains one
provider HEAD, zero result ZIP downloads, zero parsing submissions and cleanup.

The independent `mineru-result-tls-probe.yml` also records two strict public-host
OpenSSL handshakes: default negotiation and a TLS 1.2 RSA diagnostic. Each makes
one TLS connection and no HTTP request. The bounded peer-provided certificate
chain records public subjects, issuers, validity dates and fingerprints plus
verification code/depth. This is distinct from a constructed trusted chain and
from complete ZIP validation. The parameters apply only to that manual cloud
diagnostic; production TLS configuration is unchanged.

The separate manual-only
[`mineru-result-cache-seed.yml`](../.github/workflows/mineru-result-cache-seed.yml)
can retrieve completed original tasks with a fixed, previously observed leaf
certificate identity. This cloud recovery is limited to
`cdn-mineru.openxlab.org.cn`, SHA-256
`12137420c572ee3fde42af27309c8f36efdfc4d07e76dcba801ddf6bc308aeb3`,
and the fixed cutoff `2026-10-05T23:59:59Z` (the original October 4 window was
extended once as recorded below). It first verifies the exact leaf and
peer chain against system and certifi roots at the last instant before that
leaf's expiry, including server purpose and hostname. This is historical chain
verification plus exact-leaf authentication; it is explicitly **not current PKI
verification**. The dedicated connection asserts the same leaf before HTTP,
rejects redirects and other origins, and checks the cutoff before connections,
body reads and private R2 writes. This manual policy is independent of the
automatic daily recovery described above.

Before downloading any ZIP, the seeder verifies the full original Daily
artifact, every PDF hash/date binding and all accepted original task members
through read-only provider lookups. It makes no parsing submission or canonical
ledger write. The default one-result canary validates the complete ZIP, stores a
separate immutable authentication receipt and the existing immutable result
cache, and reads both back. The `all` option covers completed original results;
failed members remain failures and still require the bounded recovery path.
The cache-only summary cannot establish a complete handoff or restored PDF.
The new transport requires cloud canary validation before it is reported as
working, and it cannot extend its own cutoff.

Optional accepted-child mode supplies three independent inputs: the exact
completed manual recovery run ID, reviewed provider failure-message hashes,
and the expected complete original manifest hash. It verifies the recovery's
main-branch workflow identity, existing controller policy and each fresh
predecessor result/proof before selecting that run's already accepted completed
children. Earlier children can prove an ordinal-2 predecessor but cannot become
the selected run's output. Every child lookup disables terminal persistence;
the seeder never creates a child, retries a parse or changes a canonical record.
Child ZIPs use the same production cache lineage and fixed authentication cutoff.

The bank source date owns the Market Views issue. Auxiliary sources use the
latest usable date on or before that bank date; a future auxiliary date cannot
rename or suppress the bank issue. Private handoff run IDs and report/shard
counts are validated before materialization.

## Retained cloud backup and its current limits

The original-PDF branch is a backup for Market Views. Its deployed implementation
uses readable native PDF text, original exhibit pages and explicitly enabled
cloud OCR for otherwise unsupported pages. It makes no MinerU submission and
runs on GitHub Actions. It preserves the failed report-notes conclusion;
WeChat and translation keep their normal completion gates. It is not the primary
parser and does not depend on local OCR or a user's computer.

The original backup rejected duplicate contents and scanned pages with zero
native text. The opt-in extension
retains every exact filename and SHA-256 binding while extracting and summarizing
identical PDF contents once. It checks readable language and table structure,
rather than admitting opaque strings solely by character count. Encrypted or
damaged PDFs, incomplete inventory and mismatched bytes still reject the batch.
Unsupported pages require `--enable-ocr`; full-page Tesseract OCR uses
`eng+chi_sim` at 300 dpi, retaining the original page image, raw transcript,
page coordinates, model hashes and rendering provenance. An all-white page is
accepted only with empty native text and pixel evidence.

Independent full-page and cropped numeric reads compare source positions and
actual decimal, minus, percent and negative-parenthesis pixels. Confirmed values
can enter source summaries; conflicting or omitted fields remain explicit
`[数值待核对:...]` markers with private evidence. The model must not guess or
calculate with those fields. This evidence is checked again by the PDF consumer.
The schema-2 receipt also binds the date, producer run, executing commit and
original Daily source run before synthesis or an existing-PDF skip. Report
coverage distinguishes all original file aliases from unique-content summaries.
Numbered source captions select original full-page images; uncaptioned visuals
are not inferred or redrawn.

The old eight-file experiment remains preserved as an immutable
[experimental backup patch](experiments/market-views-ocr-fallback-20261004.md).
The current implementation adds cloud dependencies and stronger gates. Local
tests do not establish cloud recovery or publication; real OCR regression
dependencies are mandatory in CI, and full actual-report quality review is
required before enabling daily OCR backup. The daily variable was enabled and
read back at 16:06 UTC on October 5 after complete October 2–4 source and PDF
acceptance. October 1 special-page acceptance remains open; the full-source and
numeric gates still reject any batch that does not pass.

### Bounded original-page edition when structured extraction is unavailable

The Daily workflow keeps MinerU and its validated private cache as the primary
path. Failed matrix work is inspected by `source-outcome`; job-level error
tolerance never admits an incomplete notes handoff to drafts, translations or
chart indexing. Complete native/OCR receipts remain the first backup. If those
gates fail, the selected original PDF artifact can produce a separate
`source-pages` handoff without OCR, model calls or another MinerU submission.

This edition is labelled **Market Views 备用来源版（解析服务异常）** on its cover,
every source page and the private catalogue item. It contains a source directory
with original PDF SHA-256 and original page positions, plus at most two full-page
images per report, 120 source pages and 64 MiB of JPEG images in total. Selection
looks only at the first 20 pages, preferring nonblank pages with native market
keywords; scanned reports use their original page order. These are partial source
excerpts, not verified summaries or a claim of complete report coverage. Every
omitted source remains recorded in the directory. An entirely blank/unreadable
batch, changed source hash or failed output validation remains a failure.

The consumer validates the exact main Daily producer, successful preview upload
gates and receipt/image hashes before rendering. It opens and rasterizes the
actual resulting PDF, archives it privately, publishes the safe copy and reads
back the private PDF/metadata pair. Only completion of that downstream job lets
`validate-market-delivery` accept a degraded Daily delivery. Existing complete
same-date publications are retained; recovered primary processing upgrades an
earlier source edition. Failed parsing records and successful MinerU cache entries
are unchanged. A deduplicated 24-hour exception email uses the existing operations
mail Worker; an email failure does not invalidate an already verified PDF.

[`market-views-native-recovery.yml`](../.github/workflows/market-views-native-recovery.yml)
accepts an exact `date_folder` and `expected_articles`, with `enable_ocr=false`
and `generate_pdf=true` defaults. `generate_pdf=false` performs complete source
validation and private R2 handoff without synthesis or model calls, retaining
the handoff for quality review. Daily OCR fallback uses the separate repository
variable `MARKET_VIEWS_OCR_BACKUP_ENABLED`; absent or false leaves OCR disabled.
`source_run_id` reuses the
original Daily report artifact; with no source run ID it downloads that exact
Dropbox date and binds a fresh manifest. It does not classify or submit those
PDFs to MinerU. A complete source receipt is checked before synthesis or an
existing-PDF skip. Backup handoffs use a separate private R2 prefix; temporary
inputs are deleted only after their PDF consumer succeeds, and failed/cancelled
consumers retain their inputs.

## Historical incident evidence

The run states in this historical section are superseded by the current
acceptance summary below. The public catalogue observed on 2026-10-04 had `market-view:260930` as its newest
entry. Saved Daily report diagnostics after that date show late Dropbox batches,
terminal MinerU failures and a result-download certificate failure at
`cdn-mineru.openxlab.org.cn`. The 2026-10-03 inspection of run `37159099752`
counted 36 provider-completed PDFs and 18 terminal failures. The specific cause
of those 18 failures remains unverified. The certificate error was observed while
retrieving already completed results; it does not establish current API health.

Four configured MinerU key slots were loaded in the saved run. The token page
was observed in Chrome on 2026-10-04 with four valid tokens and one older token
expired on October 2. That view does not establish which credentials the
historical tasks used, or that every API endpoint and result host is healthy.

Cloud diagnostic run `37211677994` verified all four configured key slots through
authenticated task lookup on 2026-10-04. The retained 18 failures were classified
from actual provider messages as `provider_internal`, with no supplied error code.
The first retained completed ZIP's host still failed certificate validation as
expired; no result GET or new task POST followed that failure.

Cloud smoke run `37212761333`
accepted and completed one newly uploaded synthetic PDF on 2026-10-04. Its
result download then failed with `tls_certificate_expired`, with zero downloaded
bytes and `complete_zip_verified=false`. This directly establishes current
authentication, upload and parsing success for that task. It also reproduces the
result-delivery blocker independently of the historical failures. The smoke task
is retained durably; rerunning the same run reuses its accepted task instead of
submitting another PDF. Complete dated Market Views delivery is still unverified.

The deployed exact-source recovery was exercised in run `37214015946` using the
54 selected originals from Daily producer `37159099752`. Its source recovery
step stopped with `tls_certificate_expired` before reaching child submission or
PDF generation. The bounded recovery code was merged in PR 220; the original
36 completed results therefore still require valid result delivery.

PR 221 was merged after ordinary GitHub access resumed. Cloud comparison run
`37217880580` at 2026-10-04 16:45 UTC independently checked the public result-CDN
root using the system CA store and certifi `2026.07.22`. Both strict clients
reported `tls_certificate_expired`, with no HTTP response or body bytes. This
rules out a failure confined to the older system trust store; it does not prove
that every CDN edge serves the same certificate or restore any dated issue.

PR 222 merged the complete-ZIP result cache and the cloud R2/Cloudflare
diagnostics at commit `4c7ae7abc53cb25f977491b5c9ae44a8af5658a6`. Read-only R2
inventory run `37219229168` completed successfully on 2026-10-04 17:06 UTC. For
each of `261001`, `261002` and `261003`, the exact generation-cache and original
producer-handoff prefixes had zero objects, with complete listings; canonical
final PDF/item objects were also absent. This is evidence for those configured
paths, not a bucket-wide assertion. Existing ledger task metadata cannot replace
the missing source material.

The first temporary-Worker run `37219241529` created and enabled the isolated
Worker, but its immediate `/probe` request returned HTTP 404. The run then deleted
the Worker successfully. No MinerU result response or ZIP was verified. Worker
deployment propagation must be distinguished from an upstream CDN failure; the
probe now checks an authenticated `/ready` endpoint that makes no provider
request, allowing only bounded deployment-404 waits before its single CDN HEAD.

PR 223 merged the readiness check at
`d0138a57a32e4722eb65c57914434647d1d52ee6`. Cloudflare run `37229206987` on
2026-10-04 19:42 UTC received readiness HTTP 404 then HTTP 200 after five seconds.
Its authenticated handler then made exactly one strict HTTPS HEAD to the official
CDN root and received HTTP 526 (`tls_invalid_certificate`). The recorded LAX
value identifies request ingress; that run did not separately prove execution location.
The temporary Worker was successfully deleted. Zero ZIP downloads, provider
POSTs and R2 writes occurred. This is CDN evidence, unlike the earlier deployment
404, and does not establish the certificate state of every possible CDN edge.

Attempt 2 of smoke run `37212761333` at the same time resumed the existing
completed one-page task with zero provider POSTs. Authentication was accepted
and the task still had one completed result; result retrieval again stopped with
`tls_certificate_expired`, zero ZIP bytes and no marker verification. Thus a
Cloudflare-to-R2 mirror has no verified upstream delivery path in these probes.
The new ZIP cache prevents loss of future successful downloads but does not
restore currently absent source bytes. A valid official result download path is
still required before the missing dated PDFs can be built.

Attempt 3 of the same smoke run at 2026-10-04 19:57 UTC retained the existing
completed task, made zero parsing POSTs and again stopped at download with
`tls_certificate_expired` and zero bytes. Separately, a read-only TLS handshake
to the same official hostname observed a valid Let's Encrypt YR1 chain with leaf
validity 2026-09-17 through 2026-12-16. That handshake did not retrieve a result
ZIP and does not establish runner or Cloudflare retrieval success. These
different observations require testing a legitimate cloud retrieval path rather
than describing every CDN edge as expired. Regional Cloudflare probes are
available for that test; region selection alone is not success evidence.

Readiness-verified regional run `37231111280` used `gcp:asia-east1` and the
platform reported `cf-placement: remote-TPE`; its single strict HEAD received
HTTP 526. Run `37231384448` used `azure:southeastasia` with
`cf-placement: remote-SIN` and also received HTTP 526. Both temporary Workers
were deleted successfully, with zero ZIP downloads, provider POSTs or R2 writes.
Thus the tested Taipei and Singapore cloud routes have not provided a valid
upstream ZIP for an R2 mirror.

Runner certificate-chain diagnostic `37232259586` on 2026-10-04 received the same
`*.openxlab.org.cn` leaf issued by RapidSSL TLS RSA CA G1 in both default and
TLS 1.2 RSA handshakes. It expired at **2026-10-02 23:59:59 UTC**; both handshakes
reported verification code 10 at depth 0, identifying the expired website leaf.
The independently observed valid Let's Encrypt chain on another connection does
not verify runner ZIP retrieval. These diagnostics downloaded no complete ZIP.
For the primary MinerU chain, verified upstream ZIP bytes must be retrieved
before R2 persistence can supply the missing source.

PR 228 merged at `f7c5a0097b86a37670c54b91c2988bd8b2557deb`. The independent
GitHub-hosted macOS ARM64 diagnostic `37233771704` at 2026-10-04 20:53 UTC also
failed strict validation. Default and TLS 1.2 RSA handshakes received the same
RapidSSL leaf and peer chain as the earlier runner, with leaf SHA-256
`12137420c572ee3fde42af27309c8f36efdfc4d07e76dcba801ddf6bc308aeb3` and code 10
at depth 0. Neither system CA nor certifi retrieved an HTTP response or ZIP bytes.
Changing the cloud runner OS therefore did not restore the tested download path.
The same accepted synthetic task was checked again in smoke attempt 4 at
2026-10-04 21:28 UTC: authentication and parsing still passed, no new task was
submitted, and strict result retrieval again failed with
`tls_certificate_expired`, zero downloaded bytes and no verified ZIP.
The [provider incident draft](experiments/mineru-result-download-incident-20261004.md)
is prepared but remains unsubmitted; submission permission has been requested
and no approval has been received.

The earlier 2026-10-03 22:34 UTC inventory note recorded `261002=4`; that count
was not independently revalidated and is superseded by the complete current
Dropbox listing and successful download of **50 PDFs** in `261002`. This does not
establish why the earlier count differed or that it belonged to another date.
Fresh recovery preserves Daily's default `selection_mode=all` scope; it must not
truncate the current batch to fit the earlier count. Run `37232193875` correctly
stopped before OCR because its expected count was still 4.

Original October 2 Daily run `37067138754` stopped at source intake: it expected
`261003`, found latest folder `261001`, and rejected age 2 against allowed ages
0–1. It downloaded no original October 2 batch and reached no MinerU parsing;
that run cannot supply an original-PDF recovery artifact for `261002`.

Current cloud source-only recovery runs are recorded separately from PDF
publication. They use `generate_pdf=false`; a successful handoff retains
original page and numeric evidence for review:

| Bank date | Source-only run | Bound original scope | Recorded state |
| --- | --- | --- | --- |
| `261001` | `37232969584` | Producer `36932674491`; 63 files, 62 unique contents | Failed at report ordinal 10, page 9; no complete handoff |
| `261002` | `37233084607` | Fresh exact Dropbox listing; 50 files; original source run explicitly empty | Failed at report ordinal 6, page 5; no complete handoff |
| `261003` | `37231899669` | Producer `37159099752`; 54 files, 1,029 pages | Failed during complete-source extraction; no complete handoff |
| `261004` | `37233077480` | Producer `37232504334`; 4 unique files, date and `content_sha256` verified | Source contract passed; private R2 handoff saved; consumer numeric fixture rejected |

October 4 source-only extraction completed successfully with all 4 originals
and 4 unique contents: 109 pages, including 82 native-text pages, 27 OCR pages
and no blank pages. Its source-contract audit passed, but
`fixture_acceptance=not_requested` means this run did not establish visual numeric
fixture acceptance. The receipt observed 1,775 numeric mentions: 1,334 primary
mentions (354 verified, 8 corrected, 972 unresolved) plus 441 secondary mentions.
In total 1,413 remained unconfirmed and excluded from usable numeric claims.
Successful source coverage is therefore separate from numeric quality approval.
Merged PR 229 adds consumer readiness and a known-field fixture audit,
including the visual `17%` field, before model synthesis. Its two focused test
suites passed 12 and 17 tests, respectively. PRs 228 and 229 are merged on main
at the recorded `0ead65e` state. Real October 4 consumer run `37235097133`
stopped with **`field_unresolved`** for the visual `17%` field; this was a numeric
fixture failure, not a fixture-input format rejection. It made zero model calls
and generated zero PDFs. The guard has now run against the real handoff, but
numeric quality and October 4 PDF/live delivery remain unaccepted.

October 3 run `37231899669` failed at 2026-10-04 20:55:55 UTC in “Extract and
verify the complete original source batch”, reporting a generic
`SourceValidationError` for report ordinal 24, page 49. The cause remains under
investigation against that exact source page. Visual inspection identified a
short disclosure-appendix divider. Earlier reports had already used
OCR successfully; this generic error does not establish missing Tesseract
models. The run produced no complete R2 source archive and reached neither the
complete-source auditor nor golden-fixture acceptance. October 1 source run
`37232969584` also failed at report ordinal 10, page 9; that original page is a
short Q&A divider. October 2 run `37233084607` failed at report ordinal 6, page 5;
its original page type has not yet been inspected. All three complete-source
extractions failed; none has a complete R2 handoff. PR 230 merged the narrow
short-structure OCR fix at `2bebbacb`, with all 43 source tests (including six
actual cloud OCR cases) and 32 receipt-audit tests passing in cloud regression
`37236018141`. It also adds bounded numeric-only evidence for rejected fixtures.
This tests the failure class; it does not claim that the failed complete source
batches have been rebuilt. The October 2 failure is not assumed to have the same
cause.

The manual `market-views-ocr-field-probe.yml` workflow verifies a complete,
exact-date original Daily artifact and all original hashes before recognizing
only explicitly requested fixture pages. It uses the production field matcher
and emits sanitized numeric diagnostics. Its output always declares
`page_probe_only=true`, `complete_source_handoff=false`, and
`production_acceptance=false`; it cannot admit a partial source, invoke a model,
publish a PDF or provide a consumer handoff. This probe supports fast actual
field diagnosis before another complete-source run.

Real R2 diagnostic run `37236412568` isolated the October 4 rejection: the
original and 450dpi field reads were `17%`; the two 600dpi crop reads were
`317%` and `17%`. The wide crop included neighboring glyphs, while the percent
pixel witness was present. The numeric reader now isolates the 600dpi OCR crop
and records its clip, policy and pixel size. The independent, wider 300dpi
punctuation witness and requirement for three agreeing positioned reads remain
in place, and existing immutable receipts remain compatible. PR 231 merged at
`6fd7ae49d239f53bb5678ea4f07f0d518cf29fe8`; mandatory cloud regression
`37237898234` passed the source, numeric and real-pixel probe suites. Actual
field probe `37238121375` then verified the October 4 `17%` field against its
original page pixels. Probe `37238128801` verified all five October 3 table
fixtures, including `(3.1)%`, `4.8` and the three decimal EPS values. Both
verified their complete original inventories before recognizing those pages;
neither is a full source handoff. Complete-source reruns remain separate:
`37238241161` for October 4, `37238269283` for October 3, `37238287811` for
October 1, and fresh 50-file October 2 run `37238318559`.

PR 232 merged the fixed-policy manual cache seeder at
`955ff9f6cc3ed2342d9f810873c559717424fa1e`. Actual cloud canary `37238317495`
verified all 54 October 3 originals and all 11 accepted original groups
(36 completed members and 18 failed members), then retrieved one complete ZIP
of 7,848,078 bytes. Full ZIP checks, the separate immutable authentication
receipt and standard private R2 cache readback all passed. It made one result
GET, zero parsing POSTs and zero canonical task writes. Authentication was the
fixed exact leaf plus two historical chain/hostname checks, explicitly not
current PKI verification. Bulk original-result cache run `37238421286` then
verified and cached all 36 completed originals, totaling 182,020,443 ZIP bytes:
35 new downloads and one existing cache hit, zero parsing POSTs and zero
canonical task writes. The 18 failed members still require approved bounded
recovery. Recovery `37238694906` stopped with a generic `LedgerError`; that type
alone cannot establish which stage failed, because the durable child verifier
wraps nested failures. Child canary `37238922606` was rejected before source,
API or result retrieval by an incorrect static workflow-name check. Actual
GitHub metadata uses the expanded `Recover MinerU Market Views 261003` run-name;
exact date-bound metadata validation fixes that check.

October 4 complete-source rerun `37238241161` passed all 4 originals and 109
pages (82 native, 27 OCR), private R2 handoff, source contract and actual `17%`
fixture. Confirmed primary numeric mentions increased from 362 to 649;
1,126 of 1,775 observed mentions remain unconfirmed and excluded from usable
numeric claims. PDF consumer `37239371856` is a separate delivery step. October
3 rerun `37238269283` stopped at report ordinal 9, page 1 with
`NumericEvidenceError`; the earlier dependency wording did not identify its
cause. Fixed-category diagnostics distinguish unavailable language models,
OCR execution, numeric geometry/pixel/field validation and durable task/result
failures. Unknown exception text is never copied to public diagnostics; an
isolated actual-page probe is required before changing the numeric gate.

Recovery is complete only after the
matching cloud source and retrieval gates, exact dated PDF, original figures,
private archive, public-safe commit and live catalogue/download are verified.
Neither the retained native backup nor the saved OCR experiment establishes
that delivery has been restored.

The earlier real-source admission review checked all 54 original PDFs from producer
`37159099752`: each hash matched its original manifest, with 54 unique contents
and 1,029 pages. The stronger language gate classified 798 pages as readable,
21 opaque-string pages and 210 pages with insufficient native text. Approximately
231 pages therefore require cloud OCR. That inventory audit did not establish
OCR acceptance. Subsequent source run `37245279463` completed the full batch,
and acceptance-only PDF consumer `37284342786` succeeded. These backup checks
do not replace the recovered primary publication. Current backup acceptance
and daily switch status are tracked in the final section below.
## 2026-10-04 cloud delivery follow-through

The original October 3 result ZIP cache is complete: 36 original DONE results
were fully downloaded, validated and reread from private R2. Two already
accepted recovery-child results were subsequently cached with the same bounded
manual certificate identity policy. This does not prove normal current-PKI
download recovery, nor does it admit an incomplete source batch.

During manual recovery only, a terminal accepted child whose sole result
download failure is the exact `tls_certificate_expired` category may be retained
while the remaining authorized original groups continue. Other network errors,
original-result failures, unknown errors, and ZIP/cache/ledger validation errors
still stop immediately. An outstanding child ZIP prevents all complete-source
receipts and downstream model/PDF generation. A later run consumes verified R2
cache entries and reuses accepted child tasks without duplicate submissions.

The October 4 cloud OCR producer `37238241161` passed the complete four-original
source contract and the real 17-percent numeric fixture. PDF consumer
`37239371856` archived a private PDF and committed its public-safe counterpart
to main. The public file has 14 pages and nine source-page images; visual QA
found one caption separated from its image, addressed by grouping each image and
caption as one pagination unit. Rebuilding and live delivery remain separate
acceptance steps.

The read-only live inspection workflow verifies requested dates' private PDF
bytes and index metadata in full, compares the public portal list, and confirms
the anonymous membership gate. It never claims that a customer-authenticated
download was tested. The original/private and sanitized/public PDF hashes are
distinct identities and are not assumed interchangeable.

The exact October 3 semicap first-page OCR probe reports
`numeric_crop_geometry_mismatch`. Bounded geometry diagnostics preserve only
positions, pixel dimensions, strict check booleans, record ID and renderer
version so a subsequent cloud probe can identify the mismatch without exposing
report prose, names, tokens or URLs. No numeric acceptance tolerance was relaxed.

Manual native recovery preserves the complete original PDF inventory in a
separate private originals archive before extraction. Exact date, count,
manifest and every PDF hash are verified both before packing and independently
inside the sealed payload before its first R2 write. The entire decoded tar,
including PAX/GNU headers, is bounded. Immutable archive and receipt writes are
confirmed by full readback. Restoring requires the exact completed main/manual
native producer and receipt context, with no R2 writes. Seven-day expiry disables
application restore; it does not claim physical deletion or delete older data.

`archive_originals_only=true` requires `generate_pdf=false`, skips OCR and all
complete-source/model/PDF gates, and cannot pass native source readiness. It
provides cloud investigation material for an OCR failure without admitting an
incomplete source batch or repeating preceding reports' OCR.

The cloud field probe keeps exact Daily golden-fixture validation as its default.
An explicit `original-archive` mode may restore a complete immutable originals
archive from an authenticated native producer and inspect at most eight selected
pages. Page diagnostics publish only bounded readability and numeric counters,
safe categories, original hashes and page numbers. No-golden diagnostics are
labelled `fixture_acceptance=not_requested`; they never admit sources or claim
production acceptance. Repeated validation covers the entire archived batch,
including every unprobed original, before and after inspection.

The first safe October 3 crop diagnostic (`37241002063`) confirms matching clip
coordinates and 78-by-128-pixel dimensions; only the field-count validation
failed. Further bounded type/overflow diagnostics distinguish that cause
without changing the numeric admission rules.

### Authenticated legacy Daily result cache

An explicit `source_kind=legacy-daily` in the manual cache workflow handles
historical Daily producers separately from canonical durable tasks. Before any
result retrieval it authenticates the exact producer, the complete original
artifact and its GitHub digest, every original PDF hash, all shard job logs,
the reviewed historical source-code hashes and every accepted retry's fresh
terminal membership. A group must have one complete DONE task; successful
members from different retries cannot be combined.

The legacy provider's copied-filename data IDs remain unchanged in independent
private R2 proof, authentication and result-cache namespaces. This route makes
no parsing POST, canonical task admission, model call or PDF publication. The
fixed exact-leaf identity policy and its original UTC cutoff remain unchanged.
Immutable authority and authentication receipts and full ZIPs require complete
R2 readback. Source admission and dated PDF delivery require separate complete
consumer validation.

Read-only cloud inspection `37241467409` identified all 52 accepted October 1
tasks. The latest task for each of 13 original groups contains all 63 members
in DONE state. The original script's five-minute wait and token resubmissions
therefore did not establish that those PDFs had failed to parse. This inspection
alone proves neither original PDF bytes nor cache or PDF delivery.

October 3 child cache run `37241908963` verified and cached 15 additional
authorized DONE members without parsing POSTs. October 4 original cache
`37241582462` verified its three original DONE results. Full recovery and PDF
acceptance remain separate from these cache receipts.

### Preserve recognized glyphs when geometric OCR order joins labels

The native cloud backup keeps geometric text order as its default. Only when
that transcript fails the existing readability policy may it read source-flow
order from the same OCR TextPage. Both transcripts must contain exactly the
same non-whitespace characters, including every sign, punctuation mark and
repeated character, and the alternative must pass the unchanged readability
gate. Positioned words use the same selected order. Recognition and complete
numeric auditing are not skipped or repeated to manufacture readable prose.

Optional layout provenance binds both readability results, transcript hashes
and the selection into page metadata and the already hashed report status.
Transferred consumers recompute those bindings and reject deletion or mutation.
Default readable pages and existing immutable receipts retain their original
shape. Safe page diagnostics report both sorted and selected readability counts
without exporting recognized text. Actual failed-report pages and complete
source batches still require separate cloud acceptance.

Cloud diagnostic `37241773243` isolated the October 3 first-page rejection:
the 78-by-128 crop matches its expected geometry, but its PSM-11 field count is
an integer above the existing 2,500-field bound. The geometry label alone must
not be interpreted as a coordinate or pixel-dimension error; the bound remains
unchanged pending a producer-side investigation.

### Complete legacy sources and PDF consumption

`market-views-legacy-recovery.yml` authenticates the complete original Daily
artifact and all accepted tasks again, then reads every selected result from
the independent verified private cache. It never directly downloads provider
results, submits tasks or changes the canonical ledger. All original aliases
remain in the source receipt; byte-identical originals are summarized once.
Missing aliases, incomplete caches or changed task bindings reject the batch.

The complete source is archived under the dedicated legacy handoff prefix.
Its full R2 readback and exact manual/main producer, execution SHA, date and
count must pass before the existing PDF workflow accepts `legacy-daily`.
Native and durable source gates remain in place. Legacy receipts explicitly
retain `canonical_task_admission=false` and do not claim proof of the bytes
historically uploaded to the provider. Full original artifact authentication
and result membership are separate, recorded evidence.

October 4 backup PDF consumer `37241008754` completed its rebuild: the sanitized
PDF has 15 pages and nine original-page images, all visually verified with
captions on the same pages. Live inspection `37241582682` verified the private
PDF and index in full, matched the dated public catalogue entry and checked the
anonymous membership gate. Customer-authenticated download remains unchecked.
October 3 primary recovery `37242315004` has validated all 54 sources and
archived the complete source; its PDF consumer is `37242405117`. October 4
primary recovery `37242512036` likewise validated all four sources; its PDF
consumer is `37242538572`. Those primary PDF consumers require separate final
publication and live acceptance.

### Complete fresh intake before result retrieval

For a genuinely missed source date, `market-views-fresh-mineru-intake.yml`
restores an exact immutable original-only archive. It verifies every original
and creates a complete immutable intake authority, all planned canonical roots
and all original claims before the first parsing POST. It then accepts each
planned root at most once, without polling or downloading results. Accepted or
submitting roots cannot be submitted again; ambiguous submissions stop. A
later explicit resume can admit only the same authority's remaining planned
roots. The existing mixed-claims rejection in ordinary recovery is unchanged.

The manual cache workflow's explicit `source_kind=original-archive` authenticates
the same complete archive, immutable intake authority and every accepted root
before performing fresh GET-only terminal membership checks. Only then may it
cache DONE ZIPs, rechecking the unchanged source authority before each retrieval
and write. This route submits no task, changes no ledger and admits no partial
source. Its canonical identities retain the empty original Daily producer ID;
the native archive producer is a distinct, authenticated byte source. Ordinary
recovery starts only after all roots and claims have been accepted.

### Bounded isolated recovery for crop OCR overflow

Numeric crop reads now require a candidate's own bounding box to be contained
in its source crop, rejecting large mosaic boxes borrowed across rows. Only
when a crop's original positional count exceeds the unchanged 2,500-field
bound may that exact 600-dpi crop be read once more, with the same PSM and a
fixed white border. Continued overflow rejects the page; zero, multiple or
conflicting reads remain unconfirmed. The independent full-page read, both crop
PSMs and punctuation pixel witnesses retain their original acceptance rules.

Private, canonical recovery metadata binds the original lossless RGB crop,
isolated canvas, geometry, hashes and overflow lower bound. Consumers validate
bounded PNG decoding and reconstruct that canvas; they do not claim to have
reopened the original PDF. Default reads and existing receipts remain
compatible. Real failed-report fixtures and complete-source cloud runs are
separate acceptance steps.

Read-only `market-views-original-page-qa.yml` authenticates and restores a
complete private original archive, then exports only the explicitly selected
original page for visual review. An exact bounded RSA recipient certificate is
validated before source reads. The page PDF, PNG and hash receipt are encrypted
with an AES-256 CMS envelope; only ciphertext and safe hashes are Actions
artifacts. It performs no OCR, model call, task submission, ledger write or R2
source admission. The reviewer's temporary decryption key is not a production
pipeline dependency.

Original-page QA disables MuPDF's native error and warning channels during all
PDF open, render, page-copy, serialization and close operations, restoring the
prior settings on success or exception. Python stream redirection alone does
not suppress those native diagnostics. A real subprocess regression with a
valid original containing an unknown content-stream operator confirms that no
original operator token reaches workflow stdout or stderr.

### One full-page alternate recognition after unreadable default OCR

When both default OCR text orders fail the unchanged language policy, the cloud
backup may recognize the complete original RGB page once with fixed 300-dpi
Tesseract PSM 11. It preserves every returned TSV word and its geometry, records
both rejected default transcripts and binds the alternate engine, configuration,
models and full-page pixels. Engine or model errors stop; numeric failures do
not authorize another recognition. An unreadable alternate still rejects the
page. No page region is omitted or accepted by a reduced language threshold.

The transferred consumer rebuilds the selected transcript from the complete
word list, recomputes the default rejections and selected acceptance, verifies
the original-page pixel identity and replays every primary numeric position.
Independent 450-dpi and both 600-dpi numeric reads and punctuation witnesses
remain unchanged. Existing readable default and source-flow paths retain their
original receipt shape. Cloud diagnostics expose only bounded candidate counts
and reasons. Real affected report pages and a complete backup batch must pass
before enabling the daily OCR backup switch.

### Archive-backed accepted recovery results

The manual cache workflow can now select results from an exact completed recovery
run for an archive-backed fresh intake. It authenticates the original archive,
unchanged intake authority, all original roots and claims, exact manifest and
completed main-branch recovery producer before reading accepted child results.
Only children accepted by that run are selected; an earlier failed child is
proof for a later ordinal, not a source of mixed output. All live terminal
membership and authorized failure proofs must match before any ZIP retrieval.

This cache route performs no POST or canonical ledger write. It preserves the
empty original Daily producer ID and records the archive and recovery producers
separately. The fixed manual transport cutoff is unchanged. Workflow dispatch
inputs are not claimed as proven by the GitHub run metadata; canonical source,
manifest and controller records provide the binding.

Immutable task snapshot checks use at most eight concurrent independent R2 GETs.
Every original snapshot still receives one complete comparison, all worker
results are consumed and workers joined before any ZIP request or cache write.
A changed or unreadable record rejects the operation with the same fixed
category. Submission, result downloads, cache writes and cutoff checks remain
serial and unchanged.

### Second fixed manual recovery window

The original fixed window ended at 2026-10-04T23:59:59Z while the October 2
failed-member recovery was still running. The reviewed follow-up allows
one additional fixed day, ending 2026-10-05T23:59:59Z. The user instructed the
repair to continue after the pending window and connection retry were explained.
It preserves the exact same leaf, host, historical system/certifi chain checks,
current intermediate checks, complete-source/task proofs and GET-only cache
route. At that release Daily still used strict PKI alone; the later automatic
recovery above resolves that remaining delivery gap. Old authenticated R2 cache bytes remain reusable;
this window only governs new manual result retrieval and cache writes. The
transport cannot extend the new cutoff itself.

The second window preserves complete legacy caches with a separate
stored-authentication validator. It accepts only the original fixed October 4
cutoff or the explicitly deployed current cutoff, retaining every other strict
field, fingerprint and chain condition. Only reads of already bound immutable
ZIP/authentication/proof receipts use this validator. New connections, new cache
authentication and legacy writes still require the current cutoff exactly.
A partial previous authentication object without a complete cache cannot be
overwritten: it remains an explicit immutable-write conflict. Cross-window
fixtures verify complete old bytes are reused without new result retrieval or
cache writes.

Rejected OCR page diagnostics now report bounded long-ASCII-run lengths and
source-page regions for each failed text candidate. Regions are mapped only
when the complete non-whitespace character stream and word boundaries agree;
ambiguous, changed-order or invalid geometry remains explicitly unlocated.
The output contains fixed categories, coordinates and counts, never OCR words
or source names. It reuses the existing recognition result and does not change
readability, numeric checks or production source admission.

The field probe's `retain_private_evidence` option defaults to false and permits
only one explicitly selected `original-archive` page. It preserves the existing
recognition candidates and 300-dpi pixels, bound to the source run/date/PDF
hash/page, manifest hash, probe commit and model provenance. It performs no
additional OCR. The two files use a private directory and the separate private
R2 `ocr-probe-evidence` namespace; public artifacts still contain only the
sanitized summary. They contain no complete-source receipt or manifest and
cannot enter the PDF source-consumption contract. Failed page checks retain
their original nonzero exit; retention failure is reported as unavailable and
never promotes the page to accepted source material.
The same opt-in private payload can retain regional plans and each completed
rotated read, including attempts followed by rejection or timeout. It reuses
the existing reader calls and keeps the preceding whole-page candidates and
model provenance. The trace defaults to `None`, is excluded from production
source receipts and public summaries, and remains subject to the existing
single-page, two-file and private-payload size limits.

### Complete cloud PDF acceptance without live publication

The PDF consumer's explicit `acceptance_only=true` mode rebuilds the complete
selected source even when a valid dated live PDF already exists. Source
producer/receipt checks, numeric fixtures, model synthesis, rendering, public
sanitization and identity validation all run normally. It skips the live R2
PDF/catalogue archive and main-branch commit, retaining only the successfully
validated public-safe PDF as a one-day Actions artifact. Source originals,
Markdown, logs and audit/usage JSON are not artifacts in this mode. Its default
false preserves the publishing route. An acceptance artifact is evidence of
PDF construction, not a new live publication.

### Bounded recovery of vertically printed chart dates

The retained cloud OCR backup now has a locally implemented rotated-date route
for pages whose geometric, source-flow and full-page PSM 11 transcripts all fail
only the unchanged long-ASCII readability rule. It identifies at most four
interior axis bands from complete retained word positions and original 300-dpi
RGB pixels. Each band receives fixed 90- and 270-degree reads, at most eight
reads total, with a shared 180-second budget and a 30-second per-read limit.
Only one unambiguous direction containing complete date words is eligible;
prose, clipped words, partial dates and ambiguous directions reject the page.

Original-PDF visual QA of October 1 source ordinal 23 page 3 confirms four
bottom-to-top axes with full `YYYY/MM` labels. A fresh 300-dpi render of the
verified original is 2550 by 3234 pixels. The older 980 by 1242 PNG is a reduced
preview and must not be described as a full-resolution OCR proof. Replaying
the retained opaque-run positions against the fresh render found that the
proposed bands also included the chart baseline and horizontal scale zero.
That extra content can correctly cause the date-only reader to reject a band.

The local follow-up separates an axis band from a chart baseline only when
the original pixels contain a bounded, sufficiently wide white gap. Complete
word containment, body collisions, region boundaries and pixel margins still
apply, and the consumer recomputes the selection from the original RGB image.
Horizontal zero and all other text outside the replacement spans remain in
the original transcript and their existing numeric checks. Identical opaque
strings on separate axes are allowed only through their exact original word
indices and global spans; exchanging those positions still rejects the proof.

The fragment-support extension first preserves the earlier strict planner.
Only a word-membership rejection may attempt independently separated bands
seeded by the existing opaque runs. It assigns a cross-chart source word once,
using all original non-white pixels across the complete set of bands; any
baseline exception must identify the actual long gray separator stroke and
its proved white gap. A successful rotated direction must contain complete
date words in separate non-overlapping rows. Original boxes remain unchanged.
Earlier successful exact-box, one-pixel component and version-2 ledger proofs
keep their existing shape. The version-3 fallback still requires every dark
core pixel to remain in one original date box and rejects other-word contact
or overhang beyond two pixels. A supporting path takes at most two steps,
never gets lighter, and must become strictly darker at least once. Every step
outside the box moves closer; after entering the box, a final darker step
inside the same box may prove a quantized equal-gray edge.

Completely isolated near-white micro-components are never called dates. Each
has at most two pixels, all gray 240–244, and an independent untranscribed
ledger of original coordinates, values and hashes. Version 3 records nearest
word distances only as diagnostics, allowing ties without assigning semantic
ownership. Combined residual size is at most 0.1% of the band's ink and 32
pixels, whichever is smaller. The unchanged source crop is bound to the full
original page, and every residual component is mapped back to verify its full
eight-neighbor halo, including across crop boundaries. A cropped fragment of
a larger source stroke therefore cannot be accepted as a micro-component.
Every pixel below the unchanged 245 threshold belongs either to a proved
glyph component or the bounded untranscribed ledger. The ledger cannot supply
numeric confirmation or invented text. Original candidates, word indices,
support hashes and replacement spans remain; the consumer recomputes the full
pixel/support/coverage proof. A short token, thin box or missing
alternate read alone never authorizes deletion. The actual affected-page cloud
acceptance remains pending; a geometric replay is not recognition acceptance.

The retained diagnostic omits the full word list. Its geometry-only replay uses
explicit synthetic placeholders for the known positions and performs no OCR,
source admission or numeric acceptance. Real affected-page recognition remains
an independent cloud acceptance requirement.

Private provenance preserves all three rejected transcripts, every original
word, original pixels, crop and rotated hashes, affine mappings and the exact
replacement ledger. The consumer reconstructs the selection from these inputs
and validates every numeric binding. Unchanged horizontal values retain their
independent full-page, two crop and punctuation checks. Newly rotated values
remain unconfirmed and are masked; this route does not authorize their use as
verified numbers. Both real-field and ordinal probes forward the same private
proof without including transcripts or proof contents in public diagnostics.

The axis module includes a Linux-only actual
Tesseract regression with the production `eng+chi_sim` models, real model
hashes, vertical `YYYY/MM` labels and adjacent scale zero. It does not mock
the region reader or independent numeric reads. The regression workflow's
required-OCR flag makes missing CLI/models a failure; macOS skips this case
without executing local OCR. Cloud regression `37283762826` passed the actual
engine cases before PR 251 merged. Actual affected-page and remaining complete
backup acceptance are separate checks. The daily switch was still disabled at
that stage; its later enablement is recorded in the current acceptance below.
MinerU remains the primary parser and GitHub Actions remains the production
execution environment. Local geometry and rendering QA provide development
evidence and are never scheduled production dependencies.

### Primary PDF visual acceptance and retained figure defects

The recovered October 1, 3 and 4 public-safe files have verified hashes and
46, 47 and 18 pages respectively. October 1's complete 46-page contact sheets
have now been inspected: all 44 images have same-page captions, with no
out-of-page text or image/text overlap. Its source coverage is 63 original
aliases, 62 unique contents and one preserved duplicate binding.

This proves complete source binding and PDF pagination, not perfect MinerU
figure selection. Four October 1 embedded images on PDF pages 24, 38 and 42
are disclaimer blocks rather than analytical charts. The Cash Flow table on
PDF page 28 has title glyphs already cut at the embedded JPEG's top edge;
the PDF renderer preserves that JPEG and its data table. Separate original-page
comparisons also identified cut title/legend material in the October 3 page-36
and October 4 page-11 source crops. Raw result ZIPs remain in private R2;
the consumed handoff excludes raw MinerU JSON, so source `page_idx`/`bbox`
metadata had to be recovered from those cached ZIPs before implementing a
source-bound figure repair. The existing published files still contain these
defects; the locally implemented repair below is not deployed acceptance.

Original-page visual comparisons bind October 1 PDF page 28 image 2 to source
ordinal 27 page 2; page 24 image 1 to ordinal 8 page 3; page 38 image 1 to
ordinal 11 page 10; and page 42 images 1 and 2 to ordinal 10 pages 16 and 13.
These visual bindings under the verified complete manifest have now been
matched to the actual cached provider image hashes and `img_path`/`page_idx`
metadata. Both original-page and provider metadata provenance must accompany
any repaired crop.

The initial independent R2 check on October 5 at approximately 03:42 UTC
timed out before identifying an account or retrieving an object. A subsequent
normal Wrangler OAuth identity check at 04:13 UTC succeeded without changing
local network or Git transport settings. Read-only R2 access to the existing
configured private R2 bucket then retrieved five October 1 legacy result ZIPs and
the October 3/4 target ZIPs. Their receipts, admitted cache identities, byte
counts and ZIP hashes match the previously verified seed records. These are
private source QA reads, with no new parsing POST, R2 write or source admission.

The actual `content_list` and `middle_v2` metadata establish exact
`img_path`, zero-based `page_idx` and image-body boxes. Content-list coordinates
are normalized to 0–1000 and checked against middle-file point boxes using the
provider's recorded page size. Original-page crops instead use the exact
300/72 render matrix and actual original geometry, without stretching point
coordinates through rounded provider dimensions. Parent boxes do not include
captions or footnotes. Some footnotes are assigned to another column's parent,
so parent membership alone cannot authorize enlarging a crop. Generic
`image` entries include valid analytical charts and must not be excluded by type.

Comparisons of the affected original pages with the rewritten PDF inside each
ZIP found identical page frames and 300-dpi RGB pixels. Their PDF byte hashes
are different: the ZIP's PDF is not an authenticated substitute for the original.
In particular, October 1 original 27 page 2 has a fractional crop-box height
while the provider records integer page dimensions; both coordinate frames
must be retained explicitly. The local selection/crop repair uses these actual
source bindings, not a schema inferred from cache summaries.

An independent Cloudflare Worker strict-HTTPS HEAD check at approximately
04:36 UTC still returned `526` with category `tls_invalid_certificate` for
`cdn-mineru.openxlab.org.cn`. It performed one provider HEAD and no ZIP download,
parsing POST or R2 write. The temporary Worker was deleted and its absence
confirmed by a separate 404 readback. `SJC` describes request ingress; the
Worker's execution location was not observed. This current certificate-validity
failure is separate from successful R2 cache reads and from GitHub authorization.
It does not re-identify the certificate leaf or prove a new expiry timestamp.

### Source-bound figure repair and cloud deployment

`scripts/mineru_figure_sources.py` validates the actual content-list/middle-file
pair and each unique provider image reference. Metadata absent from both
families preserves the older cache route; incomplete, ambiguous or malformed
present metadata rejects instead of reverting to image guessing. Legal-body
cues and an immediate same-column disclosure heading exclude the confirmed
disclaimer images. Valid generic `image` entries remain eligible, and a report
with no reliable analytical images may have zero figures.

Daily and complete-source recovery producers pass the frozen original PDF
path and admitted SHA. They compare each used page with the rewritten provider
PDF, retaining actual geometry and 300-dpi RGB identity. Body, captions and
footnotes receive a single unambiguous spatial owner across the page; a wrong
parent, wide cross-column note or equally near alternative does not authorize
including another column. Old filename-only legacy consumption explicitly
retains an unproven original identity and provider JPEGs, without original-page
recropping.

The private `source_figure_map.json` binds typed metadata, every inclusion or
exclusion, provider JPEG hashes, original-page PNG carriers and exact derived
crop pixels. The existing closed v1 image map remains compatible. Status binds
the sidecar name and SHA; the source and PDF consumers replay the proof and
require each canonical reference to map to its exact asset. Deleted, empty,
mutated or dangling declarations cannot downgrade to an older route. Original
identity comes from the trusted producer and outer immutable receipt, not
from a self-declared inner hash.

The PDF consumer ranks retained figures by the unchanged provider image's
existing visual score and byte size, including its original filename hint,
then displays the repaired crop. This retains prior visual priority while
avoiding a blind first-page selection. Lower-ranked valid figures remain
eligible. Under the default four-figure limit, the actual Cash Flow, Factor
Profile and Figure 9 targets remain selected at ranks 1, 2 and 4 respectively.

Seven actual cached results passed original/ZIP hash checks, source generation,
consumer replay and figure extraction. The three repaired unions match the
independent original-page QA: `[310,290,563,493]`, `[358,497,554,649]` and
`[46,188,293,343]`. The production ReportLab renderer also produced a private
nine-page layout QA file with all three source images: embedded RGB hashes
and pixel dimensions match the derived PNGs, and all three captions follow
their complete image on the same page. This is a layout/pixel check, not a
complete dated Market Views rebuild, cloud OCR run or live publication.

Finalization and sensitive-text guards preserve the sidecar and all files in
`figure_source_evidence`. Private handoff retains these carriers; public
publish-ready packages exclude them while retaining selected figure assets
and generated public articles. Source proof must never be edited as copy or
packaged as an extra original-page attachment.

The integration regression includes source contracts, old-cache compatibility,
numeric/axis proof, private transfer, packaging and actual ReportLab rendering.
The offline run has 410 passing tests and 14 skipped actual-cloud-OCR tests;
no local OCR was executed. The new module and consumer checks are included in
the Actions regression workflow. Isolated subprocess checks also preserve
stdlib-only authorization/source checks and keep TLS/cache entry points usable
before image dependencies are installed; image decoding and PDF rendering
load their dependencies only when invoked. Cloud CI `37283762826` subsequently
passed the actual OCR cases. PR 251 merged at `95110608` after the real-engine
test fixture was corrected to include its intended chart baseline. No production
OCR admission rule was relaxed. The subsequent PR 252 follow-up permits only
MinerU's exact table-equation serialization difference: middle-file
`<eq>...</eq>` must match content-list ` $...$ ` with every formula character,
table cell and other HTML byte preserved. Both original provider hashes remain
bound. The narrow image-path compatibility additionally permits only a bare
64-lowercase-hex `.jpg` in the exact `<img src="..."/>` form to gain `images/`
in the content list. Image basenames, formula characters, cell structure and
all remaining bytes must match. Exact equality and the earlier equation-only
form remain accepted; arbitrary HTML cleanup or path rewriting is forbidden.
Regression fixtures retain both raw JSON hashes and complete consumer pixel
replay, and reject changed numbers, formulas, image identities and paths.

Both complete-source recovery CLIs bind a figure failure to the actual report
enumeration and publish only its fixed category plus an optional
`source_ordinal`. The ordinal must be a plain integer between one and the exact
expected report count, with a maximum of 1,000. Filenames, titles, source text,
URLs, booleans, malformed values and out-of-range ordinals are not diagnostic
output. This adds report-level location without accepting a partial handoff.

Original-page carriers are written and replayed one page at a time,
with at most 80 million pixels per page and one billion pixels across unique
selected pages. Duplicate image references still reject; aggregate overages
report `figure_page_budget_exceeded`. Existing proof schemas and complete crop
replay remain unchanged. Ten distinct cached reports passed private source QA;
that local check does not establish cloud publication. PR 252 merged at
`eb80a3e5` on October 5 at 10:35:54 UTC after cloud CI `37297176568` passed.
Current independent backup acceptance and enablement are recorded below.

### October 5 current delivery and cloud backup acceptance

The primary architecture remains Dropbox → GitHub Actions → MinerU API →
private R2 → Market Views PDF → member portal. Cloud OCR is a retained automatic
backup; production execution does not depend on local QA or a local computer.
The provider's final strict result-CDN probe `37347310154` still reported an
expired certificate at 17:18 UTC, independently of successful task API
authentication and GitHub access. The primary path now retains strict PKI first
and adds the automatic known-certificate identity recovery described above.

Complete primary recovery `37284033767` and PDF consumer `37284226601`
succeeded for all 50 October 2 originals. Fresh live inspection `37343103500`
verified the latest October 1–4 full private PDF hashes and index records
against the public dated list, and anonymous download requests returned HTTP
401. Actual authenticated member-browser downloads matched the private R2
receipts for both October 2 and the rebuilt October 3 PDF:

| Member original | Pages | Bytes | SHA-256 |
| --- | --- | --- | --- |
| October 2 | 54 | 3,619,892 | `dc902a24cae3672e7f5292a600048436b5805b3a111403aea48269262394acd3` |
| October 3 | 46 | 30,252,678 | `7a1b9af4609923b1bddd3a1560aac13381b3c95a50c568a4ef878b8011649f0c` |

The October 3 download is bound to PDF run `37341517817` and the fresh live
inspection. October 1 and 4 have not had this authenticated browser-download
acceptance. The separate October 2 public-safe PDF has 53 pages after
sanitization; its page count or hash must not be compared with the member
original.

After PR 252, October 4 primary source rebuild `37297655439` and PDF
`37297840175`, and October 1 legacy source rebuild `37297927956` and child PDF
`37298965236`, succeeded. October 3 rebuild `37340380301` passed all 54 source
checks at 16:30:59 UTC and the private R2 handoff at 16:31:38. PDF child
`37341517817` succeeded at 16:42:21 on `ce16fb2a`, and the parent completed
successfully at 16:42:30. The public-safe PDF was committed at `615d5602`.
The fresh live inspection and October 3 authenticated download above verified
this latest publication against its full private PDF receipt.

PR 254 merged at `ce16fb2a` at 16:22 UTC after CI `37339774011` passed actual
OCR and renderer checks in 3 minutes 45 seconds. Final ReportLab and LaTeX
display now replaces only complete internal numeric-pending field markers with
the explicit Chinese pending-value message. Original IDs remain in inputs,
receipts and structured data; the value remains unresolved. Confirmed values
and original figure pixels are unchanged.

| Complete cloud backup | Source evidence | Successful acceptance-only PDF |
| --- | --- | --- |
| October 2 | 50 originals, 663 pages (341 OCR); producer `37245268724`, re-audit `37297634646` | `37335782776` |
| October 3 | 54 originals, 1,029 pages; producer `37245279463` | `37284342786` |
| October 4 | Four originals, 109 pages (82 native, 27 OCR); producer `37244394621` | `37297644728` |

All three complete PDF consumers passed their source, numeric, synthesis,
rendering and sanitization gates with `acceptance_only=true`, without replacing
live publications. October 2's old source run completed extraction/validation
and the 777-file private handoff before its audit failed. Successful re-audit
measured the unchanged receipt at 325,008,524 bytes, confirming it exceeded the
old independent 256,000,000-byte audit limit. All 50 reports and 663 pages
passed with zero OCR, MinerU or model calls.

The deployed re-audit hashes a stable regular receipt in bounded chunks before
and after the unchanged full validator. Its main-only workflow admits an old
handoff only when original extraction/archive succeeded and audit failed.
The original producer and receipt remain unchanged; a small immutable receipt
binds the new successful audit run/attempt/SHA to the old source run/SHA/date,
count and receipt hash/bytes. The explicit PDF consumer verifies that binding
and repeats complete validation and numeric audit. Ordinary readiness gates
remain unchanged. Acceptance-only PDF concurrency is isolated by run ID;
normal publications keep their shared serial queue.

Based on these three complete real-source and PDF acceptances, the repository
variable `MARKET_VIEWS_OCR_BACKUP_ENABLED` was set to `true` and read back at
16:06 UTC on October 5. This enables the verified backup capability before
October 1's exceptional page is resolved. Daily fallback uses only that run's
exact selected originals, requires the complete source and numeric receipts,
and stops on invalid evidence; failed report notes remain failed. Enablement
is confirmed, while the next actual Daily fallback-to-publication execution
still requires its own end-to-end acceptance.

October 1 cloud backup remains incomplete. PR 253 merged at `b9a79ae0`; actual
probe `37336781381` passed the earlier 0.1373-pixel horizontal word-box
intersection but still rejected a second thin word crossing chart regions.
At that stage the affected page and complete 63-alias/62-unique batch needed
further cloud acceptance. The switch does not bypass rejection or claim all dates are
covered. Complete-source, readability and independent numeric gates remain
unchanged; geometric local replay alone is not OCR acceptance.
Private probe `37340394718` kept its original failed exit and retained two
private files whose hashes, source binding and model provenance were verified.
They show multiple short horizontal OCR word boxes crossing date-axis regions.
PR 255 merged at `8e984e74` after actual Ubuntu OCR CI `37345360545`
passed. Real-page probe `37346104127` then passed the four-band planner and
unique complete-date direction but rejected source-pixel coverage in the first
band. Verified private evidence contains 31,487 non-white pixels: 444 outside
word boxes have direct one-pixel support, 21 have a strictly darker two-step
path into a unique original box, and eight near-white pixels are isolated.
Those isolated pixels cannot be called recognized dates; the follow-up
retains an explicit untranscribed ledger. Pixel replay accounts for all
31,487 pixels as 31,479 glyph pixels plus eight untranscribed pixels; it
performs no OCR and does not replace fresh cloud acceptance. The integrated
suite has 213 tests: 198 passed locally, with 15 real-engine cases reserved
for Ubuntu CI. The opt-in private probe now collects all already-planned
regions within the existing eight-read/180-second budget after a first
rejection, preserves that rejection and never emits a partial success proof.
Default production still stops at its first rejected region. Affected-page
and full-batch acceptance remain open. Private diagnostics are not complete source handoffs.


PR 257 merged at `dcf10862` after real OCR CI `37348001486` passed.
Private probe `37348761613` retained all eight reads for four regions; each
region had one unambiguous 34-word complete-date direction. The first region
passed, while later regions exposed a same-gray quantization edge and
independent near-white residuals beyond version 2's arbitrary nearest-word
and per-region limits. Full-page component analysis verified that none was a
clipped larger stroke. The version-3 repair accounts for 127,723 ink pixels as
127,670 glyph pixels plus 53 explicitly untranscribed pixels across four bands.
A complete producer, composed-text and consumer replay using the eight cached
cloud reads passed without running local OCR. It preserved 85 unique source
word edits and 38 horizontal numeric positions; all 272 rotated numeric
mentions remain unresolved rather than gaining confirmation from this repair.
Fresh cloud whole-page and golden numeric probe `37351321483` subsequently
passed on main `a0c69fe6`. This resolves the affected-page probe; it does not
establish a complete October 1 backup PDF. Further OCR refinement is secondary
to the primary MinerU delivery path; the retained backup target is readable
output with unresolved values clearly marked and original source binding kept.

PR 256 merged at `1da60820` at 17:19 UTC. All four required CI checks passed
on `693b31f5`, including actual workflow-resolver regressions. Same-date reruns
skip only when the repository PDF exists and the private member PDF/catalogue
pair passes complete hash, byte length, date and metadata validation. Explicit
absence or content inconsistency rebuilds from the verified full source; no
public-safe PDF is uploaded as a member original. R2 authorization, TLS,
timeout, unreadable lengths and short reads still fail without triggering
synthesis. Force and acceptance-only semantics and private-before-public
publication order are preserved.


#### Bounded source edition acceptance and honest Daily status

A failed matrix is eligible for successful degraded delivery only when each failed
batch recorded a known MinerU failure and the only failed job step was generation.
Checkout, source binding, private checkpoint/cache integrity, model quality,
installation and handoff failures remain failures even if an independent backup
PDF was delivered. A zero selected-source inventory is an explicit no-op and does
not claim a new PDF. Both native/OCR delivery and source-page delivery send a
24-hour deduplicated exception notice after successful publication; reusing an
existing standard publication does not send a backup-published notice. A private
and public edition mismatch fails instead of silently reclassifying the issue.
New PDFs must open and render all pages before upload; the final private readback
checks the exact SHA-256 recorded before public identity removal.

For a no-provider production-cloud rehearsal, dispatch the manual-only
`market-views-source-preview-acceptance.yml` on `main` with
`source_run_id=37232504334` and `date_folder=261004`. It verifies the historical
Daily selection/upload gates, reads the retained original selection, runs failure
classification injections, generates a real labelled PDF and public-safe copy,
and uploads/reads back only an isolated run/attempt-specific private object. It
verifies the existing production issue before and after, then deletes that exact
temporary object. It has no MinerU/DeepSeek secrets and does not overwrite, commit
or email a production issue. A successful rehearsal is distinct from the next
scheduled Daily run and its downstream publication.

The recovery job reserves its final fallback budget: optional OCR installation is
limited to 5 minutes, strict extraction/validation to 20 minutes and receipt audit
to 10 minutes, within the 120-minute job. Original-page preparation has its own
15-minute limit; strict-attempt timeout is eligible for the subsequent page path.


#### Replay the real Daily graph without new MinerU submissions

`dropbox-latest-pdf-to-xhs-sharded.yml` also supports the optional manual-only
`replay_source_run_id` input. Leave it empty for the normal daily schedule. A
replay verifies the completed main producer and successful source-artifact upload,
downloads that frozen selection, checks every PDF SHA against its unchanged
manifest and requires every original Dropbox path to belong to the requested
root/date. The current run uploads its own verified source artifact and a small
receipt linking original/current run and code identities.

Replay requires `force_reprocess=false`, `wechat_draft_upload=false`,
`translated_report_count=0`, `max_total_reports=0` and an explicit
`dropbox_date_folder`. It skips source download/classification and sets
`MINERU_FORBID_NEW_SUBMISSIONS=1` for the real generation wrapper. The ledger
rejects missing, changed or never-accepted bindings before any task claim or POST;
definitively rejected authentication claims also cannot rotate credentials and
submit. These conditions fail the replay and do not authorize a backup. Trusted
accepted tasks are queried normally; their actual provider failure may enter the
usual source-outcome, bounded recovery, downstream Market Views and final
publication gate. Completed tasks and original result caches are preserved.

For the retained four-report October 4 batch, dispatch the real Daily workflow on
`main` with `replay_source_run_id=37232504334`, `dropbox_date_folder=261004`, the four
required safe options above, and the original extraction settings
`mineru_model=vlm`, `language=en`, `ocr=true`, `reports_per_shard=5`, `batch_size=5`,
`shard_count=40`, `report_selection_mode=all`. Keep `wechat_freepublish=false` and
`commit_results=false`. Historical evidence shows one accepted original batch
with three completed reports and one failed report. Re-observing this state
requires no new MinerU POST and skips article synthesis; the downstream child
can verify and reuse the existing complete October 4 publication. If the provider
now reports every original completed, normal report synthesis may run on a new
code-bound generation checkpoint. Zero new MinerU submissions does not imply
zero model calls in that different branch. The final Daily and child run results,
not an isolated renderer test, determine end-to-end acceptance.
