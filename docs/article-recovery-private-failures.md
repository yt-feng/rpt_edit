# Recovered article failure evidence

The durable article generator continues independent reports after an individual
failure. Each failed report now preserves its original exception chain and any
producer status updates before the next report starts. The first batch failure
keeps that cause when the CLI eventually exits; `--private-diagnostics` remains
the only way to emit its traceback, and the recovery workflow already redirects
that output into the private generation log.

Each failure also writes a bounded, private snapshot at
`checkpoint/private-diagnostics/article-failures/ordinal_NNNN.json`. It contains
the ordinal, fixed exception types (unknown classes become `UnknownException`),
failure category, source/provenance/generation-contract hashes, status/progress
snapshot hashes, and at most 128 KiB of private traceback. This diagnostic text
must never be copied into public logs, issues, artifacts, WeChat or Blog content.
The normal CLI still emits only its fixed category and source ordinal.

The existing `save_generation` callback archives these records with the private
checkpoint. They are outside `checkpoint/articles`, its validation receipt, and
the article handoff used for delivery. A diagnostic record describes a past
failure; consumers must compare its status and progress hashes before treating
it as a diagnosis of the current checkpoint. A later successful article may
leave its earlier private evidence in place. Failure to save diagnostic evidence
or persist the resulting checkpoint stops further requests in that run.

This change does not alter the saved body/title response schema, request IDs,
generation contract, four-title-request bound, or provider call settings.
Completed responses remain reusable and unknown pending requests remain blocked.
It grants no additional title attempts and does not reclassify a rejected title
as publishable.

The read-only production inspection `38057091623` of run `38056186143` reported
43 of 44 articles bound, report 28 repaired, and report 38 with a completed body,
four completed title responses and no pending request. Report 38 still failed
the title gates, rather than failing with an ambiguous provider exception. This
patch preserves evidence for future exceptions; it does not fix that title.
Those counts do not authorize another request or establish
WeChat/Blog delivery; that batch still requires a separate, exact-source recovery
and full downstream acceptance. This diagnostic-only patch is covered by local
synthetic provider/storage tests and awaits cloud validation.
