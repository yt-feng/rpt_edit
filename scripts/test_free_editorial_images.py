from __future__ import annotations

import io
import json
import contextlib
import hashlib
import statistics
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image, ImageDraw
from requests.exceptions import SSLError

import free_editorial_images as media


class Response:
    def __init__(self, body=b"", *, status=200, content_type="application/json", headers=None, url=None):
        self.body = body
        self.status_code = status
        self.headers = {"Content-Type": content_type, **(headers or {})}
        self.closed = False
        if url is not None:
            self.url = url

    def iter_content(self, chunk_size):
        for start in range(0, len(self.body), chunk_size):
            yield self.body[start:start + chunk_size]

    def raise_for_status(self):
        if self.status_code >= 400:
            raise ValueError("http_error")

    def close(self):
        self.closed = True


class Session:
    def __init__(self, responses=()):
        self.responses = list(responses)
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append((url, kwargs))
        if not self.responses:
            raise AssertionError("unexpected network request")
        result = self.responses.pop(0)
        if isinstance(result, Exception):
            raise result
        return result


def picture(seed=1, size=(960, 600), image_format="PNG"):
    image = Image.new("RGB", size, "#244768")
    draw = ImageDraw.Draw(image)
    for i in range(35):
        x, y = (i * 57 + seed * 37) % 850, (i * 81) % 470
        draw.rectangle((x, y, x + 100, y + 110), fill=(i * 7 % 255, 140 + i % 100, i * 17 % 255))
    result = io.BytesIO()
    image.save(result, image_format)
    return result.getvalue()


def page(identifier=1, *, license_name="CC BY 4.0", license_url="https://creativecommons.org/licenses/by/4.0/", author="Example Author"):
    return {"pageid": identifier, "imageinfo": [{
        "mime": "image/png", "width": 960, "height": 600,
        "url": f"https://upload.wikimedia.org/wikipedia/commons/a/ab/Photo{identifier}.png",
        "descriptionurl": f"https://commons.wikimedia.org/wiki/File:Photo{identifier}.png",
        "extmetadata": {"Artist": {"value": author}, "LicenseShortName": {"value": license_name},
                        "LicenseUrl": {"value": license_url}},
    }]}


def results(*pages):
    return Response(json.dumps({"query": {"pages": list(pages)}}).encode())


def download_response(seed=1):
    return Response(picture(seed), content_type="image/png")


def thumbnail_page(identifier=1, **kwargs):
    item = page(identifier, **kwargs)
    item.update(ns=6, title=f"File:Photo{identifier}.png", imagerepository="local")
    info = item["imageinfo"][0]
    info.update(width=12000, height=8000, size=24 * 1024 * 1024,
                thumburl=f"https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Photo{identifier}.png/1280px-Photo{identifier}.png",
                thumbwidth=1280, thumbheight=853, thumbmime="image/png")
    return item


def expected_diagnostics(**values):
    result = dict(search_results=0, admitted=0, rejections={}, validation_failures={},
                  thumbnail_candidates=0, original_candidates=0, thumbnail_attempts=0, original_attempts=0)
    result.update(values)
    return result


