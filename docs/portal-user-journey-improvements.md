# Incremental user journey improvements

This change improves report discovery, return visits, and membership applications
without moving the established navigation, report list, report links, or download
controls. It does not change membership entitlements or password download access.

## Application flow

The existing membership and access links open the existing account dialog in an
application view. Its title and initial focus now match the requested action. The
view explains that an application can be sent without registration or login, and
keeps the existing required contact fields and optional note. Applicants can
switch to login and return without losing the current draft.

An application is complete only after the existing API accepts it. Errors retain
the draft and permit an explicit retry. A response for an expired login clears
only that same login, allowing a subsequent guest application; it never silently
repeats a submission or clears a newer login. Temporary account verification
errors no longer log users out. All download entitlements remain server-checked.

## Search and return visits

The original search field gains a small, conditional resume control. The browser
stores at most one keyword for 30 days, scoped to the page language. Restoring
it requires a click; a fresh homepage still shows current reports, and a URL
query or text already entered takes precedence. The record can be cleared. User
keywords are rendered as text, and unavailable browser storage does not break
search. Filters and pagination are not automatically restored. A restored query
uses the normal input event so the catalog and any localized collection update
together, while the existing catalog content language remains unchanged.

A zero-result message applies specifically to the current catalog. When filters
are active, an inline action clears those filters while retaining the keyword.
The existing remote sources and search timing remain in place.

## Measurement

Both the common browser analytics client and the Worker now accept the existing
`membership_request` event. Previously each allowlist omitted it. Historical
absence therefore cannot establish zero applications.

Versioned events identify form display, opening, first edit, submission attempt,
accepted response, duplicate acceptance, error, and abandonment. Application
kind, action, status, placement, and error are controlled labels. Form email,
contact value, note, and arbitrary response text are excluded from telemetry.
Membership, access, support, privacy, and refund requests remain separate.

The aggregate review also reports device and new/returning/unknown segments,
download waiting/error outcomes, and their overlap with observed success. See
[the growth metric definitions](portal-growth-operating-system.md) for coverage
and denominator rules. Private aggregate evidence stays outside public source.

## Evaluation after publication

Record the actual accepted release and observation start before comparing
outcomes. Do not backdate the experiment ledger to the implementation date.

- First validate application event delivery and successful-response accounting.
- Compare membership/access application completion within versioned observed
  sessions, including mobile and returning-user segments when samples permit.
- Track report-open and observed download-success sessions alongside applications;
  an increase in applications does not justify making report access harder.
- Compare new cohorts only after their complete D1/D7 observation windows. Local
  search restoration is a hypothesis to evaluate, not evidence of improved
  retention by itself.
- Keep the existing navigation and download paths during evaluation. If a change
  interferes with core behavior, revert that change while retaining measurement.

The local preview uses API fixtures and sends no real membership application.
Local tests and preview acceptance do not establish a production deployment or
an improvement in conversion or retention.
