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

The source-day queue and independent bounded cursors are implemented below.
Actual staging recovery and automatic production updates still require runtime
evidence; configuration and local tests alone do not prove those outcomes.

## Daily queue implementation, not yet merged

The fast `Extended locale source admission` workflow follows successful source
refreshes independently of the slow CPU matrix lock. It admits only the current
Shanghai source day, verifies the page-owned publication date, and freezes its
bounded <=500-page inventory privately in R2 before publishing a queue pointer.
No public model inference, translation artifact/cache or historical fetch occurs
in this admission step.

Each of the 33 locale cursors selects at most 24 unfinished/changed pages from
the immutable inventory. A locale that completed the first 24 can select its
next 2 while another locale resumes its first 24. Jobs carry their own exact
source generation; checkpoint memos still reuse validated unchanged units.
Hot newly admitted days have priority. Older work is only an already-admitted
R2 snapshot, never new discovery of historical URLs. Queue capacity is bounded
at 32 unfinished source days; overflow is explicit and discards nothing.

Continuation compares durable completed-page receipts against the admitted
inventory. Partial success can advance healthy locales, but unchanged failures
cannot self-dispatch forever. The two-CPU-worker/four-hour-per-locale limits,
complete-candidate requirement, approved-page carry-forward, normal release
lock and exact cutover/rollback are unchanged.

Delayed consumers now carry a checksum-bound admission proof. Before delegated
approval, the reviewer verifies the original capture's real main/public run,
attempt/SHA, successful source job, source day and exact inventory subset via
GitHub and R2. Merely labeling an old source as new cannot receive approval.
Existing reviewer identity and exact candidate/tree checks are not bypassed.

The roundtrip operation adds a separate unserved private staging probe for
source/admission/checkpoint recovery and independent cursor simulation. It
uses synthetic storage fixtures, zero model calls and no ready candidates;
synthetic completion metadata cannot be published. This probe has passed with
the in-memory R2 harness; a real Actions/R2 result is still required.

Local checks: queue/provenance/staging 16, daily incremental 21, handoff 10,
delegated review 15, publication/carry-forward 15, restore 3, R2 6 and financial
quantity 13 passed. Workflow syntax also passes the non-browser YAML parser.
Local PyYAML is absent; the Linux CI job installs it for the broader checks.

The exact Khmer failure in producer `36801745121`, job `110177654930`, is a
four-hour budget timeout (exit 75): 23/24 pages completed, checkpoint/candidate
storage steps passed, zero unit failures and zero paid-provider requests.
It is not an R2 or English-filter failure. Its durable partial checkpoint must
be resumed against the same source; an incomplete 23/24 candidate is not live.

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
The gateway plus existing membership-request and Newsfeed worker suites passed
29 tests together. The API is noindex/private/no-store; the future public
English preview HTML remains the SEO surface.

A live receipt refresh in this pass hit a DNS-resolution timeout. No local
network state was inspected or changed. The preceding verified production
baseline remains evidence; this failed check is not current live acceptance.