class EditorialImagesTest(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        self.target = self.root / "image.jpg"
        self.reset_provider()

    def reset_provider(self):
        for name in ("_SEARCH_CACHE", "_USED", "_SELECTIONS", "_BATCH_URL_OWNERS", "_BATCH_CONTENT_OWNERS", "_LOADED_SELECTION_CACHES"):
            getattr(media, name).clear()
        media._COOLDOWN_UNTIL = 0.0
        media._COOLDOWN_REASON = ""

    def tearDown(self):
        self.directory.cleanup()

    def run_provider(self, session, title="半导体研发", **kwargs):
        return media.download_editorial_image(session, title, self.target, 15, **kwargs)

    def test_downloads_licensed_image_and_never_transmits_private_title(self):
        session = Session([results(page()), download_response()])
        path, info = self.run_provider(session, "私密报告 未公开客户名字 2026 芯片需求")
        self.assertEqual(info["source"], "wikimedia_commons")
        self.assertEqual(info["license"], "CC BY 4.0")
        self.assertEqual(info["author"], "Example Author")
        with Image.open(path) as image:
            self.assertEqual(image.size, (1200, 675))
        self.assertEqual(len(session.calls), 2)
        requests = json.dumps(session.calls, ensure_ascii=False)
        self.assertNotIn("私密", requests)
        self.assertNotIn("客户名字", requests)
        self.assertIn("semiconductor", requests)
        self.assertEqual(info["search_diagnostics"], expected_diagnostics(
            search_results=1, admitted=1, original_candidates=1, original_attempts=1))
        self.assertTrue(all(not call[1]["allow_redirects"] for call in session.calls))
        self.assertTrue(all(call[1]["timeout"] <= 10 for call in session.calls))

    def test_discovery_uses_official_category_union_and_fixed_topic_only(self):
        for title in ("芯片 私密客户原文", "金融 未公开2027预测", "能源 一家公司"):
            session = Session([results()])
            self.run_provider(session, title)
            query = session.calls[0][1]["params"]["gsrsearch"]
            self.assertEqual(query.count("incategory:"), 1)
            self.assertIn('incategory:"CC-Zero|CC-BY-2.0|CC-BY-2.5|CC-BY-3.0|CC-BY-4.0"', query)
            self.assertNotIn(" OR ", query)
            self.assertNotIn("CC-BY-SA", query)
            self.assertNotIn("2027", query)
            self.assertTrue(query.isascii())
        self.assertEqual(media._topic("能源")[1], "solar panels")
        self.assertEqual(media._topic("金融")[1], "city skyline")

    def test_search_filter_has_its_own_cache_identity(self):
        cache = self.root / "cache"; cache.mkdir()
        query = media._topic("芯片")[1]
        stale = {"time": media.time.time(), "results": []}
        for old_key in (query, media._search_query(query)):
            (cache / (hashlib.sha256(old_key.encode()).hexdigest() + ".json")).write_text(json.dumps(stale))
            media._SEARCH_CACHE[old_key] = (media.time.time(), [])
        session = Session([results(page()), download_response()])
        _, info = self.run_provider(session, cache_dir=cache)
        self.assertEqual(info["source"], "wikimedia_commons")
        self.assertEqual(len(session.calls), 2)

    def test_search_diagnostics_distinguish_empty_from_rejected_metadata(self):
        _, empty = self.run_provider(Session([results()]))
        self.assertEqual(empty["search_diagnostics"], expected_diagnostics())
        self.reset_provider()
        no_license = page(1, license_name="CC BY-SA 4.0", license_url="https://creativecommons.org/licenses/by-sa/4.0/")
        wrong_format = page(2); wrong_format["imageinfo"][0]["mime"] = "image/gif"
        wrong_url = page(3); wrong_url["imageinfo"][0]["url"] = "https://private.example/source.png"
        malformed = {"pageid": 4, "imageinfo": "private malformed data"}
        session = Session([results(no_license, wrong_format, wrong_url, malformed, page(5)), download_response()])
        _, info = self.run_provider(session)
        self.assertEqual(info["search_diagnostics"], expected_diagnostics(
            search_results=5, admitted=1, original_candidates=1, original_attempts=1,
            rejections={"license": 1, "format": 1, "url": 1, "metadata": 1}))
        self.assertNotIn("private", json.dumps(info["search_diagnostics"]))
        self.assertEqual(len(session.calls), 2)

    def test_diagnostics_serialization_never_accepts_untrusted_details(self):
        value = {"search_results": 100, "admitted": "private title",
                 "rejections": {"license": 3, "https://private.example": 1, "url": "private URL", "format": -1}}
        self.assertEqual(media._safe_diagnostics(value), expected_diagnostics(rejections={"license": 3}))

    def test_large_original_uses_reported_thumbnail_not_original_limits(self):
        item = thumbnail_page()
        session = Session([results(item), Response(picture(size=(1280, 853)), content_type="image/png")])
        _, info = self.run_provider(session)
        self.assertEqual(info["source"], "wikimedia_commons")
        self.assertEqual(info["download_variant"], "thumbnail")
        self.assertEqual(session.calls[1][0], item["imageinfo"][0]["thumburl"])
        self.assertNotEqual(session.calls[1][0], item["imageinfo"][0]["url"])
        params = session.calls[0][1]["params"]
        self.assertEqual((params["iiurlwidth"], params["iiurlheight"]), (1200, 1200))
        self.assertIn("thumbmime", params["iiprop"].split("|"))
        self.assertEqual(info["search_diagnostics"], expected_diagnostics(
            search_results=1, admitted=1, thumbnail_candidates=1, thumbnail_attempts=1))

    def test_bad_declared_geometry_does_not_exhaust_three_downloads(self):
        items = [thumbnail_page(i) for i in range(4)]
        for item in items[:3]:
            item["imageinfo"][0].update(thumbwidth=2400, thumbheight=400)
        session = Session([results(*items), download_response()])
        _, info = self.run_provider(session)
        self.assertEqual(info["source"], "wikimedia_commons")
        self.assertEqual(len(session.calls), 2)
        self.assertIn("Photo3.png", session.calls[1][0])
        self.assertEqual(info["search_diagnostics"], expected_diagnostics(
            search_results=4, admitted=1, thumbnail_candidates=1, thumbnail_attempts=1,
            rejections={"declared_geometry": 3}, validation_failures={"declared_aspect": 3}))

    def test_oversized_original_without_thumbnail_is_not_requested(self):
        for width, height, size, reason in ((6000, 4000, 1000, "declared_pixels"),
                                            (4000, 2500, 20 * 1024 * 1024, "declared_bytes"),
                                            (300, 200, 1000, "declared_small")):
            with self.subTest(reason=reason):
                self.reset_provider()
                item = page(); item["imageinfo"][0].update(width=width, height=height, size=size)
                session = Session([results(item)])
                _, info = self.run_provider(session)
                self.assertEqual(info["source"], "local_editorial")
                self.assertEqual(len(session.calls), 1)
                self.assertEqual(info["search_diagnostics"]["validation_failures"], {reason: 1})

    def test_thumbnail_host_and_mime_cannot_fall_back_to_original(self):
        for field, value, reason in (("thumburl", "https://private.example/image.png", "url"),
                                      ("thumbmime", "image/webp", "format")):
            with self.subTest(field=field):
                self.reset_provider()
                item = thumbnail_page(); item["imageinfo"][0][field] = value
                session = Session([results(item)])
                _, info = self.run_provider(session)
                self.assertEqual(info["source"], "local_editorial")
                self.assertEqual(len(session.calls), 1)
                self.assertEqual(info["search_diagnostics"]["rejections"], {reason: 1})

    def test_actual_bytes_still_enforce_all_image_guards(self):
        blank = io.BytesIO(); Image.new("RGB", (960, 600), "white").save(blank, "PNG")
        cases = [(b"broken", "image_decode"), (picture(size=(300, 200)), "image_too_small"),
                 (picture(size=(1800, 400)), "invalid_image_aspect"),
                 (picture(image_format="BMP"), "invalid_image_format"), (blank.getvalue(), "flat_image")]
        for payload, reason in cases:
            with self.subTest(reason=reason):
                self.reset_provider()
                session = Session([results(thumbnail_page()), Response(payload, content_type="image/png")])
                _, info = self.run_provider(session)
                self.assertEqual(info["source"], "local_editorial")
                self.assertEqual(info["search_diagnostics"]["validation_failures"], {reason: 1})
                self.assertEqual(len(session.calls), 2)
        with patch.object(media, "MAX_PIXELS", 500000):
            with self.assertRaisesRegex(ValueError, "image_too_many_pixels"):
                media._normalized_image(picture())

    def test_response_size_reason_is_fixed_and_never_contains_exception_details(self):
        session = Session([results(thumbnail_page()), Response(content_type="image/png",
                          headers={"Content-Length": str(media.MAX_IMAGE_BYTES + 1)})])
        _, info = self.run_provider(session)
        self.assertEqual(info["search_diagnostics"]["validation_failures"], {"response_too_large": 1})
        self.assertEqual(media._validation_reason(ValueError("private URL with title")), "other_validation")
        value = dict(validation_failures={"https://private.example": 1, "image_decode": 2,
                                          "invalid_image_aspect": "private text"}, thumbnail_attempts="private text")
        clean = media._safe_diagnostics(value)
        self.assertEqual(clean["validation_failures"], {"image_decode": 2})
        self.assertEqual(clean["thumbnail_attempts"], 0)
        self.assertNotIn("private", json.dumps(clean))

    def test_smoke_manifest_carries_thumbnail_validation_evidence(self):
        output = self.root / "smoke-thumbnail"
        wide = thumbnail_page(1); wide["imageinfo"][0].update(thumbwidth=2400, thumbheight=400)
        session = Session([results(wide, thumbnail_page(2)), download_response()])
        with patch.object(media.requests.Session, "get", side_effect=session.get), \
             patch("sys.argv", ["free_editorial_images.py", "--smoke-dir", str(output), "--require-commons"]), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(media._smoke_main(), 0)
        report = json.loads((output / "provider-report.json").read_text())
        self.assertEqual((report["search_results"], report["admitted"], report["network_requests"]), (2, 1, 2))
        self.assertEqual(report["validation_failures"], {"declared_aspect": 1})
        self.assertEqual((report["thumbnail_attempts"], report["original_attempts"]), (1, 0))
        self.assertEqual(report["source"], "wikimedia_commons")

    def test_restrictive_or_ambiguous_licenses_do_not_download(self):
        for name, url in [
            ("CC BY-SA 4.0", "https://creativecommons.org/licenses/by-sa/4.0/"),
            ("CC BY-NC 4.0", "https://creativecommons.org/licenses/by-nc/4.0/"),
            ("CC BY-ND 4.0", "https://creativecommons.org/licenses/by-nd/4.0/"),
            ("Public domain", ""),
            ("CC BY 4.0", "https://creativecommons.org.evil.test/licenses/by/4.0/"),
            ("CC BY 4.0", "https://creativecommons.org/licenses/by/4.0/?other=1"),
            ("CC BY 4.0", "https://creativecommons.org/licenses/by-nc/4.0/"),
        ]:
            with self.subTest(name=name, url=url):
                self.reset_provider()
                session = Session([results(page(license_name=name, license_url=url))])
                _, info = self.run_provider(session)
                self.assertEqual(info["source"], "local_editorial")
                self.assertEqual(len(session.calls), 1)

    def test_cc0_allowed_and_by_without_author_rejected(self):
        cc0 = page(license_name="CC0", license_url="http://creativecommons.org/publicdomain/zero/1.0/", author="")
        self.assertEqual(media._license(cc0["imageinfo"][0])["license"], "CC0 1.0")
        self.assertIsNone(media._license(page(author="")["imageinfo"][0]))

    def test_conflicting_license_fields_are_rejected(self):
        for key, value in [("License", "cc-by-nc-4.0"), ("License", "cc-by-sa-4.0"),
                           ("License", "cc0"), ("UsageTerms", "Attribution-NonCommercial 4.0"),
                           ("UsageTerms", "CC BY-ND 4.0")]:
            with self.subTest(key=key, value=value):
                info = page()["imageinfo"][0]
                info["extmetadata"][key] = {"value": value}
                self.assertIsNone(media._license(info))

    def test_preserves_safe_attribution_without_remote_html(self):
        item = page(author='<a href="https://bad.test">A &amp; B</a><script>do_bad()</script>')
        session = Session([results(item), download_response()])
        _, info = self.run_provider(session)
        self.assertEqual(info["author"], "A & B")
        rendered = media.attribution_html(info)
        self.assertIn("A &amp; B", rendered)
        self.assertIn("creativecommons.org/licenses/by/4.0/", rendered)
        self.assertNotIn("script", rendered)
        self.assertNotIn("bad.test", rendered)
        self.assertIn("非报告原图", rendered)
        self.assertIn('data-editorial-credit="1"', rendered)
        self.assertIn('图片来源：https://commons.wikimedia.org/wiki/File:', rendered)
        self.assertIn('许可：https://creativecommons.org/licenses/by/4.0/', rendered)
        self.assertNotIn('<a ', rendered)
        self.assertIn('font-size:11px', rendered)
        self.assertIn('word-break:break-all', rendered)
        self.assertIn('overflow-wrap:anywhere', rendered)

    def test_rejects_external_or_private_source_urls(self):
        for url in ("http://upload.wikimedia.org/a.png", "https://127.0.0.1/a.png",
                    "https://upload.wikimedia.org.evil.test/a.png", "https://user:password@upload.wikimedia.org/a.png",
                    "https://upload.wikimedia.org:8443/a.png", "file:///tmp/photo.png"):
            with self.subTest(url=url):
                self.reset_provider()
                item = page()
                item["imageinfo"][0]["url"] = url
                session = Session([results(item)])
                _, info = self.run_provider(session)
                self.assertEqual(info["source"], "local_editorial")
                self.assertEqual(len(session.calls), 1)

    def test_redirect_to_external_host_is_never_requested(self):
        response = Response(status=302, headers={"Location": "https://127.0.0.1/private"})
        session = Session([results(page()), response])
        _, info = self.run_provider(session)
        self.assertEqual(info["source"], "local_editorial")
        self.assertEqual(len(session.calls), 2)
        self.assertTrue(response.closed)

    def test_redirect_count_is_bounded_and_success_within_allowlist(self):
        target_url = "https://thumb.wikimedia.org/wikipedia/commons/a/ab/photo.png"
        session = Session([results(page()), Response(status=302, headers={"Location": target_url}), download_response()])
        _, info = self.run_provider(session)
        self.assertEqual(info["source"], "wikimedia_commons")
        self.assertEqual(len(session.calls), 3)
        self.reset_provider()
        media._USED.clear()
        session = Session([results(page())] + [Response(status=302, headers={"Location": target_url}) for _ in range(4)])
        _, info = self.run_provider(session)
        self.assertEqual(info["source"], "local_editorial")
        self.assertEqual(len(session.calls), 4)

    def test_tls_failure_stops_requests_and_uses_offline_art(self):
        session = Session([results(page(1), page(2)), SSLError("certificate verify failed")])
        _, info = self.run_provider(session)
        self.assertEqual(info["source"], "local_editorial")
        self.assertEqual(len(session.calls), 2)

    def test_one_outage_does_not_repeat_for_43_articles_across_topics(self):
        for failure in (SSLError("certificate verify failed"), Response(b"not json", content_type="text/html"),
                        Response(b"", status=429)):
            with self.subTest(failure=type(failure).__name__):
                self.reset_provider()
                media._COOLDOWN_UNTIL = 0.0
                session = Session([failure])
                for index in range(43):
                    title = ("芯片", "能源", "制造", "医疗", "货运", "零售", "金融")[index % 7] + str(index)
                    _, info = self.run_provider(session, title)
                    self.assertEqual(info["source"], "local_editorial")
                    self.assertIn(info["fallback_reason"], ("commons_tls_failed", "commons_unavailable"))
                self.assertEqual(len(session.calls), 1)

    def test_cooldown_does_not_block_already_cached_licensed_image(self):
        cache = self.root / "cache"
        _, first = self.run_provider(Session([results(page()), download_response()]), cache_dir=cache)
        media._COOLDOWN_UNTIL = media.time.monotonic() + 300
        media._COOLDOWN_REASON = "commons_unavailable"
        session = Session()
        _, cached = self.run_provider(session, cache_dir=cache)
        self.assertEqual(cached["source"], "wikimedia_commons")
        self.assertEqual(first["sha256"], cached["sha256"])
        self.assertEqual(session.calls, [])

    def test_cooldown_expires_and_allows_normal_recovery(self):
        media._COOLDOWN_UNTIL = media.time.monotonic() - 1
        session = Session([results(page()), download_response()])
        _, info = self.run_provider(session)
        self.assertEqual(info["source"], "wikimedia_commons")
        self.assertEqual(len(session.calls), 2)

    def test_empty_results_do_not_repeat_network_search(self):
        session = Session([results()])
        self.run_provider(session)
        self.run_provider(session, index=2)
        self.assertEqual(len(session.calls), 1)

    def test_reuses_topic_search_and_deduplicates_article_images(self):
        session = Session([results(page(1), page(2)), download_response(1), download_response(2)])
        _, first = self.run_provider(session, index=1)
        _, second = self.run_provider(session, index=2)
        _, third = self.run_provider(session, index=3)
        self.assertEqual(first["source"], "wikimedia_commons")
        self.assertEqual(second["source"], "wikimedia_commons")
        self.assertNotEqual(first["sha256"], second["sha256"])
        self.assertEqual(third["source"], "local_editorial")
        self.assertEqual(len(session.calls), 3)

    def test_image_content_dedupe_even_when_urls_differ(self):
        session = Session([results(page(1), page(2)), download_response(1), download_response(1)])
        _, first = self.run_provider(session, index=1)
        _, second = self.run_provider(session, index=2)
        self.assertEqual(first["source"], "wikimedia_commons")
        self.assertEqual(second["source"], "local_editorial")

    def test_commons_url_is_not_reused_by_different_articles(self):
        session = Session([results(page()), download_response()])
        _, first = self.run_provider(session, "芯片文章一")
        _, second = self.run_provider(session, "芯片文章二")
        self.assertEqual(first["source"], "wikimedia_commons")
        self.assertEqual(second["source"], "local_editorial")
        self.assertNotEqual(first["sha256"], second["sha256"])
        self.assertEqual(len(session.calls), 2)

    def test_commons_aliases_cannot_repeat_same_pixels_across_articles(self):
        session = Session([results(page(1), page(2)), download_response(), download_response()])
        _, first = self.run_provider(session, "芯片文章一")
        _, second = self.run_provider(session, "芯片文章二")
        _, third = self.run_provider(session, "芯片文章三")
        self.assertEqual(first["source"], "wikimedia_commons")
        self.assertEqual(second["source"], "local_editorial")
        self.assertEqual(third["source"], "local_editorial")
        self.assertEqual(len(session.calls), 3)

    def test_same_article_slot_reuses_exact_image_during_retry(self):
        session = Session([results(page(1), page(2)), download_response()])
        _, first = self.run_provider(session)
        original = self.target.read_bytes()
        _, retry = self.run_provider(session)
        self.assertEqual(first, retry)
        self.assertEqual(original, self.target.read_bytes())
        self.assertEqual(len(session.calls), 2)

    def test_persisted_claims_prevent_repeat_in_resumed_batch(self):
        cache = self.root / "cache"
        session = Session([results(page(1), page(2)), download_response(1)])
        _, first = self.run_provider(session, "芯片文章一", cache_dir=cache)
        self.reset_provider()
        resumed = Session([download_response(2)])
        _, second = self.run_provider(resumed, "芯片文章二", cache_dir=cache)
        self.assertNotEqual(first["sha256"], second["sha256"])
        self.assertEqual(second["source"], "wikimedia_commons")
        self.assertEqual(len(resumed.calls), 1)
        self.assertIn("Photo2.png", resumed.calls[0][0])

    def test_local_choice_persists_when_provider_recovers(self):
        cache = self.root / "cache"
        _, first = self.run_provider(Session([results()]), cache_dir=cache)
        original = self.target.read_bytes()
        self.reset_provider()
        session = Session()
        _, retry = self.run_provider(session, cache_dir=cache)
        self.assertEqual(first, retry)
        self.assertEqual(original, self.target.read_bytes())
        self.assertEqual(session.calls, [])

    def test_corrupt_selection_cannot_be_replayed(self):
        cache = self.root / "cache"
        self.run_provider(Session([results()]), cache_dir=cache)
        next(cache.glob("selection-*.jpg")).write_bytes(b"not an image")
        self.reset_provider()
        _, retry = self.run_provider(Session(), cache_dir=cache)
        with Image.open(self.target) as image:
            image.verify()
        self.assertEqual(retry["source"], "local_editorial")

    def test_persistent_cache_keeps_bytes_and_attribution_without_more_network(self):
        cache = self.root / "cache"
        session = Session([results(page()), download_response()])
        _, first = self.run_provider(session, cache_dir=cache)
        self.reset_provider()
        media._USED.clear()
        offline = Session()
        _, second = self.run_provider(offline, cache_dir=cache)
        self.assertEqual(first, second)
        self.assertEqual(len(offline.calls), 0)

    def test_expired_search_cache_is_not_reused_for_new_article(self):
        cache = self.root / "cache"
        self.run_provider(Session([results(page()), download_response()]), cache_dir=cache)
        for path in cache.glob("*.json"):
            record = json.loads(path.read_text())
            record["time"] = 0
            path.write_text(json.dumps(record))
        self.reset_provider()
        session = Session([results()])
        _, info = self.run_provider(session, "芯片新的文章", cache_dir=cache)
        self.assertEqual(info["source"], "local_editorial")
        self.assertEqual(len(session.calls), 1)

    def test_non_image_and_empty_pixels_use_art(self):
        for body, mime in [(b"<html>error</html>", "text/html"), (b"broken bytes", "image/png")]:
            with self.subTest(mime=mime):
                self.reset_provider()
                session = Session([results(page()), Response(body, content_type=mime)])
                _, info = self.run_provider(session)
                self.assertEqual(info["source"], "local_editorial")
        blank = io.BytesIO()
        Image.new("RGB", (960, 600), "white").save(blank, "PNG")
        self.reset_provider()
        session = Session([results(page()), Response(blank.getvalue(), content_type="image/png")])
        _, info = self.run_provider(session)
        self.assertEqual(info["source"], "local_editorial")

    def test_oversize_response_is_rejected_before_stream(self):
        response = Response(b"", content_type="image/png", headers={"Content-Length": str(media.MAX_IMAGE_BYTES + 1)})
        session = Session([results(page()), response])
        _, info = self.run_provider(session)
        self.assertEqual(info["source"], "local_editorial")
        self.assertTrue(response.closed)

    def test_streaming_limit_catches_missing_content_length(self):
        with patch.object(media, "MAX_IMAGE_BYTES", 64):
            session = Session([results(page()), download_response()])
            _, info = self.run_provider(session)
        self.assertEqual(info["source"], "local_editorial")

    def test_zero_budget_never_requests_network(self):
        session = Session()
        _, info = media.download_editorial_image(session, "energy", self.target, 0)
        self.assertEqual(info["source"], "local_editorial")
        self.assertEqual(session.calls, [])
        self.assertEqual(media._COOLDOWN_UNTIL, 0.0)

    def test_maximum_three_download_candidates(self):
        session = Session([results(*(page(i) for i in range(8)))] + [Response(b"invalid", content_type="image/png") for _ in range(8)])
        _, info = self.run_provider(session)
        self.assertEqual(info["source"], "local_editorial")
        self.assertEqual(len(session.calls), 4)
        self.assertEqual(info["search_diagnostics"], expected_diagnostics(
            search_results=8, admitted=8, original_candidates=8, original_attempts=3,
            rejections={"image_validation": 3, "download_limit": 1}, validation_failures={"image_decode": 3}))

    def test_original_artworks_are_deterministic_substantive_and_distinct(self):
        hashes = set()
        for title in ("芯片", "电力", "制造", "货运", "医疗", "零售", "金融"):
            _, first = media.bundled_fallback_image(self.target, title, 1)
            data = self.target.read_bytes()
            _, again = media.bundled_fallback_image(self.target, title, 1)
            self.assertEqual(data, self.target.read_bytes())
            self.assertEqual(first, again)
            self.assertEqual(first["license"], "original")
            self.assertEqual(first["license_url"], "")
            with Image.open(self.target) as image:
                self.assertEqual(image.size, (1200, 675))
                self.assertGreater(image.convert("L").entropy(), 4)
            hashes.add(first["sha256"])
            _, variant = media.bundled_fallback_image(self.target, title, 2)
            self.assertNotEqual(first["sha256"], variant["sha256"])
        self.assertEqual(len(hashes), 7)

    def test_thirty_same_topic_illustrations_change_actual_geometry(self):
        # Compare silhouettes after removing ALL colors and background accents.
        # Unique hashes from palette/noise changes alone cannot pass this gate.
        masks, variants, motifs, counts = [], set(), set(), set()
        for index in range(30):
            seed, plan = media._scene_plan(f"芯片研究观点 {index + 1:02d}", 1)
            variants.add(plan["variant"])
            counts.add(len(plan["objects"]))
            motifs.update(obj["motif"] for obj in plan["objects"])
            image = media._render_scene(plan, seed, geometry_only=True).resize((96, 54)).convert("L")
            masks.append([value > 40 for value in image.tobytes()])
        differences = [sum(a != b for a, b in zip(masks[i], masks[j])) / len(masks[i])
                       for i in range(30) for j in range(i)]
        self.assertEqual(variants, {"hero", "cascade", "constellation", "panorama", "duet"})
        self.assertEqual(motifs, {"chip", "servers", "network", "board"})
        self.assertEqual(counts, {2, 3, 4, 5})
        self.assertGreater(min(differences), .05)
        self.assertGreater(statistics.median(differences), .20)

    def test_geometry_metadata_is_opaque_and_same_slot_stable(self):
        title = "芯片 私密客户名称 未公开研究"
        _, first = media.bundled_fallback_image(self.target, title, 1)
        _, second = media.bundled_fallback_image(self.target, title, 2)
        _, repeat = media.bundled_fallback_image(self.target, title, 1)
        self.assertEqual(first, repeat)
        self.assertNotEqual(first["geometry_signature"], second["geometry_signature"])
        self.assertRegex(first["seed"], r"^[0-9a-f]{16}$")
        self.assertRegex(first["geometry_signature"], r"^[0-9a-f]{64}$")
        self.assertNotIn("私密客户名称", json.dumps(first, ensure_ascii=False))

    def test_local_attribution_does_not_imply_photo_or_external_license(self):
        _, info = media.bundled_fallback_image(self.target, "芯片")
        rendered = media.attribution_html(info)
        self.assertIn("原创插画", rendered)
        self.assertIn("非实拍或数据图", rendered)
        self.assertIn('data-editorial-credit="1"', rendered)
        self.assertNotIn("href=", rendered)

    def test_smoke_report_does_not_claim_local_art_as_commons_acceptance(self):
        output = self.root / "smoke"
        artwork, metadata = media.bundled_fallback_image(self.target, "finance")

        def fake_download(session, title, target, timeout):
            Path(target).write_bytes(artwork.read_bytes())
            return Path(target), metadata

        with patch.object(media, "download_editorial_image", fake_download), \
             patch("sys.argv", ["free_editorial_images.py", "--smoke-dir", str(output), "--require-commons"]), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(media._smoke_main(), 1)
        report = json.loads((output / "provider-report.json").read_text())
        self.assertFalse(report["commons_download_verified"])
        self.assertEqual(report["wechat_writes"], 0)
        self.assertEqual(report["publication_writes"], 0)
        self.assertEqual(report["network_requests"], 0)
        self.assertEqual(report["search_results"], 0)
        self.assertEqual(report["admitted"], 0)
        self.assertEqual(report["rejections"], {})
        self.assertTrue((output / "sample.jpg").is_file())

    def test_canary_workflow_network_is_manual_only_and_without_secrets(self):
        workflow = Path(__file__).resolve().parents[1] / ".github/workflows/editorial-image-provider-smoke.yml"
        text = workflow.read_text()
        self.assertIn("if: github.event_name == 'workflow_dispatch'", text)
        self.assertIn("--require-commons", text)
        self.assertIn("contents: read", text)
        self.assertIn("persist-credentials: false", text)
        self.assertNotIn("schedule:", text)
        self.assertNotIn("secrets.", text)
        contract = text.split("  public-provider-canary:", 1)[0]
        self.assertNotIn("--smoke-dir", contract)
        self.assertIn("scripts/test_free_editorial_images.py", contract)


if __name__ == "__main__":
    unittest.main()
