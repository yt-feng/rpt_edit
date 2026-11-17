#!/usr/bin/env python3
"""Read-only clock inspection must expose only bounded, typed evidence."""
import contextlib
import io
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import yaml
import inspect_daily_source_clock as clock


class Missing(Exception):
    def __init__(self, code):
        self.response = {'Error': {'Code': code, 'Message': 'private bucket and token'}}


class ReadOnlyApi:
    def __init__(self, schedules=None, error=None):
        self.schedules, self.error, self.calls = schedules, error, 0
    def get(self):
        self.calls += 1
        if self.error:
            raise self.error
        return self.schedules


class ReadOnlyR2:
    def __init__(self, value=None, error=None):
        self.error, self.calls = error, []
        self.body = io.BytesIO(json.dumps(value).encode() if not isinstance(value, bytes) else value)
    def get_object(self, **kwargs):
        self.calls.append(kwargs)
        if self.error:
            raise self.error
        return {'Body': self.body}


class ClockInspectionTests(unittest.TestCase):
    def receipt(self, **changes):
        return {'state': 'observed', 'requested_at': '2026-11-17T02:30:00.125Z',
                'previous_dispatch_run_id': 123, 'run_id': 456, **changes}

    def inspect(self, client, api=None):
        api = api or ReadOnlyApi([clock.HALF_HOURLY])
        result = clock.inspect_clock(lambda: api, lambda: client, lambda: 'private-test-bucket')
        self.assertEqual(api.calls, 1)
        self.assertEqual(client.calls, [{'Bucket': 'private-test-bucket', 'Key': clock.RECEIPT_KEY}])
        return result

    def test_observed_receipt_has_only_typed_fields_and_reads_no_other_object(self):
        client = ReadOnlyR2(self.receipt(token='private-token', bucket='private-test-bucket',
                                       message='private response body'))
        result = self.inspect(client)
        self.assertEqual(result, {'inspection_state': 'read_only', 'schedule_state': 'half_hourly_verified',
            'receipt_state': 'observed', 'requested_at': '2026-11-17T02:30:00.125Z',
            'previous_dispatch_run_id': 123, 'run_id': 456})
        self.assertTrue(client.body.closed)
        self.assertNotIn('private', json.dumps(result))

    def test_first_tick_without_receipt_is_explicitly_not_observed(self):
        result = self.inspect(ReadOnlyR2(error=Missing('NoSuchKey')))
        self.assertEqual(result['receipt_state'], 'not_observed')
        self.assertNotIn('run_id', result)

    def test_permission_bucket_and_transport_errors_are_not_absence_or_raw_messages(self):
        for error in (Missing('AccessDenied'), Missing('NoSuchBucket'), RuntimeError('private-token')):
            result = self.inspect(ReadOnlyR2(error=error), ReadOnlyApi(error=RuntimeError('private-api-body')))
            self.assertEqual(result, {'inspection_state': 'read_only', 'schedule_state': 'unavailable',
                                      'receipt_state': 'unavailable'})

    def test_unconfirmed_post_states_do_not_claim_a_workflow_run_was_observed(self):
        for state in ('dispatching', 'accepted', 'unknown', 'rejected'):
            result = self.inspect(ReadOnlyR2(self.receipt(state=state, run_id=None)))
            self.assertEqual(result['receipt_state'], state)
            self.assertNotIn('run_id', result)

    def test_invalid_fields_or_oversized_objects_are_never_echoed(self):
        cases = [self.receipt(state='private-token'), self.receipt(state=['private-token']),
                 self.receipt(requested_at='private-time'), self.receipt(requested_at='2026-13-17T02:30:00Z'),
                 self.receipt(run_id=True), self.receipt(run_id=-1), self.receipt(run_id=None),
                 self.receipt(previous_dispatch_run_id='private-id'), self.receipt(run_id=2**53),
                 b'private-body', b'x' * (clock.MAX_RECEIPT_BYTES + 1)]
        for value in cases:
            with self.subTest(value=type(value).__name__):
                client = ReadOnlyR2(value)
                self.assertEqual(self.inspect(client)['receipt_state'], 'invalid')
                self.assertTrue(client.body.closed)

    def test_unexpected_schedule_is_reported_without_echoing_cron_data(self):
        result = self.inspect(ReadOnlyR2(error=Missing('NoSuchKey')), ReadOnlyApi(['private cron body']))
        self.assertEqual(result['schedule_state'], 'mismatch')
        self.assertNotIn('private', json.dumps(result))

    def test_entrypoint_is_read_only_and_successful_absence_does_not_fail(self):
        for receipt_state, expected_code in (('not_observed', 0), ('invalid', 1), ('unavailable', 1)):
            output = io.StringIO()
            result = {'inspection_state': 'read_only', 'schedule_state': 'half_hourly_verified',
                      'receipt_state': receipt_state}
            with patch.object(clock, 'inspect_clock', return_value=result), contextlib.redirect_stdout(output):
                self.assertEqual(clock.main(), expected_code)
            self.assertEqual(json.loads(output.getvalue()), result)

    def test_workflow_inspection_cannot_reach_deployment_or_github_dispatch(self):
        path = Path(__file__).resolve().parents[1] / '.github/workflows/daily-source-clock-deploy.yml'
        workflow = yaml.safe_load(path.read_text())
        events = workflow.get('on', workflow.get(True))
        option = events['workflow_dispatch']['inputs']['inspect_only']
        self.assertEqual(option['type'], 'boolean'); self.assertFalse(option['default'])
        self.assertIn('!inputs.inspect_only', workflow['jobs']['deploy']['if'])
        job = workflow['jobs']['inspect']
        self.assertNotIn('needs', job)
        self.assertIn("github.ref == 'refs/heads/main' && inputs.inspect_only", job['if'])
        self.assertEqual(workflow['permissions'], {'contents': 'read'})
        runs = [step['run'] for step in job['steps'] if 'run' in step]
        self.assertEqual(runs, ['python -m pip install boto3', 'python scripts/inspect_daily_source_clock.py'])
        self.assertTrue(all('wrangler' not in step.get('uses', '') for step in job['steps']))
        read_step = job['steps'][-1]
        self.assertNotIn('GH_DISPATCH_TOKEN', read_step['env'])
        self.assertNotIn('GH_TOKEN', read_step['env'])
        self.assertIn('R2_ACCESS_KEY_ID', read_step['env'])


if __name__ == '__main__':
    unittest.main()
