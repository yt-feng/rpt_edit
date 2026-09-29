# Publication handoff, 2026-09-29

The operator now requests activation of the additional non-English detail pages.
This is distinct from the prior read-only recovery test. English remains excluded.
No historic URL discovery or fresh full-batch translation is authorized by this
resume: only the exact already-started 24-page generation is eligible.

Production baseline checked: `6b0be8ab66d1a7d541df1270e169ac42ee77a337`.
PR #182 head before this work: `c85ae7004f995339bf55ae6d196cf65035be195f`.
The isolated existing worktree was fast-forwarded, then merged with current main;
the primary checkout's uncommitted work was not changed.

## Stage 1: durable recovery

`publication-resume` requires an explicit immutable daily generation and an
existing checksum-verified checkpoint for every requested locale. It discovers
no URLs, preserves the 24-page bound, and saves accepted progress and candidates
to private R2. Unlike `recovery-test`, it advances completed receipts only after
the complete candidate has been verified and persisted. It does not publish.
The operator's original two-concurrent-worker limit is restored; a 33-language
matrix is not promised to finish within one day at the maximum per-job budget.

Generation: `2b9081823e32528f402348f968d0771468dab06ea116b1a293fdf90a6621718b`.
Outstanding durable locales: `km,my,fa,gu,he,mr,bn,ta,mn,yue,de,kk`.
The other 21 locales already have complete R2 candidates from `36216968278`.
Read-only recovery `36336380713` proved 24/24 for the twelve above, but wrote
neither checkpoints nor candidates. It is not durable-completion evidence.

## Stage 2: inactive publication integration

The publication composer reads carry-forward approvals only from the captured
active release's checksum-verified R2 manifest and assembly ledger. Each new
locale also requires an explicit immutable generation/candidate map. It restores
the complete original candidate and checkpoint and reproduces the approved HTML
byte-for-byte with a cache-only translator. Cache misses are errors, not invented
translations or newly accepted source fallbacks.

After verifying unchanged source content (including links, dates, quantities and
metadata), it renders against the final inactive HTML. The new exact generation,
checkpoint and complete candidate are persisted privately; the unchanged raw
source-HTML SHA assembler verifies that new generation. No inference is used by
publication and no source SHA check is removed. Changed source content requires
a newly reviewed candidate rather than being silently reused.

Assembly now follows the established ko/ja/ar build and Chinese parity check.
It preserves their bodies and existing application assets, adds only coherent
per-page alternates, and merges approved batches across languages and dates.
The root sitemap retains its entries and adds the extended sitemap; robots
retains crawler policy and adds one sitemap line. Detailed page counts are kept
per locale. No fake language homepage is generated. Remote validation checks the
full declared detail-page set; live audit samples actual sitemap URLs. Acceptance
and rollback cover inherited pages as well as explicitly requested additions.

Local validation before dispatch: 304 Python tests passed, one skipped because
PyYAML is unavailable; 65 edge-host Node tests passed. The three changed workflows
parse with Ruby YAML and all 69 shell blocks pass `bash -n`. Public identity scan
passed on 6,035 files. Further runner and production evidence remains required;
local tests are not deployment.

## Publication gates still to satisfy

- Complete the twelve-locale durable resume, then obtain the exact candidate IDs.
- Pass PR checks on the new source revision and use the normal reviewed merge.
- Exercise the newly implemented inactive assembly on the real stored corpus.
- Preserve exact-source, complete-candidate, protected-Chinese, inactive-object,
  environment approval, atomic switch, acceptance and rollback gates.
- The initial check found only the existing protected multilingual environment.
  After the operator explicitly delegated environment setup and this release's
  approval operation, `portal-extended-locales-production` was created at
  `2026-09-29T12:12:17Z` with required reviewer `yt-feng`, matching the existing
  environment. The same-run identity variables and deployment review still must
  be recorded before activation; the gate has not been removed or bypassed.

No new language is claimed live by this checkpoint.

## Stage 3: release recovery parity

The first publication-integration CI (`36565103623`, source `3e22ffd1`)
failed the generated-recovery workflow equality test, not translation/R2 tests.
Regenerated recovery from the current release gates and fixed the related
immutable-candidate path: recovery verifies/downloads the extended ledger and
objects, derives their original identity without assembly or inference, and
requires a fresh exact-set environment approval before switching. Extended live
acceptance and rollback remain identical to the ordinary production workflow.
122 targeted Python regressions pass, including identity preservation, rejected
corruption/incomplete ledgers, and generated shell/Python parsing.

Current main `29a693066f418adf4e654c60ab5d33fa05bfca8c` was merged normally.
Durable resume `36565145888` has completed `km`; `my` and `fa` were running at
this check, with the remaining nine queued. This is not a publication claim.

