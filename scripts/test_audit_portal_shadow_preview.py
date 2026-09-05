#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
import sys
from unittest import mock
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_portal_shadow_preview.py"
SPEC = importlib.util.spec_from_file_location("audit_portal_shadow_preview", SCRIPT)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


BASE_URL = "https://portal-locale-shadow.example.workers.dev"
PUBLIC_ORIGIN = "https://portal.example.invalid"
RELEASE = "a" * 32
TREE = "b" * 64


class FakeHeaders(dict[str, str]):
    def get(self, key: str, default=None):  # noqa: ANN001, ANN201
        target = key.casefold()
        for name, value in self.items():
            if name.casefold() == target:
                return value
        return default


class FakeResponse:
    def __init__(
        self,
        body: bytes,
        *,
        headers: dict[str, str] | None = None,
        status: int = 200,
    ) -> None:
        self.body = body
        self.headers = FakeHeaders(headers or {})
        self.status = status

    def read(self, limit: int = -1) -> bytes:
        if limit < 0:
            return self.body
        return self.body[:limit]


class FakeOpener:
    def __init__(self, responses: dict[str, FakeResponse | BaseException]) -> None:
        self.responses = responses
        self.requests = []

    def open(self, request, timeout: int):  # noqa: ANN001, ANN201
        if timeout != 30:
            raise AssertionError(f"unexpected timeout: {timeout}")
        parsed = urlsplit(request.full_url)
        if f"{parsed.scheme}://{parsed.netloc}" != BASE_URL:
            raise AssertionError(f"audit escaped the shadow origin: {request.full_url}")
        relative = parsed.path + (("?" + parsed.query) if parsed.query else "")
        self.requests.append(request)
        response = self.responses.get(relative)
        if response is None:
            raise URLError(f"missing fake response for {relative}")
        if isinstance(response, BaseException):
            raise response
        return response


def protected_headers(locale: str | None = None) -> dict[str, str]:
    headers = {"X-Robots-Tag": audit.SHADOW_ROBOTS_HEADER}
    if locale is not None:
        headers["Content-Language"] = locale
    return headers


def sample_plan() -> dict:
    samples = []
    for locale, direction in audit.LOCALES.items():
        for kind, path, forbid_zsxq in (
            ("home", f"/{locale}/", False),
            ("blog", f"/{locale}/blog/", True),
            ("blog-detail", f"/{locale}/blog/market-outlook.html", True),
            ("reports", f"/{locale}/reports/", False),
            ("report-detail", f"/{locale}/reports/ai-industry.html", False),
            ("charts", f"/{locale}/charts.html", False),
        ):
            samples.append({
                "kind": kind,
                "locale": locale,
                "direction": direction,
                "path": path,
                "forbid_zsxq": forbid_zsxq,
            })
    return {"schema_version": 1, "samples": samples}


def locale_html(locale: str, direction: str) -> bytes:
    return (
        f'<!doctype html><html lang="{locale}" dir="{direction}"><head>'
        '<link rel="stylesheet" href="/assets/locale.css">'
        '<script src="/assets/locale-runtime.js"></script>'
        f'<script src="/{locale}/assets/app.js"></script>'
        "</head><body>translated locale page</body></html>"
    ).encode("utf-8")


def write_plan_site(root: Path) -> None:
    for sample in sample_plan()["samples"]:
        relative = sample["path"].lstrip("/")
        if relative.endswith("/"):
            relative += "index.html"
        page = root / relative
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_bytes(locale_html(sample["locale"], sample["direction"]))


def manifest_fixture() -> tuple[dict, dict[str, bytes]]:
    manifest = {
        "schema_version": 1,
        "quality_gate_version": 3,
        "locales": list(audit.LOCALES),
        "coverage": {locale: 1.0 for locale in audit.LOCALES},
        "catalog_overlays": {locale: {} for locale in audit.LOCALES},
        "catalog_detail_overlays": {locale: {} for locale in audit.LOCALES},
        "locale_data_files": {locale: {} for locale in audit.LOCALES},
        "chart_overlays": {},
        "hot_report_overlays": {},
    }
    bodies: dict[str, bytes] = {}

    def row(path: str, body: bytes) -> dict:
        bodies["/" + path] = body
        return {
            "path": path,
            "byte_size": len(body),
            "sha256": hashlib.sha256(body).hexdigest(),
        }

    for locale in audit.LOCALES:
        manifest["catalog_overlays"][locale]["public"] = row(
            f"data/i18n/{locale}/catalog.json",
            json.dumps({"locale": locale, "kind": "catalog"}).encode("utf-8"),
        )
        manifest["chart_overlays"][locale] = row(
            f"data/i18n/{locale}/charts.json",
            json.dumps({"locale": locale, "kind": "charts"}).encode("utf-8"),
        )
        manifest["hot_report_overlays"][locale] = row(
            f"data/i18n/{locale}/hot-reports.json",
            json.dumps({"locale": locale, "kind": "hot-reports"}).encode("utf-8"),
        )
    manifest["required_paths"] = sorted(path.removeprefix("/") for path in bodies)
    return manifest, bodies


