#!/usr/bin/env python3
"""Audit or reconcile Cloudflare Email Routing for the private portal domain.

The public repository never contains the deployed domain or forwarding
destination.  The domain is derived from ``PORTAL_SITE_URL`` and the forwarding
destination is supplied only through ``PORTAL_FORWARD_DESTINATION_EMAIL``.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any, Mapping, Protocol, Sequence


API_ROOT = "https://api.cloudflare.com/client/v4"
PAGE_SIZE = 50
MAX_PAGES = 1000
PUBLIC_CONTACT_LOCAL_PART = "info"
LITERAL_RULE_NAME = "Portal public contact forwarding"
CATCH_ALL_RULE_NAME = "Portal catch-all forwarding"
READY_ROUTING_STATUS = "ready"


class RoutingError(RuntimeError):
    """A safe-to-print configuration failure code."""


class DestinationVerificationRequired(RoutingError):
    """The destination exists but still needs inbox verification."""


@dataclass(frozen=True)
class ApiResponse:
    result: Any
    result_info: Mapping[str, Any]


class ApiClient(Protocol):
    def call(
        self,
        path: str,
        *,
        method: str = "GET",
        body: Mapping[str, Any] | None = None,
        stage: str = "cloud_api",
    ) -> ApiResponse: ...


class CloudflareApi:
    def __init__(self, token: str, *, timeout: int = 30) -> None:
        if not token:
            raise RoutingError("api_token_missing")
        self._token = token
        self._timeout = timeout

    def call(
        self,
        path: str,
        *,
        method: str = "GET",
        body: Mapping[str, Any] | None = None,
        stage: str = "cloud_api",
    ) -> ApiResponse:
        data = None if body is None else json.dumps(body, separators=(",", ":")).encode("utf-8")
        request = urllib.request.Request(
            API_ROOT + path,
            data=data,
            method=method,
            headers={
                "Authorization": f"Bearer {self._token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=self._timeout) as response:
                payload = json.load(response)
        except urllib.error.HTTPError as error:
            raise RoutingError(f"{stage}_http_{error.code}") from None
        except (OSError, ValueError):
            raise RoutingError(f"{stage}_request_failed") from None
        if not isinstance(payload, dict) or payload.get("success") is not True:
            raise RoutingError(f"{stage}_rejected")
        result_info = payload.get("result_info")
        return ApiResponse(
            result=payload.get("result"),
            result_info=result_info if isinstance(result_info, dict) else {},
        )


@dataclass(frozen=True)
class RuntimeConfig:
    site_origin: str
    site_hostname: str
    forwarding_destination: str
    raw_forwarding_destination: str
    api_token: str
    expected_account_id: str


@dataclass(frozen=True)
class ZoneContext:
    zone_id: str
    zone_name: str
    account_id: str

    @property
    def public_contact(self) -> str:
        return f"{PUBLIC_CONTACT_LOCAL_PART}@{self.zone_name}"


@dataclass(frozen=True)
class AuditState:
    destination_present: bool
    destination_verified: bool
    routing_dns_ready: bool
    literal_rule_ready: bool
    catch_all_ready: bool

    @property
    def ready(self) -> bool:
        return all((
            self.destination_present,
            self.destination_verified,
            self.routing_dns_ready,
            self.literal_rule_ready,
            self.catch_all_ready,
        ))

    def incomplete_components(self) -> tuple[str, ...]:
        components: list[str] = []
        if not self.destination_present:
            components.append("destination_missing")
        elif not self.destination_verified:
            components.append("destination_unverified")
        if not self.routing_dns_ready:
            components.append("routing_dns")
        if not self.literal_rule_ready:
            components.append("literal_rule")
        if not self.catch_all_ready:
            components.append("catch_all")
        return tuple(components)


def clean_env(value: object) -> str:
    return str(value or "").strip()


def normalize_email(value: object) -> str:
    email = clean_env(value).lower()
    if len(email) > 254 or email.count("@") != 1 or re.search(r"\s", email):
        return ""
    local, domain = email.rsplit("@", 1)
    if not local or len(local) > 64 or not valid_hostname(domain):
        return ""
    return email


def valid_hostname(value: object) -> bool:
    hostname = clean_env(value).lower().rstrip(".")
    if not hostname or len(hostname) > 253 or "." not in hostname:
        return False
    labels = hostname.split(".")
    return all(
        label
        and len(label) <= 63
        and re.fullmatch(r"[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", label)
        for label in labels
    )


def parse_site_origin(value: object) -> tuple[str, str]:
    raw = clean_env(value)
    try:
        parsed = urllib.parse.urlsplit(raw)
    except ValueError:
        raise RoutingError("site_url_invalid") from None
    hostname = clean_env(parsed.hostname).lower().rstrip(".")
    try:
        port = parsed.port
    except ValueError:
        raise RoutingError("site_url_invalid") from None
    if (
        parsed.scheme != "https"
        or not valid_hostname(hostname)
        or parsed.username
        or parsed.password
        or port is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise RoutingError("site_url_must_be_bare_https_origin")
    return f"https://{hostname}", hostname


def runtime_config(environment: Mapping[str, str] | None = None) -> RuntimeConfig:
    env = os.environ if environment is None else environment
    site_origin, site_hostname = parse_site_origin(env.get("PORTAL_SITE_URL", ""))
    raw_destination = clean_env(env.get("PORTAL_FORWARD_DESTINATION_EMAIL", ""))
    destination = normalize_email(raw_destination)
    if not destination:
        raise RoutingError("forwarding_destination_invalid")
    api_token = clean_env(
        env.get("CLOUDFLARE_EMAIL_ROUTING_API_TOKEN", "")
        or env.get("CLOUDFLARE_API_TOKEN", "")
    )
    if not api_token:
        raise RoutingError("api_token_missing")
    expected_account_id = clean_env(
        env.get("CLOUDFLARE_EMAIL_ROUTING_ACCOUNT_ID", "")
        or env.get("CLOUDFLARE_ACCOUNT_ID", "")
        or env.get("R2_ACCOUNT_ID", "")
    )
    return RuntimeConfig(
        site_origin=site_origin,
        site_hostname=site_hostname,
        forwarding_destination=destination,
        raw_forwarding_destination=raw_destination,
        api_token=api_token,
        expected_account_id=expected_account_id,
    )


def zone_candidates(hostname: str) -> tuple[str, ...]:
    labels = hostname.split(".")
    return tuple(".".join(labels[offset:]) for offset in range(max(1, len(labels) - 1)))


def discover_zone(api: ApiClient, hostname: str, expected_account_id: str = "") -> ZoneContext:
    for candidate in zone_candidates(hostname):
        query = urllib.parse.urlencode({"name": candidate, "status": "active", "per_page": PAGE_SIZE})
        response = api.call(f"/zones?{query}", stage="zone_lookup")
        rows = response.result if isinstance(response.result, list) else []
        matches = [
            row for row in rows
            if isinstance(row, dict) and clean_env(row.get("name")).lower().rstrip(".") == candidate
        ]
        if len(matches) > 1:
            raise RoutingError("zone_lookup_ambiguous")
        if not matches:
            continue
        row = matches[0]
        zone_id = clean_env(row.get("id"))
        account = row.get("account") if isinstance(row.get("account"), dict) else {}
        discovered_account_id = clean_env(account.get("id"))
        if not zone_id:
            raise RoutingError("zone_id_missing")
        if expected_account_id and discovered_account_id and expected_account_id != discovered_account_id:
            raise RoutingError("account_id_mismatch")
        account_id = discovered_account_id or expected_account_id
        if not account_id:
            raise RoutingError("account_id_missing")
        return ZoneContext(zone_id=zone_id, zone_name=candidate, account_id=account_id)
    raise RoutingError("zone_not_found")


def paginated_rows(api: ApiClient, path: str, *, stage: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    separator = "&" if "?" in path else "?"
    for page in range(1, MAX_PAGES + 1):
        query_path = f"{path}{separator}{urllib.parse.urlencode({'page': page, 'per_page': PAGE_SIZE})}"
        response = api.call(query_path, stage=stage)
        batch = response.result if isinstance(response.result, list) else []
        rows.extend(row for row in batch if isinstance(row, dict))
        total_pages = response.result_info.get("total_pages")
        try:
            total_pages_number = int(total_pages)
        except (TypeError, ValueError):
            total_pages_number = 0
        if (total_pages_number and page >= total_pages_number) or len(batch) < PAGE_SIZE:
            return rows
    raise RoutingError(f"{stage}_pagination_limit")


def destination_matches(rows: Sequence[Mapping[str, Any]], destination: str) -> list[Mapping[str, Any]]:
    return [row for row in rows if normalize_email(row.get("email")) == destination]


def destination_is_verified(row: Mapping[str, Any]) -> bool:
    return bool(row.get("verified"))


def routing_dns_ready(settings: object) -> bool:
    return bool(
        isinstance(settings, dict)
        and settings.get("enabled") is True
        and clean_env(settings.get("status")).lower() == READY_ROUTING_STATUS
    )


def action_forwards_to(actions: object, destination: str) -> bool:
    if not isinstance(actions, list) or len(actions) != 1 or not isinstance(actions[0], dict):
        return False
    action = actions[0]
    values = action.get("value")
    normalized_values = [normalize_email(value) for value in values] if isinstance(values, list) else []
    return action.get("type") == "forward" and normalized_values == [destination]


def literal_rule_matches(rule: object, public_contact: str, destination: str) -> bool:
    if not isinstance(rule, dict) or rule.get("enabled") is not True:
        return False
    matchers = rule.get("matchers")
    if not isinstance(matchers, list) or len(matchers) != 1 or not isinstance(matchers[0], dict):
        return False
    matcher = matchers[0]
    return bool(
        matcher.get("type") == "literal"
        and matcher.get("field") == "to"
        and normalize_email(matcher.get("value")) == public_contact
        and action_forwards_to(rule.get("actions"), destination)
    )


def catch_all_matches(rule: object, destination: str) -> bool:
    if not isinstance(rule, dict) or rule.get("enabled") is not True:
        return False
    matchers = rule.get("matchers")
    return bool(
        isinstance(matchers, list)
        and len(matchers) == 1
        and isinstance(matchers[0], dict)
        and matchers[0].get("type") == "all"
        and action_forwards_to(rule.get("actions"), destination)
    )


def literal_rule_body(public_contact: str, destination: str) -> dict[str, Any]:
    return {
        "name": LITERAL_RULE_NAME,
        "enabled": True,
        "source": "api",
        "matchers": [{"type": "literal", "field": "to", "value": public_contact}],
        "actions": [{"type": "forward", "value": [destination]}],
    }


def catch_all_body(destination: str) -> dict[str, Any]:
    return {
        "name": CATCH_ALL_RULE_NAME,
        "enabled": True,
        "source": "api",
        "matchers": [{"type": "all"}],
        "actions": [{"type": "forward", "value": [destination]}],
    }


class EmailRoutingConfigurator:
    def __init__(self, api: ApiClient, zone: ZoneContext, destination: str) -> None:
        self.api = api
        self.zone = zone
        self.forwarding_destination = destination

    @property
    def destination_path(self) -> str:
        return f"/accounts/{urllib.parse.quote(self.zone.account_id, safe='')}/email/routing/addresses"

    @property
    def settings_path(self) -> str:
        return f"/zones/{urllib.parse.quote(self.zone.zone_id, safe='')}/email/routing"

    @property
    def dns_path(self) -> str:
        return f"{self.settings_path}/dns"

    @property
    def rules_path(self) -> str:
        return f"{self.settings_path}/rules"

    @property
    def catch_all_path(self) -> str:
        return f"{self.rules_path}/catch_all"

    def destinations(self) -> list[dict[str, Any]]:
        return paginated_rows(self.api, self.destination_path, stage="destination_list")

    def destination_record(self) -> Mapping[str, Any] | None:
        matches = destination_matches(self.destinations(), self.forwarding_destination)
        if len(matches) > 1:
            raise RoutingError("destination_ambiguous")
        return matches[0] if matches else None

    def settings(self) -> Mapping[str, Any]:
        result = self.api.call(self.settings_path, stage="routing_settings").result
        return result if isinstance(result, dict) else {}

    def literal_rules(self) -> list[dict[str, Any]]:
        return paginated_rows(self.api, self.rules_path, stage="rule_list")

    def matching_literal_rules(self, rows: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
        public_contact = self.zone.public_contact
        matches = []
        for row in rows:
            matchers = row.get("matchers")
            if not isinstance(matchers, list):
                continue
            if any(
                isinstance(matcher, dict)
                and matcher.get("type") == "literal"
                and matcher.get("field") == "to"
                and normalize_email(matcher.get("value")) == public_contact
                for matcher in matchers
            ):
                matches.append(row)
        if len(matches) > 1:
            raise RoutingError("literal_rule_ambiguous")
        return matches

    def catch_all(self) -> Mapping[str, Any]:
        result = self.api.call(self.catch_all_path, stage="catch_all_read").result
        return result if isinstance(result, dict) else {}

    def inspect(self) -> AuditState:
        destination = self.destination_record()
        present = destination is not None
        verified = bool(destination and destination_is_verified(destination))
        settings = self.settings()
        dns_ready = routing_dns_ready(settings)
        if not dns_ready:
            return AuditState(present, verified, False, False, False)
        literal_matches = self.matching_literal_rules(self.literal_rules())
        literal_ready = bool(
            literal_matches
            and literal_rule_matches(
                literal_matches[0],
                self.zone.public_contact,
                self.forwarding_destination,
            )
        )
        catch_ready = catch_all_matches(self.catch_all(), self.forwarding_destination)
        return AuditState(present, verified, True, literal_ready, catch_ready)

    def ensure_verified_destination(self) -> None:
        existing = self.destination_record()
        if existing is None:
            created = self.api.call(
                self.destination_path,
                method="POST",
                body={"email": self.forwarding_destination},
                stage="destination_create",
            ).result
            if not isinstance(created, dict) or not destination_is_verified(created):
                raise DestinationVerificationRequired("destination_verification_required")
            return
        if not destination_is_verified(existing):
            raise DestinationVerificationRequired("destination_verification_required")

    def ensure_routing_dns(self) -> None:
        if routing_dns_ready(self.settings()):
            return
        self.api.call(
            self.dns_path,
            method="POST",
            body={"name": self.zone.zone_name},
            stage="routing_dns_enable",
        )
        if not routing_dns_ready(self.settings()):
            raise RoutingError("routing_dns_not_ready")

    def ensure_literal_rule(self) -> None:
        matches = self.matching_literal_rules(self.literal_rules())
        desired = literal_rule_body(self.zone.public_contact, self.forwarding_destination)
        if not matches:
            self.api.call(self.rules_path, method="POST", body=desired, stage="literal_rule_create")
            return
        existing = matches[0]
        if literal_rule_matches(
            existing,
            self.zone.public_contact,
            self.forwarding_destination,
        ):
            return
        rule_id = clean_env(existing.get("id"))
        if not rule_id:
            raise RoutingError("literal_rule_id_missing")
        self.api.call(
            f"{self.rules_path}/{urllib.parse.quote(rule_id, safe='')}",
            method="PUT",
            body=desired,
            stage="literal_rule_update",
        )

    def ensure_catch_all(self) -> None:
        existing = self.catch_all()
        if catch_all_matches(existing, self.forwarding_destination):
            return
        self.api.call(
            self.catch_all_path,
            method="PUT",
            body=catch_all_body(self.forwarding_destination),
            stage="catch_all_update",
        )

    def apply(self) -> AuditState:
        self.ensure_verified_destination()
        self.ensure_routing_dns()
        self.ensure_literal_rule()
        self.ensure_catch_all()
        state = self.inspect()
        if not state.ready:
            raise RoutingError("read_back_validation_failed")
        return state


def emit_github_masks(values: Sequence[str]) -> None:
    seen: set[str] = set()
    for value in values:
        clean = clean_env(value)
        if not clean or clean in seen:
            continue
        seen.add(clean)
        escaped = clean.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        print(f"::add-mask::{escaped}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audit or apply the portal Email Routing configuration.")
    parser.add_argument("--mode", choices=("audit", "apply"), default="audit")
    parser.add_argument("--github-add-mask", action="store_true")
    return parser


def run(argv: Sequence[str] | None = None, environment: Mapping[str, str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        config = runtime_config(environment)
        api = CloudflareApi(config.api_token)
        zone = discover_zone(api, config.site_hostname, config.expected_account_id)
        if args.github_add_mask:
            emit_github_masks((
                config.raw_forwarding_destination,
                config.forwarding_destination,
                config.site_origin,
                zone.public_contact,
            ))
        configurator = EmailRoutingConfigurator(api, zone, config.forwarding_destination)
        if args.mode == "audit":
            state = configurator.inspect()
            if not state.ready:
                print(f"email routing audit: changes_required components={','.join(state.incomplete_components())}")
                return 1
            print("email routing audit: destination=verified dns=ready literal=ready catch_all=ready")
            return 0
        configurator.apply()
        print("email routing apply: destination=verified dns=ready literal=ready catch_all=ready")
        return 0
    except DestinationVerificationRequired:
        print("email routing apply: destination verification required; verify the inbox message and rerun")
        return 3
    except RoutingError as error:
        print(f"email routing configuration failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(run())
