#!/usr/bin/env python3
"""No-network resume proof using in-memory GitHub and R2 fixtures."""
from __future__ import annotations

import copy
import base64
from collections import Counter
import hashlib
import io
import json
import random
from pathlib import Path
import tempfile
import threading
import unittest
import weakref
from unittest.mock import Mock, call, patch
from urllib.error import HTTPError
from urllib.request import Request
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
            return {"artifacts": [{"id": 99, "name": self.artifact_name, "expired": False,
                                   "size_in_bytes": len(self.archive()), "workflow_run": {"id": 321}}]}
        raise AssertionError(path)

    def archive(self):
        output = io.BytesIO()
        with zipfile.ZipFile(output, "w") as archive:
            for name, body in {**self.diagnostics, **self.archive_extra}.items():
                archive.writestr(name, body)
        return output.getvalue()

    def bytes(self, path):
        if path.endswith("/jobs/123/logs"):
            return self.logs.encode()
        raise AssertionError(path)

    def artifact_bytes(self, path, *, size_in_bytes):
        if path.endswith("/artifacts/99/zip"):
            body = self.archive()
            assert len(body) <= size_in_bytes
            return body
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

    def test_old_candidate_restores_chart_index_for_new_public_acceptance_gate(self):
        from compare_portal_release_semantics import COMPONENT_KEYS, digest, stable_value
        from verify_public_chart_index import main as chart_gate

        chart_path = "data/chart_search_index.json"
        index = {"schema_version": 1, "report_count": 1, "item_count": 1, "reports": [
            {"report_id": "original-report", "chart_count": 1, "charts": [
                {"image_id": "a" * 64, "description": "unchanged original chart"}]}]}
        components = dict.fromkeys(COMPONENT_KEYS, "0" * 64)
        components["chart_search_index"] = digest(stable_value(index))
        semantics = {"schema_version": 1, "normalizer_version": 1, "components": components,
                     "semantic_sha256": digest(components)}
        for relative, value in ((chart_path, index), ("data/release-semantics.json", semantics)):
            body = encoded(value)
            descriptor = {**self.manifest["files"][relative], "size": len(body),
                          "sha256": hashlib.sha256(body).hexdigest()}
            self.manifest["files"][relative] = descriptor
            self.r2.objects[publisher.slot_prefix("b") + relative] = {
                "body": body, "metadata": {"sha256": descriptor["sha256"]}}
        self.r2.operations.clear()
        downloaded = resume.download_candidate_files(self.r2, "bucket", self.manifest, self.site, workers=1)
        self.assertIn(chart_path, downloaded)
        self.assertIn(("get", publisher.slot_prefix("b") + chart_path), self.r2.operations)
        self.assertEqual((self.site / chart_path).read_bytes(), encoded(index))
        self.assertTrue(all(operation == "get" for operation, _key in self.r2.operations))
        receipt = self.work / "chart-expected.json"
        self.assertEqual(chart_gate(["prepare", "--index", str(self.site / chart_path),
                                    "--semantics", str(self.site / "data/release-semantics.json"),
                                    "--output", str(receipt)]), 0)
        self.assertEqual(json.loads(receipt.read_text())["item_count"], 1)

    def test_resumed_chart_index_cannot_be_missing_or_differ_from_committed_hash(self):
        relative = "data/chart_search_index.json"
        key = publisher.slot_prefix("b") + relative
        self.r2.objects[key]["body"] = b"altered file"
        with self.assertRaisesRegex(resume.ResumeError, "Candidate object read failed"):
            resume.download_candidate_files(self.r2, "bucket", self.manifest, self.site, workers=1)
        self.assertFalse((self.site / relative).exists())
        self.manifest["files"].pop(relative)
        with self.assertRaisesRegex(resume.ResumeError, "missing an audit or public artifact file"):
            resume.download_candidate_files(self.r2, "bucket", self.manifest, self.site, workers=1)

    def test_download_extended_release_verifies_before_preserving_its_exact_objects(self):
        extra = {'data/extended-locales/assembly.json': b'{}', 'sitemap-extended.xml': b'index',
                 'sitemap-extended-fr.xml': b'sitemap', 'fr/llms.txt': b'links', 'fr/blog/new.html': b'approved page'}
        for name, body in extra.items():
            sha = hashlib.sha256(body).hexdigest()
            self.manifest['files'][name] = {'size':len(body), 'sha256':sha}
            self.r2.objects[publisher.slot_prefix('b')+name] = {'body':body, 'metadata':{'sha256':sha}}
        with patch('verify_prepared_static_slot.verify_extended_static_tree', return_value={'locales':['fr']}) as verify:
            downloaded = resume.download_candidate_files(self.r2, 'bucket', self.manifest, self.site, workers=1)
            verify.assert_called_once()
            self.assertTrue(set(extra).issubset(downloaded))
            for name, body in extra.items():
                self.assertEqual((self.site/name).read_bytes(), body)
        with patch('verify_prepared_static_slot.verify_extended_static_tree', side_effect=RuntimeError('checksum mismatch')):
            with self.assertRaisesRegex(RuntimeError, 'checksum mismatch'):
                resume.download_candidate_files(self.r2, 'bucket', self.manifest, self.site, workers=1)

    def test_extended_validation_captures_exact_bytes_without_a_second_download(self):
        from test_verify_prepared_static_slot import PreparedStaticSlotTests
        from test_verify_portal_locale_routes import ORIGIN as fixture_origin
        extra = PreparedStaticSlotTests().extended_files(locales=['fr', 'de'], pages_per_locale=40)
        for name, body in extra.items():
            sha = hashlib.sha256(body).hexdigest()
            self.manifest['files'][name] = {'size': len(body), 'sha256': sha}
            self.r2.objects[publisher.slot_prefix('b')+name] = {'body': body, 'metadata': {'sha256': sha}}
        self.r2.operations.clear()
        with patch('portal_extended_locales.ORIGIN', fixture_origin):
            downloaded = resume.download_candidate_files(self.r2, 'bucket', self.manifest, self.site, workers=16)
        operations = Counter(self.r2.operations)
        self.assertTrue(set(extra).issubset(downloaded))
        for name, body in extra.items():
            self.assertEqual(operations['get', publisher.slot_prefix('b')+name], 1, name)
            self.assertEqual((self.site/name).read_bytes(), body)
        self.assertEqual(list(self.site.rglob('.resume-*.tmp')), [])

    def test_extended_capture_does_not_preserve_a_checksum_mismatch(self):
        from test_verify_prepared_static_slot import PreparedStaticSlotTests
        from test_verify_portal_locale_routes import ORIGIN as fixture_origin
        extra = PreparedStaticSlotTests().extended_files(locales=['fr'], pages_per_locale=2)
        for name, body in extra.items():
            sha = hashlib.sha256(body).hexdigest()
            self.manifest['files'][name] = {'size': len(body), 'sha256': sha}
            self.r2.objects[publisher.slot_prefix('b')+name] = {'body': body, 'metadata': {'sha256': sha}}
        changed = 'fr/blog/20261116-report-0.html'
        self.r2.objects[publisher.slot_prefix('b')+changed]['body'] = b'x' * len(extra[changed])
        with patch('portal_extended_locales.ORIGIN', fixture_origin):
            with self.assertRaisesRegex(RuntimeError, 'content differs'):
                resume.download_candidate_files(self.r2, 'bucket', self.manifest, self.site, workers=16)
        self.assertFalse((self.site/changed).exists())
        self.assertEqual(list(self.site.rglob('.resume-*.tmp')), [])

    def test_atomic_local_capture_preserves_previous_file_and_cleans_failed_replace(self):
        target = self.site/'capture.json'; self.site.mkdir(exist_ok=True); target.write_bytes(b'previous')
        with patch.object(resume.os, 'replace', side_effect=OSError('local replace failed')):
            with self.assertRaisesRegex(OSError, 'local replace failed'):
                resume.write_local(self.site, 'capture.json', b'new verified bytes')
        self.assertEqual(target.read_bytes(), b'previous')
        self.assertEqual(list(self.site.rglob('.resume-*.tmp')), [])

    def test_download_english_recovery_preserves_only_the_verified_public_previews_and_assets(self):
        extra = {'data/english-commentary/assembly.json': b'{}', 'sitemap-en.xml': b'sitemap',
                 'en/index.html': b'preview home', 'en/blog/20261001-0000000000000001.html': b'preview',
                 'assets/english-commentary.js': b'text-only client', 'assets/english-commentary.css': b'style',
                 'assets/extended-locales.js': b'shared search', 'assets/extended-locales.css': b'shared style'}
        for name, body in extra.items():
            sha = hashlib.sha256(body).hexdigest(); self.manifest['files'][name] = {'size': len(body), 'sha256': sha}
            self.r2.objects[publisher.slot_prefix('b')+name] = {'body': body, 'metadata': {'sha256': sha}}
        public = {name: {} for name in extra if name.startswith('en/') or name == 'sitemap-en.xml'}
        with patch('portal_english_publication.read_static_assembly', return_value={'public_files': public}) as verify:
            downloaded = resume.download_candidate_files(self.r2, 'bucket', self.manifest, self.site, workers=1)
            verify.assert_called_once(); self.assertTrue(set(extra).issubset(downloaded))
            for name, body in extra.items(): self.assertEqual((self.site/name).read_bytes(), body)
        with patch('portal_english_publication.read_static_assembly', side_effect=RuntimeError('checksum mismatch')):
            with self.assertRaisesRegex(RuntimeError, 'checksum mismatch'):
                resume.download_candidate_files(self.r2, 'bucket', self.manifest, self.site, workers=1)

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
        with patch("verify_portal_locale_routes.release_fetch.subprocess.run", side_effect=AssertionError("No live HTTP")):
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

    def use_pre_deployment_failure(self):
        self.use_rolled_back_source()
        steps = self.github.jobs[1]['steps']
        for step in steps:
            if step['name'] == 'Verify committed candidate immediately before cutover':
                step['conclusion'] = 'failure'
            elif step['number'] > 4 and step['name'] != resume.OUTCOME_STEP:
                step['conclusion'] = 'skipped'
        steps.insert(6, {'name': 'Audit extended locale pages after live cutover',
                         'status': 'completed', 'conclusion': 'skipped'})
        for number, step in enumerate(steps, 1):
            step['number'] = number

    def test_pre_deployment_failure_restores_without_translation_or_remote_writes(self):
        self.use_pre_deployment_failure()
        result = self.restore()
        self.assertEqual(result['source_failure_phase'], 'pre_deployment_guard')
        self.assertFalse(result['source_deployment_performed'])
        self.assertFalse(result['source_rollback_verified'])
        self.assertEqual(result['remote_mutations'], 0)
        self.assertEqual(result['verified_remote_objects'], self.manifest['file_count'])
        self.assertEqual(self.live.call_count, 2)

    def use_english_cutover_failure(self, *, bind_failure=False):
        self.use_rolled_back_source(); steps = self.github.jobs[1]['steps']
        for step in steps:
            if step['name'] == resume.LIVE_ACCEPTANCE_STEP: step['conclusion'] = 'success'
        steps.insert(4, {'name': resume.ENGLISH_BIND_STEP, 'status': 'completed', 'conclusion': 'failure' if bind_failure else 'success'})
        steps.insert(7, {'name': 'Audit extended locale pages after live cutover', 'status': 'completed', 'conclusion': 'skipped'})
        steps.insert(8, {'name': resume.ENGLISH_AUDIT_STEP, 'status': 'completed', 'conclusion': 'skipped' if bind_failure else 'failure'})
        steps.insert(11, {'name': resume.ENGLISH_ROLLBACK_STEP, 'status': 'completed', 'conclusion': 'skipped' if bind_failure else 'success'})
        if bind_failure:
            for step in steps[5:]:
                if step['name'] != resume.OUTCOME_STEP: step['conclusion'] = 'skipped'
        for number, step in enumerate(steps, 1): step['number'] = number

    def test_english_bind_failure_recovers_immutable_candidate_before_any_deployment(self):
        self.use_english_cutover_failure(bind_failure=True); result = self.restore()
        self.assertFalse(result['source_deployment_performed']); self.assertFalse(result['source_rollback_verified'])
        self.assertEqual(result['remote_mutations'], 0)

    def test_english_acceptance_failure_recovers_only_after_verified_english_rollback(self):
        self.use_english_cutover_failure(); result = self.restore()
        self.assertEqual(result['source_failure_phase'], 'english_acceptance_rolled_back')
        self.assertTrue(result['source_rollback_verified']); self.assertEqual(result['remote_mutations'], 0)
        original = copy.deepcopy(self.github.jobs)
        for name in (resume.ENGLISH_BIND_STEP, resume.LIVE_ACCEPTANCE_STEP, resume.ENGLISH_ROLLBACK_STEP):
            for outcome in ('skipped', 'failure', 'cancelled'):
                self.github.jobs = copy.deepcopy(original)
                next(step for step in self.github.jobs[1]['steps'] if step['name'] == name)['conclusion'] = outcome
                with self.subTest(name=name, outcome=outcome), self.assertRaises(resume.ResumeError): self.restore()
        for name in (resume.ENGLISH_BIND_STEP, resume.ENGLISH_AUDIT_STEP, resume.ENGLISH_ROLLBACK_STEP,
                     'Deploy prepared neutral edge release', resume.ROLLBACK_VERIFY_STEP):
            self.github.jobs = copy.deepcopy(original)
            next(step for step in self.github.jobs[1]['steps'] if step['name'] == name)['number'] = 999
            with self.subTest(order=name), self.assertRaises(resume.ResumeError): self.restore()

    def test_pre_deployment_recovery_rejects_missing_or_ambiguous_execution_evidence(self):
        self.use_pre_deployment_failure()
        original = copy.deepcopy(self.github.jobs)
        for index, step in enumerate(original[1]['steps']):
            for outcome in ({'success', 'failure', 'skipped', 'cancelled', 'timed_out'} - {step['conclusion']}):
                with self.subTest(step=step['name'], outcome=outcome):
                    self.github.jobs = copy.deepcopy(original)
                    self.github.jobs[1]['steps'][index]['conclusion'] = outcome
                    with self.assertRaises(resume.ResumeError): self.restore()
            self.github.jobs = copy.deepcopy(original)
            del self.github.jobs[1]['steps'][index]
            with self.assertRaises(resume.ResumeError): self.restore()
        self.assertEqual(self.r2.operations, [])
        self.live.assert_not_called()

    def test_pre_deployment_recovery_still_rejects_changed_live_or_candidate_identity(self):
        self.use_pre_deployment_failure()
        self.live.return_value = {**PREVIOUS, 'tree_sha256': '9'*64}
        with self.assertRaisesRegex(resume.ResumeError, 'changed'): self.restore()
        self.live.return_value = copy.deepcopy(PREVIOUS)
        self.manifest['files']['index.html']['sha256'] = '0'*64
        self.save_manifest()
        with self.assertRaisesRegex(resume.ResumeError, 'tree digest'): self.restore()

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
        from test_portal_locale_manifest import with_source_fallback, compress_source_fallback

        path = "data/i18n/manifest.json"
        object_key = publisher.slot_prefix("b") + path
        payload = with_source_fallback(json.loads(self.r2.objects[object_key]["body"]))

        def save_payload(compressed):
            body = encoded(compress_source_fallback(payload) if compressed else payload)
            self.r2.objects[object_key]["body"] = body
            self.manifest["files"][path].update(size=len(body), sha256=hashlib.sha256(body).hexdigest())

        for compressed in (False, True):
            payload['source_fallbacks']['counts']['ko'] = 1
            save_payload(compressed)
            restored = resume.download_candidate_files(self.r2, "bucket", self.manifest, self.site, workers=1)
            self.assertIn(path, restored)
            payload["source_fallbacks"]["counts"]["ko"] = 2
            save_payload(compressed)
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

    def test_download_resolves_all_source_shards_only_inside_committed_slot(self):
        from test_verify_portal_locale_manifest_bundle import sharded_fixture
        path = 'data/i18n/manifest.json'
        prefix = publisher.slot_prefix('b')
        value, shards = sharded_fixture(json.loads(self.r2.objects[prefix + path]['body']))
        for relative, body in {path: encoded(value), **shards}.items():
            self.r2.objects[prefix + relative] = {'body': body}
            self.manifest['files'][relative] = {'size': len(body), 'sha256': hashlib.sha256(body).hexdigest()}
        restored = resume.download_candidate_files(self.r2, 'bucket', self.manifest, self.site, workers=1)
        self.assertTrue(set(shards).issubset(restored))
        for relative, body in shards.items():
            self.assertEqual((self.site / relative).read_bytes(), body)
        relative = next(iter(shards))
        self.manifest['files'][relative]['sha256'] = '0' * 64
        self.r2.operations.clear()
        with self.assertRaisesRegex(resume.ResumeError, 'source shard differs from committed'):
            resume.download_candidate_files(self.r2, 'bucket', self.manifest, self.site, workers=1)
        self.assertNotIn(('get', prefix + relative), self.r2.operations)

    def restore(self, **kwargs):
        previous = getattr(self, "retained_previous", PREVIOUS)
        options = dict(github=self.github, client=self.r2, bucket="bucket", repository=REPO, run_id=321, run_attempt=1,
                       site_dir=self.site, diagnostics_dir=self.diag, work_dir=self.work, origin=ORIGIN,
                       expected_slot="b", expected_release=RELEASE, expected_tree=self.tree, expected_commit=COMMIT,
                       expected_previous_release=previous["release_id"], expected_previous_tree=previous["tree_sha256"],
                       fetch_live=self.live, workers=4)
        return resume.resume_candidate(**{**options, **kwargs})

    def use_retained_candidate(self):
        from test_audit_portal_shadow_preview import manifest_fixture
        import retain_published_core_locales as retention
        locale, bodies = manifest_fixture()
        locale.update(html_page_count=6, translation_scope="full", index_policy={"mode": "noindex"})
        # Legacy manifests have no application_routes group, but their Chinese
        # lazy asset must still be downloaded and rebound exactly.
        old_lazy, new_lazy = b"old Chinese lazy module", b"fresh Chinese lazy module"
        locale["lazy_javascript_assets"] = {"zh-Hans": {
            "path": "assets/newsfeed-app.js", "byte_size": len(old_lazy),
            "sha256": hashlib.sha256(old_lazy).hexdigest()}}
        source_manifest = encoded(locale)
        locale["lazy_javascript_assets"]["zh-Hans"].update(byte_size=len(new_lazy), sha256=hashlib.sha256(new_lazy).hexdigest())
        bodies["/" + retention.MANIFEST] = encoded(locale)
        bodies["/assets/newsfeed-app.js"] = new_lazy
        for relative in retention.SHARED_ASSETS:
            bodies.setdefault("/" + relative, b"published shared locale asset")
        # Inventory-only locale assets must also be restored and rechecked.
        bodies["/ko/assets/retained-only.js"] = b"published inventory-only locale asset"
        for path, body in bodies.items():
            relative = path.lstrip("/")
            descriptor = {"size": len(body), "sha256": hashlib.sha256(body).hexdigest(),
                          "content_type": "application/json", "cache_control": "public, max-age=0, must-revalidate"}
            self.manifest["files"][relative] = descriptor
            self.r2.objects[publisher.slot_prefix("b") + relative] = {"body": body, "metadata": {"sha256": descriptor["sha256"]}}
        old_tree = self.tree
        self.tree = resume.static_tree_sha256(self.manifest["files"])
        self.manifest.update(tree_sha256=self.tree, file_count=len(self.manifest["files"]),
                             total_bytes=sum(row["size"] for row in self.manifest["files"].values()))
        self.save_manifest()
        self.github.logs = self.github.logs.replace(old_tree, self.tree)
        paths = retention.selected_paths(self.manifest["files"])
        old_files = {path: copy.deepcopy(self.manifest["files"][path]) for path in paths | {"assets/app.js", "assets/newsfeed-app.js"}}
        old_files[retention.MANIFEST].update(size=len(source_manifest), sha256=hashlib.sha256(source_manifest).hexdigest())
        old_files["assets/newsfeed-app.js"].update(size=len(old_lazy), sha256=hashlib.sha256(old_lazy).hexdigest())
        self.retained_previous = {**PREVIOUS, "tree_sha256": resume.static_tree_sha256(old_files)}
        self.previous_manifest = {**self.retained_previous, "files": old_files, "file_count": len(old_files),
                                  "total_bytes": sum(row["size"] for row in old_files.values())}
        self.r2.objects[publisher.manifest_key("a")] = {"body": encoded(self.previous_manifest)}
        for path in old_files:
            self.r2.objects[publisher.slot_prefix("a") + path] = copy.deepcopy(self.r2.objects[publisher.slot_prefix("b") + path])
        for path, body in ((retention.MANIFEST, source_manifest), ("assets/newsfeed-app.js", old_lazy)):
            self.r2.objects[publisher.slot_prefix("a") + path] = {"body": body, "metadata": {"sha256": hashlib.sha256(body).hexdigest()}}
        (self.work / "previous-edge-state.json").write_bytes(encoded(self.retained_previous))
        self.live.return_value = copy.deepcopy(self.retained_previous)
        receipt = {"schema_version": 1, "kind": "published-core-locales", "source_state": self.retained_previous,
                   "retained_files": len(paths), "provider_requests": 0,
                   "source_manifest_b64": base64.b64encode(source_manifest).decode()}
        self.github.diagnostics = {name: body for name, body in self.github.diagnostics.items() if name.startswith("chinese-")}
        self.github.diagnostics.update({"locale-retention.json": encoded(receipt),
                                        "locale-retention-active-manifest.json": encoded(self.previous_manifest)})
        self.github.logs += "core_locale_publication_mode=retained\n"
        self.attest_retention_proofs()
        return receipt

    def attest_retention_proofs(self):
        self.github.logs = "\n".join(line for line in self.github.logs.splitlines()
                                     if not line.startswith(("retention_receipt_sha256=", "retention_active_manifest_sha256="))) + "\n"
        for name, label in (("locale-retention.json", "retention_receipt_sha256"),
                            ("locale-retention-active-manifest.json", "retention_active_manifest_sha256")):
            self.github.logs += label + "=" + hashlib.sha256(self.github.diagnostics[name]).hexdigest() + "\n"

    def test_retained_catalog_candidate_restores_exact_old_coverage_without_fresh_translation_reports(self):
        self.use_retained_candidate()
        result = self.restore()
        self.assertEqual(result["publication_mode"], "retained")
        self.assertTrue(result["retention_verified"] and result["locale_ready"])
        self.assertFalse(result["preflight_passed"])
        self.assertTrue(result["performance_passed"])
        self.assertEqual(json.loads((self.site / "data/i18n/manifest.json").read_bytes())["translation_scope"], "full")
        self.assertEqual((self.site / "ko/assets/retained-only.js").read_bytes(), b"published inventory-only locale asset")
        self.assertEqual((self.site / "assets/newsfeed-app.js").read_bytes(), b"fresh Chinese lazy module")
        for name in resume.RETENTION_DIAGNOSTICS:
            self.assertEqual((self.work / name).read_bytes(), self.github.diagnostics[name])
        self.assertFalse((self.work / "locale-full-diagnostics.json").exists())
        self.assertFalse((self.work / "locale-preflight-diagnostics.json").exists())
        self.assertTrue(all(operation in {"head", "get"} for operation, _key in self.r2.operations))

    def test_retention_cannot_replace_fresh_evidence_without_explicit_source_mode(self):
        self.use_retained_candidate()
        self.github.logs = self.github.logs.replace("core_locale_publication_mode=retained\n", "")
        with self.assertRaisesRegex(resume.ResumeError, "mix retained and fresh"):
            self.restore()
        self.assertFalse(self.site.exists())

    def test_retention_rejects_missing_or_unattested_proof_before_bulk_reads(self):
        self.use_retained_candidate()
        for name in ("locale-retention.json", "locale-retention-active-manifest.json"):
            body = self.github.diagnostics.pop(name)
            with self.subTest(missing=name), self.assertRaisesRegex(resume.ResumeError, "incomplete"):
                self.restore()
            self.github.diagnostics[name] = body
        self.github.logs = self.github.logs.replace("retention_receipt_sha256=", "unattested_receipt=")
        with self.assertRaisesRegex(resume.ResumeError, "does not attest"):
            self.restore()
        self.assertFalse(self.site.exists())

    def test_retention_proof_cannot_rebind_previous_identity_or_original_manifest_bytes(self):
        receipt = self.use_retained_candidate()
        for change, message in (({"source_state": {**self.retained_previous, "release_id": "9" * 32}}, "source state"),
                                ({"source_manifest_b64": base64.b64encode(b"{}").decode()}, "source manifest proof")):
            self.github.diagnostics["locale-retention.json"] = encoded({**receipt, **change})
            self.attest_retention_proofs()
            with self.subTest(change=change), self.assertRaisesRegex(resume.ResumeError, message):
                self.restore()
            self.assertFalse(self.site.exists())

    def test_retained_file_descriptors_cannot_change_even_in_a_new_valid_candidate_tree(self):
        self.use_retained_candidate()
        old_tree = self.tree
        self.manifest["files"]["ko/index.html"]["sha256"] = "f" * 64
        self.tree = resume.static_tree_sha256(self.manifest["files"])
        self.manifest["tree_sha256"] = self.tree
        self.save_manifest()
        self.github.logs = self.github.logs.replace(old_tree, self.tree)
        with self.assertRaisesRegex(resume.ResumeError, "Retained candidate descriptor changed"):
            self.restore()
        self.assertFalse(self.site.exists())

    def test_every_restored_retained_body_is_rechecked_before_emitting_identity(self):
        self.use_retained_candidate()
        download = resume.download_candidate_files
        def corrupt_after_restore(*args, **kwargs):
            result = download(*args, **kwargs)
            (self.site / "ko/assets/retained-only.js").write_bytes(b"corrupt")
            return result
        with patch.object(resume, "download_candidate_files", side_effect=corrupt_after_restore):
            with self.assertRaisesRegex(RuntimeError, "published file changed"):
                self.restore()
        self.assertFalse((self.work / "locale-resume-identity.json").exists())

    def test_retained_mode_still_requires_fresh_chinese_performance_and_parity(self):
        self.use_retained_candidate()
        self.github.diagnostics["chinese-performance.json"] = encoded({"status": "passed", "active_compared": False})
        with self.assertRaisesRegex(resume.ResumeError, "does not match uploaded app"):
            self.restore()
        self.assertFalse(self.site.exists())

    def use_published_history_followup(self):
        from portal_locale_history import plan_history_release
        from restore_published_chinese_source import CORE_MANIFEST, HISTORY_LEDGER, read_core_policy
        receipt = self.use_retained_candidate()
        source = json.loads(base64.b64decode(receipt["source_manifest_b64"]))
        candidates = {ORIGIN + "/blog/new.html": "2026-09-01"}
        old_history = plan_history_release(candidates, history_start_date="2026-08-05", launch_date="2026-10-01",
                                          today="2026-10-02", previous=None)
        paused = plan_history_release(candidates, history_start_date="2026-08-05", launch_date="2026-10-01",
                                     today="2026-10-03", previous=old_history, paused=True)
        source.update(translation_scope="release", index_policy={
            "mode": "fixed-publication-cutoff", "default": "hubs-only", "index_start_date": "2026-10-01", "allowlist_count": 0,
            "history_release": {"history_start_date": "2026-08-05", "daily_limit": 100,
                                "released_count": 1, "selected_today_count": 1, "paused": False}})
        current = copy.deepcopy(source)
        current["lazy_javascript_assets"] = json.loads(self.r2.objects[publisher.slot_prefix("b") + CORE_MANIFEST]["body"])["lazy_javascript_assets"]
        current["index_policy"]["history_release"].update(paused=True, selected_today_count=0)
        def update(slot, relative, body, manifest):
            row = {"size": len(body), "sha256": hashlib.sha256(body).hexdigest(),
                   "content_type": "application/json", "cache_control": "public, max-age=0, must-revalidate"}
            manifest["files"][relative] = row
            self.r2.objects[publisher.slot_prefix(slot) + relative] = {"body": body, "metadata": {"sha256": row["sha256"]}}
        for slot, manifest, locale, ledger in (("a", self.previous_manifest, source, old_history),
                                               ("b", self.manifest, current, paused)):
            update(slot, CORE_MANIFEST, encoded(locale), manifest)
            update(slot, HISTORY_LEDGER, encoded(ledger), manifest)
            for code in resume.LOCALES:
                update(slot, f"sitemap-{code}.xml", f"<urlset><url><loc>{ORIGIN}/{code}/blog/new.html</loc></url></urlset>".encode(), manifest)
            manifest.update(tree_sha256=resume.static_tree_sha256(manifest["files"]), file_count=len(manifest["files"]),
                            total_bytes=sum(row["size"] for row in manifest["files"].values()))
            self.r2.objects[publisher.manifest_key(slot)] = {"body": encoded(manifest)}
        self.retained_previous["tree_sha256"] = self.previous_manifest["tree_sha256"]
        (self.work / "previous-edge-state.json").write_bytes(encoded(self.retained_previous))
        self.live.return_value = copy.deepcopy(self.retained_previous)
        self.github.logs = self.github.logs.replace(self.tree, self.manifest["tree_sha256"])
        self.tree = self.manifest["tree_sha256"]
        core = read_core_policy(self.r2, "bucket", self.previous_manifest, ORIGIN)
        proof = {"schema_version": 1, "kind": "published-chinese-source", "source_state": self.retained_previous,
                 "site_origin": ORIGIN, "source_tree_sha256": self.retained_previous["tree_sha256"],
                 "source_file_count": self.previous_manifest["file_count"], "provider_requests": 0, "remote_mutations": 0,
                 "core_locales": core}
        self.github.logs = "\n".join(line for line in self.github.logs.splitlines()
                                     if not line.startswith(("retention_", "core_locale_publication_mode="))) + "\ncore_locale_publication_mode=translated\n"
        self.github.diagnostics = {name: body for name, body in self.github.diagnostics.items() if name.startswith("chinese-")}
        self.github.diagnostics.update({"locale-preflight-diagnostics.json": encoded({"status": "passed", "preflight_only": True}),
                                        "locale-full-diagnostics.json": encoded({"status": "passed", "ready": True}),
                                        resume.SOURCE_PROOF: encoded(proof)})
        self.github.logs += "chinese_locale_source_sha256=" + hashlib.sha256(encoded(proof)).hexdigest() + "\n"
        return proof, old_history

    def test_pinned_paused_history_followup_recovers_without_reopening_publication(self):
        proof, previous_history = self.use_published_history_followup()
        result = self.restore()
        self.assertTrue(result["source_snapshot_verified"] and result["preflight_passed"])
        self.assertEqual(result["publication_mode"], "translated")
        self.assertEqual(json.loads((self.work / resume.SOURCE_PROOF).read_bytes()), proof)
        history = json.loads((self.site / "data/i18n/history-release.json").read_bytes())
        self.assertEqual(history["released"], previous_history["released"])
        self.assertEqual(history["last_release_date"], previous_history["last_release_date"])
        self.assertTrue(history["paused"])

    def test_historical_candidate_without_logged_source_proof_still_cannot_recover(self):
        self.use_published_history_followup()
        del self.github.diagnostics[resume.SOURCE_PROOF]
        self.github.logs = "\n".join(line for line in self.github.logs.splitlines() if not line.startswith("chinese_locale_source_sha256="))
        with self.assertRaisesRegex(resume.ResumeError, "not an incremental"):
            self.restore()
        self.assertFalse((self.work / "locale-resume-identity.json").exists())

    def test_logged_source_policy_must_equal_the_pinned_previous_policy(self):
        proof, _history = self.use_published_history_followup()
        proof["core_locales"]["index_policy"]["allowlist_count"] = 2
        self.github.diagnostics[resume.SOURCE_PROOF] = encoded(proof)
        self.github.logs = "\n".join(line for line in self.github.logs.splitlines() if not line.startswith("chinese_locale_source_sha256="))
        self.github.logs += "\nchinese_locale_source_sha256=" + hashlib.sha256(encoded(proof)).hexdigest() + "\n"
        with self.assertRaisesRegex(resume.ResumeError, "policy differs from the pinned"):
            self.restore()
        self.assertFalse(self.site.exists())

    def test_followup_cannot_consume_another_history_day_after_restore(self):
        self.use_published_history_followup()
        download = resume.download_candidate_files
        def advance_history(*args, **kwargs):
            result = download(*args, **kwargs)
            path = self.site / "data/i18n/history-release.json"
            value = json.loads(path.read_bytes()); value["last_release_date"] = "2026-10-03"
            path.write_bytes(encoded(value))
            return result
        with patch.object(resume, "download_candidate_files", side_effect=advance_history):
            with self.assertRaisesRegex(RuntimeError, "consumed a release day"):
                self.restore()
        self.assertFalse((self.work / "locale-resume-identity.json").exists())

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
            with self.assertRaisesRegex(resume.ResumeError, "size_invalid"):
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

    def test_full_catalog_diagnostics_over_legacy_16_mib_are_preserved_and_checked(self):
        value = {'schema_version': 1, 'status': 'passed', 'ready': True,
                 'diagnostic_padding': 'x' * (16 * 1024 * 1024)}
        body = encoded(value)
        self.assertGreater(len(body), 16 * 1024 * 1024)
        self.github.diagnostics['locale-full-diagnostics.json'] = body
        result = self.restore()
        self.assertEqual(result['remote_mutations'], 0)
        self.assertEqual((self.diag/'locale-full-diagnostics.json').read_bytes(), body)
        value['ready'] = False
        self.github.diagnostics['locale-full-diagnostics.json'] = encoded(value)
        resume.download_diagnostics(self.github, REPO, 321, 1, self.diag)
        with self.assertRaisesRegex(resume.ResumeError, 'not ready'):
            resume.validate_diagnostics(self.diag, APP, self.github.logs, ORIGIN, active_app=APP)

    def test_expanded_diagnostics_still_reject_duplicates_per_file_and_total_overflow(self):
        self.github.archive_extra = {'copy/locale-full-diagnostics.json': encoded({'ready':True})}
        with self.assertRaisesRegex(resume.ResumeError, 'duplicate'):
            resume.download_diagnostics(self.github, REPO, 321, 1, self.diag)
        self.github.archive_extra = {}
        with patch.dict(resume.DIAGNOSTIC_MAX_BYTES, {'locale-full-diagnostics.json': 1}):
            with self.assertRaisesRegex(resume.ResumeError, 'expanded byte bound'):
                resume.download_diagnostics(self.github, REPO, 321, 1, self.diag)
        with patch.object(resume, 'MAX_DIAGNOSTICS_EXPANDED_BYTES', 1):
            with self.assertRaisesRegex(resume.ResumeError, 'total expanded'):
                resume.download_diagnostics(self.github, REPO, 321, 1, self.diag)

    def test_production_sized_locale_diagnostics_are_preserved_and_validated_sequentially(self):
        sizes = {"locale-preflight-diagnostics.json": 225330008, "locale-full-diagnostics.json": 225241451}
        archive_buffer = io.BytesIO()
        expected_hashes = {}
        chunk = b"x" * (1024 * 1024)
        with zipfile.ZipFile(archive_buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=1) as archive:
            for name, size in sizes.items():
                fields = b'"preflight_only":true' if "preflight" in name else b'"ready":true'
                prefix = b'{"status":"passed",' + fields + b',"padding":"'
                digest = hashlib.sha256()
                with archive.open(name, "w") as member:
                    member.write(prefix)
                    digest.update(prefix)
                    remaining = size - len(prefix) - 2
                    while remaining:
                        part = chunk[:min(remaining, len(chunk))]
                        member.write(part)
                        digest.update(part)
                        remaining -= len(part)
                    member.write(b'"}')
                    digest.update(b'"}')
                expected_hashes[name] = digest.hexdigest()
            for name in ("chinese-parity.json", "chinese-performance.json"):
                archive.writestr(name, self.github.diagnostics[name])
        payload = archive_buffer.getvalue()
        github = Mock()
        github.json.return_value = {"artifacts": [{
            "id": 99, "name": "neutral-translation-diagnostics-321-1", "expired": False,
            "workflow_run": {"id": 321}, "size_in_bytes": len(payload),
        }]}
        github.artifact_bytes.return_value = payload
        resume.download_diagnostics(github, REPO, 321, 1, self.diag)
        for name, size in sizes.items():
            path = self.diag / name
            self.assertEqual(path.stat().st_size, size)
            with path.open("rb") as source:
                self.assertEqual(hashlib.file_digest(source, "sha256").hexdigest(), expected_hashes[name])
        result = resume.validate_diagnostics(self.diag, APP, self.github.logs, ORIGIN, active_app=APP)
        self.assertTrue(result["preflight_passed"] and result["locale_ready"])

    def test_locale_json_trees_are_released_before_reading_the_next_diagnostic(self):
        resume.download_diagnostics(self.github, REPO, 321, 1, self.diag)
        decode = resume.decode_json
        loaded = []
        locale_tree = None

        class TrackedDict(dict):
            pass

        def tracked_decode(body, name):
            nonlocal locale_tree
            if locale_tree is not None:
                self.assertIsNone(locale_tree(), "Previous large locale JSON tree is still retained")
            value = decode(body, name)
            loaded.append(name)
            if name.startswith("locale-"):
                value = TrackedDict(value)
                locale_tree = weakref.ref(value)
            return value

        with patch.object(resume, "decode_json", side_effect=tracked_decode):
            result = resume.validate_diagnostics(self.diag, APP, self.github.logs, ORIGIN, active_app=APP)
        self.assertEqual(loaded, list(resume.DIAGNOSTICS))
        self.assertTrue(result["locale_ready"])

    def test_artifact_size_metadata_is_checked_before_download(self):
        for size in (None, 0, -1, True, "100", 1.5, resume.MAX_ARTIFACT_DOWNLOAD_BYTES + 1):
            github = Mock()
            github.json.return_value = {"artifacts": [{
                "id": 99, "name": "neutral-translation-diagnostics-321-1", "expired": False,
                "workflow_run": {"id": 321}, "size_in_bytes": size,
            }]}
            with self.subTest(size=size), self.assertRaisesRegex(resume.ResumeError, "download size"):
                resume.download_diagnostics(github, REPO, 321, 1, self.diag)
            github.artifact_bytes.assert_not_called()

    def test_live_change_during_restore_does_not_emit_resume_identity(self):
        self.live.side_effect = [PREVIOUS, {**PREVIOUS, "release_id": "9" * 32}]
        with self.assertRaisesRegex(resume.ResumeError, "during candidate restore"):
            self.restore()
        self.assertFalse((self.work / "locale-resume-identity.json").exists())


