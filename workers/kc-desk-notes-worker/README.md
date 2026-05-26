# KC Desk Notes Worker

This Worker validates KC Desk Notes passwords and serves private PDFs from Cloudflare R2 as attachments.

Required Worker configuration:

- R2 binding: `REPORT_BUCKET`
- Secret: `PASSWORD_SECRET`
- Vars: `CATALOG_URL`, `PASSWORD_RULES_URL`, `ALLOWED_ORIGIN`
- Optional var: `R2_OBJECT_PREFIX`, default `reports`

The GitHub Actions deployment can keep `kc_desk_notes/password_rules.json` as a template. If `KC_DESK_DOWNLOAD_PASSWORD` and `PASSWORD_SECRET` are present as GitHub Actions secrets, the Pages artifact receives the generated password hash automatically.

The Pages workflow can generate a `wrangler.toml` during deployment when the GitHub repository has:

- Secret `CLOUDFLARE_API_TOKEN`
- Variable `CLOUDFLARE_ACCOUNT_ID`
- Variable or secret `R2_BUCKET`
- Variable `KC_DESK_PAGES_URL`

Manual setup:

```bash
cp wrangler.toml.example wrangler.toml
wrangler secret put PASSWORD_SECRET
wrangler deploy
```
