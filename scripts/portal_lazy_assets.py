"""Fingerprint lazy modules before their loaders and HTML are fingerprinted."""
from __future__ import annotations

import hashlib
from pathlib import Path
import re


NEWSFEED_MODULE = "newsfeed-app.js"
NEWSFEED_LOADER = re.compile(r'(const NEWSFEED_APP_ASSET = "assets/newsfeed-app\.js\?v=)[^"\s]+(";)')


def fingerprint_newsfeed_loader(root: Path) -> None:
    app, module = root / "assets/app.js", root / "assets" / NEWSFEED_MODULE
    if not app.is_file():
        return
    source = app.read_text(encoding="utf-8")
    matches = list(NEWSFEED_LOADER.finditer(source))
    if not matches and not module.is_file():
        return
    if len(matches) != 1 or not module.is_file():
        raise ValueError("Lazy Newsfeed module and unique loader must be present together")
    digest = hashlib.sha256(module.read_bytes()).hexdigest()[:12]
    updated = NEWSFEED_LOADER.sub(lambda match: match[1] + digest + match[2], source)
    if updated != source:
        app.write_text(updated, encoding="utf-8")
