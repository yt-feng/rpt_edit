#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import io
import unittest
import urllib.parse
from typing import Any, Mapping
from unittest.mock import patch

import configure_portal_email_routing as routing


DESTINATION = "owner@example.net"
ZONE_NAME = "portal.example.invalid"
ZONE_ID = "zone-1"
ACCOUNT_ID = "account-1"


def literal_rule(*, enabled: bool = True, destination: str = DESTINATION) -> dict[str, Any]:
    return {
        "id": "literal-1",
        "name": routing.LITERAL_RULE_NAME,
        "enabled": enabled,
        "source": "api",
        "matchers": [{"type": "literal", "field": "to", "value": f"info@{ZONE_NAME}"}],
        "actions": [{"type": "forward", "value": [destination]}],
    }


def catch_all(*, enabled: bool = True, destination: str = DESTINATION) -> dict[str, Any]:
    return {
        "id": "catch-1",
        "name": routing.CATCH_ALL_RULE_NAME,
        "enabled": enabled,
        "source": "api",
        "matchers": [{"type": "all"}],
        "actions": [{"type": "forward", "value": [destination]}],
    }


class FakeApi:
    def __init__(
        self,
        *,
        destination: Mapping[str, Any] | None = None,
        dns_ready: bool = True,
        literal: Mapping[str, Any] | None = None,
        catch: Mapping[str, Any] | None = None,
    ) -> None:
        self.destination = dict(destination) if destination else None
        self.dns_ready = dns_ready
        self.literal = dict(literal) if literal else None
        self.catch = dict(catch) if catch else catch_all(enabled=False)
        self.calls: list[tuple[str, str, Mapping[str, Any] | None, str]] = []

    def call(
        self,
        path: str,
        *,
        method: str = "GET",
        body: Mapping[str, Any] | None = None,
        stage: str = "cloud_api",
    ) -> routing.ApiResponse:
        self.calls.append((path, method, body, stage))
        parsed = urllib.parse.urlsplit(path)
        clean_path = parsed.path
        if clean_path == "/zones" and method == "GET":
            return routing.ApiResponse(
                [{"id": ZONE_ID, "name": ZONE_NAME, "account": {"id": ACCOUNT_ID}}],
                {},
            )
        if clean_path.endswith("/email/routing/addresses"):
            if method == "GET":
                rows = [self.destination] if self.destination else []
                return routing.ApiResponse(rows, {"total_pages": 1})
            self.destination = {"id": "destination-1", "email": str(body and body["email"]), "verified": None}
            return routing.ApiResponse(self.destination, {})
        if clean_path.endswith("/email/routing/dns") and method == "POST":
            self.dns_ready = True
            return routing.ApiResponse({"enabled": True, "status": "ready"}, {})
        if clean_path.endswith("/email/routing") and method == "GET":
            status = "ready" if self.dns_ready else "unconfigured"
            return routing.ApiResponse({"enabled": self.dns_ready, "status": status}, {})
        if clean_path.endswith("/email/routing/rules/catch_all"):
            if method == "GET":
                return routing.ApiResponse(self.catch, {})
            self.catch = {"id": "catch-1", **dict(body or {})}
            return routing.ApiResponse(self.catch, {})
        if clean_path.endswith("/email/routing/rules"):
            if method == "GET":
                rows = [self.literal] if self.literal else []
                return routing.ApiResponse(rows, {"total_pages": 1})
            self.literal = {"id": "literal-1", **dict(body or {})}
            return routing.ApiResponse(self.literal, {})
        if "/email/routing/rules/" in clean_path and method == "PUT":
            self.literal = {"id": clean_path.rsplit("/", 1)[-1], **dict(body or {})}
            return routing.ApiResponse(self.literal, {})
        raise AssertionError(f"unexpected fake API call: {method} {clean_path}")

    def write_calls(self) -> list[tuple[str, str, Mapping[str, Any] | None, str]]:
        return [call for call in self.calls if call[1] != "GET"]


def config_env() -> dict[str, str]:
    return {
        "PORTAL_SITE_URL": f"https://{ZONE_NAME}",
        "PORTAL_FORWARD_DESTINATION_EMAIL": DESTINATION,
        "CLOUDFLARE_EMAIL_ROUTING_API_TOKEN": "dedicated-token",
        "CLOUDFLARE_API_TOKEN": "fallback-token",
        "CLOUDFLARE_EMAIL_ROUTING_ACCOUNT_ID": ACCOUNT_ID,
    }


