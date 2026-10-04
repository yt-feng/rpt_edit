# MinerU in-flight recovery

## Explicit terminal-failure recovery

[`market-views-mineru-recovery.yml`](../.github/workflows/market-views-mineru-recovery.yml)
runs only as a reviewed `main` dispatch. It freezes the complete original PDF
manifest and bytes, rebuilds the original batch membership from source claims,
and retrieves every successful original ZIP before admitting a retry.
`TerminalRecovery` preserves the original source pointers and task records while
an independent private controller reserves at most two child tasks containing
only verified failed members. The allowed error codes or exact message hashes
and manifest hash stay fixed across reruns. Pending or ambiguous children never
authorize another child.

Conditional-store conflicts cannot grant ownership by reading back identical
content. Each submission intent has its own nonce, so two runners cannot mistake
the same saved state for their own successful claim. Explicit authentication
rejections may move the same child to another key; accepted tasks retain their
accepted key. Every successful descendant is bound back to its original PDF,
task and data ID, and all original members must be resolved before generation.

The source-only receipt binds the original producer, recovery producer and both
execution commits, exact source inventory, ZIP hashes, markdown, images and task
lineage. The PDF consumer verifies the recovery producer workflow and commit
before accepting that receipt. Completed source recovery, PDF archive, public
commit and the dated live catalogue/download still require separate acceptance.

MinerU API parsing remains the production architecture. GitHub Actions runs the
client, stores its durable ledger in private R2, retrieves provider results and
continues to the existing generation and publishing gates. This recovery does
not require the user's computer. See the full chain in
[Automation Pipeline Overview](pipeline-overview-v2.md).

A queue timeout is an unfinished accepted task. It must not trigger another
upload, token rotation, or a successful publication result.

The PDF wrapper preserves a stable original relative source name when it copies
PDFs into temporary indexed batches. Each source claim binds this name, exact
SHA-256 and byte length, pipeline scope, provider endpoint, and extraction options.
A private batch manifest binds the admitted 1–5 sources to the original token's
nonsecret fingerprint. The canonical task ledger stores neither credentials nor
signed upload/result URLs. Separate private diagnostic receipts can preserve the
original provider response, including result URLs; they never enter public logs
or review packages.

Production callers set `MINERU_LEDGER_BACKEND=r2` and a stable pipeline scope.
Their existing workflow concurrency and shard admission remain unchanged. The
private S3 API stores manifests and immutable per-source claims beneath
`_workflow-cache/mineru-inflight/v1/`. Keep this prefix out of cleanup and lifecycle
expiry: deleting a claim removes the evidence needed to prevent resubmission.
Local CLI runs use an output-directory ledger; keep that directory when resuming.

Before POST, a new batch writes its manifest, conditionally claims every source,
and records submission intent. The provider batch ID is saved and read back
before any upload or polling. A later run follows each requested PDF's claim and
polls its original batch with its original credential, even after days or changed
batch grouping. It may submit one batch containing only genuinely unclaimed
inputs. No pending, failed, interrupted, or ambiguous task expires into permission
to POST again. An unavailable original credential blocks accepted-task recovery.

## Explicit authentication rejection

Before each POST, the client durably records submission intent and the credential
identity. It may try the next configured key only when the provider explicitly
rejects authentication with HTTP 401, `A0202` (invalid token), or `A0211` (expired
token), and the response contains no `batch_id` or `file_urls` acceptance
acknowledgement. A 429, 5xx, transport failure, timeout, malformed response
without definitive authentication rejection, or conflicting acknowledgement
remains a stopped or ambiguous submission. The
client saves each definitive rejection as `auth_rejected` before moving on.

If every key is definitively rejected, the original claims and exact batch stay
in place. A later attempt may resume that unaccepted batch only with its complete
original source bindings and a new credential that was not already rejected.
Changing names, bytes, batch membership or options does not release those claims.
An old rejected key may be removed from configuration, but an accepted batch
still requires its original key. Accepted, uploaded and terminal batches cannot
switch keys and submit again; an authentication error during polling does not
enter submission fallback.

This key fallback addresses explicit authentication rejection. It does not repair
provider parsing failures or result-download TLS failures. The key-expiry monitor
described in [the pipeline overview](pipeline-overview-v2.md) is a separate,
GET-only health check.

## Complete batches and result retrieval

R2 conditional writes use `IfNoneMatch='*'` for new objects and `IfMatch=ETag` for
updates. Every write requires exact canonical JSON byte readback, preserving
JSON types (a boolean cannot replace an integer). Schema versions require integer
type. If an acknowledgement is
lost, the code reads back once and continues only when the exact intended object
is present; it never retries that write or provider submission. Corrupt, truncated,
wrong-scope, conflicting, and unknown-state checkpoints stop before new work.
The SDK model is checked before private-store access. Workflow installs require
`boto3>=1.37.32,<2`.

Provider polling retains the existing time/no-progress budgets. Missing or
nonterminal selected results produce exit 75; terminal provider errors produce
exit 2. Neither permits paid generation or publication. The wrapper cannot turn
partial successes into exit 0. A usable provider batch requires completed rows and source result URLs for
every originally admitted ID. Resuming a completed subset cannot hide pending,
missing, or failed neighbours. Summaries distinguish selected counts from each
original batch inventory and expose `ready_for_generation`; incomplete batches
retain diagnostic counts but release no result rows to generation. Terminal
failures anywhere in an original batch block every selected subset. Downstream source, chart, semantic and publication checks still apply.

