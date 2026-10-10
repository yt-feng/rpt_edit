# Extended locale consumer queue admission

The source workflow and translation consumer have separate concurrency contracts.
The consumer serializes eligible work in `extended-locales-r2-pipeline`, with
`cancel-in-progress: false` and at most two locale workers. GitHub evaluates this
workflow-level concurrency before job conditions and retains only one pending
run in a group. A new completion event can replace pending work even when all
of its own jobs will be skipped.

On 2026-10-10, manual recovery run `38062743991` was cancelled when skipped source
admission `38063336945` created no-op consumer `38063339570`. This did not interrupt
the running translation batch, but displaced the useful pending successor.

Rejected source completions now use a run-and-attempt-specific ineligible group.
Eligibility is the same as the source job: upstream success, repository default
branch and the same head repository. Eligible automatic and manual candidate
work still share the existing single-writer group; round-trip, publication-check
and recovery-test keep their established isolated groups. Job conditions remain
unchanged, so this change grants no new source admission or publication authority.

Tests evaluate the actual checked-in expressions across upstream conclusions,
branches and repositories, replay the observed pending-replacement sequence,
and retain all manual operation groups. Cloud checks and a useful queued successor
are separate acceptance steps. This does not claim that all 33 locale outputs are
complete or published.
