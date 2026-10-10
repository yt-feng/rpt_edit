# Retained article checkpoint diagnostics

The read-only inspector keeps the original 44-report Daily source, OCR handoff, manifest, and private checkpoint key fixed. An optional `generation_run_id` authenticates a later completed failed standalone recovery on same-repository `main`, including successful source restoration, failed generation, and successful progress save. It does not start generation, write/delete objects, or contact model providers.

The private generation checkpoint is mutable. Results are observations of its current checksum-verified bytes, not proof that those bytes were exclusively produced by the supplied run. Output carries the observed archive/context/log hashes, authenticated generation job identity, and an explicit `checkpoint_observation_only` marker. The existing receipt and exact per-report source/binding checks remain required before counting complete articles.

Incomplete report diagnostics expose only ordinal, bounded fixed title rejection categories, sizes and hashes. Durable progress observation calls the non-mutating state reader, validates bounded request entries and retained response checksums, and reports complete/pending counts without text, URLs, model responses or prompts. A pending request remains unknown; diagnosis never authorizes another provider call. Raw logs, article bodies and progress responses remain in private R2.

After a new failed recovery, dispatch the inspector with its run ID; read the completed job's typed JSON. Do not reuse earlier observed hashes as current evidence, infer completion from a missing legacy pending filename, or bypass source/editorial/delivery gates. Live article acceptance still requires complete generation, exact WeChat draft readback and canonical Blog publication.

Word-boundary diagnosis counts candidates containing a long Latin word before normalization separately from candidates where deleting whitespace creates such a word. This can distinguish untranslated English from cleaner-introduced joins without exposing candidate text. These counts alone do not approve a title or change generation behavior.