The follow-up `publication-check` operation verifies complete R2 receipts and
replays their exact checkpoints against the current public source HTML. All
writes go to a unique `_extended-locales/staging/publication-RUN-ATTEMPT` prefix;
it cannot write the production candidate namespace, publish a static slot, or
invoke inference. Snapshot URLs are limited to the stored source pages and
their existing ko/ja/ar counterparts. No generated content becomes an Actions
artifact. This check is independent of, and cannot substitute for, production
approval and acceptance. A new full committed-object regression also caught and
fixed validation of localized sitemap paths: validate the source route after
the declared locale prefix, rather than rejecting the locale prefix itself.

Source `4cb023f0038ed7483ec4fe854b87bed86a3db3f9` passed 88 targeted local
checks and dispatched French staging publication check `36566608873`.
The added all-33 synthetic composition test passes too: each namespace contains
an indexable reading page, no invented homepage, no English original namespace,
and zero inference calls. This is routing/storage coverage, not a claim of
human-reviewed translation quality or live publication.

French real-data staging check `36566608873` succeeded: 24 pages restored from
candidate `509d97a8ae3b772655b3d602a9eac13d361ffdb1dc8120746ad3f046998a7062`,
99 public snapshot files, zero inference/paid calls and zero production writes.
Checkpoint checksum `484bf08c0f8a051dc28f1f6a169bfe871359f4cbbf95d8b0787551dc2b556f2a`
reproduced the approved bytes. Replayed generation
`908f95ce1545c940bb1a32138134ff1ba1ff09e2f7215ad82bc87e318e1524fc` and candidate
`0a3ed2ec2ff50f48fbdf03dc7912c02f5da701cdceb66f7a9042b11416e60196` are isolated
under `_extended-locales/staging/publication-36566608873-1`, not deployed.
The public identity scan rejected the checker's branded HTTP User-Agent; changed
it to the repository-neutral identifier, preserving the scan unchanged.

## Latest stopping point

