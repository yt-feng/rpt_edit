# Extended locales R2 progress

This checkpoint is maintained alongside the implementation. It records code and
verification state only; generated source, translations, checkpoints, candidate
HTML and credentials stay out of Git.

## Stage B — private R2 persistence

- Code commit: `e005d692fe47e5f5c6e3a6ade4e38c151a301aa0`
- Source identity: the checkpoint now carries the fixed corpus
  `documents_sha256`; a restored checkpoint is rejected when its locale, model,
  provider, version or source generation differs.
- Namespaces: private `sources`, immutable checkpoint objects plus `latest`
  pointers, and candidate objects under their source generation/locale/candidate
  digest. A complete candidate alone gets a `candidate-ready.json` receipt.
- Validation: every put/read verifies bounded byte count and SHA-256 metadata;
  missing objects, permission failures, transient failures and integrity errors
  remain distinct. Incomplete candidates have no ready receipt and cannot be
  restored for assembly.
- Actions: `.github/workflows/portal-extended-locales-r2.yml` adds a manually
  dispatched private round-trip and bounded candidate pipeline. It uses the
  existing `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, and
  `R2_BUCKET` names, standard Ubuntu runners, the pinned Hy-MT2 action, a 24-page
  source batch, 1..2400 seconds per locale, and matrix concurrency of two.
- Local verification: `test_portal_extended_r2.py` 6/6, extended locale tests
  57/57, hardening tests 10/10, Python syntax and both workflow YAML parses pass.

## Current boundary

The R2 round-trip is implemented but not yet run against the repository's live
private bucket from Actions. The candidate pipeline is intentionally not a
publication path. Inactive-tree assembly, extended-locale approval, production
cutover, live acceptance and rollback remain separate stages.
