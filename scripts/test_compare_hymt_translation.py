#!/usr/bin/env python3
"""Model-free coverage for the separate Actions-only Hy-MT2 comparison."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import compare_hymt_translation as comparison


BASE = Path(__file__).parent


class ComparisonTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((BASE / 'hymt_translation_model_manifest.json').read_text())

    def test_no_inference_on_local_machine(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(RuntimeError, 'restricted'):
                comparison.require_actions()

    def test_sources_and_artifact_are_pinned(self):
        self.assertEqual(self.manifest['runtime']['repository'], 'ggml-org/llama.cpp')
        self.assertEqual(self.manifest['model']['repository'], 'tencent/Hy-MT2-1.8B-GGUF')
        for source in ('runtime', 'model'):
            self.assertRegex(self.manifest[source]['revision'], r'^[0-9a-f]{40}$')
        self.assertRegex(self.manifest['model']['sha256'], r'^[0-9a-f]{64}$')
        self.assertEqual(self.manifest['model']['quantization'], 'Q8_0')

    def test_model_checksum_rejects_changed_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            model = Path(directory) / 'test.gguf'
            model.write_bytes(b'public-test-fixture')
            manifest = {'model': {'sha256': hashlib.sha256(model.read_bytes()).hexdigest()}}
            self.assertEqual(comparison.verify_model(model, manifest), manifest['model']['sha256'])
            model.write_bytes(b'changed')
            with self.assertRaisesRegex(ValueError, 'SHA256'):
                comparison.verify_model(model, manifest)

    def test_complete_propositions_and_values_are_in_prompt(self):
        sample = {'target_language': 'ko', 'text': '今年公司收入增长12.5%，营业利润率为8%。'}
        payload = comparison.translation_request(sample, self.manifest)
        self.assertEqual(len(payload['messages']), 1)
        self.assertEqual(payload['messages'][0]['role'], 'user')
        self.assertTrue(payload['messages'][0]['content'].endswith(sample['text']))
        self.assertIn('Korean', payload['messages'][0]['content'])
        self.assertEqual(payload['seed'], 20260920)
        self.assertFalse(payload['cache_prompt'])

    def test_shared_samples_cover_required_directions_and_paragraphs(self):
        samples = comparison.load_samples(BASE / 'translation_quality_samples.json')
        directions = [(row['source_language'], row['target_language']) for row in samples]
        self.assertGreaterEqual(directions.count(('en', 'zh')), 3)
        self.assertGreaterEqual(directions.count(('zh', 'en')), 3)
        for target in ('ko', 'ja', 'ar'):
            self.assertGreaterEqual(directions.count(('zh', target)), 1)
        self.assertGreaterEqual(sum('paragraph' in row['id'] for row in samples), 2)

    def test_truncated_response_is_not_a_pass(self):
        response = {'choices': [{'message': {'content': '营业利润率'}, 'finish_reason': 'length'}]}
        issues = comparison.structural_issues({'target_language': 'zh'}, response)
        self.assertIn('incomplete_finish_reason:length', issues)

    def test_checkpoint_and_pending_semantics_survive_transport_failure(self):
        samples = comparison.load_samples(BASE / 'translation_quality_samples.json')[:2]
        process = mock.Mock()
        process.poll.return_value = None
        process.returncode = -15
        response = {'choices': [{'message': {'content': '2026年上半年收入同比下降8.2%。'}, 'finish_reason': 'stop'}]}
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'output'
            args = argparse.Namespace(
                manifest=BASE / 'hymt_translation_model_manifest.json', samples=BASE / 'translation_quality_samples.json',
                model=Path(directory) / 'model.gguf', runtime_source=Path(directory),
                server_bin=Path(directory) / 'llama-server', output_dir=output,
                threads=4, port=18088, startup_timeout=180, sample_timeout=180, max_seconds=1800,
            )
            with mock.patch.dict(os.environ, {'GITHUB_ACTIONS': 'true', 'RUNNER_OS': 'Linux'}), \
                 mock.patch.object(comparison.platform, 'platform', return_value='Linux-fixture'), \
                 mock.patch.object(comparison, 'load_samples', return_value=samples), \
                 mock.patch.object(comparison, 'verify_model', return_value=self.manifest['model']['sha256']), \
                 mock.patch.object(comparison.subprocess, 'check_output', side_effect=[self.manifest['runtime']['revision'], 'llama.cpp v0.4.1']), \
                 mock.patch.object(comparison.subprocess, 'Popen', return_value=process), \
                 mock.patch.object(comparison, 'request_json', side_effect=[{'status': 'ok'}, response, TimeoutError('fixture timeout')]):
                result = comparison.run_comparison(args)
            self.assertEqual(result, 1)
            saved = json.loads((output / 'diagnostics.json').read_text())
            self.assertEqual(saved['samples'][0]['translation'], response['choices'][0]['message']['content'])
            self.assertEqual(saved['samples'][0]['status'], 'generated-review-required')
            self.assertEqual(saved['samples'][1]['status'], 'failed')
            self.assertEqual(saved['semantic_review'], 'pending-human-review')
            self.assertIn('pending human review', (output / 'review.md').read_text())
            process.terminate.assert_called_once()


if __name__ == '__main__':
    unittest.main()
