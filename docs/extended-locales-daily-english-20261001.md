# Daily reading locales and English editorial access

## Reconciled baseline

Work continues from reviewed main `1c1c704f2eb678dce59e83967553e03b1df053e0`
in the existing clean isolated worktree. The dirty primary checkout is untouched.
All 33 non-English locale roots already use `portal-shared-v1`; the preceding
production acceptance retained 24 approved articles per locale (792 total).
That does not prove daily-new-content coverage.

Current daily producer `36801745121` is still working, not stopped: completed
locale jobs exist, two CPU jobs are active, and the remaining matrix jobs are
queued under the two-worker limit. One Khmer job failed; failure diagnosis and
durable recovery remain open. Refresh-triggered run `36907095539` is pending
behind it. Do not cancel or restart solely because the aggregate run says queued.

## Daily production policy restored

The repository lacked the opt-in variables used by its existing reviewed
handoff/reviewer code. The operator's request authorizes daily updates for the
already-live locale set. The following values were set and read back:

- `PORTAL_EXTENDED_INCREMENTAL_LOCALES=all-supported`
- `PORTAL_EXTENDED_AUTO_PUBLISH_LOCALES=all-supported`
- `PORTAL_EXTENDED_AUTO_REVIEW=true`

The environment still requires reviewer `yt-feng`; the existing
`GH_DISPATCH_TOKEN` name is present. No credential value was read or printed.
The 13 delegated-review regressions pass. Exact source/candidate/tree approval,
already-live locale limits, cutover acceptance and rollback remain required.
This is configuration, **not** a claim that a new daily batch is live.

Still required: freeze each source-day inventory before the slow locale queue;
advance deterministic <=24-page batches independently per language so one
failed language cannot starve the other 32; drain stored admitted work without
scraping historical pages; prove actual automatic production updates.

## English access implementation, not deployed

English is a separate text-only secondary-commentary product. It must not
reuse the full-reading renderer, report directory, chart pages or original
report bodies. Public HTML, JSON-LD and catalogues contain only preview text.
Full translated secondary commentary resides under private
`_english-commentary/v1/bodies/<sha256>.json` and is served only by the new
Worker access boundary.

Initial product rule: each registered account has 3 distinct full-commentary
reads, lifetime. Rereading an unlocked article does not spend another read.
Active existing website memberships (the established >=1 month membership
authority) have unlimited commentary reads; report/download trial quotas are
unchanged. Disabled or revoked sessions are checked by existing authentication.
Anonymous visitors see only previews and sign-in; exhausted accounts are
directed to the existing membership-request flow. No new payment system.

The new gateway allows only an approved versioned ledger and checksum-matched
text-only bodies. Unknown fields, original/report kinds, quoted-original blocks,
charts, images, embedded URLs, HTML and original-language prose fail closed.
Free grants use conditional R2 writes; concurrent requests cannot exceed 3.
Missing/corrupt content and permission/auth/membership errors cannot reset
allowances or return private text. Replies are private/no-store. Request bodies,
objects, field sizes, catalogue pages and quota retries are bounded.

14 synthetic gateway regressions currently pass, including concurrency,
membership expiry, anonymous requests, tampering and actual Worker route wiring.
Only code/tests exist at this checkpoint: the English source whitelist,
Hy-MT2 CPU builder, candidate/approval/cutover integration, public preview UI,
membership UX and live authenticated acceptance are still required. No English
page or translated commentary was fabricated, generated locally or published.

A live receipt refresh in this pass hit a DNS-resolution timeout. No local
network state was inspected or changed. The preceding verified production
baseline remains evidence; this failed check is not current live acceptance.
