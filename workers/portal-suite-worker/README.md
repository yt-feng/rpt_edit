# Document Gateway Worker

This Worker validates access and serves private document files from object storage as attachments.

## Runtime

Runtime bindings and variables are supplied by the deployment workflow. Account-store configuration is explicit, and incomplete account-store setup fails closed.

## Access Model

The Worker supports multiple authorization paths:

- authenticated account access;
- shared access phrase validation;
- single-item derived access codes;
- admin-created custom grants.

Single-item codes are derived with HMAC-SHA256 over a private message domain and the item identifier, then base32-encoded, truncated, and grouped for display. See `docs/service-architecture.md` for the neutral architecture description.

## Operational Alerts

Workflow failure email alerts use a signed server-to-server endpoint:

- the recipient is selected server-side;
- requests carry a timestamp and HMAC signature;
- successful sends are deduplicated in object storage for a bounded window;
- callers cannot override the destination recipient.

## External Adapter Support

The Worker can proxy optional source adapters and cache prepared files in object storage. Public UI and documentation should describe these as generic source adapters rather than naming upstream brands.

Historical endpoints may remain available so existing frontend code keeps working.

## Development Checks

```bash
node --check workers/portal-suite-worker/src/index.js
```

Run the relevant Worker tests before deploying behavior changes.
