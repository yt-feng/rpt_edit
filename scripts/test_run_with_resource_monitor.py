#!/usr/bin/env python3
"""Resource observation must preserve command results and cancellation."""
from __future__ import annotations

import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest

from run_with_resource_monitor import available_memory_bytes, process_group_rss_bytes


SCRIPT = Path(__file__).with_name("run_with_resource_monitor.py")


class ResourceMonitorTests(unittest.TestCase):
    def command(self, source: str, *options: str) -> list[str]:
        return [sys.executable, str(SCRIPT), "--label", "locale-test", *options,
                "--", sys.executable, "-c", source]

    def test_exit_code_and_unbuffered_child_streams_survive_monitor(self):
        result = subprocess.run(self.command("import sys; print('child stdout'); print('child stderr', file=sys.stderr); sys.exit(7)"),
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 7, result)
        self.assertIn("child stdout", result.stdout)
        self.assertIn("child stderr", result.stderr)
        self.assertIn("RESOURCE label=locale-test", result.stdout)
        self.assertIn("disk_free_mib=", result.stdout)

    def test_periodic_heartbeat_while_child_is_silent(self):
        result = subprocess.run(self.command("import time; time.sleep(.3)", "--interval", ".04"),
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertGreaterEqual(result.stdout.count("RESOURCE label="), 4)

    def test_signal_failure_is_not_rewritten_to_success(self):
        result = subprocess.run(self.command("import os, signal; os.kill(os.getpid(), signal.SIGTERM)"),
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 128 + signal.SIGTERM)

    def test_cancel_forwards_signal_and_preserves_cancel_even_if_child_exits_zero(self):
        with tempfile.TemporaryDirectory() as temporary:
            ready = Path(temporary) / "ready"
            stopped = Path(temporary) / "stopped"
            source = (
                "import pathlib, signal, sys, time; "
                f"signal.signal(signal.SIGTERM, lambda *_: (pathlib.Path({str(stopped)!r}).touch(), sys.exit(0))); "
                f"pathlib.Path({str(ready)!r}).touch(); time.sleep(30)"
            )
            process = subprocess.Popen(self.command(source, "--termination-grace-seconds", ".2"),
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            try:
                deadline = time.monotonic() + 5
                while not ready.exists() and time.monotonic() < deadline:
                    time.sleep(.01)
                self.assertTrue(ready.exists())
                process.send_signal(signal.SIGTERM)
                output, error = process.communicate(timeout=3)
                self.assertEqual(process.returncode, 128 + signal.SIGTERM, output + error)
                self.assertTrue(stopped.exists())
            finally:
                if process.poll() is None:
                    process.kill()
                    process.wait()

    def test_cancel_escalates_only_launched_group_when_child_ignores_term(self):
        with tempfile.TemporaryDirectory() as temporary:
            ready = Path(temporary) / "ready"
            source = ("import pathlib, signal, time; signal.signal(signal.SIGTERM, signal.SIG_IGN); "
                      f"pathlib.Path({str(ready)!r}).touch(); time.sleep(30)")
            process = subprocess.Popen(self.command(source, "--termination-grace-seconds", ".1"),
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            try:
                deadline = time.monotonic() + 5
                while not ready.exists() and time.monotonic() < deadline:
                    time.sleep(.01)
                self.assertTrue(ready.exists())
                process.send_signal(signal.SIGTERM)
                process.communicate(timeout=3)
                self.assertEqual(process.returncode, 128 + signal.SIGTERM)
            finally:
                if process.poll() is None:
                    process.kill()
                    process.wait()

    def test_cancel_reaches_inference_grandchild_in_same_group(self):
        with tempfile.TemporaryDirectory() as temporary:
            ready = Path(temporary) / "ready"
            stopped = Path(temporary) / "stopped"
            grandchild = (
                "import pathlib, signal, sys, time; "
                f"signal.signal(signal.SIGTERM, lambda *_: (pathlib.Path({str(stopped)!r}).touch(), sys.exit(0))); "
                f"pathlib.Path({str(ready)!r}).touch(); time.sleep(30)"
            )
            source = ("import subprocess, sys; "
                      f"subprocess.run([sys.executable, '-c', {grandchild!r}])")
            process = subprocess.Popen(self.command(source, "--termination-grace-seconds", ".1"),
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            try:
                deadline = time.monotonic() + 5
                while not ready.exists() and time.monotonic() < deadline:
                    time.sleep(.01)
                self.assertTrue(ready.exists())
                process.send_signal(signal.SIGTERM)
                process.communicate(timeout=3)
                self.assertEqual(process.returncode, 128 + signal.SIGTERM)
                self.assertTrue(stopped.exists())
            finally:
                if process.poll() is None:
                    process.kill()
                    process.wait()

    def test_proc_rss_filters_group_and_handles_exiting_or_unusual_names(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for pid, group, rss in ((11, 22, 4), (12, 22, 7), (13, 33, 100)):
                fields = ["S", "1", str(group)] + ["0"] * 19
                fields[21] = str(rss)
                directory = root / str(pid)
                directory.mkdir()
                (directory / "stat").write_text(f"{pid} (odd ) process name) " + " ".join(fields))
            (root / "14").mkdir()
            self.assertEqual(process_group_rss_bytes(22, root), 11 * os.sysconf("SC_PAGE_SIZE"))
            self.assertIsNone(process_group_rss_bytes(44, root))
            (root / "meminfo").write_text("MemTotal: 100 kB\nMemAvailable: 51 kB\n")
            self.assertEqual(available_memory_bytes(root), 51 * 1024)
            (root / "meminfo").write_text("MemAvailable: malformed kB\n")
            self.assertIsNone(available_memory_bytes(root))

    def test_no_proc_reports_unknown_without_failing_command(self):
        with tempfile.TemporaryDirectory() as temporary:
            missing = Path(temporary) / "absent"
            self.assertIsNone(process_group_rss_bytes(1, missing))
            self.assertIsNone(available_memory_bytes(missing))

    def test_invalid_interval_and_missing_delimiter_are_rejected(self):
        for interval in ("0", "-1", "nan", "inf"):
            with self.subTest(interval=interval):
                result = subprocess.run(self.command("pass", "--interval", interval), capture_output=True)
                self.assertEqual(result.returncode, 2)
        result = subprocess.run([sys.executable, str(SCRIPT), "--label", "test", sys.executable], capture_output=True)
        self.assertEqual(result.returncode, 2)

    def test_missing_executable_is_failure_without_echoing_arguments(self):
        result = subprocess.run([sys.executable, str(SCRIPT), "--label", "test", "--",
                                 "/missing-monitor-command", "private-argument"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 127)
        self.assertNotIn("private-argument", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