Pushed implementation: `b52f1c281a27cefbba1cb8201cb2e5ca5a7874b9` (PR #182).
The neutral public-identity scan passes locally on 6,039 files; the extended
Python suite ran 252 tests with one dependency-related skip. The latest PR
checks were running when observed (public identity `36566979454`, extended
regression `36566979400`). No merge or production dispatch was performed.
The last successful durable-resume snapshot had `km,fa,my` complete, in addition
to the original 21; `gu,he` were active. All completed candidates have 24 pages.

The next GitHub run-status read failed with `net/http: TLS handshake timeout`.
Per the operator's explicit network rule, stopped external operations without
retry, transport changes, proxy/network inspection, or a substitute endpoint.
Environment setup is authorized and complete. After normal connectivity is
available, check current CI/head and resume through the exact-candidate normal
merge, first French activation, and remaining-locale activation. Do not repeat
translation or treat staging success as production success.

## Stage 4: merged release and full-inventory verification

Connectivity returned through the unchanged normal connection. PR #182 passed
all required checks on `f9e704084b79bd19e6243e7e47b6930b01f23646` and merged as
`537a206535fb003a959280465f152e8c3a5f74c3`. CPU preflight `36567198787` passed on
Ubuntu 22.04 and 24.04; regression `36567198878` and identity `36567198738` passed.
French production activation `36567911713` uses that merge SHA and the original
exact 24-page candidate map. It is pending the shared release lock held by
existing ordinary refresh `36565643908`; no duplicate release was launched.

Real R2 staging verification `36567341027` passed for 26 locales / 624 pages
in 10m30s, with 26 checksum-verified checkpoint restores, no inference, no paid
requests, and no production writes. The content-free evidence JSON beside this
file records every locale's page count, candidate ID and restored checkpoint
digest. This result is not production acceptance. The other seven locales are
not included in this staging proof, even where their translation has finished.

For the larger 33-locale release, final candidate verification now uses four
bounded concurrent page reads and a 15-minute step budget. It still validates
every page's checksum, language, direction, canonical and robots policy, not
just endpoint samples. A corrupted middle-page regression proves this; the
81 targeted tests pass and generated recovery retains identical release gates.

Follow-up PR #187 contains the bounded full-object checks and evidence, head
`f6c5f3f5e0ba54454e1c77545fd53ae605b0a45c`. Its regression, identity and locale
manifest checks passed. API-cost CI `36568821352` failed only downloading its
just-uploaded synthetic fixture (artifact ID `11032484134` not found); reran
only that failed synthetic job, with no translation or paid calls. The rerun
job `109408286699` was confirmed active, but watching that run then returned
`net/http: TLS handshake timeout`. Its final status and PR merge are unverified;
the command stopped before attempting the merge.

At the last durable-resume snapshot, `mr,km,fa,gu,ta,my,he,yue,bn` had completed,
making 30/33 complete candidates with the original 21. `de,mn` were running and
`kk` remained queued. French production `36567911713` was last confirmed pending
behind `36565643908`, whose ko/ja/ar build was still active. No production success
is asserted. Stop only the local read-only watcher on the network failure;
leave the Actions themselves running. Resume these exact run IDs on the next
successful normal connection, not duplicate jobs.

Remaining scope still includes verifying all 33 real published detail-page
sets and the current-day incremental handoff. The merged translation hook
produces candidates and carry-forward preserves approved pages; this alone
does not prove that later new candidates are automatically activated. Keep
that distinction in the completion audit rather than declaring the goal done
when the initial fixed-generation rollout finishes.

## Stage 5: all candidates complete; French prepared, approval not submitted

PR #187 is merged as `71925539ec0147b1691b62f1d935fe5555393e5b`.
The local continuation merged that main revision without overwriting changes.
Durable resume `36565145888` completed successfully, including the final `kk`
job at `2026-09-29T14:05:39Z`. Together with the original 21 locales, all 33
non-English candidates now have 24 complete pages in private R2. These are the
explicitly authorized already-started September 26 generation, not a claim of
33 live locales or new historical discovery.

Staging publication check `36569579402` passed for `mr,bn,ta,mn,yue` (120 pages,
zero inference and production writes). Check `36580358485`, dispatched on main,
passed for `de,kk`; together with `36567341027`, all 33 candidate locale sets
have passed the real isolated publication check. The already-started log read
returned successfully; the final seven exact candidate/checkpoint identities
are saved in `extended-locales-publication-evidence-remaining-20260929.json`.

French production run `36567911713`, pinned to
`537a206535fb003a959280465f152e8c3a5f74c3`, has completed `prepare_release`
successfully and is waiting at `extended_locales_approval`. The pending
environment is `portal-extended-locales-production`, id `23015803292`, with
required reviewer `yt-feng` and `current_user_can_approve=true`. The operator
delegated this approval operation; no additional permission question is needed.
Same-run validation artifact `11043421830` is named
`neutral-release-validation-36567911713-1`, size 11,872,186 bytes, and is bound
to that exact run and commit. The artifact download failed with
`read: connection reset by peer` before the review identity could be read.
No exact-version approval variables were set and no deployment approval was
submitted. Per the operator's network rule, no retry, alternate endpoint,
transport change or network inspection was attempted. Continue from this
waiting run, not a replacement translation or release.

Daily run `36576367899` has passed source collection and started its 33-locale
matrix with two concurrent jobs. Its completion and publication are unverified.
The planned daily candidate-to-publication handoff has not been implemented;
do not mistake an announced next step for committed functionality.

## Stage 6: French review artifact verified; approval setup partially saved

After normal connectivity resumed, the unchanged waiting run `36567911713`
and successful prepare job were reverified. Same-run validation artifact
`11043421830` downloaded successfully and its exact identity was inspected:

- Commit: `537a206535fb003a959280465f152e8c3a5f74c3`.
- Static tree: `d3674a2b873f54f6d2f247c9f37b2a47bcc8d784ca17ee48259a67e925efa00a`.
- Locale/page count: `fr`, 24.
- Source generation and French candidate equal the Stage 1/3 fixed identities.
- Provider `hymt`, pinned Hy-MT2 model, zero paid calls.
- Assembly complete; checkpoint digest equals the Stage 3 French digest;
  replay used zero inference and reproduced the same replayed candidate.
- Captured previous production: slot `a`, release
  `43609ac6ff5766859cf5e165672429f9`, tree
  `4c4a0558ae6e0e29b3dd2cc2a7054ad5c78c0304af3ff6a72fa49b1cd3b3dce0`.

The protected environment was confirmed pending for this run with current-user
approval permitted. Setting `PORTAL_EXTENDED_APPROVED_COMMIT_SHA` and
`PORTAL_EXTENDED_APPROVED_STATIC_TREE` succeeded. Setting
`PORTAL_EXTENDED_APPROVED_SOURCE_GENERATION` then failed during GitHub CLI
repository lookup with `net/http: TLS handshake timeout`. The shell stopped
immediately: the remaining identity variables and final activation flag were
not written, and the pending-deployment approval POST was not executed. No
network changes or alternate transport were attempted. Recheck current state
and finish the exact same-run identity setup before normal approval; do not
assume the partial environment setup constitutes approval or deployment.
