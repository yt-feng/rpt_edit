# DeepSeek usage accounting

The Python request wrapper now records provider-reported token counts for each
physical HTTP attempt. It does not require another API key. Existing stage keys
remain useful for comparing these observations against the provider dashboard.

## What is recorded

Each immutable JSON event contains the workflow, job, run ID, run attempt,
configured stage, source-code operation/call site, requested model after model
normalization, HTTP/retry/model-switch/key-ordinal counters, elapsed time, status,
and the provider's input/output/cache-hit/cache-miss/total token counters. It also
records `thinking_mode` (`enabled`, `disabled`, or `unknown`) and the optional
`usage.completion_tokens_details.reasoning_tokens` counter. Reasoning is a subset
of output tokens: it is shown separately for attribution and never added again to
output/total tokens or estimated cost. Absent reasoning counters remain unknown.

The shared wrapper explicitly disables thinking for ordinary editing calls. An
explicit thinking override (including the legacy reasoner alias) is preserved and
identified in the ledger, allowing its usage to be compared separately. This is a
statement of current request behavior, not proof of any historical savings.

The operation comes from a source-code function and line number, or an explicit
static operation name. **Report labels/titles, prompts, generated text, URLs,
response IDs, headers, API keys/key fingerprints, and original errors are never
recorded.** The ledger is suitable for public Actions artifacts. The existing
content and operational log artifacts have separate handling and are not made
public by this feature.

Only numeric provider usage is counted. An HTTP or transport failure with no
usage is marked missing; it is not assumed to have consumed zero billed tokens.
Every real rerun remains a new set of attempts. Model fallback and key failover
are visible. Key fallback shares a logical request ID, without storing key names
or values.

## Workflow integration

Set this workflow/job environment variable outside the checkout so that generated
usage does not enter content commits and survives a checkout reset:

```yaml
env:
  DEEPSEEK_USAGE_DIR: ${{ github.workspace }}/../deepseek-usage
```

Set `DEEPSEEK_USAGE_STAGE` on each paid step to a stable stage such as `selection`,
`report-notes`, `report-article`, `finalize`, or `market-views`. Stages can contain many distinct
source-code operations; splitting those operations does not require new keys.
Each GitHub-hosted job has an independent ledger directory. A matrix job must
include its matrix identity in the upload artifact name.

At job end, including failures:

```sh
python scripts/summarize_deepseek_usage.py \
  --input-dir "$DEEPSEEK_USAGE_DIR" \
  --output "$DEEPSEEK_USAGE_DIR/summary.json" \
  --markdown "$DEEPSEEK_USAGE_DIR/summary.md" --github-summary
```

Upload the directory with an artifact name beginning `deepseek-usage-`, containing
run ID and run attempt (plus shard ID for matrices). The current workflows retain
these artifacts for 30 days. If usage cannot be persisted, accounting emits a
content-free warning and does not retry a paid request solely for logging.

## Daily breakdown and billing comparison

`deepseek-usage-daily.yml` runs daily at 10:20 Asia/Shanghai and summarizes the
previous local calendar day. It can also be dispatched with a specific date.
The collector uses `actions: read` to download only unexpired `deepseek-usage-*`
artifacts. It considers uploads on the requested day and the following day, then
filters individual events by their actual timestamp; an upload date is not the
token-consumption date. Download/authentication failures stop the collection
instead of producing a successful empty bill.

Only artifacts already uploaded at collection time are visible. In-flight jobs,
failed/cancelled uploads, expired/deleted artifacts, and uploads outside that
two-day window are not recovered automatically. Re-dispatch the date after late
jobs finish to include available late arrivals. The collection manifest reports
artifact/event counts and this coverage limit. A zero count means no matching
observations were found, not zero account spend. Neither the collector nor extra
API keys can reconstruct operation-level history from before instrumentation.

Download relevant `deepseek-usage-*` artifacts, keeping all original event files,
and aggregate them recursively:

