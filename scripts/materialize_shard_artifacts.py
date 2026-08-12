#!/usr/bin/env python3
"""Rebuild ``shard_N`` directories from downloaded GitHub Actions artifacts.

Both the original one-artifact-per-shard layout and the split ``publish_ready``
ZIP layout are supported.  ZIPs are streamed into a staging directory and are
never extracted with ``extractall``.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import stat
import struct
import tempfile
import zipfile
import zlib
from pathlib import Path, PurePosixPath
from typing import BinaryIO


ARTIFACT_INDEX_RE = re.compile(r"-(\d+)$")
DATE_RE = re.compile(r"^\d{6}(?:\d{2})?$")
DATE_TOKEN_RE = re.compile(r"(?<!\d)(\d{6}|\d{8})(?!\d)")
SHARD_NAME_RE = re.compile(r"^shard_(\d+)$")
PUBLISH_READY_ZIP_RE = re.compile(
    r"^publish_ready_(?P<date>\d{6}(?:\d{2})?)(?:_part(?P<part>\d+))?\.zip$",
    re.IGNORECASE,
)
SOURCE_IMAGE_RE = re.compile(r"^source_image_(\d+)\.(?:png|jpe?g|webp)$", re.IGNORECASE)
SOURCE_IMAGE_PREFIX_RE = re.compile(r"^source_image_", re.IGNORECASE)
REPORT_MARKERS = (
    "wechat_article.md",
    "note.md",
    "source_mineru.md",
    "wechat_article_en.md",
    "zhihu_article.md",
    "xianyu_note.md",
    "wechat_article.txt",
    "note.txt",
    "wechat_article_en.txt",
    "zhihu_article.txt",
    "xianyu_note.txt",
)
RESTORED_MARKDOWN_NAMES = {
    "note.txt": "note.md",
    "wechat_article.txt": "wechat_article.md",
    "wechat_article_en.txt": "wechat_article_en.md",
    "zhihu_article.txt": "zhihu_article.md",
    "xianyu_note.txt": "xianyu_note.md",
}
MAX_ZIP_ENTRIES = 100_000
MAX_ZIP_MEMBER_BYTES = 1024 * 1024 * 1024
MAX_ZIP_TOTAL_BYTES = 8 * 1024 * 1024 * 1024
MAX_COMPRESSION_RATIO = 1000
MAX_ZIP_COMPRESSED_BYTES = 1024 * 1024 * 1024
LOCAL_FILE_HEADER = struct.Struct("<4s5H3I2H")
LOCAL_FILE_HEADER_SIGNATURE = b"PK\x03\x04"


def artifact_index(path: Path) -> int:
    match = ARTIFACT_INDEX_RE.search(path.name)
    if not match:
        raise RuntimeError(f"Cannot resolve shard index from artifact directory: {path.name}")
    return int(match.group(1))


def report_dirs(shard_dir: Path) -> list[Path]:
    return sorted(
        child
        for child in shard_dir.iterdir()
        if child.is_dir()
        and not child.is_symlink()
        and any((child / marker).is_file() for marker in REPORT_MARKERS)
    )


def _validate_expected_date(expected_date: str, destination: Path) -> str:
    value = expected_date.strip()
    if value and not DATE_RE.fullmatch(value):
        raise RuntimeError(f"Expected date must contain 6 or 8 digits: {value!r}")
    if value and DATE_RE.fullmatch(destination.name) and destination.name != value:
        raise RuntimeError(
            f"Destination date {destination.name!r} does not match expected date {value!r}"
        )
    return value


def _assert_tree_has_no_symlinks(root: Path) -> None:
    if root.is_symlink():
        raise RuntimeError(f"Artifact input cannot be a symlink: {root}")
    for current, directories, filenames in os.walk(root, followlinks=False):
        current_path = Path(current)
        for name in [*directories, *filenames]:
            path = current_path / name
            if path.is_symlink():
                raise RuntimeError(f"Artifact input contains a symlink: {path}")


def _publish_ready_zip_key(path: Path) -> tuple[str, int, str]:
    match = PUBLISH_READY_ZIP_RE.fullmatch(path.name)
    if not match:  # pragma: no cover - caller filters first
        return (path.name, 0, path.as_posix())
    part = int(match.group("part") or 0)
    return (match.group("date"), part, path.as_posix())


def _find_publish_ready_zips(artifact_root: Path) -> list[Path]:
    matches: list[Path] = []
    for path in artifact_root.rglob("*.zip"):
        if not PUBLISH_READY_ZIP_RE.fullmatch(path.name):
            continue
        if path.is_symlink() or not path.is_file():
            raise RuntimeError(f"Publish-ready ZIP must be a regular file: {path}")
        matches.append(path)
    matches = sorted(matches, key=_publish_ready_zip_key)
    if not matches:
        return matches

    parsed = [PUBLISH_READY_ZIP_RE.fullmatch(path.name) for path in matches]
    parts = [match.group("part") for match in parsed if match]  # type: ignore[union-attr]
    if any(part is None for part in parts):
        if len(matches) != 1 or parts != [None]:
            raise RuntimeError(
                "Publish-ready ZIP input must use either one unsplit archive or numbered parts"
            )
        return matches

    part_numbers = [int(part) for part in parts if part is not None]
    if any(part != f"{number:03d}" for part, number in zip(parts, part_numbers)):
        raise RuntimeError("Publish-ready ZIP part numbers must use three digits")
    if len(set(part_numbers)) != len(part_numbers):
        raise RuntimeError(f"Duplicate publish-ready ZIP part numbers: {part_numbers}")
    expected_parts = list(range(1, len(part_numbers) + 1))
    if sorted(part_numbers) != expected_parts:
        raise RuntimeError(
            f"Publish-ready ZIP parts must be continuous from part001: "
            f"expected {expected_parts}, found {sorted(part_numbers)}"
        )
    return matches


def _validate_shard_indices(indices: list[int], expected_shards: int) -> None:
    if len(set(indices)) != len(indices):
        raise RuntimeError(f"Duplicate shard indices: {indices}")
    if expected_shards:
        expected_indices = list(range(expected_shards))
        if indices != expected_indices:
            raise RuntimeError(
                f"Expected shard indices {expected_indices}, found {indices}"
            )


def _direct_artifact_dirs(
    artifact_root: Path,
    expected_shards: int,
    expected_date: str,
) -> list[tuple[int, Path]]:
    artifact_dirs: list[Path] = []
    for path in artifact_root.iterdir():
        if not ARTIFACT_INDEX_RE.search(path.name):
            continue
        if path.is_symlink():
            raise RuntimeError(f"Shard artifact directory cannot be a symlink: {path}")
        if path.is_dir():
            artifact_dirs.append(path)
    if not artifact_dirs:
        raise RuntimeError(f"No shard artifact directories or publish-ready ZIPs found under {artifact_root}")

    indexed = sorted(((artifact_index(path), path) for path in artifact_dirs), key=lambda row: row[0])
    indices = [index for index, _path in indexed]
    _validate_shard_indices(indices, expected_shards)
    if expected_date:
        for _index, path in indexed:
            date_tokens = DATE_TOKEN_RE.findall(path.name)
            if expected_date not in date_tokens:
                raise RuntimeError(
                    f"Shard artifact {path.name!r} does not identify expected date {expected_date}"
                )
    return indexed


def _copy_direct_artifacts(indexed: list[tuple[int, Path]], staging: Path) -> None:
    for index, artifact_dir in indexed:
        _assert_tree_has_no_symlinks(artifact_dir)
        shard_destination = staging / f"shard_{index}"
        shutil.copytree(artifact_dir, shard_destination)


def _zip_member_type(info: zipfile.ZipInfo) -> int:
    unix_mode = (info.external_attr >> 16) & 0xFFFF
    return stat.S_IFMT(unix_mode)


def _validate_local_zip_header(
    archive: zipfile.ZipFile,
    info: zipfile.ZipInfo,
) -> int:
    """Bind trusted central metadata to the producer's local file header.

    Python's ZIP readers allocate from the compressed stream before applying a
    forged central-directory ``file_size`` limit.  The package producer writes
    ordinary, seekable DEFLATE entries without data descriptors, so rejecting
    any other form closes that allocation-amplification path before extraction.
    """
    archive.fp.seek(info.header_offset)  # type: ignore[union-attr]
    raw = archive.fp.read(LOCAL_FILE_HEADER.size)  # type: ignore[union-attr]
    if len(raw) != LOCAL_FILE_HEADER.size:
        raise RuntimeError(f"Truncated ZIP local header: {info.filename!r}")
    (
        signature,
        _version,
        flags,
        compression,
        _mtime,
        _mdate,
        crc,
        compressed_size,
        file_size,
        filename_size,
        extra_size,
    ) = LOCAL_FILE_HEADER.unpack(raw)
    if signature != LOCAL_FILE_HEADER_SIGNATURE:
        raise RuntimeError(f"Invalid ZIP local header: {info.filename!r}")
    if flags & 0x08:
        raise RuntimeError(f"ZIP data descriptors are not supported: {info.filename!r}")
    if flags != info.flag_bits or compression != info.compress_type:
        raise RuntimeError(f"Conflicting ZIP member headers: {info.filename!r}")
    if (crc, compressed_size, file_size) != (info.CRC, info.compress_size, info.file_size):
        raise RuntimeError(f"Conflicting ZIP member sizes or checksum: {info.filename!r}")
    filename = archive.fp.read(filename_size)  # type: ignore[union-attr]
    archive.fp.seek(extra_size, os.SEEK_CUR)  # type: ignore[union-attr]
    try:
        decoded_name = filename.decode("utf-8" if flags & 0x800 else "cp437")
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"Invalid ZIP member encoding: {info.filename!r}") from exc
    if decoded_name != info.orig_filename:
        raise RuntimeError(f"Conflicting ZIP member names: {info.filename!r}")
    return info.header_offset + LOCAL_FILE_HEADER.size + filename_size + extra_size


def _validate_deflate_payload(
    archive: zipfile.ZipFile,
    info: zipfile.ZipInfo,
    data_offset: int,
) -> None:
    """Verify actual DEFLATE size/CRC without trusting central-directory sizes.

    ``ZipExtFile`` may let the codec expand a forged stream before truncating
    it to a false central ``file_size``.  The bounded decoder below emits at
    most one MiB at a time and stops as soon as actual output exceeds the
    declared, already-capped size.
    """
    archive.fp.seek(data_offset)  # type: ignore[union-attr]
    decoder = zlib.decompressobj(-zlib.MAX_WBITS)
    compressed_remaining = info.compress_size
    output_size = 0
    output_crc = 0
    while compressed_remaining > 0:
        chunk = archive.fp.read(min(1024 * 1024, compressed_remaining))  # type: ignore[union-attr]
        if not chunk:
            raise RuntimeError(f"Truncated ZIP compressed data: {info.filename!r}")
        compressed_remaining -= len(chunk)
        pending = chunk
        while pending:
            previous_size = len(pending)
            output_limit = min(1024 * 1024, max(1, info.file_size - output_size + 1))
            try:
                output = decoder.decompress(pending, output_limit)
            except zlib.error as exc:
                raise RuntimeError(f"Invalid ZIP DEFLATE stream: {info.filename!r}") from exc
            pending = decoder.unconsumed_tail
            output_size += len(output)
            output_crc = zlib.crc32(output, output_crc)
            if output_size > info.file_size:
                raise RuntimeError(f"ZIP member decompressed size exceeds its declaration: {info.filename!r}")
            if decoder.unused_data or (decoder.eof and (pending or compressed_remaining)):
                raise RuntimeError(f"ZIP member compressed size exceeds its stream: {info.filename!r}")
            if not output and len(pending) == previous_size:
                raise RuntimeError(f"ZIP DEFLATE stream made no progress: {info.filename!r}")
    if not decoder.eof:
        try:
            trailing = decoder.decompress(b"", 1)
        except zlib.error as exc:
            raise RuntimeError(f"Invalid ZIP DEFLATE stream: {info.filename!r}") from exc
        if trailing:
            raise RuntimeError(f"ZIP member decompressed size exceeds its declaration: {info.filename!r}")
    if not decoder.eof or output_size != info.file_size or output_crc != info.CRC:
        raise RuntimeError(f"ZIP member size or checksum does not match its payload: {info.filename!r}")


def _validate_zip_member(archive: zipfile.ZipFile, info: zipfile.ZipInfo) -> PurePosixPath:
    raw_name = info.filename
    if not raw_name or "\x00" in raw_name or "\\" in raw_name:
        raise RuntimeError(f"Unsafe ZIP member name: {raw_name!r}")
    member_path = PurePosixPath(raw_name)
    raw_parts = raw_name.rstrip("/").split("/")
    if (
        member_path.is_absolute()
        or any(part in {"", ".", ".."} for part in raw_parts)
        or ".." in member_path.parts
    ):
        raise RuntimeError(f"Unsafe ZIP member path: {raw_name!r}")
    member_type = _zip_member_type(info)
    if member_type not in {0, stat.S_IFREG, stat.S_IFDIR}:
        raise RuntimeError(f"Unsupported ZIP member type: {raw_name!r}")
    if info.flag_bits & 0x1:
        raise RuntimeError(f"Encrypted ZIP member is not supported: {raw_name!r}")
    if info.compress_type != zipfile.ZIP_DEFLATED:
        raise RuntimeError(f"Unsupported ZIP compression method: {raw_name!r}")
    data_offset = _validate_local_zip_header(archive, info)
    if info.file_size > MAX_ZIP_MEMBER_BYTES:
        raise RuntimeError(f"ZIP member is too large: {raw_name!r}")
    if (
        info.file_size > 0
        and info.compress_size > 0
        and info.file_size / info.compress_size > MAX_COMPRESSION_RATIO
    ):
        raise RuntimeError(f"ZIP member has an unsafe compression ratio: {raw_name!r}")
    _validate_deflate_payload(archive, info, data_offset)
    return member_path


def _sha256_stream(stream: BinaryIO) -> str:
    digest = hashlib.sha256()
    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
        digest.update(chunk)
    return digest.hexdigest()


def _copy_zip_member(
    archive: zipfile.ZipFile,
    info: zipfile.ZipInfo,
    target: Path,
    staging: Path,
) -> None:
    resolved_staging = staging.resolve()
    resolved_target = target.resolve(strict=False)
    if resolved_staging not in resolved_target.parents:
        raise RuntimeError(f"ZIP member target escapes staging: {info.filename!r}")
    current = target.parent
    while current != staging:
        if current.is_symlink():
            raise RuntimeError(f"ZIP member target traverses a symlink: {target}")
        current = current.parent
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.is_symlink():
        raise RuntimeError(f"ZIP member target traverses a symlink: {target}")
    with archive.open(info, "r") as source:
        if target.exists():
            if not target.is_file() or target.stat().st_size != info.file_size:
                raise RuntimeError(f"Conflicting split-ZIP member: {info.filename!r}")
            source_hash = _sha256_stream(source)
            with target.open("rb") as existing:
                target_hash = _sha256_stream(existing)
            if source_hash != target_hash:
                raise RuntimeError(f"Conflicting split-ZIP member: {info.filename!r}")
            return
        temporary: Path | None = None
        try:
            with tempfile.NamedTemporaryFile(
                prefix=f".{target.name}.",
                suffix=".materializing",
                dir=target.parent,
                delete=False,
            ) as output:
                temporary = Path(output.name)
                shutil.copyfileobj(source, output, length=1024 * 1024)
            if temporary.stat().st_size != info.file_size:
                raise RuntimeError(f"ZIP member size mismatch: {info.filename!r}")
            temporary.replace(target)
        finally:
            if temporary is not None and temporary.exists():
                temporary.unlink()


def _zip_target(
    member_path: PurePosixPath,
    *,
    archive_date: str,
    expected_date: str,
) -> tuple[Path, int]:
    parts = member_path.parts
    if len(parts) < 4:
        raise RuntimeError(
            f"Publish-ready ZIP file must use date/shard/report/file layout: {member_path}"
        )
    member_date, shard_name, report_name, *relative_parts = parts
    if not DATE_RE.fullmatch(member_date):
        raise RuntimeError(f"Invalid date directory in publish-ready ZIP: {member_path}")
    required_date = expected_date or archive_date
    if member_date != archive_date or member_date != required_date:
        raise RuntimeError(
            f"Publish-ready ZIP date {member_date!r} does not match required date {required_date!r}"
        )
    shard_match = SHARD_NAME_RE.fullmatch(shard_name)
    if not shard_match:
        raise RuntimeError(f"Invalid shard directory in publish-ready ZIP: {member_path}")
    if not report_name or report_name.startswith("."):
        raise RuntimeError(f"Invalid report directory in publish-ready ZIP: {member_path}")
    if not relative_parts:
        raise RuntimeError(f"Report file path is empty in publish-ready ZIP: {member_path}")

    if len(relative_parts) == 1:
        relative_parts[0] = RESTORED_MARKDOWN_NAMES.get(relative_parts[0], relative_parts[0])
    filename = relative_parts[-1]
    if SOURCE_IMAGE_PREFIX_RE.match(filename):
        valid_location = len(relative_parts) == 2 and relative_parts[0] == "assets"
        if not valid_location or not SOURCE_IMAGE_RE.fullmatch(filename):
            raise RuntimeError(f"Invalid source image path in publish-ready ZIP: {member_path}")
    relative = Path(shard_name, report_name, *relative_parts)
    return relative, int(shard_match.group(1))


def _extract_publish_ready_zips(
    zip_paths: list[Path],
    staging: Path,
    expected_date: str,
) -> set[int]:
    archive_dates = {
        PUBLISH_READY_ZIP_RE.fullmatch(path.name).group("date")  # type: ignore[union-attr]
        for path in zip_paths
    }
    if len(archive_dates) != 1:
        raise RuntimeError(f"Publish-ready ZIPs contain multiple dates: {sorted(archive_dates)}")
    archive_date = next(iter(archive_dates))
    if expected_date and archive_date != expected_date:
        raise RuntimeError(
            f"Publish-ready ZIP filename date {archive_date!r} does not match expected date {expected_date!r}"
        )

    total_entries = 0
    total_bytes = 0
    total_compressed_bytes = 0
    shard_indices: set[int] = set()
    for zip_path in zip_paths:
        _assert_tree_has_no_symlinks(zip_path)
        if zip_path.stat().st_size > MAX_ZIP_COMPRESSED_BYTES:
            raise RuntimeError(f"Publish-ready ZIP is too large: {zip_path.name}")
        with zipfile.ZipFile(zip_path, "r") as archive:
            for info in archive.infolist():
                member_path = _validate_zip_member(archive, info)
                total_entries += 1
                total_bytes += info.file_size
                total_compressed_bytes += info.compress_size
                if (
                    total_entries > MAX_ZIP_ENTRIES
                    or total_bytes > MAX_ZIP_TOTAL_BYTES
                    or total_compressed_bytes > MAX_ZIP_COMPRESSED_BYTES
                ):
                    raise RuntimeError("Publish-ready ZIP set exceeds safe extraction limits")
                if info.is_dir():
                    continue
                relative, shard_index = _zip_target(
                    member_path,
                    archive_date=archive_date,
                    expected_date=expected_date,
                )
                shard_indices.add(shard_index)
                _copy_zip_member(archive, info, staging / relative, staging)
        print(f"Merged publish-ready ZIP: {zip_path.name}")
    return shard_indices


def _validate_source_image(path: Path) -> None:
    if path.is_symlink() or not path.is_file() or not SOURCE_IMAGE_RE.fullmatch(path.name):
        raise RuntimeError(f"Invalid source image: {path}")
    if path.stat().st_size <= 0:
        raise RuntimeError(f"Source image is empty: {path}")
    with path.open("rb") as source:
        header = source.read(12)
    suffix = path.suffix.lower()
    signatures_match = (
        (suffix == ".png" and header.startswith(b"\x89PNG\r\n\x1a\n"))
        or (suffix in {".jpg", ".jpeg"} and header.startswith(b"\xff\xd8\xff"))
        or (suffix == ".webp" and len(header) >= 12 and header[:4] == b"RIFF" and header[8:12] == b"WEBP")
    )
    if not signatures_match:
        raise RuntimeError(f"Source image signature does not match its extension: {path}")


def _validate_materialized(
    staging: Path,
    expected_shards: int,
    expected_reports: int,
    require_images: bool,
) -> tuple[int, int, int]:
    _assert_tree_has_no_symlinks(staging)
    shard_dirs: list[tuple[int, Path]] = []
    for child in staging.iterdir():
        match = SHARD_NAME_RE.fullmatch(child.name)
        if not match or not child.is_dir() or child.is_symlink():
            raise RuntimeError(f"Unexpected materialized shard entry: {child}")
        shard_dirs.append((int(match.group(1)), child))
    shard_dirs.sort(key=lambda row: row[0])
    indices = [index for index, _path in shard_dirs]
    if not indices:
        raise RuntimeError("No shard directories were materialized")
    _validate_shard_indices(indices, expected_shards)

    total_reports = 0
    total_images = 0
    for index, shard_dir in shard_dirs:
        reports = report_dirs(shard_dir)
        child_dirs = sorted(child for child in shard_dir.iterdir() if child.is_dir())
        if len(reports) != len(child_dirs):
            missing = [child.name for child in child_dirs if child not in reports]
            raise RuntimeError(
                f"Shard {index} contains report directories without a report marker: {missing}"
            )
        if not reports:
            raise RuntimeError(f"Shard {index} contains no report directories")
        for report_dir in reports:
            assets = report_dir / "assets"
            if assets.exists() and (assets.is_symlink() or not assets.is_dir()):
                raise RuntimeError(f"Invalid report assets directory: {assets}")
            for path in report_dir.rglob("*"):
                if not SOURCE_IMAGE_PREFIX_RE.match(path.name):
                    continue
                if path.parent != assets:
                    raise RuntimeError(f"Source image is outside the report assets directory: {path}")
                _validate_source_image(path)
                total_images += 1
        total_reports += len(reports)
        print(f"Validated shard_{index}: reports={len(reports)}")

    if expected_reports and total_reports != expected_reports:
        raise RuntimeError(f"Expected {expected_reports} reports, found {total_reports}")
    if require_images and total_images == 0:
        raise RuntimeError("Materialized artifacts contain no assets/source_image_* files")
    return len(shard_dirs), total_reports, total_images


def _install_staging(staging: Path, destination: Path, temporary_root: Path) -> None:
    if destination.is_symlink():
        raise RuntimeError(f"Destination cannot be a symlink: {destination}")
    if destination.exists() and not destination.is_dir():
        raise RuntimeError(f"Destination must be a directory: {destination}")
    backup = temporary_root / "previous-destination"
    had_destination = destination.exists()
    if had_destination:
        destination.rename(backup)
    try:
        staging.rename(destination)
    except BaseException:
        if had_destination and backup.exists() and not destination.exists():
            backup.rename(destination)
        raise
    if backup.exists():
        shutil.rmtree(backup)


def materialize(
    artifact_root: Path,
    destination: Path,
    expected_shards: int = 0,
    expected_reports: int = 0,
    *,
    expected_date: str = "",
    require_images: bool = False,
) -> tuple[int, int]:
    if not artifact_root.is_dir() or artifact_root.is_symlink():
        raise RuntimeError(f"Artifact root does not exist or is unsafe: {artifact_root}")
    expected_date = _validate_expected_date(expected_date, destination)
    zip_paths = _find_publish_ready_zips(artifact_root)

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".materialize-shards-",
        dir=destination.parent,
    ) as temp_dir:
        temporary_root = Path(temp_dir)
        staging = temporary_root / "payload"
        staging.mkdir()
        if zip_paths:
            print(f"Detected split publish-ready ZIP input: parts={len(zip_paths)}")
            _extract_publish_ready_zips(zip_paths, staging, expected_date)
        else:
            indexed = _direct_artifact_dirs(
                artifact_root,
                max(0, expected_shards),
                expected_date,
            )
            _copy_direct_artifacts(indexed, staging)
            print(f"Detected direct shard artifact input: shards={len(indexed)}")

        shard_count, report_count, image_count = _validate_materialized(
            staging,
            max(0, expected_shards),
            max(0, expected_reports),
            require_images,
        )
        _install_staging(staging, destination, temporary_root)

    print(
        "Materialized shard artifacts: "
        f"shards={shard_count}, reports={report_count}, source_images={image_count}"
    )
    return shard_count, report_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-root", required=True)
    parser.add_argument("--destination", required=True)
    parser.add_argument("--expected-shards", type=int, default=0)
    parser.add_argument("--expected-reports", type=int, default=0)
    parser.add_argument("--expected-date", default="")
    parser.add_argument(
        "--require-images",
        action="store_true",
        help="fail unless at least one non-empty assets/source_image_* file is materialized",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    materialize(
        Path(args.artifact_root),
        Path(args.destination),
        max(0, args.expected_shards),
        max(0, args.expected_reports),
        expected_date=args.expected_date,
        require_images=args.require_images,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
