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
to the CDN root. LAX was the recorded ingress, not a separately proven execution
location. It received HTTP 526 (`tls_invalid_certificate`); the
Worker was subsequently deleted. No ZIP or document contents were requested by
that probe. A contemporaneous rerun of the existing completed synthetic task
made zero new parsing submissions and again failed its result download with
`tls_certificate_expired`, retrieving zero bytes.

Evidence runs in the public repository automation:

- New synthetic task and same-task reruns: `37212761333`, attempts 1 through 3.
- System CA / certifi comparison: `37217880580`.
- Readiness-verified Cloudflare HEAD: `37229206987`.
- Platform-confirmed Cloudflare TPE and SIN execution: `37231111280` and
  `37231384448`; both strict HEAD requests returned HTTP 526 and both temporary
  Workers were deleted. No ZIP, provider submission or R2 write occurred.

The cloud runner's exact public certificate chain was captured at
2026-10-04 20:29 UTC in run
[`37232259586`](https://github.com/yt-feng/rpt_edit/actions/runs/37232259586).
Both default negotiation and a separate TLS 1.2 RSA handshake failed strict
verification with code 10 at depth 0. Both received the same leaf:

- Subject: `CN=*.openxlab.org.cn`.
- Issuer: `RapidSSL TLS RSA CA G1`, DigiCert.
- Validity: 2026-03-18 00:00:00 UTC through **2026-10-02 23:59:59 UTC**.
- SHA-256: `12137420c572ee3fde42af27309c8f36efdfc4d07e76dcba801ddf6bc308aeb3`.
- The supplied intermediate remains valid through 2027-11-02; the failure is
  the expired website leaf certificate, not an expired intermediate.

Separately, a strict public-host handshake observed a different valid Let's
Encrypt YR1 leaf for the same hostname, valid 2026-09-17 through 2026-12-16,
SHA-256 `1e147f041f9b57d2897777429cc01970047022f2140006d826ac84726604a0ef`.
This does not establish a working cloud result download. The different observed
certificates suggest inconsistent certificate deployment across the service's
connection paths; the provider needs to verify its actual serving configuration.
The exact expired certificate explains the current result-download failure. It
does not establish the cause of separate historical parsing failures or all
earlier missing issues.

Cloudflare documents external Worker subrequests as requiring valid origin TLS:
https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/

Could you check the certificate chain served by the official result CDN, or
provide a documented, valid HTTPS alternative for retrieving completed tasks?
Authentication and parsing are working in the new-task test; result retrieval
is preventing the downstream document workflow from completing.
