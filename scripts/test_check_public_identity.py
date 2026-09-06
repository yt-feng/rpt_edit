"""The one approved public mailbox does not expose other deployment identity."""
import unittest
import check_public_identity as guard


class PublicContactAllowlistTests(unittest.TestCase):
    def test_exact_public_mailbox_is_allowed_in_plain_text_and_mailto(self):
        for text in ('开通账号联系 info@kcdesk.com', 'href="mailto:info@kcdesk.com"', '"info@kcdesk.com"'):
            sanitized = guard.redact_approved_public_contact(guard.confusable_skeleton(text))
            self.assertFalse(any(marker in sanitized for marker in guard.private_markers()))

    def test_domain_other_mailboxes_and_lookalikes_remain_blocked(self):
        domain = guard.private_markers()[1]
        for text in (domain, 'https://' + domain, 'admin@' + domain, 'xinfo@' + domain,
                     'info@' + domain + '.example', 'info@' + domain + '-other'):
            sanitized = guard.redact_approved_public_contact(text)
            self.assertTrue(any(marker in sanitized for marker in guard.private_markers()), text)


if __name__ == '__main__':
    unittest.main()
