#!/usr/bin/env python3

import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import preflight_social_publish as preflight


class Result:
    def __init__(self, status="healthy", reason="authenticated"):
        self.status = status
        self.reason = reason


def complete_env() -> dict[str, str]:
    return {
        "YOUTUBE_CLIENT_ID": "youtube-client-secret-value",
        "YOUTUBE_CLIENT_SECRET": "youtube-client-secret",
        "YOUTUBE_REFRESH_TOKEN": "youtube-refresh-secret",
        "YOUTUBE_CHANNEL_ID": "expected-youtube-channel",
        "LINKEDIN_CLIENT_ID": "linkedin-client",
        "LINKEDIN_CLIENT_SECRET": "linkedin-client-secret",
        "LINKEDIN_ACCESS_TOKEN": "linkedin-access-secret",
        "LINKEDIN_AUTHOR_URN": "urn:li:person:expected-author",
        "X_API_KEY": "x-key-secret",
        "X_API_SECRET": "x-api-secret",
        "X_ACCESS_TOKEN": "x-access-secret",
        "X_ACCESS_TOKEN_SECRET": "x-token-secret",
        "X_USER_ID": "expected-x-user",
        "X_OAUTH1_SCOPES": "read write",
    }


class PreflightTests(unittest.TestCase):
    def test_each_platform_exports_only_its_credentials_after_healthy_probe(self):
        env = complete_env()
        probes = {
            "youtube_probe": lambda _env: Result(),
            "linkedin_probe": lambda _env: Result(),
            "x_probe": lambda _env: Result(),
        }
        for platform, expected_names in preflight.PLATFORM_EXPORTS.items():
            with self.subTest(platform=platform), tempfile.TemporaryDirectory() as temporary:
                values = preflight.preflight(platform, env, **probes)
                self.assertEqual(set(values), set(expected_names))
                output = Path(temporary) / "github-env"
                preflight.append_github_env(output, values)
                rendered = output.read_text(encoding="utf-8")
                self.assertEqual(
                    {line.split("=", 1)[0] for line in rendered.splitlines()},
                    set(expected_names),
                )

    def test_nonhealthy_or_mismatched_identity_configuration_exports_nothing(self):
        env = complete_env()
        with self.assertRaisesRegex(preflight.PreflightError, "permission_denied"):
            preflight.preflight(
                "x",
                env,
                x_probe=lambda _env: Result("permission_denied", "identity_mismatch"),
            )
        missing_identity = dict(env)
        missing_identity.pop("YOUTUBE_CHANNEL_ID")
        with self.assertRaisesRegex(preflight.PreflightError, "YOUTUBE_CHANNEL_ID"):
            preflight.preflight(
                "youtube",
                missing_identity,
                youtube_probe=lambda _env: Result(),
            )

    def test_cli_output_never_contains_exported_secret_values(self):
        env = complete_env()
        with tempfile.TemporaryDirectory() as temporary:
            github_env = Path(temporary) / "github-env"
            stdout = io.StringIO()
            stderr = io.StringIO()
            original = preflight.preflight
            try:
                preflight.preflight = lambda platform, _env: {
                    name: env[name] for name in preflight.PLATFORM_EXPORTS[platform]
                }
                with redirect_stdout(stdout), redirect_stderr(stderr):
                    result = preflight.main([
                        "--platform", "x", "--github-env", str(github_env),
                    ])
            finally:
                preflight.preflight = original
            self.assertEqual(result, 0)
            rendered = stdout.getvalue() + stderr.getvalue()
            for secret in env.values():
                self.assertNotIn(secret, rendered)


if __name__ == "__main__":
    unittest.main()
