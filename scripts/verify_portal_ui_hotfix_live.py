"""Read-only acceptance of a prepared UI hotfix, with exact version checks."""
from __future__ import annotations
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urlsplit
import requests
from portal_english_ui import account_session_key


def identity(receipt):
    value = {"schema_version": 1, "slot": receipt["slot"], "release_id": receipt["release_id"], "tree_sha256": receipt["tree_sha256"]}
    if value["slot"] not in {"a", "b"} or not re.fullmatch(r"[0-9a-f]{32}", value["release_id"]) or not re.fullmatch(r"[0-9a-f]{64}", value["tree_sha256"]):
        raise ValueError("Invalid candidate identity")
    return value


def fetch(session, url, *, body=None):
    kwargs = {"timeout": (10, 30), "allow_redirects": False}
    response = session.get(url, **kwargs) if body is None else session.post(url, json=body, **kwargs)
    if len(response.content) > 4 * 1024 * 1024:
        raise ValueError("Acceptance response exceeds bound")
    return response


def verify_english_account_session(origin, page, session, *, cached=None):
    """Check the deployed scripts referenced by this exact English preview."""
    references = {name: [] for name in ("app.js", "english-commentary.js")}
    class Scripts(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != "script":
                return
            for key, value in attrs:
                if key != "src" or not value:
                    continue
                for name in references:
                    if urlsplit(value).path == "/assets/" + name:
                        references[name].append(value)
        handle_startendtag = handle_starttag
    parser = Scripts(); parser.feed(page.decode("utf-8")); parser.close()
    scripts = {}
    for name, values in references.items():
        if len(values) != 1 or not re.fullmatch(r"/assets/" + re.escape(name) + r"\?v=[0-9a-f]{12}", values[0]):
            raise ValueError("English account script reference is missing or ambiguous")
        url = origin.rstrip("/") + values[0]
        raw = (cached or {}).get(url)
        if raw is None:
            response = fetch(session, url)
            if response.status_code != 200:
                raise ValueError("English account script is unavailable")
            raw = response.content
        if hashlib.sha256(raw).hexdigest()[:12] != values[0].rsplit("=", 1)[1]:
            raise ValueError("English account script fingerprint differs")
        scripts[name] = raw
    if account_session_key(scripts["app.js"], "AUTH_SESSION_KEY") != account_session_key(scripts["english-commentary.js"], "SESSION"):
        raise ValueError("English commentary and account session keys differ")
    return {"english_account_session": "matched"}


def verify(origin, receipt, session, *, expect_previous=False):
    parsed = urlsplit(origin)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password or parsed.port or parsed.path not in {"", "/"} or parsed.query or parsed.fragment:
        raise ValueError("Expected bare HTTPS origin")
    origin = origin.rstrip("/")
    expected = receipt["previous"] if expect_previous else identity(receipt)
    state = fetch(session, origin + "/.well-known/edge-state?ui-hotfix=" + receipt["release_id"])
    if state.status_code != 200 or state.json() != expected:
        raise ValueError("Live static identity does not match expected release")
    if expect_previous:
        return {"status": "passed", "previous_unchanged": True}
    changes = receipt["changed_files"]
    if not isinstance(changes, dict) or not changes:
        raise ValueError("Missing changed asset inventory")
    samples = {name for name in changes if name.startswith("assets/") or "/" not in name}
    english = sorted(name for name in changes if re.fullmatch(r"en/blog/\d{8}-[0-9a-f]{16}\.html", name))
    if english:
        samples.update(["en/index.html", english[0], english[-1]])
    checked = {}
    for name in sorted(samples):
        if not re.fullmatch(r"(?:assets/[A-Za-z0-9._-]+|[A-Za-z0-9._-]+\.html|en/(?:index|blog/\d{8}-[0-9a-f]{16})\.html)", name):
            raise ValueError("Unexpected acceptance path")
        descriptor = changes[name]
        digest = descriptor["sha256"]
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValueError("Invalid asset digest")
        route = {"index.html": "/", "charts.html": "/charts", "en/index.html": "/en/"}.get(name, "/" + name)
        url = origin + route + ("?v=" + digest[:12] if name.startswith("assets/") else "")
        response = fetch(session, url)
        if response.status_code != 200 or len(response.content) != descriptor["size"] or hashlib.sha256(response.content).hexdigest() != digest:
            raise ValueError("Live UI bytes differ from committed candidate")
        checked[url] = response.content
    account_session = {}
    if english:
        account_session = verify_english_account_session(origin, checked[origin + "/" + english[0]], session, cached=checked)
    health = fetch(session, origin + "/api/health")
    if health.status_code != 200:
        raise ValueError("API health failed")
    access = fetch(session, origin + "/api/course/full/access")
    if access.status_code != 401:
        raise ValueError("Anonymous course access boundary differs")
    if english:
        article_id = Path(english[0]).stem
        read = fetch(session, origin + "/api/english/commentary/read", body={"id": article_id})
        if read.status_code != 401 or read.json() != {"error": "login_required"} or "no-store" not in read.headers.get("Cache-Control", ""):
            raise ValueError("Anonymous English full-read boundary differs")
    # A concurrent release during the checks must not be accepted.
    state = fetch(session, origin + "/.well-known/edge-state?ui-hotfix=" + receipt["release_id"])
    if state.status_code != 200 or state.json() != expected:
        raise ValueError("Live release changed during acceptance")
    return {"status": "passed", "release_id": receipt["release_id"], "public_assets_verified": len(samples), "anonymous_full_reads": "denied", **account_session}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--origin", required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--expect-previous", action="store_true")
    args = parser.parse_args()
    with requests.Session() as session:
        print(json.dumps(verify(args.origin, json.loads(args.receipt.read_text()), session, expect_previous=args.expect_previous)))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        raise SystemExit("UI hotfix acceptance failed; private details omitted") from None