A `done` row and result URL prove provider completion, not that the ZIP can be
retrieved or that the final PDF exists. Result download and source parsing must
succeed before paid report generation. Complete report shards then pass through
the private R2 handoff to Market Views. PDF rendering, original-figure checks,
private archive, public-safe commit, and live catalogue/download acceptance are
later independent steps; none is implied by a successful poll.

Interrupted claiming, an unknown POST outcome, accepted-but-incomplete uploads,
or an expired provider result require investigation of the saved batch. Do not
delete claims or change credentials to make them retry. Historical logs alone
are insufficient for adopting older batches: independently verify the frozen PDF
bytes, original provider data IDs, scope, options and credential first. This
change deliberately does not fabricate those bindings or parsed results.

## Private diagnostics

The cloud entry **Diagnose MinerU API and saved results**
[`mineru-api-diagnostics.yml`](../.github/workflows/mineru-api-diagnostics.yml)
provides read-only diagnostics on GitHub Actions. Its inputs select the original
`inspection_run_id`, `inspection_attempt`, `input_sha256` and `receipt_sha256`.
It reads the fixed private inspection prefix without rewriting its receipt or
canonical task ledger. The optional `stream_probe` reads only four result bytes;
the safe summary explicitly reports `full_zip_verified=false`.

The summary separates `historical_tasks` (cached states and normalized failure
reason/code counts), `authentication` (four configured slots and their observed
authentication/expiry result), and `result_download` (host, TLS/HEAD and optional
ZIP-prefix evidence). Credentials, credential fingerprints, signed URLs and
analyst contact details stay out of the public summary. The job submits no new
task and sends no email.

Current API health is an observation from those probes, not an inference from historical failures or the
number of configured keys. Read its safe summary together with the private
provider response before assigning a cause. No parsing POST or replacement task
is authorized by a diagnostic result.

[`mineru-durable-inspect.yml`](../.github/workflows/mineru-durable-inspect.yml)
accepts exact saved ledger batch keys, verifies their source/task bindings and
GETs each original task with its original credential. It does not alter canonical
claims. The separate receipt store is
`_workflow-cache/mineru-legacy-inspections/v1/<inspection-run>-<attempt>/<request-sha256>/`.
Its `receipt-<sha256>.json` lists private objects containing exact response bytes
in `raw_response_base64` and, when JSON is valid, `provider_response`.
`err_msg`, `error`, `err_code` and other original provider fields must be read from
that private payload; public categories and hashes alone are insufficient.

For the historical 2026-10-03 inspection run `37160198464`, the public receipt
records 11 private response objects, 36 completed PDFs and 18 failed PDFs. The
request hash is
`ece9b3164c1bc7ca2a99e07ca6ef1a3b93396f196f27d7b08141424322d34bd8`
and private receipt hash is
`0bc3bc20b57d520056109123c6ba50a76ca8a6486bd20b4c4bd75c3340fbc369`.
The saved public diagnosis is only `other_provider_failure`; the 18 failures'
specific cause has not been established. The canonical ledger records task state,
not the full result rows, so the independent private receipt is the relevant
evidence source.

The later 2026-10-04 read-only diagnostic run
`37211677994`
verified authentication for all four configured key slots and classified the
retained failure messages as `provider_internal`, without a supplied error code.
That classification does not establish the provider's underlying cause.
Cloud smoke run
`37212761333`
then accepted and completed one new PDF. Its full ZIP download failed certificate
validation at the provider result CDN. No ZIP bytes were retrieved. Current
authentication and parsing are therefore verified for the smoke task, while
result delivery remains blocked. Never turn this download failure into another
submission or disable TLS validation; an accepted smoke rerun reuses its task.

[`mineru-result-tls-probe.yml`](../.github/workflows/mineru-result-tls-probe.yml)
compares the system CA store with Requests using the current certifi bundle on
GitHub Actions. Each independent client makes one strict HTTPS HEAD request to
the fixed public result-CDN root, without credentials, redirects, retries or body
reads. An HTTP error status still proves that TLS completed; it does not verify a
result ZIP. The sanitized report distinguishes a trust-store difference from two
clients failing validation. This diagnostic changes no task, URL or network setting.

Protocol references checked for this implementation:

- [Cloudflare R2 S3 compatibility](https://developers.cloudflare.com/r2/api/s3/api/)
  documents both conditional headers for PutObject.
- [Cloudflare R2 consistency](https://developers.cloudflare.com/r2/reference/consistency/)
  documents strong read-after-write consistency through its private S3 API.
- [Boto3 1.37.32 PutObject](https://boto3.amazonaws.com/v1/documentation/api/1.37.32/reference/services/s3/bucket/put_object.html)
  documents `IfMatch` and `IfNoneMatch` parameters and conditional failures.

Run `python scripts/test_mineru_task_ledger.py` for offline recovery and
failure-injection regressions. CI also verifies the installed SDK operation model.

The manually dispatched `MinerU private checkpoint canary` performs only private
R2 operations on two tiny synthetic objects under a run/attempt-specific
`_workflow-smoke/mineru-cas/v1/` prefix. It requires HTTP 412 for duplicate create
and stale update, verifies a valid CAS and exact readback, and retains a private
cleanup manifest for inspection. It never deletes objects, calls MinerU, or sends
WeChat messages. Public diagnostics expose only booleans, counts and hashes.
