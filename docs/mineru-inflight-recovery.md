# MinerU in-flight recovery

A queue timeout is an unfinished accepted task. It must not trigger another
upload, token rotation, or a successful publication result.

The PDF wrapper preserves a stable original relative source name when it copies
PDFs into temporary indexed batches. Each source claim binds this name, exact
SHA-256 and byte length, pipeline scope, provider endpoint, and extraction options.
A private batch manifest binds the admitted 1–5 sources to the original token's
nonsecret fingerprint. Credentials and signed upload/result URLs are never saved.

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
to POST again. An unavailable original credential blocks recovery.

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

Interrupted claiming, an unknown POST outcome, accepted-but-incomplete uploads,
or an expired provider result require investigation of the saved batch. Do not
delete claims or change credentials to make them retry. Historical logs alone
are insufficient for adopting older batches: independently verify the frozen PDF
bytes, original provider data IDs, scope, options and credential first. This
change deliberately does not fabricate those bindings or parsed results.

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