class CandidateReadRetryTests(unittest.TestCase):
    BODY = b"committed candidate object"
    KEY = "edge-static/slots/b/ko/blog/new.html"

    def setUp(self):
        jitter = patch("r2_transport.random.uniform", return_value=0)
        jitter.start()
        self.addCleanup(jitter.stop)

    def descriptor(self):
        return {"size": len(self.BODY), "sha256": hashlib.sha256(self.BODY).hexdigest()}

    def test_empty_static_file_keeps_bounded_read_compatibility(self):
        stream = io.BytesIO(b'')
        client = Mock()
        client.get_object.return_value = {'Body': stream}
        self.assertEqual(resume.read_candidate_object(client, 'bucket', self.KEY,
                         {'size': 0, 'sha256': hashlib.sha256(b'').hexdigest()}), b'')
        self.assertTrue(stream.closed)
        client.get_object.assert_called_once_with(Bucket='bucket', Key=self.KEY)

    def test_oversized_descriptor_stops_before_read_and_stream_is_bounded(self):
        client = Mock()
        with self.assertRaisesRegex(resume.ResumeError, 'byte size bound'):
            resume.read_candidate_object(client, 'bucket', self.KEY, self.descriptor(), maximum=1)
        client.get_object.assert_not_called()
        stream = Mock()
        stream.read.return_value = b'x' * (len(self.BODY) + 1)
        client.get_object.return_value = {'Body': stream}
        with self.assertRaisesRegex(resume.ResumeError, 'read failed'):
            resume.read_candidate_object(client, 'bucket', self.KEY, self.descriptor())
        stream.read.assert_called_once_with(len(self.BODY) + 1)
        stream.close.assert_called_once_with()

    @staticmethod
    def read_error(code):
        error = RuntimeError("injected object read error")
        error.response = {"Error": {"Code": code}}
        return error

    @patch("r2_transport.time.sleep")
    def test_request_throttling_does_not_start_another_native_sdk_chain(self, sleep):
        for code in ("ServiceUnavailable", "SlowDown", "429"):
            for retries in (None, 0, 8):
                with self.subTest(code=code, retries=retries):
                    error = self.read_error(code)
                    if retries is not None:
                        error.response["ResponseMetadata"] = {"RetryAttempts": retries}
                    client = Mock()
                    client.get_object.side_effect = error
                    with self.assertRaisesRegex(resume.ResumeError, "Candidate object read failed"):
                        resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor())
                    client.get_object.assert_called_once_with(Bucket="bucket", Key=self.KEY)
        sleep.assert_not_called()

    @patch("r2_transport.time.sleep")
    def test_access_denied_and_no_such_key_never_retry(self, sleep):
        for code in ("AccessDenied", "NoSuchKey"):
            with self.subTest(code=code):
                client = Mock()
                client.get_object.side_effect = self.read_error(code)
                with self.assertRaisesRegex(resume.ResumeError, "Candidate object read failed"):
                    resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor())
                client.get_object.assert_called_once_with(Bucket="bucket", Key=self.KEY)
        sleep.assert_not_called()

    @patch("r2_transport.time.sleep")
    def test_hash_mismatch_never_retries_and_closes_stream(self, sleep):
        stream = io.BytesIO(b"x" * len(self.BODY))
        client = Mock()
        client.get_object.return_value = {"Body": stream}
        with self.assertRaisesRegex(resume.ResumeError, "differs from manifest"):
            resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor())
        self.assertEqual(client.get_object.call_count, 1)
        self.assertTrue(stream.closed)
        sleep.assert_not_called()

    @patch("r2_transport.time.sleep")
    def test_successful_stream_is_closed_without_wait(self, sleep):
        stream = io.BytesIO(self.BODY)
        client = Mock()
        client.get_object.return_value = {"Body": stream}
        self.assertEqual(resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor()), self.BODY)
        self.assertTrue(stream.closed)
        sleep.assert_not_called()

    @patch("r2_transport.time.sleep")
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

    @patch("r2_transport.time.sleep")
    def test_transient_stream_is_closed_before_backoff_and_next_attempt(self, sleep):
        failed_stream = Mock()
        failed_stream.read.side_effect = TimeoutError("interrupted response")
        good_stream = io.BytesIO(self.BODY)
        client = Mock()
        client.get_object.side_effect = [{"Body": failed_stream}, {"Body": good_stream}]
        sleep.side_effect = lambda _delay: failed_stream.close.assert_called_once_with()
        self.assertEqual(resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor()), self.BODY)
        failed_stream.close.assert_called_once_with()
        self.assertTrue(good_stream.closed)
        sleep.assert_called_once_with(2)

    @patch("r2_transport.time.sleep")
    def test_stream_failure_after_sdk_retries_does_not_restart_get(self, sleep):
        stream = Mock()
        stream.read.side_effect = TimeoutError("interrupted response")
        client = Mock()
        client.get_object.return_value = {"Body": stream, "ResponseMetadata": {"RetryAttempts": 1}}
        with self.assertRaisesRegex(resume.ResumeError, "code=TimeoutError"):
            resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor())
        client.get_object.assert_called_once_with(Bucket="bucket", Key=self.KEY)
        stream.close.assert_called_once_with()
        sleep.assert_not_called()

    @patch("r2_transport.time.sleep")
    def test_stream_recovery_stops_after_four_gets_and_closes_every_response(self, sleep):
        streams = [Mock() for _ in range(4)]
        for stream in streams:
            stream.read.side_effect = TimeoutError("interrupted response")
        client = Mock()
        client.get_object.side_effect = [{"Body": stream} for stream in streams]
        with self.assertRaisesRegex(resume.ResumeError, "code=TimeoutError"):
            resume.read_candidate_object(client, "bucket", self.KEY, self.descriptor())
        for stream in streams:
            stream.close.assert_called_once_with()
        self.assertEqual(client.get_object.call_count, 4)
        self.assertEqual(sleep.call_args_list, [call(2), call(4), call(8)])


