"""Real stdio protocol checks; all content requests are absent or faked."""
import asyncio
import importlib.util
import json
import os
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
AVAILABLE = importlib.util.find_spec("mcp") is not None


@unittest.skipUnless(AVAILABLE, "Install requirements-mcp.txt to run SDK transport checks")
class McpTests(unittest.IsolatedAsyncioTestCase):
    async def exchange(self, process, payload):
        process.stdin.write((json.dumps(payload) + "\n").encode())
        await process.stdin.drain()
        if "id" not in payload:
            return None
        while True:
            line = await asyncio.wait_for(process.stdout.readline(), timeout=10)
            self.assertTrue(line, "MCP server terminated without a response")
            result = json.loads(line)
            if result.get("id") == payload["id"]:
                return result

    async def test_initialize_versions_tools_and_explicit_errors_without_key(self):
        for version in ["2025-06-18", "2025-11-25"]:
            with self.subTest(version=version):
                env = {**os.environ, "KCD_API_KEY": "", "CONTENT_API_BASE_URL": "https://api.example.invalid"}
                process = await asyncio.create_subprocess_exec(sys.executable, str(ROOT / "scripts/content_mcp.py"),
                    stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, env=env)
                try:
                    initialized = await self.exchange(process, {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
                        "protocolVersion": version, "capabilities": {}, "clientInfo": {"name": "offline-test", "version": "1"}}})
                    self.assertEqual(initialized["result"]["protocolVersion"], version)
                    self.assertEqual(initialized["result"]["serverInfo"]["name"], "content-api")
                    await self.exchange(process, {"jsonrpc": "2.0", "method": "notifications/initialized"})
                    listed = await self.exchange(process, {"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
                    self.assertEqual(len(listed["result"]["tools"]), 6)
                    download = next(tool for tool in listed["result"]["tools"] if tool["name"] == "content_download")
                    self.assertFalse(download["annotations"]["readOnlyHint"])
                    for request_id, name, args, code in [
                        (3, "content_get_report", {"report_id": "a" * 24}, "missing_api_key"),
                        (4, "content_get_report", {"report_id": "../private"}, "invalid_arguments"),
                        (5, "content_arbitrary_url", {}, "unknown_tool"),
                    ]:
                        called = await self.exchange(process, {"jsonrpc": "2.0", "id": request_id, "method": "tools/call", "params": {"name": name, "arguments": args}})
                        self.assertTrue(called["result"]["isError"])
                        self.assertEqual(json.loads(called["result"]["content"][0]["text"])["error"], code)
                finally:
                    process.stdin.close()
                    await asyncio.wait_for(process.wait(), timeout=10)
                self.assertEqual(process.returncode, 0, (await process.stderr.read()).decode())

    async def test_sdk_client_reads_fake_upstream_through_stdio(self):
        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client
        program = '''
import sys, asyncio
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, sys.argv[2])
from content_mcp import create_server
from content_client import Client
from test_client import Response, FakeOpener, KEY
from mcp.server.stdio import stdio_server
opener = FakeOpener(Response(b'{"items":[{"id":"aaaaaaaaaaaaaaaaaaaaaaaa","title":"Research"}],"next_cursor":null}'), Response(b"source text", "text/plain"))
async def run():
    server = create_server(lambda: Client(api_key=KEY, opener=opener))
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())
asyncio.run(run())
'''
        params = StdioServerParameters(command=sys.executable, args=["-c", program, str(ROOT / "scripts"), str(ROOT / "tests")])
        async with stdio_client(params) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                result = await session.call_tool("content_search_reports", {"q": "AI"})
                self.assertFalse(result.isError)
                self.assertEqual(result.structuredContent["items"][0]["title"], "Research")
                self.assertEqual(result.structuredContent["api_requests"], {"attempted": 1, "http_200": 1})
                result = await session.call_tool("content_read_artifact", {"report_id": "a" * 24, "artifact_id": "extracted-text", "max_chars": 6})
                self.assertFalse(result.isError)
                self.assertEqual(result.structuredContent["text"], "source")
                self.assertTrue(result.structuredContent["truncated"])


if __name__ == "__main__":
    unittest.main()
