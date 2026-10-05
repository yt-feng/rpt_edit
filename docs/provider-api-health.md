# Provider account monitoring

`provider-api-health.yml` checks the eight production DeepSeek secret slots hourly
at minute 27. It queries account balance only; no generation request is submitted.
The existing operations email endpoint and fixed recipient deliver alerts. Healthy
checks are silent; an unchanged issue is deduplicated for 24 hours. Changes from low
balance to exhaustion or another status produce a distinct alert.

Consumer repositories keep their own API keys. Their default-branch workflow runs
the pinned `scripts/provider_health_monitor.py` with `--key tikhub:TIKHUB_API_KEY`
and `--key deepseek:DEEPSEEK_API_KEY`, validates the report, and uploads the single
file `provider-health-report.json` as artifact `provider-health-report`. The report
contains only provider/secret-slot names, enumerated states, and run provenance.
It never contains exact balances, credentials, provider responses, or email addresses.

Set `PROVIDER_HEALTH_REPOSITORIES` to a comma-separated list of consumer repositories.
The existing `GH_DISPATCH_TOKEN` must have Actions read access there. The collector
requires the latest successful completed default-branch health workflow, matching
run/attempt/SHA, exact artifact layout, and report age under three hours. Missing,
failed, stale, and unreadable reports generate a monitor alert rather than a false
healthy result. Signed artifact redirects receive no GitHub authorization header.

Defaults are TikHub paid balance at most 5 USD and DeepSeek total balance at most
20 CNY or 5 USD (a funded currency above its threshold prevents a low-balance alert).
Set repository variables `PROVIDER_TIKHUB_LOW_BALANCE`, `PROVIDER_DEEPSEEK_LOW_CNY`,
and `PROVIDER_DEEPSEEK_LOW_USD` in the repository performing the probe to adjust.
TikHub free credits do not clear a zero paid-wallet warning because paid endpoints
may reject free credits. Key expiry within 14 days also triggers an alert.

HTTP 401, 402, 403, 429, server failure, and connection failure remain distinct.
Malformed or absent balances never become zero. Every stage-specific key is
checked separately; checking the repository's runtime secret does not establish
that a separately deployed Worker currently uses the same value.

Manual dispatch with `dry_run=true` validates probing and cross-repository access
without email. A normal dispatch sends only real actionable findings, with the same
deduplication as scheduled runs. Workflow summaries distinguish mail acceptance and
deduplication; they do not prove inbox delivery.
Manual `send_test_email=true` sends one explicitly labelled activation test, with
its own 24-hour dedupe key. It defaults to false, is ignored in dry runs, and cannot
be enabled by the schedule.

Contracts: [DeepSeek balance API](https://api-docs.deepseek.com/api/get-user-balance/)
and [TikHub user API](https://github.com/TikHub/TikHub-API-Java-SDK/blob/main/docs/TikHubUserApiApi.md).

Run `python3 -B scripts/test_provider_health_monitor.py` for offline regression tests.