def response_fixture() -> tuple[dict, dict[str, FakeResponse | BaseException]]:
    plan = sample_plan()
    responses: dict[str, FakeResponse | BaseException] = {
        "/.well-known/edge-state": FakeResponse(
            json.dumps({
                "schema_version": 1,
                "release_id": RELEASE,
                "tree_sha256": TREE,
                "slot": "b",
            }).encode("utf-8"),
            headers=protected_headers(),
        ),
        "/robots.txt": FakeResponse(audit.SHADOW_ROBOTS, headers=protected_headers()),
        "/assets/locale.css": FakeResponse(b"html[dir=rtl]{direction:rtl}", headers=protected_headers()),
        "/assets/locale-runtime.js": FakeResponse(b"window.KC_LOCALE=true;", headers=protected_headers()),
    }
    for sample in plan["samples"]:
        locale = sample["locale"]
        responses[sample["path"]] = FakeResponse(
            locale_html(locale, sample["direction"]),
            headers=protected_headers(locale),
        )
        responses[f"/{locale}/assets/app.js"] = FakeResponse(
            f"window.locale='{locale}';".encode("utf-8"),
            headers=protected_headers(locale),
        )
    manifest, data_bodies = manifest_fixture()
    responses["/data/i18n/manifest.json"] = FakeResponse(
        json.dumps(manifest, sort_keys=True).encode("utf-8"),
        headers=protected_headers(),
    )
    for path, body in data_bodies.items():
        locale = path.split("/")[3]
        responses[path] = FakeResponse(body, headers=protected_headers(locale))
    for locale in audit.LOCALES:
        responses[f"/sitemap-{locale}.xml"] = FakeResponse(
            (
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                f"<url><loc>https://portal.example.invalid/{locale}/</loc></url>"
                f"<url><loc>https://portal.example.invalid/{locale}/blog/</loc></url>"
                "</urlset>"
            ).encode("utf-8"),
            headers=protected_headers(locale),
        )
        responses[f"/{locale}/feed.xml"] = FakeResponse(
            (
                "<rss version='2.0'><channel>"
                f"<language>{locale}</language>"
                f"<link>https://portal.example.invalid/{locale}/</link>"
                f"<item><link>https://portal.example.invalid/{locale}/blog/market-outlook.html</link>"
                f"<guid>https://portal.example.invalid/{locale}/blog/market-outlook.html</guid></item>"
                "</channel></rss>"
            ).encode("utf-8"),
            headers=protected_headers(locale),
        )
    return plan, responses


def replace_json_response(
    responses: dict[str, FakeResponse | BaseException],
    path: str,
    mutator,
) -> None:
    response = responses[path]
    assert isinstance(response, FakeResponse)
    payload = json.loads(response.body)
    mutator(payload)
    responses[path] = FakeResponse(
        json.dumps(payload, sort_keys=True).encode("utf-8"),
        headers=dict(response.headers),
        status=response.status,
    )


