#!/usr/bin/env python3
"""Render deployment-only values and files without persisting their config.

The profile is base64-encoded JSON with ``version``, ``replacements``, and an
optional ``files`` array.  A file entry's ``root`` is the zero-based index of
the corresponding ``--root`` option in command-line order.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


CONFIG_ENV = "PORTAL_PRIVATE_CONFIG_B64"
CONFIG_VERSION = 1


class RenderError(Exception):
    """An expected validation or rendering failure safe to report."""


@dataclass(frozen=True)
class Replacement:
    public: str
    private: str


@dataclass(frozen=True)
class GeneratedFile:
    root_index: int
    relative_parts: tuple[str, ...]
    content: bytes


@dataclass(frozen=True)
class Profile:
    replacements: tuple[Replacement, ...]
    files: tuple[GeneratedFile, ...]


@dataclass(frozen=True)
class Root:
    path: Path
    is_directory: bool


@dataclass(frozen=True)
class GeneratedTarget:
    root: Path
    relative_parts: tuple[str, ...]
    path: Path
    content: bytes


def _object_without_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise RenderError("configuration contains duplicate object keys")
        result[key] = value
    return result


def _decode_base64(value: object, *, label: str, allow_empty: bool = False) -> bytes:
    if not isinstance(value, str):
        raise RenderError(f"{label} must be a non-empty base64 string")
    compact = "".join(value.split())
    if not compact and not allow_empty:
        raise RenderError(f"{label} must be a non-empty base64 string")
    try:
        return base64.b64decode(compact, validate=True)
    except (binascii.Error, ValueError):
        raise RenderError(f"{label} is not valid base64") from None


def _parse_relative_file_path(value: object, *, index: int) -> tuple[str, ...]:
    if not isinstance(value, str) or not value or "\x00" in value:
        raise RenderError(f"file entry {index} has an invalid path")
    if value.startswith("/") or "\\" in value:
        raise RenderError(f"file entry {index} path must be relative")
    parts = tuple(value.split("/"))
    if any(part in {"", ".", "..", ".git"} for part in parts):
        raise RenderError(f"file entry {index} path is not allowed")
    return parts


def load_profile(encoded: str | None) -> Profile:
    if not encoded:
        raise RenderError(f"{CONFIG_ENV} is required")
    decoded = _decode_base64(encoded, label="configuration")
    try:
        text = decoded.decode("utf-8")
        raw = json.loads(text, object_pairs_hook=_object_without_duplicate_keys)
    except UnicodeDecodeError:
        raise RenderError("configuration must be UTF-8 JSON") from None
    except json.JSONDecodeError:
        raise RenderError("configuration is not valid JSON") from None

    if not isinstance(raw, dict):
        raise RenderError("configuration must be a JSON object")
    allowed_keys = {"version", "replacements", "files"}
    if set(raw) - allowed_keys or "version" not in raw or "replacements" not in raw:
        raise RenderError("configuration has an unsupported shape")
    if type(raw["version"]) is not int or raw["version"] != CONFIG_VERSION:
        raise RenderError("configuration version is unsupported")

    replacement_entries = raw["replacements"]
    if not isinstance(replacement_entries, list):
        raise RenderError("replacements must be an array")
    replacements: list[Replacement] = []
    public_values: set[str] = set()
    private_values: set[str] = set()
    for index, entry in enumerate(replacement_entries):
        if not isinstance(entry, dict) or set(entry) != {"public", "private"}:
            raise RenderError(f"replacement entry {index} has an unsupported shape")
        public = entry["public"]
        private = entry["private"]
        if (
            not isinstance(public, str)
            or not isinstance(private, str)
            or not public
            or not private
            or "\x00" in public
            or "\x00" in private
        ):
            raise RenderError(f"replacement entry {index} has invalid values")
        if public == private:
            raise RenderError(f"replacement entry {index} does not change its value")
        if public in public_values or private in private_values:
            raise RenderError("replacement entries collide")
        public_values.add(public)
        private_values.add(private)
        replacements.append(Replacement(public=public, private=private))

    file_entries = raw.get("files", [])
    if not isinstance(file_entries, list):
        raise RenderError("files must be an array")
    files: list[GeneratedFile] = []
    file_keys: set[tuple[int, tuple[str, ...]]] = set()
    for index, entry in enumerate(file_entries):
        if not isinstance(entry, dict) or set(entry) != {"root", "path", "content_b64"}:
            raise RenderError(f"file entry {index} has an unsupported shape")
        root_index = entry["root"]
        if type(root_index) is not int or root_index < 0:
            raise RenderError(f"file entry {index} has an invalid root index")
        relative_parts = _parse_relative_file_path(entry["path"], index=index)
        content = _decode_base64(
            entry["content_b64"],
            label=f"file entry {index} content",
            allow_empty=True,
        )
        key = (root_index, relative_parts)
        if key in file_keys:
            raise RenderError("file entries collide")
        file_keys.add(key)
        files.append(
            GeneratedFile(
                root_index=root_index,
                relative_parts=relative_parts,
                content=content,
            )
        )

    if not replacements and not files:
        raise RenderError("configuration has no rendering actions")
    return Profile(replacements=tuple(replacements), files=tuple(files))


def _is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def resolve_roots(raw_roots: Sequence[str], *, workspace: Path) -> tuple[Root, ...]:
    try:
        workspace = workspace.resolve(strict=True)
    except OSError:
        raise RenderError("working directory cannot be resolved") from None

    roots: list[Root] = []
    for raw_root in raw_roots:
        requested = Path(raw_root)
        if not requested.is_absolute():
            requested = workspace / requested
        if requested.is_symlink():
            raise RenderError("a root may not be a symbolic link")
        try:
            resolved = requested.resolve(strict=True)
        except OSError:
            raise RenderError("a root does not exist") from None
        if not _is_within(resolved, workspace):
            raise RenderError("a root is outside the working directory")
        relative = resolved.relative_to(workspace)
        if ".git" in relative.parts:
            raise RenderError("a root may not select repository metadata")
        if resolved.is_dir():
            roots.append(Root(path=resolved, is_directory=True))
        elif resolved.is_file():
            roots.append(Root(path=resolved, is_directory=False))
        else:
            raise RenderError("a root must be a regular file or directory")
    return tuple(roots)


def _validate_target_components(root: Path, parts: tuple[str, ...]) -> Path:
    current = root
    for index, part in enumerate(parts):
        current = current / part
        if current.is_symlink():
            raise RenderError("a generated file path contains a symbolic link")
        if index < len(parts) - 1 and current.exists() and not current.is_dir():
            raise RenderError("a generated file parent is not a directory")
    try:
        resolved = current.resolve(strict=False)
    except OSError:
        raise RenderError("a generated file path cannot be resolved") from None
    if not _is_within(resolved, root):
        raise RenderError("a generated file path escapes its root")
    if current.exists() and not current.is_file():
        raise RenderError("a generated file target is not a regular file")
    return current


def prepare_generated_targets(
    profile: Profile,
    roots: Sequence[Root],
    *,
    reverse: bool,
) -> tuple[GeneratedTarget, ...]:
    targets: list[GeneratedTarget] = []
    seen: set[Path] = set()
    for generated in profile.files:
        if generated.root_index >= len(roots):
            raise RenderError("a generated file root index is out of range")
        root = roots[generated.root_index]
        if not root.is_directory:
            raise RenderError("a generated file root must be a directory")
        target = _validate_target_components(root.path, generated.relative_parts)
        resolved_target = target.resolve(strict=False)
        if resolved_target in seen:
            raise RenderError("generated file targets collide")
        seen.add(resolved_target)
        if target.exists():
            try:
                existing = target.read_bytes()
            except OSError:
                raise RenderError("a generated file cannot be read") from None
            if existing != generated.content:
                action = "removed" if reverse else "created"
                raise RenderError(f"a generated file cannot be safely {action}")
        targets.append(
            GeneratedTarget(
                root=root.path,
                relative_parts=generated.relative_parts,
                path=target,
                content=generated.content,
            )
        )
    return tuple(targets)


def _iter_root_files(roots: Sequence[Root]) -> Iterable[Path]:
    seen: set[Path] = set()
    for root in roots:
        if not root.is_directory:
            candidates = (root.path,)
        else:
            collected: list[Path] = []
            for directory, directory_names, file_names in os.walk(
                root.path, topdown=True, followlinks=False
            ):
                directory_path = Path(directory)
                directory_names[:] = sorted(
                    name
                    for name in directory_names
                    if name != ".git" and not (directory_path / name).is_symlink()
                )
                for name in sorted(file_names):
                    if name == ".git":
                        continue
                    candidate = directory_path / name
                    if not candidate.is_symlink() and candidate.is_file():
                        collected.append(candidate)
            candidates = collected
        for candidate in candidates:
            try:
                resolved = candidate.resolve(strict=True)
            except OSError:
                raise RenderError("a file cannot be resolved") from None
            if resolved not in seen:
                seen.add(resolved)
                yield candidate


def _replacement_engine(
    replacements: Sequence[Replacement], *, reverse: bool
) -> tuple[re.Pattern[str] | None, dict[str, str]]:
    if reverse:
        mapping = {item.private: item.public for item in replacements}
    else:
        mapping = {item.public: item.private for item in replacements}
    if not mapping:
        return None, mapping
    ordered = sorted(mapping, key=lambda value: (-len(value), value))
    return re.compile("|".join(re.escape(value) for value in ordered)), mapping


def render_text_files(
    roots: Sequence[Root],
    replacements: Sequence[Replacement],
    *,
    reverse: bool,
    excluded: set[Path],
) -> tuple[int, int]:
    pattern, mapping = _replacement_engine(replacements, reverse=reverse)
    processed = 0
    changed = 0
    for path in _iter_root_files(roots):
        try:
            resolved = path.resolve(strict=True)
        except OSError:
            raise RenderError("a file cannot be resolved") from None
        if resolved in excluded:
            continue
        try:
            data = path.read_bytes()
        except OSError:
            raise RenderError("a file cannot be read") from None
        if b"\x00" in data:
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
        processed += 1
        if pattern is None:
            continue
        rendered = pattern.sub(lambda match: mapping[match.group(0)], text)
        if rendered == text:
            continue
        try:
            path.write_bytes(rendered.encode("utf-8"))
        except OSError:
            raise RenderError("a file cannot be written") from None
        changed += 1
    return processed, changed


def remove_generated_files(targets: Sequence[GeneratedTarget]) -> int:
    removed = 0
    for target in targets:
        if not target.path.exists():
            continue
        try:
            if target.path.is_symlink() or target.path.read_bytes() != target.content:
                raise RenderError("a generated file cannot be safely removed")
            target.path.unlink()
        except RenderError:
            raise
        except OSError:
            raise RenderError("a generated file cannot be removed") from None
        removed += 1
    return removed


def create_generated_files(targets: Sequence[GeneratedTarget]) -> int:
    created = 0
    for target in targets:
        if target.path.exists():
            continue
        try:
            target.path.parent.mkdir(parents=True, exist_ok=True)
            verified_target = _validate_target_components(
                target.root, target.relative_parts
            )
            if verified_target != target.path:
                raise RenderError("a generated file path changed during rendering")
            with target.path.open("xb") as handle:
                handle.write(target.content)
        except FileExistsError:
            try:
                if target.path.is_symlink() or target.path.read_bytes() != target.content:
                    raise RenderError("a generated file cannot be safely created")
            except OSError:
                raise RenderError("a generated file cannot be verified") from None
        except RenderError:
            raise
        except OSError:
            raise RenderError("a generated file cannot be created") from None
        else:
            created += 1
    return created


def _escape_workflow_command(value: str) -> str:
    return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def emit_github_masks(replacements: Sequence[Replacement]) -> None:
    private_values = {item.private for item in replacements}
    for private in sorted(private_values, key=lambda value: (-len(value), value)):
        sys.stdout.write(f"::add-mask::{_escape_workflow_command(private)}\n")
    sys.stdout.flush()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Render a base64-encoded private deployment profile in place.",
        epilog=(
            "Each files[].root value is a zero-based index into the --root options "
            "in command-line order."
        ),
    )
    parser.add_argument(
        "--root",
        action="append",
        default=[],
        help="File or directory inside the working directory; may be repeated.",
    )
    parser.add_argument(
        "--reverse",
        action="store_true",
        help="Replace private values with public values and remove generated files.",
    )
    parser.add_argument(
        "--github-add-mask",
        action="store_true",
        help="Register private replacement values with GitHub Actions masking.",
    )
    parser.add_argument(
        "--skip-generated-files",
        action="store_true",
        help="Apply text replacements without creating or removing profile files.",
    )
    return parser


def run(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.root and not args.github_add_mask:
        parser.error("at least one --root or --github-add-mask is required")

    try:
        profile = load_profile(os.environ.get(CONFIG_ENV))
        roots = resolve_roots(args.root, workspace=Path.cwd())
        targets = (
            prepare_generated_targets(profile, roots, reverse=args.reverse)
            if roots and not args.skip_generated_files
            else ()
        )

        if args.github_add_mask:
            emit_github_masks(profile.replacements)

        removed = 0
        created = 0
        if args.reverse:
            removed = remove_generated_files(targets)
        excluded = {target.path.resolve(strict=False) for target in targets}
        processed, changed = render_text_files(
            roots,
            profile.replacements,
            reverse=args.reverse,
            excluded=excluded,
        )
        if not args.reverse:
            created = create_generated_files(targets)
    except RenderError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    except OSError:
        print("error: file operation failed", file=sys.stderr)
        return 2

    if roots:
        print(
            f"processed={processed} changed={changed} "
            f"created={created} removed={removed}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
