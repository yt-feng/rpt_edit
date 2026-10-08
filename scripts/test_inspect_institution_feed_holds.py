import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import requests
import inspect_institution_feed_holds as probe
import fetch_institution_latest_pdfs as producer


class Response:
    status_code = 200
    def __init__(self, data): self.payload = json.dumps(data).encode()
    def __enter__(self): return self
    def __exit__(self, *args): pass
    def iter_content(self, size): yield self.payload


class Session:
    def __init__(self, response): self.response, self.calls = response, []
    def post(self, url, **kwargs):
        self.calls.append((url, kwargs))
        if isinstance(self.response, Exception): raise self.response
        return self.response
    def get(self, *args, **kwargs): raise AssertionError('No PDF, landing or provider requests')


class FeedHoldTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.archive = Path(self.temp.name)/'absent.jsonl'
        self.url = 'https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026216-source-pdf.pdf'
        self.page = 'https://www.imf.org/en/publications/wp/issues/2026/10/03/does-foreign-borrowing-lift-growth-580148'
        self.result = {'title': 'Does Foreign Borrowing Lift Growth', 'raw': {'clickableuri': self.page,
            'permanentid': 'fixed-fixture-id', 'imfdate': 1790913600000,
            'imfseries': 'Working Paper', 'seriesvolumeno': '2026/216'}}
        self.data = {'results': [self.result]}
        item = producer.collect_coveo_items(producer.INSTITUTIONS['imf'],
            probe.SingleFeedRequest(Session(Response(self.data))), 30, 60)[0]
        self.name = f"IMF_{producer.slug(item['title'])}_{producer.short_hash('imf:'+item['guid'])}.pdf"
        self.holds = {'schema': 1, 'sources': [{'source': self.name, 'sha256': 'a'*64, 'size': 17202708}],
            'versions': [{'local_filename': self.name, 'bytes': 17202708,
                          'source_page_url': self.page, 'published': item['date'], 'pdf_url': self.url}]}

    def test_actual_collector_pair_selects_hold_without_any_original_request(self):
        session = Session(Response(self.data))
        value = probe.inspect(self.holds, self.archive, probe.source_hash(self.name), session=session)
        self.assertTrue(value['expected_source_held'])
        self.assertEqual(value['held_source_count'], 1)
        self.assertEqual(value['feed_queries'], 1)
        self.assertEqual((value['pdf_gets'], value['landing_gets'], value['provider_posts'], value['production_writes']), (0,0,0,0))
        self.assertEqual(len(session.calls), 1)
        self.assertFalse(session.calls[0][1]['allow_redirects'])

    def test_changed_pdf_version_and_new_guid_are_not_suppressed(self):
        for field, value in [('seriesvolumeno', '2026/217'), ('permanentid', 'new-fixture-id')]:
            data = copy.deepcopy(self.data); data['results'][0]['raw'][field] = value
            result = probe.inspect(self.holds, self.archive, probe.source_hash(self.name), session=Session(Response(data)))
            self.assertFalse(result['expected_source_held'])

    def test_empty_feed_does_not_claim_target_acceptance(self):
        value = probe.inspect(self.holds, self.archive, probe.source_hash(self.name), session=Session(Response({'results': []})))
        self.assertFalse(value['expected_source_held'])

    def test_http_failure_and_transport_exception_never_repeat_request(self):
        failed = Response({}); failed.status_code = 503
        for response in (failed, requests.Timeout('private transport details')):
            session = Session(response)
            with patch.object(producer.time, 'sleep', side_effect=AssertionError('No retries')), self.assertRaises(probe.FeedStopped) as stopped:
                probe.inspect(self.holds, self.archive, probe.source_hash(self.name), session=session)
            self.assertEqual(len(session.calls), 1)
            self.assertEqual(stopped.exception.status, 503 if response is failed else None)

    def test_oversized_feed_and_wrong_target_stop(self):
        response = Response({}); response.payload = b'x'*(probe.MAX_FEED_BYTES+1)
        session = Session(response)
        with self.assertRaises(probe.FeedStopped):
            probe.inspect(self.holds, self.archive, probe.source_hash(self.name), session=session)
        untouched = Session(Response(self.data))
        with self.assertRaises(probe.FeedStopped):
            probe.inspect(self.holds, self.archive, 'f'*64, session=untouched)
        self.assertFalse(untouched.calls)


if __name__ == '__main__': unittest.main()
