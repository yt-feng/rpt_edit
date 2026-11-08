"""Exercise balanced groups and interrupted replacement without losing source drafts."""
import copy
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import regroup_wechat_drafts as regroup
from push_portal_translated_to_wechat_drafts import WeChatError
from wechat_draft_grouping import account_group_sizes, draft_group_sizes


def article(number, *, note=""):
    return {"title": f"Report {number}", "content": f"<p>Current text {number}{note}</p>",
            "thumb_media_id": f"cover-{number}", "author": "Editor", "need_open_comment": 1}


class Checkpoint:
    def __init__(self):
        self.saved = None

    def save(self, state):
        self.saved = copy.deepcopy(state)


class FakeWeChat:
    def __init__(self):
        self.drafts = {}
        self.adds, self.deletes = [], []
        self.lose_add_ack = False
        self.lose_delete_ack = False
        self.bad_readback = False

    def catalog(self, _session, token, _timeout):
        return [{"media_id": media, "content": {"news_item": copy.deepcopy(rows)}}
                for (account, media), rows in self.drafts.items() if account == token]

    def get(self, _session, token, media, _timeout):
        if (token, media) not in self.drafts:
            raise WeChatError("missing", errcode=40007)
        rows = copy.deepcopy(self.drafts[token, media])
        if self.bad_readback and media.startswith("new-"):
            rows[0]["content"] += "changed"
        return {"news_item": rows}

    def add(self, _session, token, rows, _timeout):
        media = f"new-{len(self.adds)}"
        self.adds.append((token, media))
        self.drafts[token, media] = copy.deepcopy(rows)
        if self.lose_add_ack:
            self.lose_add_ack = False
            raise WeChatError("lost acknowledgement")
        return media

    def delete(self, _session, token, media, _timeout):
        self.deletes.append((token, media))
        del self.drafts[token, media]
        if self.lose_delete_ack:
            self.lose_delete_ack = False
            raise WeChatError("lost acknowledgement")
        return {"errcode": 0}


