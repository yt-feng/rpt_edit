# Portal Suite Worker

This Worker validates Portal Suite passwords and serves private PDFs from Cloudflare R2 as attachments.

Required Worker configuration:

- R2 binding: `REPORT_BUCKET`
- Secrets: `PASSWORD_SECRET`, `CALC_KEY`
- Vars: `CATALOG_URL`, `PASSWORD_RULES_URL`, `ALLOWED_ORIGIN`
- Optional var: `R2_OBJECT_PREFIX`, default `reports`

Workflow failure email alerts reuse the configured Newsfeed mail provider:

- Var `OPS_ALERT_EMAIL`: operations recipient.
- Secret `OPS_ALERT_SIGNING_KEY`: HMAC key shared only by GitHub Actions and the Worker.
- Endpoint `POST /ops/alerts/email`: accepts signed server-to-server requests, never accepts a caller-provided recipient, and deduplicates successful sends in R2 for 24 hours.
- Headers: `X-Portal-Timestamp` and `X-Portal-Signature: sha256=<hmac(timestamp.body)>`.

## Reportify module

The Worker also proxies the public reportify.cn search and serves reportify PDFs for the
"其他报告 · Reportify" section on the search page:

- `GET /reportify/search?q=<keyword>&page=<n>` — proxies `api.reportify.cn/reports?query=...`
  (no login) and returns a slim `{ items, page, total_page }`.
- `GET /reportify/pdf?id=<report_id>` — three-step delivery:
  1. directly readable reports → stream their presigned PDF (instant, no browser);
  2. else if the PDF was already grabbed → stream it from R2 key `reportify/<id>.pdf`;
  3. else (gated) → fire the `reportify-grab` GitHub workflow via `repository_dispatch` and
     return `202 {status:"pending"}`. The grab uploads the PDF to R2; a later request serves it.
- `GET /reportify/status?id=<report_id>` — `{ ready: bool }` (R2 object present), used for polling.

Extra config for this module (only needed so a gated click can trigger the grab):

- Var `GH_REPO` — e.g. `source/example`.
- Secret `GH_DISPATCH_TOKEN` — a fine-grained GitHub PAT with **Actions: read and write** on this
  repo (`wrangler secret put GH_DISPATCH_TOKEN`). Without it, readable reports still work; gated
  reports return a link to view on reportify.cn instead.

The GitHub Actions deployment can keep `portal_suite/password_rules.json` as a template. If `PORTAL_DOWNLOAD_PASSWORD` and `PASSWORD_SECRET` are present as GitHub Actions secrets, the Pages artifact receives the generated password hash automatically.

Per-report pseudo-passwords are also accepted. The rule is:

```text
PORTAL-<first 12 chars of base32(hmac_sha256(PASSWORD_SECRET, "portal-suite:" + report_id)) grouped as 4-4-4>
```

Use the hidden Worker calculator endpoint to avoid exposing `PASSWORD_SECRET`:

```text
https://<worker>/calc?id=<report_id>&key=<CALC_KEY>
```

The Pages workflow can generate a `wrangler.toml` during deployment when the GitHub repository has:

- Secret `CLOUDFLARE_API_TOKEN`
- Variable `CLOUDFLARE_ACCOUNT_ID`
- Variable or secret `R2_BUCKET`
- Variable `PORTAL_PAGES_URL`

Manual setup:

```bash
cp wrangler.toml.example wrangler.toml
wrangler secret put PASSWORD_SECRET
wrangler secret put CALC_KEY
wrangler deploy
```
