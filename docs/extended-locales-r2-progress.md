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
- Live staging verification: Actions run `36002784789` completed successfully on
  the branch head `85ab68a06242140967d490d73f768726209422d5`. Its isolated
  private prefix was `_extended-locales/staging/roundtrip-36002784789-1`; the
  readback receipt was 79 bytes with SHA-256
  `ed595ebe90a93c9db028b0a0d06ebf1418f5a32c4236c14bcc6e52ef9557a4ec`.
  The same run classified the deliberate permission probe as `R2PermissionError`.
  No secret value or translation payload was printed.

## Current boundary

The candidate pipeline is intentionally not a publication path. Inactive-tree
assembly, extended-locale approval, production cutover, live acceptance and
rollback remain separate stages. The first real 24-page candidate has not yet
been accepted or published.

## 2026-09-24 handoff verification

- Current branch head: `c075fbda` (`fix: keep R2 progress free of public
  identity markers`). The preceding recovery workflow fix is `d0ecc1b2`,
  and the production-candidate input splitter is `dc182c56`; the recovery
  workflow generator now includes the R2 extended candidate assembly step and its
  generated target is exact.
- Local verification after the recovery fix: extended-locale tests 59/59,
  Hy-MT2 tests 33/33, R2 tests 6/6, hardening tests 10/10, Neutral cutover
  tests 34/34, recovery workflow tests 7/7, and restore/assembly tests 2/2.
- Candidate run: Actions `36015823873` ran on
  `dc182c5625174b8ed4eb947f77b86e533c209d71`, standard Ubuntu CPU runner,
  pinned Hy-MT2, locale `en`, fixed source generation
  `f334aac3023978818d18a4d28ed16cb2541a7b9b6ea803021f1fcd0502c812aa`, and
  budget `2400` seconds. Source collection and R2 restore succeeded; the
  build produced `1/24` pages and failed closed on 23 pages with
  `offline-quantity-validation` and `table-structure-validation`. Paid
  provider requests were `0`.
- R2 recovery evidence from that run: checkpoint readback began at 48,041
  bytes with SHA-256
  `30a3c8d91302e2585a9911d8aab706211c37c1e70582041e5b0e8aab6e7ffcbc` and
  the final immutable checkpoint persisted 78,890 bytes with SHA-256
  `535ba8ace83174e7a0722d15bf74931721a448262083fbda904001fbd52d51e5`.
  The private candidate receipt is incomplete: candidate
  `e0202939a30ffd63774511aad7481add6691f48b549350c98d7a3333ce6d016e`,
  manifest SHA-256
  `cbb0a720fd2af78cd9b146c225e73e158b07ea6731bd5625473bce97fcee37d0`,
  `ready=false`; no ready receipt was written.
- Production state: no inactive-tree assembly, approval, cutover or live
  sample was run for the new locales. Existing production locales and the
  existing release path were not changed. PR #180 remains draft until a
  complete candidate passes all gates.
