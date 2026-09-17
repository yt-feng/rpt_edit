# External report download integration

Portal account access and source-provider download access are separate checks. A Portal member may be allowed to download a report while the upstream connection is absent, expired, or lacks the relevant allowance. A report preview is never a replacement for the full file.

## Download path

1. Authenticate the Portal request and check its existing report entitlement.
2. Read upstream access controls from the response envelope, with a deliberate fallback only for older payloads. Report page counts may be nested under `main.meta_data`.
3. Serve only a validated stored PDF. For older stored files without validation metadata, preserve the original and validate its actual pages before delivery.
4. If the upstream permits a new download, dispatch only the report ID. The background job reads the saved upstream session directly from private storage; session credentials never appear in dispatch data, public responses or diagnostics.
5. Download the API-provided PDF, check its real page count, sanitize external links and upload with validation metadata. Do not convert preview images or print the page shell into a purported full report.
6. Poll preparation status with the current Portal authentication headers. The existing privileged owner can receive a reconnect QR flow; ordinary members receive the Portal report-request path.

Source access denial should return a specific login/access state without starting repeated anonymous browser jobs. Provider transport errors remain distinct from permission failures. The saved connection is confirmed by storage readback before the interface reports successful connection.

## Incident reproduced on 2026-09-17

Two report IDs, `1294129388408934400` and `1256239582803005440`, failed in Actions runs `35195321371` and `35195433668`. Both upstream responses placed `readable: false` and `resource_limit: 0` at the top level, while the previous parser inspected `main`. The jobs had no upstream cookie or token and saw image previews. The source metadata reported five and six pages respectively.

The status poll also omitted Portal authentication headers, hiding the owner's reconnect instructions. A separate size-only status check could reject valid short PDFs; verification now relies on the file's actual page count and stored validation evidence.

Production acceptance requires the live page and API state, the background job's typed result, and a full validated PDF when the connected account permits it. A merged change, accepted dispatch, PDF header or green upload step alone does not establish successful delivery.
