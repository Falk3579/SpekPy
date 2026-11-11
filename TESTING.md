# Testing SpekPy

SpekPy's existing numerical regression tests live in `tests/test_SpekPy.py`.
They compare spectra, attenuation-related metrics, and reference values against
committed JSON fixtures. Do not regenerate the reference fixtures as part of
tooling or formatting changes.

## Local baseline

From a checkout, create and activate a Python 3.11 virtual environment, then:

```sh
python -m pip install -e . pytest
python -m pytest tests -q
```

To verify that the suite does not depend on your current working directory,
run it from elsewhere after installing the package:

```sh
cd /tmp
python -m pytest /path/to/SpekPy/tests -q
```

Use the actual checkout path in the last command.

## Test isolation

Reference JSON fixture locations are derived from the test module's path.
The tests write exported spectra to pytest's `tmp_path`. An autouse fixture
in `tests/conftest.py` redirects only package-local *user-created* materials
and states to temporary directories. Bundled reference data continue to be
read from the package without modification.

## CI

`.github/workflows/tests.yml` installs SpekPy and pytest on Python 3.11,
then executes the suite from outside the checkout. This is the initial
baseline; expanding supported Python versions and adding other quality
checks belong to later modernization phases.