class ShadowPreviewAuditTests(unittest.TestCase):
    def run_audit(
        self,
        plan: dict,
        responses: dict[str, FakeResponse | BaseException],
        *,
        base_url: str = BASE_URL,
        expected_release: str = RELEASE,
        expected_tree: str = TREE,
    ):
        opener = FakeOpener(responses)
        with tempfile.TemporaryDirectory() as directory:
            samples = Path(directory) / "samples.json"
            samples.write_text(json.dumps(plan), encoding="utf-8")
            with (
                mock.patch.object(audit, "build_opener", return_value=opener),
                mock.patch.object(audit.time, "sleep"),
            ):
                result = audit.audit_preview(
                    base_url,
                    PUBLIC_ORIGIN,
                    samples,
                    expected_release,
                    expected_tree,
                )
        return result, opener

    def test_build_plan_covers_each_locale_surface_and_zsxq_cleanup_sample(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_zsxq = root / "blog" / "z-paid-note.html"
            source_zsxq.parent.mkdir(parents=True)
            source_zsxq.write_text("<html><body><img src='https://zsxq.img/x'></body></html>", encoding="utf-8")
            for locale in audit.LOCALES:
                locale_root = root / locale
                for path in (
                    locale_root / "index.html",
                    locale_root / "blog" / "index.html",
                    locale_root / "blog" / "a-public-note.html",
                    locale_root / "blog" / "z-paid-note.html",
                    locale_root / "reports" / "index.html",
                    locale_root / "reports" / "industry.html",
                    locale_root / "charts.html",
                ):
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text("<html></html>", encoding="utf-8")

            plan = audit.build_plan(root)
            samples = audit.validate_samples(plan)
            self.assertEqual(len(samples), 21)
            for locale in audit.LOCALES:
                locale_samples = [row for row in samples if row["locale"] == locale]
                self.assertEqual(
                    {row["kind"] for row in locale_samples},
                    set(audit.REQUIRED_SAMPLE_KINDS) | {"blog-zsxq-clean"},
                )
                self.assertIn(f"/{locale}/blog/z-paid-note.html", {row["path"] for row in locale_samples})

    def test_build_plan_requires_real_detail_pages(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            locale_root = root / "ko"
            for path in (
                locale_root / "index.html",
                locale_root / "blog" / "index.html",
                locale_root / "reports" / "index.html",
                locale_root / "reports" / "detail.html",
                locale_root / "charts.html",
            ):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("<html></html>", encoding="utf-8")
            with self.assertRaisesRegex(audit.AuditError, "no blog detail"):
                audit.build_plan(root)

    def test_first_detail_skips_deferred_notices_and_noindex_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            blog = root / "blog"
            blog.mkdir()
            (blog / "a-notice.html").write_text(
                '<html><body><main data-kc-locale-deferred="true">Generic translated notice</main></body></html>',
                encoding="utf-8",
            )
            (blog / "b-noindex.html").write_text(
                "<html><head><meta content='NOINDEX, FOLLOW' name='robots'></head><body>Unpublished old article</body></html>",
                encoding="utf-8",
            )
            published = blog / "c-published.html"
            published.write_text(
                '<html><head><meta name="robots" content="index,follow"></head><body>Published article</body></html>',
                encoding="utf-8",
            )
            self.assertEqual(audit.first_detail(root, "blog"), published)
            published.write_text('<html><meta name="robots" content="none"></html>', encoding="utf-8")
            with self.assertRaisesRegex(audit.AuditError, "no published blog detail"):
                audit.first_detail(root, "blog")

    def test_build_plan_zsxq_uses_published_counterpart_not_first_chinese_source(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_plan_site(root)
            source_blog = root / "blog"
            source_blog.mkdir()
            for name in ("a-unreleased.html", "z-published.html"):
                (source_blog / name).write_text('<html><img src="https://zsxq.img/image"></html>', encoding="utf-8")
            for locale, direction in audit.LOCALES.items():
                (root / locale / "blog/a-unreleased.html").write_text(
                    '<html><main data-kc-locale-deferred="true">Translated notice</main></html>', encoding="utf-8",
                )
                (root / locale / "blog/z-published.html").write_bytes(locale_html(locale, direction))
            plan = audit.build_plan(root)
            self.assertEqual(len(audit.validate_samples(plan)), 21)
            for locale in audit.LOCALES:
                self.assertEqual(plan["zsxq_cleanup"][locale], {
                    "status": "sampled", "path": f"/{locale}/blog/z-published.html",
                })
                self.assertFalse(any("a-unreleased.html" in row["path"] for row in plan["samples"]))

    def test_unreleased_image_source_is_explicitly_not_applicable_in_audit_result(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_plan_site(root)
            source = root / "blog/a-unreleased.html"
            source.parent.mkdir()
            source.write_text('<html><img src="https://zsxq.img/image"></html>', encoding="utf-8")
            for locale in audit.LOCALES:
                (root / locale / "blog/a-unreleased.html").write_text(
                    '<html><meta name="robots" content="noindex,follow"><main data-kc-locale-deferred="true">Notice</main></html>',
                    encoding="utf-8",
                )
            plan = audit.build_plan(root)
        self.assertEqual(len(audit.validate_samples(plan)), 18)
        _, responses = response_fixture()
        result, opener = self.run_audit(plan, responses)
        for locale in audit.LOCALES:
            self.assertEqual(result["zsxq_cleanup"][locale], {
                "status": "not_applicable", "reason": "no-published-localized-source-image-page",
            })
        self.assertEqual(result["sample_count"], 18)
        self.assertEqual(result["asset_count"], 5)
        self.assertEqual(len(opener.requests), len(responses))
        self.assertEqual({row["path"] for row in result["checks"]}, set(responses))

    def test_zsxq_source_already_selected_as_detail_is_verified_without_duplicate_fetch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_plan_site(root)
            source = root / "blog/market-outlook.html"
            source.parent.mkdir()
            source.write_text('<html><img src="https://zsxq.img/image"></html>', encoding="utf-8")
            plan = audit.build_plan(root)
        _, responses = response_fixture()
        result, opener = self.run_audit(plan, responses)
        self.assertEqual(result["sample_count"], 18)
        self.assertEqual(len(opener.requests), len(responses))
        for locale in audit.LOCALES:
            self.assertEqual(result["zsxq_cleanup"][locale], {
                "status": "passed", "path": f"/{locale}/blog/market-outlook.html",
            })

    def test_shadow_detail_cannot_change_to_a_notice_after_plan_selection(self) -> None:
        for marker in (
            '<main data-kc-locale-deferred="true">Notice</main>',
            '<meta name="robots" content="noindex,follow">',
        ):
            with self.subTest(marker=marker):
                plan, responses = response_fixture()
                path = "/ko/blog/market-outlook.html"
                body = locale_html("ko", "ltr").replace(b"</body>", marker.encode("utf-8") + b"</body>")
                responses[path] = FakeResponse(body, headers=protected_headers("ko"))
                with self.assertRaisesRegex(audit.AuditError, "not published content"):
                    self.run_audit(plan, responses)

    def test_unverified_zsxq_path_cannot_be_claimed_as_sampled(self) -> None:
        plan, responses = response_fixture()
        plan["zsxq_cleanup"] = {
            locale: {"status": "sampled", "path": f"/{locale}/blog/not-in-plan.html"}
            for locale in audit.LOCALES
        }
        with self.assertRaisesRegex(audit.AuditError, "cleanup applicability is invalid"):
            self.run_audit(plan, responses)

    def test_full_offline_shadow_audit_succeeds(self) -> None:
        plan, responses = response_fixture()
        result, opener = self.run_audit(plan, responses)
        self.assertEqual(result["release_id"], RELEASE)
        self.assertEqual(result["tree_sha256"], TREE)
        self.assertEqual(result["sample_count"], 18)
        self.assertEqual(result["asset_count"], 5)
        self.assertEqual({row["path"] for row in result["checks"]}, set(responses))
        self.assertEqual(len(opener.requests), len(responses))
        for request in opener.requests:
            self.assertEqual(request.get_header("Cache-control"), "no-cache")
            self.assertEqual(request.get_header("User-agent"), "Portal-Shadow-Audit/1.0")

    def test_rejects_non_bare_or_malformed_shadow_origins_before_network(self) -> None:
        plan, responses = response_fixture()
        for value in (
            "http://shadow.example.workers.dev",
            "https://workers.dev",
            "https://evilworkers.dev",
            "https://bad_label.example.workers.dev",
            "https://user@shadow.example.workers.dev",
            "https://shadow.example.workers.dev:not-a-port",
            "https://shadow.example.workers.dev/path",
            "https://shadow.example.workers.dev/?query=1",
        ):
            with self.subTest(value=value):
                with self.assertRaisesRegex(audit.AuditError, "bare workers.dev HTTPS origin"):
                    self.run_audit(plan, responses, base_url=value)

    def test_rejects_unsafe_or_incomplete_sample_plans_before_network(self) -> None:
        for mutation, message in (
            (
                lambda plan: plan["samples"][0].update(path="/ko/%2e%2e/robots.txt"),
                "Unsafe preview path",
            ),
            (
                lambda plan: plan["samples"].__setitem__(
                    -1,
                    dict(plan["samples"][0]),
                ),
                "duplicated|incomplete|invalid",
            ),
        ):
            plan, responses = response_fixture()
            mutation(plan)
            with self.subTest(message=message):
                with self.assertRaisesRegex(audit.AuditError, message):
                    self.run_audit(plan, responses)

    def test_rejects_wrong_edge_release_or_tree_identity(self) -> None:
        plan, responses = response_fixture()
        replace_json_response(
            responses,
            "/.well-known/edge-state",
            lambda payload: payload.update(tree_sha256="c" * 64),
        )
        with self.assertRaisesRegex(audit.AuditError, "does not match"):
            self.run_audit(plan, responses)

    def test_requires_x_robots_tag_on_every_response(self) -> None:
        plan, responses = response_fixture()
        response = responses["/.well-known/edge-state"]
        assert isinstance(response, FakeResponse)
        response.headers.clear()
        with self.assertRaisesRegex(audit.AuditError, "indexing header is missing"):
            self.run_audit(plan, responses)

    def test_requires_global_robots_disallow(self) -> None:
        plan, responses = response_fixture()
        responses["/robots.txt"] = FakeResponse(
            b"User-agent: *\nAllow: /\n",
            headers=protected_headers(),
        )
        with self.assertRaisesRegex(audit.AuditError, "does not disallow"):
            self.run_audit(plan, responses)

    def test_requires_arabic_rtl_and_locale_content_language(self) -> None:
        plan, responses = response_fixture()
        responses["/ar/"] = FakeResponse(
            locale_html("ar", "ltr"),
            headers=protected_headers("ar"),
        )
        with self.assertRaisesRegex(audit.AuditError, "direction is invalid"):
            self.run_audit(plan, responses)

        plan, responses = response_fixture()
        response = responses["/ja/"]
        assert isinstance(response, FakeResponse)
        response.headers["Content-Language"] = "ko"
        with self.assertRaisesRegex(audit.AuditError, "wrong Content-Language"):
            self.run_audit(plan, responses)

    def test_rejects_zsxq_images_from_localized_blog(self) -> None:
        plan, responses = response_fixture()
        response = responses["/ko/blog/market-outlook.html"]
        assert isinstance(response, FakeResponse)
        response.body = response.body.replace(
            b"</body>",
            b"<img src='https://zsxq.img/private.png'></body>",
        )
        with self.assertRaisesRegex(audit.AuditError, "still contains zsxq.img"):
            self.run_audit(plan, responses)

    def test_rejects_incomplete_or_cross_locale_manifest(self) -> None:
        plan, responses = response_fixture()
        replace_json_response(
            responses,
            "/data/i18n/manifest.json",
            lambda payload: payload["coverage"].update(ar=0.99),
        )
        with self.assertRaisesRegex(audit.AuditError, "manifest is incomplete"):
            self.run_audit(plan, responses)

        plan, responses = response_fixture()

        def cross_locale(payload: dict) -> None:
            row = payload["chart_overlays"]["ko"]
            old_path = row["path"]
            row["path"] = "data/i18n/ja/crossed.json"
            payload["required_paths"].remove(old_path)
            payload["required_paths"].append(row["path"])
            payload["required_paths"].sort()

        replace_json_response(responses, "/data/i18n/manifest.json", cross_locale)
        with self.assertRaisesRegex(audit.AuditError, "crosses locale boundaries"):
            self.run_audit(plan, responses)

    def test_verifies_manifest_data_size_and_digest(self) -> None:
        plan, responses = response_fixture()
        response = responses["/data/i18n/ja/charts.json"]
        assert isinstance(response, FakeResponse)
        response.body += b"tampered"
        with self.assertRaisesRegex(audit.AuditError, "does not match its manifest"):
            self.run_audit(plan, responses)

    def test_validates_locale_sitemap_and_feed(self) -> None:
        plan, responses = response_fixture()
        responses["/sitemap-ar.xml"] = FakeResponse(
            b"<urlset><url><loc>https://portal.example.invalid/ja/</loc></url></urlset>",
            headers=protected_headers("ar"),
        )
        with self.assertRaisesRegex(audit.AuditError, "sitemap has an invalid locale URL"):
            self.run_audit(plan, responses)

        plan, responses = response_fixture()
        response = responses["/ja/feed.xml"]
        assert isinstance(response, FakeResponse)
        response.body = response.body.replace(b"<language>ja</language>", b"<language>ko</language>")
        with self.assertRaisesRegex(audit.AuditError, "feed has the wrong language"):
            self.run_audit(plan, responses)

    def test_missing_or_redirected_locale_asset_fails_closed(self) -> None:
        plan, responses = response_fixture()
        redirect = HTTPError(
            BASE_URL + "/assets/locale-runtime.js",
            302,
            "Found",
            {},
            None,
        )
        responses["/assets/locale-runtime.js"] = redirect
        try:
            with self.assertRaisesRegex(audit.AuditError, "fetch failed after retries"):
                self.run_audit(plan, responses)
        finally:
            redirect.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
