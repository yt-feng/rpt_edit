# GitHub-hosted social publishing control plane

Last reviewed: 2026-08-31

## Decision

Use the official YouTube, LinkedIn, and X APIs from GitHub-hosted Actions. Do
not store browser Cookies and do not automate any platform website.

The first production shape is deliberately narrow:

- upload one approved long-form video to YouTube;
- publish independently written supporting posts to LinkedIn and X;
- use a protected GitHub Environment for the first canary posts;
- keep the hourly automatic queue disabled until the canary comparison passes;
- monitor credentials and public reach from GitHub Actions, with email through
  the existing signed Worker to Brevo path.

This design removes the known policy problem created by browser scripting. It
does not claim that any delivery method can guarantee views. None of the three
platforms publishes a guarantee that API posts receive identical distribution,
and all three reserve discretion over ranking. The controls below address the
factors their public policies do identify: visibility settings, repetitive or
mass-produced content, high-volume patterns, misleading links, unsolicited
automation, authorization state, and processing failures.

## Tool research

| Option | GitHub integration | Credential handling | YouTube coverage | Fit for this project |
| --- | --- | --- | --- | --- |
| Direct official APIs | Native HTTP from Actions | Our Secrets and daily read-only checks | Long-form and Shorts | **Selected.** Fewest intermediaries and every publishing field is explicit. |
| Buffer API | GraphQL API from Actions; official partner integrations | Buffer owns social OAuth; API keys can be 7 days to 1 year and Buffer emails before/at expiry | Shorts only, up to 3 minutes; no long-form | Best fallback if maintaining LinkedIn/X OAuth becomes undesirable. Optional monitor support is included. |
| Metricool | API can be called from Actions | Metricool owns social OAuth | Supports YouTube scheduling | Good for a larger editorial/analytics team, but API requires Advanced or Custom and X is a paid add-on. |
| Native platform schedulers | No custom GitHub pipeline | Platform session | Full native features | Appropriate for occasional manual posts, not the requested cloud workflow. |
| Cookie/browser automation | Technically scriptable but not an official publishing interface | Browser session must be copied and renewed | Website-dependent | **Excluded.** LinkedIn and X explicitly prohibit scripting their websites; it also creates fragile login challenges. |

Primary tool sources:

- [YouTube `videos.insert`](https://developers.google.com/youtube/v3/docs/videos/insert)
- [LinkedIn Posts API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api?view=li-lms-2026-08)
- [X Manage Posts API](https://docs.x.com/x-api/posts/manage-tweets/introduction)
- [Buffer API and supported channels](https://support.buffer.com/en-us/articles/using-buffers-api-GtIYIQilz5)
- [Buffer API-key expiry emails](https://support.buffer.com/en-us/articles/how-to-create-your-buffer-api-key-ShIgYVwM6j)
- [Buffer YouTube Shorts limitation](https://support.buffer.com/en-us/articles/using-youtube-shorts-with-buffer-Jl8iR6jIck)
- [Metricool plans and API access](https://help.metricool.com/plans-add-ons-and-api-access-explained-xux1u)

## What the platform rules actually support

### YouTube

The official API is a supported upload channel. YouTube's published performance
framework focuses on whether viewers choose a video, keep watching, and report
satisfaction; it does not list `videos.insert` as a negative ranking signal.
That is evidence for using the official API, not a written promise of equal
distribution.

Two concrete causes can look like “API upload got zero views”:

1. API projects created after 2020-07-28 that have not passed a YouTube API
   compliance audit have their uploads restricted to `private`.
2. A scheduled upload must remain `private` until `status.publishAt`; processing
   or status mismatches must be read back after upload.

The publisher therefore uses resumable upload, writes the visibility and
schedule in the initial request, polls `videos.list`, and stops if the returned
visibility differs from the requested public/unlisted state. Before launch,
complete the [YouTube API audit form](https://support.google.com/youtube/contact/yt_api_form).

YouTube now explicitly prohibits automated or synthetic mass-production of
many minimally different videos. Its monetization policy calls mass-produced,
template-like output “inauthentic content.” Every manifest must therefore have
unique metadata and a durable near-duplicate check. See the
[YouTube spam policy](https://support.google.com/youtube/answer/2801973?hl=en)
and [channel monetization policy](https://support.google.com/youtube/answer/1311392).

`status.containsSyntheticMedia` is mandatory in this control plane. YouTube
says correct disclosure of realistic altered/synthetic material does not, by
itself, limit audience or monetization eligibility. See
[YouTube's GenAI disclosure guidance](https://support.google.com/youtube/answer/14328491?hl=en)
and the [`containsSyntheticMedia` API field](https://developers.google.com/youtube/v3/docs/videos#status.containsSyntheticMedia).

### LinkedIn

Personal profile publishing can use the self-service `Share on LinkedIn`
product and `w_member_social`. Company Page publishing uses
`w_organization_social`, an eligible Page role, and the applicable Community
Management review. See [Share on LinkedIn](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin)
and the [Posts API permissions](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api?view=li-lms-2026-08).

Every post payload is forced to:

```json
{
  "visibility": "PUBLIC",
  "distribution": {
    "feedDistribution": "MAIN_FEED",
    "targetEntities": [],
    "thirdPartyDistributionChannels": []
  },
  "lifecycleState": "PUBLISHED"
}
```

This prevents an accidental dark post (`feedDistribution: NONE`) from being
mistaken for an organic post. LinkedIn's public ranking explanation lists
identity, content relevance/quality, relationships, activity, and recency; it
does not list the official Posts API as an automatic penalty. LinkedIn does,
however, restrict high-volume or spam-like behavior and explicitly prohibits
software that automates its website. See
[LinkedIn feed relevance](https://www.linkedin.com/help/linkedin/answer/a1339724),
[high-volume content](https://www.linkedin.com/help/linkedin/answer/a1339697/high-volume-of-messages-sent),
and [automated activity](https://www.linkedin.com/help/linkedin/answer/a1340567/automated-activity-on-linkedin?lang=en).

### X

The publisher uses `POST /2/tweets` with OAuth 1.0a user context. For a single
owned account this avoids the rotating refresh-token storage required by an
OAuth 2.0 PKCE integration. The App must be configured as read/write.

X explicitly permits useful automated information broadcasts through its API,
but prohibits non-API website scripting, automated trend hijacking, duplicate
or substantially similar posts, misleading links, unsolicited mentions and
replies, and automated engagement. X also states that these patterns can remove
posts from search or other discovery surfaces. See the
[X automation rules](https://help.x.com/en/rules-and-policies/x-automation),
[X search rules](https://help.x.com/en/rules-and-policies/x-search-policies),
and [authenticity policy](https://help.x.com/en/rules-and-policies/authenticity).

The X API currently uses prepaid pay-per-use credits. The published rate table
lists a lower write price for content without a URL and a materially higher
price for content containing a URL, so budget the supporting posts accordingly:
[X API pricing](https://docs.x.com/x-api/getting-started/pricing).

## Account-distribution protection built into the code

The following are system rules, not claimed platform “safe thresholds”:

1. **Official API only.** There is no Cookie, Selenium, Playwright, browser
   extension, native-app scripting, automated reply, comment, like, follow,
   repost, or trend endpoint.
2. **Approved manifest only.** Manual production requires a matching
   `confirm_content_id` and approval through the `social-production` GitHub
   Environment. The automatic queue reads only `approved: true` manifests.
   The manifest digest, approved code SHA, exact upstream run, workflow name,
   successful main-branch conclusion, artifact name, and video SHA-256 are all
   checked before a provider write.
3. **One item at a time.** GitHub concurrency and a single-item queue prevent
   bursts.
4. **Minimum interval.** The default is 20 hours per platform. GitHub Variable
   `SOCIAL_MIN_INTERVAL_HOURS` may be 4–168, but should stay at 20 through the
   canary phase.
5. **Duplicate guard.** Exact SHA-256 and a 64-bit SimHash reject identical or
   very-near-duplicate copy across prior receipts.
6. **Platform-specific copy.** LinkedIn and X text cannot be identical. X is
   capped at two hashtags and one cashtag; LinkedIn is capped at three hashtags.
   Automated mentions are rejected.
7. **Final links only.** Common URL shorteners and URLs containing credentials
   are rejected.
8. **YouTube declarations are explicit.** Child-directed status, altered or
   synthetic media status, subscriber notification, privacy, category and
   schedule cannot silently fall back to defaults.
9. **Fail closed before retry.** A receipt is committed as `reserved` before
   the first external write. Any interrupted or partial run pauses the queue.
   Actions reruns are rejected and the system never automatically retries an
   uncertain POST.
10. **Fresh target-account preflight.** Immediately before reservation,
    YouTube must match `YOUTUBE_CHANNEL_ID`, X must match `X_USER_ID`, and
    LinkedIn must pass token introspection and author-format validation. Only
    enabled platforms expose credentials to the publisher step.
11. **Visibility receipt.** YouTube processing and privacy are read back;
    LinkedIn requires a 201 plus the returned post URN; X requires a 201 plus
    the returned Post ID.

## GitHub workflows

### `social-publish-control.yml`

- Runs only on `ubuntu-latest`.
- Manual `validate` is the default and does not expose provider credentials.
- Manual `publish` requires `SOCIAL_PUBLISH_ENABLED=true`, a matching content
  ID, `main`, and the protected `social-production` Environment.
- The hourly queue remains dormant unless
  `SOCIAL_AUTO_PUBLISH_ENABLED=true`.
- The exact upstream Actions run ID and artifact name are used. “Latest” is
  never downloaded.
- Manual inputs cannot replace the artifact recorded in the approved manifest.
- Provider IDs are split from the public receipt, AES-256-GCM encrypted, and
  stored only as authenticated ciphertext. Plaintext locators exist only in
  the hosted runner. The encrypted artifact copy is a recovery fallback if the
  durable Git push fails.
- A failed or partial publication commits its sanitized receipt, sends an
  email, and pauses the queue without an automatic resend.
- An unresolved `reserved`, `partial`, or `failed` receipt blocks manual as
  well as automatic publication. Final commits stage only that content ID's
  public receipt and encrypted companion, so an unrelated receipt entering
  `main` concurrently is preserved.
- YouTube writes the validated `video_id` to the private locator immediately
  after upload and before processing/status polling. A later polling failure
  therefore remains exactly traceable without another upload.

### `social-credential-monitor.yml`

Runs daily at 09:27 Asia/Shanghai and performs only read-only checks:

- LinkedIn `introspectToken`: active state, client, scope and expiry;
- X OAuth 1.0a `GET /2/users/me`: credentials and expected identity;
- YouTube refresh-token exchange plus `channels.list(mine=true)`;
- optional Buffer account/channel connection checks.

It sends a deduplicated Brevo email for missing, revoked, invalid, insufficient,
disconnected, or 14-day/3-day expiry states. The email names only the provider
slot and corrective action; it does not contain tokens, account/channel IDs, or
provider response bodies.

### `social-reach-monitor.yml`

The reach monitor decrypts successful provider locators only inside its hosted
runner and performs bounded 1-hour `[1,24)` and 24-hour `[24,48)` checks. At 1
hour it records a baseline. At 24 hours, a confirmed zero metric sends an email
and commits `social_publish/PAUSED.json`, which blocks both manual and automatic
publication until it is inspected and removed. YouTube and X can be checked directly;
LinkedIn is reported as unsupported unless the app has the required post
analytics permission. Unsupported analytics must never be interpreted as zero.

## Manifest contract

Copy the example into `social_publish/outbox/`, change `content_id`, select the
exact upstream artifact, write platform-specific copy, and set `approved: true`
only after editorial review.

Important fields:

- `source.run_id` and `source.artifact_name` identify one retained GitHub
  Actions artifact. They must be set together.
- `media_path` is relative to that artifact and may not escape it.
- `media_sha256` is the lowercase SHA-256 of the exact video bytes and prevents
  an artifact replacement from inheriting an earlier approval.
- `{{YOUTUBE_URL}}` is resolved only after YouTube returns a receipt.
- `{{SOURCE_URL}}` resolves to the final HTTPS `source_url`.
- Disabled platform objects remain available for one-platform canaries.

See [social-publishing-manifest.example.json](social-publishing-manifest.example.json).

## One-time GitHub configuration

### Environment

Create two Environments:

1. `social-production`: add a required reviewer during the canary phase and
   allow deployment only from `main`.
2. `social-monitor`: no reviewer, allow deployment only from `main`. Credential
   and reach checks remain automatic, while provider secrets stay unavailable
   to workflows dispatched from another branch.

Provider credentials used by both publishing and monitoring must be added to
both Environments. Keep them out of repository-level Secrets.

### Secrets

```text
YOUTUBE_CLIENT_ID
YOUTUBE_CLIENT_SECRET
YOUTUBE_REFRESH_TOKEN
YOUTUBE_CHANNEL_ID

LINKEDIN_CLIENT_ID
LINKEDIN_CLIENT_SECRET
LINKEDIN_ACCESS_TOKEN
LINKEDIN_AUTHOR_URN

X_API_KEY
X_API_SECRET
X_ACCESS_TOKEN
X_ACCESS_TOKEN_SECRET
X_USER_ID

SOCIAL_RECEIPT_KEY_B64

OPS_ALERT_SIGNING_KEY
PORTAL_WORKER_URL
PORTAL_PRIVATE_CONFIG_B64
```

Generate `SOCIAL_RECEIPT_KEY_B64` once as 32 random bytes encoded with canonical
Base64, then put the same value in both Environments. Rotating it requires
re-encrypting existing locator receipts.

Use Secrets, not repository files, for account IDs/URNs as well as tokens. The
account identifiers are not needed in logs or artifacts.

### Variables

```text
SOCIAL_CREDENTIAL_MONITOR_ENABLED=true
SOCIAL_REACH_MONITOR_ENABLED=true
SOCIAL_PUBLISH_ENABLED=false
SOCIAL_AUTO_PUBLISH_ENABLED=false
SOCIAL_MIN_INTERVAL_HOURS=20
SOCIAL_REACH_MAX_RECEIPTS=50
SOCIAL_REACH_PAUSE_AFTER_CONSECUTIVE=2
SOCIAL_ALLOWED_SOURCE_WORKFLOWS=Daily bilingual podcast videos

LINKEDIN_API_VERSION=202608
LINKEDIN_REQUIRED_SCOPES=w_member_social
LINKEDIN_CREDENTIAL_EXPIRES_AT=YYYY-MM-DD
LINKEDIN_CREDENTIAL_VERSION=1

X_OAUTH1_SCOPES=read write
X_CREDENTIAL_VERSION=1

YOUTUBE_REQUIRED_SCOPES=https://www.googleapis.com/auth/youtube.upload
YOUTUBE_CREDENTIAL_VERSION=1
```

`X_OAUTH1_SCOPES` is a required declaration from the X Developer App settings;
the read-only identity probe cannot infer write permission. YouTube write scope
is checked from the OAuth refresh response before the credential is considered
healthy.

`*_CREDENTIAL_EXPIRES_AT` is an advance reminder, not the source of truth.
Actual 401/403, inactive, scope, identity and refresh responses always take
precedence. Increment the non-sensitive credential version when replacing a
credential so a new alert can bypass the old dedupe fingerprint.

### Provider setup

1. **YouTube:** put the OAuth consent app into production, request the narrow
   `youtube.upload` scope, generate one offline refresh token, reuse it, and
   complete the separate YouTube API audit. Google documents that an External
   app left in Testing issues a refresh token that expires after seven days:
   [Google OAuth token expiration](https://developers.google.com/identity/protocols/oauth2#expiration).
2. **LinkedIn:** add `Share on LinkedIn` for a personal profile, or complete the
   Page/Community Management path for an organization. Access tokens normally
   last 60 days. Programmatic one-year refresh tokens are available only to
   approved Marketing Developer Platform partners:
   [LinkedIn refresh tokens](https://learn.microsoft.com/en-us/linkedin/shared/authentication/programmatic-refresh-tokens).
3. **X:** create a Developer App, set it to read/write, generate a fresh OAuth
   1.0a token pair after changing permissions, fund pay-per-use credits, and do
   not enable automated replies or engagement.

## Canary acceptance

Keep `SOCIAL_AUTO_PUBLISH_ENABLED=false` for at least three individually
approved posts per enabled platform:

1. preserve the account's normal editorial cadence and publishing window;
2. start with one platform enabled per manifest, then test the full sequence;
3. confirm YouTube is not unexpectedly private and completes processing;
4. confirm LinkedIn appears in `MAIN_FEED` and X has a public Post receipt;
5. compare 1-hour and 24-hour reach, YouTube click-through/watch time, and
   LinkedIn/X impressions against a similar manual-post baseline;
6. investigate any zero metric before another automatic item is allowed;
7. only then set `SOCIAL_AUTO_PUBLISH_ENABLED=true`.

The baseline is the account's own comparable manual history. No universal view
count or posting frequency is represented here as a platform-approved line.

To resume after a confirmed 24-hour zero, inspect the provider page and the
sanitized GitHub report, resolve the cause, then remove
`social_publish/PAUSED.json` in a reviewed commit. Do not rerun the original
publish Action.

An uncertain publish receipt needs a separate reviewed resolution before any
new manual or automatic item can reserve a slot:

- If no provider write occurred, edit that public receipt to
  `state: resolved_not_published` and add
  `resolution.decision: confirmed_no_provider_write`, `reviewed_by`, and an
  ISO `reviewed_at`. Keep the encrypted companion and Git history.
- If one or more providers did publish, keep only sanitized platform states,
  set the receipt to `published`, and retain the actual provider IDs only in
  the encrypted companion. This also activates the cadence and duplicate
  guards for the confirmed platform(s).
- Never delete the receipt or rerun the original Action as a way to unlock the
  queue.

## Verification

```text
python3 -B scripts/test_social_publish_control.py
python3 -B scripts/test_social_publish_youtube.py
python3 -B scripts/test_preflight_social_publish.py
python3 -B scripts/test_commit_social_receipt.py
python3 -B scripts/test_check_social_credentials.py
python3 -B scripts/test_check_social_reach.py
node --test scripts/test_social_receipt_crypto.mjs
python3 -B scripts/test_social_publish_workflows.py
python3 -B scripts/test_send_portal_ops_alert.py
python3 -B scripts/check_public_identity.py
git diff --check
```