class GroupingTests(unittest.TestCase):
    def test_balanced_sizes_cover_three_groups_and_no_more_than_three_articles(self):
        self.assertEqual([3, 3, 2], draft_group_sizes(8))
        self.assertEqual([3, 3, 2, 2], draft_group_sizes(10))
        self.assertEqual([3, 3, 3], draft_group_sizes(9))
        self.assertEqual([1, 1], draft_group_sizes(2))
        for count in range(100):
            sizes = draft_group_sizes(count)
            self.assertEqual(count, sum(sizes))
            if count:
                self.assertLessEqual(max(sizes), 3)
                self.assertLessEqual(max(sizes) - min(sizes), 1)
                self.assertGreaterEqual(len(sizes), min(count, 3))

    def test_existing_accepted_group_boundaries_survive_the_new_default(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            selected = [Path(f"source/{index:02d}") for index in range(10)]
            routes = dict.fromkeys(selected, "kc")
            (output / "wechat_draft_summary.json").write_text(json.dumps({
                "dry_run": False, "drafts": [{"account": "kc", "media_id": "old-eight", "article_count": 8,
                                             "report_dirs": [str(path) for path in selected[:8]]}],
            }))
            self.assertEqual({"kc": [8, 1, 1]}, account_group_sizes(selected, routes, output, 3))
            routes[selected[-1]] = "tt"
            self.assertEqual({"kc": [8, 1], "tt": [1]}, account_group_sizes(selected, routes, output, 3))


class RegroupTests(unittest.TestCase):
    def setUp(self):
        self.api = FakeWeChat()
        for name in ("get", "add", "delete"):
            self.enterContext(patch.object(regroup, name + "_draft", getattr(self.api, name)))
        self.enterContext(patch.object(regroup, "read_complete_draft_catalog", self.api.catalog))
        self.enterContext(patch.dict(os.environ, {
            "WECHAT_MP_APPID": "kc-app", "WECHAT_MP_APPSECRET": "secret",
            "WECHAT_MP_APPID_TT": "tt-app", "WECHAT_MP_APPSECRET_TT": "secret",
            "WECHAT_MP_APPID_PANKOU": "pankou-app", "WECHAT_MP_APPSECRET_PANKOU": "secret",
        }))
        self.checkpoint = Checkpoint()

    def fixture(self, counts):
        drafts = []
        for account, count in counts.items():
            for index, start in enumerate(range(0, count, 8)):
                rows = [article(f"{account}-{number}", note=" manually edited") for number in range(start, min(count, start + 8))]
                media = f"{account}-original-{index}"
                self.api.drafts[account, media] = rows
                drafts.append({"account": account, "media_id": media,
                               "articles": [{**row, "content": "archived text"} for row in rows]})
        tokens = dict.fromkeys(counts)
        tokens.update({account: account for account in counts})
        state = {"accounts": regroup.snapshot(drafts, tokens, None, 1)}
        self.checkpoint.save(state)
        return state

    def apply(self, state):
        for account in state["accounts"]:
            regroup.apply_account(state, account, account, None, 1, self.checkpoint)

    def test_remaining_three_accounts_are_balanced_and_manual_edits_survive(self):
        state = self.fixture({"kc": 10, "tt": 9, "pankou": 9})
        original = [copy.deepcopy(row) for rows in self.api.drafts.values() for row in rows]
        self.apply(state)
        sizes = {account: sorted(len(rows) for (name, _), rows in self.api.drafts.items() if name == account)
                 for account in state["accounts"]}
        self.assertEqual({"kc": [2, 2, 3, 3], "tt": [3, 3, 3], "pankou": [3, 3, 3]}, sizes)
        self.assertCountEqual(original, [row for rows in self.api.drafts.values() for row in rows])
        operations = len(self.api.adds), len(self.api.deletes)
        self.apply(copy.deepcopy(self.checkpoint.saved))
        self.assertEqual(operations, (len(self.api.adds), len(self.api.deletes)))

    def test_absent_original_is_excluded_from_the_snapshot(self):
        rows = [article(1), article(2)]
        drafts = [{"account": "kc", "media_id": "absent", "articles": rows},
                  {"account": "kc", "media_id": "present", "articles": rows}]
        self.api.drafts["kc", "present"] = rows
        state = {"accounts": regroup.snapshot(drafts, {"kc": "kc"}, None, 1)}
        self.assertEqual(1, len(state["accounts"]["kc"]["unavailable"]))
        self.apply(state)
        self.assertEqual(2, sum(len(rows) for rows in self.api.drafts.values()))

    def test_lost_add_ack_resumes_from_exact_content_without_resubmitting(self):
        state = self.fixture({"kc": 8})
        self.api.lose_add_ack = True
        with self.assertRaises(WeChatError):
            self.apply(state)
        self.assertEqual(1, len(self.api.adds))
        self.assertEqual([], self.api.deletes)
        self.apply(copy.deepcopy(self.checkpoint.saved))
        self.assertEqual(3, len(self.api.adds))
        self.assertEqual(3, len(self.api.drafts))

    def test_unknown_add_without_any_match_never_submits_again(self):
        state = self.fixture({"kc": 8})
        self.api.lose_add_ack = True
        with self.assertRaises(WeChatError):
            self.apply(state)
        del self.api.drafts[self.api.adds[0]]
        with self.assertRaisesRegex(ValueError, "previous_draft_add_outcome_unresolved"):
            self.apply(copy.deepcopy(self.checkpoint.saved))
        self.assertEqual(1, len(self.api.adds))
        self.assertEqual([], self.api.deletes)

    def test_failed_readback_keeps_every_original(self):
        state = self.fixture({"kc": 8})
        self.api.bad_readback = True
        with self.assertRaisesRegex(ValueError, "replacement_content_changed"):
            self.apply(state)
        self.assertIn(("kc", "kc-original-0"), self.api.drafts)
        self.assertEqual([], self.api.deletes)

    def test_source_edit_before_cleanup_blocks_deletion(self):
        state = self.fixture({"kc": 8})
        self.api.drafts["kc", "kc-original-0"][0]["content"] = "Later editor change"
        with self.assertRaisesRegex(ValueError, "original_content_changed"):
            self.apply(state)
        self.assertEqual([], self.api.deletes)

    def test_lost_delete_ack_is_resolved_by_absence_without_creating_duplicates(self):
        state = self.fixture({"kc": 8})
        self.api.lose_delete_ack = True
        with self.assertRaises(WeChatError):
            self.apply(state)
        self.apply(copy.deepcopy(self.checkpoint.saved))
        self.assertEqual(3, len(self.api.adds))
        self.assertEqual(1, len(self.api.deletes))
        self.assertEqual("complete", self.checkpoint.saved["accounts"]["kc"]["status"])


if __name__ == "__main__":
    unittest.main()
