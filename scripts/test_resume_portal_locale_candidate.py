#!/usr/bin/env python3
"""No-network resume proof using in-memory GitHub and R2 fixtures."""
from __future__ import annotations

import copy
import gzip
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch
from urllib.error import HTTPError
import zipfile

import publish_static_slot as publisher
import resume_portal_locale_candidate as resume
import verify_portal_chinese_parity as parity
from test_publish_static_slot import FakeR2


REPO = "example/repository"
ORIGIN = "https://portal.example.invalid"
COMMIT = "1" * 40
RELEASE = "2" * 32
PREVIOUS = {"schema_version": 1, "slot": "a", "release_id": "3" * 32, "tree_sha256": "4" * 64}


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
        app = b"console.log('Chinese app remains unchanged');"
        files["assets/app.js"] = app
        for locale in resume.LOCALES:
            for path in ("index.html", "blog/index.html", "blog/new.html", "reports/index.html", "reports/new.html", "charts.html"):
                files[locale + "/" + path] = ("locale page " + path).encode()
                files[path] = ("Chinese page " + path).encode()
        files["blog/historical.html"] = b"historical content must not be downloaded"
        for name in publisher.DEFAULT_RUNTIME_PATHS:
            files.setdefault(name, b"{}")
        locale_manifest = {"quality_gate_version": 3, "locales": list(resume.LOCALES),
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
        report = parity._with_digest({"schema_version": 1, "kind": parity.VERIFY_KIND, "site_origin": ORIGIN,
                                      "snapshot_digest": "5" * 64, "verified_tree_digest": "6" * 64, "counts": {"files": len(files)}})
        performance = {"schema_version": 1, "candidate_bytes": len(app), "candidate_gzip_bytes": len(gzip.compress(app, mtime=0)),
                       "candidate_sha256": hashlib.sha256(app).hexdigest(), "active_compared": True,
                       "raw_delta_bytes": 0, "gzip_delta_bytes": 0}
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

    def restore(self, **kwargs):
        options = dict(github=self.github, client=self.r2, bucket="bucket", repository=REPO, run_id=321, run_attempt=1,
                       site_dir=self.site, diagnostics_dir=self.diag, work_dir=self.work, origin=ORIGIN,
                       expected_slot="b", expected_release=RELEASE, expected_tree=self.tree, expected_commit=COMMIT,
                       expected_previous_release=PREVIOUS["release_id"], expected_previous_tree=PREVIOUS["tree_sha256"],
                       fetch_live=self.live, workers=4)
        return resume.resume_candidate(**{**options, **kwargs})

    def test_complete_restore_verifies_all_metadata_downloads_only_audit_files_and_never_mutates_remote(self):
        result = self.restore()
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
