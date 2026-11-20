# Numerical regression tests and CI

The tests on `MuEn_Data` provide the baseline for the modernization work.
The existing `tests/test_SpekPy.py` suite checks seven physics modes against
committed reference JSON snapshots and includes NIST/Med Phys comparisons,
filtration, spectrum export/import, materials and saved-state operations,
and all seven transmission-target materials.

**Do not regenerate or adjust reference data as part of a tooling-only change.**
When updating numerical algorithms, review changes to the reference snapshots
separately and explain the expected physical/numerical differences.

## Local development

With Python 3.12 or newer and [uv](https://docs.astral.sh/uv/) installed:

```console
uv venv
uv pip install --python .venv/bin/python -e . "pytest>=9,<10"
.venv/bin/python -m pytest -q
```

Run from any working directory using `pytest -c /path/to/pyproject.toml`
when needed. The test configuration resolves the `tests` directory from
the project root.

## Test isolation

An autouse fixture in `tests/conftest.py` points `spekpy.IO.PATH` at a
fresh temporary directory for each test. The reference data directories are
symlinks to the real, read-only package data; user materials and states are
created only under the temporary directory. The working directory is also
temporary, so exported spectrum files do not pollute the repository. The
fixture currently requires an environment with directory-symlink support;
CI runs on Linux.

## CI

GitHub Actions runs the suite on CPython 3.12, 3.13, 3.14 and 3.15 using
the latest verified stable releases of checkout, setup-python and setup-uv,
pinned by commit SHA. The initial PR intentionally keeps setuptools and
does not introduce a lockfile; the uv/Hatchling migration and locked dev
environment belong to PR 2.

A green matrix means the current numerical references remain compatible on
all four declared interpreter versions. It is not a claim of clinical
validation. Test failures must be investigated rather than skipped or
silenced through relaxed tolerances.
