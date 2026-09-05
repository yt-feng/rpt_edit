#!/usr/bin/env python3
from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/neutral-edge-cutover.yml"


class NeutralEdgeCutoverWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_schedule_and_content_triggers_are_gated_and_reviewed(self) -> None:
        trigger = self.workflow[: self.workflow.index("\npermissions:\n")]
        self.assertIn('cron: "30 1,5,9,13 * * *"', trigger)
        self.assertIn("workflow_run:", trigger)
        for producer in (
            "Bank report catalog",
            "Final PDF to XHS notes",
            "Institution latest PDF to WeChat",
            "Consulting latest PDF to WeChat",
            "ARK Invest feed to WeChat",
            "Upload XHS notes to WeChat drafts",
            "Portal chart search index",
        ):
            self.assertIn(f"- {producer}", trigger)
        self.assertNotIn("Portal Search Mirror", trigger)
        self.assertIn("types: [completed]", trigger)
        self.assertIn("branches: [main]", trigger)
        self.assertRegex(trigger, r"(?m)^\s+- rehearse\s*$")
        self.assertRegex(trigger, r"(?m)^\s+- locale-shadow\s*$")
        self.assertRegex(trigger, r"(?m)^\s+- migrate\s*$")
        self.assertNotIn("switch", trigger)
        self.assertIn("default: rehearse", trigger)
        self.assertIn("vars.NEUTRAL_SCHEDULE_ENABLED == 'true'", self.workflow)
        self.assertIn("vars.PORTAL_MULTILINGUAL_ENABLED != 'true'", self.workflow)
        self.assertIn("vars.PORTAL_MULTILINGUAL_LIVE == 'true'", self.workflow)
        self.assertIn("github.event.workflow_run.conclusion == 'success'", self.workflow)
        self.assertIn("github.event.workflow_run.head_branch == github.event.repository.default_branch", self.workflow)
        self.assertIn("github.event.workflow_run.head_repository.full_name == github.repository", self.workflow)
        self.assertIn('case "$GITHUB_EVENT_NAME" in', self.workflow)
        self.assertIn('rehearse|locale-shadow|migrate) operation="$REQUESTED_OPERATION"', self.workflow)
        self.assertIn('schedule|workflow_run)', self.workflow)

        operation = self.workflow[
            self.workflow.index("Require reviewed main operation"):
            self.workflow.index("Checkout public source")
        ]
        self.assertIn(
            "PORTAL_MULTILINGUAL_INDEX_START_DATE: "
            "${{ vars.PORTAL_MULTILINGUAL_INDEX_START_DATE || '' }}",
            operation,
        )
        self.assertIn(
            "PORTAL_MULTILINGUAL_LIVE_CONFIGURED: "
            "${{ vars.PORTAL_MULTILINGUAL_LIVE || 'false' }}",
            operation,
        )
        self.assertIn('if [ "$operation" = "locale-shadow" ]; then', operation)
        self.assertIn('multilingual_enabled="true"', operation)
        self.assertNotIn("PORTAL_MULTILINGUAL_ACTIVATION_APPROVED", operation)
        self.assertNotIn("PORTAL_MULTILINGUAL_APPROVED_STATIC_TREE", operation)
        self.assertIn('true|false) multilingual_live="$PORTAL_MULTILINGUAL_LIVE_CONFIGURED"', operation)
        self.assertIn("PORTAL_MULTILINGUAL_LIVE must be true or false", operation)
        self.assertIn('if [ -n "$PORTAL_MULTILINGUAL_INDEX_START_DATE" ]; then', operation)
        self.assertIn('parsed = date.fromisoformat(value)', operation)
        self.assertIn('parsed.isoformat() != value', operation)
        self.assertIn('elif [ "$operation" != "locale-shadow" ]; then', operation)
        self.assertIn(
            "Multilingual cutover requires a fixed PORTAL_MULTILINGUAL_INDEX_START_DATE",
            operation,
        )
        self.assertIn("printf 'commit_sha=%s\\n'", operation)
        self.assertIn("printf 'multilingual_enabled=%s\\n'", operation)
        self.assertIn("printf 'multilingual_live=%s\\n'", operation)

    def test_prepare_and_cutover_are_separate_bounded_jobs(self) -> None:
        self.assertIn("  prepare_release:\n", self.workflow)
        self.assertIn("  multilingual_approval:\n", self.workflow)
        self.assertIn("  cutover:\n", self.workflow)
        self.assertIn("needs: [prepare_release, multilingual_approval]", self.workflow)
        prepare = self.workflow.index("  prepare_release:\n")
        upload = self.workflow.index("Upload inactive static slot and immutable runtime")
        approval = self.workflow.index("  multilingual_approval:\n")
        cutover = self.workflow.index("  cutover:\n")
        deploy = self.workflow.index("Deploy prepared neutral edge release")
        self.assertLess(prepare, upload)
        self.assertLess(upload, approval)
        self.assertLess(approval, cutover)
        self.assertLess(upload, cutover)
        self.assertLess(cutover, deploy)
        self.assertIn("--max-workers 4", self.workflow[upload:cutover])
        self.assertIn("timeout-minutes: 150", self.workflow[prepare:cutover])
        self.assertIn("timeout-minutes: 65", self.workflow[cutover:])
        self.assertEqual(self.workflow.count("ref: ${{ github.sha }}"), 2)
        self.assertNotIn("ref: main", self.workflow)
        self.assertNotIn('echo "::add-mask::$release_id"', self.workflow)

    def test_portal_suite_uses_stable_isolated_node_runner(self) -> None:
        self.assertIn("for test_file in portal_suite/tests/*.test.mjs; do", self.workflow)
        self.assertIn('node "$test_file"', self.workflow)
        self.assertNotIn("node --test portal_suite/tests/*.test.mjs", self.workflow)
        self.assertNotIn("--test-isolation", self.workflow)

    def test_multilingual_release_is_opt_in_cached_and_transactional(self) -> None:
        prepare_start = self.workflow.index("  prepare_release:\n")
        prepare_steps = self.workflow.index("    steps:\n", prepare_start)
        prepare_header = self.workflow[prepare_start:prepare_steps]
        validate_source = self.workflow[
            self.workflow.index("Validate public source"):
            self.workflow.index("Prepare masked release context")
        ]
        restore = self.workflow.index("Restore resumable multilingual translation checkpoint")
        active_cache = self.workflow.index("Use active multilingual cache only without a CI checkpoint")
        hot_report_source = self.workflow.index("Download public Hot Reports translation source")
        base_build = self.workflow.index("Build private static release")
        locale_build = self.workflow.index("Build Korean Japanese and Arabic static locales")
        detect_checkpoint = self.workflow.index("Detect multilingual translation checkpoint")
        save_checkpoint = self.workflow.index("Save multilingual translation checkpoint")
        validate_release = self.workflow.index("Validate complete static release")
        brand_check = self.workflow.index("Validate built public brand")
        upload = self.workflow.index("Upload inactive static slot and immutable runtime")

        self.assertLess(restore, active_cache)
        self.assertLess(hot_report_source, locale_build)
        self.assertLess(active_cache, base_build)
        self.assertLess(base_build, locale_build)
        self.assertLess(locale_build, detect_checkpoint)
        self.assertLess(detect_checkpoint, save_checkpoint)
        self.assertLess(save_checkpoint, validate_release)
        self.assertLess(locale_build, validate_release)
        self.assertLess(validate_release, brand_check)
        self.assertLess(brand_check, upload)
        self.assertGreaterEqual(
            self.workflow.count("if: steps.operation.outputs.multilingual_enabled == 'true'"),
            3,
        )
        self.assertIn(
            "multilingual_enabled: ${{ steps.operation.outputs.multilingual_enabled }}",
            prepare_header,
        )
        self.assertIn(
            "multilingual_live: ${{ steps.operation.outputs.multilingual_live }}",
            prepare_header,
        )

        hot_report_download = self.workflow[hot_report_source:restore]
        self.assertIn("if: steps.operation.outputs.multilingual_enabled == 'true'", hot_report_download)
        self.assertIn('key = "_hot-reports/indexes/public-v2.json"', hot_report_download)
        self.assertIn("client.get_object(Bucket=bucket, Key=key)", hot_report_download)
        self.assertIn("Hot Reports public translation source is unavailable", hot_report_download)
        self.assertIn('Path(os.environ["RUNNER_TEMP"]) / "hot-reports-public-v2.json"', hot_report_download)

        restore_cache = self.workflow[restore:active_cache]
        self.assertIn("uses: actions/cache/restore@v4", restore_cache)
        self.assertIn("${{ runner.temp }}/portal-locale-cache/cache-v1.json.gz", restore_cache)
        self.assertIn(
            "key: portal-locale-cache-${{ hashFiles('scripts/build_portal_locales.py') }}-"
            "${{ github.run_id }}-${{ github.run_attempt }}",
            restore_cache,
        )
        restore_keys = restore_cache.split("restore-keys: |\n", 1)[1].split("\n\n", 1)[0]
        self.assertEqual(
            [line.strip() for line in restore_keys.splitlines()],
            [
                "portal-locale-cache-${{ hashFiles('scripts/build_portal_locales.py') }}-",
                "portal-locale-cache-",
            ],
        )

        cache = self.workflow[active_cache:base_build]
        checkpoint_guard = cache.index('if [ -s "$cache_path" ]; then')
        active_download = cache.index('status="$(curl')
        self.assertLess(checkpoint_guard, active_download)
        self.assertIn("Using the latest resumable CI translation checkpoint", cache)
        self.assertIn("exit 0", cache[checkpoint_guard:active_download])
        self.assertIn(
            "$LIVE_ORIGIN/.well-known/edge-release/$PREVIOUS_STATIC_RELEASE/data/i18n/cache-v1.json.gz",
            cache,
        )
        self.assertRegex(cache, r"(?m)^\s+404\)\s*$")
        self.assertIn('mv "$active_cache" "$cache_path"', cache)
        self.assertNotIn('rm -f "$cache_path"', cache)

        locale = self.workflow[locale_build:detect_checkpoint]
        for secret in (
            "DEEPSEEK_API_KEY",
            "DEEPSEEK_API_KEY_BACKUP",
            "DEEPSEEK_API_KEY_2",
            "DEEPSEEK_API_KEYS",
        ):
            self.assertIn(f"{secret}: ${{{{ secrets.{secret} }}}}", locale)
        self.assertIn("DEEPSEEK_BASE_URL", locale)
        self.assertIn("DEEPSEEK_MODEL", locale)
        self.assertIn("PORTAL_MULTILINGUAL_WORKERS: ${{ vars.PORTAL_MULTILINGUAL_WORKERS || '32' }}", locale)
        self.assertIn(
            "PORTAL_MULTILINGUAL_INDEX_START_DATE: "
            "${{ vars.PORTAL_MULTILINGUAL_INDEX_START_DATE || '' }}",
            locale,
        )
        self.assertIn(
            "PORTAL_MULTILINGUAL_INDEX_ALLOWLIST_PATH: "
            "${{ vars.PORTAL_MULTILINGUAL_INDEX_ALLOWLIST_PATH || '' }}",
            locale,
        )
        self.assertIn('[ "$PORTAL_MULTILINGUAL_WORKERS" -gt 500 ]', locale)
        for argument in (
            "--root _neutral_site",
            '--site-url "$LIVE_ORIGIN"',
            '--hot-report-index "$RUNNER_TEMP/hot-reports-public-v2.json"',
            "--cache-out _neutral_site/data/i18n/cache-v1.json.gz",
            "--assets-root portal_suite/locale_assets",
            '--workers "$PORTAL_MULTILINGUAL_WORKERS"',
            '--model "$DEEPSEEK_MODEL"',
            '--deepseek-base-url "$DEEPSEEK_BASE_URL"',
        ):
            self.assertIn(argument, locale)
        self.assertIn('cache_args+=(--cache-in "$RUNNER_TEMP/portal-locale-cache/cache-v1.json.gz")', locale)
        self.assertEqual(locale.count("--cache-in"), 2)
        preflight = locale.index("--preflight-only --preflight-batches-per-locale 1")
        full = locale.index("--cache-in _neutral_site/data/i18n/cache-v1.json.gz")
        self.assertLess(preflight, full)
        self.assertIn("set -euo pipefail", locale)
        self.assertIn("--workers 1 --attempts 2 --max-provider-requests 6", locale[:full])
        self.assertIn('test -s _neutral_site/data/i18n/cache-v1.json.gz', locale[preflight:full])
        self.assertIn('"$RUNNER_TEMP/locale-preflight-diagnostics.json"', locale)
        self.assertIn('"$RUNNER_TEMP/locale-full-diagnostics.json"', locale)
        self.assertIn("--max-provider-cost-cny 400", locale[full:])
        self.assertNotIn("|| true", locale)
        diagnostics = self.workflow.index("Preserve translation diagnostics even on failure")
        self.assertLess(save_checkpoint, diagnostics)
        self.assertLess(diagnostics, validate_release)
        diagnostics_step = self.workflow[diagnostics:self.workflow.index("Verify protected Chinese release", diagnostics)]
        self.assertIn("if: always() && steps.operation.outputs.multilingual_enabled == 'true'", diagnostics_step)
        self.assertIn("uses: actions/upload-artifact@v4", diagnostics_step)
        self.assertIn("locale-preflight-diagnostics.json", diagnostics_step)
        self.assertIn("locale-full-diagnostics.json", diagnostics_step)
        self.assertIn('index_args=(--index-start-date "$PORTAL_MULTILINGUAL_INDEX_START_DATE")', locale)
        self.assertIn('if [ -n "$PORTAL_MULTILINGUAL_INDEX_ALLOWLIST_PATH" ]; then', locale)
        self.assertIn('PurePosixPath(value)', locale)
        self.assertIn('candidate.resolve().relative_to(Path.cwd().resolve())', locale)
        self.assertIn('not candidate.is_file() or candidate.is_symlink()', locale)
        self.assertIn(
            'git ls-files --error-unmatch -- "$PORTAL_MULTILINGUAL_INDEX_ALLOWLIST_PATH"',
            locale,
        )
        self.assertIn(
            'index_args+=(--index-allowlist "$PORTAL_MULTILINGUAL_INDEX_ALLOWLIST_PATH")',
            locale,
        )
        self.assertIn('"${index_args[@]}"', locale)

        checkpoint = self.workflow[detect_checkpoint:validate_release]
        self.assertIn("if: always() && steps.operation.outputs.multilingual_enabled == 'true'", checkpoint)
        self.assertIn('cp "_neutral_site/data/i18n/cache-v1.json.gz"', checkpoint)
        self.assertIn('echo "present=true" >> "$GITHUB_OUTPUT"', checkpoint)
        self.assertIn("uses: actions/cache/save@v4", checkpoint)
        self.assertIn("if: always() && steps.locale_checkpoint.outputs.present == 'true'", checkpoint)
        self.assertIn("${{ runner.temp }}/portal-locale-cache/cache-v1.json.gz", checkpoint)
        self.assertIn(
            "key: portal-locale-cache-${{ hashFiles('scripts/build_portal_locales.py') }}-"
            "${{ github.run_id }}-${{ github.run_attempt }}",
            checkpoint,
        )

        self.assertIn("scripts/test_build_portal_locales.py", validate_source)
        self.assertIn("scripts/test_portal_locale_runtime.js", validate_source)
        self.assertIn("scripts/build_portal_locales.py", validate_source)
        self.assertIn("portal_suite/locale_assets/locale-runtime.js", validate_source)

        release_gate = self.workflow[validate_release:brand_check]
        for path in (
            '"$locale/index.html"',
            '"$locale/assets/$locale_asset"',
            '"$locale/data/course-materials.json"',
            '"sitemap-$locale.xml"',
            "data/i18n/cache-v1.json.gz",
            "data/i18n/manifest.json",
            "assets/locale.css",
            "assets/locale-runtime.js",
        ):
            self.assertIn(path, release_gate)
        for asset in (
            "app.js",
            "charts.js",
            "contact.js",
            "locale-runtime.js",
            "report-chat.js",
            "report-research-export.js",
            "site-runtime.js",
            "xlsx-export.js",
            "locale.css",
        ):
            self.assertIn(asset, release_gate)
        self.assertIn("node --check", release_gate)
        self.assertIn('locale_directions = {"ko": "ltr", "ja": "ltr", "ar": "rtl"}', release_gate)
        self.assertIn('root / f"sitemap-{locale}.xml"', release_gate)
        self.assertIn("gzip.open(cache_path", release_gate)
        self.assertIn('manifest.get("quality_gate_version") != 2', release_gate)
        self.assertIn('manifest.get("coverage")', release_gate)
        self.assertIn('manifest.get("html_page_count")', release_gate)
        self.assertIn('actual_html_page_count != expected_html_page_count', release_gate)
        self.assertNotIn('"data/i18n/$locale/catalog-titles.json"', release_gate)
        self.assertIn('manifest.get("required_paths")', release_gate)
        self.assertIn('manifest.get("catalog_overlays")', release_gate)
        self.assertIn('manifest.get("catalog_detail_overlays")', release_gate)
        self.assertIn('manifest.get("chart_overlays")', release_gate)
        self.assertIn('manifest.get("hot_report_overlays")', release_gate)
        self.assertIn('manifest.get("locale_data_files")', release_gate)
        self.assertIn('runtime_data_byte_limits = {', release_gate)
        self.assertIn('"preview": 512_000', release_gate)
        self.assertIn('"detail": 512_000', release_gate)
        self.assertIn('"full": 8_000_000', release_gate)
        self.assertIn('"charts": 32_000_000', release_gate)
        self.assertIn('"hot-reports": 6_000_000', release_gate)
        self.assertIn('"course-materials": 2_000_000', release_gate)
        self.assertIn('expected_size > maximum_size', release_gate)
        self.assertIn('kind.startswith("detail:")', release_gate)
        self.assertIn('register_metadata(locale, "hot-reports", metadata)', release_gate)
        self.assertIn('register_metadata(locale, "charts", metadata)', release_gate)
        self.assertIn('register_locale_data(locale, kind, metadata)', release_gate)
        self.assertIn('PurePosixPath(value)', release_gate)
        self.assertIn('relative.is_absolute()', release_gate)
        self.assertIn('any(part in {"", ".", ".."}', release_gate)
        self.assertIn('set(required_paths) != set(manifest_metadata)', release_gate)
        self.assertIn('hashlib.sha256(payload_bytes).hexdigest()', release_gate)
        self.assertIn('payload.get("locale") != locale', release_gate)
        self.assertIn('payload.get("kind") != kind', release_gate)
        self.assertIn('payload.get("item_count") != item_count', release_gate)
        self.assertIn('"assets/locale-runtime.js": 32_768', release_gate)
        self.assertIn('"assets/locale.css": 24_576', release_gate)
        self.assertIn('size <= maximum_asset_bytes', release_gate)
        self.assertIn('localized_asset.read_bytes() != expected', release_gate)
        self.assertIn('index_policy.get("index_start_date") != configured_start_date', release_gate)
        self.assertIn("maximum_files = 100_000 if multilingual else 20_000", release_gate)
        self.assertIn("maximum_bytes = 2_500_000_000 if multilingual else 1_000_000_000", release_gate)
        self.assertIn("len(files) <= maximum_files", release_gate)

        delta = self.workflow[
            self.workflow.index("Detect meaningful public release changes"):
            upload
        ]
        self.assertIn("--build-contract scripts/build_portal_locales.py", delta)
        self.assertIn("--build-contract portal_suite/locale_assets/locale.css", delta)
        self.assertIn("--build-contract portal_suite/locale_assets/locale-runtime.js", delta)
        for generated_contract in (
            "_neutral_site/data/i18n/cache-v1.json.gz",
            "_neutral_site/data/i18n/manifest.json",
            "_neutral_site/sitemap-ko.xml",
            "_neutral_site/sitemap-ja.xml",
            "_neutral_site/sitemap-ar.xml",
        ):
            self.assertIn(f"--build-contract {generated_contract}", delta)
        self.assertIn("--public-root _neutral_site", delta)
        self.assertIn('if [ "$PORTAL_MULTILINGUAL_ENABLED" = "true" ]; then', delta)

    def test_multilingual_chinese_parity_gate_wraps_locale_build(self) -> None:
        validate_source = self.workflow[
            self.workflow.index("Validate public source"):
            self.workflow.index("Prepare masked release context")
        ]
        capture_manifest = self.workflow.index("Capture exact active static manifest")
        base_build = self.workflow.index("Build private static release")
        snapshot = self.workflow.index("Snapshot protected Chinese release before locale build")
        locale_build = self.workflow.index("Build Korean Japanese and Arabic static locales")
        save_checkpoint = self.workflow.index("Save multilingual translation checkpoint")
        parity = self.workflow.index("Verify protected Chinese release after locale build")
        validate_release = self.workflow.index("Validate complete static release")

        self.assertLess(capture_manifest, base_build)
        self.assertLess(base_build, snapshot)
        self.assertLess(snapshot, locale_build)
        self.assertLess(locale_build, save_checkpoint)
        self.assertLess(save_checkpoint, parity)
        self.assertLess(parity, validate_release)

        active_manifest_step = self.workflow[capture_manifest:base_build]
        self.assertIn('manifest["files"].get("assets/app.js")', active_manifest_step)
        self.assertIn('slot_prefix(state["slot"]) + "assets/app.js"', active_manifest_step)
        self.assertIn('runner / "previous-active-app.js"', active_manifest_step)

        snapshot_step = self.workflow[snapshot:locale_build]
        self.assertIn("if: steps.operation.outputs.multilingual_enabled == 'true'", snapshot_step)
        self.assertIn('if [ "$MULTILINGUAL_LIVE" != "true" ]; then', snapshot_step)
        self.assertIn('--active-manifest "$RUNNER_TEMP/previous-slot-manifest.json"', snapshot_step)
        self.assertIn("verify_portal_chinese_parity.py snapshot", snapshot_step)
        self.assertIn('--output "$RUNNER_TEMP/chinese-before-locales.json"', snapshot_step)
        self.assertIn("candidate_gzip = gzip.compress(candidate, compresslevel=9, mtime=0)", snapshot_step)
        self.assertIn("len(candidate) > 700_000 or len(candidate_gzip) > 150_000", snapshot_step)
        self.assertIn("raw_delta > 24_000 or gzip_delta > 6_000", snapshot_step)

        parity_step = self.workflow[parity:validate_release]
        self.assertIn("id: chinese_parity", parity_step)
        self.assertIn("verify_portal_chinese_parity.py verify", parity_step)
        self.assertIn('--snapshot "$RUNNER_TEMP/chinese-before-locales.json"', parity_step)
        self.assertIn('--output "$RUNNER_TEMP/chinese-parity.json"', parity_step)
        self.assertIn('print(f"sha256={hashlib.sha256(report.read_bytes()).hexdigest()}")', parity_step)

        self.assertIn("scripts/test_verify_portal_chinese_parity.py", validate_source)
        self.assertIn("scripts/test_audit_portal_shadow_preview.py", validate_source)
        self.assertIn("chinese_parity_sha256: ${{ steps.chinese_parity.outputs.sha256 }}", self.workflow)
        self.assertIn("PORTAL_MULTILINGUAL_APPROVED_CHINESE_PARITY_SHA256", self.workflow)
        self.assertIn('_release_validation/candidate/chinese-performance.json', self.workflow)

    def test_multilingual_candidate_is_exactly_accepted_without_rollback_assumption(self) -> None:
        artifact = self.workflow[
            self.workflow.index("Build public validation artifact"):
            self.workflow.index("Upload release validation artifact")
        ]
        self.assertIn(
            "PORTAL_MULTILINGUAL_ENABLED: ${{ steps.operation.outputs.multilingual_enabled }}",
            artifact,
        )
        self.assertIn('if [ "$PORTAL_MULTILINGUAL_ENABLED" = "true" ]; then', artifact)
        for candidate in (
            '"_release_validation/candidate/$locale/index.html"',
            '"_release_validation/candidate/sitemap-$locale.xml"',
            "_release_validation/candidate/data/i18n/manifest.json",
        ):
            self.assertIn(candidate, artifact)

        cutover_start = self.workflow.index("  cutover:\n")
        cutover_steps = self.workflow.index("    steps:\n", cutover_start)
        cutover_env = self.workflow[cutover_start:cutover_steps]
        self.assertIn(
            "PORTAL_MULTILINGUAL_ENABLED: ${{ needs.prepare_release.outputs.multilingual_enabled }}",
            cutover_env,
        )
        self.assertIn("needs.prepare_release.outputs.changed == 'true'", cutover_env)
        self.assertIn("needs.prepare_release.outputs.operation != 'locale-shadow'", cutover_env)

        acceptance = self.workflow[
            self.workflow.index("Accept prepared release through the live edge"):
            self.workflow.index("Roll back failed release or completed rehearsal")
        ]
        self.assertIn('if [ "$PORTAL_MULTILINGUAL_ENABLED" = "true" ]; then', acceptance)
        for live_path in (
            '"$origin/$locale/"',
            '"$origin/sitemap-$locale.xml"',
            '"$origin/data/i18n/manifest.json"',
        ):
            self.assertIn(live_path, acceptance)
        for candidate in (
            '"_release_validation/candidate/$locale/index.html"',
            '"_release_validation/candidate/sitemap-$locale.xml"',
            "_release_validation/candidate/data/i18n/manifest.json",
        ):
            self.assertIn(candidate, acceptance)
        self.assertIn("--dump-header", acceptance)
        self.assertIn('if values != [locale]:', acceptance)
        self.assertIn('expected_direction = "rtl" if locale == "ar" else "ltr"', acceptance)
        self.assertIn('relative = parsed.path[len(prefix):].strip("/")', acceptance)
        self.assertIn('if "/" in relative:', acceptance)
        self.assertIn('sorted(set(candidates))[0]', acceptance)
        self.assertIn("--write-out '%{http_code}'", acceptance)
        self.assertIn('test "$deep_status" = "200"', acceptance)
        self.assertIn('parser.canonicals != [deep_url]', acceptance)
        self.assertIn('parser.meta.get("og:url") != [deep_url]', acceptance)
        self.assertIn('set(parser.alternates) != set(expected_alternates)', acceptance)
        self.assertIn('Deep locale page has invalid JSON-LD', acceptance)
        self.assertIn('Deep locale page has no JSON-LD', acceptance)
        self.assertIn('has_locale_language(document)', acceptance)

        rollback = self.workflow[
            self.workflow.index("Verify exact previous release after rollback"):
            self.workflow.index("Enforce transactional outcome")
        ]
        self.assertIn(
            'cmp _release_validation/previous/edge-state.json "$RUNNER_TEMP/rollback-edge-state.json"',
            rollback,
        )
        self.assertIn(
            'cmp _release_validation/previous/catalog.json "$RUNNER_TEMP/rollback-public-catalog.json"',
            rollback,
        )
        self.assertNotIn('"$origin/$locale/"', rollback)
        self.assertNotIn('"$origin/sitemap-$locale.xml"', rollback)
        self.assertNotIn("public-locale-manifest", rollback)

    def test_multilingual_shadow_is_isolated_reviewable_and_removed(self) -> None:
        upload = self.workflow.index("Upload inactive static slot and immutable runtime")
        prepare = self.workflow.index("Prepare isolated multilingual shadow worker")
        deploy = self.workflow.index("Deploy isolated multilingual shadow worker")
        verify = self.workflow.index("Verify isolated multilingual shadow worker")
        artifact = self.workflow.index("Build public validation artifact")
        hold = self.workflow.index("  shadow_review_hold:\n")
        approval = self.workflow.index("  multilingual_approval:\n")
        cleanup = self.workflow.index("  cleanup_multilingual_shadow:\n")
        self.assertLess(upload, prepare)
        self.assertLess(prepare, deploy)
        self.assertLess(deploy, verify)
        self.assertLess(verify, artifact)
        self.assertLess(artifact, hold)
        self.assertLess(hold, approval)
        self.assertGreater(cleanup, self.workflow.index("  cutover:\n"))

        shadow = self.workflow[prepare:artifact]
        self.assertIn("portal-locale-shadow-${GITHUB_RUN_ID}-${GITHUB_RUN_ATTEMPT}", shadow)
        self.assertIn("workers_dev = true", shadow)
        self.assertIn("preview_urls = false", shadow)
        self.assertIn('CANONICAL_HOST = ""', shadow)
        self.assertIn('--public-origin "$LIVE_ORIGIN"', shadow)
        self.assertIn('SHADOW_MODE = "true"', shadow)
        self.assertIn('service = "portal-suite-worker"', shadow)
        self.assertIn("steps.operation.outputs.operation == 'locale-shadow'", shadow)
        self.assertIn("steps.operation.outputs.multilingual_live != 'true'", shadow)
        self.assertIn("uses: cloudflare/wrangler-action@v4", shadow)
        self.assertIn("workingDirectory: .neutral_edge_shadow", shadow)
        self.assertIn("command: deploy", shadow)
        self.assertNotIn("versions deploy", shadow)
        self.assertIn("audit_portal_shadow_preview.py plan", shadow)
        self.assertIn("audit_portal_shadow_preview.py audit", shadow)

        artifact_section = self.workflow[artifact:self.workflow.index("Upload release validation artifact")]
        for name in (
            "chinese-parity.json",
            "shadow-preview.json",
            "shadow-samples.json",
            "shadow-http-audit.json",
            "assets/locale.css",
            "assets/locale-runtime.js",
        ):
            self.assertIn(name, artifact_section)

        hold_section = self.workflow[hold:approval]
        self.assertIn("name: portal-multilingual-shadow-review", hold_section)
        self.assertIn("needs.prepare_release.outputs.operation == 'locale-shadow'", hold_section)
        self.assertIn("Download exact shadow review artifact", hold_section)
        self.assertIn("Confirm reviewed shadow identity", hold_section)
        self.assertIn("shadow-http-audit.json", hold_section)

        cleanup_section = self.workflow[cleanup:]
        self.assertIn(
            "needs: [prepare_release, shadow_review_hold, multilingual_approval, cutover]",
            cleanup_section,
        )
        self.assertIn('test "$SHADOW_WORKER_NAME" = "$expected"', cleanup_section)
        self.assertIn("/workers/scripts/$SHADOW_WORKER_NAME", cleanup_section)
        self.assertIn('payload.get("success") is not True', cleanup_section)

    def test_multilingual_cutover_is_bound_to_the_reviewed_candidate_identity(self) -> None:
        policy_start = self.workflow.index("Compute multilingual index policy identity")
        compare_start = self.workflow.index("Detect meaningful public release changes")
        upload_start = self.workflow.index("Upload inactive static slot and immutable runtime")
        review_start = self.workflow.index("Publish multilingual review identity")
        artifact_start = self.workflow.index("Build public validation artifact")
        artifact_upload = self.workflow.index("Upload release validation artifact")
        approval_job = self.workflow.index("  multilingual_approval:\n")
        cutover_job = self.workflow.index("  cutover:\n")
        self.assertLess(policy_start, compare_start)
        self.assertLess(compare_start, upload_start)
        self.assertLess(upload_start, review_start)
        self.assertLess(review_start, artifact_start)
        self.assertLess(artifact_start, artifact_upload)
        self.assertLess(artifact_upload, approval_job)
        self.assertLess(approval_job, cutover_job)

        policy = self.workflow[policy_start:compare_start]
        self.assertIn("id: locale_policy", policy)
        self.assertIn('manifest.get("index_policy")', policy)
        self.assertIn('hashlib.sha256(allowlist_bytes).hexdigest()', policy)
        self.assertIn('sort_keys=True', policy)
        self.assertIn('index_policy_sha256={digest}', policy)

        review = self.workflow[review_start:artifact_start]
        self.assertNotIn("PORTAL_MULTILINGUAL_APPROVED_", review)
        self.assertIn(
            "CANDIDATE_COMMIT_SHA: ${{ steps.operation.outputs.commit_sha }}",
            review,
        )
        self.assertIn(
            "CANDIDATE_STATIC_TREE: ${{ steps.static_upload.outputs.tree_sha256 }}",
            review,
        )
        self.assertIn(
            "CANDIDATE_INDEX_POLICY_SHA256: ${{ steps.locale_policy.outputs.index_policy_sha256 }}",
            review,
        )
        self.assertNotIn('if approved != actual:', review)
        self.assertIn("GITHUB_STEP_SUMMARY", review)
        self.assertIn("Static tree SHA-256", review)
        self.assertIn("Index policy SHA-256", review)

        artifact = self.workflow[
            artifact_start:
            self.workflow.index("Upload release validation artifact")
        ]
        self.assertIn("multilingual-review-identity.json", artifact)
        artifact_upload_step = self.workflow[artifact_upload:approval_job]
        self.assertIn("retention-days: 7", artifact_upload_step)

        approval = self.workflow[approval_job:cutover_job]
        self.assertIn("needs: prepare_release", approval)
        self.assertIn("needs.prepare_release.outputs.operation != 'locale-shadow'", approval)
        self.assertIn("needs.prepare_release.outputs.multilingual_enabled == 'true'", approval)
        self.assertIn("needs.prepare_release.outputs.multilingual_live != 'true'", approval)
        self.assertIn("name: portal-multilingual-production", approval)
        self.assertIn("Download exact multilingual candidate identity", approval)
        self.assertIn("Approve exact same-run multilingual candidate", approval)
        self.assertNotIn("actions/checkout", approval)
        self.assertNotIn("build_portal_locales.py", approval)
        self.assertIn(
            "CANDIDATE_COMMIT_SHA: ${{ needs.prepare_release.outputs.candidate_commit }}",
            approval,
        )
        self.assertIn(
            "CANDIDATE_STATIC_TREE: ${{ needs.prepare_release.outputs.static_tree }}",
            approval,
        )
        self.assertIn(
            "CANDIDATE_INDEX_POLICY_SHA256: "
            "${{ needs.prepare_release.outputs.multilingual_index_policy_sha256 }}",
            approval,
        )
        for environment_variable in (
            "PORTAL_MULTILINGUAL_APPROVED_COMMIT_SHA",
            "PORTAL_MULTILINGUAL_APPROVED_STATIC_TREE",
            "PORTAL_MULTILINGUAL_APPROVED_INDEX_POLICY_SHA256",
        ):
            self.assertIn(f"vars.{environment_variable}", approval)
        self.assertIn("vars.PORTAL_MULTILINGUAL_ACTIVATION_APPROVED", approval)
        self.assertIn('if os.environ["PORTAL_MULTILINGUAL_ACTIVATION_APPROVED"] != "true":', approval)
        self.assertIn('artifact_identity != actual', approval)
        self.assertIn('if approved != actual:', approval)
        self.assertIn("Multilingual environment identity mismatch", approval)

        cutover_header = self.workflow[
            cutover_job:
            self.workflow.index("    steps:\n", cutover_job)
        ]
        self.assertIn("needs: [prepare_release, multilingual_approval]", cutover_header)
        self.assertIn("always()", cutover_header)
        self.assertIn("needs.prepare_release.result == 'success'", cutover_header)
        self.assertIn("needs.multilingual_approval.result == 'success'", cutover_header)
        self.assertIn("needs.prepare_release.outputs.multilingual_enabled != 'true'", cutover_header)
        self.assertIn("needs.prepare_release.outputs.multilingual_live == 'true'", cutover_header)
        self.assertNotIn("gh variable set", self.workflow)
        self.assertNotIn("PORTAL_MULTILINGUAL_LIVE_CONFIGURED=true", self.workflow)

    def test_multilingual_live_truth_table_preserves_noop_and_skipped_dependencies(self) -> None:
        def automatic_prepare_allowed(
            *, schedule_enabled: bool = True, multilingual: bool = False,
            live: bool = False,
        ) -> bool:
            return schedule_enabled and (not multilingual or live)

        def approval_required(
            *, prepare_result: str = "success", changed: bool = True,
            operation: str = "migrate", multilingual: bool = True, live: bool = False,
        ) -> bool:
            return (
                prepare_result == "success"
                and changed
                and operation != "locale-shadow"
                and multilingual
                and not live
            )

        def cutover_allowed(
            *, prepare_result: str = "success", changed: bool = True,
            operation: str = "migrate", multilingual: bool = True, live: bool = False,
            approval_result: str = "skipped",
        ) -> bool:
            return (
                prepare_result == "success"
                and changed
                and operation != "locale-shadow"
                and (
                    not multilingual
                    or live
                    or approval_result == "success"
                )
            )

        self.assertTrue(automatic_prepare_allowed(multilingual=False, live=False))
        self.assertTrue(automatic_prepare_allowed(multilingual=True, live=True))
        self.assertFalse(automatic_prepare_allowed(multilingual=True, live=False))
        self.assertFalse(automatic_prepare_allowed(schedule_enabled=False, multilingual=False))
        self.assertTrue(approval_required())
        self.assertFalse(approval_required(live=True))
        self.assertFalse(approval_required(multilingual=False))
        self.assertFalse(approval_required(operation="locale-shadow"))
        self.assertTrue(cutover_allowed(approval_result="success"))
        self.assertFalse(cutover_allowed(approval_result="skipped"))
        self.assertFalse(cutover_allowed(approval_result="failure"))
        self.assertTrue(cutover_allowed(live=True, approval_result="skipped"))
        self.assertTrue(cutover_allowed(multilingual=False, approval_result="skipped"))
        self.assertFalse(cutover_allowed(operation="locale-shadow", live=True))
        self.assertFalse(cutover_allowed(changed=False, live=True))
        self.assertFalse(cutover_allowed(prepare_result="failure", live=True))

    def test_transaction_has_exact_state_and_operation_aware_rollback(self) -> None:
        self.assertIn("previous-edge-state.json", self.workflow)
        self.assertIn("previous_release", self.workflow)
        self.assertIn("previous_tree", self.workflow)
        self.assertIn("Prove live release is unchanged before cutover", self.workflow)
        self.assertIn("cmp _release_validation/previous/edge-state.json", self.workflow)
        self.assertIn("Capture exact edge rollback target", self.workflow)
        self.assertIn("steps.release_acceptance.outcome != 'success' || needs.prepare_release.outputs.operation == 'rehearse'", self.workflow)
        self.assertIn("rollback ${{ env.EDGE_PREVIOUS_VERSION_ID }}", self.workflow)
        self.assertIn("--expect-version \"$EDGE_PREVIOUS_VERSION_ID\"", self.workflow)
        self.assertIn("Verify exact previous release after rollback", self.workflow)
        self.assertIn("Enforce transactional outcome", self.workflow)

        previous_state = self.workflow[
            self.workflow.index("Capture exact previous state and public discovery"):
            self.workflow.index("Capture active release semantics")
        ]
        self.assertEqual(previous_state.count("python3 - <<'PY'"), 1)

    def test_semantic_manifest_prevents_unchanged_automatic_cutovers(self) -> None:
        compare = self.workflow.index("Detect meaningful public release changes")
        upload = self.workflow.index("Upload inactive static slot and immutable runtime")
        deploy = self.workflow.index("Deploy prepared neutral edge release")
        self.assertLess(compare, upload)
        self.assertLess(upload, deploy)
        self.assertIn("previous-release-semantics.json", self.workflow)
        self.assertIn('PYTHONPATH=scripts PREVIOUS_MANIFEST="$output" python3', self.workflow)
        self.assertIn("--write-current-manifest _neutral_site/data/release-semantics.json", self.workflow)
        for component in (
            "--current-catalog",
            "--current-search-index",
            "--current-chart-search-index",
            "--current-password-rules",
            "--current-runtime-config",
            "--blog-archive-root",
            "--site-source-root",
            "--public-root",
        ):
            self.assertIn(component, self.workflow)
        self.assertIn('if [ "$GITHUB_EVENT_NAME" = "workflow_dispatch" ]', self.workflow)
        self.assertEqual(self.workflow.count("--force"), 1)
        self.assertIn("if: steps.release_delta.outputs.changed == 'true'", self.workflow)
        cutover_header = self.workflow[
            self.workflow.index("  cutover:\n"):
            self.workflow.index("    steps:\n", self.workflow.index("  cutover:\n"))
        ]
        self.assertIn("needs.prepare_release.outputs.changed == 'true'", cutover_header)
        self.assertIn("needs.prepare_release.outputs.operation != 'locale-shadow'", cutover_header)
        self.assertIn("release-semantics-after.json", self.workflow)

    def test_public_brand_gate_covers_build_publish_and_live_acceptance(self) -> None:
        build = self.workflow.index("Build private static release")
        brand_check = self.workflow.index("Validate built public brand")
        compare = self.workflow.index("Detect meaningful public release changes")
        upload = self.workflow.index("Upload inactive static slot and immutable runtime")
        self.assertLess(build, brand_check)
        self.assertLess(brand_check, compare)
        self.assertLess(compare, upload)
        self.assertIn("python3 -B scripts/test_check_public_brand.py", self.workflow)
        self.assertIn("python3 -B scripts/test_render_private_config.py", self.workflow)
        self.assertIn("python3 -B scripts/check_public_brand.py _neutral_site", self.workflow)

        acceptance = self.workflow[
            self.workflow.index("Accept prepared release through the live edge"):
            self.workflow.index("Roll back failed release or completed rehearsal")
        ]
        rollback = self.workflow[
            self.workflow.index("Verify exact previous release after rollback"):
            self.workflow.index("Enforce transactional outcome")
        ]
        for section, directory in (
            (acceptance, "public-brand-after"),
            (rollback, "public-brand-rollback"),
        ):
            self.assertIn(directory, section)
            self.assertIn('"$origin/"', section)
            for path in ("assets/app.js", "assets/app-mark.svg", "doc.html", "report.html"):
                self.assertIn(f'"$origin/{path}"', section)
            self.assertIn("python3 -B scripts/check_public_brand.py", section)

    def test_member_contact_card_is_rebuilt_privately_and_changes_release_semantics(self) -> None:
        install = self.workflow.index("Install refresh dependencies")
        validate = self.workflow.index("Validate public source")
        materialize = self.workflow[
            self.workflow.index("Materialize private deployment profile"):
            self.workflow.index("Refresh report catalog with additive PDF sync")
        ]
        build = self.workflow[
            self.workflow.index("Build private static release"):
            self.workflow.index("Validate built public brand")
        ]
        delta = self.workflow[
            self.workflow.index("Detect meaningful public release changes"):
            self.workflow.index("Upload inactive static slot and immutable runtime")
        ]
        upload = self.workflow[
            self.workflow.index("Upload inactive static slot and immutable runtime"):
            self.workflow.index("Build public validation artifact")
        ]

        self.assertLess(install, validate)
        for dependency in (
            '"Pillow>=10.1,<12"',
            '"qrcode>=8,<9"',
            '"zxing-cpp>=2.3,<4"',
        ):
            self.assertIn(dependency, self.workflow)
        self.assertIn("scripts/build_member_contact_card.py", self.workflow)
        self.assertIn("scripts/test_build_member_contact_card.py", self.workflow)
        self.assertIn('member_contact_card="$RUNNER_TEMP/member-contact-card.jpg"', materialize)
        self.assertIn('--source "$legacy_contact_card"', materialize)
        self.assertIn('--output "$member_contact_card"', materialize)
        self.assertIn("--forbid-profile-private-for admin-a", materialize)
        self.assertIn(
            "--forbid-profile-private-for admin-a@users.portal.example.invalid",
            materialize,
        )
        self.assertIn('rm -f "$legacy_contact_card"', materialize)
        self.assertIn('test ! -e "$legacy_contact_card"', materialize)
        self.assertIn("test ! -e _neutral_site/assets/contact-card.jpg", build)
        self.assertIn("--build-contract scripts/build_member_contact_card.py", delta)
        self.assertIn('--build-contract "$RUNNER_TEMP/member-contact-card.jpg"', delta)
        self.assertIn('--member-contact-card "$RUNNER_TEMP/member-contact-card.jpg"', upload)
        self.assertIn(
            "NEUTRAL_OPERATION: ${{ steps.operation.outputs.operation }}",
            upload,
        )
        self.assertIn('if [ "$NEUTRAL_OPERATION" = "locale-shadow" ]; then', upload)
        self.assertIn("private_asset_args+=(--skip-shared-private-assets)", upload)
        self.assertIn('"${private_asset_args[@]}"', upload)

        artifact = self.workflow[
            self.workflow.index("Build public validation artifact"):
            self.workflow.index("Upload release validation artifact")
        ]
        self.assertNotIn("member-contact-card.jpg", artifact)

    def test_cutover_proves_portal_runtime_and_canonical_routes(self) -> None:
        cutover = self.workflow[self.workflow.index("  cutover:\n"):]
        route_context = cutover.index("Prepare masked live route context")
        route_verify = cutover.index("Prove live release is unchanged before cutover")
        capability_gate = cutover.index("Require live Portal Worker locale search capability")
        edge_prepare = cutover.index("Prepare neutral edge runtime")
        self.assertLess(route_context, route_verify)
        self.assertLess(route_verify, capability_gate)
        self.assertLess(capability_gate, edge_prepare)
        self.assertIn("printf 'SITE_HOST=%s\\n'", cutover)
        self.assertIn("printf 'EDGE_ALIAS_HOSTS=%s\\n'", cutover)
        self.assertIn("printf 'LIVE_ORIGIN=%s\\n'", cutover)
        self.assertIn("python3 -B scripts/edge_route_cutover.py verify", cutover)
        self.assertGreaterEqual(cutover.count("api/health?runtime-data=1"), 2)
        self.assertIn('runtime.get("release_id") != os.environ["STATIC_RELEASE"]', cutover)
        self.assertIn('runtime.get("catalog_versioned") is not True', cutover)
        self.assertIn('runtime.get("rules_versioned") is not True', cutover)
        self.assertIn('runtime.get("release_id") != os.environ["PREVIOUS_STATIC_RELEASE"]', cutover)
        capability = cutover[capability_gate:edge_prepare]
        self.assertIn(
            "if: needs.prepare_release.outputs.multilingual_enabled == 'true'",
            capability,
        )
        self.assertIn('"$LIVE_ORIGIN/api/health"', capability)
        self.assertIn('capabilities.get("hot_report_locale_ids_v1") is not True', capability)

    def test_destructive_and_nontransactional_tail_actions_are_absent(self) -> None:
        self.assertIn('CATALOG_PDF_CLEANUP_ENABLED: "false"', self.workflow)
        for forbidden in (
            "--enable-pdf-cleanup",
            "api/hot-reports",
            "build_report_chat_index.py",
            "build_report_research_index.py",
            "submit_portal_indexnow.py",
            "commit_output_dir.sh",
            "Prune obsolete legacy static releases",
            "edge_route_cutover.py migrate",
            "edge_route_cutover.py rollback",
            "cache_purge",
        ):
            self.assertNotIn(forbidden, self.workflow)

    def test_all_production_mutators_share_one_non_cancelling_lock(self) -> None:
        workflows = (
            WORKFLOW,
            ROOT / ".github/workflows/portal-worker-emergency-deploy.yml",
            ROOT / ".github/workflows/manual-edge-canonical-redirect-hotfix.yml",
            ROOT / ".github/workflows/manual-cloudflare-url-cache-purge.yml",
        )
        for path in workflows:
            body = path.read_text(encoding="utf-8")
            self.assertIn("group: portal-production-release", body, path.name)
            self.assertIn("cancel-in-progress: false", body, path.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
