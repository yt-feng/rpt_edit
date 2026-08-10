# Engagement, Analytics, and Course Access

This document defines the production contract for daily engagement rewards,
attribution analytics, and the gated Course page. Public source must keep using
the neutral Portal Suite identity and the existing contact placeholders.

## Daily rewards

The Worker is the only authority for reward dates, balances, streaks, and
claims. Dates use UTC+8 server time. The browser never submits a date or a
points balance.

- A successful daily check-in awards 10 points.
- The 3rd consecutive day adds 5 points, the 7th adds 20, and the 30th adds
  100. The highest applicable bonus is used.
- A check-in unlocks one ordinary catalog PDF for that server date. It cannot
  be banked.
- 70 points unlock one additional ordinary catalog PDF. At most one points
  claim is allowed per server date.
- A reward can only target a current catalog item with a PDF descriptor.
- Accounts that already have access do not consume a reward.

Reward state is stored under the private R2 account namespace and updated with
ETag compare-and-swap. This makes duplicate or concurrent check-ins and claims
idempotent without requiring a same-release database migration. The same
conditional write records a permanent report grant alongside the daily claim,
so there is no cross-object rollback window. The existing `report_purchases`
record is a compatibility mirror: its failure cannot consume a reward without
granting access, and a later request can still use the atomic reward grant.

API contract:

- `GET /rewards`: current balance, streak, today's check-in and claim state.
- `POST /rewards`: idempotent daily check-in.
- `POST /rewards/claim`: `{ "reward_kind": "daily|points", "report_id": "..." }`.

## Course gate

`courses.html` is visible in the top navigation, but its static HTML contains no
course names or course contact details. After `GET /course/access` succeeds, the
browser materializes the catalog from the authenticated response. The Worker
accepts a full membership entitlement or an unlimited full-site administrator
grant, and requires it to be lifetime or to expire at least 30 * 24 hours after
the server check. Filtered grants, finite-download grants, and trials do not
unlock Course. Privileged operational accounts remain eligible.

The gated API catalog contains 43 hand-authored, topic-based entries spanning
financial modeling, capital markets, private investing, investment research,
capital-markets law, legal professional skills, reference libraries, career
development, and general professional education. Every entry has a neutral
`id`, `category`, `title`, `summary`, and `audience`. These public-facing fields
must describe subject matter only. They must never be copied from an upstream
directory name, file name, provider label, community name, instructor name, or
private storage locator. Investment-bank names may be retained when they are
material to the subject matter.

During the frontend rollout, an eligible response includes both `courses`, a
title-only string array for the previous client, and `course_catalog`, the 43
structured entries used by the current client. An anonymous response contains
neither field, while an authenticated but ineligible response contains empty
arrays. This keeps catalog details behind the same server-side membership gate
throughout a Worker-first or static-site-first deployment.

Contact details are returned only in the successful authenticated response and
come from the private release injection process; do not place a real personal
address in public source. Raw inventory documents, exact resource counts,
storage paths, and source file names remain outside the repository and are
never serialized by this API.

## Analytics collection

`assets/analytics.js` is the common client for application, legal, generated
report-index, SEO report, and Blog pages. It emits one page view per page/path
and supplies the same context to application events:

- persistent anonymous visitor ID;
- 30-minute session ID, landing path, and first-seen/returning state;
- referrer and referrer host;
- UTM source, medium, campaign, term, and content;
- language, screen, navigation type, and coarse device hint.

The browser records only `pathname`; UTM values have dedicated bounded fields.
The Worker independently removes query strings and fragments from path,
landing, and referrer values, so password or download-token parameters cannot
enter the archive. The public endpoint accepts only same-origin requests,
bounded JSON bodies, and an event-type allow-list.

The Worker adds country/colo, a keyed IP hash, coarse device classification,
and available Cloudflare bot-management hints. Raw IP addresses are never
written, and the IP hash is omitted if its deployment secret is unavailable.
Every event remains mirrored under the primary and backup private R2 analytics
prefixes.

## Per-day administrator summary

`GET /account-admin/analytics-day-summary?date=YYYY-MM-DD` is super-user only.
Large days are scanned in bounded R2 batches. An incomplete response returns a
private opaque `job_id`; the caller repeats the request with the date and job
ID until `has_more` is false. Completed summaries are cached privately by date.
`refresh=1` starts a clean rescan.

The public response includes event/page-view counts, unique visitor/session
counts, top paths, referrer hosts, countries, devices, bot hints, event types,
and UTM dimensions. It never returns visitor IDs, IP hashes, or the internal
deduplication set. The Activity page implements the polling and progress UI.

## Verification

Coverage is provided by:

- `portal_suite/tests/engagement-rewards.test.mjs`
- `portal_suite/tests/analytics-attribution.test.mjs`
- the existing portal frontend, export-pagination, Blog build, and SEO suites.
