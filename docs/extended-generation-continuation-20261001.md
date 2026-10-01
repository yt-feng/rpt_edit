# Continue a started daily generation across calendar days

Run `36801745121` saved Khmer's real checkpoint and 23 of its 24 candidate
pages, then correctly failed with exit 75 after the unchanged four-hour CPU
budget. The old source selector only searched the current Shanghai calendar
day. It did not maintain a pending-generation queue, so later refreshes could
select a new day while leaving this exact generation unfinished. In addition,
`publication-resume` was excluded from the publication handoff, and the daily
reviewer required the new source job's date rather than proof of the original
source job. These are separate links in the same continuation path.

## Durable continuation contract

The source job registers its immutable source SHA, original daily date,
producer run/attempt/commit and locale inventory before launching the matrix.
Each locale maintains a separate bounded queue. Matrix workers cannot overwrite
another locale's progress. The existing global `extended-locales-r2-pipeline`
concurrency group remains unchanged, with cancellation disabled and two workers.

A subsequent normal source job first selects the oldest pending **one source
generation**, validates its exact stored checkpoint and budget-exhausted
incomplete manifest, and claims only that generation's unfinished locales.
It restores the original corpus bytes before any collection of today's pages.
The locale job restores the claimed immutable checkpoint SHA, not a mutable
`latest` pointer. Already complete locales do not enter inference again.

A locale may continue at most three times, each within the existing 14,400-second
budget. Each result must retain prior resolved unit identities and complete-page
coverage and must add resolved units or complete pages unless it finishes.
No progress, an unknown/interrupted outcome, a non-budget failure, corrupt proof,
or exhausted continuation count stops with a diagnostic. Exit 75 remains a
failed/incomplete job, never a successful candidate. Retrying only a locale job
without a new source-job claim stops before model setup.

There are at most 64 outstanding generations per locale. A full queue rejects
new registration; it does not evict history. Complete output remains queued
until its exact `(locale, generation, candidate)` appears in the verified active
publication ledger. Original source and immutable attempt receipts remain after
queue acknowledgement. Partial candidate IDs hash page inventories, so distinct
attempts with the same page set additionally retain their exact manifest bytes
under a content-addressed private key.

## Publication and original-date proof

Both normal daily refresh and `publication-resume` can hand complete registered
candidates to the existing protected release workflow. An old-day completed
candidate is selected from the registered queue, not by listing historical
folders. One handoff always contains a single corpus generation. Current enabled
and already-live locale checks, complete-candidate verification, source/candidate
hashes, model identity, source-fallback accounting, exact release tree approval,
required reviewer, release acceptance and rollback checks remain in force.

For a registered handoff the reviewer independently reads the immutable origin
and checkpoint objects, then verifies the original GitHub run/attempt/commit and
successful original `source` job on that Shanghai date. The current producer
still needs successful `source` and `publication_handoff` jobs. A historical
handoff without this proof continues to fail the old date check.

## Existing generation from before queue registration

Do not cancel the original matrix or run another writer alongside it. First use
`portal-extended-continuation-inspect.yml` with exact generation, locale,
checkpoint SHA and candidate ID. This independent read-only job neither acquires
nor cancels the translation lock. It does not list R2 objects or run a model.
Only `inspection.json` (hashes, counts, next-unit hash/length and remaining public
URLs) is uploaded. The source, checkpoint, manifest, body and translations remain
on temporary runner disk and in their existing private R2 objects, never in a
public-repository artifact.

After the original run finishes and the global group is available, dispatch
`portal-extended-locales-r2.yml` with `operation=publication-resume`, its original
`source_generation`, and only the explicitly proved locale(s). For pre-ledger
work supply `continuation_evidence` as a JSON object:

```json
{
  "producer": {"run_id": "123", "attempt": "1", "sha": "<40-hex-original-commit>"},
  "locales": {
    "km": {
      "checkpoint_sha256": "<64-hex-exact-checkpoint>",
      "candidate_id": "<64-hex-exact-incomplete-candidate>",
      "manifest_sha256": "<64-hex-manifest-from-inspection>"
    }
  }
}
```

Adoption verifies every selected immutable object and the completed original
GitHub run/source/locale jobs before writing any queue state. It accepts only
real checkpointed budget-incomplete work. It cannot reset an already registered
generation or infer readiness of unlisted locales. Subsequent continuations omit
the adoption evidence and retain the accumulated attempt count.

The local regressions use fake R2 and a fake translator; they prove continuation,
identity, handoff and stop behavior without model/network calls. Successful
inspection, recovery, protected cutover and live acceptance are separate
production evidence and are not implied by those tests.
