# Private report generation checkpoints

The sharded report workflow restores paid drafting/finalization outputs before
checking whether a shard is complete. A new GitHub-hosted runner can reuse the
previous runner's completed work instead of depending on generated files being
committed to the public repository.

Checkpoints live under the existing private R2 bucket at
`_workflow-cache/report-generation/v1/<date>/shard_<index>/<identity>.tar.gz`.
They are separate from the short-lived, run-specific handoff that downstream
publication jobs delete after completion. Text, images, prompts and generation
memos remain private. The handoff archive policy excludes original PDFs, ZIPs,
raw MinerU folders and audio/video.

The input identity includes the actual SHA-256 of each selected PDF, its copied
filename, shard membership, relevant generation options, active code and prompt
files. Source hashes are calculated when selected PDFs are copied into the
producer artifact. Missing hashes fail closed. Same filenames with changed PDF
bytes, different prompts/models/lengths, or different shard membership cannot
silently restore old text. Both the checkpoint identity and the existing source
manifest/complete-shard check must match before the whole shard is skipped.
The source check follows the batch runner's actual lexical filename ordering,
including selections with more than 99 reports.

The workflow saves checkpoints with `always()` after a successful restore attempt,
including partial work after a generation failure. Finished report articles and
successful Zhihu/content-guard memos can then be reused individually; incomplete
report markers are removed during restoration so they do not satisfy the batch
runner's file-presence skip condition. A failed or missing finalization memo does
not mark the whole checkpoint complete. `force_reprocess=true` explicitly bypasses
restoration and regenerates the requested shard.

A missing R2 object means a cold start. Authentication, transport, checksum or
identity failures stop the job instead of silently repeating paid generation.
Restored complete shards are uploaded again to the current run's private handoff,
so the existing downstream jobs receive their expected run-specific inputs.

Validation uses real local archive round trips between separate simulated runner
directories, plus content-change, configuration-change, partial failure, and
storage failure checks:

```sh
PYTHONPATH=scripts python3 -m unittest \
  scripts.test_private_generation_checkpoint \
  scripts.test_check_completed_shard \
  scripts.test_generation_cost_controls
```
