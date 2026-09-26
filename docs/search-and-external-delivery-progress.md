# Search and external full-text delivery (2026-09-26)

## Scope and evidence

The operator requested whole-title/middle-phrase search and full-PDF-first delivery
for Other reports, with one-page preview and a full-text request form only as a
fallback. Work is isolated from the primary checkout's uncommitted changes and
from the extended-locale branch. Baseline: main
`5d3259476527350afd6b6dfcfafc904876276eac`.

A read-only live catalog check found the reported Bernstein title at report ID
`bd2f0e55e45760414e4424a7`, date `260325`, in the 14,677-item catalog updated
`2026-09-26 10:02:31 +0800`. It is marked text-only (`available=false`). The current
catalog matcher already supports the exact title and `unlock solid`; this does
not reproduce or explain the September 12 incident. A PDF-only/date filter can
exclude that row. Tests now retain these cases, plus invisible PDF-copy characters,
missing English connective words and exact-phrase ranking. Subject terms, numbers
and negations remain required. Search help explains that no keyword count is needed.
No new remote search calls, paid model, history translation or permissions change
is introduced by the search improvement.

## Delivery change

The frontend previously returned before checking ordinary members' entitlements;
the external PDF endpoint also rejected them before trying the source or verified
cache. Eligible accounts now use the existing entitlement decision, source
readability checks, acquisition workflow, PDF/page-count verification and final
quota recheck. An ordinary shared password alone still does not grant external
full access; administrator-issued report-bound deliveries remain supported.

Pending acquisition stays pending and does not consume quota. Source denial,
failed acquisition or source unavailability can expose a one-page preview and
the prefilled, deduplicated **索取全文** form. The initial detail page prioritizes
the account full-download action; its preview starts hidden. Connection/QR/token
management stays administrator-only. No unvalidated bytes or one-page PDF are
accepted as a full report. Existing Hot-report archive policies remain unchanged.

## Handoff boundary

Local validation: 538 tests across all 56 frontend/Worker test files passed;
35 Python API-acquisition/deployment-contract tests passed. Legacy entitlement,
detached-payment, source-lead and chart-search scripts passed. App loading budget,
JavaScript syntax, public identity audit (5,914 files) and diff whitespace passed.
The local Python QR decoder suite could not import `zxingcpp`; it was not counted
as passed. The PR workflow already installs this dependency and runs that suite.
The changed search/auth-refresh tests are now included in the PR audit as well.

Submit through normal PR checks. Do not rerun article generation or change
network settings. No production deployment or real authenticated full download
is claimed by these local contract tests. The user requested no Action monitoring.
The separately dispatched 33-locale candidate run is `36216968278`, source
`044d268a6ec79b54b5d70d77f39130e1d6093ef2`; do not poll it.
