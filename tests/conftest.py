"""Keep the existing integration tests from writing into the installed package."""

from pathlib import Path

import pytest

import spekpy.IO as spek_io


@pytest.fixture(autouse=True)
def isolated_spekpy_files(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Provide real reference data but private, writable user-data directories.

    SpekPy currently resolves both reference tables and user files relative to
    spekpy.IO.PATH. Repoint that root to an isolated directory for each test;
    symlink only the read-only reference data to avoid copying large tables.
    This is intentionally test-only until storage is redesigned separately.
    """
    package_root = Path(spek_io.__file__).resolve().parent
    data_root = tmp_path / "package" / "data"
    data_root.mkdir(parents=True)

    for name in ("tables", "matl_def", "state_def"):
        (data_root / name).symlink_to(package_root / "data" / name, target_is_directory=True)
    for name in ("matl_usr", "state_usr"):
        (data_root / name).mkdir()

    monkeypatch.setattr(spek_io, "PATH", str(data_root.parent))
    # Export/import tests use a relative spectrum filename.
    monkeypatch.chdir(tmp_path)
