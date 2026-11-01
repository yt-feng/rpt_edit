"""Keep locale HTML bodies on disk while retaining deterministic mapping order."""
from __future__ import annotations

from collections.abc import Iterable, Iterator, Mapping, MutableMapping
from pathlib import Path


class FileTextMapping(Mapping[Path, str]):
    """Read an unchanged source inventory one page at a time, without a body cache."""

    def __init__(self, paths: Iterable[Path]):
        self._paths = dict.fromkeys(paths)

    def __getitem__(self, path: Path) -> str:
        if path not in self._paths:
            raise KeyError(path)
        return path.read_text(encoding="utf-8")

    def __iter__(self) -> Iterator[Path]:
        return iter(self._paths)

    def __contains__(self, path: object) -> bool:
        return path in self._paths

    def __len__(self) -> int:
        return len(self._paths)


class StagedTextMapping(MutableMapping[Path, str]):
    """Stage transformed pages outside the release; retain only paths in memory.

    The caller owns the workspace lifetime. Original paths are mapping keys,
    never output paths, so preparing an update cannot mutate Chinese content.
    """

    def __init__(self, directory: Path):
        self.directory = directory
        self.directory.mkdir(parents=True, exist_ok=False)
        self._paths: dict[Path, Path] = {}
        self._next_file = 0

    def __getitem__(self, path: Path) -> str:
        return self._paths[path].read_text(encoding="utf-8")

    def __setitem__(self, path: Path, value: str) -> None:
        staged = self._paths.get(path)
        if staged is None:
            staged = self.directory / str(self._next_file)
            self._next_file += 1
        temporary = staged.with_suffix(".tmp")
        temporary.write_text(value, encoding="utf-8")
        temporary.replace(staged)
        self._paths[path] = staged

    def __delitem__(self, path: Path) -> None:
        self._paths[path].unlink()
        del self._paths[path]

    def __iter__(self) -> Iterator[Path]:
        return iter(self._paths)

    def __contains__(self, path: object) -> bool:
        return path in self._paths

    def __len__(self) -> int:
        return len(self._paths)
