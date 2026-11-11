"""Check scientific resources in both hatchling build artifacts.

Compare file names and *uncompressed* sizes with the checked-out source tree.
Also verify checksums of the largest and newly introduced reference tables.
No third-party dependencies are needed to run this check.
"""

from __future__ import annotations

import hashlib
import tarfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESOURCE_SUFFIXES = {".comp", ".dat", ".npz", ".state"}
IMPORTANT_RESOURCES = (
    "spekpy/data/tables/advanced/KQP.npz",
    "spekpy/data/tables/pe.dat",
    "spekpy/data/tables/nist_muen.dat",
    "spekpy/data/tables/pene_muen.dat",
)


def source_manifest() -> dict[str, int]:
    data_directory = ROOT / "spekpy" / "data"
    manifest = {
        path.relative_to(ROOT).as_posix(): path.stat().st_size
        for path in data_directory.rglob("*")
        if path.is_file() and path.suffix in RESOURCE_SUFFIXES
    }
    if not manifest or not set(IMPORTANT_RESOURCES).issubset(manifest):
        raise SystemExit("Missing expected scientific resources in source tree")
    return manifest


def check_manifest(
    label: str, actual: dict[str, int], expected: dict[str, int]
) -> None:
    missing = expected.keys() - actual.keys()
    extra = actual.keys() - expected.keys()
    differing = {
        name: (expected[name], actual[name])
        for name in expected.keys() & actual.keys()
        if expected[name] != actual[name]
    }
    if missing or extra or differing:
        raise SystemExit(
            f"{label} resource mismatch: missing={sorted(missing)}, "
            f"extra={sorted(extra)}, size_differences={differing}"
        )
    print(f"{label}: verified {len(actual)} scientific resource files")


def sha256(stream: object) -> str:
    digest = hashlib.sha256()
    while chunk := stream.read(1024 * 1024):
        digest.update(chunk)
    return digest.hexdigest()


def check_wheel(wheel: Path, expected: dict[str, int]) -> None:
    with zipfile.ZipFile(wheel) as archive:
        found = {
            item.filename: item.file_size
            for item in archive.infolist()
            if item.filename.startswith("spekpy/data/")
            and Path(item.filename).suffix in RESOURCE_SUFFIXES
        }
        check_manifest("wheel", found, expected)
        for name in IMPORTANT_RESOURCES:
            with open(ROOT / name, "rb") as original, archive.open(name) as built:
                if sha256(original) != sha256(built):
                    raise SystemExit(f"Wheel resource differs from source: {name}")


def check_sdist(sdist: Path, expected: dict[str, int]) -> None:
    with tarfile.open(sdist, "r:gz") as archive:
        members = {}
        for item in archive.getmembers():
            if not item.isfile():
                continue
            # An sdist has a single top-level package-version directory.
            parts = Path(item.name).parts
            if len(parts) < 3:
                continue
            name = Path(*parts[1:]).as_posix()
            if name.startswith("spekpy/data/") and Path(name).suffix in RESOURCE_SUFFIXES:
                members[name] = item
        check_manifest(
            "sdist", {name: item.size for name, item in members.items()}, expected
        )
        for name in IMPORTANT_RESOURCES:
            built = archive.extractfile(members[name])
            if built is None:
                raise SystemExit(f"Unable to read sdist resource: {name}")
            with open(ROOT / name, "rb") as original, built:
                if sha256(original) != sha256(built):
                    raise SystemExit(f"SDist resource differs from source: {name}")


def main() -> None:
    dist = ROOT / "dist"
    wheels = list(dist.glob("spekpy-*.whl"))
    sdists = list(dist.glob("spekpy-*.tar.gz"))
    if len(wheels) != 1 or len(sdists) != 1:
        raise SystemExit(
            f"Expected one wheel and one sdist in {dist}; "
            f"found {len(wheels)} wheels and {len(sdists)} sdists"
        )
    expected = source_manifest()
    check_wheel(wheels[0], expected)
    check_sdist(sdists[0], expected)
    for artifact in (wheels[0], sdists[0]):
        size_mib = artifact.stat().st_size / (1024 * 1024)
        print(f"{artifact.name}: {size_mib:.1f} MiB")
    print("All packaged scientific data matches the source tree.")


if __name__ == "__main__":
    main()
