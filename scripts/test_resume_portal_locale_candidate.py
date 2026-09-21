#!/usr/bin/env python3
"""No-network resume proof using in-memory GitHub and R2 fixtures."""
from __future__ import annotations

import copy
import hashlib
import io
import json
import random
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, call, patch
from urllib.error import HTTPError
import zipfile

import publish_static_slot as publisher
from check_portal_app_budget import check_budget
import resume_portal_locale_candidate as resume
import verify_portal_chinese_parity as parity
import verify_portal_locale_routes as locale_routes
from test_publish_static_slot import FakeR2


REPO = "example/repository"
ORIGIN = "https://portal.example.invalid"
COMMIT = "1" * 40
RELEASE = "2" * 32
APP = b"console.log('Chinese app remains unchanged');"
PREVIOUS_FILES = {"assets/app.js": {"size": len(APP), "sha256": hashlib.sha256(APP).hexdigest(),
                                  "content_type": "application/json", "cache_control": "public, max-age=0, must-revalidate"}}
PREVIOUS = {"schema_version": 1, "slot": "a", "release_id": "3" * 32,
            "tree_sha256": resume.static_tree_sha256(PREVIOUS_FILES)}


def encoded(value):
    return publisher.json_bytes(value)


class FakeGitHub:
    def __init__(self, run, jobs, logs, diagnostics):
        self.run, self.jobs, self.logs = run, jobs, logs
        self.diagnostics = diagnostics
        self.artifact_name = "neutral-translation-diagnostics-321-1"
        self.archive_extra = {}

    def json(self, path):
        if path.endswith("/attempts/1"):
            return self.run
        if "/jobs?" in path:
            return {"jobs": self.jobs}
        if "/artifacts?" in path:
            return {"artifacts": [{"id": 99, "name": self.artifact_name, "expired": False, "workflow_run": {"id": 321}}]}
        raise AssertionError(path)

    def bytes(self, path):
        if path.endswith("/jobs/123/logs"):
            return self.logs.encode()
        if path.endswith("/artifacts/99/zip"):
            output = io.BytesIO()
            with zipfile.ZipFile(output, "w") as archive:
                for name, body in {**self.diagnostics, **self.archive_extra}.items():
                    archive.writestr(name, body)
            return output.getvalue()
        raise AssertionError(path)


class ResumeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.work = Path(self.temporary.name).resolve()
        self.site = self.work / "site"
        self.diag = self.work / "diagnostics"
        (self.work / "previous-edge-state.json").write_bytes(encoded(PREVIOUS))
        self.r2 = FakeR2()
        files = {name: b"public file" for name in resume.PUBLIC_PATHS}
        app = APP
        files["assets/app.js"] = app
        for locale in resume.LOCALES:
            for path in ("index.html", "blog/index.html", "blog/new.html", "reports/index.html", "reports/new.html", "charts.html"):
                files[locale + "/" + path] = ("locale page " + path).encode()
                files[path] = ("Chinese page " + path).encode()
        files["blog/historical.html"] = b"historical content must not be downloaded"
        for name in publisher.DEFAULT_RUNTIME_PATHS:
            files.setdefault(name, b"{}")
        locale_manifest = {"schema_version": 1, "quality_gate_version": 3, "locales": list(resume.LOCALES),
                           "coverage": {locale: 1 for locale in resume.LOCALES}, "html_page_count": 6,
                           "translation_scope": "incremental", "index_policy": {"mode": "incremental-publication-cutoff"},
                           "required_paths": ["data/i18n/ko/overlay.json"]}
        files["data/i18n/manifest.json"] = encoded(locale_manifest)
        files["data/i18n/ko/overlay.json"] = b"{}"
        def descriptor(body):
            return {"size": len(body), "sha256": hashlib.sha256(body).hexdigest(),
                    "content_type": "application/json", "cache_control": "public, max-age=0, must-revalidate"}
        entries = {name: descriptor(body) for name, body in files.items()}
        for name, body in files.items():
            self.r2.objects[publisher.slot_prefix("b") + name] = {"body": body, "metadata": {"sha256": entries[name]["sha256"]}}
        runtime_entries = {}
        for path in publisher.DEFAULT_RUNTIME_PATHS:
            name = Path(path).name
            row = {**descriptor(files[path]), "cache_control": "no-store"}
            runtime_entries[name] = row
            self.r2.objects[publisher.runtime_release_prefix(RELEASE) + name] = {
                "body": files[path], "metadata": {"sha256": row["sha256"], "release-id": RELEASE},
                "content_type": "application/json", "cache_control": "no-store"}
        runtime = {"schema_version": 1, "release_id": RELEASE, "prefix": publisher.runtime_release_prefix(RELEASE),
                   "tree_sha256": publisher.runtime_tree_sha256(runtime_entries), "files": runtime_entries, "file_count": len(runtime_entries)}
        self.r2.objects[publisher.runtime_manifest_key(RELEASE)] = {"body": encoded(runtime)}
        self.tree = resume.static_tree_sha256(entries)
        self.manifest = {"schema_version": 1, "slot": "b", "release_id": RELEASE, "tree_sha256": self.tree,
                         "file_count": len(entries), "total_bytes": sum(row["size"] for row in entries.values()), "files": entries,
                         "runtime_data": {key: runtime[key] for key in ("schema_version", "release_id", "prefix", "tree_sha256")}}
        self.save_manifest()
        self.previous_manifest = {**PREVIOUS, "file_count": len(PREVIOUS_FILES), "files": copy.deepcopy(PREVIOUS_FILES),
                                  "total_bytes": len(app)}
        self.r2.objects[publisher.manifest_key("a")] = {"body": encoded(self.previous_manifest)}
        self.r2.objects[publisher.slot_prefix("a") + "assets/app.js"] = {
            "body": app, "metadata": {"sha256": hashlib.sha256(app).hexdigest()}}
        report = parity._with_digest({"schema_version": 1, "kind": parity.VERIFY_KIND, "site_origin": ORIGIN,
                                      "snapshot_digest": "5" * 64, "verified_tree_digest": "6" * 64, "counts": {"files": len(files)}})
        # Production multilingual reports have this exact absolute-only shape:
        # passed, limits and no active/delta fields, with active_compared=false.
        performance = check_budget(app)
        diagnostics = {"locale-preflight-diagnostics.json": encoded({"status": "passed", "preflight_only": True}),
                       "locale-full-diagnostics.json": encoded({"schema_version": 1, "status": "passed", "ready": True}),
                       "chinese-parity.json": encoded(report), "chinese-performance.json": encoded(performance)}
        run = {"id": 321, "run_attempt": 1, "status": "completed", "conclusion": "failure", "head_branch": "main", "head_sha": COMMIT,
               "path": resume.WORKFLOW_PATH, "repository": {"full_name": REPO}, "head_repository": {"full_name": REPO}}
        steps = [{"name": name, "number": index, "conclusion": "success", "started_at": "2026-09-06T02:00:00Z"}
                 for index, name in enumerate(resume.REQUIRED_STEPS, 1)]
        steps.append({"name": resume.AUDIT_STEP, "number": 4, "conclusion": "failure"})
        job = {"id": 123, "name": "prepare_release", "status": "completed", "conclusion": "failure", "steps": steps}
        logs = "2026-09-06T01:00:00Z static_slot=a STATIC_RELEASE=" + "9" * 32 + "\n"
        logs += "2026-09-06T01:50:00Z " + json.dumps({"digest": report["digest"], "verified_tree_digest": report["verified_tree_digest"]}) + "\n"
        logs += "2026-09-06T01:50:00Z " + json.dumps(performance) + "\n"
        for name, value in {"NEUTRAL_OPERATION": "migrate", "static_slot": "b", "STATIC_RELEASE": RELEASE,
                            "STATIC_TREE_SHA256": self.tree, "CANDIDATE_COMMIT_SHA": COMMIT,
                            "ACTIVE_STATIC_SLOT": "a", "PREVIOUS_STATIC_RELEASE": PREVIOUS["release_id"]}.items():
            logs += f"2026-09-06T02:01:00.1234567Z   {name}: {value}\n"
        self.github = FakeGitHub(run, [job], logs, diagnostics)
        self.live = Mock(return_value=copy.deepcopy(PREVIOUS))

    def save_manifest(self):
        self.r2.objects[publisher.manifest_key("b")] = {"body": encoded(self.manifest)}

    def prepare_declared_locale_routes(self):
        from test_verify_portal_locale_routes import describe, fixture

        declared, responses = fixture()
        declared["lazy_javascript_assets"] = {}
        for language, prefix in [("zh-Hans", ""), *((locale, f"{locale}/") for locale in resume.LOCALES)]:
            path = prefix + "assets/newsfeed-app.js"
            body = f"export function initNewsfeedApp() {{ /* {language} */ }}".encode()
            declared["lazy_javascript_assets"][language] = describe(path, body)
            responses[ORIGIN + "/" + path] = (200, {}, body)
        path = locale_routes.DETAIL_PATH
        body = b"/* locale detail */"
        declared["detail_asset"] = describe(path, body)
        responses[ORIGIN + "/" + path] = (200, {}, body)

        def store(relative, body):
            descriptor = {"size": len(body), "sha256": hashlib.sha256(body).hexdigest(),
                          "content_type": "application/javascript" if relative.endswith(".js") else "text/html",
                          "cache_control": "public, max-age=0, must-revalidate"}
            self.manifest["files"][relative] = descriptor
            self.r2.objects[publisher.slot_prefix("b") + relative] = {
                "body": body, "metadata": {"sha256": descriptor["sha256"]}}

        for url, response in responses.items():
            relative = url.removeprefix(ORIGIN + "/")
            store(relative, response[2])
            if relative.endswith(".html"):
                store(relative.split("/", 1)[1], b"Chinese original application")
        manifest_path = "data/i18n/manifest.json"
        locale_manifest = json.loads(self.r2.objects[publisher.slot_prefix("b") + manifest_path]["body"])
        locale_manifest.update(declared)
        locale_manifest["html_page_count"] = 12
        store(manifest_path, encoded(locale_manifest))
        return locale_manifest, store

    def test_download_restores_all_declared_routes_for_the_local_live_contract_gate(self):
        manifest, _store = self.prepare_declared_locale_routes()
        self.r2.operations.clear()
        downloaded = resume.download_candidate_files(self.r2, "bucket", self.manifest, self.site, workers=1)
        expected_assets = {"assets/locale-recovery.js", "assets/locale-detail.js", "assets/newsfeed-app.js",
                           *(f"{locale}/assets/newsfeed-app.js" for locale in resume.LOCALES)}
        self.assertTrue(expected_assets.issubset(downloaded))
        with patch("verify_portal_locale_routes.subprocess.run", side_effect=AssertionError("No live HTTP")):
            report = locale_routes.verify_local_locale_routes(manifest, ORIGIN, self.site)
        self.assertEqual(report["status"], "passed")
        self.assertEqual((report["route_count"], report["asset_count"]), (18, 6))
        self.assertTrue(all(operation == "get" for operation, _key in self.r2.operations))

    def test_declared_asset_must_match_committed_size_and_hash_before_body_downloads(self):
        manifest, store = self.prepare_declared_locale_routes()
        original = copy.deepcopy(manifest)
        for field, value in (("sha256", "0" * 64), ("byte_size", 1)):
            with self.subTest(field=field):
                manifest = copy.deepcopy(original)
                manifest["lazy_javascript_assets"]["ar"][field] = value
                store("data/i18n/manifest.json", encoded(manifest))
                self.r2.operations.clear()
                with self.assertRaisesRegex(resume.ResumeError, "descriptor differs from the committed static manifest"):
                    resume.download_candidate_files(self.r2, "bucket", self.manifest, self.site, workers=1)
                self.assertEqual(self.r2.operations, [("get", publisher.slot_prefix("b") + "data/i18n/manifest.json")])

    def use_rolled_back_source(self):
        prepare = self.github.jobs[0]
        prepare["conclusion"] = "success"
        for step in prepare["steps"]:
            step["status"] = "completed"
            if step["name"] == "Verify isolated multilingual shadow worker":
                step["conclusion"] = "skipped"
        for number, name in enumerate(("Publish multilingual review identity", "Build public validation artifact",
                                       "Upload release validation artifact"), 5):
            prepare["steps"].append({"name": name, "number": number, "status": "completed", "conclusion": "success"})
        outcomes = (
            ("Download release validation artifact", "success"),
            ("Prove live release is unchanged before cutover", "success"),
            ("Capture exact edge rollback target", "success"),
            ("Verify committed candidate immediately before cutover", "success"),
            ("Deploy prepared neutral edge release", "success"),
            ("Accept prepared release through the live edge", "failure"),
            ("Roll back failed release or completed rehearsal", "success"),
            ("Verify exact previous release after rollback", "success"),
            ("Enforce transactional outcome", "failure"),
        )
        self.github.jobs.append({"id": 456, "name": "cutover", "status": "completed", "conclusion": "failure",
                                 "steps": [{"name": name, "number": number, "status": "completed", "conclusion": outcome}
                                           for number, (name, outcome) in enumerate(outcomes, 1)]})

    def test_completed_prepare_and_verified_rollback_restores_without_remote_mutation(self):
        self.use_rolled_back_source()
        result = self.restore()
        self.assertEqual(result["source_failure_phase"], "live_acceptance_rolled_back")
        self.assertEqual(result["source_cutover_job_id"], 456)
        self.assertIs(result["source_rollback_verified"], True)
        self.assertEqual(result["remote_mutations"], 0)
        self.assertEqual(result["verified_remote_objects"], self.manifest["file_count"])
        self.assertEqual(self.live.call_count, 2)
        self.assertTrue((self.site / "ko/blog/new.html").is_file())
        self.assertTrue(all(operation in {"head", "get"} for operation, _key in self.r2.operations))

    def test_rollback_source_rejects_each_missing_or_unsuccessful_gate_before_remote_reads(self):
        self.use_rolled_back_source()
        original = copy.deepcopy(self.github.jobs)
        for job_index, job in enumerate(original):
            for step_index, step in enumerate(job["steps"]):
                if step["name"] == "Verify isolated multilingual shadow worker":
                    continue  # A successful prepare may intentionally skip this isolated preview.
                for outcome in ("skipped", "cancelled", "timed_out", "success" if step["conclusion"] == "failure" else "failure"):
                    with self.subTest(step=step["name"], outcome=outcome):
                        self.github.jobs = copy.deepcopy(original)
                        self.github.jobs[job_index]["steps"][step_index]["conclusion"] = outcome
                        with self.assertRaises(resume.ResumeError):
                            self.restore()
                with self.subTest(missing_step=step["name"]):
                    self.github.jobs = copy.deepcopy(original)
                    del self.github.jobs[job_index]["steps"][step_index]
                    with self.assertRaises(resume.ResumeError):
                        self.restore()
        self.assertEqual(self.r2.operations, [])
        self.live.assert_not_called()

    def test_rollback_source_rejects_ambiguous_extra_or_out_of_order_failure_evidence(self):
        self.use_rolled_back_source()
        original = copy.deepcopy(self.github.jobs)
        def cutover(steps):
            return steps[1]["steps"]
        mutations = (
            lambda jobs: jobs.append(copy.deepcopy(jobs[1])),
            lambda jobs: jobs.append({"name": "other", "status": "completed", "conclusion": "failure"}),
            lambda jobs: jobs.append({"name": "other", "status": "in_progress", "conclusion": None}),
            lambda jobs: jobs.append({"name": "earlier_cutover", "status": "completed", "conclusion": "success"}),
            lambda jobs: jobs[1].update(conclusion="success"),
            lambda jobs: jobs[1].update(status="in_progress"),
            lambda jobs: jobs[1].update(id=True),
            lambda jobs: cutover(jobs).append({"name": "Extra failure", "number": 10, "status": "completed", "conclusion": "failure"}),
            lambda jobs: cutover(jobs).append({"name": "Accept prepared release through the live edge", "number": 10, "status": "completed", "conclusion": "failure"}),
            lambda jobs: cutover(jobs)[7].update(number=cutover(jobs)[6]["number"]),
            lambda jobs: cutover(jobs)[7].update(number=11),
            lambda jobs: cutover(jobs)[7].update(status="in_progress"),
            lambda jobs: jobs[0]["steps"][-1].update(number=0),
        )
        for index, mutate in enumerate(mutations):
            with self.subTest(index=index):
                self.github.jobs = copy.deepcopy(original)
                mutate(self.github.jobs)
                with self.assertRaises(resume.ResumeError):
                    self.restore()
        self.assertEqual(self.r2.operations, [])

    def test_rollback_source_still_requires_original_attempt_identity_and_unchanged_active_release(self):
        self.use_rolled_back_source()
        original = copy.deepcopy(self.github.run)
        for change in ({"head_branch": "feature"}, {"head_sha": "9" * 40}, {"run_attempt": 2},
                       {"conclusion": "success"}, {"repository": {"full_name": "other/repo"}}):
            with self.subTest(change=change):
                self.github.run = {**original, **change}
                with self.assertRaises(resume.ResumeError):
                    self.restore()
        self.github.run = original
        self.live.return_value = {**PREVIOUS, "release_id": "7" * 32}
        with self.assertRaisesRegex(resume.ResumeError, "changed"):
            self.restore()
        self.assertEqual(self.r2.operations, [])

    def test_rollback_source_does_not_relax_committed_manifest_integrity(self):
        self.use_rolled_back_source()
        self.manifest["files"]["index.html"]["sha256"] = "0" * 64
        self.save_manifest()
        with self.assertRaisesRegex(resume.ResumeError, "tree digest"):
            self.restore()
        self.assertFalse((self.work / "locale-resume-identity.json").exists())

    def test_download_accepts_only_accounted_source_fallbacks(self):
        from test_portal_locale_manifest import with_source_fallback

        path = "data/i18n/manifest.json"
        object_key = publisher.slot_prefix("b") + path
        payload = with_source_fallback(json.loads(self.r2.objects[object_key]["body"]))

        def save_payload():
            body = encoded(payload)
            self.r2.objects[object_key]["body"] = body
            self.manifest["files"][path].update(size=len(body), sha256=hashlib.sha256(body).hexdigest())

        save_payload()
        restored = resume.download_candidate_files(self.r2, "bucket", self.manifest, self.site, workers=1)
        self.assertIn(path, restored)
        payload["source_fallbacks"]["counts"]["ko"] = 2
        save_payload()
        with self.assertRaisesRegex(resume.ResumeError, "source fallback count differs"):
            resume.download_candidate_files(self.r2, "bucket", self.manifest, self.site, workers=1)

    def test_candidate_download_uses_shared_manifest_schema_and_finite_size_contract(self):
        path = "data/i18n/manifest.json"
        object_key = publisher.slot_prefix("b") + path
        original = json.loads(self.r2.objects[object_key]["body"])
        def save_payload(payload):
            body = encoded(payload)
            self.r2.objects[object_key]["body"] = body
            self.manifest["files"][path].update(size=len(body), sha256=hashlib.sha256(body).hexdigest())
        save_payload({**original, "diagnostic_padding": "x" * (3 * 1024 * 1024)})
        restored = resume.download_candidate_files(self.r2, "bucket", self.manifest, self.site, workers=1)
        self.assertIn(path, restored)
        for payload in ({**original, "schema_version": 2},
                        {**original, "diagnostic_padding": "x" * (17 * 1024 * 1024)}):
            with self.subTest(schema=payload["schema_version"], oversized="diagnostic_padding" in payload):
                save_payload(payload)
                with self.assertRaisesRegex(resume.ResumeError, "locale manifest is invalid"):
                    resume.download_candidate_files(self.r2, "bucket", self.manifest, self.site, workers=1)

    def restore(self, **kwargs):
        options = dict(github=self.github, client=self.r2, bucket="bucket", repository=REPO, run_id=321, run_attempt=1,
                       site_dir=self.site, diagnostics_dir=self.diag, work_dir=self.work, origin=ORIGIN,
                       expected_slot="b", expected_release=RELEASE, expected_tree=self.tree, expected_commit=COMMIT,
                       expected_previous_release=PREVIOUS["release_id"], expected_previous_tree=PREVIOUS["tree_sha256"],
                       fetch_live=self.live, workers=4)
        return resume.resume_candidate(**{**options, **kwargs})

    def test_complete_restore_verifies_all_metadata_downloads_only_audit_files_and_never_mutates_remote(self):
        result = self.restore()
        self.assertEqual(result["source_failure_phase"], "shadow_http_audit")
        self.assertEqual(result["static_release"], RELEASE)
        self.assertEqual(result["verified_remote_objects"], self.manifest["file_count"])
        self.assertEqual(result["remote_mutations"], 0)
        self.assertEqual(self.live.call_count, 2)
        self.assertTrue((self.site / "blog/new.html").is_file())
        self.assertFalse((self.site / "blog/historical.html").exists())
        self.assertTrue((self.work / "locale-resume-identity.json").is_file())
        self.assertTrue((self.work / "chinese-parity.json").is_file())
        self.assertTrue(all(operation in {"head", "get"} for operation, _key in self.r2.operations))
        self.assertIn(("head", publisher.slot_prefix("b") + "blog/historical.html"), self.r2.operations)
        self.assertNotIn(("get", publisher.slot_prefix("b") + "blog/historical.html"), self.r2.operations)

    def test_absolute_only_producer_report_gets_a_fresh_pinned_baseline_comparison_before_bulk_reads(self):
        result = self.restore()
        comparison = json.loads((self.work / "chinese-recovery-performance.json").read_bytes())
        expected = {**check_budget(APP, APP), "baseline_slot": PREVIOUS["slot"],
                    "baseline_release_id": PREVIOUS["release_id"], "baseline_tree_sha256": PREVIOUS["tree_sha256"],
                    "source_active_compared": False}
        self.assertEqual(comparison, expected)
        self.assertFalse(result["source_performance_active_compared"])
        self.assertTrue(result["performance_comparison"]["active_compared"])
        source = self.github.diagnostics["chinese-performance.json"]
        self.assertEqual((self.work / "chinese-performance.json").read_bytes(), source)
        reads = self.r2.operations
        self.assertLess(reads.index(("get", publisher.slot_prefix("a") + "assets/app.js")),
                        reads.index(("head", publisher.slot_prefix("b") + "blog/historical.html")))

    def test_existing_compared_source_report_still_requires_exact_previous_app_evidence(self):
        self.github.diagnostics["chinese-performance.json"] = encoded(check_budget(APP, APP))
        result = self.restore()
        self.assertTrue(result["source_performance_active_compared"])

    def test_shrinking_candidate_can_compare_against_a_larger_legacy_baseline(self):
        active = b"legacy bundle" * 60_000
        self.assertGreater(len(active), 700_000)
        descriptor = self.previous_manifest["files"]["assets/app.js"]
        descriptor.update(size=len(active), sha256=hashlib.sha256(active).hexdigest())
        self.previous_manifest.update(tree_sha256=resume.static_tree_sha256(self.previous_manifest["files"]),
                                      total_bytes=len(active))
        previous = {field: self.previous_manifest[field] for field in PREVIOUS}
        self.r2.objects[publisher.manifest_key("a")] = {"body": encoded(self.previous_manifest)}
        self.r2.objects[publisher.slot_prefix("a") + "assets/app.js"] = {
            "body": active, "metadata": {"sha256": descriptor["sha256"]}}
        (self.work / "previous-edge-state.json").write_bytes(encoded(previous))
        self.live.return_value = previous
        result = self.restore(expected_previous_tree=previous["tree_sha256"])
        self.assertEqual(result["performance_comparison"], check_budget(APP, active))
        self.assertEqual(result["performance_comparison"]["status"], "passed")

    def test_changed_previous_manifest_at_completion_never_emits_resume_identity(self):
        original_get = self.r2.get_object
        count = 0
        def changed_get(**kwargs):
            nonlocal count
            if kwargs["Key"] == publisher.manifest_key("a"):
                count += 1
                if count == 2:
                    changed = {**self.previous_manifest, "release_id": "9" * 32}
                    return {"Body": io.BytesIO(encoded(changed))}
            return original_get(**kwargs)
        with patch.object(self.r2, "get_object", side_effect=changed_get):
            with self.assertRaisesRegex(resume.ResumeError, "Pinned slot manifest identity"):
                self.restore()
        self.assertFalse((self.work / "locale-resume-identity.json").exists())

    def test_pinned_reads_bound_and_close_r2_streams_even_on_failure(self):
        streams = []
        original_get = self.r2.get_object
        def tracked_get(**kwargs):
            response = original_get(**kwargs)
            streams.append(response["Body"])
            return response
        with patch.object(self.r2, "get_object", side_effect=tracked_get):
            manifest = resume.read_pinned_manifest(self.r2, "bucket", PREVIOUS)
            self.assertEqual(resume.read_pinned_app(self.r2, "bucket", manifest), APP)
        self.assertTrue(all(stream.closed for stream in streams))
        oversized = io.BytesIO(b"x" * 33)
        with patch("verify_prepared_static_slot.MAX_COMMITTED_MANIFEST_BYTES", 32), \
             patch.object(self.r2, "get_object", return_value={"Body": oversized}):
            with self.assertRaisesRegex(resume.ResumeError, "byte size bound"):
                resume.read_pinned_manifest(self.r2, "bucket", PREVIOUS)
        self.assertTrue(oversized.closed)
        corrupted = io.BytesIO(b"x" * (len(APP) + 1))
        with patch.object(self.r2, "get_object", return_value={"Body": corrupted}):
            with self.assertRaisesRegex(resume.ResumeError, "byte size bound"):
                resume.read_pinned_app(self.r2, "bucket", self.previous_manifest)
        self.assertTrue(corrupted.closed)
        manifest = copy.deepcopy(self.previous_manifest)
        manifest["files"]["assets/app.js"]["size"] = resume.MAX_APP_BUNDLE_BYTES + 1
        with patch.object(self.r2, "get_object") as getter:
            with self.assertRaisesRegex(resume.ResumeError, "exceeds its bound"):
                resume.read_pinned_app(self.r2, "bucket", manifest)
        getter.assert_not_called()

    def test_source_performance_cannot_claim_pass_with_tampered_candidate_or_comparison(self):
        original = check_budget(APP)
        for change in ({"candidate_sha256": "0" * 64}, {"candidate_bytes": 1}, {"status": "failed"},
                       {"violations": ["absolute loading budget"]}, {"active_compared": None},
                       {"raw_delta_bytes": 0}, {"limits": {}}, {"active_compared": True}):
            with self.subTest(change=change):
                self.github.diagnostics["chinese-performance.json"] = encoded({**original, **change})
                self.r2.operations.clear()
                with self.assertRaisesRegex(resume.ResumeError, "Chinese performance"):
                    self.restore()
                self.assertFalse(any(key.endswith("/ko/blog/new.html") for _operation, key in self.r2.operations))
                self.assertFalse((self.work / "locale-resume-identity.json").exists())

    def test_fresh_comparison_rejects_raw_and_gzip_delta_before_bulk_download(self):
        for candidate in (b"a" * 24_100, random.Random(13).randbytes(6500)):
            with self.subTest(size=len(candidate)):
                # Both source checks pass absolute budgets, but not the fresh
                # comparison to the much smaller committed previous bundle.
                self.assertEqual(check_budget(candidate)["status"], "passed")
                descriptor = self.manifest["files"]["assets/app.js"]
                descriptor.update(size=len(candidate), sha256=hashlib.sha256(candidate).hexdigest())
                self.r2.objects[publisher.slot_prefix("b") + "assets/app.js"] = {
                    "body": candidate, "metadata": {"sha256": descriptor["sha256"]}}
                old_tree = self.tree
                self.tree = resume.static_tree_sha256(self.manifest["files"])
                self.manifest.update(tree_sha256=self.tree, total_bytes=sum(row["size"] for row in self.manifest["files"].values()))
                self.github.logs = self.github.logs.replace(old_tree, self.tree) + "\n" + descriptor["sha256"]
                self.github.diagnostics["chinese-performance.json"] = encoded(check_budget(candidate))
                self.save_manifest()
                self.r2.operations.clear()
                with self.assertRaisesRegex(resume.ResumeError, "Fresh Chinese performance comparison did not pass.*delta"):
                    self.restore()
                self.assertFalse(any(key.endswith("/ko/blog/new.html") for _operation, key in self.r2.operations))

    def test_previous_manifest_identity_tree_and_app_bytes_are_verified_before_bulk_download(self):
        original = copy.deepcopy(self.r2.objects)
        for mutation in ("release", "tree", "descriptor", "app"):
            with self.subTest(mutation=mutation):
                self.r2.objects = copy.deepcopy(original)
                manifest = copy.deepcopy(self.previous_manifest)
                if mutation == "release":
                    manifest["release_id"] = "9" * 32
                elif mutation == "tree":
                    manifest["tree_sha256"] = "9" * 64
                elif mutation == "descriptor":
                    manifest["files"]["assets/app.js"]["sha256"] = "9" * 64
                else:
                    self.r2.objects[publisher.slot_prefix("a") + "assets/app.js"]["body"] = b"x" * len(APP)
                self.r2.objects[publisher.manifest_key("a")] = {"body": encoded(manifest)}
                self.r2.operations.clear()
                with self.assertRaisesRegex(resume.ResumeError, "Pinned"):
                    self.restore()
                self.assertFalse(any(key.endswith("/ko/blog/new.html") for _operation, key in self.r2.operations))

    def test_run_requires_same_repo_main_failed_attempt_and_successful_prerequisites(self):
        changes = ({"head_branch": "feature"}, {"head_sha": "9" * 40}, {"conclusion": "success"},
                   {"head_repository": {"full_name": "other/repo"}}, {"run_attempt": 2}, {"path": "other.yml"})
        original = copy.deepcopy(self.github.run)
        for change in changes:
            with self.subTest(change=change):
                self.github.run = {**original, **change}
                with self.assertRaises(resume.ResumeError):
                    self.restore()
        self.github.run = original
        self.github.jobs[0]["steps"][0]["conclusion"] = "failure"
        with self.assertRaisesRegex(resume.ResumeError, "prerequisite"):
            self.restore()
        self.assertEqual(self.r2.operations, [])

    def test_active_or_changed_baseline_is_rejected_before_remote_reads(self):
        with self.assertRaisesRegex(resume.ResumeError, "active slot"):
            self.restore(expected_slot="a")
        self.live.return_value = {**PREVIOUS, "release_id": "7" * 32}
        with self.assertRaisesRegex(resume.ResumeError, "changed"):
            self.restore()
        self.assertEqual(self.r2.operations, [])

    def test_non_migrate_or_wrong_identity_cannot_resume(self):
        self.github.logs = self.github.logs.replace("NEUTRAL_OPERATION: migrate", "NEUTRAL_OPERATION: locale-shadow")
        with self.assertRaisesRegex(resume.ResumeError, "migrate"):
            self.restore()

    def test_incomplete_marker_or_extra_objects_or_wrong_metadata_are_rejected(self):
        key = publisher.incomplete_key("b")
        self.r2.objects[key] = {"body": b"null"}
        with self.assertRaisesRegex(resume.ResumeError, "incomplete"):
            self.restore()
        del self.r2.objects[key]
        extra = publisher.slot_prefix("b") + "extra.txt"
        self.r2.objects[extra] = {"body": b"extra"}
        with self.assertRaisesRegex(resume.ResumeError, "object tree"):
            self.restore()
        del self.r2.objects[extra]
        self.r2.objects[publisher.slot_prefix("b") + "blog/historical.html"]["metadata"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(resume.ResumeError, "metadata"):
            self.restore()

    def test_descriptor_tree_and_downloaded_bytes_are_both_verified(self):
        self.manifest["files"]["index.html"]["sha256"] = "0" * 64
        self.save_manifest()
        with self.assertRaisesRegex(resume.ResumeError, "tree digest"):
            self.restore()

    def test_same_size_corruption_during_get_is_rejected(self):
        original_get = self.r2.get_object
        def changed_get(**kwargs):
            value = original_get(**kwargs)
            if kwargs["Key"].endswith("/ko/blog/new.html"):
                body = value["Body"].read()
                value["Body"] = io.BytesIO(b"x" * len(body))
            return value
        with patch.object(self.r2, "get_object", side_effect=changed_get):
            with self.assertRaisesRegex(resume.ResumeError, "downloaded file"):
                self.restore()

    def test_diagnostics_must_be_exact_attempt_safe_and_ready(self):
        self.github.artifact_name = "neutral-translation-diagnostics-321-2"
        with self.assertRaisesRegex(resume.ResumeError, "artifact"):
            self.restore()
        self.github.artifact_name = "neutral-translation-diagnostics-321-1"
        self.github.archive_extra = {"../escape.json": b"{}"}
        with self.assertRaisesRegex(resume.ResumeError, "archive"):
            self.restore()
        self.github.archive_extra = {}
        self.github.diagnostics["locale-full-diagnostics.json"] = encoded({"status": "passed", "ready": False})
        with self.assertRaisesRegex(resume.ResumeError, "not ready"):
            self.restore()

    def test_live_change_during_restore_does_not_emit_resume_identity(self):
        self.live.side_effect = [PREVIOUS, {**PREVIOUS, "release_id": "9" * 32}]
        with self.assertRaisesRegex(resume.ResumeError, "during candidate restore"):
            self.restore()
        self.assertFalse((self.work / "locale-resume-identity.json").exists())


class CandidateReadRetryTests(unittest.TestCase):
    BODY = b"committed candidate object"
    KEY = "edge-static/slots/b/ko/blog/new.html"

    def descriptor(self):
        return {"size": len(self.BODY), "sha256": hashlib.sha256(self.BODY).hexdigest()}

    @staticmethod
    def read_error(code):
        error = RuntimeError("injected object read error")
        error.response = {"Error": {"Code": code}}
        return error

    @patch.object(resume.time, "sleep")
    def test_service_unavailable_and_slowdown_retry_then_succeed(self, sleep):
        for code in ("ServiceUnavailable", "SlowDown"):
            with self.subTest(code=code):
                sleep.reset_mock()
                stream = io.BytesIO(self.BODY)
                client = Mock()
                client.get_object.side_effect = [self.read_error(code), self.read_error(code), {"Body": stream}]
                self.assertEqual(resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor()), self.BODY)
                self.assertEqual(client.get_object.call_count, 3)
                self.assertEqual(sleep.call_args_list, [call(2), call(5)])
                self.assertTrue(stream.closed)

    @patch.object(resume.time, "sleep")
    def test_access_denied_and_no_such_key_never_retry(self, sleep):
        for code in ("AccessDenied", "NoSuchKey"):
            with self.subTest(code=code):
                client = Mock()
                client.get_object.side_effect = self.read_error(code)
                with self.assertRaisesRegex(resume.ResumeError, "Candidate object read failed"):
                    resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor())
                client.get_object.assert_called_once_with(Bucket="bucket", Key=self.KEY)
        sleep.assert_not_called()

    @patch.object(resume.time, "sleep")
    def test_hash_mismatch_never_retries_and_closes_stream(self, sleep):
        stream = io.BytesIO(b"x" * len(self.BODY))
        client = Mock()
        client.get_object.return_value = {"Body": stream}
        with self.assertRaisesRegex(resume.ResumeError, "differs from manifest"):
            resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor())
        self.assertEqual(client.get_object.call_count, 1)
        self.assertTrue(stream.closed)
        sleep.assert_not_called()

    @patch.object(resume.time, "sleep")
    def test_successful_stream_is_closed_without_wait(self, sleep):
        stream = io.BytesIO(self.BODY)
        client = Mock()
        client.get_object.return_value = {"Body": stream}
        self.assertEqual(resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor()), self.BODY)
        self.assertTrue(stream.closed)
        sleep.assert_not_called()

    @patch.object(resume.time, "sleep")
    def test_nonretryable_stream_failure_is_closed(self, sleep):
        stream = Mock()
        stream.read.side_effect = ValueError("malformed stream")
        client = Mock()
        client.get_object.return_value = {"Body": stream}
        with self.assertRaisesRegex(resume.ResumeError, "ValueError"):
            resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor())
        stream.close.assert_called_once_with()
        self.assertEqual(client.get_object.call_count, 1)
        sleep.assert_not_called()

    @patch.object(resume.time, "sleep")
    def test_transient_stream_is_closed_before_backoff_and_next_attempt(self, sleep):
        failed_stream = Mock()
        failed_stream.read.side_effect = self.read_error("ServiceUnavailable")
        good_stream = io.BytesIO(self.BODY)
        client = Mock()
        client.get_object.side_effect = [{"Body": failed_stream}, {"Body": good_stream}]
        sleep.side_effect = lambda _delay: failed_stream.close.assert_called_once_with()
        self.assertEqual(resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor()), self.BODY)
        failed_stream.close.assert_called_once_with()
        self.assertTrue(good_stream.closed)
        sleep.assert_called_once_with(2)

    @patch.object(resume.time, "sleep")
    def test_retry_exhaustion_has_six_attempts_and_bounded_waits(self, sleep):
        client = Mock()
        client.get_object.side_effect = self.read_error("SlowDown")
        with self.assertRaisesRegex(resume.ResumeError, "code=slowdown"):
            resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor())
        self.assertEqual(client.get_object.call_count, 6)
        self.assertEqual(sleep.call_args_list, [call(2), call(5), call(10), call(20), call(30)])

    @patch.object(resume.time, "sleep")
    def test_retry_exhaustion_closes_every_failed_stream(self, sleep):
        streams = [Mock() for _ in range(6)]
        for stream in streams:
            stream.read.side_effect = self.read_error("ServiceUnavailable")
        client = Mock()
        client.get_object.side_effect = [{"Body": stream} for stream in streams]
        with self.assertRaisesRegex(resume.ResumeError, "code=serviceunavailable"):
            resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor())
        for stream in streams:
            stream.close.assert_called_once_with()
        self.assertEqual(client.get_object.call_count, 6)
        self.assertEqual(sleep.call_count, 5)


