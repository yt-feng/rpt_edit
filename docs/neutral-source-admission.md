# Neutral source admission

A queued catalog release keeps its original GitHub commit. If a UI hotfix is
published while it waits, the old catalog job must not replace that UI with old
code. The existing live-release comparison only detects a change during a build;
it does not detect a newer UI that was already live when an old job began.

`source_admission` runs under the existing `portal-production-release` lock before
`prepare_release`, private configuration, or cloud writes. It resolves `main`
once, fetches that exact Git object for comparison, and compares raw tracked code
projections with the frozen `GITHUB_SHA`. It never switches the checkout or changes
the candidate commit used by review. Main changes after admission do not abort a
long-running build; the publication lock prevents another release from cutting
over during that build.

Only this admission checkout retains its `contents: read` GitHub token for the
exact-object fetch, so the comparison also works for a private origin. Checkout
cleans up the ephemeral credential configuration when the job ends. The helper
never prints authentication output, changes the remote, or pushes Git objects.

The versioned `neutral-code-v1` projection includes the Neutral workflow, UI
templates and static assets, locale assets, Edge Worker source, executable build
helpers (including indirect helpers), dependency constraints, and build policy
and private-asset source files. Test helpers, repository documentation, reports,
catalogs, blog archives, generated locale checkpoints and `site_src/data` are
excluded. All executable scripts are deliberately included, so an indirect helper
change is covered without maintaining an incomplete import list. Their contents
are never included in admission artifacts; only Git object hashes and code paths
are compared. Private deployment values are not loaded by this job.

Admission has three outcomes:

- `ready`: the code projections match. Catalog-only commits can differ; normal
  preparation and existing acceptance checks continue.
- `superseded`: the projections differ. The workflow finishes successfully with
  preparation, reviews, cutover and locale follow-up skipped. **This means no
  publication occurred.** The job summary says replay is required.
- A source lookup, incomplete tree, invalid input, or comparison error fails the
  job. It never becomes a successful skip and cannot admit publication.

The seven-day `neutral-source-admission-<run>-<attempt>` artifact contains
`neutral-source-admission.json`, including the original run/attempt/SHA, the main
SHA observed at admission, both fingerprints, changed code paths, and a replay
request. For manual runs all ten original business input values are retained;
`original_manual_inputs` also preserves which fields were actually supplied.
Automatic runs are explicitly labeled `reconstructed_automatic_defaults` and
replay `migrate/incremental/catalog`. No private event payload is exported.

To replay, download that exact artifact and inspect its `state`, `source`, and
`replay` fields. Dispatch `replay.workflow` on `replay.ref` (`main`) with the exact
`replay.inputs` object. With GitHub CLI and `jq` this is:

```sh
jq -e '.state == "superseded" and .replay_required == true' neutral-source-admission.json
jq '.replay.inputs' neutral-source-admission.json > neutral-replay-inputs.json
gh workflow run neutral-edge-cutover.yml --ref main --json < neutral-replay-inputs.json
```

Check the queue before retrying a dispatch whose outcome is unknown. This patch
does not automatically dispatch or coalesce requests: exact handoff replay needs
its own correlated, deduplicated protocol. Old workflow revisions already queued
before this gate was introduced still need the one-time reviewed queue
consolidation. The gate is Neutral-only; UI hotfix and API Worker deployment are
separate workflows.

Validation: `python3 -B scripts/test_neutral_edge_cutover_workflow.py` includes the
source-admission fixtures and downstream gating checks. They cover data-only
changes, UI/build/Edge changes, missing main, exact manual handoffs, reconstructed
automatic defaults, sanitized failures and the absence of cloud writes/dispatch.
