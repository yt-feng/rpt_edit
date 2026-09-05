import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import audit_portal_chinese_discovery_plan as audit_module
import build_portal_locales as builder
import build_portal_suite_site as site_builder
import verify_portal_chinese_parity as parity


ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://portal.example.invalid"


def page(language="zh-Hans", *, robots="index,follow", extra="", default=None):
    canonical = ORIGIN + "/sample.html"
    return (
        f'<html lang="{language}"><head><meta name="robots" content="{robots}">'
        f'<link rel="canonical" href="{canonical}">'
        f'<link rel="alternate" hreflang="{language}" href="{canonical}">'
        f'<link rel="alternate" hreflang="x-default" href="{default or canonical}">'
        f'{extra}<title>Protected source</title></head><body>Protected body</body></html>'
    )


class ChineseDiscoveryPlanTests(unittest.TestCase):
    def test_only_complete_existing_chinese_clusters_receive_links(self):
        canonical = ORIGIN + "/sample.html"
        for source, eligible in (
            (page(), True),
            (page("en"), False),
            (page("zh-CN"), False),
            (page(robots="noindex,follow"), False),
            (page(default=ORIGIN + "/different.html"), False),
            (page(extra=f'<link rel="alternate" hreflang="zh-Hans" href="{canonical}">'), False),
            (page(extra=f'<link rel="canonical" href="{canonical}">'), False),
        ):
            with self.subTest(eligible=eligible, source=source):
                self.assertEqual(builder.root_discovery_eligible(source, canonical, ORIGIN), eligible)
                rendered = builder.inject_root_discovery(source, canonical, ORIGIN, "0123456789ab")
                self.assertEqual('hreflang="ko"' in rendered, eligible)
                self.assertEqual(parity._body(source.encode(), relative="sample.html"), parity._body(rendered.encode(), relative="sample.html"))
                self.assertEqual(parity._neutral_head(source.encode(), relative="sample.html"), parity._neutral_head(rendered.encode(), relative="sample.html"))

    def test_foreign_fragment_and_locale_canonicals_are_not_eligible(self):
        original = ORIGIN + "/sample.html"
        for canonical in ("http://portal.example.invalid/sample.html", "https://other.example/sample.html", original + "#section", ORIGIN + "/ko/sample.html"):
            with self.subTest(canonical=canonical):
                self.assertFalse(builder.root_discovery_eligible(page().replace(original, canonical), canonical, ORIGIN))

    def test_all_real_source_templates_pass_without_source_mutation_or_provider_calls(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for path in (ROOT / "portal_suite/site_src").glob("*.html"):
                (root / path.name).write_bytes(path.read_bytes())
            site_builder.enhance_public_landing_pages(root, ORIGIN)
            before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in root.glob("*.html")}
            with mock.patch.object(builder, "translate_missing_units", side_effect=AssertionError("No paid calls")):
                report = audit_module.audit(root, ORIGIN)
            self.assertEqual(report, {"status": "passed", "html_checked": 11, "eligible_clusters": 2, "provider_requests": 0})
            self.assertEqual(before, {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in root.glob("*.html")})
            for name in ("privacy.html", "terms.html"):
                source = (root / name).read_text()
                rendered = builder.inject_root_discovery(source, builder.extract_canonical(source), ORIGIN, "0123456789ab")
                links = parity._alternate_map(parity._head_links(rendered.encode(), relative=name), relative=name)
                self.assertEqual(set(links), {"en", "x-default"})

    def test_plan_audit_rejects_body_mutation_before_any_translation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "sample.html").write_text(page())
            inject = builder.inject_root_discovery
            with mock.patch.object(builder, "inject_root_discovery", side_effect=lambda *args: inject(*args).replace("Protected body", "Changed body")):
                with self.assertRaisesRegex(parity.ParityError, "protected body"):
                    audit_module.audit(root, ORIGIN)

    def test_workflow_runs_the_dry_plan_before_paid_locale_build(self):
        workflow = (ROOT / ".github/workflows/neutral-edge-cutover.yml").read_text()
        self.assertLess(workflow.index("Validate planned Chinese discovery before paid translation"), workflow.index("Build Korean Japanese and Arabic static locales"))


if __name__ == "__main__":
    unittest.main()
