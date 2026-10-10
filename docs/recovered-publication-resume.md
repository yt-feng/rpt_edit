# Resume a recovered article publication after release failure

`Recover report article delivery` has separate `generate`, `deliver` and `publish`
jobs. The delivery job saves a request binding the pushed Blog archive commit and
each article's canonical identity and complete body/reference digest. The publish
job saves its watcher state even when the child Neutral release fails or times
out. Rerunning only this failed job restores those exact request/state artifacts;
it does not run article generation or WeChat upload again.

The watcher records a failed release before looking once for a later eligible
successor. Every successor must use the existing Neutral release workflow, the
same repository and main branch, an accepted dispatch/schedule/workflow-run event,
and a commit containing the exact requested archive. A completed successful
successor may have the same head as the failure, covering an external transient
failure that was repaired without changing code. An unfinished successor must
have a different head; an unfinished retry of the same failed head is not enough.
Known failed, skipped and cancelled candidates are excluded. A completed success
is preferred to an earlier unfinished candidate, then the smallest later run ID.

This lookup never dispatches another release. With no eligible successor, the
original failure remains recorded and the publish job fails. A later publish-only
rerun may find a now-completed or newly repaired successor from the same saved
state. The original failed Actions run retains its failed conclusion. Each chosen
successor is read again by exact run ID before use; the run inventory is bounded
to 100 and the existing 350-minute watch budget remains in force. A replacement
that fails is examined once and cannot be revisited by that watch's history.

A green release alone cannot complete the request. Every requested live Blog
page must still pass canonical and full body/reference identity checks. A changed
or missing page stays unaccepted. This preserves the publication receipt consumed
by the separate historical locale-admission path; accepted WeChat drafts are not
repeated merely to obtain a new release receipt.
If the original failed release succeeds on a rerun under the same run ID, the
existing state follows it directly. Every accepted completion removes the stale
failure conclusion field while retaining the exact run-ID history, including a
failed → cancelled successor → accepted successor sequence.

Cancellation keeps the existing exact-archive successor behavior for replacement
of GitHub's pending concurrency slot. Ambiguous initial dispatch acknowledgement
still requires its existing explicit confirmation path and never auto-dispatches
again. Generation-quality failures and unknown pending model requests are outside
this publication-only recovery mechanism.
