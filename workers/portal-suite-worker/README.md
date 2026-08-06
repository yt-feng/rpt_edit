# Document Gateway Worker

This Worker validates access and serves private document files from object storage as attachments. Public naming is intentionally generic; historical route and directory names remain for compatibility.

## Required Configuration

- R2 binding: `REPORT_BUCKET`
- Secrets: `PASSWORD_SECRET`, `CALC_KEY`
- Vars: `CATALOG_URL`, `PASSWORD_RULES_URL`, `ALLOWED_ORIGIN`, `ACCOUNT_STORE_MODE`
- Optional var: `R2_OBJECT_PREFIX`, default `reports`

Production must set `ACCOUNT_STORE_MODE = "supabase"` and configure both the account-store URL and service-role credential. Missing, partial, or mixed account-store configuration fails closed; it never falls back to legacy object-storage user indexes. The object-storage account mode is reserved for local tests and controlled migration work.

## Access Model

The Worker supports multiple authorization paths:

- authenticated account access;
- shared access phrase validation;
- single-item derived access codes;
- admin-created custom grants.

Single-item codes are derived with HMAC-SHA256 over a private message domain and the item identifier, then base32-encoded, truncated, and grouped for display. See `docs/service-architecture.md` for the neutral architecture description.

## Operational Alerts

Workflow failure email alerts use a signed server-to-server endpoint:

- the recipient is configured server-side;
- requests carry a timestamp and HMAC signature;
- successful sends are deduplicated in object storage for a bounded window;
- callers cannot override the destination recipient.

## External Adapter Support

The Worker can proxy optional source adapters and cache prepared files in object storage. Public UI and documentation should describe these as generic source adapters rather than naming upstream brands.

Historical endpoints may remain available so existing frontend code keeps working. Do not add new public docs that market those route names as product features.

## Development Checks

```bash
node --check workers/portal-suite-worker/src/index.js
```

Run the relevant Worker tests before deploying behavior changes.
