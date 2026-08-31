"""Build the deterministic public artifact manifest."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "cases"
OUTPUT = ROOT / "manifests" / "artifacts.json"
EXCLUDED_SUFFIXES = (
    ".aux",
    ".bbl",
    ".blg",
    ".log",
    ".out",
    ".synctex.gz",
    ".toc",
)


def digest(path: Path) -> str:
    if path.suffix.lower() != ".pdf":
        content = path.read_bytes().replace(b"\r\n", b"\n")
        return hashlib.sha256(content).hexdigest()
    result = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def main() -> None:
    paths = sorted(
        path
        for path in CASES.rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and not path.name.endswith(EXCLUDED_SUFFIXES)
    )
    payload = {
        "schema_version": 1,
        "artifacts": [
            {
                "path": path.relative_to(ROOT).as_posix(),
                "sha256": digest(path),
            }
            for path in paths
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
