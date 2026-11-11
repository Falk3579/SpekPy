# Developing and testing SpekPy

SpekPy uses [uv](https://docs.astral.sh/uv/) to manage the local development
environment and the reproducible `uv.lock` file. Distribution builds use
[hatchling](https://hatch.pypa.io/) via the standard `pyproject.toml`.
Python 3.11 is the baseline development version (see `.python-version`).

## Setup and regression tests

```sh
uv sync --locked
uv run --locked pytest tests -q
```

The 24 pytest-style regression tests in `tests/test_SpekPy.py` compare
spectra, attenuation-related metrics, and reference values against committed
JSON fixtures. **Do not regenerate the numerical reference fixtures during
packaging, tooling, or formatting changes.**

To verify that tests work outside the repository root, activate the project's
environment and run pytest on the checkout's `tests` directory from another
working directory. CI does exactly this.

## Distribution verification

```sh
uv build
uv run --locked python scripts/verify_dist.py
```

The verification script checks that **both the wheel and sdist** contain all
bundled scientific `.dat`, `.npz`, `.comp`, and `.state` resources.
It compares every resource's name and uncompressed size against the source
tree and verifies checksums for the large KQP/electron tables and the
mass-energy-absorption tables added on `MuEn_Data`.

The CI workflow installs both artifacts in fresh virtual environments. It
runs the regression suite against the installed **wheel**, and an independent
calculation smoke test against the installed **sdist**.

## Test isolation

Reference JSON fixtures resolve relative to the test module, not the current
working directory. Exported spectra go to pytest's `tmp_path`; the
`tests/conftest.py` fixture redirects only the package-local, user-created
material and state directories into pytest-managed temporary storage.
Bundled reference data remain unchanged.

## CI and upcoming tooling

`.github/workflows/tests.yml` uses SHA-pinned, current GitHub Actions
releases and an uv-managed Python 3.11 environment. The development dependency
group includes Ruff and Pyrefly for the later linting and typing phases;
those checks are not enforced by this packaging PR.

## Ruff

Run the same checks as CI:

```sh
uv run --locked ruff check .
uv run --locked ruff format --check .
```

To apply mechanical fixes locally, run `uv run --locked ruff check --fix .`
and `uv run --locked ruff format .`. Review changes before committing,
especially in the numerical model. Existing percent-style formatting is
intentionally excluded from the modernization rule `UP031` to avoid changing
established output representations.
