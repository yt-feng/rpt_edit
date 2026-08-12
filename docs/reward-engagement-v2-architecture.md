# Reward Engagement v2

This document defines the server-side contract for the second reward policy.
The Worker is the only authority for reward dates, balances, streaks, report
credits, claims, and permanent report grants. All calendar dates use UTC+8.

## Product policy

- A successful check-in awards 10 points exactly once per server date.
- The existing streak bonuses remain unchanged: the highest applicable bonus
  is +5 on each third streak day, +20 on each seventh streak day, and +100 on
  each thirtieth streak day.
- A newly registered v2 account receives one `welcome_d1` report credit on its
  first lifetime check-in. It expires exactly 72 hours after issue.
- An account receives one `streak_d3` report credit the first time it reaches a
  three-day streak. It also expires exactly 72 hours after issue.
- No other ordinary check-in creates a report credit. In particular, checking
  in after the onboarding milestones does not create a daily free report.
- The first seven-day streak records one future streak-protection card. The v2
  release persists the milestone, but does not present it as active protection
  until automatic consumption is implemented.
- Seventy points still grant one additional ordinary catalog PDF. At most one
  points claim is allowed per server date.
- A credit or points reward can only target a current catalog item whose PDF is
  available. Existing report ownership never consumes a reward.
- Ownership is checked again inside the reward-state compare-and-swap mutation,
  so simultaneous credit and points requests for the same report consume
  exactly one reward.

The public status deliberately keeps the legacy `daily_*` response fields so
the current client remains compatible. Under v2, `daily` means "claim the
earliest-expiring valid report credit"; it no longer means "today's check-in
automatically created a report slot."

## State and credit lifecycle

Reward state remains at `_account/rewards/<normalized-email>` and is updated by
an R2 ETag compare-and-swap loop. Version 2 adds:

- `schema_version` and `policy_version`;
- `credits`, an idempotent list of issue, expiry, claim, and report metadata;
- `welcome_credit_issued` and `first_d3_credit_issued` one-time guards;
- `first_d7_freeze_issued` and the capped `freeze_cards` balance;
- `policy_migrated_at`.

Credit identifiers are stable (`welcome-v2`, `milestone-d3-v2`, and the dated
cutover identifier), so concurrent retries cannot issue duplicates. A credit
is valid only while `claimed_at` is empty and `expires_at` is strictly later
than Worker time. A `daily` claim sorts valid credits by expiry, issue time,
and identifier and atomically consumes the earliest one in the same conditional
write that creates the permanent report grant. Expired credits never authorize
access. A compatibility purchase record is written only after the atomic grant;
failure of that mirror cannot revoke or duplicate the reward.

The status response includes:

- `credits`, `credits_available`, and `next_credit_expiry`;
- `next_milestone`, with the next D1 credit, D3 credit, D7 protection card, or
  points-bonus milestone;
- `freeze_cards`;
- the legacy `daily_available`, `daily_claimed`, `daily_report_id`,
  `points_claimed_today`, `points_report_id`, and `next_bonus` fields.

## Lazy migration

The production cutover starts at `2026-08-12T00:00:00+08:00`. An environment
override exists for deterministic validation, but an invalid override falls
back to the production timestamp.

The first reward GET, check-in, or claim after deployment migrates an old object
inside the same conditional-write loop:

1. Existing points, current and longest streaks, check-in history, claims, and
   permanent grants are copied without recomputation.
2. Accounts created before the cutover are marked as having passed the welcome
   milestone and never receive a D1 credit.
3. Existing longest streaks of at least three or seven set the corresponding
   one-time milestone guard. A migrated current streak of at least seven keeps
   one protection card.
4. If an old state checked in on the cutover date but did not claim its legacy
   daily report, that same-day promise becomes one `legacy_cutover` credit. It
   expires at the end of that UTC+8 date. Migration on a later date never
   revives the expired legacy benefit.
5. The version and migration timestamp are recorded. ETag contention retries
   against the latest state, making migration and a simultaneous check-in or
   claim idempotent.

New v2 accounts are identified from the authoritative account `created_at`
timestamp. Reading reward status prepares their v2 state but does not issue a
credit; only the first successful check-in issues the D1 welcome credit.

## Request execution

- `GET /rewards` lazily migrates when needed and returns private, no-store
  status.
- `POST /rewards` migrates and checks in with one reward-state read followed by
  at most one winning conditional write. Its response is constructed from the
  winning state and does not perform a second R2 read.
- `POST /rewards/claim` accepts the existing
  `{ "reward_kind": "daily|points", "report_id": "..." }` shape. A `daily`
  request requires an unexpired credit rather than a same-day check-in.
- Check-in and claim analytics are best-effort background work registered with
  `ExecutionContext.waitUntil`; analytics storage latency never delays the
  user-facing reward response.
- The compatibility purchase mirror also runs through `waitUntil`; the atomic
  grant is immediately authoritative and mirror latency cannot delay a claim.
- GET computes an effective streak from the server date. If the last check-in
  is older than yesterday, the displayed current streak is zero before the next
  check-in while the historical longest streak remains unchanged.

## Verification contract

The focused reward suite covers D1 and D3 issue/expiry, the D7 protection-card
record, duplicate and concurrent check-ins, concurrent claims, earliest-expiry
selection, expired-credit rejection, lazy legacy migration, cutover-day
preservation, old-account exclusion from the D1 reward, permanent authorization
when the compatibility mirror fails, and the absence of a second reward-state
read after check-in.
