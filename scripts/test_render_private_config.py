#!/usr/bin/env python3

from __future__ import annotations

import base64
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("render_private_config.py").resolve()
CONFIG_ENV = "PORTAL_PRIVATE_CONFIG_B64"


def encoded_profile(*, replacements: list[dict[str, str]], files: list[dict] | None = None) -> str:
    payload = {
        "version": 1,
        "replacements": replacements,
        "files": files or [],
    }
    return base64.b64encode(
        json.dumps(payload, ensure_ascii=False).encode("utf-8")
    ).decode("ascii")


def encoded_content(content: bytes) -> str:
    return base64.b64encode(content).decode("ascii")


class RenderPrivateConfigTests(unittest.TestCase):
    def run_renderer(
        self,
        workspace: Path,
        profile: str,
        *arguments: str,
    ) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        environment[CONFIG_ENV] = profile
        return subprocess.run(
            [sys.executable, str(SCRIPT), *arguments],
            cwd=workspace,
            env=environment,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def test_forward_multiple_roots_skips_binary_and_git_and_creates_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            first = workspace / "first"
            second = workspace / "second"
            first.mkdir()
            second.mkdir()
            (first / "page.txt").write_text(
                "updates@alias.invalid https://alias.invalid\n", encoding="utf-8"
            )
            binary = first / "asset.bin"
            binary.write_bytes(b"\x00alias.invalid\xff")
            metadata = first / ".git"
            metadata.mkdir()
            (metadata / "config").write_text("alias.invalid", encoding="utf-8")
            (second / "worker.js").write_text("alias.invalid", encoding="utf-8")
            git_pointer = second / ".git"
            git_pointer.write_text("gitdir: alias.invalid", encoding="utf-8")
            generated_content = b"verification-private-content\n"
            profile = encoded_profile(
                replacements=[
                    {
                        "public": "updates@alias.invalid",
                        "private": "mail@live.invalid",
                    },
                    {"public": "alias.invalid", "private": "live.invalid"},
                ],
                files=[
                    {
                        "root": 1,
                        "path": "verification/proof.txt",
                        "content_b64": encoded_content(generated_content),
                    }
                ],
            )

            result = self.run_renderer(
                workspace,
                profile,
                "--root",
                "first",
                "--root",
                "second",
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(
                (first / "page.txt").read_text(encoding="utf-8"),
                "mail@live.invalid https://live.invalid\n",
            )
            self.assertEqual((second / "worker.js").read_text(), "live.invalid")
            self.assertEqual(binary.read_bytes(), b"\x00alias.invalid\xff")
            self.assertEqual((metadata / "config").read_text(), "alias.invalid")
            self.assertEqual(git_pointer.read_text(), "gitdir: alias.invalid")
            self.assertEqual(
                (second / "verification" / "proof.txt").read_bytes(), generated_content
            )
            self.assertNotIn("mail@live.invalid", result.stdout + result.stderr)
            self.assertNotIn("verification-private-content", result.stdout + result.stderr)

    def test_reverse_restores_text_and_removes_matching_generated_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            output = workspace / "output"
            output.mkdir()
            source = output / "index.html"
            source.write_text("alias.invalid", encoding="utf-8")
            profile = encoded_profile(
                replacements=[{"public": "alias.invalid", "private": "live.invalid"}],
                files=[
                    {
                        "root": 0,
                        "path": "proof.txt",
                        "content_b64": encoded_content(b"private-proof"),
                    }
                ],
            )

            forward = self.run_renderer(workspace, profile, "--root", "output")
            reverse = self.run_renderer(
                workspace, profile, "--reverse", "--root", "output"
            )

            self.assertEqual(forward.returncode, 0, forward.stderr)
            self.assertEqual(reverse.returncode, 0, reverse.stderr)
            self.assertEqual(source.read_text(encoding="utf-8"), "alias.invalid")
            self.assertFalse((output / "proof.txt").exists())

    def test_replacements_are_simultaneous_and_round_trip_with_overlap(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            source = workspace / "values.txt"
            source.write_text("a ab", encoding="utf-8")
            profile = encoded_profile(
                replacements=[
                    {"public": "a", "private": "b"},
                    {"public": "ab", "private": "c"},
                ]
            )

            forward = self.run_renderer(workspace, profile, "--root", "values.txt")
            self.assertEqual(forward.returncode, 0, forward.stderr)
            self.assertEqual(source.read_text(), "b c")
            reverse = self.run_renderer(
                workspace, profile, "--reverse", "--root", "values.txt"
            )
            self.assertEqual(reverse.returncode, 0, reverse.stderr)
            self.assertEqual(source.read_text(), "a ab")

    def test_duplicate_replacement_collision_is_rejected_before_mutation(self) -> None:
        cases = [
            [
                {"public": "same", "private": "private-one"},
                {"public": "same", "private": "private-two"},
            ],
            [
                {"public": "public-one", "private": "same"},
                {"public": "public-two", "private": "same"},
            ],
        ]
        for replacements in cases:
            with self.subTest(replacements=replacements):
                with tempfile.TemporaryDirectory() as temporary:
                    workspace = Path(temporary)
                    source = workspace / "file.txt"
                    source.write_text("same public-one", encoding="utf-8")
                    result = self.run_renderer(
                        workspace,
                        encoded_profile(replacements=replacements),
                        "--root",
                        "file.txt",
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertEqual(source.read_text(), "same public-one")
                    self.assertIn("collide", result.stderr)

    def test_outside_root_and_symlink_escape_are_rejected_without_secret_leak(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            parent = Path(temporary)
            workspace = parent / "workspace"
            outside = parent / "outside"
            workspace.mkdir()
            outside.mkdir()
            outside_file = outside / "data.txt"
            outside_file.write_text("alias.invalid", encoding="utf-8")
            profile = encoded_profile(
                replacements=[
                    {"public": "alias.invalid", "private": "private-live-value"}
                ]
            )

            outside_result = self.run_renderer(
                workspace, profile, "--root", "../outside"
            )
            link = workspace / "linked"
            link.symlink_to(outside, target_is_directory=True)
            link_result = self.run_renderer(workspace, profile, "--root", "linked")

            self.assertEqual(outside_result.returncode, 2)
            self.assertEqual(link_result.returncode, 2)
            self.assertEqual(outside_file.read_text(), "alias.invalid")
            combined = (
                outside_result.stdout
                + outside_result.stderr
                + link_result.stdout
                + link_result.stderr
            )
            self.assertNotIn("private-live-value", combined)

    def test_generated_path_traversal_and_git_paths_are_rejected(self) -> None:
        invalid_paths = ["../proof.txt", "/proof.txt", ".git/config", "a//proof.txt"]
        for invalid_path in invalid_paths:
            with self.subTest(path=invalid_path):
                with tempfile.TemporaryDirectory() as temporary:
                    workspace = Path(temporary)
                    output = workspace / "output"
                    output.mkdir()
                    profile = encoded_profile(
                        replacements=[],
                        files=[
                            {
                                "root": 0,
                                "path": invalid_path,
                                "content_b64": encoded_content(b"private-proof"),
                            }
                        ],
                    )
                    result = self.run_renderer(
                        workspace, profile, "--root", "output"
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertNotIn("private-proof", result.stdout + result.stderr)

    def test_generated_file_never_overwrites_or_deletes_different_content(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            output = workspace / "output"
            output.mkdir()
            target = output / "proof.txt"
            target.write_bytes(b"existing-public-content")
            profile = encoded_profile(
                replacements=[],
                files=[
                    {
                        "root": 0,
                        "path": "proof.txt",
                        "content_b64": encoded_content(b"private-proof"),
                    }
                ],
            )

            forward = self.run_renderer(workspace, profile, "--root", "output")
            reverse = self.run_renderer(
                workspace, profile, "--reverse", "--root", "output"
            )

            self.assertEqual(forward.returncode, 2)
            self.assertEqual(reverse.returncode, 2)
            self.assertEqual(target.read_bytes(), b"existing-public-content")
            self.assertNotIn("private-proof", forward.stderr + reverse.stderr)

    def test_generated_file_rejects_symlink_parent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            output = workspace / "output"
            outside = workspace / "outside"
            output.mkdir()
            outside.mkdir()
            (output / "linked").symlink_to(outside, target_is_directory=True)
            profile = encoded_profile(
                replacements=[],
                files=[
                    {
                        "root": 0,
                        "path": "linked/proof.txt",
                        "content_b64": encoded_content(b"private-proof"),
                    }
                ],
            )

            result = self.run_renderer(workspace, profile, "--root", "output")

            self.assertEqual(result.returncode, 2)
            self.assertFalse((outside / "proof.txt").exists())

    def test_empty_generated_file_is_supported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            output = workspace / "output"
            output.mkdir()
            profile = encoded_profile(
                replacements=[],
                files=[
                    {"root": 0, "path": "empty.txt", "content_b64": ""}
                ],
            )

            result = self.run_renderer(workspace, profile, "--root", "output")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((output / "empty.txt").read_bytes(), b"")

    def test_github_mask_mode_escapes_workflow_command_characters(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            profile = encoded_profile(
                replacements=[
                    {"public": "alias", "private": "value%line\r\nnext"}
                ]
            )

            result = self.run_renderer(workspace, profile, "--github-add-mask")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(
                result.stdout, "::add-mask::value%25line%0D%0Anext\n"
            )
            self.assertEqual(result.stderr, "")

    def test_skip_generated_files_only_renders_text(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            source = workspace / "worker.js"
            source.write_text("alias.invalid", encoding="utf-8")
            profile = encoded_profile(
                replacements=[
                    {"public": "alias.invalid", "private": "live.invalid"}
                ],
                files=[
                    {
                        "root": 9,
                        "path": "proof.txt",
                        "content_b64": encoded_content(b"private-proof"),
                    }
                ],
            )

            forward = self.run_renderer(
                workspace,
                profile,
                "--skip-generated-files",
                "--root",
                "worker.js",
            )
            reverse = self.run_renderer(
                workspace,
                profile,
                "--reverse",
                "--skip-generated-files",
                "--root",
                "worker.js",
            )

            self.assertEqual(forward.returncode, 0, forward.stderr)
            self.assertEqual(reverse.returncode, 0, reverse.stderr)
            self.assertEqual(source.read_text(encoding="utf-8"), "alias.invalid")
            self.assertFalse((workspace / "proof.txt").exists())

    def test_invalid_base64_configuration_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            source = workspace / "file.txt"
            source.write_text("unchanged", encoding="utf-8")

            result = self.run_renderer(
                workspace, "not-base64!", "--root", "file.txt"
            )

            self.assertEqual(result.returncode, 2)
            self.assertEqual(source.read_text(), "unchanged")
            self.assertIn("not valid base64", result.stderr)


if __name__ == "__main__":
    unittest.main()
