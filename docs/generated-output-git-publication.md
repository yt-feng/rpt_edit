# Publish only a producer's generated Git delta

`commit_output_dir.sh` previously fetched main, moved its index with
`reset --mixed`, then staged the entire stale output directory. In a pinned
checkout this could delete a concurrently added Blog record and overwrite a
concurrent edit even though the producer never changed those paths.

The helper now freezes the requested output's final working-tree state in a
temporary index before fetching. Its immutable intent is merged against every
fresh main tree using an explicit base and a separate temporary index and empty
scratch worktree. Only changed merge files are materialized; there is no second
repository checkout. A rejected push retries that same intent. A final readback
also recognizes a push accepted before its acknowledgement was lost, avoiding a
second commit for an already applied intent.

The producer's HEAD, real index, files and Git identity configuration stay
unchanged. A private `refs/codex-output-producers/*` baseline advances only after
push acknowledgement or independent readback. It is scoped to code HEAD,
repository, Actions run, attempt and job. Its tree contains only this producer's
acknowledged changes, never remote-only additions. This lets one job update a
file from v0 to v1 and then v2, including a later wider directory output, without
adopting another producer's records as local deletion targets. A different run or
attempt cannot reuse that baseline. Non-Actions callers can supply a unique
`OUTPUT_PRODUCER_ID` to opt into a shared invocation baseline; otherwise each
call uses its checked-out HEAD as the base.

Explicit tracked deletions and renames remain part of the producer intent.
Nonoverlapping edits to the same file merge; actual conflicts stop without a
push. After merging, every change relative to fresh main must remain inside the
requested directory or exact file. A remote rename cannot redirect a producer's
edit outside that boundary. Optional callers retain exit 0 with a diagnostic
after an unresolved handoff; `require_push_success=true` fails that handoff.
Invalid configuration and oversized blobs still fail immediately. Both the
frozen intent and the merged result are checked against the GitHub size limit.
Ignored PDFs require the existing explicit opt-in; an exact PDF request cannot
include other PDFs or ignored synthesis inputs.

The portable implementation uses Git's existing `read-tree`, `merge-recursive`,
`write-tree`, `commit-tree` and `update-ref` plumbing, including Git 2.34 on the
deployed runner. It does not require the newer `merge-tree --merge-base` option
and does not upgrade Git. The
[Git 2.34 merge implementation](https://github.com/git/git/blob/v2.34.1/builtin/merge-recursive.c)
accepts an explicit base; the
[environment variable documentation](https://github.com/git/git/blob/v2.34.1/Documentation/git.txt)
defines the independent index and worktree paths. Only a successful merge may
produce a commit; an unmerged index is never pushed.

`generated-output-git-regression.yml` runs temporary bare-Git race fixtures on
hosted runners and in a disposable Ubuntu 22.04 container with Git 2.34. Its
manual main-only compatibility job runs those same cold temporary fixtures on
the deployed runner with read-only repository permissions. Pull requests cannot
schedule that self-hosted job. These checks do not invoke source collection,
models, publishing APIs or media generation and do not push to the user repo.
