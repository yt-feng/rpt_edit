"""Public website/contact approval never approves unrelated private identity."""
import unittest
import check_public_identity as guard


class PublicContactAllowlistTests(unittest.TestCase):
    def test_exact_public_mailbox_is_allowed_in_plain_text_and_mailto(self):
        for text in ('开通账号联系 info@kcdesk.com', 'href="mailto:info@kcdesk.com"', '"info@kcdesk.com"'):
            sanitized = guard.redact_approved_public_contact(guard.confusable_skeleton(text))
            self.assertFalse(any(marker in sanitized for marker in guard.private_markers()))

    def test_public_domain_is_allowed_without_approving_other_mailboxes(self):
        for text in ('kcdesk.com', 'https://kcdesk.com/ja/', 'https://www.kcdesk.com/',
                     '中文站点：kcdesk.com', 'href="https://kcdesk.com/report.html?id=example"'):
            sanitized = guard.redact_approved_public_contact(guard.confusable_skeleton(text))
            self.assertFalse(any(marker in sanitized for marker in guard.private_markers()), text)

    def test_other_mailboxes_and_lookalikes_remain_blocked(self):
        domain = guard.private_markers()[1]
        for text in ('admin@' + domain, 'xinfo@' + domain, 'admin@www.' + domain,
                     'info@' + domain + '.example', 'info@' + domain + '-other',
                     domain + '@example.invalid', domain + '.example', 'other' + domain):
            sanitized = guard.redact_approved_public_contact(text)
            self.assertTrue(any(marker in sanitized for marker in guard.private_markers()), text)

    def test_private_email_is_not_changed_or_approved_by_public_allowlist(self):
        for value in ('private.fixture@gmail.com', 'private.fixture@outlook.com'):
            self.assertEqual(guard.redact_approved_public_contact(value), value)
        for marker in guard.private_markers()[5:]:
            self.assertEqual(guard.redact_approved_public_contact(marker), marker)


if __name__ == '__main__':
    unittest.main()
