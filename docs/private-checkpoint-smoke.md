# Private checkpoint storage smoke

In **Portal offline translation preflight**, manually dispatch with
`verify_private_checkpoint=true` to add the isolated storage smoke job. The input
defaults to false. Pull requests only run local tests and the existing public
translation samples; they never run the storage job or receive its credentials.

The smoke uses the same existing R2 credentials as production, but only built-in
public synthetic fixtures. It does not read real reports, call a paid model,
generate a real article, or contact WeChat. No local translation model is needed
by this job. The separate model preflight job keeps its existing behavior.

The three phases run in separate Python processes:

1. Save synthetic generation output and translation/editorial memo checkpoints.
2. Restore both into fresh empty temporary directories, compare every included
   file byte-for-byte, and run the production completed-shard reuse gate. Republish
   the restored generation as a current-run handoff, then restore and verify it.
   Raw PDFs, media and MinerU raw files are deliberately excluded and checked absent.
3. Always delete and verify absence of exactly the three dedicated test objects.
   There is no prefix listing or deletion. Keys are constructed only from numeric
   GitHub run ID and run attempt under `_workflow-smoke/private-checkpoints/v1`.

The job proves real private storage authorization and persistence across separate
processes with empty local directories. It does not itself schedule a second
physical runner. Every phase rebuilds expectations from public source fixtures;
no local cache or artifact transfers the payload between save and verify.

Public diagnostics contain only fixed phase/status fields, counts, and the hash
of synthetic expected files. Storage keys, bucket names, endpoints, report text,
credentials and raw SDK errors are never included in logs or uploaded artifacts.
A failed restore/checksum/delete produces a failed phase, never a false success.
An interrupted save is followed by the unconditional cleanup step; a hard runner
termination can prevent any `always()` step from executing, so inspect cleanup
status when judging a run. Re-running cleanup for the same run ID/attempt is safe.

The job is limited to 10 minutes with 2/3/2-minute save/verify/cleanup step limits
and two SDK attempts. Unit tests use in-memory object storage while executing
the real checkpoint and archive implementations; they do not need credentials.
