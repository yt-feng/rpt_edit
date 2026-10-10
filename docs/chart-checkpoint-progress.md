# Chart checkpoint progress evidence

The chart checkpoint diagnostic reads one existing private checkpoint with no
model requests or object writes. Its completed job log exposes only status
counts and reusable counts for the entire checkpoint and the requested run's
exact last-attempt identity. The filtered artifact retains the existing detailed
diagnostic contract; private image content is never copied to either output.

The log projection permits progress inspection when artifact downloads are
unavailable. A failed read has no progress counts and is not empty success.
An active chart-index job's logs are not needed: run this separate read-only
diagnostic and inspect its completed job log.

These counts do not establish candidate coverage or publication. Cache hits may
retain an older last-attempt identity, and the checkpoint has no full candidate
manifest. Final acceptance still requires the indexing job's complete candidate
validation and successful searchable-index publication. Do not infer an ETA or
completion percentage from the diagnostic counts.
