# Supplemental source-lead adapter

This adapter adds metadata-only report leads from a privately configured search
service. Public code, API responses, fixtures, errors, and logs use the neutral
`supplemental` identity. The upstream hostname and any source-specific redaction
terms exist only in encrypted deployment configuration.

## Deployment secrets

Configure these Worker secrets; do not commit their values:

- `SUPPLEMENTAL_SEARCH_URL`: HTTPS search endpoint.
- `SUPPLEMENTAL_SEARCH_HMAC_SECRET`: at least 16 characters. It converts each
  private upstream locator into a stable opaque ID.
- `SUPPLEMENTAL_SEARCH_REDACT_TERMS`: optional comma/newline-separated source
  labels that must be removed from public metadata.

The Worker also needs its existing private `REPORT_BUCKET` binding. The adapter
is disabled unless the URL, HMAC secret, and bucket are all present.

## Preferred JSON contract

The adapter sends a `GET` request with both generic and compatibility query
parameters:

- `q` and `kw`: the user query.
- `page`: one-based page number.
- `p`: zero-based page number.
- `page_size`: currently `20`.

The preferred response is JSON:

```json
{
  "total": 1,
  "items": [
    {
      "url": "https://search.example.invalid/reports/1001.html",
      "title": "Example report title",
      "date": "2026-08-09",
      "institution": "Example Research",
      "page_count": 24,
      "tags": ["components"],
      "summary": "Public-safe metadata only."
    }
  ]
}
```

Common aliases such as `results`, `records`, `published_at`, `publisher`, and
`pages` are accepted. JSON is preferred because it avoids coupling the Worker to
presentation markup.

## HTML compatibility

When the endpoint returns HTML, the compatibility parser reads:

- one result per `article.excerpt`;
- title and locator from `header h2 a`;
- date from `time`;
- institution and page count from `.meta .cat`;
- tags from `.article-tags a`.

The source must explicitly allow automated access to the configured endpoint.
If its public search route disallows automation, expose a dedicated private JSON
feed instead and store that URL in `SUPPLEMENTAL_SEARCH_URL`.

## Privacy boundary

For every accepted result, the adapter:

1. resolves and validates the HTTPS locator;
2. derives `supplemental:<opaque-id>` with HMAC-SHA-256;
3. writes the raw locator plus sanitized metadata only to
   `_source-leads/items/<opaque-id>.json` in private R2;
4. returns only the opaque ID and public-safe metadata to the browser.

URLs, email addresses, configured source labels, and hostname labels are removed
from public text. Upstream failures become a fixed neutral error and never echo a
URL, response body, or source name.

## Worker integration points

Import from `workers/portal-suite-worker/src/source-lead-adapter.js`:

- `sourceLeadAdapterEnabled(env)` for feature detection;
- `searchSourceLeadMetadata({ env, query, page })` for on-demand search;
- `sanitizeSourceLeadError(error)` for a neutral API error;
- `readStoredSourceLead(env, id)` for private operator-side lead resolution.

The Worker integrates these records into `GET /authority/search`. Browser-facing
records keep the established `source: "authority"` contract and use
`kind: "domestic-lead"` plus the neutral `国内报告线索` label. Supplemental lookup
runs independently in parallel, so a failure does not remove results from the
existing authority sources.

`GET /authority/item?id=supplemental:<opaque-id>` returns the same sanitized
metadata. It never returns the stored locator. The existing `/authority/pdf`
endpoint remains contact-only and returns `403` for every authority kind.
The unified detail page shows the privately injected support channel and email,
and its request button emits only a neutral `report_request` analytics event.

Both `portal-worker-emergency-deploy.yml` and `neutral-edge-cutover.yml` upload
the three configuration values as Wrangler secrets. The neutral-edge refresh
leaves existing Worker secrets untouched when the required URL or HMAC secret is
missing.

Run the contract tests with:

```bash
node scripts/test_source_lead_adapter.js
node scripts/test_portal_source_lead_integration.js
```