class EmailRoutingTests(unittest.TestCase):
    def test_runtime_config_prefers_dedicated_token_and_requires_bare_origin(self) -> None:
        config = routing.runtime_config(config_env())
        self.assertEqual(config.api_token, "dedicated-token")
        self.assertEqual(config.site_hostname, ZONE_NAME)
        with self.assertRaisesRegex(routing.RoutingError, "bare_https_origin"):
            routing.runtime_config({**config_env(), "PORTAL_SITE_URL": f"https://{ZONE_NAME}/private"})

    def test_zone_discovery_walks_from_host_to_parent_and_checks_account(self) -> None:
        class DiscoveryApi:
            def __init__(self) -> None:
                self.names: list[str] = []

            def call(self, path: str, **_kwargs: object) -> routing.ApiResponse:
                name = urllib.parse.parse_qs(urllib.parse.urlsplit(path).query)["name"][0]
                self.names.append(name)
                rows = [] if name.startswith("www.") else [
                    {"id": ZONE_ID, "name": ZONE_NAME, "account": {"id": ACCOUNT_ID}}
                ]
                return routing.ApiResponse(rows, {})

        api = DiscoveryApi()
        zone = routing.discover_zone(api, f"www.{ZONE_NAME}", ACCOUNT_ID)
        self.assertEqual(api.names, [f"www.{ZONE_NAME}", ZONE_NAME])
        self.assertEqual(zone, routing.ZoneContext(ZONE_ID, ZONE_NAME, ACCOUNT_ID))
        with self.assertRaisesRegex(routing.RoutingError, "account_id_mismatch"):
            routing.discover_zone(api, ZONE_NAME, "wrong-account")

    def test_ready_apply_is_idempotent_and_performs_no_writes(self) -> None:
        api = FakeApi(
            destination={"id": "destination-1", "email": DESTINATION, "verified": "2026-01-01T00:00:00Z"},
            literal=literal_rule(),
            catch=catch_all(),
        )
        configurator = routing.EmailRoutingConfigurator(
            api,
            routing.ZoneContext(ZONE_ID, ZONE_NAME, ACCOUNT_ID),
            DESTINATION,
        )

        state = configurator.apply()

        self.assertTrue(state.ready)
        self.assertEqual(api.write_calls(), [])

    def test_apply_creates_missing_destination_then_stops_for_verification(self) -> None:
        api = FakeApi(dns_ready=False, literal=None, catch=catch_all(enabled=False))
        configurator = routing.EmailRoutingConfigurator(
            api,
            routing.ZoneContext(ZONE_ID, ZONE_NAME, ACCOUNT_ID),
            DESTINATION,
        )

        with self.assertRaises(routing.DestinationVerificationRequired):
            configurator.apply()

        writes = api.write_calls()
        self.assertEqual(len(writes), 1)
        self.assertTrue(writes[0][0].endswith("/email/routing/addresses"))
        self.assertEqual(writes[0][1], "POST")
        self.assertEqual(writes[0][2], {"email": DESTINATION})

    def test_apply_enables_dns_and_upserts_literal_and_catch_all(self) -> None:
        api = FakeApi(
            destination={"id": "destination-1", "email": DESTINATION, "verified": "2026-01-01T00:00:00Z"},
            dns_ready=False,
            literal=literal_rule(enabled=False, destination="old@example.net"),
            catch=catch_all(enabled=False, destination="old@example.net"),
        )
        configurator = routing.EmailRoutingConfigurator(
            api,
            routing.ZoneContext(ZONE_ID, ZONE_NAME, ACCOUNT_ID),
            DESTINATION,
        )

        state = configurator.apply()

        self.assertTrue(state.ready)
        writes = api.write_calls()
        self.assertEqual([call[3] for call in writes], [
            "routing_dns_enable",
            "literal_rule_update",
            "catch_all_update",
        ])
        self.assertEqual(writes[0][2], {"name": ZONE_NAME})
        self.assertEqual(writes[1][2], routing.literal_rule_body(f"info@{ZONE_NAME}", DESTINATION))
        self.assertEqual(writes[2][2], routing.catch_all_body(DESTINATION))
        final_write_index = max(index for index, call in enumerate(api.calls) if call[1] != "GET")
        self.assertEqual(
            [call[3] for call in api.calls[final_write_index + 1:]],
            ["destination_list", "routing_settings", "rule_list", "catch_all_read"],
        )

    def test_audit_reports_drift_without_writes(self) -> None:
        api = FakeApi(
            destination={"id": "destination-1", "email": DESTINATION, "verified": None},
            dns_ready=False,
        )
        configurator = routing.EmailRoutingConfigurator(
            api,
            routing.ZoneContext(ZONE_ID, ZONE_NAME, ACCOUNT_ID),
            DESTINATION,
        )

        state = configurator.inspect()

        self.assertFalse(state.ready)
        self.assertEqual(
            state.incomplete_components(),
            ("destination_unverified", "routing_dns", "literal_rule", "catch_all"),
        )
        self.assertEqual(api.write_calls(), [])

    def test_cli_masks_private_values_and_never_reports_them_in_status(self) -> None:
        api = FakeApi(
            destination={"id": "destination-1", "email": DESTINATION, "verified": "2026-01-01T00:00:00Z"},
            literal=literal_rule(),
            catch=catch_all(),
        )
        output = io.StringIO()
        with (
            patch.object(routing, "CloudflareApi", return_value=api),
            contextlib.redirect_stdout(output),
        ):
            code = routing.run(["--mode", "audit", "--github-add-mask"], config_env())

        self.assertEqual(code, 0)
        lines = output.getvalue().splitlines()
        self.assertTrue(any(line == f"::add-mask::{DESTINATION}" for line in lines))
        status_lines = [line for line in lines if not line.startswith("::add-mask::")]
        self.assertEqual(len(status_lines), 1)
        self.assertNotIn(DESTINATION, status_lines[0])
        self.assertNotIn(ZONE_NAME, status_lines[0])

    def test_http_error_uses_safe_stage_code_without_response_body(self) -> None:
        secret = "private-forward@example.net"
        error = urllib.error.HTTPError(
            "https://api.cloudflare.com/client/v4/example",
            403,
            secret,
            {},
            None,
        )
        with patch.object(routing.urllib.request, "urlopen", side_effect=error):
            with self.assertRaisesRegex(routing.RoutingError, "destination_list_http_403") as raised:
                routing.CloudflareApi("token").call("/example", stage="destination_list")
        self.assertNotIn(secret, str(raised.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2)
