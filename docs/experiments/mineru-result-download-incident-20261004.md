# Draft provider report: completed API task cannot retrieve its result

Status: prepared for review; not submitted.

Suggested destination: the official MinerU support channel or upstream issue tracker.

## Proposed title

Completed cloud API task: official result CDN HTTPS certificate validation fails

## Proposed report

On 2026-10-04, a GitHub Actions runner successfully authenticated, uploaded and
completed parsing of one new synthetic one-page PDF through the official MinerU
API. The task reached `done`. Downloading the returned full-result ZIP then
failed strict TLS validation at `cdn-mineru.openxlab.org.cn`, reporting an
expired certificate. Zero ZIP bytes were retrieved.

The same error was reproduced when retrieving already completed results from
retained production tasks. The later exact-source recovery runner used Python
3.11.16 and again stopped with `tls_certificate_expired` at result retrieval.
The client uses the provider-returned URL and normal HTTPS validation, without
hostname rewriting or redirects. Credentials and document contents are not
included in this report.

An independent GitHub Actions comparison at 2026-10-04 16:45 UTC used the system
CA store and certifi 2026.07.22. Both strict clients reported
`tls_certificate_expired`; neither received an HTTP response or body bytes.
This rules out a failure confined to the system trust store.

A separate authenticated temporary Cloudflare Worker at 2026-10-04 19:42 UTC
verified its own deployment readiness, then made exactly one strict HTTPS HEAD
to the CDN root from LAX. It received HTTP 526 (`tls_invalid_certificate`); the
Worker was subsequently deleted. No ZIP or document contents were requested by
that probe. A contemporaneous rerun of the existing completed synthetic task
made zero new parsing submissions and again failed its result download with
`tls_certificate_expired`, retrieving zero bytes.

Evidence runs in the public repository automation:

- New synthetic task and same-task rerun: `37212761333`, attempts 1 and 2.
- System CA / certifi comparison: `37217880580`.
- Readiness-verified Cloudflare HEAD: `37229206987`.

Cloudflare documents external Worker subrequests as requiring valid origin TLS:
https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/

Could you check the certificate chain served by the official result CDN, or
provide a documented, valid HTTPS alternative for retrieving completed tasks?
Authentication and parsing are working in the new-task test; result retrieval
is preventing the downstream document workflow from completing.
