#!/usr/bin/env python3
"""Read one DeepSeek balance snapshot without generating text or changing funds."""

from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
import json
import os
from pathlib import Path
import re
import sys
from typing import Any, Callable

from build_portal_locales import DEEPSEEK_KEY_ENV_NAMES


BALANCE_URL = "https://api.deepseek.com/user/balance"
BALANCE_FIELDS = ("total_balance", "granted_balance", "topped_up_balance")


class BalanceCheckError(RuntimeError):
    """Only locally generated, credential-free messages may use this type."""


def _balance_number(raw: Any) -> str:
    if not isinstance(raw, str) or not raw.strip() or len(raw) > 64:
        raise BalanceCheckError("Invalid balance number")
    try:
        value = Decimal(raw.strip())
    except InvalidOperation:
        raise BalanceCheckError("Invalid balance number") from None
    if not value.is_finite() or value.adjusted() > 30 or value.as_tuple().exponent < -30:
        raise BalanceCheckError("Invalid balance number")
    return format(value, "f")


def read_balance(
    *, diagnostics_out: Path | None = None, transport: Callable[..., Any] | None = None,
) -> dict[str, Any]:
    """Return a safe status report; callers must check status and is_available."""
    report: dict[str, Any] = {
        "schema_version": 1, "mode": "balance", "status": "failed",
        "provider_requests": 0, "balance_requests": 0,
    }
    try:
        credential = next((
            value.strip()
            for name in DEEPSEEK_KEY_ENV_NAMES
            for value in re.split(r"[\n,;]+", os.getenv(name, ""))
            if value.strip()
        ), "")
        if not credential:
            raise BalanceCheckError("A DeepSeek API key is required for the balance check")
        if transport is None:
            import requests

            transport = requests.get
        report["balance_requests"] = 1
        try:
            response = transport(
                BALANCE_URL, headers={"Authorization": f"Bearer {credential}"},
                timeout=30, allow_redirects=False,
            )
        except Exception as error:
            # Transport exception text may echo URLs, headers or credentials.
            raise BalanceCheckError(f"Balance request failed ({type(error).__name__})") from None
        status = getattr(response, "status_code", None)
        if type(status) is not int or not 100 <= status <= 599:
            raise BalanceCheckError("Invalid balance HTTP status")
        report["http_status"] = status
        if status != 200:
            raise BalanceCheckError(f"Balance endpoint returned HTTP {status}")
        try:
            payload = response.json()
        except Exception:
            raise BalanceCheckError("Balance endpoint returned invalid JSON") from None
        if not isinstance(payload, dict) or type(payload.get("is_available")) is not bool:
            raise BalanceCheckError("Invalid balance availability field")
        infos = payload.get("balance_infos")
        if not isinstance(infos, list) or len(infos) > 20:
            raise BalanceCheckError("Invalid balance information list")
        balances, currencies = [], set()
        for item in infos:
            if not isinstance(item, dict):
                raise BalanceCheckError("Invalid balance information row")
            currency = item.get("currency")
            if not isinstance(currency, str) or currency not in {"CNY", "USD"} or currency in currencies:
                raise BalanceCheckError("Invalid or repeated balance currency")
            currencies.add(currency)
            balances.append({"currency": currency, **{field: _balance_number(item.get(field)) for field in BALANCE_FIELDS}})
        report.update(status="passed", is_available=payload["is_available"], balance_infos=balances)
    except BalanceCheckError as error:
        report["error"] = str(error)
    except Exception as error:
        report["error"] = f"Balance check failed ({type(error).__name__})"
    if diagnostics_out is not None:
        diagnostics_out.parent.mkdir(parents=True, exist_ok=True)
        diagnostics_out.write_text(json.dumps(report, ensure_ascii=True, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--diagnostics-out", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = read_balance(diagnostics_out=args.diagnostics_out)
    except OSError:
        print("Unable to save balance diagnostics", file=sys.stderr)
        return 1
    print(json.dumps(report, ensure_ascii=True, sort_keys=True))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
