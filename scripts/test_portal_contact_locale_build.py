#!/usr/bin/env python3
"""Keep reviewed public contact copy stable through the locale JS builder."""

from pathlib import Path
import subprocess
import unittest

import build_portal_locales as builder


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "portal_suite/site_src/assets/contact.js").read_text(encoding="utf-8")
COPY = (
    "开通账号联系", "계정 개설 문의", "アカウント開設のお問い合わせ", "لفتح حساب، تواصل مع",
)
EXISTING_REQUEST_COPY = {
    "ko": {"申请加入会员": "회원 가입 신청", "站内申请": "사이트 내 신청"},
    "ja": {"申请加入会员": "会員登録を申請", "站内申请": "サイト内申請"},
    "ar": {"申请加入会员": "طلب العضوية", "站内申请": "طلب عبر الموقع"},
}


class PublicContactBuildTests(unittest.TestCase):
    def test_reviewed_contact_adds_no_paid_translation_units(self):
        units = {}
        builder.collect_javascript_units(SOURCE, "contact.js", units)
        self.assertEqual({unit.source for unit in units.values()}, {"申请加入会员", "站内申请"})
        self.assertTrue(all(unit.context == "javascript:contact.js" for unit in units.values()))

    def test_locale_render_keeps_fixed_copy_address_and_program_tokens(self):
        units = {}
        builder.collect_javascript_units(SOURCE, "contact.js", units)
        cache = builder.empty_cache()
        for locale, translations in EXISTING_REQUEST_COPY.items():
            for unit in units.values():
                cache["locales"][locale][unit.key] = {
                    "source": unit.source,
                    "translation": translations[unit.source],
                }
        for locale in EXISTING_REQUEST_COPY:
            with self.subTest(locale=locale):
                rendered = builder.render_localized_javascript(SOURCE, "contact.js", locale, cache)
                builder.validate_localized_javascript_residuals(SOURCE, rendered, "contact.js", locale, cache)
                for literal in (*COPY, "info@kcdesk.com", "data-kc-public-account-contact", ".legal-footer"):
                    self.assertIn(literal, rendered)
                self.assertIn('link.href = "mailto:info@kcdesk.com"', rendered)
                self.assertIn('return `/?request=${encodeURIComponent(requestKind(value))}`', rendered)
                self.assertIn('const PUBLIC_ACCOUNT_COPY = Object.freeze(JSON.parse(JSON.stringify({', rendered)
                result = subprocess.run(["node", "--check"], input=rendered, text=True, capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
