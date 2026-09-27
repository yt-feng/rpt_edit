# September 26 candidate recurrence investigation

## Incident evidence

`36216968278` ran against candidate PR #182 at `044d268a`, not production main.
Its fixed generation was
`2b9081823e32528f402348f968d0771468dab06ea116b1a293fdf90a6621718b`.
Of 33 locale jobs, 21 completed and 12 failed. All failed jobs saved their
checkpoints and incomplete candidates successfully; this was not an R2 outage.

- German and Kazakh set `budget_exhausted=true` after 23.32 and 25.55 minutes,
  despite a 240-minute budget. The model's 240-second HTTP timeout escaped as
  Python `TimeoutError`; the builder treated every such exception as the whole
  run deadline. Fault injection reproduces that premature stop.
- Khmer, Burmese, Persian, Gujarati, Hebrew, Marathi, Bengali, Tamil, Mongolian
  and Cantonese reported only `offline-runtime`. Those old logs do not identify
  the underlying cause. Exact stored-generation replay is required before
  attributing all ten to transport failures.
- Translation consumed 50.31 aggregate hours. Two concurrent workers took the
  full matrix past a 24-hour cycle. This queueing defect remained even if every
  individual locale stayed inside its four-hour budget.

The earlier short canary covered four languages and two sentences. Those checks
and synthetic happy paths did not exercise a timed-out request inside a live
four-hour budget, a complete 33-language daily matrix, or the original failed
source units.

## Recovery contract

`TranslationBudgetExceeded` now means only an elapsed monotonic run deadline.
Transient model requests get at most three attempts with 240/480/720-second
allowances; each allowance is clipped to the remaining run budget. HTTP client
errors that cannot recover are not retried. Exhausted requests remain failed
units with specific bounded diagnostic codes, not content fallbacks.

All existing quantity, protected-placeholder, Markdown, target-script and
page-completeness validation remains in place. No rejected model text enters a
translation cache. A request that recovers still has to pass those gates.

The normal matrix allows up to eight workers: five waves at the 270-minute job
cap fit within 22.5 hours of execution. Runner queueing and account availability
can still add wall-clock time. The global candidate lock and production release
lock are unchanged.

`recovery-test` reads an exact stored daily generation and existing checkpoints,
including an older generation solely for diagnosis. It uses a separate
concurrency group and does not upload checkpoints, upload candidates, advance
completion receipts, or publish pages. Ordinary candidate collection and explicit
candidate resumes still accept only the current Shanghai calendar day.

## Validation

- Failure injection fails on the preceding implementation and passes after the
  fix. It covers transient recovery, repeated failure, real deadline exhaustion,
  per-attempt remaining budget, exact checkpoint reuse, next-day reuse without
  old-page selection, and quantity rejection after a recovered request.
- 231 Python tests and 65 edge-static-host Node tests passed locally.
- Both workflow YAML files and their 16 shell blocks parse; public identity scan
  passed on 5,917 files.
- Original twelve-locale read-only replay: Actions run `36335431911`. Its final outcomes
  must be reviewed before claiming all original locale failures are recovered.

## Unrelated cancelled refreshes

`36281666805` and `36283908998` had no jobs and were replaced by the pending newer
`36283996092` under the production concurrency group. Both cancelled heads are
ancestors of replacement head `786ae0ca`. That cumulative release included blog,
catalog and search changes, passed object verification, and passed live
acceptance with 24 requests covering 18 routes and six assets. Later scheduled
runs `36301098093` and `36327080434` also succeeded. These cancellations did not
leave the corresponding committed inputs unreleased.
