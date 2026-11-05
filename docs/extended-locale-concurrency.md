# Extended locale consumer queue admission

The source workflow and translation consumer have separate concurrency contracts.
The consumer serializes eligible work in `extended-locales-r2-pipeline`, with
`cancel-in-progress: false`, `queue: max` and at most two locale workers. GitHub
evaluates workflow-level concurrency before job conditions. The default
`queue: single` retains only one pending run and lets a later incoming request
replace it, even with cancellation of the running job disabled.

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

## Preserve exact recovery behind eligible automatic work

On 2026-11-05, Khmer recovery `41957250517` waited behind the healthy translation
matrix `41930937314`. Successful source admission `41963541042` then dispatched
eligible automatic consumer `41963884620`. GitHub cancelled the Khmer request
before any job started because both used the default single pending slot.
Filtering skipped upstream events could not prevent this eligible replacement.

Every workflow and job sharing the affected translation, per-locale,
source-admission or `portal-production-release` writer groups now opts into
`queue: max` and retains `cancel-in-progress: false`. This keeps serialization
and the existing two-worker matrix budget while preserving up to 100 pending
jobs/runs in each group. A full queue rejects additional incoming requests;
the queue is bounded. GitHub orders waiting entries by when they entered the
group, so workflow dispatch timestamps alone do not guarantee their order.

The syntax is documented for both workflow and job concurrency in the official
[GitHub concurrency guide](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency#example-queueing-multiple-pending-runs).
It cannot be combined with `cancel-in-progress: true`. The policy regression
enumerates every checked-in owner of these shared groups, including emergency
and manual release workflows, because an incoming owner with the default policy
could otherwise displace another workflow's exact pending request.
`actions-durable-queues-regression.yml` runs that policy check on pull requests
and main pushes touching any workflow, its generator or the policy test. It
parses checked-in YAML only; it does not invoke source collection or models.

Already cancelled requests must be dispatched again from fixed main after
checking the remote outcome. Observing both ordinary and exact recovery entries
in GitHub's concurrency group proves queue admission; the recovery's successful
candidate, handoff and accepted release remain separate completion evidence.