```sh
python scripts/summarize_deepseek_usage.py \
  --input-dir downloaded-usage \
  --date 2026-09-20 --timezone Asia/Shanghai \
  --output usage-day.json --markdown usage-day.md --github-summary
```

`--input-dir` may be repeated. The summary groups by local calendar date,
workflow/job, run/attempt, stage, operation, model and thinking mode. UTC event times are
converted to the requested timezone before filtering. Re-downloaded/copy artifacts
are deduplicated by event ID; separately billed reruns are not deduplicated.
Malformed records and conflicting duplicates are explicitly counted. Unique
atomic event files avoid concurrent append corruption and lost counter updates.

No prices are hard-coded. Optional `--prices-json` accepts a JSON object keyed by
model, each with `input_cache_hit`, `input_cache_miss`, and `output` rates in CNY
per million tokens. Populate these from the applicable provider rate sheet. A
cost estimate is calculated only for responses containing every required token
counter and a configured rate; unpriced responses are counted separately. The
output labels this as an estimate, never the provider invoice. By default the
cost is unknown, not zero. The scheduled daily workflow does not supply a price
file, so its default output is token breakdown rather than a currency estimate.
With rates configured, the estimate is only the subtotal of priceable responses;
always read it alongside missing-usage and unpriced-response counts. It is not a
billing cap or a reconstruction of unobserved charges.

## Coverage and current key map

- `DEEPSEEK_SELECTION_API_KEY`: macro report selection.
- `DEEPSEEK_REPORT_NOTES_API_KEY`: report/WeChat drafting. Article-style report
  jobs use stage `report-article`; operations separate body editing, title
  refinement, and title repair. A job with "translated" in its name may still
  contain institution/consulting editorial work, including mixed Dropbox batches.
- `DEEPSEEK_FINALIZE_API_KEY`: remaining finalization and content rewrites.
- `DEEPSEEK_MARKET_VIEWS_API_KEY`: daily Market Views synthesis.
- `DEEPSEEK_REPORT_TRANSLATION_API_KEY`: no longer used by scheduled pure
  translation; these steps use pinned Hy-MT2 CPU inference on Actions. Remaining editorial calls in report
  PDF jobs use the report-notes key, including the manual PDF test workflow.
- `DEEPSEEK_CATALOG_TITLES_API_KEY`: no longer needed by scheduled title
  translation after migration to offline models.
- `DEEPSEEK_PODCAST_API_KEY`: unused by disabled automatic podcast production.
- `DEEPSEEK_PORTAL_RUNTIME_API_KEY`: separately deployed Worker use; outside this
  Python/Actions ledger.

Shared Python-wrapper coverage includes selection, report drafting, finalization,
content rewriting, Market Views, the retained Zhihu generator, and any explicit legacy paid locale
translation paths using the wrapper. Offline translation makes no paid API calls
and contributes no DeepSeek tokens.

**This is an observation ledger, not an account-wide bill.** Existing Worker
runtime calls, other repositories, historical calls before instrumentation, and
old manually launched test scripts that bypass the wrapper are outside it.
Worker locale-detail translation has its own persistent cache and daily limits;
its provider usage belongs to the portal-runtime key and must be compared
separately. A cache-missing POST can still call DeepSeek when the Worker key is
configured; GET polling does not call the provider. The current defaults are
100 requests and 100,000 source characters per UTC day, configurable separately
from the Actions ledger. Offline batch migration does not disable this path.
Other services such as source PDF parsing are also outside DeepSeek accounting.
A run without recorded events does not establish that the whole
account had no consumption. Historical screenshots cannot be retroactively split
into operations that were not instrumented at the time.

## Verification

```sh
PYTHONPATH=scripts python3 -m unittest \
  scripts.test_deepseek_http scripts.test_deepseek_usage \
  scripts.test_collect_deepseek_usage_artifacts
```

The accounting tests cover content/key exclusion, transport failures and HTTP
retries, model fallback/key failover, copied-artifact deduplication versus real
reruns, concurrent immutable writes, timezone boundaries, malformed counters,
explicit cost estimates, reasoning as an output subset, and a logging failure that must never repeat a paid call.
