#!/usr/bin/env python3
from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from pdf_to_xhs_batch import mineru_tokens_from_env


class MinerUKeyRotationTests(unittest.TestCase):
    @patch.dict(
        os.environ,
        {
            "MINER_U": "key-1",
            "MINER_U_2": "key-2",
            "MINER_U_3": "key-3",
            "MINER_U_4": "key-4",
            "MINER_U_TOKEN_OFFSET": "2",
        },
        clear=True,
    )
    def test_rotates_numbered_keys_by_shard_offset(self) -> None:
        self.assertEqual(
            mineru_tokens_from_env(),
            [
                ("MINER_U_3", "key-3"),
                ("MINER_U_4", "key-4"),
                ("MINER_U", "key-1"),
                ("MINER_U_2", "key-2"),
            ],
        )

    @patch.dict(
        os.environ,
        {
            "MINER_U_KEYS": "key-1,key-2",
            "MINER_U": "key-1",
            "MINER_U_2": "key-2",
            "MINER_U_3": "key-3",
        },
        clear=True,
    )
    def test_deduplicates_combined_and_numbered_keys(self) -> None:
        self.assertEqual(
            [token for _label, token in mineru_tokens_from_env()],
            ["key-1", "key-2", "key-3"],
        )


if __name__ == "__main__":
    unittest.main()