class CandidateStreamingDownloadTests(unittest.TestCase):
    KEY = "edge-static/slots/b/ko/blog/new.html"
    RELATIVE = "ko/blog/new.html"

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.target = self.root / self.RELATIVE
        self.target.parent.mkdir(parents=True)
        self.target.write_bytes(b"previous verified file")
        jitter = patch("r2_transport.random.uniform", return_value=0)
        jitter.start()
        self.addCleanup(jitter.stop)

    @staticmethod
    def descriptor(body):
        return {"size": len(body), "sha256": hashlib.sha256(body).hexdigest()}

    def download(self, client, body, **kwargs):
        resume.download_candidate_object(client, "bucket", self.KEY, self.descriptor(body),
                                         self.root, self.RELATIVE, **kwargs)

    def assert_no_partial_files(self):
        self.assertEqual(list(self.root.rglob(".resume-*.tmp")), [])

    def test_streams_large_body_in_bounded_chunks_and_atomically_publishes(self):
        body = b"verified data" * (3 * 1024 * 1024 // 13 + 1)
        amounts = []
        case = self
        class Stream(io.BytesIO):
            def read(self, amount=-1):
                amounts.append(amount)
                case.assertEqual(case.target.read_bytes(), b"previous verified file")
                case.assertGreater(amount, 0)
                case.assertLessEqual(amount, resume.r2_transport.READ_CHUNK_BYTES)
                return super().read(amount)
        stream = Stream(body)
        client = Mock()
        client.get_object.return_value = {"Body": stream, "ContentLength": len(body)}
        self.download(client, body)
        self.assertGreater(len(amounts), 3)
        self.assertEqual(self.target.read_bytes(), body)
        self.assertTrue(stream.closed)
        client.get_object.assert_called_once_with(Bucket="bucket", Key=self.KEY)
        self.assert_no_partial_files()

    @patch("r2_transport.time.sleep")
    def test_invalid_content_never_replaces_existing_file_or_retries(self, sleep):
        body = b"exact committed body"
        for changed, declared in ((body[:-1], None), (b"x" * len(body), None),
                                  (body + b"x", None), (body, len(body) - 1),
                                  (body, True)):
            with self.subTest(size=len(changed), declared=declared):
                stream = io.BytesIO(changed)
                client = Mock()
                client.get_object.return_value = {"Body": stream}
                if declared is not None:
                    client.get_object.return_value["ContentLength"] = declared
                with self.assertRaises(resume.ResumeError):
                    self.download(client, body)
                self.assertEqual(self.target.read_bytes(), b"previous verified file")
                self.assertTrue(stream.closed)
                self.assertEqual(client.get_object.call_count, 1)
                self.assert_no_partial_files()
        sleep.assert_not_called()

    @patch("r2_transport.time.sleep")
    def test_interrupted_stream_is_closed_and_partial_file_removed_before_retry(self, sleep):
        body = b"exact committed body"
        failed = Mock()
        failed.read.side_effect = [body[:4], TimeoutError("interrupted body")]
        good = io.BytesIO(body)
        client = Mock()
        client.get_object.side_effect = [{"Body": failed}, {"Body": good}]
        def before_retry(_delay):
            failed.close.assert_called_once_with()
            self.assertEqual(self.target.read_bytes(), b"previous verified file")
            self.assert_no_partial_files()
        sleep.side_effect = before_retry
        self.download(client, body)
        self.assertEqual(self.target.read_bytes(), body)
        self.assertTrue(good.closed)
        self.assertEqual(client.get_object.call_count, 2)
        sleep.assert_called_once_with(2)
        self.assert_no_partial_files()

    @patch("r2_transport.time.sleep")
    def test_sdk_retry_authority_and_permanent_request_errors_are_not_restarted(self, sleep):
        body = b"exact committed body"
        for code in ("SlowDown", "AccessDenied", "NoSuchKey"):
            client = Mock()
            error = CandidateReadRetryTests.read_error(code)
            error.response["ResponseMetadata"] = {"RetryAttempts": 0}
            client.get_object.side_effect = error
            with self.assertRaises(resume.ResumeError):
                self.download(client, body)
            self.assertEqual(client.get_object.call_count, 1)
        for retries in (1, 8, -1):
            stream = Mock()
            stream.read.side_effect = TimeoutError("interrupted body")
            client = Mock()
            client.get_object.return_value = {"Body": stream, "ResponseMetadata": {"RetryAttempts": retries}}
            with self.assertRaises(resume.ResumeError):
                self.download(client, body)
            stream.close.assert_called_once_with()
            self.assertEqual(client.get_object.call_count, 1)
        self.assertEqual(self.target.read_bytes(), b"previous verified file")
        self.assert_no_partial_files()
        sleep.assert_not_called()

    @patch("r2_transport.time.sleep")
    def test_stream_retry_budget_is_finite_and_every_partial_is_removed(self, sleep):
        streams = [Mock() for _ in range(4)]
        for stream in streams:
            stream.read.side_effect = [b"part", TimeoutError("interrupted")]
        client = Mock()
        client.get_object.side_effect = [{"Body": stream} for stream in streams]
        with self.assertRaises(resume.ResumeError):
            self.download(client, b"exact committed body")
        self.assertEqual(client.get_object.call_count, 4)
        for stream in streams:
            stream.close.assert_called_once_with()
        self.assertEqual(sleep.call_args_list, [call(2), call(4), call(8)])
        self.assertEqual(self.target.read_bytes(), b"previous verified file")
        self.assert_no_partial_files()

    def test_empty_file_is_verified_and_bounds_or_symlinks_stop_before_get(self):
        stream = io.BytesIO(b"")
        client = Mock()
        client.get_object.return_value = {"Body": stream, "ContentLength": 0}
        self.download(client, b"")
        self.assertEqual(self.target.read_bytes(), b"")
        self.assertTrue(stream.closed)
        client.reset_mock()
        with self.assertRaisesRegex(resume.ResumeError, "byte size bound"):
            self.download(client, b"larger than allowed", maximum=1)
        self.target.unlink()
        self.target.symlink_to(self.root / "elsewhere")
        with self.assertRaisesRegex(resume.ResumeError, "symbolic"):
            self.download(client, b"body")
        client.get_object.assert_not_called()
        self.assert_no_partial_files()

    def test_missing_or_malformed_body_is_rejected_without_partial_output(self):
        for response in ({}, {"Body": io.StringIO("not bytes")}):
            with self.subTest(response_keys=list(response)):
                client = Mock()
                client.get_object.return_value = response
                with self.assertRaises(resume.ResumeError):
                    self.download(client, b"body")
                self.assertEqual(client.get_object.call_count, 1)
                self.assertEqual(self.target.read_bytes(), b"previous verified file")
                self.assert_no_partial_files()
                if "Body" in response:
                    self.assertTrue(response["Body"].closed)


class BoundedRecoverySchedulingTests(unittest.TestCase):
    def test_production_file_count_keeps_only_sixteen_submitted_results_and_runs_in_parallel(self):
        worker_count = resume.DOWNLOAD_WORKERS
        self.assertEqual(worker_count, 16)
        lock = threading.Lock()
        ready = threading.Event()
        active = maximum_active = retained = maximum_retained = 0
        original_pool = resume.ThreadPoolExecutor
        class TrackingPool(original_pool):
            def submit(self, *args, **kwargs):
                nonlocal retained, maximum_retained
                with lock:
                    retained += 1
                    maximum_retained = max(maximum_retained, retained)
                future = super().submit(*args, **kwargs)
                original_result = future.result
                def result(*result_args, **result_kwargs):
                    nonlocal retained
                    try:
                        return original_result(*result_args, **result_kwargs)
                    finally:
                        with lock:
                            retained -= 1
                future.result = result
                return future
        def verify(index):
            nonlocal active, maximum_active
            with lock:
                active += 1
                maximum_active = max(maximum_active, active)
                if active == worker_count:
                    ready.set()
            try:
                if index < worker_count and not ready.wait(5):
                    raise AssertionError("Initial downloads did not run concurrently")
                return index
            finally:
                with lock:
                    active -= 1
        with patch.object(resume, "ThreadPoolExecutor", TrackingPool):
            completed = list(resume.bounded_results(range(37286), verify, workers=worker_count))
        self.assertEqual(set(completed), set(range(37286)))
        self.assertEqual(len(completed), 37286)
        self.assertEqual(maximum_active, worker_count)
        self.assertLessEqual(maximum_retained, worker_count)
        self.assertEqual(retained, 0)

    def test_first_failure_does_not_submit_the_remaining_catalog(self):
        submitted = []
        def items():
            for index in range(37286):
                submitted.append(index)
                yield index
        def verify(index):
            raise ValueError("injected permanent failure")
        with self.assertRaisesRegex(ValueError, "permanent failure"):
            list(resume.bounded_results(items(), verify, workers=16))
        self.assertLessEqual(len(submitted), 16)


class ReadTransportTests(unittest.TestCase):
    def test_production_sized_artifact_uses_its_own_bound_and_extracts_required_diagnostics(self):
        # The real source archive is 183,693,428 bytes (~175 MiB), and includes
        # other diagnostic snapshots beyond the four required receipts.
        output = io.BytesIO()
        required = {name: encoded({"status": "passed"}) for name in resume.DIAGNOSTICS}
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_STORED) as archive:
            for name, body in required.items():
                archive.writestr(name, body)
            with archive.open("other-diagnostic-snapshot.bin", "w") as padding:
                chunk = b"x" * (1024 * 1024)
                for _ in range(175):
                    padding.write(chunk)
        payload = output.getvalue()
        self.assertGreater(len(payload), resume.MAX_API_BYTES)
        self.assertLess(len(payload), resume.MAX_ARTIFACT_DOWNLOAD_BYTES)
        client = resume.GitHubClient("private-test-token")
        client.opener = Mock()
        response = io.BytesIO(payload)
        client.opener.open.return_value = response
        artifacts = {"artifacts": [{
            "id": 99, "name": "neutral-translation-diagnostics-321-1", "expired": False,
            "workflow_run": {"id": 321}, "size_in_bytes": len(payload),
        }]}
        with tempfile.TemporaryDirectory() as destination, patch.object(client, "json", return_value=artifacts):
            resume.download_diagnostics(client, REPO, 321, 1, Path(destination))
            for name, body in required.items():
                self.assertEqual((Path(destination) / name).read_bytes(), body)
            self.assertEqual(set(path.name for path in Path(destination).iterdir()), set(required))
        self.assertTrue(response.closed)

    def test_artifact_reader_rejects_invalid_size_and_still_bounds_actual_response(self):
        client = resume.GitHubClient("private-test-token")
        client.opener = Mock()
        path = "/repos/example/repository/actions/artifacts/99/zip"
        for size in (None, 0, -1, True, "100", resume.MAX_ARTIFACT_DOWNLOAD_BYTES + 1):
            with self.subTest(size=size), self.assertRaisesRegex(resume.ResumeError, "download size"):
                client.artifact_bytes(path, size_in_bytes=size)
        client.opener.open.assert_not_called()
        oversized = io.BytesIO(b"12345")
        client.opener.open.return_value = oversized
        with self.assertRaisesRegex(resume.ResumeError, "oversized"):
            client.artifact_bytes(path, size_in_bytes=4)
        self.assertTrue(oversized.closed)
        with self.assertRaisesRegex(resume.ResumeError, "artifact route"):
            client.artifact_bytes("/repos/example/repository/actions/jobs/123/logs", size_in_bytes=100)

    def test_api_and_log_reader_keep_the_smaller_default_bound(self):
        client = resume.GitHubClient("private-test-token")
        client.opener = Mock()
        for path in ("/repos/example/repository/actions/jobs/123/logs", "/repos/example/repository/actions/runs/321"):
            response = io.BytesIO(b"12345")
            client.opener.open.return_value = response
            with self.subTest(path=path), patch.object(resume, "MAX_API_BYTES", 4):
                with self.assertRaisesRegex(resume.ResumeError, "oversized"):
                    client.bytes(path)
            self.assertTrue(response.closed)

    def test_github_redirect_keeps_https_and_strips_cross_host_authorization(self):
        handler = resume.GitHubRedirect()
        request = Request("https://api.github.com/repos/example/repository/actions/artifacts/99/zip",
                          headers={"Authorization": "Bearer private-test-token"})
        redirected = handler.redirect_request(request, None, 302, "", {}, "https://downloads.example.invalid/archive")
        self.assertIsNone(redirected.get_header("Authorization"))
        same_host = handler.redirect_request(request, None, 302, "", {}, "https://api.github.com/archive")
        self.assertEqual(same_host.get_header("Authorization"), "Bearer private-test-token")
        with self.assertRaisesRegex(resume.ResumeError, "outside HTTPS"):
            handler.redirect_request(request, None, 302, "", {}, "http://downloads.example.invalid/archive")

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
