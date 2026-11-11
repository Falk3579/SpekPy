"""Isolate SpekPy's legacy package-local user data during tests.

Production resource locations remain unchanged; only the two directories used for
user-created materials and states are redirected into pytest's temporary space.
"""

from pathlib import Path

import pytest

from spekpy import IO, SpekConstants, SpekState, SpekTools


@pytest.fixture(autouse=True)
def isolate_user_data(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    original_full_file = IO.full_file
    user_directories = {
        SpekConstants.dir_matl_usr,
        SpekConstants.dir_state_usr,
    }

    def full_file(*parts: str) -> str:
        if (
            len(parts) >= 2
            and parts[0] == SpekConstants.dir_data
            and parts[1] in user_directories
        ):
            return str(tmp_path.joinpath(*parts))
        return original_full_file(*parts)

    # These modules imported full_file directly, so patch all three names.
    for module in (IO, SpekState, SpekTools):
        monkeypatch.setattr(module, "full_file", full_file)
