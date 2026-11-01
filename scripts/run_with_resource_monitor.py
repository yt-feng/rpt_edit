#!/usr/bin/env python3
"""Run a command with bounded, content-free resource heartbeat messages."""
from __future__ import annotations

import argparse
import math
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import time


def process_group_rss_bytes(group: int, proc_root: Path = Path("/proc")) -> int | None:
    """Sum resident pages for this command's process group on Linux.

    RSS counts shared pages in each process, as normal process RSS does. It is
    not a claim about unique physical memory. Other platforms report unknown.
    """
    if not proc_root.is_dir():
        return None
    pages = 0
    found = False
    try:
        entries = list(proc_root.iterdir())
    except OSError:
        return None
    for entry in entries:
        if not entry.name.isdecimal():
            continue
        try:
            # The parenthesized process name can itself contain spaces or ')'.
            fields = (entry / "stat").read_text().rsplit(")", 1)[1].split()
            if int(fields[2]) == group:
                pages += max(0, int(fields[21]))
                found = True
        except (OSError, ValueError, IndexError):
            # Processes may exit between directory listing and stat reading.
            continue
    return pages * os.sysconf("SC_PAGE_SIZE") if found else None


def available_memory_bytes(proc_root: Path = Path("/proc")) -> int | None:
    try:
        for line in (proc_root / "meminfo").read_text().splitlines():
            fields = line.split()
            if fields and fields[0] == "MemAvailable:" and fields[2:] == ["kB"]:
                return int(fields[1]) * 1024
    except (OSError, ValueError):
        pass
    return None


def heartbeat(label: str, group: int, started: float) -> None:
    def mib(value: int | None) -> str:
        return "unknown" if value is None else str(value // (1024 * 1024))

    try:
        disk_free = shutil.disk_usage(Path.cwd()).free
    except OSError:
        disk_free = None
    print(
        f"RESOURCE label={label} elapsed_seconds={int(time.monotonic() - started)} "
        f"group_rss_mib={mib(process_group_rss_bytes(group))} "
        f"memory_available_mib={mib(available_memory_bytes())} "
        f"disk_free_mib={mib(disk_free)}",
        flush=True,
    )


def signal_group(group: int, signum: int) -> bool:
    try:
        os.killpg(group, signum)
        return True
    except ProcessLookupError:
        return False


def run(command: list[str], *, label: str, interval: float = 60,
        termination_grace_seconds: float = 5) -> int:
    started = time.monotonic()
    try:
        child = subprocess.Popen(command, start_new_session=True)
    except OSError as error:
        # Do not echo arguments, environment values or private paths.
        print(f"::error::Resource-monitored command could not start ({type(error).__name__}).", flush=True)
        return 127 if isinstance(error, FileNotFoundError) else 126
    received_signal: int | None = None
    terminate_at: float | None = None

    def forward_signal(signum: int, _frame: object) -> None:
        nonlocal received_signal, terminate_at
        if received_signal is None:
            received_signal = signum
            terminate_at = time.monotonic() + termination_grace_seconds
            signal_group(child.pid, signum)

    previous = {signum: signal.signal(signum, forward_signal)
                for signum in (signal.SIGTERM, signal.SIGINT)}
    next_heartbeat = started
    try:
        while True:
            now = time.monotonic()
            if now >= next_heartbeat:
                heartbeat(label, child.pid, started)
                next_heartbeat = now + interval
            status = child.poll()
            if received_signal is not None:
                # A parent may exit before its inference subprocess. Keep the
                # wrapper alive until the exact launched group is gone/killed.
                if not signal_group(child.pid, 0):
                    break
                if now >= terminate_at:
                    signal_group(child.pid, signal.SIGKILL)
                    child.wait()
                    break
            elif status is not None:
                break
            time.sleep(min(0.1, max(0.001, next_heartbeat - time.monotonic())))
        heartbeat(label, child.pid, started)
        if received_signal is not None:
            return 128 + received_signal
        status = child.wait()
        return status if status >= 0 else 128 - status
    finally:
        if child.poll() is None:
            signal_group(child.pid, signal.SIGTERM)
            try:
                child.wait(timeout=termination_grace_seconds)
            except subprocess.TimeoutExpired:
                signal_group(child.pid, signal.SIGKILL)
                child.wait()
        for signum, handler in previous.items():
            signal.signal(signum, handler)


def positive_seconds(value: str) -> float:
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("must be finite and positive")
    return number


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", required=True)
    parser.add_argument("--interval", type=positive_seconds, default=60)
    parser.add_argument("--termination-grace-seconds", type=positive_seconds, default=5)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,80}", args.label):
        parser.error("label must contain 1-80 letters, digits, underscores or hyphens")
    if not args.command or args.command[0] != "--" or len(args.command) < 2:
        parser.error("command must follow --")
    return run(args.command[1:], label=args.label, interval=args.interval,
               termination_grace_seconds=args.termination_grace_seconds)


if __name__ == "__main__":
    sys.exit(main())