class ReadTransportTests(unittest.TestCase):
    def test_github_user_agent_identifies_the_resume_client(self):
        client = resume.GitHubClient("private-test-token")
        client.opener = Mock()
        client.opener.open.return_value = io.BytesIO(b"{}")
        self.assertEqual(client.json("/repos/example/repository/actions/runs/321"), {})
        request = client.opener.open.call_args.args[0]
        self.assertEqual(request.get_header("User-agent"), "Portal-Locale-Resume/1.0")
        self.assertEqual(request.get_header("Authorization"), "Bearer private-test-token")

    def test_github_forbidden_error_names_safe_api_route_and_json_message(self):
        client = resume.GitHubClient("private-test-token")
        error = HTTPError(
            "https://signed-download.example.invalid/data?signature=SECRET",
            403, "Forbidden", {"X-Private": "header-secret"}, io.BytesIO(encoded({
                "message": "Resource not accessible by integration. private-test-token\n"
                           "https://signed-download.example.invalid/data?signature=SECRET ghp_other_private_token",
                "headers": {"X-Private": "header-secret"},
            })),
        )
        client.opener = Mock()
        client.opener.open.side_effect = error
        with self.assertRaises(resume.ResumeError) as captured:
            client.bytes("/repos/example/repository/actions/jobs/123/logs?private-query=omitted")
        text = str(captured.exception)
        self.assertIn("route=/repos/example/repository/actions/jobs/123/logs status=403", text)
        self.assertIn("Resource not accessible by integration", text)
        for secret in ("private-test-token", "ghp_other_private_token", "signed-download", "signature", "SECRET", "header-secret", "private-query", "\n"):
            self.assertNotIn(secret, text)

    def test_non_json_github_error_does_not_print_download_body_or_url(self):
        client = resume.GitHubClient("test-token")
        client.opener = Mock()
        client.opener.open.side_effect = HTTPError("https://signed.invalid/?secret=value", 403, "Forbidden", {}, io.BytesIO(b"<Error>private XML</Error>"))
        with self.assertRaisesRegex(resume.ResumeError, r"route=/repos/example/repository/actions/artifacts/99/zip status=403$"):
            client.bytes("/repos/example/repository/actions/artifacts/99/zip")

    @patch.object(resume, "request_status")
    def test_live_identity_uses_existing_curl_get_reader(self, reader):
        body = encoded(PREVIOUS)
        reader.return_value = (200, {"content-length": str(len(body))}, body)
        self.assertEqual(resume.live_state(ORIGIN), PREVIOUS)
        reader.assert_called_once_with(ORIGIN + "/.well-known/edge-state", method="GET", headers={"Cache-Control": "no-cache"})

    @patch.object(resume, "request_status")
    def test_live_identity_rejects_redirect_timeout_truncation_and_oversized_length(self, reader):
        for response in ((302, {}, encoded(PREVIOUS)), (0, {}, b""), (403, {}, b"denied"),
                         (200, {}, b" " * 65536), (200, {"content-length": "65537"}, encoded(PREVIOUS))):
            with self.subTest(status=response[0], size=len(response[2])):
                reader.return_value = response
                with self.assertRaises(resume.ResumeError):
                    resume.live_state(ORIGIN)

    @patch.object(resume, "request_status")
    def test_live_identity_still_requires_bare_https_origin(self, reader):
        for origin in ("http://example.invalid", "https://name:secret@example.invalid", ORIGIN + "/other", ORIGIN + "?query=1"):
            with self.subTest(origin=origin), self.assertRaises(resume.ResumeError):
                resume.live_state(origin)
        reader.assert_not_called()

    def test_phase_progress_is_flushed(self):
        with patch("builtins.print") as output:
            resume.phase("source_attempt")
        output.assert_called_once_with("Locale resume phase=source_attempt", flush=True)


if __name__ == "__main__":
    unittest.main()
