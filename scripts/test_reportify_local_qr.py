#!/usr/bin/env python3
"""Decode real generated QR modules at both delivered and displayed dimensions."""
import base64
import json
from pathlib import Path
import re
import subprocess
import unittest
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw
import zxingcpp

ROOT = Path(__file__).resolve().parents[1]


class LocalLoginQrTests(unittest.TestCase):
    def test_exact_payload_roundtrip_and_quiet_zone(self):
        node = r'''
import { reportifyQrDataUrl } from './workers/portal-suite-worker/src/reportify-login-qr.js';
const prefix = 'http://weixin.qq.com/q/';
const payloads = [prefix + 'fixture-test', prefix + 'fixture-中文-عربي-😀',
  prefix + 'fixture%2Ftest%25', prefix + 'x'.repeat(256-prefix.length)];
console.log(JSON.stringify(payloads.map(payload => ({payload, image:reportifyQrDataUrl(payload)}))));
'''
        result = subprocess.run(["node", "--input-type=module", "-"], input=node, text=True,
                                cwd=ROOT, check=True, capture_output=True)
        for row in json.loads(result.stdout):
            svg = ET.fromstring(base64.b64decode(row["image"].split(",", 1)[1], validate=True))
            self.assertEqual(svg.attrib["width"], "320")
            self.assertEqual(svg.attrib["height"], "320")
            dimension = int(svg.attrib["viewBox"].split()[2])
            self.assertEqual(svg.attrib["viewBox"], f"0 0 {dimension} {dimension}")
            path = svg.find("{http://www.w3.org/2000/svg}path").attrib["d"]
            pieces = re.findall(r"M(\d+),(\d+)h1v1h-1z", path)
            self.assertEqual(path, "".join(f"M{x},{y}h1v1h-1z" for x, y in pieces))
            modules = Image.new("RGB", (dimension, dimension), "white")
            draw = ImageDraw.Draw(modules)
            for x, y in pieces:
                self.assertTrue(4 <= int(x) < dimension - 4 and 4 <= int(y) < dimension - 4)
                draw.point((int(x), int(y)), fill="black")
            for size in (220, 320):
                with self.subTest(bytes=len(row["payload"].encode()), size=size):
                    rendered = modules.resize((size, size), Image.Resampling.NEAREST)
                    decoded = zxingcpp.read_barcode(rendered)
                    self.assertIsNotNone(decoded)
                    self.assertEqual(decoded.bytes, row["payload"].encode("utf-8"))


if __name__ == "__main__":
    unittest.main()
